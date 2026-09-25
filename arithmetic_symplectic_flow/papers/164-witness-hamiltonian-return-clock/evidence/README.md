# Evidence — ASFS-20260915-WHR01

**Candidate ID:** ASFS-20260915-WHR01  
**Status:** STOP — COMPLETE HAMILTONIAN RETURN OWNER; INFINITE COMMON-TIME PRIME PACKETS.

## Object lock and proof method

The [version-1 card](../candidate-card.md) was created with apply_patch
before the proof files. It fixes all integer components, the entire real
Hamiltonian phase space, energy H=1, full section q=0,p>0, operational
maximal bi-return domain and actual Hamiltonian timing. No tuple field
was changed after screening. [The paper](../paper.md) gives every
derivation; [the claim ledger](../claim-ledger.md) records the scopes.

Exact inputs: ordinary trial divisibility for every integer n>=2;
a(n)=sum over 2<=d<n of 1_(d divides n); V_a=(1-a) log cosh q+a q;
H=p²/2+V_a(q)+QP. No prime list, zero data, prime-specific parameter,
numerical orbit table or manually inserted logarithmic clock is used.

Methods: bounded-force ODE estimates for ambient completeness; critical
point equations for energy regularity; full monotone-force and oscillator
energy classification; actual first-return quadrature and angular-speed
bound; direct wedge-product preservation; global section-phase flow
coordinates; full exponential transverse periodic equations; the r=1
term of the complete ordinary repetition series.

There is no numerical run or numerical error bar. All time integrals are
exact. No source theorem about Anosov flows, trace classes or published
surface dynamics is imported into the proof. Mathematical controls are
the eight explicitly separate comparator/coverage rows in paper Section 5.

## Bounded historical collision and lineage inspection

Entry sources read: local AGENTS.md, plan.md, current readme.md,
papers/paper-template.md, the 162 portfolio, the frozen 168 scope, and
docs/prior_work/README.md. Focused searches used the terms log cosh,
Hamiltonian, Poincare, oscillator, fixed energy and QP in the named
nearby records, followed by the exact related source records:

- [038 full-ledger obligation](../../038-hamiltonian-periodic-ledger-obligation/paper.md).
- [152 full witness-count card](../../152-coupled-witness-henon-escape/candidate-card.md).
- [155 derivative-roof completeness comparator](../../155-derivative-roof-completeness-test/paper.md).
- [160 dilation/reset clock card](../../160-source-geometric-return-clock/candidate-card.md).

The broader term search found the earlier coupled log-cosh potential in
149 as a different discrete cotangent construction, not this continuous
Hamiltonian/energy/section tuple. This bounded collision inspection is
not a claim of global literature novelty. No new external literature
claim is needed; no web or external-model API call was used by this author.

## Actual delegation and review provenance

Controller /root/research_controller assigned this bounded contract and
the disjoint 164 author path. Author
/root/research_controller/hamiltonian_return_source froze the card and
wrote the five core files. The author separately delegated a read-only
energy/return adversary after the card freeze, specifically to check
missed nonreturning closed orbits, completeness, and packet multiplicity.
That is pre-author feedback, not a blind review or an independent error
process. The controller coordinates a separate formal-internal review
invocation. All invocations use the inherited session model; model review
is not human peer review or proof certification.

The read-only adversary was
/root/research_controller/hamiltonian_return_source/energy_return_adversary.
It returned an actual completed report: no missing full-energy closed
orbit, correct prime E=0 complement and impossible prime E<0, bounded-
force completeness, regular H=1, full return-map wedge cancellation,
uniform roof bound, and the infinite common-time stop. Its alternative
quadrature comparison also obtains T(E)>2 pi; the paper retains its own
angular-speed proof of the sufficient lower bound. The feedback was
received while the five core files were being completed and is not
counted as a blind review or a separate formal review receipt.

The controller-assigned reviewer is
/root/research_controller/hamiltonian_owner_reviewer. The five-file draft
was delivered to that invocation after the author proof was written.
Its actual [completed review](review.md) was then read by the author:
no unresolved mathematical finding and no requested manuscript correction.
The reviewer recorded its criteria, manuscript coverage, same-model and
inherited-context limitations, a separately delegated read-only calculus
check, and SHA-256 hashes of all four core claim surfaces. No mathematical
core file changed after that review. The receipt retains the exact
distinction between full energy and return saturation, and the common-time
STOP without erasing the positive Hamiltonian ownership result.

The ARS academic-paper argument-builder guidance was read and used only
for bounded claim/evidence/reasoning and counterargument discipline. The
existing user scope controls the task; no full publication pipeline,
venue certification, profile script, external-model transport or automatic
research expansion was invoked.

## Mechanical verification receipt

On 2026-09-15 the author ran a read-only Node stdin check on exactly
README.md, paper.md, candidate-card.md, claim-ledger.md and
evidence/README.md. The method uses fs.readFileSync for these five files,
extracts Markdown link targets with /\[[^\]]*\]\(([^\s)]+)\)/g,
resolves local paths against each source file's directory, and checks
fs.existsSync. For an explicit Markdown fragment it additionally forms
the target file's heading slugs by lowercasing, removing characters other
than Unicode letters/numbers, whitespace, underscores and hyphens, then
replacing spaces by hyphens and accounting for duplicate suffixes.

The check also requires the exact candidate ID and the exact status above
in all five files, rejects trailing tabs/spaces except the deliberate
two-space Markdown line break, and rejects a blank line separating two
table rows. Exact output:

```json
{
  "files": 5,
  "localLinks": 42,
  "headingAnchors": 11,
  "idStatusChecks": 5,
  "errors": []
}
```

The evidence receipt is then updated without adding links or changing
core mathematical inputs. A final targeted metadata/format pass applies
to that update. No Git command or non-Markdown file is used by this author.
Mechanical checks and model feedback are not mathematical proofs and
do not transfer Route credit.

After the actual review arrived, the same author filesystem method was
extended to the sixth file evidence/review.md and the added review link.
It also recomputed the SHA-256 digest of paper.md, candidate-card.md,
claim-ledger.md and README.md with Node crypto.createHash('sha256') and
required the exact filename/digest row in the reviewer receipt. Output:

```json
{
  "files": 6,
  "localLinks": 50,
  "headingAnchors": 11,
  "idStatusChecks": 6,
  "reviewedCoreHashChecks": 4,
  "errors": []
}
```

This appended receipt adds no links or mathematical edits. Its own final
metadata and formatting check passed. The four reviewed mathematical
surfaces remain unchanged; further reviewer-only provenance annotations
do not imply that their proofs were rerun.
