# Er-Con Technologies — site working copy

Recovered from the ChatGPT-hosted dev site on 2026-09-22 and detached from that
platform. This folder is the full project repo, not just the published output.

## Layout

    dist/                 The site itself. This is the publish root.
    source-assets/        Originals, enhanced versions, legacy photo library (69 MB)
    .git/                 Full history — 143 commits back to 2026-09-03
    ASSET_INVENTORY.md    Where each published image came from
    CHANGELOG.md          Narrative change log
    FILE_MANIFEST.txt     File listing
    REVIEW_CHECKLIST.md   Pre-publish checks
    .openai/hosting.json  OLD platform config — delete when we pick new hosting

`dist/` is plain static HTML: 16 pages, one stylesheet, one script, no build
step and no dependencies.

## State at recovery

- The archive is 5 commits AHEAD of its old remote (`origin/main`). The remote
  is a stale mirror on the old platform; local `main` is authoritative.
- One uncommitted change: `source-assets/fcr-comparisons/enhanced/fcr-headcut-after-leveled.png`
- `dist/projects.html` exists but is not linked from any page — an orphan.
  Decide whether it comes back into the nav or gets retired.
- 32 images sit in `dist/assets/` unreferenced by any page, plus a full legacy
  photo library in `source-assets/legacy-solutions/` and two 2014 PDF brochures
  (Palisade, Pipe Supports). Worth mining for the rebrand.

## Verification performed

All 33 live-site assets and 3 independently captured HTML pages were compared
byte-for-byte against this archive. Everything matched. The archive is sound.

## PROTECTED - approved by Ron, in his words

Only verbatim statements belong in this list. An earlier version recorded
"Signal Light #08BBDE on navy" here as approved. It was not: what Ron approved
was the effect of a bright accent on navy, which he called "the blue". The
specific cyan was an inference written down as a decision, and it was then
cited back to him as a constraint for the rest of the session while he was
objecting to teal. That value is gone.

- "the first 4 i like as a whole section the blue in 'Innovation' and 'Matter'
  and 'your project'" - the dark hero compositions, as compositions.
- "that card about 'maybe your role is the one we are ready to write'" - the
  talent-invite card on Careers.
- "I don't need to be coca cola co" - no proprietary typeface. Arial.
- "I have never asked for anything teal."

The rule this establishes, which I had backwards:
dark grounds take the LOUD accent, light grounds take the QUIET one.
Both are now Er-Con Navy's own hue: Signal #0067D0 and Signal Light #4794FF.


## Palette finding: no usable second colour on light grounds

The palette is built around navy, so every accent is mid-tone. Measured against
Navy #0B2D5B on white, nothing is both clearly distinct and strongly legible:

    Navy Lift   #173F75   10.48:1   dE  8.9
    Navy Edge   #2F527F    7.97:1   dE 16.4
    Steel Blue  #2F6F8F    5.54:1   dE 31.5
    Field Slate #5F7085    5.07:1   dE 33.8
    Regrowth    #3F7A3A    5.18:1   dE 77.3

A second colour needs roughly dE 25+ to register as deliberate and 7:1+ to hold
at display size. Nothing clears both. So on light grounds, headings run in one
navy and emphasis comes from structure. On dark grounds the device works — Steel
Light #7DB3CC against white on navy — and is used throughout.

This is worth knowing for the Office templates too: the same limitation applies
to a two-tone title on a white slide.

## Type: settled for web, open for Office

**Web runs on Arial / Helvetica. Do not reintroduce a rounded face.**
Two were tried against Grandview and both were rejected as cartoonish: Barlow
(v0.24) and Source Sans 3 (v0.25-26). The failure is the same in each case —
humanist, rounded letterforms with open curves and large bowls. At display
weights the counters close up and the figures read as blobs. What the brand
wants is a neutral grotesque: closed apertures, flat terminals, no warmth.
Arial is exactly that and needs no webfont. If a webfont is ever wanted here,
audition only neutral grotesques, and judge them at 42px weight 900 on navy
and at 54px bold white on navy, which is where the previous two fell apart.

## Open decision: Office type

**The Office type pairing needs revisiting.** Grandview was chosen for PowerPoint and
Word on 2026-09-22. It descends from DIN — squared engineering and signage lettering.
On the web, the rounded-grotesque matches for it (Barlow) read as cartoonish at display
weights, so the site now runs on Source Sans 3 alone. The same loudness problem may well
show up in Office at large title sizes. Revisit before the templates go into wide use:
either soften the Grandview treatment (lighter weights, less uppercase) or reconsider the
heading face so that Office and web can converge again.

## Rebrand deltas to apply

Against the brand standards set 2026-09-22:

1. **Logo** — `dist/assets/header-logo.svg` is the old mark. Replace with the
   v3 standard logo; add the shield+E icon as favicon and app tile.
   (`header-logo.png`, `header-logo-transparent.png` and `logo.png` are older
   variants of the same legacy mark — they go too.)
2. **Color** — `dist/styles.css` predates the palette. Map to Navy #0B2D5B,
   Field Slate #5F7085, Steel Blue #2F6F8F, with the neutral ramp
   (Ink / Graphite / Fog / Haze / Frost / Mist) and the field accents.
3. **Type** — web pairing is Barlow (headings) + Source Sans 3 (body),
   fallbacks Arial Narrow / Arial.
4. **Name rule** — the footer on all 16 pages reads "Er-Con Technologies, LLC".
   Brand materials never name the entity type. Should be "Er-Con Technologies".
5. **Flush lines** — header and footer must sit at identical position and size
   on every page. Verify no drift between templates.
6. **Open item** — the letterhead and closing slide still need the website URL
   and a general email. The site uses info@er-contech.com throughout.

## Contact block as published

6715 Theall Road, Houston, TX 77066 — +1 (713) 460-4601 — info@er-contech.com
