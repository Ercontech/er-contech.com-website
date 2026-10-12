<?php
/*
 * Er-Con site survey form handler (contact page).
 * Emails each submission, with photos attached, to $TO and keeps a copy on the
 * server so nothing is lost if an email lands in junk.
 * Hosting: GoDaddy cPanel (Linux, PHP). No outside service.
 */

$TO        = 'web.inquiry@er-contech.com';
$FROM      = 'web.inquiry@er-contech.com';      // must be an address on the er-contech.com domain
$MAX_FILES = 10;
$MAX_BYTES = 25 * 1024 * 1024;                   // 25 MB total
$ALLOWED   = ['image/jpeg', 'image/png', 'image/gif', 'image/webp', 'image/heic', 'image/heif', 'application/pdf'];

// Copies go above the public web folder when possible (e.g. /home/<user>/survey-submissions)
$SAVE_DIR  = dirname(__DIR__) . '/survey-submissions';

function done($page) { header('Location: ' . $page, true, 303); exit; }
function clean($v) { return trim(str_replace(["\r", "\0"], '', is_array($v) ? implode(', ', $v) : (string)$v)); }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') done('contact.html');
if (!empty($_POST['website'])) done('thank-you.html');            // spam trap: bots fill hidden fields

$name     = clean($_POST['name'] ?? '');
$email    = clean($_POST['email'] ?? '');
$location = clean($_POST['location'] ?? '');
$details  = clean($_POST['details'] ?? '');
if ($name === '' || $location === '' || $details === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    done('contact.html?error=missing#form');
}

// ---------------------------------------------------------------- message body
$LABELS = [
  'About you'  => ['name' => 'Name', 'company' => 'Company', 'email' => 'Email', 'phone' => 'Phone'],
  'The site'   => ['location' => 'Site location', 'industry' => 'Industry', 'details' => 'What are you seeing?'],
  'Site'       => ['water' => 'Body of water', 'county' => 'County', 'project' => 'Project name', 'lat' => 'Latitude', 'long' => 'Longitude'],
  'The erosion'=> ['erosion_type' => 'Erosion type', 'flow_depth' => 'Nominal depth of flow', 'bed' => 'Bed material', 'bank' => 'Bank material'],
  'Pipeline'   => ['pipeline' => 'Pipeline involved', 'pipe_company' => 'Pipeline company', 'line' => 'Line name / number',
                   'milepost' => 'Milepost / station', 'lines_row' => 'Pipelines in right-of-way', 'diameter' => 'Pipeline diameter(s)',
                   'exposure' => 'Length of exposure', 'span' => 'Length of free span', 'pipe_visible' => 'Pipeline visible'],
  'Access'     => ['row_cleared' => 'Right-of-way cleared', 'walk' => 'Walk to site', 'trees' => 'Tree removal needed',
                   'utilities' => 'Other pipelines/utilities in ROW', 'road_limits' => 'Road or bridge weight limits',
                   'power' => 'Overhead power lines', 'weather' => 'Weather sensitive'],
];
$body = "New site survey from er-contech.com\n" . date('Y-m-d H:i T') . "\n";
$record = ['received' => date('c'), 'ip' => $_SERVER['REMOTE_ADDR'] ?? ''];
foreach ($LABELS as $group => $fields) {
    $lines = '';
    foreach ($fields as $key => $label) {
        $v = clean($_POST[$key] ?? '');
        $d = clean($_POST[$key . '_detail'] ?? '');
        if ($d !== '') $v = trim($v . ' — ' . $d, ' —');
        if ($v === '') continue;
        $lines .= str_pad($label . ':', 34) . $v . "\n";
        $record[$key] = $v;
    }
    if ($lines !== '') $body .= "\n" . strtoupper($group) . "\n" . $lines;
}

// ---------------------------------------------------------------- photos
$files = [];
if (!empty($_FILES['photos']) && is_array($_FILES['photos']['name'])) {
    $total = 0;
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    foreach ($_FILES['photos']['name'] as $i => $orig) {
        if (count($files) >= $MAX_FILES) break;
        if ($_FILES['photos']['error'][$i] !== UPLOAD_ERR_OK) continue;
        $tmp  = $_FILES['photos']['tmp_name'][$i];
        $size = (int)$_FILES['photos']['size'][$i];
        $mime = $finfo->file($tmp);
        if (!in_array($mime, $ALLOWED, true) || $total + $size > $MAX_BYTES) continue;
        $total += $size;
        $safe = preg_replace('/[^A-Za-z0-9._-]/', '_', basename($orig));
        $files[] = ['tmp' => $tmp, 'name' => $safe, 'mime' => $mime];
    }
}
if ($files) $body .= "\nPHOTOS\n" . count($files) . " attached\n";

// ---------------------------------------------------------------- keep a copy on the server
$stamp = date('Ymd-His') . '-' . bin2hex(random_bytes(3));
$dir = $SAVE_DIR . '/' . $stamp;
if (@is_dir($SAVE_DIR) || @mkdir($SAVE_DIR, 0700, true)) {
    if (!file_exists($SAVE_DIR . '/.htaccess')) @file_put_contents($SAVE_DIR . '/.htaccess', "Require all denied\n");
    if (@mkdir($dir, 0700)) {
        @file_put_contents($dir . '/submission.txt', $body);
        @file_put_contents($dir . '/submission.json', json_encode($record, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
        foreach ($files as $f) @copy($f['tmp'], $dir . '/' . $f['name']);
    }
}

// ---------------------------------------------------------------- email
$subject = 'Site survey: ' . ($record['company'] ?? $name) . ' — ' . $location;
$subject = '=?UTF-8?B?' . base64_encode(mb_substr($subject, 0, 150)) . '?=';
$boundary = 'ercon_' . bin2hex(random_bytes(8));
$replyName = str_replace(['"', "\n"], '', $name);
$headers  = "From: Er-Con Website <$FROM>\r\n";
$headers .= "Reply-To: \"$replyName\" <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: multipart/mixed; boundary=\"$boundary\"\r\n";

$msg  = "--$boundary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n\r\n";
$msg .= str_replace("\n", "\r\n", $body) . "\r\n";
foreach ($files as $f) {
    $msg .= "--$boundary\r\nContent-Type: {$f['mime']}; name=\"{$f['name']}\"\r\n";
    $msg .= "Content-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"{$f['name']}\"\r\n\r\n";
    $msg .= chunk_split(base64_encode(file_get_contents($f['tmp']))) . "\r\n";
}
$msg .= "--$boundary--\r\n";

$sent = @mail($TO, $subject, $msg, $headers, '-f' . $FROM);
done($sent ? 'thank-you.html' : 'thank-you.html?saved=1');
