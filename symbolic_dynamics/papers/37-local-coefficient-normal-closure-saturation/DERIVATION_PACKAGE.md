# Paper 37 derivation package — SD-C39

## 1. Frozen affine shift and coefficient object

Fix `r>=2` and the formal-reverse right Cayley graph of

```text
M_r=<u,v | vu=u^r v>+.
```

The cyclically nonbacktracking Hashimoto rule permits `e -> f` precisely when
`t(e)=o(f)` and `f` is not the formal reverse of `e`, including at the cyclic
join. Paths are not identified or induced. One application of the shift earns
one free factor of `z`.

Assign to every oriented edge an invertible finite-dimensional transport

```text
P_e:E_o(e)->E_t(e),  P_bar(e)=P_e^(-1).
```

With the row-fiber convention, a closed word `gamma=e_0...e_(l-1)` has

```text
W_gamma=P_(e_0)...P_(e_(l-1)).
```

Changing the base edge conjugates `W_gamma`; its trace, spectrum, and complete
determinant factor are therefore orbit invariants.

## 2. Same-object trace-class ownership

For an edge based at `(b(e),k(e))`, set

```text
d_theta(e)=theta^(1+b(e)+k(e)),  0<theta<1,
D_theta=diag(d_theta(e)).
```

There are at most four oriented edges at each affine vertex, so

```text
Tr(D_theta)<=4 sum_(b,k>=0) theta^(1+b+k)
           =4theta/(1-theta)^2<infinity.
```

For a fixed connection, let `M` be the largest norm of the four generator and
inverse transports. Each matrix Hashimoto row and column contains at most
three nonzero blocks; the block Schur test gives `||H_P||<=3M`. Hence

```text
T_(P,theta)=(D_theta tensor I) H_P (D_theta tensor I)
```

is trace class on the full uninduced oriented-edge Hilbert space. It owns the
ordinary Fredholm determinant and, near zero,

```text
-log det(I-zT)=sum_(n>=1) z^n Tr(T^n)/n.
```

This establishes `SD-C39-C1`. It does not yet establish selective relation
cancellation.

## 3. Complete primitive matrix factor

For a primitive cyclic orbit `gamma`, define the positive source weight

```text
q_theta(gamma)=product_(e in gamma) d_theta(e)^2.
```

Grouping the absolutely convergent trace-log by primitive roots and
repetitions gives

```text
-log det(I-zT_(P,theta))
 =sum_[gamma primitive] sum_(m>=1)
   q_theta(gamma)^m z^(m|gamma|) Tr(W_gamma^m)/m.
```

Thus the complete ordinary Euler factor is

```text
det(I-q_theta(gamma)z^|gamma| W_gamma)^(-1).
```

For a graded fiber `E_+ direct-sum E_-`, keep the two trace-class operators
`T_+` and `T_-` distinct and define only the explicit virtual ratio

```text
Z_gr(z)=det(I-zT_-)/det(I-zT_+).
```

Its connected logarithm is

```text
log Z_gr(z)
 =sum_[gamma] sum_(m>=1) q_theta(gamma)^m z^(m|gamma|)
  [Tr((W_gamma^+)^m)-Tr((W_gamma^-)^m)]/m.
```

No first trace, scalar specialization, or cancellation between different
primitive orbits substitutes for this factor-by-factor all-orders invariant.

## 4. Ordinary deletion is nilpotence

For a finite complex matrix `W`,

```text
det(I-tW)=1
iff Tr(W^m)=0 for every m>=1
iff W is nilpotent.
```

The determinant logarithm gives the power traces; Newton identities recover
the characteristic coefficients; Cayley--Hamilton then gives `W^d=0` in rank
`d`. Conversely a nilpotent matrix has only zero eigenvalues and determinant
polynomial one.

Holonomy built from invertible transports is invertible, hence never
nilpotent. An ordinary finite-rank local system cannot delete even one
complete primitive factor. The control

```text
J=[[0,-1],[1,0]]
```

has `Tr(J)=0` but `Tr(J^2)=-2` and `det(I-tJ)=1+t^2`; it exposes the
first-trace loophole. The nilpotent control

```text
N=[[0,1],[0,0]]
```

does delete its factor, but it is noninvertible and therefore not parallel
transport. This proves `SD-C39-C2`.

## 5. Graded all-orders criterion and flat fork

For finite matrices `W_+` and `W_-`, every super-power-trace vanishes iff

```text
det(I-tW_+)=det(I-tW_-).
```

Equivalently, their nonzero eigenvalue multisets agree with algebraic
multiplicity. No diagonalizability assumption is used. For invertible
transports this is equality of the full characteristic polynomials and ranks.

