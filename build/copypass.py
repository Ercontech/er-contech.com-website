# v0.68/v0.69 - site-wide copy pass. Never touch job descriptions (Ron, 2026-10-05). (Ron, 2026-10-05). Applied to every built page after build.py.
# Each rule must match at least once somewhere, or the build fails.
import re, glob, os
D = '/home/claude/site/dist'
CONTACT = "We'll tell you how we'd approach it."
RULES = [
  # contact line (Ron: home card, home CTA, industry CTAs, contact page). NOT the Services CTA.
  # (the home "Not sure" card rule was retired in v0.71: the card became a one-line link)
  ("any photos, surveys or history you have. We'll help determine the right path forward.",
   "any photos, surveys or history you have. " + CONTACT),
  ("which assets need protection. We’ll help determine the right path forward.",
   "which assets need protection. " + CONTACT),
  # Engineering & Drawings: findings -> engineered design -> drawings
  ("Er-Con engineers translate field conditions into practical, site-specific engineering and construction documents. Each drawing accounts for constructability and long-term performance.",
   "Our engineers turn the investigation findings into an engineered design for the site, set out in construction drawings built for the field and made to last."),
  # Construction
  ("In the field, Operations coordinates local vendors and suppliers while managing safety, quality and changing site conditions. When challenges arise, crews make informed field adjustments without compromising the intent of the design.",
   "Our own crews build it, managing safety and quality on site. If conditions on the ground turn out to be different from the drawings, the crew and our engineers work it out together."),
  # home contact block
  ("<p>Er-Con solutions are proven to protect critical assets in demanding environments.</p>",
   "<p>Send us the location, what you're seeing and any photos you have. " + CONTACT + "</p>"),
  # utilities rows
  ("We establish what is driving the movement,", "We find what is driving the movement,"),
  ("with a system suited to the water level range and the facility's operation.", "with protection designed for the range of water levels and how the facility operates."),
  # industry-page buttons
  (">Discuss Your Site<", ">Start a Conversation<"),
  # About: leadership name (v1.26, Ron) - since v1.32 the leadership grid is written by build.py step 5e
  # Careers: "Now hiring" badges removed (v1.30, Ron) - every posted job is open
  ('<span class="opening-status">Now hiring</span>', ''),
]
hits = [0]*len(RULES)
for f in glob.glob(os.path.join(D, '*.html')):
    s = open(f, encoding='utf-8').read(); o = s
    for n, (a, b) in enumerate(RULES):
        if isinstance(a, str):
            c = s.count(a); s = s.replace(a, b)
        else:
            s, c = a.subn(b, s)
        hits[n] += c
    if s != o: open(f, 'w', encoding='utf-8').write(s)
missing = [RULES[n][0] if isinstance(RULES[n][0], str) else RULES[n][0].pattern for n, h in enumerate(hits) if h == 0]
# rule 1 vs 1b: only one apostrophe style needs to exist per site, but both do here
assert not missing, missing
print('copy pass:', hits)
