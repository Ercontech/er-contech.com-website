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
$subjectPlain = mb_substr(($verified === 'unreachable' ? '[unverified] ' : '') . 'Site survey: ' . ($record['company'] ?? $name) . ' — ' . $location, 0, 150);
$htmlDoc = '<!doctype html><html><body>' . $html . '</body></html>';

// ---------------------------------------------------------------- 1. Microsoft Graph (v1.37)
// Used when all four graph_* values are in er-con-config.php; otherwise skipped.
// Mail then genuinely comes from Microsoft 365, so SPF/INKY see a real internal sender.
if (graph_ready($CFG)) {
    $gerr = '';
    $ok = graph_send($CFG, $TO, $subjectPlain, $htmlDoc, $email, $name, $files, $gerr);
    graph_log($SAVE_DIR, $gerr);                       // problems (even recovered ones) go to graph-errors.log
    if ($ok) done('thank-you.html');                   // otherwise fall through to the old route; the copy is saved either way
}

// ---------------------------------------------------------------- 2. server mail() (the original route)
$subject = '=?UTF-8?B?' . base64_encode($subjectPlain) . '?=';
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
$msg .= chunk_split(base64_encode($htmlDoc)) . "\r\n";
$msg .= "--$alt--\r\n";
foreach ($files as $f) {
    $msg .= "--$boundary\r\nContent-Type: {$f['mime']}; name=\"{$f['name']}\"\r\n";
    $msg .= "Content-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"{$f['name']}\"\r\n\r\n";
    $msg .= chunk_split(base64_encode(file_get_contents($f['tmp']))) . "\r\n";
}
$msg .= "--$boundary--\r\n";

$sent = @mail($TO, $subject, $msg, $headers, '-f' . $FROM);
done($sent ? 'thank-you.html' : 'thank-you.html?saved=1');

// ================================================================ Microsoft Graph helpers (v1.37)
// Needs, in Entra: an app with APPLICATION permissions Mail.Send (and Mail.ReadWrite for
// submissions with large photos), both restricted to the one sending mailbox.
// Small submissions: one sendMail call (Graph limit ~4 MB per request).
// Larger: create a draft, add photos (>3 MB ones via an upload session), then send.
// If the large route is refused (e.g. no Mail.ReadWrite), the email still goes out without
// the photos and says so; the photos are always in the saved copy on the server.

function graph_ready($c) {
    foreach (['graph_tenant_id', 'graph_client_id', 'graph_client_secret', 'graph_sender'] as $k)
        if (empty($c[$k])) return false;
    return true;
}

function graph_http($method, $url, $headers, $body, &$status) {
    $status = 0;
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [CURLOPT_CUSTOMREQUEST => $method, CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers, CURLOPT_TIMEOUT => 30, CURLOPT_CONNECTTIMEOUT => 10]);
        if ($body !== null) curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
        $out = curl_exec($ch);
        $status = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        return $out === false ? '' : $out;
    }
    $ctx = stream_context_create(['http' => ['method' => $method, 'header' => implode("\r\n", $headers),
        'content' => $body ?? '', 'timeout' => 30, 'ignore_errors' => true]]);
    $out = @file_get_contents($url, false, $ctx);
    if (isset($http_response_header[0]) && preg_match('#\s(\d{3})\s#', $http_response_header[0], $m)) $status = (int)$m[1];
    return $out === false ? '' : $out;
}

function graph_token($c, &$err) {
    $login = rtrim($c['graph_login_base'] ?? 'https://login.microsoftonline.com', '/');
    $out = graph_http('POST', $login . '/' . rawurlencode($c['graph_tenant_id']) . '/oauth2/v2.0/token',
        ['Content-Type: application/x-www-form-urlencoded'],
        http_build_query(['client_id' => $c['graph_client_id'], 'client_secret' => $c['graph_client_secret'],
                          'scope' => 'https://graph.microsoft.com/.default', 'grant_type' => 'client_credentials']), $st);
    $j = json_decode($out, true);
    if ($st === 200 && !empty($j['access_token'])) return $j['access_token'];
    $err = "token: HTTP $st " . ($j['error'] ?? '') . ' ' . substr($j['error_description'] ?? $out, 0, 300);
    return '';
}

