<?php
/*
 * Gives the contact page the public Cloudflare Turnstile site key from the private
 * settings file one level above public_html. No key there = the check stays off.
 * Only the PUBLIC site key is ever sent to the browser.
 */
header('Content-Type: application/javascript; charset=UTF-8');
header('Cache-Control: no-store');
$cfg = @include dirname(__DIR__) . '/er-con-config.php';
$key = is_array($cfg) ? (string)($cfg['turnstile_site_key'] ?? '') : '';
echo 'window.ER_TURNSTILE_SITE_KEY = ' . json_encode($key) . ";\n";
