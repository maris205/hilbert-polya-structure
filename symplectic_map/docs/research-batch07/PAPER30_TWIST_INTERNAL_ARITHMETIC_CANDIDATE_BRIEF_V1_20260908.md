# Candidate brief: local arithmetic of internal Lindstedt cancellation polynomials

Date: 2026-09-08. Version: V1.
Packet status: FROZEN_COMMON_CANDIDATE_INPUT_V1.
This is a selection document, not a manuscript, publication lock, page measurement,
formal Paper30 project or acceptance of a paper.
Route applicability: NOT_APPLICABLE: no Riemann determinant, arithmetic prime-orbit
clock, Hilbert–Pólya operator or target-zero claim is proposed.

## 1. A single stand-alone question

For the weighted two-harmonic twist map, consider the actual positive-frequency
diagonal jet in the uniquely normalized local periodic elimination problem.
At a prime-power rotation denominator, what is the local arithmetic decomposition
of the cancellation-parameter polynomial at the third internal small-divisor
position? Can its cancellation parameters coincide with those at either of the
first two internal positions?

The position is \(3p\), not perturbation order three and not the third full-system
resonance. The polynomial degree and the required recurrence length grow without
bound with the prime \(p\). The proposed contribution is an exact two-branch
arithmetic classification and pairwise disjointness for this specified polynomial
family. It is not a new general Newton-polygon method, and it does not claim a
classification of the final periodic resonance coefficients.

## 2. Actual object, normalization and coordinate dependence

Use momentum \(y\) here to avoid confusing it with the prime:
\[
 y'=y+\epsilon\sin q+2\lambda\epsilon^2\sin(2q),\qquad q'=q+y'.
\]
The action is the sum, not the average,
\[
 \mathcal A(q)=\sum_{j=0}^{s-1}
 \left\{\frac12(q_{j+1}-q_j)^2-\epsilon\cos q_j
                         -\lambda\epsilon^2\cos(2q_j)\right\}.
\]
For fixed coprime \(r,s\), impose
\(q_j=\theta+2\pi rj/s+u_j\) and \(\sum_j u_j=0\).
The transverse unperturbed Hessian is invertible. Its small analytic elimination
branch is unique for each fixed denominator and fixed parameter compact set;
no denominator-uniform analytic neighborhood is claimed.

Let \(t=\epsilon\exp(i(\theta+2\pi rj/s))\).
The part of \(iu_j\) whose perturbation degree equals its positive Fourier
frequency is \(v(t)\). Degree-frequency filtering of the actual equations gives
\[
 v_n=-\frac{[t^{n-1}]e^v/2+\lambda[t^{n-2}]e^{2v}}{D_n},
 \quad D_n=2-\zeta^n-\zeta^{-n},\qquad 1\le n<s.
\]
This is a unique triangular recurrence, not a polynomial manufactured from
desired roots. Source A01, Notation and Proof Steps 1–2, proves the identity.

Fix any prime \(p\ge5\), integer \(a\ge2\), and primitive \(p^a\)-th root \(\zeta\).
Work at the corresponding \(p\)-adic completion with
\[
 s=p^a,\quad h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,
 \quad K^+=\mathbb Q_p(h),\quad \mathcal O^+=\mathbb Z_p[h].
\]
Normalize \(v_h(h)=1\). Put
\[
 m=(p-1)/2,\quad M=p^{a-1}m=v_h(p),\quad D=3m+1=p+m,\quad
 \chi=(-1)^{m+1}.
\]
The residue field of \(\mathcal O^+\) is \(\mathbb F_p\).
Define the finite actual prefix by
\[
 V_n(L)=\rho^n v_n(L/\rho),\quad d_n=-D_n/h,\qquad
 d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}.
\]
Negative coefficient indices mean zero; \(V_1=1/2\). Each coefficient extraction
uses only the necessary finite prefix. For \(k=1,2,3\), set
\[
 \mathcal B_k(L)=-[x^{kp-1}]e^V-2L[x^{kp-2}]e^{2V}
               =2d_{kp}V_{kp}.
\]
Since \(3p<p^a\), all these \(d_{kp}\) are nonzero. No actual internal mode has
been projected away or set to zero. The zero of \(\mathcal B_k\) therefore
cancels the specified diagonal jet coefficient, not the entire spatial harmonic,
the final resonant action term or an invariant under arbitrary symplectic
conjugacies.

