# Hostile review B — independent round 2

**Review date:** 2026-09-01 UTC
**Technical decision:** **ACCEPT**
**External status:** **`HOLD_EXTERNAL`**
**Severity counts:** **Critical 0 / Major 0 / Minor 1**

## Decision

The round-one revision closes every acceptance gate in `HOSTILE_REVIEW_A.md`.
I independently re-derived the quotient and every low-dimensional convention,
the disconnected labelled kernel, the global spectrum, the nearest-root
inverse, and all three limitation witnesses. I found no mathematical
counterexample and no hidden use of the component partition in
`recover_component_orders(n,Q)`. The canonical verifier cold-replays exactly,
an isolated source-only build is byte-identical to the preserved round-one PDF,
and every page of both the round-zero and round-one PDFs passes visual
inspection.

The sole minor issue is bibliographic exactness for the Chen--Li--Lin item: the
primary journal PDF writes **Cheng-Kuan Lin** and is the best direct locator,
whereas `references.bib` and `SOURCE_VERIFICATION.md` omit the hyphen and link
only the DOI/institutional record. The DOI currently lands on a database record
whose pagination conflicts with the primary PDF. The manuscript's pages
1987--1994 are nevertheless correct, so this is a non-blocking provenance
polish, not an ownership or mathematics defect.

This acceptance is only for the internal mathematical and artifact state. It
does not establish novelty, priority, authorship, owner clearance, or
permission to circulate. The package must remain **`HOLD_EXTERNAL`**.

## Severity-ranked finding

### Minor — use the direct journal locator and preserve the primary author spelling

