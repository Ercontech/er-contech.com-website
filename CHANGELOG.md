# Er-Con Website Changelog

This log records meaningful design, content and experience checkpoints. Routine spacing corrections and minor cleanup remain available in source history but are not listed as separate versions.

## v0.65 - Site Investigation lead

The lead beside "We are water experts." (home and Services) no longer has five
disciplines "establishing" things. It now reads: "Every project starts with a
site investigation. Before we design anything, we study how water reaches the
site, what it does there, and what the ground can hold." The three clauses map
onto the five discipline cards below it.

## v0.64 - "One team, from site investigation through construction."

The services headline drops "One accountable partner, from site to installation"
and the Services page's "One team from the first site visit to the finished
installation". Home, Services and all five industry pages now read "One team,
from site investigation through construction." It reuses the name of the first
service, so the headline and the service list say the same thing.

The "Installation" service is now "Construction" (anchor `#construction`), and
the Services framework's last step is "Build: Construct the solution in the
field." "Accountable for solving it" now reads "the ones who solve it". On the
home page, the meta description and the engineering callout say construction
instead of installation. Verbs in the problem rows ("install support") are
unchanged.

The home-page heading is allowed to 960px so it sets on two lines.

## v0.63 - Services page: no product talk

The Services page's systems section ("The right system for the conditions", six
product cards) and "Additional capabilities" are removed. The hero lead now ends
"before recommending the right solution" instead of "the right system or
combination of systems". The page now runs: framework, Site Investigation, the
six services, Industry Applications, contact.

The six product pages still exist but nothing outside them links to them. Their
"Back to Services" link now goes to the top of Services, since the systems
anchor is gone.

## v0.62 - Industry pages: no product talk, two field cases

The industry pages no longer talk about products. The "Systems we use most in..."
section is removed from all five, as is the "Systems:" line under each problem
row.

"In the field" now shows two before/after cases side by side, each labelled with
the problem-table row it illustrates, word for word, with a one-line caption
under each photo. Six real before/after pairs exist; each page uses two, none
repeats on a page, and none is used more than twice across the site.

| Page | Cases |
|---|---|
| Pipelines & Energy | The line is exposed at a crossing · A free span needs support |
| Transportation | A culvert outlet is eroding · Roadside channels are cutting down |
| Municipal | Stormwater channels are eroding · Creek banks are failing near roads, parks or homes |
| Utilities | A water or sewer line is exposed at a creek crossing · Rights-of-way and access roads are washing out |
| Property | The riverbank or shoreline is moving toward buildings · Drainage through the property is cutting a gully |

"A free span has developed" is now "A free span needs support", and its row no
longer assumes erosion: a span can be designed and engineered. The row reads
"The line spans a gap, by design or because the ground beneath it has washed
away", and the solution is to engineer and install support, stabilising the site
where erosion opened the gap.

Home-page tile alt text no longer names products.

## v0.61 - Industry pages: shorter table, field evidence sooner

The problem table on each industry page is about 170px shorter: tighter cell
padding, a smaller problem title and 15px body text. The section heading sits on
one row with its lead to the right, and the heading itself is smaller.

A new "In the field" band follows the table, showing the industry's before and
after pair (the same pair as its home-page tile) side by side, with a one-line
caption under each. The first photograph after the hero now appears before
"How we solve it", about 370px higher than the systems photos did.

The industry hero is 40px shorter (610px). It stays a fixed height, so the back
link, title and industry switcher still sit at identical positions on all five
pages, checked by script.

## v0.60 - Discipline order

The five Site Investigation disciplines are reordered so that reading left to
right, Hydrology and Hydraulics are never side by side and no two "-ology" names
touch: Hydrology, Soil Mechanics, Geomorphology, Hydraulics, Sedimentology.
Hydraulics now reads "What the water does", since it no longer follows
Hydrology. The same order is used where the disciplines are named in text: the
Site Investigation service and the service band on the five industry pages.

## v0.59 - Navy hero, no photograph

The home hero and the statement strip beneath it are merged into one flat navy
block: eyebrow in Signal Light, title in white, the accent line, then the
statement. The rock-and-brick photograph is gone from the hero.

The first screen had eleven photographs competing (the hero and a before and
after in each of five tiles), all similar in texture. With the hero flat, the
industry tiles are the first imagery on the page and the before and after pairs
carry it. The tiles sit about 50px higher at desktop widths, and on phones the
white title on navy reads more clearly than navy over a washed photograph.

The separate strip, its styles and the phone-only white wash are removed.

## v0.58 - Strip wording

