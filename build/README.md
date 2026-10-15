# Website build source

This folder holds the source that generates the site in `../dist/`.
`dist/` is the finished website; this folder is how it was made.

- `dist-orig/`: the original pages and assets the build starts from
- `content.py`: page text, industries, services, gallery jobs and photo choices
- `build.py`: builds `dist/` from `dist-orig/` and `content.py`
- `add.css`: styles added on top of the original stylesheet
- `copypass.py`: approved site-wide wording changes applied after the build
- `survey_form.py`: the contact page's site survey form
- `newassets/`: photos and files added since the original site
- `newassets_root/`: files served from the site root (`send.php`)

To rebuild: copy `dist-orig/` to `dist/`, then run `python3 build.py`.
The scripts use absolute paths under `/home/claude/site`; change those to wherever
this folder lives before running them.