function graph_send($c, $to, $subject, $htmlDoc, $replyEmail, $replyName, $files, &$err) {
    $tok = graph_token($c, $err);
    if ($tok === '') return false;
    $api  = rtrim($c['graph_api_base'] ?? 'https://graph.microsoft.com/v1.0', '/');
    $user = $api . '/users/' . rawurlencode($c['graph_sender']);
    $auth = ['Authorization: Bearer ' . $tok, 'Content-Type: application/json'];
    $msg = ['subject' => $subject,
            'body' => ['contentType' => 'HTML', 'content' => $htmlDoc],
            'toRecipients' => [['emailAddress' => ['address' => $to]]],
            'replyTo' => [['emailAddress' => ['address' => $replyEmail, 'name' => $replyName]]]];
    $total = 0;
    foreach ($files as $f) $total += filesize($f['tmp']);

    // small: everything in one sendMail call
    if ($total <= 2800000) {
        $msg['attachments'] = [];
        foreach ($files as $f) $msg['attachments'][] = ['@odata.type' => '#microsoft.graph.fileAttachment',
            'name' => $f['name'], 'contentType' => $f['mime'], 'contentBytes' => base64_encode(file_get_contents($f['tmp']))];
        $out = graph_http('POST', $user . '/sendMail', $auth,
            json_encode(['message' => $msg, 'saveToSentItems' => false], JSON_UNESCAPED_UNICODE), $st);
        if ($st === 202) return true;
        $err = "sendMail: HTTP $st " . substr($out, 0, 300);
        return false;
    }

    // large: draft -> attachments -> send
    $out = graph_http('POST', $user . '/messages', $auth, json_encode($msg, JSON_UNESCAPED_UNICODE), $st);
    $draft = json_decode($out, true);
    if ($st !== 201 || empty($draft['id'])) {
        $err = "draft: HTTP $st " . substr($out, 0, 300) . ' | sent without photos';
        $note = '<p style="font-family:Arial,sans-serif;color:#B0301E"><b>' . count($files)
              . ' photo(s) were too large to attach automatically. They are saved with this submission on the web server.</b></p>';
        $msg['body']['content'] = str_replace('<body>', '<body>' . $note, $htmlDoc);
        $out = graph_http('POST', $user . '/sendMail', $auth,
            json_encode(['message' => $msg, 'saveToSentItems' => false], JSON_UNESCAPED_UNICODE), $st2);
        if ($st2 === 202) return true;                 // sent; $err still explains the missing photos
        $err .= " | fallback sendMail: HTTP $st2 " . substr($out, 0, 200);
        return false;
    }
    $mid = $user . '/messages/' . rawurlencode($draft['id']);
    foreach ($files as $f) {
        $size = filesize($f['tmp']);
        if ($size < 3000000) {
            $out = graph_http('POST', $mid . '/attachments', $auth, json_encode(['@odata.type' => '#microsoft.graph.fileAttachment',
                'name' => $f['name'], 'contentType' => $f['mime'], 'contentBytes' => base64_encode(file_get_contents($f['tmp']))]), $st);
            if ($st !== 201) { $err = "attach {$f['name']}: HTTP $st " . substr($out, 0, 200); return false; }
            continue;
        }
        $out = graph_http('POST', $mid . '/attachments/createUploadSession', $auth, json_encode(['AttachmentItem' =>
            ['attachmentType' => 'file', 'name' => $f['name'], 'size' => $size, 'contentType' => $f['mime']]]), $st);
        $sess = json_decode($out, true);
        if ($st !== 201 || empty($sess['uploadUrl'])) { $err = "upload session {$f['name']}: HTTP $st " . substr($out, 0, 200); return false; }
        $fh = fopen($f['tmp'], 'rb'); $pos = 0; $chunk = 3276800;        // 10 x 320 KiB, as Graph requires
        while ($pos < $size) {
            $data = fread($fh, $chunk); $len = strlen($data);
            graph_http('PUT', $sess['uploadUrl'], ['Content-Length: ' . $len,
                'Content-Range: bytes ' . $pos . '-' . ($pos + $len - 1) . '/' . $size], $data, $st);
            if ($st !== 200 && $st !== 201) { fclose($fh); $err = "upload {$f['name']} at $pos: HTTP $st"; return false; }
            $pos += $len;
        }
        fclose($fh);
    }
    $out = graph_http('POST', $mid . '/send', ['Authorization: Bearer ' . $tok, 'Content-Length: 0'], '', $st);
    if ($st === 202) return true;
    $err = "send draft: HTTP $st " . substr($out, 0, 300);
    return false;
}

function graph_log($dir, $e) {
    if ($e === '' || !@is_dir($dir)) return;
    @file_put_contents($dir . '/graph-errors.log', date('c') . '  ' . $e . "\n", FILE_APPEND);
}
