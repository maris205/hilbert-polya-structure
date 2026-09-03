#!/usr/bin/env python3
"""Emit the P32 Stage-4-prime writer patch; never apply it."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NOTES = Path(__file__).resolve().parent
PAPER = NOTES.parent
OUT = NOTES / "stage4_prime_revision_patch_round2.json"
SUPERSEDED = NOTES / "stage4_prime_layout_superseded_20260904" / OUT.name
INCIDENT = NOTES / "stage4_prime_layout_preflight_incident_round2.md"
SUPERSEDED_PATCH_SHA256 = "6e7a93bb08a7cd2e2c3d91aca8f09be03f72bdf455fd76fdf9133bfa5725a9aa"
INCIDENT_SHA256 = "626369cb512caadf4c81883d076d4bc4feddbb0744ea50dcf3e5609683617512"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def latex_hash(value: str) -> str:
    if len(value) != 64:
        raise ValueError(value)
    chunks = [value[i : i + 8] for i in range(0, 64, 8)]
    return r"\texttt{" + r"\allowbreak{}".join(chunks) + "}"


def assert_layout_only_reemission(current: dict, superseded: dict) -> list[str]:
    """Prove the current patch differs only by the enumerated TeX layout edits."""
    if {key: value for key, value in current.items() if key != "ops"} != {
        key: value for key, value in superseded.items() if key != "ops"
    }:
        raise RuntimeError("non-operation patch metadata drift from superseded attempt")
    current_ops = {op["block_id"]: op for op in current["ops"]}
    superseded_ops = {op["block_id"]: op for op in superseded["ops"]}
    if list(current_ops) != list(superseded_ops):
        raise RuntimeError("operation ordering or target drift from superseded attempt")
    for block_id in current_ops:
        current_meta = {key: value for key, value in current_ops[block_id].items() if key != "new_text"}
        prior_meta = {key: value for key, value in superseded_ops[block_id].items() if key != "new_text"}
        if current_meta != prior_meta:
            raise RuntimeError(f"operation metadata drift in {block_id}")

    changed = [
        block_id
        for block_id in current_ops
        if current_ops[block_id]["new_text"] != superseded_ops[block_id]["new_text"]
    ]
    expected_changed = ["B0044", "B0047", "B0060", "B0090", "B0098", "B0125", "B0128"]
    if changed != expected_changed:
        raise RuntimeError(f"layout-only target drift: {changed}")

    full_url = "https://github.com/maris205/hilbert-polya-structure/tree/d29a829b4acac29ff8429724467409e9820a8fa2/flow_systems/papers/32-homology-cover-renormalization-uniformity"
    compact_commit = r"\texttt{d29a829b\allowbreak{}4acac29f\allowbreak{}f8429724\allowbreak{}467409e9\allowbreak{}820a8fa2}"
    prior_commit = r"\texttt{d29a829b4acac29ff8429724467409e9820a8fa2}"
    compact_link = rf"\href{{{full_url}}}{{\texttt{{the pinned public repository tree}}}}"
    prior_link = rf"\url{{{full_url}}}"
    old_display = r"""\[
 a_{j,N}(s)=-q_N(g_j)\operatorname{Log}_0
 \!\left(1-e^{-s\ell(g_j)/q_N(g_j)}\right)
 =q_N(g_j)\sum_{r\geq1}\frac{e^{-rs\ell(g_j)/q_N(g_j)}}r,
 \qquad L(m,N;s)=\sum_{j=1}^m a_{j,N}(s).
\]"""
    split_display = r"""\[
 \begin{aligned}
 a_{j,N}(s)
 &=-q_N(g_j)\operatorname{Log}_0
 \!\left(1-e^{-s\ell(g_j)/q_N(g_j)}\right)\\
 &=q_N(g_j)\sum_{r\geq1}
 \frac{e^{-rs\ell(g_j)/q_N(g_j)}}{r},\\
 L(m,N;s)&=\sum_{j=1}^m a_{j,N}(s).
 \end{aligned}
\]"""

    normalized = {}
    for block_id in changed:
        text = current_ops[block_id]["new_text"]
        if block_id == "B0044":
            text = text.replace("\n\n\\begingroup\\sloppy\nThe raw replay is", "\n\nThe raw replay is", 1)
            text = text.removesuffix("\n\\par\\endgroup")
        elif block_id in {"B0047", "B0060", "B0128"}:
            text = text.removeprefix("\\begingroup\\sloppy\n")
            text = text.removesuffix("\n\\par\\endgroup")
        elif block_id == "B0090":
            text = text.replace(split_display, old_display, 1)
            text = text.replace(
                "\n\\begingroup\\sloppy\nThe machine-readable registry audit is",
                "\nThe machine-readable registry audit is",
                1,
            )
            text = text.removesuffix("\n\\par\\endgroup")
        elif block_id == "B0098":
            text = text.removeprefix("\\begingroup\\sloppy\n")
            text = text.removesuffix("\n\\par\\endgroup")
            text = text.replace(compact_commit, prior_commit, 1).replace(compact_link, prior_link, 1)
        elif block_id == "B0125":
            text = text.replace(compact_commit, prior_commit, 1).replace(compact_link, prior_link, 1)
        normalized[block_id] = text
        if text != superseded_ops[block_id]["new_text"]:
            raise RuntimeError(f"non-layout text drift in {block_id}")
    return changed


def main() -> None:
    if sha(SUPERSEDED) != SUPERSEDED_PATCH_SHA256:
        raise RuntimeError("superseded patch lineage drift")
    if sha(INCIDENT) != INCIDENT_SHA256:
        raise RuntimeError("layout incident lineage drift")
    superseded_patch = json.loads(SUPERSEDED.read_text(encoding="utf-8"))
    carrier_path = NOTES / "stage4_prime_writer_authority_handoff.json"
    expected_carrier = "622043c794de49fd390b332f50189466f01cb5f5d7cc7ab72a2f864e16235dd2"
    if sha(carrier_path) != expected_carrier:
        raise RuntimeError("writer authority carrier drift")
    carrier = json.loads(carrier_path.read_text(encoding="utf-8"))
    manifest = json.loads((NOTES / "stage4_prime_base.block-manifest.json").read_text(encoding="utf-8"))
    old_hashes = {row["block_id"]: row["old_hash"] for row in manifest["blocks"]}
    expected_old = {
        "B0018": "d18eb95a579e",
        "B0044": "956f129fc4cf",
        "B0047": "c5ea790bbe98",
        "B0049": "ddc6c9e8b38b",
        "B0060": "583d17ea653b",
        "B0066": "949fc4d34251",
        "B0072": "e05ef8ada14e",
        "B0081": "9d49b642bd6a",
        "B0131": "b95cd6b13817",
        "B0082": "034973da108b",
        "B0083": "8dfa65770fc2",
        "B0084": "63eaeae1a130",
        "B0090": "27fd7c95853c",
        "B0091": "d997106af0b5",
        "B0098": "838b54a25150",
        "B0109": "96855e0a6d6a",
        "B0125": "605381937adc",
        "B0128": "8a55dca1912c",
    }
    if {key: old_hashes.get(key) for key in expected_old} != expected_old:
        raise RuntimeError("authorized target hash drift")

    manifest_path = NOTES / "stage4_prime_reader_artifact_manifest_round2.json"
    replay_path = NOTES / "stage4_prime_literature_replay_round2.raw.json"
    ledger_path = NOTES / "stage4_prime_literature_screening_ledger_round2.json"
    passage_path = NOTES / "stage4_prime_claim_passage_matrix_round2.json"
    closest_path = NOTES / "stage4_prime_closest_work_comparison_matrix_round2.json"
    formal_path = NOTES / "stage4_prime_formal_definition_audit_round2.json"
    scalar_path = NOTES / "stage4_prime_conditional_scalar_lemma_audit_round2.json"
    analytic_path = NOTES / "stage4_prime_analytic_registry_audit_round2.json"
    for path in (manifest_path, replay_path, ledger_path, passage_path, closest_path, formal_path, scalar_path, analytic_path):
        if not path.exists():
            raise RuntimeError(f"missing support artifact: {path.name}")

    replacements = {
        "@@MANIFEST_SHA@@": latex_hash(sha(manifest_path)),
        "@@MANIFEST_BYTES@@": f"{manifest_path.stat().st_size:,}",
        "@@REPLAY_SHA@@": latex_hash(sha(replay_path)),
        "@@LEDGER_SHA@@": latex_hash(sha(ledger_path)),
        "@@PASSAGE_SHA@@": latex_hash(sha(passage_path)),
        "@@CLOSEST_SHA@@": latex_hash(sha(closest_path)),
        "@@FORMAL_SHA@@": latex_hash(sha(formal_path)),
        "@@SCALAR_SHA@@": latex_hash(sha(scalar_path)),
        "@@ANALYTIC_SHA@@": latex_hash(sha(analytic_path)),
    }

    texts = {}
    texts["B0018"] = r"""A bounded closest-work search retained four individually named neighbors.