The raw parameter polynomials obey
\[
 \mathcal B_k(L)=\rho^{kp-1}\mathcal B_{kp\mid p^a}(L/\rho),\qquad
 \mathcal B_{kp\mid p^a}=2D_{kp}v_{kp}.
\]
This invertible linear change preserves factor degrees, multiplicities,
splitting fields and common-root relations, whereas
\(v_h(\lambda)=v_h(L)-1\). “Positive” and “negative” clusters below refer
specifically to the declared \(L\) coordinate. A \(p\)-adic parameter root is
not being asserted to be an actual real bifurcation point.

## 3. Exact whole-package claims

Let \(S=h^{-D}p^2\mathcal B_3\). For every allowed \(p,a,\zeta\):

1. \(S\in\mathcal O^+[L]\) has actual degree \(D\) and a unique factorization
   \(S=P_{\rm cl}U_{\rm cl}\), where \(P_{\rm cl}\) is monic of degree \(m\),
   \(\overline P_{\rm cl}=L^m\), and \(U_{\rm cl}\) is of degree \(p\) with
   unit constant residue. The complete lower Newton polygon is
   \[
    (0,m-1)\longrightarrow(m,0)\longrightarrow(D,M-m).
   \]
   There are exactly two irreducible factors over \(K^+\), of degrees \(m,p\).
   Both are separable; thus the entire third polynomial is squarefree.

2. Each positive-cluster root \(\alpha_j\) has
   \[
    v_h(\alpha_j)=v_h(\alpha_i-\alpha_j)=(m-1)/m\quad(i\ne j).
   \]
   Let \(\kappa^m=-16\chi h^{m-1}\). Then
   \[
    E=K^+(\kappa)=K^+(\alpha_j)
      =\operatorname{Spl}_{K^+}(P_{\rm cl}),\qquad [E:K^+]=e=m,\quad f=1.
   \]
   This extension is cyclic and tamely totally ramified, and roots can be
   labeled \(\alpha_j=\omega_j\kappa+O(h)\), \(\omega_j\in\mu_m\subset K^+\).

3. Each of the \(p\) negative-cluster roots satisfies
   \[
    v_h(\beta)=-(M-m)/p,\qquad
    [K^+(\beta):K^+]=e=p,\quad f=1.
   \]
   These single-root extensions are wildly totally ramified. Their common
   identity, normality, full splitting field and Galois group are NOT determined.
   The compositum of \(E\) with any one of them has degree and ramification
   index \(mp\) and residue degree one; it is not identified as the full
   splitting field.

4. The three actual internal forcing polynomials are pairwise coprime:
   \[
    \gcd_{K^+[L]}(\mathcal B_i,\mathcal B_j)=1\qquad(1\le i<j\le3).
   \]
   This is stronger than merely excluding simultaneous vanishing of all three.
   The second polynomial has actual degree \(p\); a false smaller-degree
   argument is not part of this claim.

These are dependent conclusions of one structural theorem package.
They are not separate methods, independent research projects or grounds for
splitting the package into multiple papers.

## 4. Nonstandard coefficient inputs and standard consequences

The model-specific inputs include the exact normalization
\[
 \overline S=-3\chi L^m/64,\qquad
 S(0)=-3h^{m-1}/4+O(h^m),\qquad
 [L^j]S\in h^{m-j}\mathcal O^+\quad(1\le j<m),
\]
and the high-coefficient bounds
\[
 p[L^j]\mathcal B_3\in h^m\mathcal O^+\quad(j>m),\qquad
 p[L^j]\mathcal B_3\in h^{2m}\mathcal O^+\quad(p\le j\le D).
\]
The decisive high endpoint is
\[
 p[L^D]\mathcal B_3=-\frac3{16}h^p+O(h^{p+1}).
\]
Writing \(U_{\rm cl}=\sum_{r=0}^p u_rL^r\), these inputs yield
\[
 u_0=-3\chi/64+O(h),\quad
 v_h(u_r)\ge M-p\ (1\le r\le m),\quad
 v_h(u_r)\ge M-m-1\ (m+1\le r<p),\quad
 v_h(u_p)=M-m.
\]
The strict inequalities placing the intermediate points above the chord,
and the coprime horizontal/vertical lengths, then permit standard Newton
and ramification arguments. Those general arguments are not new.

