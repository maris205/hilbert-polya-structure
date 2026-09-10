# C432 — actual manuscript review, pass 2

Current-team nonauthor internal review, 2026-09-09 UTC.
The coordinator authorized this second assessment after accepting the
first manuscript pass and the separate citation audit. It is performed
in the same reviewer thread, as required by the selected workflow.

## 1. Second-pass outcome

**No required manuscript repair identified.** After rereading the
complete current article and its actual PDF text, I find its original
inverse-pair theorem and supporting all-number-field classification
complete as stated. The exposition still makes the full-group exclusion,
native-power descent, and every-original-completion requirements clear.

| Severity | Open findings | Required action |
| --- | --- | --- |
| Critical | None identified | None |
| Major | None identified | None |
| Minor | None requiring an author change identified | None |

This is an actual second manuscript reading, not merely a hash check
or a renaming of the citation audit. It is also not evidence from two
independent manuscript reviewers: the same nonauthor reviewed both
passes. No quality improvement, revision, or score increase is inferred
from rereading unchanged text. No publication, submission-readiness,
peer-review acceptance, formal-evaluation, or release verdict is issued.

## 2. Actual read extent and exact byte bindings

For this pass I again read every line of `main.tex`, all seven included
section files, the sole table, and the complete bibliography. The
compilation inputs total 735 lines: main 53, sections 615, table 21,
and bibliography 46. I again extracted the current PDF directly with
`pdftotext -layout`, separately for pages 1–4 and 5–8, and read all
eight pages through the last bibliography entry.

I read the complete raw first manuscript review (347 lines), complete
separate citation audit (258 lines), actual no-change log (118 lines),
actual lifecycle state (119 lines), and the unchanged `SOURCES.md`
(102 lines). These are actual reads, not acceptance summaries supplied
by the coordinator. All hashes below were computed on the files in
this pass. Paths are relative to the manuscript directory.

| Input | SHA256 |
| --- | --- |
| `main.pdf` | `d1f0c9bcab429d955b8700c2ce5bcc811f40f1f77f9bf7655ab8a4af0942a9aa` |
| `main.tex` | `e83ee44b45b9a4be1e98a150ec05514a3f47fcbc3f87342da90cfed55d3201c8` |
| `sections/00_abstract.tex` | `ef3ccceef4dedb08c052bf56563f6976100ac9d38b8a87419c71c543760d3ed8` |
| `sections/01_introduction.tex` | `68852fd93b21c6c7322bd9230170db19f142281d3d7d6dd4c5419d51b80dafc9` |
| `sections/02_axis.tex` | `f49282b52048a15046c3bb2be8644f252ef77e8f6e0df3b48f6e5eac41acecb0` |
| `sections/03_centralizer.tex` | `a5eb22a9144d4893e896aae6f222e917d5f337a2315a5d7b8f2a4af99f0fad56` |
| `sections/04_descent.tex` | `15e6b2f06402a64c62e4c2bb7cd787b47f4acb4a80cb26f4c92a9a85da1cb930` |
| `sections/05_places.tex` | `da4035fc48b59bad0e1a4f64f9c79bab2f05400f5e85496449f15c800eaf7ed7` |
| `sections/06_control.tex` | `7bc226b0cfab97680f02b82e5e26efa648ce1d2ee3f4c4ae98e2fa3b2beca21f` |
| `figures/TABLE_local_places.tex` | `102a0dac97aff1519c20e53122b731543ff0380f9a9ffa7568a42c33a1bcc7fb` |
| `references.bib` | `a4ce6daf2a069c51bece1a08c45ad8f241c8cfca74b20fede1d6e5cac8b564b7` |
| `SOURCES.md` | `04813dc535c7d6fc4d10140f7bd5f3a4483db05dbd240c2609422239128ef5d1` |
| `reviews/round1/REVIEW.md` | `5d1b198e0828571f57991abb8b2d74e008c5eb3dbc916ae212964d340f520c45` |
| `reviews/citations/REPORT.md` | `80b1dbf06d648de9c4ae51590a707d1dcf81e79c60b602eb246a27400cb25223` |
| `PAPER_IMPROVEMENT_LOG.md` | `d0cf47a68f64f0da1f8db4d9203f86368ac7b0c563f21cca2e66498bde4af824` |
| `PAPER_IMPROVEMENT_STATE.json` | `9521819d11f3a18278e0cd493c67d907d53619a7d9b8076d23234fdd5aaafc9e` |