Levitt and Vogtmann's surface-group Whitehead algorithm is closest to the
finite-set owner-decision component \citep{P32-CW01}; Venkov and Zograf's
finite-index Fuchsian-group factorization is closest to the cover-product
component \citep{P32-CW02}; Blute, Cockett, Jacqmin, and Scott's generalized
power-series construction is closest to the formal-support component
\citep{P32-CW03}; and Parry and Pollicott's periodic-orbit zeta monograph is
closest to the analytic-program component \citep{P32-CW04}.  The verified
four-component matrix is
\path{notes/stage4_prime_closest_work_comparison_matrix_round2.json}
(SHA-256 @@CLOSEST_SHA@@).

\begin{center}
\scriptsize
\begin{tabular}{@{}p{.11\linewidth}p{.19\linewidth}p{.19\linewidth}p{.19\linewidth}p{.19\linewidth}@{}}
\toprule
Work & Owner algorithm & Higher/zero factor & Formal carrier & Compact-uniform program \\
\midrule
P32-CW01 & finite-set surface automorphisms; no root, bytes, inverse branch, or exhaustion & no verified overlap & no verified overlap & no verified overlap \\
P32-CW02 & Fuchsian setting only; no owner interface & finite-index zeta factorization; no ownerwise multiplicity, zero branch, or frozen normalization & product context only; no coefficient equality or projection & analytic context only; no tower schedule or majorant \\
P32-CW03 & no verified overlap & expansions can house candidate factors; no cover derivation & ordered-monoid/finitary-support ring; not the frozen inverse system or zero fiber & support discipline; no scalar tail theorem \\
P32-CW04 & periodic-orbit population only; no canonicalizer & periodic-product context; no P32 content split or normalized factor & formal zeta expressions; no owner-coordinate carrier & closest analytic neighbor; no exact summand, cofinality, majorant, or interchange \\
\bottomrule
\end{tabular}
\end{center}
Each record is nearest in only one component; none closes the joint dependency
chain.  This four-record search is neither exhaustive nor evidence of priority,
and no source is transferred beyond its source-verified passage scope."""

    texts["B0044"] = r"""The executed method remains a staged synthesis over frozen literature and