The necessary earlier internal identities are
\[
 \overline{h^{-m}\mathcal B_1}=\chi(2-L^m),\qquad
 \overline{h^{-2m}p\mathcal B_2}=2,\qquad
 [L^p]\mathcal B_2=4\chi h^m+O(h^{m+1}).
\]
The highest-to-constant coefficient ratios of \(\mathcal B_2\) and
\(U_{\rm cl}\), after the common scale \(\chi ph^{-m}\), have residues \(2,4\).
This distinguishes two degree-\(p\) polynomials; irreducibility then excludes
their sharing a root. Irreducibility plus nonproportionality is standard;
the actual coefficient comparison is the object-specific input.

The exact valuation of \(S\) away from the two critical circles follows from
the Newton polygon, and at them from factorization. A23 Step 5 records it.
On the negative critical circle the full sum of distances to all negative
roots remains necessary. This short consequence does not solve their
unknown pairwise distances or add a new main proof block.

## 5. Complete author inputs and proof organization

The following 23 core author files and one narrowly used background supplement
are included unchanged. Their line counts
and hashes identify inputs only; they are not proxies for substantive pages.
The complete source files are available to both reviewers. Read the actual
proof of every lemma used by this package, including its finite ranges,
integrality and error estimates, rather than substituting a disposition or
the author's reported number of checks.

Some files also contain stronger or unrelated historical claims. The necessary
sections and exclusions are identified in the
[dependency map](PAPER30_TWIST_INTERNAL_ARITHMETIC_DEPENDENCY_MAP_20260908.md).
A01 contributes the actual diagonal identity, not its numerical root scan;
A01s Step 1 supplies the standard analytic elimination uniformly on a fixed
compact parameter set used in Section 2. Its later parity improvement,
primitive-orbit correspondence and count of local periodic orbits are excluded.
A02's detailed first-layer Frobenius classification is optional.
A09 contributes its full-\(H\) response and complete cubic endpoint, not its
three later second-order moments or the noncore \(p\ge7\) root translation.
Finite \(p=5,7\) tables and code are not evidence for universal quantifiers.
Do not omit necessary proofs merely because their conclusion was later
strengthened, and do not count excluded claims as content of this candidate.

