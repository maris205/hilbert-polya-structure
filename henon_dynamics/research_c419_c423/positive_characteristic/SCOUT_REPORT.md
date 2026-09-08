# Positive-characteristic first-pass contracts: C419–C423 research

Status: **FIRST PASS COMPLETE; THREE SCREENED; ZERO RECOMMENDED ADMISSIONS**.
Frozen on 2026-09-07 before any new exact computation. These are AI-generated
questions, not claimed theorems. This lane may write only this directory;
the coordinator owns admission and the five-paper completion gate.

## PC-F: residue-zero native forward ramification

- **Object and full family:** every prime $p\ge5$, every finite extension
  $k=\mathbb F_{p^s}$, every $b\in k$, and
  $f_b(z)=z+z^2+z^3+bz^4\in k[z]$. The cubic $b=0$ is included.
- **Domain and clock:** the formal disc $z k[[z]]$, with point map
  $h\mapsto f_b(h)$ and its ordinary iterates, not inverse-tree height.
  The finite native quotients are $z k[[z]]/(z^M)$, $M\ge2$.
- **Observable:** the complete lower ramification sequence
  $i_e(f_b)=\operatorname{ord}_z(f_b^{p^e}(z)-z)-1$, allowing infinity
  if an iterate is the identity; consequently the ordinary cycle numbers
  on every finite quotient. Scheme multiplicity is not called a global
  algebraic-closure point count.
- **One question:** classify this sequence for the entire displayed family,
  including all coefficient exceptions, in a finite explicit parameter
  stratification; determine whether any part remains beyond existing
  ramification theorems and their routine finite-jet application.
- **Intrinsic arithmetic and bridge:** wild local ramification is intrinsic.
  A proved full sequence would be source-side local arithmetic (potential
  A1 material); no spectral realization, target divisor/Euler-factor law,
  functional equation or independent A2 bridge is presently supplied.
