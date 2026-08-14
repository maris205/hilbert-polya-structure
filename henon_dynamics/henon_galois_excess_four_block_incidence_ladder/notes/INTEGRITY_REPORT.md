# Final integrity report

Date: 2026-08-14

Mode: final verification after two hostile-review rounds

Verdict: **PASS**

## Artifact and reproducibility gates

- required `README.md`, `paper/`, `code/`, `experiments/`, `results/` and
  `notes/`: PASS;
- final manuscript: PASS, 8-page PDF with Liang Wang/HUST metadata;
- deterministic repeated PDF build: byte-identical PASS;
- exact producer, independent checker and 15 unit tests: PASS;
- dependency locks: 7/7; hostile mutations: 20/20 rejected;
- normal and optimized producer output: byte-identical;
- producer source SHA-256:
  `ae772ebf7cc9343cf7e3b81abd355fc4b14896ab9cd692255e5d2b402c02f706`;
- primary certificate SHA-256:
  `c992ccb40f2fa4009a47fd5542952195430c75df322daeb9dfdac3e894000d23`;
- Route-A evaluation: conservative PASS at inherited exploratory status;
- Route B: correctly refused because no Hilbert space/operator package or
  completed full Galois-weighted determinant exists.

## High-impact claim verification

| Claim | Evidence | Verdict |
|---|---|---|
| primitive H6 cycle census through period six | producer enumeration and independent DFS | VERIFIED |
| all-width incidence ladder | closed insertion proof plus independent checks for widths 3--64 | VERIFIED |
| exact `B6` orbit and trace | six radical residuals and independent matrix product | VERIFIED |
| reciprocal quartic is irreducible | exact modulo-13 linear/quadratic-factor exclusion | VERIFIED |
| exact `B6` Galois excess and isolating interval | trace conjugation and two integer square margins | VERIFIED |
| no width-at-most-four excess potential | ladder identity plus exact strict logarithmic inequality | VERIFIED |
| seven-row witness is interpolable at width five | determinant-one selected incidence minor | VERIFIED |
| one-sided Hölder necessary condition | cylinder approximation plus all-width cancellation | VERIFIED |
| unrestricted Hölder problem remains open | explicit scope firewall and missing asymptotic theorem | VERIFIED |

## Reference and citation audit

All seven bibliography entries are cited and every key resolves.  External
metadata were checked against the official
[Hénon Springer record](https://link.springer.com/article/10.1007/BF01608556),
[Bowen Springer record](https://link.springer.com/book/10.1007/BFb0081279),
[Livshits MathNet record](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=2373&wshow=paper)
and [Parry--Pollicott NUMDAM volume](https://numdam.org/issues/AST_1990__187-188__1_0/).
The P31, P54 and P55 packages are present locally; all seven inherited
artifacts used by the executable certificate are hash-locked.  Ghost
citations: 0/7.

## Data and internal-consistency audit

- every displayed exact finite value is represented in
  `results/c56_certificate.json`;
- the independent checker reconstructs the cycle census, ladder rows,
  period-six trace field, exact inequality and width-five minor without
  importing the primary producer;
- README, proof package, paper, results and evaluators use the same family
  definitions and left-minus-right convention;
- the computation is a proof certificate and implementation guard, not a
  numerical extrapolation of the infinite theorem;
- PDF metadata, fonts, text extraction and rasterized pages 1, 3, 5 and 8
  pass; no undefined references, box warnings, clipping or blank pages
  remain.

## Originality screen

Characteristic phrases for the two cycle families, common insertion row,
four-block obstruction and width-five sharpness were searched on the public
web on 2026-08-14.  No substantive close match to the P56 theorem package
was found.  This is a heuristic public-web screen, not a commercial
plagiarism-database certification.

## AI research failure modes

The protocol modes are `CLEAR` at the stated scope; detailed dispositions
are in `FAILURE_MODE_AUDIT.md`.  Hostile review forced a finite
irreducibility certificate and prevented an infinite-incidence theorem from
being promoted to an unproved Hölder no-go.  Neither repair was counted as
new arithmetic evidence.

## Claim firewall

P56 proves an exact infinite symbolic incidence ladder, computes the first
new period-six Galois excess, and excludes locally constant excess potentials
of width at most four.  Its seven-cycle witness is interpolable at width
five.  It supplies only a necessary one-sided Hölder decay condition; the
asymptotics of that discrepancy sequence remain open.  No rational-prime
correspondence, completed Galois determinant, trace formula, self-adjoint
operator, Hilbert--Pólya realization or proof of the Riemann hypothesis is
claimed.
