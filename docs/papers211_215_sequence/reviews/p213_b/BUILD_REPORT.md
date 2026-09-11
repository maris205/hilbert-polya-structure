# B completed source-only build and actual page inspection

2026-09-11 UTC. ACCEPT_B_BUILD_DATA_AND_VISUAL_REVIEW by
/root/p213_manuscript_review_b, subject to root original-evidence reception.
This is B's new review build, neither terminal build.

Root launched actual d5a217 under a separately consumed B_BUILD_GRANT;
the sole returned session was 9998 and the sole continuation 095b8a exited
zero. Its legacy P213_INITIAL_BUILD_SUPERVISOR_EXIT label is not mistaken
for the initial build: the actual request, physical Round1 source root,
B output directory and grant fix its identity. The full 127-line recipe
was read; only its four preparation/source/binding/output assignments differ
from the accepted earlier recipe. Nine source files alone seeded source_only.
The first product snapshot contains only the eight declared absences.

The exact launch uses env-i; PATH=/usr/bin:/bin, LANG/LC_ALL=C.UTF-8, TZ=UTC,
SOURCE_DATE_EPOCH=1789084800, FORCE_SOURCE_DATE=1, openin_any/openout_any=p,
and all five MKTEX variables zero. The fixed sequence is pdflatex/BibTeX/
pdflatex/pdflatex, without shell escape and with recorder/halting flags.
Four build steps have 600-second supervisors; diagnostics and each 150-dpi
page rendering have 180-second supervisors. All fifteen recorded supervisor
statuses are zero, all step stderr and controller streams empty. These are
supervisor statuses, not invented separately observed native child exits.
No retry, extra compilation, rendering, installation or scientific run by B.

## Complete artifact DATA reception

Actual ee7b3f exits zero: 2,836 checks, all 165 new files / 4,304,377 bytes,
complete 48,777-character JSON stdout in BUILD_DATA_NATIVE.json. Its decoded
inventory has 165 entries and its complete diagnostics list 101 entries.
The displayed tool response was visually abbreviated in places, but the
stored native output itself has no truncation marker and parses completely.

BUILD_DATA_CHECK.cjs is explicit reuse of A's accepted artifact parser,
not an independently designed build parser. Its only transformations are
B namespace, Round1, actual script hash, actual session/continuation IDs,
status and explanatory comment. DELTA_CHECK.cjs checks that exact adapter
against A source SHA256 8b4256d78033438ee1bd25817444b6f21b18d40ffa8ab66860f335462df75679.
The A scientific checker/canonical are not used by this adapter. Both
scientific-review process independence and disclosed mechanical reuse remain
intact. The accepted initial-confirmation02 artifact grammar is the baseline.

All 130 unchanged artifact files match their accepted baseline counterparts
as entire raw bytes, including complete logs/stdout/BLG/BBL/AUX/guard and
snapshot semantics. Exactly 23 records have the permitted path differences:
15 recorded requests and eight FLS copies. All twelve new manifests are
revalidated against actual new files. All 223 existing selected runtime
hashes and nine Round1 source hashes pass; each source equals its cold copy.
These are finite known dependency reads, not host discovery or an unknown
FLS-path search. Pre/post guards and source-only snapshots preserve their
accepted roles. The original initial-run01 texfonts.map prepin failure stays
historical; the unchanged accepted runtime manifest prospectively includes it.

The three actual ordered FLS streams have 246/253/253 events. Each has one
PWD, 191 selected-runtime and 50 source INPUT occurrences, three OUTPUTs
and one same-pass generated AUX input. Passes two and three each have seven
prior-generated INPUTs. There is no unknown input. The BibTeX before/after
FLS copy is not mislabeled an actual BibTeX recorder. The full BLG names
main.aux, plain.bst, references.bib, three entries and warning$--0; the BBL
contains exactly the three declared bibliography keys. No nested AUX input
or extra bibliography source is inherited from the accepted baseline.

All wrapped log/stdout warnings are received. Pass warning counts are 42/5/0;
first-pass AUX/BBL absences are cold-start state, and all reference/citation
warnings resolve by the third pass. No final missing glyph, overfull/underfull,
undefined reference/citation or fatal diagnostic remains. The sole final
match is the informational file:line:error-format announcement, not an error.
All seventeen Type1 fonts are embedded, subset and Unicode-mapped. Extracted
text has seven page terminators and no unresolved or VERIFY marker.

PDF: seven A4 pages, 225,140 bytes, SHA256
0e954f185d72d6b4c4be41cd8e5265755dd4556de8dc4eebfd20fb5b4d1431ce.
The new PDF is whole-raw equal to physical Round1. That equality establishes
unchanged content, not a substitute for the following actual B viewing.

## Every new page personally viewed

B opened all seven actual new images in qa/p213_b_build_run01/pages/
page-0001.png through page-0007.png using the image viewer after the build.

1. Anonymous title, full abstract, carrier and current equation are readable;
   the large title spacing is intentional, with no lost content.
2. Vacancy/mass distinction, minimum lemma and endpoint proof are legible;
   the final endpoint equation does not collide with the footer.
3. Three clock branches, small-mass cases, doubling formula and tie convention
   are legible; the proof continuation joins coherently to page two.
4. Four-case table, dyadic division, r=1/r=2 cases and strict y_p-1 bound
   are distinct and readable, without ambiguous subscript rendering.
5. Complete atlas necessity/sufficiency, automatic mass and arithmetic-cost
   caveat are visible; the next section's opening fits normally.
6. Fixed-target short-gap exclusion, product, upper/lower bounds and packing
   proof are readable, including the final lower-bound construction.
7. The q=0-inclusive example, finite-evidence limits and all three references
   are legible; no hidden author information or unresolved placeholder.

No visible clipping, overlap, missing glyph or layout defect found.
BUILD_INPUT_PINS.sha256 includes the actual page and PDF pins. Ordinary
trusted TeX/tool/bootstrap/path traversal remains explicit; selected hashes
are not a full syscall or loaded-memory attestation. The paper-compile skill
supplied diagnostics/fonts/page requirements; project scope excluded generic
cleanup, repair/retry and venue/submission defaults. HOLD_EXTERNAL.