project records.  The historical Phase-2 aggregate is unchanged: 51 captured
manifestations, 12 duplicates removed, 39 unique records screened, 13 excluded,
and 26 sources retained.  Original-session result rows and row-level decisions
are unavailable and are not reconstructed.  Under the separate Stage-4-prime
retrieval authority, a dated metadata replay submitted all 26 exact frozen query
strings to Crossref: ranks one and two for Q01--Q25 and rank one for Q26, giving
exactly 51 current manifestations.  All 51 rows record HTTP 200 metadata.  DOI,
then normalized title and year, was the declared deduplication rule.  The current
outcome is 19 matches to the frozen inventory, 31 out-of-scope records screened
out, and one duplicate manifestation removed.  This replay neither replaces the
frozen 26-source corpus nor refreshes a scientific result.

\begingroup\sloppy
The raw replay is
\path{notes/stage4_prime_literature_replay_round2.raw.json} (SHA-256
@@REPLAY_SHA@@).  The complete retrieval/deduplication/screening/retention
ledger is \path{notes/stage4_prime_literature_screening_ledger_round2.json}
(SHA-256 @@LEDGER_SHA@@), with a byte-equivalent row surface in the companion
TSV.  Every row carries query, rank, timestamp, interface, HTTP status,
candidate identity, deduplication identity, duplicate link if any, decision,
frozen-inventory match, and reason.  Historical and current counts remain
separately labeled.
\par\endgroup"""

    texts["B0047"] = r"""\begingroup\sloppy
Citation closure is now recorded in a 30-row source-to-claim matrix at
\path{notes/stage4_prime_claim_passage_matrix_round2.json} (SHA-256
@@PASSAGE_SHA@@), with a companion TSV.  Every row gives the component or claim
role, exact passage locator or explicit null, hypotheses, correction state,
applicability statement, and prohibited stronger transfer.  P32-S01--P32-S26
retain \texttt{anchor:none} and \texttt{INCONCLUSIVE} theorem-passage status;
their missing locators were not reconstructed.  Only the narrow publisher- or
author-source scopes for P32-CW01--P32-CW04 are finalized.  Those four scopes
position adjacent components and do not establish a P32 owner interface, factor,
formal application, tail theorem, or joint novelty.  No direct quotation is
introduced, and metadata identity is not treated as theorem verification.
\par\endgroup"""

    texts["B0049"] = r"""The executed scholarly method comprised corpus capture, deterministic