A genuine local system on the filled Paper 36 Cayley `2`-complex is flat.
That complex is contractible, so every closed holonomy is gauge-conjugate to
the identity. Ordinary rank `d` retains `(1-t)^(-d)`. A graded pair of ranks
`d_+,d_-` has factor `(1-t)^(d_--d_+)`: unequal ranks retain every relation,
whereas equal ranks cancel every closed orbit. Flatness has no selective
middle branch.

## 6. Frozen non-flat shear fixture

In rank two per parity, put

```text
A=[[1,1],[0,1]],  B_c=[[1,0],[c,1]].
```

Both sectors map `u` to `A`; even maps `v` to `B_r`, odd maps `v` to
`B_(-r)`, and inverse letters receive inverse matrices. For the defining word

```text
R_r=v u bar(v) bar(u)^r,
W_c(R_r)=B_c A B_c^(-1) A^(-r),
Tr W_c(R_r)=2+c^2 r,  det W_c(R_r)=1.
```

The choices `c=r` and `c=-r` therefore have identical characteristic
polynomials. Every conjugate and every repetition of the direct relator
cancels in the graded factor.

## 7. Explicit mixed leakage

Consider

```text
M_r=bar(u)^r v bar(u)^(r-1) v u bar(v)^2.
```

It is an actual closed path based at `(r^2,0)`:

```text
(r^2,0) -> (r^2-r,0) -> (r^2-r,1) -> (0,1)
        -> (0,2) -> (r^2,2) -> (r^2,0).
```

The word is cyclically nonbacktracking. It is primitive because it contains
exactly one lowercase `u`, impossible in a proper word power. Its length is
`2r+4`, distinct from the direct relator length `r+3` and its repetitions.

Exact multiplication yields

```text
Tr W_c(M_r)
=-2c^3r^2+2c^3r-c^2r^2+6c^2r-c^2+2,
```

and hence

```text
Tr W_r(M_r)-Tr W_(-r)(M_r)=-4r^4(r-1)!=0,  r>=2.
```

The positive damping scalar cannot erase this coefficient. Thus direct
all-orders cancellation leaks on an explicit primitive mixed consequence for
every exponent in theorem scope. This proves `SD-C39-C3`.

## 8. Normal-closure saturation

Let `F=F(u,v)` and `N_r=<<R_r>>` be the normal closure. The group completion
is `G_r=F/N_r`. Every closed Cayley path has a freely reduced label in `N_r`,
and therefore admits a finite expression

```text
w=product_j a_j R_r^(epsilon_j) a_j^(-1),  epsilon_j in {+1,-1}.
```

Cancelling direct cells and their repetitions does not imply cancellation of
mixed products; the shear fixture disproves that implication. If the
obligation is strengthened to every finite mixed product of conjugated cells
and inverses, however, it applies to every closed path label. Every primitive
term in the graded trace-log vanishes, so

```text
log Z_gr(z)=0,  Z_gr(z)=1.
```

No closed primitive factor survives to carry an arithmetic label. This is
`SD-C39-C4`: partial cancellation leaks, while complete saturation erases the
ledger.

## 9. Backtrack and arithmetic firewalls

Immediate reversals are excluded before coefficients act. If they were
allowed, inverse transport would give identity holonomy, not factor deletion.
The coefficient construction cannot claim the Hashimoto rule as a success.

The shear rule cancels direct factors for balanced `r=1`, composite baseline
`r=4`, and every exponent mutation `r=2,...,8`. Random presentations also
show accidental direct-factor matches. Any surviving mixed relation residue
is therefore presentation syntax, not arithmetic recognition.

## 10. Exact-control ledger

The frozen prototype passes `131/131` checks. All eight affine direct factors
cancel, and all eight rows leak on a primitive mixed word in the bounded
census. Random one-relator controls give `9/48` direct matches and `9/9`
subsequent mixed leaks. In `2/24` paired two-relator presentations both direct
factors cancel, and both still leak. Power supertraces through order twelve
and two fresh-process scientific payloads agree exactly.

The exact rows corroborate the witness and controls; they do not prove
trace-class ownership, the arbitrary-rank nilpotence criterion, or the
normal-closure theorem.

## 11. Route consequence

- `SD-C39-C1`: same-object trace-class matrix Fredholm ownership;
- `SD-C39-C2`: ordinary factor deletion requires nilpotence;
- `SD-C39-C3`: direct graded cancellation has explicit mixed leakage;
- `SD-C39-C4`: full normal-closure saturation erases every closed factor.

Together they force

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL),
overall=ROUTE_A_REJECTED,
route_b_invocation_allowed=false.
```