| ID | Frozen author source | Lines | SHA256 |
| --- | --- | ---: | --- |
| A01 | [PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907.md](PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907.md) | 267 | `40ce08ac1bafc2da2c4643d66744ebf96c813061b0eacf3f18b0f939960ba177` |
| A01s | [PAPER30_TWIST_REDUCTION_PARITY_NOTE_V1_20260907.md](PAPER30_TWIST_REDUCTION_PARITY_NOTE_V1_20260907.md) | 133 | `0f601af6c4994e6d2f4d89248c048b0b8b081ec6345536e25dc72649ed78856b` |
| A02 | [PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md) | 430 | `f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616` |
| A03 | [PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md) | 391 | `0a70394315cfe78b860c6ac46eec53bb58ccb8b3e432c1108438f7e721ee4c34` |
| A04 | [PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md) | 640 | `278ce73d9844c8a30b93b8952b8a3a178aa577f1c808fce48c333be721c97f15` |
| A05 | [PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md) | 475 | `3ff45f425669adbd012245f5cf605083a72e3cccb131cc6469f787cc58920e04` |
| A06 | [PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md) | 640 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |
| A07 | [PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md) | 843 | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` |
| A08 | [PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md) | 455 | `da834676ba00aa72e292acee6281b1a4ee4cd4dc8ebfab964a7fd28b503b7f2f` |
| A09 | [PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md) | 761 | `3d0fea6035d33c11e912946a442278711f061bebde32724ad003a3b2f9994e6d` |
| A10 | [PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md) | 320 | `ec3f6de59e55176fe11a62b36d27da516bb8d620c438fdd0037ee6c099a260da` |
| A11 | [PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md) | 393 | `af5cd169e101948d9732cf9f913181ba2697e9fa9b4a848eebd1ffda841f21d1` |
| A12 | [PAPER30_TWIST_THIRD_FORCING_CRITICAL_PROJECTION_PROBE_V1_20260907.md](PAPER30_TWIST_THIRD_FORCING_CRITICAL_PROJECTION_PROBE_V1_20260907.md) | 482 | `c7bad052293f96ab95f7e48026472e06b114a21eb71d6c34e964b0903142e345` |
| A13 | [PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_PROBE_V1_20260907.md](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_PROBE_V1_20260907.md) | 475 | `870d90ff0e9eb85f9ae174c0a2f79a624454ed248db0acbd546b44e7856b28f6` |
| A14 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_PRECRITICAL_PROOF_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_PRECRITICAL_PROOF_V1_20260908.md) | 304 | `7d869eff22fda9975b0da74233c2d93bc962d7ccb91e209e6fbdee32c8c91516` |
| A15 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_HIGH_CRITICAL_PROBE_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_HIGH_CRITICAL_PROBE_V1_20260908.md) | 544 | `a1788d54a7e400c688c47af00e4f6bbab413b56fbfc1f137a446f17c1492ec77` |
| A16 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_BOUNDARY_HIGH_PROOF_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_BOUNDARY_HIGH_PROOF_V1_20260908.md) | 319 | `5d28cd8c32ca64fdcb4d762f4076218fc4dd77f07cd35b5c7b1155aa1c006a07` |
| A17 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md) | 306 | `033a05a8bc6f9d34125696366bf0ee23f84682049df1d7edd8dd80c702929502` |
| A18 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md) | 619 | `730fd03b7da722111250813635ac9f9ac052928b516dee805a28204124df4de7` |
| A19 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md) | 658 | `e754946905524581d55cbf1d893c8141db7fc69a1aa33050d778c1754bf789a2` |
| A20 | [PAPER30_TWIST_FIRST_FORCING_TOP_NEXT_LAYER_PROOF_V1_20260908.md](PAPER30_TWIST_FIRST_FORCING_TOP_NEXT_LAYER_PROOF_V1_20260908.md) | 229 | `e22080d67d9369db83428095141f1c8f63ad8bee7de5d3bec19135c8e76a8925` |
| A21 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_PROBE_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_PROBE_V1_20260908.md) | 458 | `9a4b698fe1a4f4e236010e735c0105bb687fd9ebf554e36840e2b9302f8c4894` |
| A22 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_PROBE_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_PROBE_V1_20260908.md) | 537 | `a21428c1dc49fcefc523c98cc8c8910ac1fc5627443769e1427f5d68c601bc48` |
| A23 | [PAPER30_TWIST_THIRD_FORCING_NEGATIVE_NEWTON_AND_COPRIME_PROOF_V1_20260908.md](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_NEWTON_AND_COPRIME_PROOF_V1_20260908.md) | 252 | `0de73ed23ab07d32b76823cdad81d3642fc259eaf1a20bfc981697d5bae0269c` |

The forward chain comprises the actual object and local ring; the first
finite reflection layer; two factorial bands and the second forcing;
the complete third action endpoint and fixed-degree separation; uniform
positive-cluster support and critical constant; all high-coefficient ranges
including the separate boundary band; finite even/odd reference and Ward
identities; the zero-order quadratic response; the three-source nonzero
endpoint; and the local algebra and pairwise coprimality.

Common definitions, factorial lemmas and response identities must each be
credited once. The negative high-range projection and its boundary are not
interchangeable. The finite even/odd window does not permit reduction of
nonintegral omitted coefficients. The positive critical projection cannot be
replaced by reflection parity beyond its legitimate range.

## 6. Independent proof checks and correction boundaries

The completed
[author-to-review roster](PAPER30_TWIST_INTERNAL_ARITHMETIC_REVIEW_BINDINGS_20260908.md)
binds all A01–A23 to 18 complete nonauthor mathematical reports and 12 scoped
acceptance dispositions. A01s is jointly covered by its R01 and D01.
Joint reports count once; no single historical report reviewed this entire
current package. Read all 18 reports in roster Section 3, together with the
actual necessary author proofs and the corresponding acceptance boundaries
in roster Section 4. The roster is a source index, not a new mathematical vote.
Its frozen SHA256 is
`13ce2b8a5617baabbc13642f9b5603e8dbe6aa278b5a5adfc9d0048de4067cb1`.

Roster Section 5 distinguishes the failed original TOP_COEFFICIENT V1 from
the independently accepted new A17; the former is not an input to the latter.
It also retains the noncore GENERAL_NEXT_LAYER_ROOT_BOUND V1 wording failure
and its narrow V2 correction, without attributing that failure to A09/A10.
A23's conditional use of the new high endpoint is closed by the separate
same-round input reviews and the final complete-structure disposition.
An interface review is not being represented as a full repeat of the upstream
mathematics. Historical source filenames do not determine reviewer independence.

Existing accepted checks support their stated mathematical portions, not
candidate novelty, stand-alone value or natural body capacity. Historical
“awaiting review” wording in frozen author notes is interpreted through the
actual later checks; original failures remain failures.

In particular, the coefficient-level adjoint in A22 is an identity over
\(\mathbb F_p\). Its subsequent characteristic-zero convolution is a
\(p\)-integral representative of the finite residue calculation, not a
characteristic-zero identity for the original unknown response endpoint.
No adjoint defect is divided by \(p\). For \(p=5\), cancellation to cubic
summands precedes application of power-sum formulas. The actual quotient
\(4^D\bmod p\) is \(4\), not \(16\).
The precise domain clarification is roster R17 Section 7. The two older
short-reference corrections are A19 to A02 equation (15), and A23 to A16
Step 5, equations (20)–(21). They do not change the frozen author proofs.

## 7. Prior-art deductions and internal noncollision

The identical external sources for the reviewers are the
[bounded novelty preflight](PAPER30_TWIST_INTERNAL_ARITHMETIC_NOVELTY_PREFLIGHT_20260908.md)
and its
[independent boundary check](PAPER30_TWIST_INTERNAL_ARITHMETIC_NOVELTY_INDEPENDENT_CHECK_20260908.md).
Their conclusion is only NO_DIRECT_MATCH_IN_READ_SCOPE; GLOBAL_NOVELTY_UNCERTAIN.
Read the stated actual source-access limits, not just the conclusion.

Mandatory deductions include:

- Olvera's weighted Fourier setting, homological recursion and continuation
  after a leading resonant coefficient vanishes. Merely using different
  \(\epsilon\) weights or advancing beyond a cancellation is not new.
- Berretti–Gentile's Lindstedt/tree recursions, resonance cancellation and
  minimal-tree mechanisms. The presence of the same classical map is not
  novelty, and “use \(p\)-adic methods on this model” alone is not a contribution.
- General Newton/Hensel/Kummer and ramification theory, including the
  coprime-length single-edge irreducibility criterion.
- The existing two-harmonic standard-map literature on island chains,
  isochronous and shearless bifurcations.
- Djakov–Mityagin's double-harmonic Hill gap formulas and the Suris background.
  No parameter-preserving identity has been proved from their linear
  spectral/path objects or full integrable potential to the nonlinear
  internal forcing here. Neither transfer of their best result nor a
  categorical proof that no bridge can exist is claimed.

The bibliography distinguishes the EPJST article's 2025 online publication from
its 2026 volume assignment. Recent source queries and access limits are already
logged. A focused primary-source check is permitted if a reviewer identifies a
specific uncertainty; there is no need to repeat an unaltered broad search.

The same
[local noncollision report](PAPER30_TWIST_INTERNAL_ARITHMETIC_NONCOLLISION_CHECK_20260908.md)
is provided to both reviewers. Its six closest-paper matrix and supplementary
comparisons distinguish coefficient valuation from the support/degree Newton
polygons in Papers20–28 and from polynomial cohomology in Paper29.
It also records the actual earlier local-resonance and jet packages.
It is a bounded comparison of read statements, not an exhaustive theorem
search through all files.

The earlier \(p,2p\) final-forcing results and the \(B_1,B_2\) and positive-cluster
stages in this same twist research chain are genuine prior work within the
program. Necessary earlier lemmas enter this one proof package once.
No publication or extra contribution is manufactured by counting research
dates, repeated derivations, increasingly sharp old root bounds or checks.

## 8. Nonclaims and forbidden extensions

The package does NOT solve the final prime-power \(C,Q\), all denominators,
all real roots, every internal layer, the full negative splitting field,
negative pair distances or the second forcing's full polygon and simplicity.
None is secretly assumed by the stated central theorem.

The internal coefficients are not claimed to be arbitrary-coordinate
dynamical invariants, physical bifurcation parameters, integrability
obstructions or a classification of actual periodic-orbit splitting.
A future dynamical application would require a separate bridge controlling
all intervening contributions, not merely an observation that the recurrence
eventually reaches \(s\).

No fitted roots, parameter tuning with \(\epsilon\), post-hoc threshold changes,
combination of different constructions, new experiment or paid/external
operation is part of this candidate. The manuscript cannot be padded with
the excluded special cases, open directions, other stopped candidates,
source listings, audit histories or textbook treatments of standard tools.

## 9. Identical contract for two fresh, mutually blind candidate reviews

Each reviewer independently evaluates this exact entire package:

1. Novelty at least 7.5/10 after the mandatory prior deductions.
2. Stand-alone scientific value at least 7.5/10.
3. Complete-proof confidence at least 9/10 for the stated full quantifiers.
4. Credible natural capacity of 22–30 substantive English body pages.

Use anonymous single-column article, 11pt, letter paper, one-inch margins and
standard spacing for the capacity judgment. References start separately and
do not count. Give your own justified low/central/high table by necessary
mathematical block, remove duplication, and explain both insufficient and
excessive-length risks. Do not infer body capacity from Chinese source lines,
proof count, agent effort or the need to finish this batch.
If the complete result naturally belongs in a shorter article, fail this
locked capacity gate without denying its mathematical merits. If a complete
proof cannot credibly fit within the upper bound, report that failure too;
omitting necessary lemmas is not an acceptable compression.

Do not read the author-capacity file, author page allocation, earlier
candidate scores, the other current review, or communications reporting them.
The author value preflight and value/scope disposition are not needed for
your decision and are excluded from the common review input.
This brief contains no author's page estimate or desired score.
You may disagree with any prior bounded interpretation after examining the
actual evidence; report a concrete claim/source/quantifier mismatch if found.

The two reviewers must not be authors or previous mathematical auditors of
this package. Neither may read, discuss, infer or import the other's report.
Each owns one disjoint output file and discloses actual identity, tools and
read scope. Use xhigh reasoning as prescribed by research-review; the
specified GPT-5.4 MCP interface is not configured, so do not claim its use,
a human review or a cross-model certificate.
Progress messages may identify read scope and factual questions, but must not
circulate provisional scores or page estimates. Any substantive factual
clarification during the reviews must be supplied identically to both
reviewers. The released packet remains unchanged; a genuine correction
requires a separately identified successor and preservation of the original.

The final decision is the conjunction of all four gates in BOTH reports.
No averaging, best-component selection, construction mixing or repeated
submission of the same failed package is permitted.
The Paper29 special natural-draft measurement exception does not carry over.
A complete candidate PASS only opens the ordinary local manuscript workflow;
it is not a completed paper, PDF acceptance or authority for external effects.

## 10. Common input identity

The accompanying
[review-input manifest](PAPER30_TWIST_INTERNAL_ARITHMETIC_REVIEW_INPUT_MANIFEST_V1_20260908.md)
binds this brief, all 24 author source files, the 18 mathematical reports,
the 12 corresponding dispositions and the six common context/index files.
It also identifies the seven archived correction/boundary documents directly
linked by the roster; their inclusion does not make their excluded results
part of the candidate theorem.
It records byte identity only, not scientific truth, candidate acceptance or
a source/publication lock for a manuscript that does not yet exist.
Both reviewers receive this exact manifest and its externally recorded digest.
There is no recursive permission to read excluded author-capacity or value
files merely because a permitted historical document links them.
