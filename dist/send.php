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

date_default_timezone_set('America/Chicago');           // Houston time in emails and file names

function done($page) { header('Location: ' . $page, true, 303); exit; }
function clean($v) { return trim(str_replace(["\r", "\0"], '', is_array($v) ? implode(', ', $v) : (string)$v)); }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') done('contact.html');
if (!empty($_POST['website'])) done('thank-you.html');            // spam trap: bots fill hidden fields

// ---------------------------------------------------------------- Cloudflare Turnstile (v1.36)
// Private settings live one level above public_html in er-con-config.php (never in GitHub).
// No secret there = check skipped. Cloudflare unreachable = let it through, marked unverified,
// because losing a real request costs more than an occasional bot.
$CFG = @include dirname(__DIR__) . '/er-con-config.php';
if (!is_array($CFG)) $CFG = [];
$verified = 'off';
if (!empty($CFG['turnstile_secret'])) {
    $token = (string)($_POST['cf-turnstile-response'] ?? '');
    if ($token === '') done('contact.html?error=verify#form');
    $ctx = stream_context_create(['http' => ['method' => 'POST', 'timeout' => 8,
        'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
        'content' => http_build_query(['secret' => $CFG['turnstile_secret'], 'response' => $token,
                                       'remoteip' => $_SERVER['REMOTE_ADDR'] ?? ''])]]);
    $res = @file_get_contents('https://challenges.cloudflare.com/turnstile/v0/siteverify', false, $ctx);
    $json = $res === false ? null : json_decode($res, true);
    if (!is_array($json))         $verified = 'unreachable';
    elseif (!empty($json['success'])) $verified = 'yes';
    else                          done('contact.html?error=verify#form');
}

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
function h($v) { return htmlspecialchars($v, ENT_QUOTES, 'UTF-8'); }
$when = date('l, F j, Y \a\t g:i A T');               // e.g. Thursday, October 29, 2026 at 6:15 PM CDT
$body = "New site survey from er-contech.com\n" . $when . "\n";
$html = '<div style="font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#1D1D1B">'
      . '<p style="margin:0 0 4px;font-size:16px;font-weight:bold;color:#0B2D5B">New site survey from er-contech.com</p>'
      . '<p style="margin:0 0 18px;color:#4A4949">' . h($when) . '</p>'
      . '<table cellpadding="0" cellspacing="0" style="border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;font-size:14px">';
$record = ['received' => date('c'), 'ip' => $_SERVER['REMOTE_ADDR'] ?? '', 'human_check' => $verified];
foreach ($LABELS as $group => $fields) {
    $lines = ''; $rows = '';
    foreach ($fields as $key => $label) {
        $v = clean($_POST[$key] ?? '');
        $d = clean($_POST[$key . '_detail'] ?? '');
        if ($d !== '') $v = trim($v . ' — ' . $d, ' —');
        if ($v === '') continue;
        $lines .= $label . ': ' . $v . "\n";
        $rows  .= '<tr><td style="padding:4px 24px 4px 0;color:#4A4949;vertical-align:top;white-space:nowrap">' . h($label)
                . '</td><td style="padding:4px 0;vertical-align:top">' . nl2br(h($v)) . '</td></tr>';
        $record[$key] = $v;
    }
    if ($lines !== '') {
        $body .= "\n" . strtoupper($group) . "\n" . $lines;
        $html .= '<tr><td colspan="2" style="padding:18px 0 6px;border-bottom:2px solid #0B2D5B;font-size:12px;font-weight:bold;letter-spacing:1px;color:#0B2D5B">'
               . h(strtoupper($group)) . '</td></tr>' . $rows;
    }
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
if ($files) {
    $body .= "\nPHOTOS\n" . count($files) . " attached\n";
    $html .= '<tr><td colspan="2" style="padding:18px 0 6px;border-bottom:2px solid #0B2D5B;font-size:12px;font-weight:bold;letter-spacing:1px;color:#0B2D5B">PHOTOS</td></tr>'
           . '<tr><td colspan="2" style="padding:4px 0">' . count($files) . ' attached</td></tr>';
}
$html .= '</table></div>';

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
$subject = ($verified === 'unreachable' ? '[unverified] ' : '') . 'Site survey: ' . ($record['company'] ?? $name) . ' — ' . $location;
$subject = '=?UTF-8?B?' . base64_encode(mb_substr($subject, 0, 150)) . '?=';
$boundary = 'ercon_' . bin2hex(random_bytes(8));
$replyName = str_replace(['"', "\n"], '', $name);
$headers  = "From: Er-Con Website <$FROM>\r\n";
$headers .= "Reply-To: \"$replyName\" <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: multipart/mixed; boundary=\"$boundary\"\r\n";

$alt  = 'ercon_alt_' . bin2hex(random_bytes(8));
$msg  = "--$boundary\r\nContent-Type: multipart/alternative; boundary=\"$alt\"\r\n\r\n";
$msg .= "--$alt\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n";
$msg .= chunk_split(base64_encode($body)) . "\r\n";
$msg .= "--$alt\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n";
$msg .= chunk_split(base64_encode('<!doctype html><html><body>' . $html . '</body></html>')) . "\r\n";
$msg .= "--$alt--\r\n";
foreach ($files as $f) {
    $msg .= "--$boundary\r\nContent-Type: {$f['mime']}; name=\"{$f['name']}\"\r\n";
    $msg .= "Content-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"{$f['name']}\"\r\n\r\n";
    $msg .= chunk_split(base64_encode(file_get_contents($f['tmp']))) . "\r\n";
}
$msg .= "--$boundary--\r\n";

$sent = @mail($TO, $subject, $msg, $headers, '-f' . $FROM);
done($sent ? 'thank-you.html' : 'thank-you.html?saved=1');