The statement under the hero now reads: "Protecting and preserving critical
infrastructure and assets: pipelines, roads and rail, public works, utilities,
and commercial and private property." The list names the five industries in the
order of the tiles below it, so the strip introduces the grid. It runs to two
lines at desktop widths.

## v0.57 - Statement strip under the hero

The hero lead ("Erosion looks different in every industry...") is removed. It
was hard to read over the photograph. In its place, a flat navy strip directly
beneath the hero carries one statement in white: "Erosion solutions for pipeline
exposures and other valuable infrastructure."

The hero is shorter to match (360px, down from 410px), so the industry tiles sit
about where they did. On phones the white wash behind the title now runs to the
bottom of the hero, because the title reaches further down it than before.

## v0.56 - "Industry Applications"

The industry picker's heading is now just "Industry Applications". The eyebrow
above it and the "Look familiar?" / "Choose your industry and let's get
started." pairing are gone, on the home page and on Services. The tiles move up
about 30px; at 1920 x 1080 the first row ends at 981px and the second row
starts in view.

## v0.55 - Site Investigation: we are water experts

Site Investigation is now the named foundation of every Er-Con service.

**New section, home and Services.** "Site Investigation / We are water experts."
states that every service starts with a site investigation, then sets out the
five disciplines in a ruled row: Hydrology, Hydraulics, Geomorphology,
Sedimentology and Soil Mechanics, each with one line on what it establishes. On
the home page it sits between the industry tiles and the services; on Services
it follows the framework.

**Services.** "Site Surveys" becomes "Site Investigation" (anchor
`#investigation`) and names the five disciplines. The home-page services intro
now reads "site investigation, engineering, permitting and field execution".

**Industry pages.** The service band says every project starts with a site
investigation and names the disciplines. Three problem rows now say "We
investigate" where they said survey, document or assess.

**Alignment, site-wide.** At wide screens, some text sat 24px left of the
logo's edge: the navy services band, every contact block, the Services framework,
and the inner containers on About, Careers, Contact, job pages and product
"How it works" sections. All now start on the logo's 124px edge (at 1440 wide),
checked by measuring every text line on all 20 pages. Below 1288px wide nothing
changes.

## v0.54 - Hero buttons removed

"Choose Your Industry" and "Tell Us About Your Project" are gone from the home
hero. The first only scrolled a short distance to tiles already in view, and the
second duplicated the contact card at the foot of the page and the "Not sure
where you fit?" card. The industry tiles directly below the hero are now the
page's call to action, and the first row sits 36px higher as a result.

## v0.53 - "Look familiar?"

The industry picker's heading changes from "Start with your industry / Who are
you protecting?" to "Industry applications / Look familiar?", with "Choose your
industry and let's get started." set on the heading's baseline and flush with
the grid's right edge. The same heading replaces "Industries we serve" on
Services. Narrow screens stack the line beneath the heading.

## v0.52 - Industry tiles in two rows of three

The five industry tiles now sit in a 3 x 2 grid, so each tile and its before
and after photographs are larger. The sixth position is a navy "Not sure where
you fit?" card that leads to Contact, for the visitor who does not see their
industry.

Rows are equal height, and at 1920 x 1080 the hero plus the first full row fill
the screen with the second row showing below it. Scrolled to the picker, both
rows fill the screen. The hero and picker padding were tightened slightly to
get there. Utilities' description was shortened so no tile needs a third line.
Between 901 and 1100px wide, where two names wrap, the names reserve two lines
so the descriptions start at the same height across a row.

## v0.51 - Before and after on the industry tiles

Each home-page industry tile now shows a before and after from the same site.
The after photograph fills the tile; the before sits inset in its bottom-left
corner, flush with the tile's edges, labelled on a navy chip. It costs no extra
height beyond a taller photo band (150px to 176px at desktop).

Pairs: Pipelines & Energy - pipeline support crossing. Transportation - roadside
channel rebuilt with FCR. Municipal & Public Agencies - creek crossing protected
with Ercoform over culverts. Utilities - headcut stabilised with stepped FCR.
Commercial & Private Property - riverbank before Palisade and five years after.

The same tiles appear on Services. The Transportation hint now names bridge
scour, embankments, culvert outlets and roadside channels, matching its photo.

## v0.50 - Industry first

The site was organised around what Er-Con sells. It is now organised around who
is visiting: a visitor finds their industry, then recognises the problem at their
site, then sees how Er-Con's services solve it. The systems are still here, as
the proof beneath the services rather than the way in.

