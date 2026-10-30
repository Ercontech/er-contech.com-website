<?php
/*
 * Er-Con website private settings.
 *
 * WHERE: save as  /home/cxvetl8k679h/er-con-config.php
 *        i.e. one level ABOVE public_html, so it can never be downloaded.
 *        File permissions 600 (owner read/write only).
 * NEVER: commit the filled-in copy to GitHub, or send the secrets by email or chat.
 *        This sample (with blanks) is the only copy that belongs in the repo.
 *
 * Leaving a value blank switches that feature off; the form keeps working.
 */
return [
    // Cloudflare Turnstile (human check on the contact form)
    // Cloudflare dashboard -> Turnstile -> Add widget. Hostnames: er-contech.com,
    // www.er-contech.com and c8w.fa8.mytemp.website. Widget mode: Managed.
    'turnstile_site_key' => '',   // public "Site Key"
    'turnstile_secret'   => '',   // private "Secret Key"

    // Microsoft Graph (sending the form email through Microsoft 365) - not wired up yet
    'graph_tenant_id'     => '',
    'graph_client_id'     => '',
    'graph_client_secret' => '',
    'graph_sender'        => '',  // the mailbox the app may send as, e.g. website@er-contech.com
];
