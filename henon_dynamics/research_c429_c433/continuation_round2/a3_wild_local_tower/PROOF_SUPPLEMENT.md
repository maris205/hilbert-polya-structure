# Exact pair certificate and precision argument

2026-09-09 UTC. Current author work; substantive independent review is pending. The full all-$(p,e)$ target is frozen in [REPORT.md](REPORT.md) and remains unproved.

## Claim, assumptions and status

Use the exact definitions of $K,R,P_s,Q_e,M_e,E_e,\sigma,w_e,y_e,a_e$ from the report. For the single pair $(p,e)=(3,2)$, the two recorded executions provide the following computer-assisted certificate:

$$
\operatorname{polar}(a_2)=s^{-6}+2s^{-4},\qquad
\operatorname{red}_{\mathrm{AS}}(a_2)=2s^{-4}+s^{-2}\ne0.
\tag{1}
$$

Consequently, using the accepted A4/E2 equivalence, $M_2$ is irreducible over $\overline{\mathbb F}_3((s))$ and its splitting field is totally ramified cyclic of degree $9$. This is **a single-pair computationally certified auxiliary result**, subject to independent code/proof review; it does not establish (AS-full) at other pairs or global PC424-D.

All computation is over $\mathbb F_3$ and then extends to $k=\overline{\mathbb F}_3$. The regular AS class disappears over $k[[s]]$, so only the full negative-power part is required. No point count is taken from a nonreduced special fibre.

## Dependency map

1. Accepted LRL/A3/E2 inputs specify the unique cluster $M_e$ and finite étale native torsor, without assuming local irreducibility.
2. Coprime Hensel lifting identifies its coefficients modulo $s^N$ exactly.
3. The integral multiplication matrix for $M_e'(\alpha)$ gives a determinant/adjugate pole bound and a rigorously tracked Cramer approximation.
4. Integral native substitution and integral algebra multiplication give a certified approximation to $a_e$ modulo a positive power of $s$.
5. Finite polar reduction proves (1); the already reviewed torsor criterion converts this to one local full-inertia result.

## 1. Exact finite algebra construction

The producer represents a polynomial in $z$ as a list of coefficients in $\mathbb F_3[s]/(s^N)$. It forms precisely nine native iterates, retains the third iterate, and divides the two iterate differences using monic division. The checked remainder is zero and the quotient has degree $504$.

At $s=0$, the accepted minimally ramified formula implies $Q_2(z,0)=z^9V(z)$ with $V(0)\ne0$. The code also checks this exact residue identity. Beginning with $M=z^9$, $N_0=V$, every Hensel step corrects $M,N_0$ from precision $h$ to $\min(2h,N)$.

For completeness, write the current error as $F=Q_2-MN_0\in s^hR[z]$. The correction $A$ of degree less than $9$ solves

$$
N_0A\equiv F\pmod M.
$$

The multiplication matrix of $N_0$ in $R[z]/M$ is invertible modulo $s$ by coprimality, hence invertible over the truncated coefficient ring. Gaussian elimination uses only unit pivots; the producer checks their availability. Put $B=(F-AN_0)/M$, with checked zero monic remainder. Both corrections are divisible by $s^h$, so

$$
(M+A)(N_0+B)-Q_2=AB\equiv0\pmod{s^{2h}}.
$$

The producer checks this identity after every step. The prescribed monic degrees and reductions persist. Uniqueness in coprime Hensel lifting therefore identifies the computed $M$ with the canonical $M_2$ modulo $s^N$; no factor irreducibility is assumed.

## 2. Discriminant and inverse precision

Let $\mathcal E=R[z]/M_2$, free on $1,\alpha,\ldots,\alpha^8$, and let $A$ be the $9\times9$ integral matrix of multiplication by $M_2'(\alpha)$. The exact determinant satisfies

$$
\det A=\pm\operatorname{Disc}(M_2).
$$

Write $\delta=v_s(\det A)$. A computed integral matrix $\widetilde A\equiv A\pmod{s^N}$ has determinant and adjugate congruent to those of $A$ modulo $s^N$, since their entries are integral polynomials in the matrix entries. If the first nonzero coefficient of $\det\widetilde A$ occurs at $\delta<N$, then that valuation and coefficient are exact.

The program computes the determinant as a polynomial in $\mathbb F_3[s]$ by fraction-free Bareiss elimination, not approximate floating-point arithmetic. Every division is checked to have zero polynomial remainder. At $N=1024$, it finds $\delta=144$ and leading coefficient $1$.

Let $b$ be the basis vector for $\alpha^8$, and write