The separately rehashed `main_round0_original.pdf`, `main_round1.pdf`,
`baseline/main.pdf`, and `build/attempt_01/main.pdf` all have the same
PDF hash as `main.pdf`. The current compilation-input hashes agree
with those personally bound in pass 1 and in the actual no-change log.

The coordinator's separate 36-binding and exact snapshot-membership
verification is not relabelled as a new check by this reviewer. The
earlier R5 proof and mathematics/source reviews, read completely in
pass 1, remain context; this pass relies on rereading the complete
typeset proofs rather than repeating that old-artifact audit.

## 3. Honest no-change disposition

The log and state accurately record zero required first-pass author
repairs, zero implemented changes, and zero additional compilations.
The named round-0 and round-1 PDFs are disclosed as copies made at
the later preservation checkpoint from an already frozen baseline.
They are not represented as distinct scientific or editorial versions,
or as PDFs produced by nonexistent review-driven builds.

The separate citation audit is expressly not counted as the second
manuscript pass. The first review and citation report remain complete
raw files, not altered author paraphrases. Their verified hashes agree
with the immutable references in the log and state.

The state still says that a second review awaits activation because it
records the preceding checkpoint. The coordinator's subsequent explicit
assignment authorizes this pass; a reviewer must not rewrite that
historical state in order to start reading. No correction to the frozen
record is requested. A separately authorized lifecycle update can later
record the actual second-pass outcome.

## 4. Rigor and exposition reassessment

### Original statement and field scope

Theorem 1.1 concerns exactly the original word

$$
F=H_{4,7}H_{1/16,15}H_{16,15}H_{1/4,7}
\quad\text{over }K=\mathbb Q(\sqrt7),
\qquad H_{c,d}(x,y)=(y,cy^d-x),
$$

with rightmost-first composition. Its rational coefficients are not
used to replace $K$ by $\mathbb Q$. The statement permits all degrees
and orders of a hypothetical global polynomial reversor. The local
involutions are constructed witnesses, not a restriction of the global
search. The question, abstract, theorem, proof, and conclusion agree.

Theorem 1.2 retains every number field $L$, every $a\in L^\times$,
and every integer $j$ in

$$
\operatorname{Rev}_L(F_a)
=\{F_a^jR_t:j\in\mathbb Z,\ t\in L^\times,\ t^8=a^2\},
\qquad R_t(x,y)=(t^{-1}y,tx).
$$

The notation $F_0$ is explicitly distinguished from the forbidden
parameter $a=0$, and the convention that `Rev` means the reversor
coset rather than the whole reversing-symmetry group is clear.

### Exhaustiveness after removal of a native power

I rechecked the possible escape routes that would invalidate a merely
affine argument. Section 2 starts with the whole plane polynomial
automorphism group. Its reduced-word tree argument and displacement
formula force every centralizer member to preserve the native axis
and act by an even integral translation, never a reflection.

The turn-degree proof handles the vertex representative, both edge
representatives, their exchange, and arbitrary left action. Thus the
least label period four for $(7,15,15,7)$ constrains the entire
centralizer, not only displayed normal forms. The original map's
eight-edge displacement is the full translation generator. The signed
power removed in Proposition 2.3 is therefore a native power, not a
potentially non-descending shorter root.

Section 3 retains both translations in the diagonal-affine fixer and
then removes them by successive coefficient comparisons. Its four
scalar equations are jointly necessary and sufficient for exactly
$\mu_8$. Their converse is actually verified by conjugation through
the four factors. This yields the full centralizer equality, and
multiplication by the palindromic swap yields all geometric reversors.
No order restriction or unproved centralizer equality enters here.

Section 4 carries this full coset across the alternating scalar twist.
All eight roots of $t^8=a^2$ occur, including $t^4=-a$. For any
$L$-defined component $F_a^jR_t$, multiplication by the $L$-defined
$F_a^{-j}$ leaves $R_t$ over $L$, forcing $t\in L$ from its actual
coefficient. This works for every signed integer $j$, so coefficient
cancellation in a high-degree reversor cannot escape the criterion.
The proof needs no classification theorem over a completion.

### Every original completion, not almost every place

The local construction is separately proved by identities over an
algebraic closure of any characteristic-zero field and descent of
those identities to the original coefficient field. Its invocation
at $K_v$ does not enlarge that completion or embed it into $\mathbb C$.