**Navigation.** Industries · Services · About · Careers · Contact. Industries
opens a menu of the five industry pages; Home is the logo. "Solutions" is gone
from the menu.

**Home.** The hero is shorter and its lead now asks the visitor to choose an
industry. Directly below it, five industry tiles - Pipelines & Energy,
Transportation, Municipal & Public Agencies, Utilities, Commercial & Private
Property - replace the product-led "Built for critical applications" block. The
six-stage service grid follows as "How we solve it", with a link to Services.
The stats band moved below the engineering callout so it no longer runs into
the navy service section.

**Industry pages (new, five).** Same template on each: photo hero, a strip to
switch between industries, a ruled table of four problems - what you're seeing,
what's driving it, how we solve it, and the systems used - then the six
services, three relevant systems, and a contact block. The hero anchors to the
top, so the back link, eyebrow and title sit at identical positions on all five
pages, as does the switcher.

**Services.** Leads with the framework as before, then a new service section
naming the six services with anchors that the industry pages link to, then
the systems (now "The systems behind our services"), additional capabilities,
and the five industries.

**Product pages.** "Back to Solutions" is now "Back to Services" and returns to
the systems section.

**Alignment.** Systems sections now share the 124px content edge the rest of
the page uses at 1440 wide; they previously sat 24px wider.

## v0.43 - One name per colour

Four tokens were aliases left over from the rebrand - `--blue`, `--navy2`,
`--sky` and `--muted` - each defined as another token so older rules kept
working. Seventy-six uses now point at the real names and the aliases are gone.
Two names for one colour is how a stylesheet drifts: the next person changes one
and not the other.

`--slate-light` was renamed `--silver`. Its value `#ABAAA9` is Silver in the
standards, a true neutral. It is not a light version of Slate `#6A5948`, which
is a warm earth tone and unrelated - the name invited exactly the wrong
substitution.

Seven declared-but-unused colours were removed: `--white`, `--green`, `--clay`,
`--amber-deep`, `--straw`, `--hazard` and `--slate`. They are chart colours and
this site has no charts. The values live in the standards, so nothing is lost by
leaving them out, and nothing goes stale by carrying them. Signal Amber stays -
it is the one earth accent the site actually uses.

The block is now grouped and commented by role rather than being one flat line.
Sixteen tokens declared, sixteen used, none dangling.

Purely mechanical: the Ercoform and careers pages render pixel-for-pixel
identical before and after.

## v0.42 - Two defects the heavy overlay had been hiding

Opening the overlay in v0.41 exposed two problems that were always there.

Signal Light #4794FF cannot be read over a photograph. The product hero
statement line was set in it, and measured against the brightest patch behind
the text it failed on all six product pages - 1.47:1 on Ercoform, 2.08:1 at
best on FCR, against a standard of 3:1. This is structural, not a bad crop:
Signal Light is too light to separate from sunlit concrete at any overlay
setting that still lets the photograph show. The statement line is now white,
which measures 3.95:1 on the worst of the six.

The rule this establishes: Signal Light is an accent for solid grounds. On a
photograph the ground is variable and no fixed accent survives it. Signal Light
is retained on the careers hero, where it sits on flat Navy Deep, and
everywhere else the ground is solid.

The careers hero photograph met the navy panel at a hard vertical seam. The
.99 overlay had concealed it. The photograph's leading edge is now feathered so
it dissolves into the panel.

## v0.41 - The photography is allowed to show

The brand standards say a near-opaque wash "removes the one thing on the page
that is actually Er-Con's work." The site contradicted its own guide: the
product hero ran navy at .98 falling to .93 across the first half of the frame,
and the careers hero at .99 to .96. At those values the photograph was gone.

Both now open at .86 and reach .74 at the midpoint, easing to .28 and .12 at
the right edge (careers holds its Navy Lift partner at .52 and .40).

The setting was chosen against measured contrast, not taste alone. Figures are
against the brightest patch of each photograph behind the text - the worst
case, not the average:

                       headline / white    body / Haze #D8D7D6
  product hero .74          7.6:1                5.3:1
  careers hero .74          8.9:1                6.2:1

The standard is 3:1 for the headline and 4.5:1 for body text, so both clear it.
One step further open - .80 falling to .64 - put the product page's lead
paragraph at 3.7:1, below the standard, which is a real failure on a phone in
daylight. That is the floor, and .74 sits above it deliberately.

Applies to all six product pages and the careers hero.

## v0.40 - The signature stresses Results everywhere

The About hero was the last instance still stressing "Innovation." It now
stresses "Results.", matching the footer and the Careers CTA. The signature
is a progression, and the accent lands on the payoff in all three places.