deduplication, inclusion-frame screening, source-effect coding, thematic
synthesis, and fail-closed propagation of unsupported transfers.  The separately
authorized Stage-4-prime supplement added a bounded exact-query metadata replay,
a four-record closest-work search, and notes-side passage and artifact matrices.
It performed no owner enumeration, cover calculation, factor derivation,
coefficient comparison, panel, compact-uniform estimate, limit, or scientific
result refresh.  The following Revision-1 freeze statement governs the earlier
Phase-6 drafting pass; it does not erase the later, separately recorded
metadata-only supplement."""

    texts["B0060"] = r"""\begingroup\sloppy
\textbf{Conditional scalar lemma.}  If \(\ell>0\), \(s>0\) is real, and
\(m\geq2\) is an integer, then
\[
 \Phi_m(s)=\bigl(1-e^{-s\ell/m}\bigr)^{-m}
 \;>\;
 B(s)=\bigl(1-e^{-s\ell}\bigr)^{-1}.
\]
Indeed, put \(x=e^{-s\ell/m}\).  Then \(0<x<1\) and
\(e^{-s\ell}=x^m\).  Since \(m\geq2\),
\[
 (1-x)^m<(1-x)<(1-x^m).
\]
All three quantities are positive, so taking reciprocals reverses both strict
inequalities:
\[
 (1-x)^{-m}>(1-x)^{-1}>(1-x^m)^{-1}.
\]
The outer terms are \(\Phi_m(s)\) and \(B(s)\).  The proof audit is
\path{notes/stage4_prime_conditional_scalar_lemma_audit_round2.json}
(SHA-256 @@SCALAR_SHA@@).  This exact lemma concerns candidate positive real
functions only; it performs no factor derivation, owner observation, coefficient
execution, global obstruction, recovery determination, or Route evaluation.
\par\endgroup"""

    texts["B0066"] = r"""For a higher-content owner with \(d\geq2\), the lemma applies with
\(m=d\) only after the frozen factorial schedule reaches \(d\mid N\), a valid
cover calculation derives the displayed higher-content factor with
\(q_N(g)=d\), and the permitted finite scalar or singleton comparison is bound.
Under all of those antecedents it gives the strict scalar inequality
\(\Phi_d(s)>B(s)\) for every real \(s>0\).  None of the antecedent scientific
derivations or an ownerwise execution is present here.  Thus this is a conditional
implication, not a reported mismatch or global obstruction; failure of any gate
returns \texttt{NOT\_EVALUABLE}."""

    texts["B0072"] = r"""For zero content and a fixed integer \(N\geq2\), the same lemma applies
with \(m=N\) only after the separate zero-content deck, component,
primitive-lift, and normalization derivation yields its displayed factor and the
one-owner \(H_g\) scalar domain is valid.  Under those antecedents it gives
\(\Phi_N(s)>B(s)\) for every real \(s>0\).  It is not obtained by substituting
\(d=0\) in the positive-content system.  No such derivation or owner comparison
was executed, so zero-content scientific status remains
\texttt{NOT\_EVALUABLE}; the conditional inequality alone supplies no global
obstruction, recovery conclusion, or Route credit."""

    texts["B0081"] = r"""Let \(\mathcal O_+\) and \(\mathcal O_0\) be disjoint typed sets of