Section 5 retains all odd rational primes, with a nonzero quadratic
residue among $2,-2,-1$ and a simple Hensel lift already in
$\mathbb Q_p$. It explicitly includes the ramified prime seven.
At the unique dyadic place, the strict inequality $3>2$ gives a
square root of $-7$ in $\mathbb Q_2$; the resulting square root
of $-1$ belongs to the actual $\mathbb Q_2(\sqrt7)$ completion.
Both real places have $\sqrt2$, and there are no complex places.
The table agrees with these branches and does not conceal an exception.

The global non-root argument is independent of the local construction:
a real root of $t^8=16$ must be $\pm\sqrt2$, and neither belongs
to $K$. Applying the exhaustive family theorem excludes every global
polynomial reversor, rather than just the displayed local formulas.

### Control and readability

The two-factor control is not a second counterexample. Its explicit
nonlinear involutions satisfy $T=E_2E_1$ and $E_1TE_1=T^{-1}$
over $K$, even though the selected affine swap would require the
unsolvable equation $t^8=16$. This is a useful exact explanation
of why the full-group proof is necessary.

The article includes the construction, its exhaustion proof, the
descent, and every local branch in the main text. No central new
argument is replaced by a working-note link. The proof order is
noncircular, and the notation and cross-references allow the stated
theorems to be checked from the article itself.

## 5. Sources and retained limitations

No citation, statement, or source-dependent hypothesis changed since
pass 1. I therefore did not repeat the already performed primary-source
queries or attempt a new literature survey. My earlier independent
primary access remains recorded in the raw first review; the separate
258-line citation audit records its own accesses and limitations.

Rereading the actual citation sentences confirms the same boundaries:
Jung–van der Kulk and the reversing-symmetry framework are classical;
Gómez–Meiss is not used to turn a subgroup inclusion into an equality;
Baake–Roberts' restricted roots-of-unity conclusions are not imposed
over $\mathbb C$; Song Wang's precise power class is old; and
Cantat–Dujardin's scalar-root/full-centralizer mechanism is explicitly
deducted. Combining the latter with Wang is presented as an inferred
arbitrary-pair consequence, not as a source-stated inverse-pair theorem.
The claimed increment stays the constrained pair $(F,F^{-1})$ with
all its polynomial reversing components controlled.

All four bibliography entries remain cited in the appropriate contexts
and render with the same identifiers in the PDF text. The article does
not claim new methods, worldwide priority, minimal degree, a shortest
word, or a classification of all reversible words. Algebraic reversal
is not promoted to physical or quantum time reversal or target
Euler-factor, root-number, automorphy, or Hilbert–Pólya conclusions.

The citation audit's uncompleted status checks remain uncompleted:
authoritative live retraction/Crossmark verification is unavailable
beyond the observed signals; both IOP landing pages were inaccessible;
the published Song Wang full text was not obtained; and the ARS
structural PDF preflight was unavailable because `pypdf` was absent.
The no-change log/state preserve those limitations correctly. This
review neither certifies clean retraction status nor treats an access
limitation as a demonstrated mathematical or citation error.

This pass's full PDF text reading is not an independent all-page visual
inspection or an ARS structural-PASS result. It does not replace the
separately required two fresh deterministic final builds and visual QA.
No original Wang source access or unrelated source proof audit is
newly claimed.

## 6. Scope, execution, and final freeze

The complete auto-paper-improvement-loop skill was reread for this
pass. Its same-thread follow-up and honest review preservation apply
under the explicit current-team mathematics contract. Legacy external
model/API, ML venue, synthetic experiment, score, automatic notification,
and automatic author-edit examples were not executed. There was no fix
requiring a recompilation, and none was invented.

Only this new `reviews/round2/REVIEW.md` was written. The raw first
review, citation audit, log/state, original proofs, all author sources,
PDFs, baselines, and snapshots were preserved. There was no mathematical
diagnostic, source-search rerun, compilation, image rendering, package
installation, new agent, external-model operation, Git action, formal
evaluation, shared-state change, or publication action.

After complete report readback and final binding checks, this second
review is frozen for coordinator adjudication. Its result is zero open
required repairs on the stated manuscript scope. Completion of the
review is not completion of the downstream author lifecycle, final
builds, release, or publication gates.
