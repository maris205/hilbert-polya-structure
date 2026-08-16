# HCS-C59 derivation

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

This document derives the locked formulas from the exact premises certified
by the promoted C59 machine tuple. The producer/checker chain has
`PREFREEZE_CODE_RESULTS_PASS`, and its independent post-refresh hostile audit
has `POSTREFRESH_PASS`; the updated 13-root formal package has an independent
`FORMAL_DOCS_PASS`.

## 1. Group and field degrees

The exact subgroups satisfy

\[
|G|=51840,\qquad |H_+|=|H_-|=162,\qquad [G:H_\pm]=320.
\]

C59-EXACT-1 proves that each canonical scaled integral orbit sum
$\eta_\pm$ has 320 distinct conjugates. Since it is fixed by $H_\pm$,

\[
\operatorname{Stab}_G(\eta_\pm)=H_\pm,\qquad
\mathbf Q(\eta_\pm)=K^{H_\pm}.
\]

The optional unscaled invariant is $\widetilde\eta_\pm$, with
$\eta_\pm=L^2\widetilde\eta_\pm$. Both generate the same field, but only
the scaled (eta) is used for the integral product resolvent and modular
coefficient hashes.

## 2. Normal closure and nonisomorphism

For (F=K^H), the normal closure inside (K) is fixed by
$\operatorname{Core}_G(H)$. Both cores are trivial, so both normal closures
are $K$. A $\mathbf Q$-isomorphism $F_+\to F_-$ would extend to an
automorphism of an algebraic closure, preserve (K), and conjugate (H_+)
to (H_-). Their abelianizations `[2,3]` and `[2]` differ, hence the
subgroups are not isomorphic and cannot be conjugate. Thus the fields are not
isomorphic.

## 3. Zeta equality

The full rational permutation-character identity is

\[
\operatorname{Ind}_{H_+}^G\mathbf1
=\operatorname{Ind}_{H_-}^G\mathbf1.
\]

Artin formalism therefore gives

\[
\zeta_{F_+}(s)=\zeta_{F_-}(s).
\]

This equality is not deduced from sampled good primes and does not determine
the ramification-index structure of the bad local algebras.

## 4. Orbit-count conductor formula

For a finite group (J) acting on a 320-point coset carrier, write (o(J))
for the number of orbits. The codimension of fixed vectors in the permutation
module is (320-o(J)). The common orbit counts are

| subgroup | $I_3$ | $P_3$ | $Q_3$ | $I_5$ | $P_5$ | tame $C_3$ | reflection $C_2$ | $C_\infty$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| orbit count | 36 | 56 | 112 | 16 | 64 | 128 | 160 | 168 |

At 3, the C58 lower filtration gives

\[
v_3(\operatorname{Disc}F)
=(320-36)+\frac{320-56}{2}+(320-112)=624.
\]

At 5,

\[
v_5(\operatorname{Disc}F)
=(320-16)+\frac34(320-64)=304+192=496.
\]

At each tame (C_3) prime,

\[
v_p(\operatorname{Disc}F)=320-128=192,
\]

and at each reflection prime,

\[
v_p(\operatorname{Disc}F)=320-160=160.
\]

## 5. Signature and sign

Let (o=168) be the number of complex-conjugation orbits on 320 embeddings.
If (r_1) embeddings are fixed and (r_2) pairs are exchanged, then

\[
r_1+2r_2=320,\qquad r_1+r_2=168.
\]

Hence

\[
r_1=16,\qquad r_2=152.
\]

The discriminant sign is ((-1)^{152}=+1).

## 6. Exact global discriminant and support

Put

\[
q=14932047182473291995860108491583652133938007263719,
\]
\[
A=181\cdot997\cdot2346241=423395612137,
\]
\[
B=283\cdot1801\cdot q
=7610610604104534884325967676315830570581925356194091077.
\]

The preceding exponents yield

\[
\operatorname{Disc}(F_\pm)
=+3^{624}5^{496}A^{192}B^{160}.
\]

C58 proves that (K), and hence its subfields, is unramified outside
({3,5,181,283,997,1801,2346241,q\}). Every displayed exponent is
positive, so all eight primes ramify and the support is exact.

The promoted certificate rebuilds the positive 11,658-digit integer and
matches its no-newline unsigned decimal digest
`7f3ed0f731e5905f9af8254df2114ad15c2bb7d96cfa9a8b464a58ae8ea3ae70`.
The integer is not printed in the certificate.

## 7. Local factor formulas

For a decomposition group (D), inertia (I), subgroup (H), and double-
coset representative $g$, set $J=D\cap gHg^{-1}$. Then

\[
n=[D:J],\qquad e=[I:I\cap J],\qquad f=[D:IJ],\qquad n=ef.
\]

The double cosets $D\backslash G/H$ index the completion factors. If $d$
is the local different exponent, the factor contributes (fd) to the global
discriminant exponent.

## 8. ToM-140 arithmetic audit

For (F_+), the degree total is

\[
8\cdot1+10\cdot6+8\cdot9+10\cdot18=320,
\]

the factor count is (8+10+8+10=36), and

\[
8(1)(0)+10(1)(11)+8(1)(18)+10(1)(37)=624.
\]

For (F_-),

\[
4\cdot2+12\cdot3+4\cdot6+4\cdot9+12\cdot18=320,
\]

the factor count is (4+12+4+4+12=36), and

\[
4(1)(1)+12(1)(5)+4(1)(11)+4(1)(18)+12(1)(37)=624.
\]

The first degree multiset contains (1^8); the second contains no degree-one
factor.

## 9. ToM-206 arithmetic audit

For (F_+),

\[
4\cdot2+5\cdot12+4\cdot18+5\cdot36=320,
\]

the factor count is (4+5+4+5=18), and

\[
4(2)(0)+5(2)(11)+4(2)(18)+5(2)(37)=624.
\]

For (F_-),

\[
2\cdot4+6\cdot6+2\cdot12+2\cdot18+6\cdot36=320,
\]

the factor count is (2+6+2+2+6=18), and

\[
2(2)(1)+6(2)(5)+2(2)(11)+2(2)(18)+6(2)(37)=624.
\]

The first table has four `(2,1,2,0)` factors, hence four unramified quadratic
extensions. The second has no factor of degree two.

## 10. Exact local conclusion and converse firewall

An isomorphism of finite etale $\mathbf Q_3$-algebras preserves the multiset
of field-factor degrees. The differing degree multisets prove
nonisomorphism in both branches. This proves only a sufficient obstruction:
an `(n,e,f,d)` tuple does not classify a high-degree local field.

## 11. Derivation firewalls

The derivation does not select (D_3), infer expanded resolvent coefficients,
identify a maximal order, equate polynomial and field discriminants, or
derive any bad Euler/Frobenius/epsilon/root-number datum.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force. All finite inputs to this
derivation are certified by C59-EXACT-0--7 on the promoted tuple; paper,
release, and the refreshed formal-root audit are not thereby certified.

## 12. Promoted machine handoff

The exact inventory is 13 code files and 8 result files, hence 21 live
code/result leaves; the self-excluding scoped manifest has 20 entries. The
48-test source suite passed. The checker rebuilt 10,412 payload leaves,
rejected 20,894 certificate mutations and 8 self-consistent evidence-rebound
mutations, and bound the following identities:

```text
payload  a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b
shape    788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2
G0       ac445822702b5e376eed6fbfa86a4df81c7f8177ca35c8211282dca830123d5d
cert     3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a
check    271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3
schema   07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4
group    0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958
resolver 667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6
manifest c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda
```
