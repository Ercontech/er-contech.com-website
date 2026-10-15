# er-contech.com website

The public website for **Er-Con Technologies**: engineered erosion mitigation and
bank stabilization for pipelines and energy, transportation, geohazards, utilities,
and commercial and private property.

This repository is private and proprietary to Er-Con Technologies. All rights reserved.

## What's here

| Folder / file | What it is |
|---|---|
| `dist/` | **The finished website.** Plain HTML, CSS and JavaScript, ready to upload to the web host. |
| `build/` | The source that generates `dist/`: page text, photo choices and the build scripts. See `build/README.md`. |
| `source-assets/` | Original photos and graphics the site was built from. |
| `tools/` | Supporting tools, such as the generator for the downloadable Site Survey PDF. |
| `CHANGELOG.md` | Every change to the site, version by version. |
| `Push Er-Con.command` | Double-click on the Mac to back up this folder to GitHub. |
| `Preview Site.command` | Double-click on the Mac to preview the site locally. |

## The site

- **Home:** industry tiles, site investigation, how we work, contact
- **Industries:** Pipelines & Energy, Transportation, Geohazards, Utilities, Commercial & Private Property. Each page has a problem table and an "In the field" gallery of before/after jobs.
- **Services, About, Safety, Careers, Contact**

## Hosting

The site is static, so any web host works. It is intended for GoDaddy cPanel hosting.
The contact form posts to `dist/send.php`, which emails submissions (with photos)
to web.inquiry@er-contech.com and keeps a copy on the server outside the public
web folder. That address must exist before launch.

To publish, upload the contents of `dist/` to the site's web root.

## Versions

Versions are listed in `CHANGELOG.md`. The launch baseline is tagged `v.Launch`.
