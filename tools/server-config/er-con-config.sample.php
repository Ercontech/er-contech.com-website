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

    // Microsoft Graph (sends the form email through Microsoft 365). All four filled = on.
    // Entra -> App registrations -> new app. API permissions (APPLICATION, admin consent):
    //   Mail.Send       - sending
    //   Mail.ReadWrite  - only for submissions with large photos (draft + upload)
    // Restrict the app to the sending mailbox ONLY (Exchange application access policy or
    // RBAC for Applications), so it cannot touch any other mailbox.
    // Problems are logged to /home/cxvetl8k679h/survey-submissions/graph-errors.log and the
    // form falls back to the old route, so no request is lost.
    'graph_tenant_id'     => '',
    'graph_client_id'     => '',
    'graph_client_secret' => '',
    'graph_sender'        => '',  // the mailbox the app may send as, e.g. website@er-contech.com
];