On the dark ground the accent is Signal Light #4794FF; on light grounds it is
Signal #0067D0. Same word, same role, correct partner for the ground.

## v0.39 - Three more burned-in "AFTER" labels removed

The same defect fixed on the home hero in v0.26 was present on three other
images, never checked at the time:

- assets/project_pipeline.jpg   - the Contact page hero
- assets/project_channel.jpg    - a project card
- assets/project_restoration.jpg - the FCR product hero

Each carried a black rounded label with "AFTER" burned into the top-left
corner, left over from before/after deck slides. On Contact it sat directly
above the headline and was plainly visible through the navy overlay.

Repaired the same way as the hero: adjacent content mirrored over the label
with a feathered mask, preserving the full frame. No clean originals exist.

## v0.38 - Eyebrow removed from the Careers signature block

"Work with purpose" sat above "Experience. Innovation. Results." and added
nothing - the signature is the statement, and a label above it explained what
the reader could already see. The headline now opens the band.

## v0.37 - The signature is one rule everywhere

"Experience. Innovation. Results." appears in three places and was being
treated three different ways:

- the footer, on all 15 pages - accent on "Results."
- the Careers CTA - no accent at all, plain navy
- the About hero, on navy - accent on "Innovation."

The Careers CTA had simply been missed: same three words, same light ground,
same role as the footer, but no markup to hang the accent on. It now carries
the same spans and the rule was generalised to cover both light-ground
instances rather than just the footer.

The About hero is a different composition on a dark ground and still
emphasises "Innovation." - left as it is pending a decision on whether the
signature should always stress the same word.

## v0.36 - The accent joins the navy

Er-Con Navy sits at hue -77. It is a blue. The accent was a teal at hue -133,
56 degrees away, in a different colour family - which is why it never read as
belonging to the mark it sat beside.

The teal came from a brief about water. Water was what was asked for; teal was
an interpretation of it, and it drifted twice: the hue was placed two thirds of
the way toward the tropical end of the described range rather than the middle,
and the whole family was wrong to begin with. A cyan for dark grounds had also
been recorded in the working notes as approved. It never was - what had been
approved was the effect of a bright accent on navy, not that specific value,
and the inference was then cited back as a constraint.

Both accents now sit on the navy's own hue:

  Signal        #0067D0   hue -75   chroma 63   5.45:1 on white
  Signal Light  #4794FF   hue -77   chroma 61   4.51:1 on navy