- **Ownership to subtract:** the local minimal-germ scout
  `research_c409_c413/positive_characteristic/CANDIDATE_SCREEN.md` (PC-E),
  the failed global-forward scouts in
  `continuation_c414_c418_round2/forward_charp/`, C408's finite-field
  orbit-product lift, and C410's inverse tower. Lindahl–Rivera-Letelier
  [arXiv:1501.03965v2](https://arxiv.org/abs/1501.03965v2) own the minimal
  iterative-residue criterion. Here $i_0=1$ and the iterative residue is
  $1-1=0$, so that specific minimal case is deliberately excluded.
  Laubie–Saïne and Nordqvist remain important possible owners of the
  nonminimal continuation; their exact hypotheses must be checked.
- **Proposed residual increment:** an all-prime, all-$b$ classification
  after those owners are deducted, not the observation that the residue
  vanishes and not a table of several $p$-iterates.
- **Cheap falsifier and success test:** first source-check whether the whole
  question reduces to an established theorem plus one bounded coefficient;
  then, only if needed, compute $i_1$ for all $b\in\mathbb F_5$ and
  $\mathbb F_7$ with explicit truncation and unresolved cases labelled.
  Exceptional strata outside the source theorem disprove uniform generic
  extrapolation; a short classical classification fails the paper gate.
- **Replacement boundary:** do not drop exceptional $b$, freeze a convenient
  jet cutoff as a theorem, or relabel inverse ramification as forward time.
  If the complete family is unresolved or routine, stop this contract;
  an unrelated replacement would require a newly frozen question.

## PC-D: finite-field rank-two Drinfeld point dynamics

- **Object and full family:** $A=\mathbb F_q[T]$, every prime power $q$,
  every finite $A$-field $L=\mathbb F_{q^s}$ with structural image
  $T\mapsto\theta\in L$, and every rank-two Drinfeld module
  $\phi_T(X)=\theta X+gX^q+\Delta X^{q^2}$, with $g\in L$ and
  $\Delta\in L^\times$. Include ordinary and supersingular modules.
- **Domain and clock:** for each $r\ge1$, the finite point module
  $M_r=\phi(\mathbb F_{q^{sr}})$; for every $a\in A$, the ordinary
  iterate of the self-map $\phi_a:M_r\to M_r$.
- **Observable:** all ordinary finite-set fixed counts, exact periods and
  preperiod distributions, expressed uniformly through module invariants;
  no conflation with inseparable polynomial degree or geometric torsion length.
- **One question:** obtain the complete cycle/preperiod law for every $r,a$
  from the Frobenius/module structure, including nonsemisimple and
  characteristic-primary components, and identify any nonclassical residual.
- **Intrinsic arithmetic and bridge:** the $A$-action, structural prime,
  Frobenius and invariant factors are intrinsic. These are source A1 data;
  replacing rank one by rank two supplies no target A2 bridge by itself.
- **Ownership to subtract:** C389's full Carlitz torsion/module-cycle tower,
  C409's wild additive/FAD mechanism, standard finite PID-module structure,
  and primary Drinfeld structure work. In particular
  [Mohamed Ahmed, arXiv:math/0412368v5](https://arxiv.org/abs/math/0412368v5)
  studies rank-two finite-point module structure, and
  [Leudière–Scheidler, arXiv:2602.03803v1](https://arxiv.org/abs/2602.03803v1)
  explicitly addresses submodules of points for general Drinfeld modules.
  Abstract access is not asserted to verify an unseen theorem's hypotheses.
- **Proposed residual increment:** a genuinely new complete arithmetic
  classification not recovered from invariant factors and existing
  Frobenius/submodule algorithms. A larger rank, matrix or computed table
  alone is explicitly insufficient.
- **Cheap falsifier and success test:** check whether
  $M_r\simeq\bigoplus_j A/(d_j)$ gives every required count directly by
  the kernels of $a^u(a^v-1)$, while the primary literature already gives
  the $d_j$. If so, reject as classical reconstruction without computation.
- **Replacement boundary:** do not turn this into a generic algorithm paper,
  restrict to semisimple/good primes, omit extension fields, or silently
  change to inverse torsion height. Stop unless a separate nonclassical
  complete question is frozen and justified.

## PC-H: genuinely coefficient-twisted Hénon–Frobenius return

- **Object and full family:** every odd prime power $q\ge3$,
  $a,c\in\mathbb F_{q^2}^\times$, and
  $H_{a,c}(x,y)=(y,y^q+cy^2-ax)$, with coordinate $q$-power Frobenius
  $\Phi_q(x,y)=(x^q,y^q)$. The native map is
  $S_{a,c}=H_{a,c}^{-1}\circ\Phi_q$, including all coefficient choices;
  the genuinely twisted stratum has at least one coefficient outside
  $\mathbb F_q$.
- **Domain and clock:** $\mathbb A^2(\overline{\mathbb F}_q)$, with the
  ordinary powers $S_{a,c}^n$, $n\ge1$. The clock is not replaced by
  $H^{-n}\Phi_q^n$, nor by a $q^2$-Frobenius clock.
- **Observable:** $N_n(a,c)=\#\operatorname{Fix}(S_{a,c}^n)$ of ordinary
  geometric points. Finiteness and reducedness must be established before
  any elimination degree is called this count.
- **One question:** determine the full all-$n$, all-$(a,c)$ count law,
  including descent/conjugacy and exceptional coefficient strata, and
  test whether Frobenius twisting creates a genuinely new complete family.
- **Intrinsic arithmetic and bridge:** coefficient descent and its Frobenius
  cocycle are intrinsic. A closed native count is source arithmetic only;
  no target spectral/zero/Euler/root-number or functional-equation bridge
  has been constructed.
- **Ownership to subtract:** C401's nonresonant Hénon–Frobenius intersection,
  C404's $\mathbb F_q$-coefficient sub-$q$ resonant formula, and C415's
  $2p$-perturbation family. The present nonlinear degree is still two;
  the intended change is coefficient-Frobenius noncommutation, not another
  degree threshold. Twisted Lang–Weil/trace machinery is a possible general
  owner but an asymptotic in Frobenius size is not automatically this exact
  all-native-period resonant law.
- **Proposed residual increment:** an exact, complete coefficient-twisted
  law not conjugate to the owned base-field cases, with an honest account
  of any surviving semilinear arithmetic. Losing commutation alone is
  neither novelty nor an admitted theorem.
- **Cheap falsifier and success test:** explicitly derive the native
  two-step map and diagonal-conjugacy/descent conditions; test fixed counts
  at $n=1,2$ over $\mathbb F_9$ coefficients by bounded exact elimination
  if symbolic screening does not already settle the issue. A base-change
  conjugacy to C404, or dependence on exceptional coefficients not addressed
  by a complete mechanism, blocks admission.
- **Replacement boundary:** do not retain the invalid equality
  $S^n=H^{-n}\Phi_q^n$, discard exceptional coefficients, replace the
  native clock, count a finite sample as a geometric all-$n$ theorem, or
  claim a target A2 bridge from a source zeta function.

## Screening record and dispositions

The question scopes above were frozen before the new exact checks. The
formal-disc point action has subsequently been spelled out to avoid confusing
it with precomposition acting on the power-series ring. No parameter or clock
was replaced. The only further computational refinement was to keep $b$
symbolic in the same two characteristics, because a prime-field-only sample
cannot see all allowed finite-extension coefficients.

| Contract | Decisive evidence | Recommended disposition |
|---|---|---|
| PC-F | The minimal-residue theorem deliberately does not apply. Exact $p=7,b=6$ gives $i_1=22$, while the other six prime-field values give 15. Nonconstant leading-coefficient polynomials also force finite-extension exceptions. | **HOLD / NOT ADMISSIBLE:** the complete exceptional all-prime family is unclosed; no generic stratum is promoted. |
| PC-D | Finite PID-module decomposition gives every requested count; current primary work explicitly supplies point-module and torsion algorithms. | **REJECT AS CLASSICAL RECONSTRUCTION:** no residual paper-level question in the frozen observable. |
| PC-H | A short semilinear repair restores C404's exact leading-degree mechanism for the correct native clock, even without coefficient commutation. | **REJECT AS STANDALONE PAPER:** retain the scope-extension observation, not a new five-paper slot. |

### PC-F: what the new falsifier actually establishes

The exact script computes in $\mathbb F_p[z]/(z^M)$, using both left and
right composition orders. No coefficient preceding the reported leading
term is discarded by the cutoff. For $p=5$, all five $b\in\mathbb F_5$
have $i_1=11$. For $p=7$, $b=0,\ldots,5$ have $i_1=15$, but $b=6$
has $i_1=22$. All are exact valuations, not lower bounds from a zero jet.

Keeping $b$ indeterminate gives the following exact first terms:

\[
\begin{aligned}
f_b^5(z)-z
 &= (3+4b^2+4b^3)z^{12}+O(z^{13}) &&\text{in }\mathbb F_5[b][[z]],\\
f_b^7(z)-z
 &= (4+2b+6b^2+2b^3+b^4)z^{16}+O(z^{17})
 &&\text{in }\mathbb F_7[b][[z]].
\end{aligned}
\]

The first polynomial is cubic with no root in $\mathbb F_5$ (the exact
prime-field evaluations are nonzero), so it has roots in $\mathbb F_{125}$.
Those allowed parameters cannot have $i_1=11$. Thus even the uniformly
positive $\mathbb F_5$ sample cannot support the frozen full family.
The second polynomial vanishes at $b=6$, where the longer jet detects the
next actual leading term at degree 23. These facts decisively refute a
coefficient-uniform generic first-jump guess; they do not classify the
remaining coefficients or all higher jumps.

Nordqvist's [latest arXiv v3](https://arxiv.org/html/1909.10782v3),
Theorems A/B, requires a starting ramification index larger than $p$,
whereas this germ starts with $i_0=1$. Applying such results to $f_b^p$
would first require the appropriate residue data on every exceptional
stratum. The Laubie–Saïne continuation threshold is relevant to many first
jumps, but the original full text was not accessed successfully, and the
accessible later restatement has an indexing inconsistency. No full tower
formula is imported from that inconsistent display. This is an access and
closure limitation, not a claim that the classical theorem is false.

The unmet scientific task is an all-prime classification of the coefficient
strata and their higher ramification, followed by an explicit deduction of
the stated finite-disc point cycles. Neither a list of small primes nor the
already-owned minimal-germ/finite-quotient framework fills that gap. No
further census or proof scaffold was launched.

### PC-D: complete collision certificate

Write the finite point module as $M_r\simeq\bigoplus_j A/(d_j)$, using its
actual invariant factors, without any squarefreeness assumption. For

\[
K(u,v)=\#\{x\in M_r:\phi_a^{u+v}(x)=\phi_a^u(x)\},
\qquad u\ge0,\ v\ge1,
\]

the elementary PID kernel formula gives

\[
K(u,v)=q^{\sum_j\deg\gcd(d_j,a^u(a^v-1))}.
\]

Here $a^0=1$, including $a=0$, and $\gcd(d,0)=d$. In particular

\[
\#\operatorname{Fix}(\phi_a^v)
=q^{\sum_j\deg\gcd(d_j,a^v-1)}.
\]

For a fixed $u$, Möbius inversion of $K(u,v)$ gives the number with
preperiod at most $u$ and exact eventual period $v$; subtracting the
corresponding $u-1$ quantity gives exact preperiod $u>0$. Taking $u=0$
and dividing exact-period points by $v$ gives cycle counts. Thus the
displayed observable, including all primary factors and nilpotent pieces,
contains no information beyond the finite module and elementary inversion.

[Leudière–Scheidler v1](https://arxiv.org/html/2602.03803v1), §2.5.1 and
Algorithm 5, supply precisely the point-module decomposition; §4.1.2
explicitly computes torsion through gcds with its invariant factors.
Their algorithms are not claimed here as new, independently benchmarked,
or error-free in every displayed implementation detail. Their directly
read mathematical module framework plus the elementary kernel identity
already settle the ownership collision. No Drinfeld numerical check was
needed. C389 had already used the rank-one instance locally.

### PC-H: why genuine twisting still fails the substantive-increment gate

The bounded semilinear reduction is recorded in
[SEMILINEAR_REDUCTION.md](SEMILINEAR_REDUCTION.md). It identifies the correct
native cocycle and explains exactly which parts of the existing
[C404 proof](../../continuation_c404_c408_round2/henon_resonance/PROOF_PACKAGE.md)
carry over. It does not edit or retroactively enlarge the frozen C404 claim.

The new exact checks use $\mathbb F_9=\mathbb F_3[\eta]/(\eta^2+1)$ with

\[
(a,c)=(\eta,1+\eta),\qquad (a,c)=(1,\eta).
\]

For each, the correct twisted fixed-equation pairs at $n=1,2,3$ have
coprime leading monomials of degrees $(3,2),(9,6),(27,14)$, giving quotient
lengths $6,54,378$. The script also checks semilinear commutation and the
characteristic-three binomial identity; it verifies the native two-step
equation equivalence on every one of the 81 $\mathbb F_9$-points. This
last check is not used as a geometric point census.

The important outcome is not numerical agreement. Both semilinear operators
act on coefficients in the same way, so the leading-degree and
$p$-divisibility argument is the same one already owned by C404. The
coefficient-field extension is a useful correction to an overly strong
intuition that noncommutation must create a new count law; it is not
substantial enough by itself to justify a separate paper.

## Deliverables and boundary

- [SOURCE_AUDIT.md](SOURCE_AUDIT.md): bounded primary-source access,
  applicability, local ownership and unsuccessful-access record.
- [SEMILINEAR_REDUCTION.md](SEMILINEAR_REDUCTION.md): short collision/scope
  reduction, not a manuscript or standalone admitted proof contract.
- [exact_screen.py](exact_screen.py) and [CHECK_RESULTS.md](CHECK_RESULTS.md):
  newly scoped exact falsifiers and actual results, with finite limitations.

No old accepted test or build was rerun. No full new proof package,
manuscript, formal Route A evaluation, seal, commit or state/index mutation
was made by this lane. All three source-side carriers lack an independent
target A2 bridge. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional; no
Euler, root-number, automorphy, functional-equation or Hilbert–Pólya target
claim is licensed by these calculations. The coordinator retains the final
admission decision; this lane recommends **zero** first-pass admissions.