oriented primitive owners with \(d(g)\geq1\) and \(d(g)=0\), respectively, and
\(\ell(g)>0\).  The positive carrier retains the frozen initial system.  For a
finite \(F\subset\mathcal O_+\) and \(D\in\mathbb N_0\), set
\[
 \mathfrak m_F=(u_g:g\in F),\qquad
 R_{F,D}=\mathbb Q[u_g:g\in F]/\mathfrak m_F^{D+1}.
\]
Order indices by \((F,D)\preceq(F',D')\) exactly when
\(F\subseteq F'\) and \(D\leq D'\).  The map
\(\rho_{(F',D'),(F,D)}:R_{F',D'}\to R_{F,D}\) sets variables in
\(F'\setminus F\) to zero and then truncates total degree above \(D\).  Define
\[
 R_+=\varprojlim_{(F,D)}R_{F,D}.
\]
Each coordinate has the discrete topology and \(R_+\) has the inverse-limit
topology.  Equality means equality in every \((F,D)\) coordinate; convergence
means eventual coordinate stability.  Thus \(R_+\) is a Hausdorff complete
topological \(\mathbb Q\)-algebra, independently of any scalar product."""

    texts["B0131"] = r"""\begin{center}
\small
\begin{tabular}{@{}p{.21\linewidth}p{.41\linewidth}p{.29\linewidth}@{}}
\toprule
Object or map & Exact typed surface & Status and remaining gate \\
\midrule
\(R_{F,D}\), \(\rho\), \(R_+\) & finite-owner/degree quotients; inverse-limit topology and coordinate equality & \texttt{DEFINED}; carrier compatibility proved \\
\(A_F\), \(j_F\) & declared unit denominators and embedding into \(R_+\) & \texttt{DEFINED}; factor derivation pending \\
\(R_0=\bigsqcup_g\{g\}\times H_g\) & separately typed one-owner rational-exponent Hahn fibers & \texttt{DEFINED}; no multivariate zero product \\
\(\pi_g\) & \(R_+\to\mathbb Q[[u_g]]\), compatible at every degree & \texttt{DEFINED}; no global-product conclusion \\
finite scalar maps & \(A_F\to\mathbb C\) and stated zero-fiber subalgebra to \(\mathbb C\), \(\operatorname{Re}s>0\) & \texttt{DEFINED}; no map on all \(R_+\) or \(H_g\) \\
factor application & project factor to carrier and permitted owner comparison & \texttt{NOT\_EVALUABLE}; cover derivations absent \\
majorant and AN-1--AN-5 & exact logarithmic summands on each frozen compact & \texttt{UNPROVED}; enumeration, tail, and interchange absent \\
\bottomrule
\end{tabular}
\end{center}
Here \texttt{DEFINED} refers only to the self-contained algebraic carrier.  The
broader phrases ``formal object unresolved'' or ``not closed'' elsewhere retain
their scientific meaning: no project factor has been derived into the carrier,
no global product or infinite scalar specialization exists, and no recovery or
Route disposition changes."""

    texts["B0082"] = r"""For finite \(F\subset\mathcal O_+\), define the exact localization
\[
 A_F=\mathbb Q[u_g:g\in F]
 [(1-u_g^r)^{-1}:g\in F,\ r\in\mathbb N].
\]
Every denominator has constant term one.  Its truncated geometric inverse in
each \(R_{E,D}\) defines a canonical homomorphism \(j_F:A_F\to R_+\), setting
variables in \(F\setminus E\) to zero at coordinate \((E,D)\).  For
\(\operatorname{Re}s>0\), the finite scalar map
\(\sigma_{s,F}:A_F\to\mathbb C\) is
\(u_g\mapsto e^{-s\ell(g)/d(g)}\); all denominator images are nonzero.  No map
from all of \(R_+\) is declared.

For each \(g\in\mathcal O_0\), let
\[
 H_g=\left\{\sum_{q\in S}a_qz_g^q:a_q\in\mathbb Q,
 \ S\subset\mathbb Q_{\geq0}\text{ well ordered}\right\}.
\]
Equality is rational-exponent coefficientwise and the valuation topology has
neighborhoods \(v(f)>r\), where \(v(f)=\min\operatorname{supp}f\).
The zero type is the tagged family
\(R_0=\bigsqcup_{g\in\mathcal O_0}\{g\}\times H_g\): operations occur only
inside one \(H_g\), with no cross-owner product and no coercion to \(R_+\).
For fixed \(N\), put
\(A^0_{g,N}=\mathbb Q[z_g^{1/N}]
[(1-z_g^{1/N})^{-1},(1-z_g)^{-1}]\subset H_g\) and define
\(\tau_{s,g,N}:A^0_{g,N}\to\mathbb C\) by
\(z_g^q\mapsto e^{-s\ell(g)q}\) for \(\operatorname{Re}s>0\).  The
literature comparison
\texttt{CP-P32-004} remains unresolved and is not a premise of these definitions."""

    texts["B0083"] = r"""\textbf{Formal compatibility lemma.}  The transition maps above are
well-defined continuous unital homomorphisms, satisfy identity and composition,
and make \(R_+\) Hausdorff and complete.  The maps \(j_F\) are injective and
commute with finite-owner restriction.  For every \(g\in\mathcal O_+\),
\[
 \pi_g:R_+\longrightarrow
 \mathbb Q[[u_g]]=\varprojlim_D\mathbb Q[u_g]/(u_g^{D+1})
\]
is a well-defined continuous unital homomorphism satisfying
\(\pi_{g,D}=\rho_{(F,D),(\{g\},D)}\circ p_{F,D}\) for every finite
\(F\ni g\).  Hahn convolution and the stated finite scalar maps are likewise
well defined.

\emph{Proof.}  Variable deletion preserves total degree; hence an element of
\(\mathfrak m_{F'}^{D'+1}\) maps to zero modulo
\(\mathfrak m_F^{D+1}\) when \(D\leq D'\).  Substitution and truncation
compose, proving the inverse-system laws.  The limit is the closed equalizer of
these laws inside a product of complete Hausdorff discrete algebras, so it is
complete and Hausdorff.  In every truncation, \((1-u_g^r)^{-1}\) is the finite
geometric sum through degree \(D\), and these sums commute with transition.  If
\(j_F(p/q)=0\), multiplying by the unit expansion of \(q\) gives \(p=0\) in
every degree, hence \(p=0\); thus \(j_F\) is injective.  The inverse-limit
equations make \(\pi_g\) independent of \(F\) and prove its displayed
compatibility.  For well-ordered supports in \(\mathbb Q_{\geq0}\), sums of
supports are well ordered and each exponent has finitely many decompositions:
an infinite family would contain increasing exponents in one support and force
a descending family in the other.  Hahn convolution is therefore
coefficient-finite; the candidate supports \(\{r/N:r\geq0\}\) and
\(\{r:r\geq0\}\) qualify.  Finally, \(\operatorname{Re}s>0\) makes every
evaluated monomial have modulus below one, so the declared denominator images
are nonzero.  The full audit is
\path{notes/stage4_prime_formal_definition_audit_round2.json} (SHA-256
@@FORMAL_SHA@@)."""

    texts["B0084"] = r"""Singleton projection supplies a one-way falsification rule.  If two
elements of \(R_+\) are equal, their \(\pi_g\) images are equal; therefore a
proved inequality in one compatible singleton coordinate disproves equality of
those two already-defined elements.  The same-owner zero-content comparison is
made only inside its tagged \(H_g\) fiber.  Conversely, singleton projections
are not jointly faithful on mixed-owner monomials: for distinct \(g,h\), every
singleton projection kills \(u_gu_h\).  Thus the lemma neither constructs nor
recovers a global product.  The conditional scalar inequality can witness a
local difference only after the corresponding project factor is independently
derived and mapped through the declared finite scalar domain.  Those scientific
antecedents remain absent, so no ownerwise observation, obstruction, recovery,
or Route credit follows."""

    texts["B0090"] = r"""Let \(g_1,g_2,\ldots\) denote a prospective certified cofinal order of
content-one owners, and put \(q_N(g_j)=1\).  Conditional on the factor derivation,
define the exact logarithmic summand by
\[
 \begin{aligned}
 a_{j,N}(s)
 &=-q_N(g_j)\operatorname{Log}_0
 \!\left(1-e^{-s\ell(g_j)/q_N(g_j)}\right)\\
 &=q_N(g_j)\sum_{r\geq1}
 \frac{e^{-rs\ell(g_j)/q_N(g_j)}}{r},\\
 L(m,N;s)&=\sum_{j=1}^m a_{j,N}(s).
 \end{aligned}
\]
Here \(\operatorname{Log}_0\) is defined by the displayed absolutely convergent
series and tends to zero as \(\operatorname{Re}s\to\infty\).  Every row below
uses
\(K=K(\delta,T,R)\) with \(\delta>0\), finite \(T\geq0\), and finite
\(R\geq1+\delta\), and one of the separate schedules
\(S_k\in\{k!,2(k!)\}\).  The explicit pointwise bound is
\[
 M_{j,N,K}=-q_N(g_j)\log\!\left(1-e^{-(1+\delta)\ell(g_j)/q_N(g_j)}\right),
\]
which becomes \(M_{j,K}=-\log(1-e^{-(1+\delta)\ell(g_j)})\) for content one.

\begin{center}
\scriptsize
\begin{tabular}{@{}p{.06\linewidth}p{.17\linewidth}p{.25\linewidth}p{.23\linewidth}p{.17\linewidth}@{}}
\toprule
ID & Indices and coupling & Limit on \(K\) and exact interchange & Majorant obligation & Prerequisites/status \\
\midrule
AN-1 & fix schedule and \(k\); \(N=S_k\); \(m\to\infty\) & \(\lim_m L(m,S_k)=\sum_{j\geq1}a_{j,S_k}\), uniformly on \(K\) & prove \(\sum_jM_{j,S_k,K}<\infty\) & factor, branch, cofinal owner order; \texttt{UNPROVED} \\
AN-2 & fix \(m\); \(k\to\infty\), separately for both \(S_k\) & \(\lim_k\sum_{j\leq m}a_{j,S_k}=\sum_{j\leq m}\lim_ka_{j,S_k}\) on \(K\) & for \(j\leq m\), \(\sup_{k,s\in K}|a_{j,S_k}(s)|\leq M_{j,K}<\infty\) & factor and content-one applicability; \texttt{UNPROVED} \\
AN-3 & first \(m\to\infty\), then \(k\to\infty\) & \(\lim_k\sum_ja_{j,S_k}=\sum_j\lim_ka_{j,S_k}\), uniformly on \(K\) & one \(k\)-independent \(\sum_jM_j(K)<\infty\) & AN-1, component limits, cofinality; \texttt{UNPROVED} \\
AN-4 & first \(k\to\infty\), then \(m\to\infty\) & justify \(\lim_m\lim_kL=\lim_k\lim_mL\) and the common owner sum on \(K\) & same summable \(M_j(K)\) and component convergence & AN-2/AN-3, common order; \texttt{UNPROVED} \\
AN-5 & \(m_k=2^k\), \(N=S_k\), both schedules & identify \(\lim_kL(2^k,S_k)\) with the common AN-3/AN-4 limit on \(K\) & \(\sum_jM_j(K)<\infty\) and \(\sum_{j>2^k}M_j(K)\to0\) & cofinal diagonal and common iterated limit; \texttt{UNPROVED} \\
\bottomrule
\end{tabular}
\end{center}
\begingroup\sloppy
The machine-readable registry audit is
\path{notes/stage4_prime_analytic_registry_audit_round2.json} (SHA-256
@@ANALYTIC_SHA@@).
\par\endgroup"""

    texts["B0091"] = r"""The five rows are obligations, not limit results.  The prospective
content-one identity \(q_N=1\) makes the displayed candidate summand independent
of \(N\), but it cannot replace the missing factor derivation, certified cofinal
owner order, or absolute owner tail.  AN-1 fixes \(k\); AN-2 fixes \(m\);
AN-3 and AN-4 declare opposite iterated orders; and AN-5 couples
\(m_k=2^k\) to each full infinite modulus schedule.  A proof for one row or one
schedule cannot be transferred silently to another.  The prospective
\(1\leq k\leq8\) prefix and panels
\(m\in\{8,16,32,64,128\}\) remain unexecuted diagnostics and have no
convergence, cofinality, majorant, interchange, infinite-scalar, or scientific
force."""

    texts["B0098"] = r"""\begingroup\sloppy
Every artifact claimed current in this section is enumerated in
\path{notes/stage4_prime_reader_artifact_manifest_round2.json} (SHA-256
@@MANIFEST_SHA@@; @@MANIFEST_BYTES@@ bytes; schema
\path{round10-stage4-prime-reader-artifact-manifest/1.0}).  Its stable public
base is the exact repository commit
\texttt{d29a829b\allowbreak{}4acac29f\allowbreak{}f8429724\allowbreak{}467409e9\allowbreak{}820a8fa2} at
\href{https://github.com/maris205/hilbert-polya-structure/tree/d29a829b4acac29ff8429724467409e9820a8fa2/flow_systems/papers/32-homology-cover-renormalization-uniformity}{\texttt{the pinned public repository tree}}.
The manifest gives path, full SHA-256, byte count, schema version or explicit
non-schema media type, access state, and bounded evidentiary role for all 11
claimed Section-6 inputs: source inventory, verification rows, Phase-4 report,
four Phase-5 reviews, synthesis, Phase-6 checkpoint, frozen methodology
contract, and ClaimIntent manifest.  All 11 were byte-verified at that commit.

The same manifest inventories 14 current Stage-4-prime notes sidecars as
\path{LOCAL_NOTES_SIDECAR_NOT_PRESENT_AT_PINNED_COMMIT}.  They are
not misrepresented as remotely reader-resolved; repository synchronization and
post-apply audit remain pending.  The commit locator is content-addressed but is
not a persistent archive, release DOI, or preservation guarantee.  Artifact
hash closure does not make prose generation deterministic, passage transfer
theorem-verified, or any scientific result reproducible.
\par\endgroup"""

    texts["B0109"] = r"""The dated supplement exposes all 51 current replay manifestations and
their row decisions, but it is not a reconstruction of the unavailable
historical 51 rows.  Its 19 inventory matches, 31 out-of-scope screens, and one
duplicate do not replace or recalculate the frozen 26-source corpus.  The 30-row
claim-passage matrix preserves \texttt{INCONCLUSIVE} status for all 26 inherited
\texttt{anchor:none} uses and finalizes only four narrow closest-work method
scopes.  Exact theorem passages and hypotheses for the inherited uses remain
unavailable; general correction, retraction, source-conflict, and conflict-of-
interest screening was not expanded.  The new sidecars are local and pending
repository synchronization.  No missing evidence or remote access state is
reconstructed."""

    texts["B0125"] = r"""\paragraph{Data and materials availability.}\begingroup\sloppy
The exact inventory is
\path{notes/stage4_prime_reader_artifact_manifest_round2.json} (SHA-256
@@MANIFEST_SHA@@; @@MANIFEST_BYTES@@ bytes).  It records a schema or explicit media type,
byte count, full digest, access state, and bounded role for every listed file.
The 11 artifacts claimed current in Section 6 are byte-identical at public
commit \texttt{d29a829b\allowbreak{}4acac29f\allowbreak{}f8429724\allowbreak{}467409e9\allowbreak{}820a8fa2}; its resolving base is
\href{https://github.com/maris205/hilbert-polya-structure/tree/d29a829b4acac29ff8429724467409e9820a8fa2/flow_systems/papers/32-homology-cover-renormalization-uniformity}{\texttt{the pinned public repository tree}}.
The 14 Stage-4-prime support files, including the versioned notes-side
bibliography, replay ledger, passage matrix, and proof audits, are explicitly
marked local and absent from that pinned commit pending synchronization.  The
canonical bibliography, manuscript, PDF, code, experiments, results, routes,
and README remain unchanged.  The commit is not claimed to be a persistent
archive or DOI.  No owner panel, cover computation, coefficient table, tail
dataset, factor certificate, or scientific result was generated.
\par\endgroup"""

    texts["B0128"] = r"""\begingroup\sloppy
\paragraph{Development provenance.}  Four procedurally separated review
labels---citation integrity, Devil's Advocate, editorial, and ethics/integrity---
were instantiated within one Codex model family.  Their same-family,
correlated-error limitation remains explicit; role separation is not independent
validation.  The recorded \texttt{MAJOR\_REVISION} code and Liang Wang's author
adjudication are workflow history, not evidence for a factor, formal equality,
inequality application, obstruction, recovery result, or limit theorem.  The 26
inherited uses in the preceding paragraph still lack passage locators; the four
new closest-work records have only their separately bounded narrow scopes.
\par\endgroup"""

    for key, value in list(texts.items()):
        for token, replacement in replacements.items():
            value = value.replace(token, replacement)
        if "@@" in value:
            raise RuntimeError(f"unexpanded token in {key}")
        texts[key] = value.strip()

    item_for = {
        "B0018": "REV-P32-EIC-W1",
        "B0098": "REV-P32-EIC-W2",
        "B0125": "REV-P32-EIC-W2",
        "B0049": "REV-P32-EIC-W4",
        "B0128": "REV-P32-EIC-W4",
        "B0081": "REV-P32-R1-W1",
        "B0082": "REV-P32-R1-W1",
        "B0083": "REV-P32-R1-W1",
        "B0084": "REV-P32-R1-W1",
        "B0131": "REV-P32-R1-W1",
        "B0090": "REV-P32-R1-W2",
        "B0091": "REV-P32-R1-W2",
        "B0044": "REV-P32-R1-W4",
        "B0047": "REV-P32-R1-W4",
        "B0109": "REV-P32-R1-W4",
        "B0060": "REV-P32-DA-M1",
        "B0066": "REV-P32-DA-M1",
        "B0072": "REV-P32-DA-M1",
    }
    base_order = [row["block_id"] for row in manifest["blocks"]]
    target_order = sorted(texts, key=base_order.index)
    ops = []
    for block_id in target_order:
        op = "insert_after" if block_id == "B0128" else "replace_block"
        ops.append(
            {
                "op": op,
                "block_id": block_id,
                "old_hash": old_hashes[block_id],
                "new_text": texts[block_id],
                "roadmap_item_ids": [item_for[block_id]],
                "claim_strength_changes": [],
                "collateral_authorization_ids": [],
            }
        )
    patch = {
        "patch_format_version": "1.1",
        "authorization_context": "review_roadmap",
        "revision_round": 2,
        "base_draft_hash": manifest["base_draft_hash"],
        "roadmap_sha256": carrier["roadmap"]["sha256"],
        "author_adjudication_sha256": carrier["author_adjudication"]["sha256"],
        "author_decision_digest": carrier["author_decision_digest"],
        "claim_surface_manifest_sha256": carrier["claim_surface_manifest"]["sha256"],
        "ops": ops,
        "emitted_by": "draft_writer_agent",
    }
    layout_targets = assert_layout_only_reemission(patch, superseded_patch)
    OUT.write_text(json.dumps(patch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "path": "notes/" + OUT.name,
                "sha256": sha(OUT),
                "ops": len(ops),
                "supersedes_patch_sha256": SUPERSEDED_PATCH_SHA256,
                "layout_only_changed_targets": layout_targets,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