Chroma 63 against the 25.5 that was called washed out, and close to the legacy
site blue (#0878DD, chroma 60) whose energy was liked from the start.

Logo SVGs and all twelve PNG exports, the site header marks, favicons and app
tile, and three rationale comment blocks regenerated against the new values.

## v0.35 - The signature line lands on Results

"Experience. Innovation. Results." ran Navy / Signal / Slate. Two problems:

- Slate was used exactly once on the whole site - that word. It read as
  arbitrary because it was arbitrary: no system behind it, no echo anywhere
  else. Its chroma is 13 against Navy at 32 and Signal at 28, so it also
  looked faded rather than chosen.
- The accent sat on "Innovation." and the payoff faded out. The line is a
  progression, and the colour was arguing against the sentence.

Now Navy / Navy / Signal. Two words set the premise in one voice and the
accent arrives on the word a client actually buys. Signal already carries 38
uses across the site, so "Results." joins a system instead of standing alone.

Red Clay was considered and rejected for the same reason Slate failed: it is
at zero uses, so it would have swapped one orphan colour for another. The
brand standards also reserve the earth accents for charts rather than page
furniture - the site's photography is already dirt, clay and water.

`--slate` now has no uses. Left declared as a documented reserve.

## v0.34 - Superseded accent values swept from live rules

Seven rules were still painting the old Steel Blue and Steel Light. They were
written as rgba() so the earlier hex sweep missed them:

- the form focus ring (`.form-field input:focus`)
- the "Completed application" figcaptions on six product pages
- the Palisade five-year figcaption
- borders on `.project-environments li`, `.framework-step` and `.dark .service-card`
- the ghost numeral on `.dark .service-card span`

The two dead tokens carrying those values are removed from `:root` entirely rather than
recoloured. They were unused, and leaving tokens that resolve to superseded
values invites someone to pick them up later.

## v0.33 - Small-size optical variant of the icon

At 16 and 32px the concrete form sat too close to navy to register and the mark
carried more tile padding than it needed. A dedicated small-size variant tightens
the crop and lifts the concrete to #D8D7D6. Master set unchanged at 180px and up.
Adds favicon-16 and references it from all 15 pages.

## v0.32 - Master logo set regenerated against the settled palette

Ten PNGs re-rendered from the updated SVGs at their original dimensions with
transparent backgrounds. Concrete grey moves to a true neutral (#8C8B8A, #ABAAA9
reverse) and the accent to Signal (#03778E, #08BBDE), resolving the dE 13.4
collision between the shield and the accent. Site favicon and apple-touch-icon
re-synced from the new app tile.

## v0.31 - The mark rejoins the system

- The lower shield represents concrete. It was Field Slate #5F7085, a blue-tinted grey at chroma 13.7, against measured concrete at 0.4 to 0.9. It is now Concrete #8C8B8A and reads as the material it depicts.
- That tint was also why the mark looked muddy. Field Slate and Steel Blue sat 2.4 lightness apart at dE 13.4 — below the threshold at which two colours read as different things — so the two non-navy elements blurred into one smudge against 80% navy.
- The dot and TECHNOLOGIES move from Steel Blue to Channel #03778E, matching the site. Leaving them at Steel Blue would have put two blues on the page at dE 10.1, which is the worst of both worlds: too close to read as a choice, too far to read as the same colour.
- The reverse mark takes the loud on-navy pair: Signal Light #08BBDE and a light neutral concrete.
- The icon carries the same concrete correction.
- The mark's proportions are unchanged: 80% navy, 16% carrying colour. The gain is separation, not saturation — three legible registers where there were two.

## v0.30 - Field palette applied (trial)

- Replaced the navy-tinted neutrals with measured concrete greys. Sampling 307,000 pixels across 40 project photographs put real concrete at a chroma of 0.4 to 0.9, against 4.8 to 11.7 for the neutrals being used. This is the largest single correction and the main reason the site read corporate rather than like the work.
- Set the accent to Channel #03778E — water between Caribbean and deep Pacific, at the most chroma that hue allows on screen. Water in the photography is quiet, so the accent is quiet by design.
- Put Signal Amber to work for the first time, on the hiring status pills and the hero accent rule. Yellow iron is the one loud thing on a job site, so it is the one loud thing here.
- Moved the footer signature's third word to Dark Earth, a measured value.
- Every foreground and background pair was checked: nothing falls below 4.5:1.
- Applied to the stylesheet only. The brand standards are unchanged pending review of how this reads in use.

## v0.29 - Two-tone headings retired on light grounds

- The "Expertise that travels. Local knowledge that matters." headline now runs in a single navy. The two-colour treatment was reading as a mistake rather than a choice.
- Reason, measured: a second colour has to pass two tests — be clearly different from navy, and stay legible. Against Navy on white, Navy Lift is 10.48:1 but only dE 8.9 apart, which is below the threshold where a difference registers as deliberate. Everything that is genuinely distinct — Steel Blue, Field Slate, Regrowth Green — lands between 5.07:1 and 5.54:1 and reads weak at display size.
- This is a property of the palette rather than bad luck. It is built around navy, so every accent is mid-tone, and no colour in it is both distinct and strong on a light ground.
- The device is kept on dark grounds, where it works: Steel Light against white on navy is a genuine, high-contrast distinction. The hero, careers, contact, about and solutions headings are unchanged.
- Emphasis on light grounds now comes from structure — the accent rule and the line break — rather than hue.

## v0.28 - Contrast and section rhythm

- Darkened the accent half of the "Expertise that travels" headline from Steel Blue to Navy Lift. Steel Blue sits at 5.06:1 on Mist against Navy's 12.46:1, so the sentence visibly faded out halfway through. Navy Lift holds at 9.58:1 and still reads as a distinct second colour.
- Established the rule that Steel Blue is an accent, not a display-text colour on light grounds. It stays on rules, eyebrows and small labels, where it passes AA comfortably.
- Moved the local-partnerships section to white. It and the closing call to action were both Mist, so the CTA had no edge above it and stopped reading as its own band. The CTA is now the only light-grey band at the foot of the page.
- Removed the hard 43% vertical seam that the old split background created across that section.

## v0.27 - Type reverted to the original Arial stack

- Removed the Source Sans 3 webfont and returned the site to Arial / Helvetica, which is what it ran on before the rebrand began.
- Reason: both faces tried against Grandview are rounded, humanist designs. At display weights their bowls close up and the figures read as blobs — friendly rather than engineered. A neutral grotesque with closed apertures and flat terminals is the correct register for the brand.
- Removes two webfont requests per page, so the site also loads faster and no longer depends on an external font host.

## v0.26 - Hero image cleanup

- Removed the black "AFTER" label burned into the top-left corner of the homepage hero photograph. It came from a before-and-after presentation slide and was visible on wide screens.
- Patched rather than cropped, by mirroring the adjacent treeline over the label, so the full frame and composition are preserved. No clean original exists; the source was AI-enhanced.

## v0.25 - Web type diverges from the Office pairing

- Dropped Barlow. Grandview descends from DIN, the squared lettering used for German engineering and signage; Barlow is a rounded grotesque, and at display weights in uppercase it read as cartoonish rather than engineered.
- Set Source Sans 3 across the whole site, with Arial as the fallback. It was already the brand body face, so the web now runs on a single face and degrades to what the site used before.
- Accepted that the website and the PowerPoint template no longer share letterforms. The logo, the palette and the flush-line discipline carry the brand across both.
- Returned the statistics figures to white. They had been mapped to Steel Light, a reverse-partner tint intended for small accents on navy, which read washed out at 42px.

## v0.24 - Brand system applied

- Replaced the legacy header mark with the v3 Er-Con logo, and added the shield-and-E icon as favicon, SVG icon and app tile. Retired the three older PNG variants of the legacy mark.
- Reserved the logo's box at its exact aspect ratio so the header no longer reflows while the page loads, keeping it identical in position and size across every page.
- Rebuilt the stylesheet's color layer on the brand palette. The palette had never been tokenized: six variables sat alongside roughly ninety hard-coded color literals. All of them now resolve to named brand tokens.
- Shifted the accent from the previous bright blue to Steel Blue, with Steel Light carrying accents on dark backgrounds. Neutrals now run on the brand ramp of Ink, Graphite, Fog, Haze, Frost and Mist.
- Set the brand type pairing: Barlow for headings and display figures, Source Sans 3 for body copy, with Arial Narrow and Arial as fallbacks.
- Removed the entity type from the site footer on every page, per the brand name rule. The legal name is reserved for contracts, legal notices and filings.
- Retired the Projects page, which was unlinked and awaiting case-study material. It remains recoverable in source history.

## v0.23 - Careers hero framing correction

- Reframed the Careers photograph as a contained right-side field image instead of a full-width cover crop.
- Reduced the apparent scale and repositioned the field professional so the person and surveying activity remain recognizable beside the headline.
- Refined the overlay to keep the left-side copy highly legible while allowing more photographic detail to remain visible on the right.

## v0.22 - Careers field-work hero

- Added a real Er-Con field-survey photograph behind the Careers hero to align its visual treatment with Contact while keeping the page focused on people doing technical field work.
- Mirrored and tightly framed the image through the page presentation so the field professional remains visible beside the headline and the embedded timestamp stays outside the displayed crop.
- Applied the established deep-blue overlay to preserve headline contrast and keep the photograph intentionally understated.

## v0.21 - Hero hierarchy refinement

- Connected the Home-page eyebrow more clearly to the primary headline with brand-blue color and tighter spacing.
- Strengthened the translucent white fill behind Discover Solutions while preserving its secondary relationship to the primary call to action.

## v0.20 - Cleaner application cards

- Removed the circular application icons from the Home-page cards after authentic project photography made them redundant.
- Tightened the card hierarchy so each application now leads directly with its title, explanation and field image.

## v0.19 - Projects held for current field proof

- Removed Projects from the primary navigation and Home while preserving the working page for future development.
- Removed the selected-project preview and project links from Home so the launch does not promise an underdeveloped gallery.
- Defined the checklist for rebuilding the section as Recent Projects from consistent field-superintendent closeout photography organized by type of work.

## v0.18 - Authentic home-page applications

- Replaced all four illustrative application-card images with real Er-Con project photography.
- Used the five-year Palisade result for River Bends, the completed support crossing for Pipeline Free Spans and the FCR roadside installation for Installed Solutions.
- Restored the legacy bridge-protection photograph for a brighter, clearer Critical Infrastructure image while preserving the project itself.

## v0.17 - Palisade schematic alignment

- Aligned the Palisade engineering schematic with the left edge of its supporting copy to match the other solution pages.

## v0.16 - Palisade schematic clarity

- Replaced the low-resolution Palisade schematic with a clearer user-supplied version sized for near-native display in the engineering frame.
- Preserved the earlier source for history while keeping technical labels and permeability values subject to expert-team confirmation.

## v0.15 - Palisade proof hierarchy

- Recast the Palisade field story as a clean Field Condition / Completed Application comparison followed by a separate full-width Five-Year Update.
- Replaced the cropped brochure illustration with the more complete user-supplied Palisade system and permeability schematic.
- Preserved the five-year result as a distinct proof point rather than presenting all three images as equal milestones.

## v0.14 - Palisade pattern and engineering pass

- Brought the Palisade field story into the shared Field Condition / Completed Application pattern while retaining the documented five-year result that is distinctive to the system.
- Added the variable-permeability schematic recovered from the 2014 Palisade brochure to the product-process section.
- Expanded the process explanation to connect synthetic panels, fabricated attachment assemblies, pipe pilings and varying permeability as one coordinated river-training system.
- Flagged the legacy schematic, component terminology and technical statements for expert-team confirmation before public launch.

## v0.13 - Engineering detail pass

- Added the recovered Ercoform standard mat detail to the product-process section, extending the engineering-drawing treatment established on the Eco-Flex page.
- Replaced the Pipeline Supports construction-detail photograph in the process section with a clean crop of the technical assembly schematic from the 2014 product brochure.
- Strengthened the Pipeline Supports story around root cause, foundation conditions, project-specific engineering and coordination with the broader erosion response.
- Flagged both legacy drawings and the brochure-derived technical language for expert-team verification before public launch.

## v0.12 - Pipeline Supports proof page

- Rebuilt the Pipeline Supports page around a Field Condition / Completed Application proof pair supplied for team confirmation.
- Replaced the legacy Solutions tile and hero imagery with the brighter completed crossing photograph.
- Added one close installation detail to the process section without interrupting the main before-and-after pattern.
- Added Pipeline Supports image and configuration checks to the review checklist.

## v0.11 - System 21 page foundation

- Rebuilt the System 21 detail page around the shared Field Condition / Completed Application proof pattern.
- Added honest project-image placeholders pending a verified System 21 before-and-after pair.
- Replaced the darker Solutions tile image with a brighter, tighter treatment of the second System 21 image from the legacy site.
- Added System 21 image and technical verification items to the review checklist.

## v0.10 - Eco-Flex page foundation

- Replaced the visually busy Eco-Flex Solutions-card photograph with a cleaner recovered field image that makes the open-cell mat and developing vegetation immediately legible.
- Rebuilt the Eco-Flex detail page around the field-proof structure and reserved a clearly labeled field-condition and completed-application pair for verified project imagery.
- Added the recovered Eco-Flex mat-detail and typical-cross-section drawing to reinforce the engineering behind the revegetated application.

## v0.9 - Ercoform field-proof template

- Rebuilt the Ercoform detail page around two field-condition and completed-application comparisons, with provisional technical framing pending expert-team verification.
- Replaced the generic Ercoform hero with a completed field application and preserved the supplied originals alongside restrained, documentary-style enhancements.
- Brightened the second Ercoform completed-application image to open the shaded installation area, recover foreground detail and improve visual clarity.
- Moved each Solutions-page action into a dedicated footer below the completed-project image.
- Restored the translucent, blurred sticky-header treatment and introduced an exact transparent-background master of the existing logo so the mark remains visually seamless while scrolling.

## v0.8 - Solution-card hierarchy

- Reordered all six Solutions-page tiles to follow a consistent border, text and completed-project image hierarchy.
- Moved the image divider below the copy so the blue card border reads cleanly and consistently instead of competing with the photographs.
- Refined the Solutions-page conversation prompt to sound more consultative and clarify that the discussion begins with the assets the customer is trying to protect.

## v0.7 - FCR field-proof template

- Rebuilt the Flexible Concrete Revetment detail page around two before-and-after project comparisons covering channel reconstruction and head-cut stabilization.
- Enhanced the supplied field photographs for cleaner exposure, stronger natural color and consistent presentation while preserving the documented sites and installed systems.
- Replaced the FCR hero and Solutions teaser with completed-project imagery.
- Strengthened the page language around reconstructing the failed geometry and engineering the protective application around actual field conditions.

## v0.6 - Number-free process treatment

- Removed decorative numbering from the Home capability cards, Solution Framework, all six solution-process sections and the Palisade field sequence.
- Retained meaningful Palisade stage labels and directional arrows while reclaiming the visual space previously reserved for numbers.

## v0.5 - Palisade product-story template

- Rebuilt the Palisade detail page around an authentic three-stage field sequence: active bank loss, engineered application and developing recovery.
- Enhanced the supplied project photographs for cleaner exposure, stronger natural color and more consistent presentation while preserving the documented site and installed system.
- Replaced the Palisade hero and Solutions teaser with the recovered-bank photograph.
- Reframed the Palisade facts and process around an engineered site-specific layout rather than a configured product.
- Preserved the supplied originals, enhanced masters and web-ready derivatives with documented source notes.
- Replaced the six Solutions-card collages with single completed-condition photographs for a cleaner and more confident overview.
- Standardized the completed-work crops and applied restrained brightness, contrast and saturation adjustments across the grid.

## v0.4 - Project and solution proof structure

- Added recovered Er-Con project imagery to all six core solution cards, shifting the Solutions page from text-only tiles to visual product teasers.
- Archived the recoverable legacy Solutions-page image set as source material for individual product pages and future project galleries.
- Replaced "selects and configures" with language that presents each solution as an engineered application of the right system.
- Split the Project Environments positioning into two sentences for faster reading.
- Removed the redundant "Selected work" eyebrow from the Projects introduction so the section opens directly with its headline.
- Strengthened the Project Environments message around protecting asset integrity and preventing further erosion and damage to the surrounding area.
- Built a dedicated Projects page that separates solution selection from proof of application in the field.
- Reframed the Home-page progression around applications, in-house capabilities and selected project proof.
- Updated Projects navigation across the site to open the dedicated page.
- Established a deliberate naming pattern: "Er-Con Technologies" for formal identification and "Er-Con" for conversational and repeated references.
- Tightened the Home-page applications language to move cleanly from creeks and rivers through stormwater systems and coastlines.
- Added landowner inclusion and representation as an explicit content-review question.
- Replaced the Home CTA's remaining services language with the established solutions positioning.

## v0.3 - Pre-projects-page checkpoint

- Broadened the Home-page applications language to include creeks, streams, rivers, bayous, lakes, ponds, stormwater systems and coastlines.
- Refined the Careers invitation around roles Er-Con may be ready to write, centered the email action and replaced the left accent rule with a dark-navy top border.
- Added a standing Careers invitation for exceptional candidates who do not see a matching open role, including a direct email introduction and resume path.
- Removed the circular 50-year badge from the Home hero while retaining the experience proof in the page content.
- Shortened Solution Framework Step 02 to "Find the Root Cause" so the four blue process steps remain visually balanced.
- Added a Home-page section explaining how Er-Con combines traveling expertise with local knowledge, resources and community participation while retaining ownership of the work.
- Added the site-stewardship message around minimizing the project footprint and leaving the site better than it was found.
- Replaced the remaining "accountable team" language on the Home page with ownership from first look through installation.
- Continue page-by-page review against `REVIEW_CHECKLIST.md`.
- Reserve `v.Base` for the first fully reviewed and approved baseline.

## v0.2 - Solutions hierarchy and visual framework

- Removed the Solutions-page hero that repeated the Home-page positioning.
- Led the page with the Er-Con Solution Framework and positioned the six core solution cards directly beneath it.
- Replaced the opening headline with "Treat the whole problem" and restored light-blue emphasis within the headline.
- Reframed the methodology around evaluating both the visible damage and its root cause, comparing available systems and reviewing the recommended approach with the customer before execution.
- Removed the redundant framework label and tightened the opening spacing so readers reach the process faster.
- Replaced the shaped Solution Review gate with a larger white rectangular decision step emphasized through scale, blue edging and elevation.
- Gave the framework steps and Home-page capability tiles stronger solid-blue surfaces, clearer borders, higher text contrast and subtle elevation against their dark-blue bands.
- Preserved additional capabilities and the project-conversation call to action after the primary solutions and framework.

## v0.1 - First recoverable working site

- Established the responsive HTML and CSS site structure without page-builder or image-baked text dependencies.
- Built Home, Solutions, About, Contact and Careers pages.
- Added individual pages for the six core erosion-control solutions.
- Added Careers detail pages for Project Manager, Field Construction Technician, Civil Designer and Regional Account Manager.
- Established site-wide navigation in the order Home, Solutions, Projects, Contact, Careers and About.
- Added the Er-Con origin story and leadership team with illustrated portrait placeholders.
- Added project selection behavior to the Home-page project gallery.
- Established proof points around more than 50 years, 3,000+ projects completed around the world and 35+ U.S. states served.
- Added the first Er-Con Solution Framework and customer review decision gate.
- Removed unsupported precast-mat positioning and kept Er-Con and Armorform in distinct brand swimlanes.
- Standardized visible copy without em dashes or unnecessary accent marks.

## Versioning convention

- `v0.x` identifies meaningful working checkpoints before the first approved baseline.
- `v.Base` will identify the first complete site approved for detailed finalization and launch preparation.
- Published Site versions and source history preserve exact restoration points between these named checkpoints.