`references.bib:57-66` and the corresponding row of
`SOURCE_VERIFICATION.md` identify the correct article, DOI, volume, issue, and
pages. The [primary Journal of Internet Technology
PDF](https://jit.ndhu.edu.tw/article/download/2185/2198), however, spells the
third author's name **Cheng-Kuan Lin** on its first page and visibly runs from
journal pages 1987 through 1994. The current DOI
`10.3966/160792642019102006027` resolves to an ERICDATA landing record that,
at review time, reports inconsistent pages 1985--1992. The independent
[NYCU institutional record](https://scholar.nycu.edu.tw/en/publications/random-walks-on-the-folded-hypercube/)
agrees with the manuscript's correct pages 1987--1994 but normalises the name
without the hyphen.

**Recommended future polish.** Preserve `Lin, Cheng-Kuan` in BibTeX and add
the journal PDF as the primary locator beside the institutional record. No
mathematical statement, owner assignment, or present decision depends on this
edit.

## Hostile mathematical re-audit

### 1. Component quotient and the boundaries \(s=1,2\): pass

For a connected component \(C\) of order \(s\), the restriction of the cut map
has

\[
 \ker(\delta|_{\mathbb F_2^C})=\langle\mathbf 1_C\rangle.
\]

Hence its push orbit is a torsor for

\[
 A_C=\mathbb F_2^C/\langle\mathbf 1_C\rangle.
\]

Choose a pivot \(*\in C\). The manuscript's map

\[
 \theta_*([a])=(a_v+a_*)_{v\ne *}
\]

is well defined because adding \(\mathbf 1_C\) flips both terms in every
coordinate. It is surjective by taking the representative \(a_*=0\), and the
same representative proves injectivity. Direct substitution gives

\[
 \theta_*([e_v])=e_v\quad(v\ne *),\qquad
 \theta_*([e_*])=\mathbf 1_{s-1}.
\]

Thus for \(s\ge3\) the \(s\) distinct labelled push generators are exactly the
coordinate generators and the all-ones generator of the stated
\(FQ_{s-1}\) Cayley presentation.

The two degenerate cases are also correct:

| component order | quotient | labelled generator images | component move |
|---:|---|---|---|
| \(s=1\) | \(\mathbb F_2^0\) | one zero image | identity loop |
| \(s=2\) | \(\mathbb F_2\) | \((1,1)\) | unnormalised \(2T_1\), normalised \(T_1\) |
| \(s\ge3\) | \(\mathbb F_2^{s-1}\) | \(e_1,\ldots,e_{s-1},\mathbf1\), all distinct | standard simple \(FQ_{s-1}\) walk |

The manuscript therefore does not confuse the labelled Markov operator with a
loop- or parallel-edge-suppressed simple adjacency matrix. The corresponding
finite control constructs these images for every \(1\le s\le12\), including
the literal tuples `(0,)` and `(1,1)`.

### 2. Disconnected labelled weighted kernel: pass

For components \(C_1,\ldots,C_c\), the state group decomposes as

\[
 A_G\cong\prod_i
 \mathbb F_2^{C_i}/\langle\mathbf1_{C_i}\rangle.
\]

The literal one-step operator is

\[
 P_G=\frac1n\sum_{v\in V}T_{[e_v]}.
\]

Grouping this labelled sum by components gives component \(i\) probability
\(s_i/n\), followed by a uniform choice among its \(s_i\) vertex labels.
Every singleton label is zero in its quotient, so \(m_1\) isolates contribute
\(m_1/n\) times the global identity. Therefore the exact kernel is

\[
 P_G=\sum_{i:s_i\ge2}\frac{s_i}{n}
 \bigl(P_{FQ_{s_i-1}}\otimes I_{\ne i}\bigr)
 +\frac{m_1}{n}I.
\]

This formula has the correct total mass and handles both difficult cases:
isolate loops remain visible, and the \(s_i=2\) weight counts two labels even
though they induce the same translation. It is a weighted random-scan tensor
sum, not an unweighted simple-graph Cartesian product.

### 3. Residual after full folded-hypercube owner subtraction: pass

The revision explicitly assigns the following zero contribution credit in the
abstract and `main.tex:73-94`:

- vertex pushing and push equivalence;
- the component identification with the folded hypercube;
- the single-component folded-hypercube spectrum and bipartiteness;
- folded-hypercube random-walk facts;
- generic finite-abelian Fourier diagonalisation, stationarity, and spectral
  moments.

It retains only narrow multi-component packaging and the known-\(n\) factor
inverse, while making no novelty or priority claim. That residual is logically
closed. In fact, the global multiplicity formula can be re-derived without
using the named single-factor spectrum: the dual of

\[
 A_G=\mathbb F_2^V/
 \operatorname{span}\{\mathbf1_{C_i}\}
\]

is the set of \(b\in\mathbb F_2^V\) having even weight on every component. For
the character \(\chi_b([a])=(-1)^{a\cdot b}\),

\[
 P_G\chi_b=\frac1n\sum_{v\in V}(-1)^{b_v}\chi_b
 =\frac{n-2|b|}{n}\chi_b.
\]

Counting such \(b\) by weight gives exactly

\[
 M_G(x)=\prod_i\sum_{j\text{ even}}\binom{s_i}{j}x^j.
\]

The return formula is then the standard character average. Parity descends to
the quotient exactly when every \(s_i\) is even, producing period two; an odd
component relation gives an odd closed walk, and an isolate gives a one-step
loop. This direct derivation is a robustness check, not a restored contribution
claim. The strongest surviving item remains the component-order inverse below.

### 4. Nearest-root recovery and shared roots: pass

For

\[
 E_s(y)=\sum_{r\ge0}\binom{s}{2r}y^r,
\]

the identity

\[
 E_s(-t^2)=(1+t^2)^{s/2}\cos(s\arctan t)
\]

gives the complete root list

\[
 -\tan^2\!\left(\frac{(2j+1)\pi}{2s}\right),
 \qquad j\ge0,\quad 2j+1<s.
\]

There are \(\lfloor s/2\rfloor=\deg E_s\) distinct roots, so all are simple and
negative. The nearest root is

\[
 \rho_s=-\tan^2\!\left(\frac{\pi}{2s}\right),
\]

and \(|\rho_s|\) strictly decreases with \(s\). If \(r<s\) and
\(E_r(\rho_s)=0\), then principal-angle injectivity forces

\[
 \frac r s=2j+1,
\]

which is impossible because the left side is below one.

Shared roots do exist and therefore had to be tested explicitly. For example,

\[
 E_2(y)=1+y,
 \qquad
 E_6(y)=1+15y+15y^2+y^3
       =(1+y)(y^2+14y+1).
\]

This does **not** break the proof. At the descending scan for \(s\), all larger
orders have already been removed. If an absent \(E_s\) divided the remaining
product of smaller factors, evaluating at \(\rho_s\) would force some smaller
factor to vanish there, contradicting the separator above. Repetition recovers
the exact multiplicity of \(s\); known \(n\) then supplies the isolates because
\(E_1=1\). No pairwise-coprimality premise is used.

The final integrality sentence also survives scrutiny, but not because the
factors are monic: \(E_s\) has leading coefficient \(s\) when \(s\) is odd.
The algorithm explicitly asks whether \(E_s\) divides the remainder **in**
\(\mathbb Z[y]\), so an accepted quotient is integral by the stated test.
Equivalently, if one first reads the test in \(\mathbb Q[y]\), constant term
one makes \(E_s\) primitive and Gauss's lemma supplies the integral quotient.
For a factor actually present in \(Q_G\), integrality is immediate from the
remaining product of integer-coefficient \(E_r\)'s. Thus main.tex:326-327 is
compressed/redundant wording, not a false closure step and not a severity
finding.

The executable audit agrees with the proof:

- `recover_component_orders(total, compressed)` has only those two arguments;
- inside the routine, factor choices depend only on `total`, the current
  `remainder`, and exact `even_factor(size)` divisibility;
- the only globals touched are write-only coverage counters;
- non-integral rational quotients are rejected explicitly;
- the ground-truth `part` occurs in the caller to construct a test input and
  only after return as the expected answer; it is never available to the
  routine's factor-selection logic.

All 28,628 integer partitions of every fixed total through 30 recover exactly,
covering 624,834 candidate divisions and 144,024 successful peels.

### 5. Boundary witnesses: pass

**\(P_4/K_4\).** The revised verifier constructs the three-edge path and the
six-edge complete graph as different literal edge sets. It derives both cut
generator systems, both eight-state labelled Markov matrices, and both exact
characteristic polynomials. Independent evaluation gives, for each,

\[
 \det(zI-P)=z^8-z^6=z^6(z-1)(z+1).
\]

Thus equal spectra are no longer obtained by calling the component formula
twice; the internal-adjacency counterexample is real.

**Starting orientation.** Every orbit is a coset
\(h+\operatorname{im}\delta\) in \(\mathbb F_2^E\). For a translation
\(S_h(x)=x+h\) and every labelled push translation \(T_g\),

\[
 S_hT_g=T_gS_h.
\]

Translation therefore conjugates the labelled kernels on any two affine
cosets, while an internal translation changes the marked state. The revised
wording correctly treats starting orientation as information absent from an
unmarked kernel, not as a substantive spectral reconstruction target.

**Unknown \(n\).** An edgeless graph of every positive order has one orientation
state and every labelled push is the identity. Orders \(1,2,\ldots\) therefore
all have the same spectrum \(\{1\}\) but different component-order multisets.
The verifier constructs orders 1 through 6 and obtains characteristic
polynomial \(z-1\) each time. This is a sharp genuine witness that the theorem
requires supplied \(n\).

## Primary-source and owner-locator audit

The six cited records all exist, their main metadata are supported, and every
entry is actually cited in the settled `.aux`/`.bbl` files.

| Source | Independent primary/official check | Role verdict |
|---|---|---|
| Klostermeyer (1999), 51:65--75 | [publisher article record](https://combinatorialpress.com/ars-articles/volume-051-ars-articles/pushing-vertices-and-orienting-edges/) and publisher PDF state the incident-edge reversal operation | correct zero-credit push source |
| Pretzel (1991), 161--186 | [Cambridge chapter record](https://www.cambridge.org/core/books/abs/surveys-in-combinatorics-1991/orientations-and-edge-functions-on-graphs/32F2109C1CDE8948D1C07405EC3F9F4E) confirms author, editor, pages, year, and DOI `10.1017/CBO9780511666216.007` | correct zero-credit orientation framework |
| Terras (1999) | [Cambridge book record](https://www.cambridge.org/core/books/fourier-analysis-on-finite-groups-and-applications/8662B523E28C44A6F245AB50A2B06EBD) confirms author, series 43, print year, ISBN, and DOI | correct generic Fourier source |
| Xu--Meng (2009), 92:3--9 | [publisher record](https://combinatorialpress.com/ars-articles/volume-092-ars-articles/on-the-folded-hypercube-and-bi-folded-hypercube/) and [primary PDF](https://combinatorialpress.com/article/ars/Volume%20092/volume-92-paper-1.pdf); journal p. 4 gives the coordinate-plus-all-ones Cayley presentation and Theorem 2.3 on journal p. 6 gives the spectrum | direct owner correctly identified and subtracted |
| Xu--Ma (2006), 19(2):140--145 | [Elsevier record](https://www.sciencedirect.com/science/article/pii/S0893965905002065) confirms authors, issue, pages, DOI, and the bipartite iff odd-dimension boundary | direct bipartiteness owner correctly subtracted |
| Chen--Li--Lin (2019), 20(6):1987--1994 | [primary journal PDF](https://jit.ndhu.edu.tw/article/download/2185/2198) and [NYCU record](https://scholar.nycu.edu.tw/en/publications/random-walks-on-the-folded-hypercube/) confirm the article and its folded-hypercube random-walk role | role and pages correct; minor locator/name polish noted above |

The bounded inverse-owner search remains only a documented non-hit. The
revision correctly refuses to treat it as novelty, priority, clearance, or
release evidence. A redundant later folded-hypercube spectrum source does not
change the subtraction because the earlier Xu--Meng direct owner already gets
zero credit. No inspected primary source was found in this bounded audit that
states the known-\(n\) component-factor inverse, but this is not a clearance
finding.

## Verifier and transcript audit

I copied only `verify_p145.py` and `verification_output.txt` to a fresh
directory and ran the verifier with an otherwise empty environment, fixed
`PATH`/`LC_ALL`, and `PYTHONDONTWRITEBYTECODE=1`. The result compared byte for
byte with the frozen transcript:

```text
P145_EXACT_CONTROL_V2
component_partitions_total_n_le_30=28628
input_only_recovery_cases=28628
recovery_division_attempts=624834
successful_input_only_factor_peels=144024
exact_assertions=155901
status=PASS
external_status=HOLD_EXTERNAL
```

The replay, copied script, and copied transcript retained the recorded hashes:

```text
8ddc8bda503147a72778fc501dc3d6aa535ce7503edd5b72df6d0d21cd81f65a  verify_p145.py
89aaeddaa2cfc8c66a1d05681e3ef3115f7b13bca665a894b1a48aa2f5df92d9  verification_output.txt
89aaeddaa2cfc8c66a1d05681e3ef3115f7b13bca665a894b1a48aa2f5df92d9  cold replay
```

Source inspection confirms only standard-library integer and `Fraction`
arithmetic, with no randomness, floating point, third-party import, network
access, timestamp, or hidden data file. The lower round-one assertion count is
honest: the old hypothesis-restating root controls were deleted rather than
relabelled as evidence.

## Isolated build and PDF audit

Only `main.tex` and `references.bib` were copied into a fresh directory. The
four-stage `pdflatex`/`bibtex`/`pdflatex`/`pdflatex` build exited zero. The
settled log has no LaTeX/package warning, undefined citation or reference,
multiply defined label, overfull/underfull box, or rerun request. The isolated
PDF is byte-identical to both `main.pdf` and `main_round1.pdf`.

| artifact | pages | visual inspection | fonts | SHA-256 |
|---|---:|---|---|---|
| `main_round0_original.pdf` | 4 A4 | every page inspected; no clipping, collision, malformed formula, broken reference, or unreadable table | 20 rows, all embedded | `abf75d832a1bd874ce31155d8c71e55e8cf3bb23f17029b82b6a88e645a49dea` |
| `main_round1.pdf` | 5 A4 | every page inspected; no clipping, collision, malformed formula, broken reference, or unreadable table; page-five whitespace is intentional | 30 rows, all embedded | `aed3fcd367940666cc2b5489f83ac1d54a72a60e6351ccd4b9d34c73117eeb14` |
| `main.pdf` | 5 A4 | byte-identical to round one | 30 rows, all embedded | `aed3fcd367940666cc2b5489f83ac1d54a72a60e6351ccd4b9d34c73117eeb14` |
| isolated round-two build | 5 A4 | byte-identical to round one | 30 rows, all embedded | `aed3fcd367940666cc2b5489f83ac1d54a72a60e6351ccd4b9d34c73117eeb14` |

Both preserved PDFs are unencrypted A4 files with blank title, author,
subject, and keyword metadata, no forms, no JavaScript, and no raster images.
The visible anonymous author line is intentional. The round-zero preservation
hash matches `HOSTILE_REVIEW_A.md` and `BUILD.md`; the revised PDF hash matches
the frozen round-one build ledger.

## Round-one acceptance-gate disposition

| Gate from `HOSTILE_REVIEW_A.md` | Round-two result |
|---|---|
| explicit folded-hypercube quotient, \(s=1,2\), and transition/adjacency conventions | **PASS** |
| exact disconnected weighted kernel and isolate loop weight | **PASS** |
| direct owners cited and all folded-hypercube inputs assigned zero credit | **PASS** |
| residual restricted to owner-thin product packaging and known-\(n\) inverse, with no novelty language | **PASS** |
| genuine public-input exact recovery control | **PASS** |
| nearest-root proof survives real shared roots | **PASS** |
| genuinely constructed \(P_4/K_4\) witness | **PASS** |
| starting orientation correctly demoted to an unmarked-category boundary | **PASS** |
| genuine unknown-\(n\) counterexample | **PASS** |
| fresh transcript, clean isolated build, and preserved round-zero PDF | **PASS** |

## Final disposition

**ACCEPT** the round-one revision as an internally correct, reproducible,
owner-subtracted theorem record, with the one non-blocking bibliographic polish
above. **Critical 0 / Major 0 / Minor 1.** Continue to make no novelty or
priority claim and keep all external circulation, posting, submission, and
specialist contact at **`HOLD_EXTERNAL`**.

Review method note: the main audit was supplemented by an independent
maximum-depth mathematical review under task
`/root/p145_round2_independent/independent_math_audit`, followed by a targeted
challenge on owner subtraction, zero-multiplicity wording, the weighted-kernel
terminology, integer divisibility, and the \(FQ_1\) convention. That secondary
review also returned `ACCEPT` and found no additional countable defect.