$$
\det A=s^\delta d,\qquad
w_2=A^{-1}b=s^{-\delta}W,
\qquad W=d^{-1}\operatorname{adj}(A)b\in\mathcal E.
$$

The unit $d$ is known modulo $s^{N-\delta}$, its inverse is known to that same order, and every adjugate numerator is known modulo $s^N$. Therefore the computed $\widetilde W$ determines $W$ modulo

$$
s^T\mathcal E,\qquad T=N-\delta.
\tag{2}
$$

The Cramer determinants in the code are the entries of $\operatorname{adj}(A)b$ with their correct column-replacement signs. It additionally checks

$$
M_2'(\alpha)\widetilde W=s^\delta\alpha^8\pmod{s^T\mathcal E}.
$$

Thus $w_2$ is known modulo $s^{N-2\delta}\mathcal E$ and has coordinate pole at most $\delta$. The bound is conservative; no unproved cancellation is used to reduce it.

## 3. Native substitution and complete polar precision

The matrices of $\sigma$ and multiplication in the monic basis of $\mathcal E$ have integral entries determined by $M_2$ modulo $s^N$. Define

$$
Y=-\sum_{i=0}^{8}(i\bmod3)\sigma^i(W),\qquad y_2=s^{-\delta}Y.
$$

Equation (2) therefore determines $Y$ modulo $s^T\mathcal E$. The code checks, at that precision, the trace-one and difference identities

$$
\sum_{i=0}^8\sigma^i(\widetilde W)=s^\delta,
\qquad \sigma\widetilde Y-\widetilde Y=s^\delta,
\qquad \sigma^9\widetilde W=\widetilde W.
$$

Now

$$
a_2=s^{-3\delta}\bigl(Y^3-s^{2\delta}Y\bigr).
\tag{3}
$$

All operations in the parenthesis are integral. Computing them modulo $s^T$ loses no further precision before the displayed division. Hence (3) determines $a_2$ modulo

$$
s^{T-3\delta}\mathcal E=s^{N-4\delta}\mathcal E.
\tag{4}
$$

The exact $a_2$ belongs to $K$, by the accepted trace-resolvent identity. In the monic basis its other eight coordinates are exactly zero; the code independently checks their computed vanishing modulo $s^T$. The scalar coordinate in (4), with $N-4\delta>0$, therefore determines **every negative coefficient**, not just a selected leading prefix. Its pole is at most $3\delta=432$.

For the allocated $N=1024$, $T=880$ and $N-4\delta=448$. The stronger precommitted gate $N>4\delta+8$ also passes. By contrast the first run at $N=512$ fails that gate and was correctly recorded as inconclusive; it is not retroactively relabelled successful.

## 4. Actual arithmetic result and AS reduction

The full [second execution log](execution_n1024.log) records all successful identity checks and the complete negative coefficients. Its `CERTIFIED_PAIR_RESULT` is

$$
\operatorname{polar}(a_2)=s^{-6}+2s^{-4}.
$$

The same log contains all ten coefficient lists of $M_2\bmod s^{1024}$, including its leading $1$, permitting a separate reconstruction. The SHA256 printed for their compact JSON representation is `32cc82b84a460d6982bde8e5d2406a787aab5087f0030ff9340b96b5a8fecea5`; this is a byte-integrity aid, not a replacement for mathematical checking.

Since $\wp(s^{-2})=s^{-6}-s^{-2}$, subtraction leaves

$$
2s^{-4}+s^{-2}.
$$

Both pole exponents are prime to $3$, and the coefficient at pole $4$ is nonzero. A Laurent series of negative valuation has AS image with highest pole divisible by $3$, while a regular series has regular AS image. This reduced polar polynomial is therefore nonzero in $K/\wp(K)$, proving the claimed single-pair local conclusion from the certified arithmetic.

## 5. A useful nonidentification and the remaining gap

The accepted prime-level degree-$3$ field has break $2$. The first degree-$3$ quotient of this degree-$9$ field has break $4$ by (1). Thus these particular two AS subextensions are not the same over $K$: proportional nonzero AS classes describing the same degree-$3$ extension have the same highest reduced pole. This explicitly defeats identification of the first quotient of every higher native cycle with the prime-level field. It does not defeat full inertia, which holds at the computed pair.

The entire odd-prime/all-level lemma remains **NOT CURRENTLY JUSTIFIED**: no uniform polar coefficient, induction, or vanishing classification has yet been established. Neither a second pair nor an additional precision is authorized here. Even uniform local nonvanishing would still leave the independent global native-cycle quotient problem. The result is auxiliary and is not offered as a paper or global component theorem.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
