# Hostile Review A — P111 Positive Heisenberg Word-Area Cocycles

Review date: 2026-08-29 UTC. Scope: the frozen post-Review-B manuscript,
bibliography, evidence documents, exact verifier and stored output, compiled
PDF, and the internal collision boundary. Review B's edits were preserved.
This review does not constitute an external novelty clearance.

## Verdict

**GO_INTERNAL / HOLD_EXTERNAL.**

- **CRITICAL:** 0.
- **MAJOR (mathematics):** 0.
- **MAJOR (owner/scope):** 1, repaired.
- **MINOR:** 0 new findings.

The theorem package survives independent reconstruction, including all
orientation, endpoint, parity, sign, and limiting-quantifier attacks. The
one substantive defect was an incomplete direct-owner subtraction for the
fair binary specialization. The manuscript previously cited related
random-word work but did not name the closer uniform word/lattice-path
owners. That boundary is now explicit. External circulation remains HOLD
because this audit is not an exhaustive global search.

## Mathematical reconstruction

### 1. Product order and the central coordinate

For

    H(a,b,c) H(a',b',c') = H(a+a', b+b', c+c'+ab'),

left multiplication by X sends (J,K,C) to (J+1,K,C+K), while left
multiplication by Y sends it to (J,K+1,C). With the declared chronological
product M_n=A_n...A_1, this is exactly the update for the number of earlier
Y letters followed by the new X. Thus C_n counts Y-before-X pairs, not the
opposite orientation, and M_n=H(J_n,K_n,C_n) is correct for every finite
word, including n=0.

### 2. Exact finite-word law

Splitting a word by its last letter gives

    G_(n,j)(z)=G_(n-1,j)(z)+z^(n-j) G_(n-1,j-1)(z).

This agrees with the chosen area orientation and with the Gaussian-binomial
recurrence. Every word in the j-slice has probability p^j q^(n-j), so the
displayed Bernoulli mixture is an identity of formal polynomials. The
endpoint convention 0^0=1 makes the p=0,1 formulas literal rather than
limiting shorthand.

### 3. Conditional and biased moments

Differentiating the logarithm of the Gaussian product at z=e^t gives

    E(C_n | J_n=j) = j(n-j)/2,
    Var(C_n | J_n=j) = j(n-j)(n+1)/12.

Mixing against J_n distributed as Bin(n,p) yields the displayed mean and
variance. A separate pair-incidence calculation gives, for each ordered
triple i<j<k, the three shared-index covariances

    p^3 q,  p q^3,  -p^2 q^2.

Their sum is pq(1-3pq), which recovers

    Var(C_n)
      = binom(n,2) pq(1-pq) + 2 binom(n,3) pq(1-3pq)

and simplifies to the manuscript's closed polynomial. Checks at n=0,1 and
p=0,1 give zero variance as required.

### 4. Strong law and central limit theorem

With eta_k=B_k-p, direct expansion gives

    C_n-E C_n = L_n+R_n,
    L_n = sum_k [k-1-p(n-1)] eta_k,
    R_n = -sum_(i<j) eta_i eta_j.

Summation by parts and the ordinary strong law give L_n=o(n^2); the
quadratic identity for R_n gives R_n=o(n^2) almost surely. For the CLT,

    Var(L_n)/n^3 -> pq(3p^2-3p+1)/3.

For fixed 0<p<1 this limit is positive. Individual triangular-array
summands have size O(n), whereas the standard deviation has order
n^(3/2), so Lindeberg is eventually automatic. Also E|R_n|<=npq, hence
R_n/n^(3/2) tends to zero in probability. Slutsky then proves the stated
CLT. The deterministic endpoints are separated explicitly and are not
obtained by dividing by a vanishing variance.

### 5. Matrix growth

The Frobenius identity

    ||M_n||_F^2 = 3+J_n^2+K_n^2+C_n^2

and C_n/n^2 -> pq/2 give logarithmic norm exponent two in the interior.
At p=0 or 1, one off-diagonal entry equals n and the central entry is zero,
so the exponent is one. Finite-dimensional norm equivalence transfers the
result to every fixed matrix norm. The statement is not a positive
Lyapunov-exponent claim.

### 6. Extremizers and quadratic pressure

For fixed content j, at most j(n-j) Y-before-X pairs occur, with equality
only for the monotone word Y^(n-j)X^j. Maximizing over j gives floor(n^2/4):
one balanced word for even n and two for odd n. Their total probability is
(pq)^floor(n/2), including the odd case. Zero area consists exactly of the
monotone words X^jY^(n-j), giving the stated geometric sum; the removable
p=q singularity and both deterministic endpoints are handled.

For theta>0, the exact maximizer probability supplies the lower bound and
C_n<=floor(n^2/4) the upper bound, both converging to theta/4 after division
by n^2. For theta<0, the zero-area event supplies the lower bound and one
the upper bound, both converging to zero. Theta=0 and p=0,1 are direct.
Finally pq<=1/4 makes the annealed-typical gap strict for every nonzero
theta and fixed 0<p<1.

## Owner and collision audit

### Repaired owner/scope MAJOR

The frozen draft described iid random-word work as nearby but omitted two
closer direct owners of its p=1/2 statistic:

1. Lajos Takács, “Some Asymptotic Formulas for Lattice Paths,” Journal of
   Statistical Planning and Inference 14(1), 123–142 (1986), DOI
   10.1016/0378-3758(86)90016-9, directly treats the area under a uniformly
   random north-east lattice path and its moment/limit behavior.
2. Svante Janson, “Generalized Galois Numbers, Inversions, Lattice Paths,
   Ferrers Diagrams and Limit Theorems,” Electronic Journal of Combinatorics
   19(3), P34 (2012), DOI 10.37236/2188, gives uniform random-word inversion
   interpretations, exact moments, limit theorems, and a Hoeffding
   decomposition; its binary case is this manuscript's fair law.

The metadata and scope were checked against the
[official EJC record](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v19i3p34),
the [author-deposited arXiv record](https://arxiv.org/abs/1203.6480), and
the [Takács publisher record](https://www.sciencedirect.com/science/article/abs/pii/0378375886900169).

The repair added both DOI records to references.bib and revised main.tex,
README.md, and CLAIMS_EVIDENCE.md to subtract the fair binary specialization
explicitly. The residual is now described only as the arbitrary-bias
conjunction for this matrix cocycle, its norm-exponent boundary, and its
quadratic pressure calculation—and even that wording is a scope boundary,
not a novelty claim. No theorem or verifier code changed.

### Existing owner and internal firewalls

- Canfield–Janson–Zeilberger, including the corrigendum, remain the stated
  owner boundary for fixed-content Mahonian/Gaussian-binomial asymptotics.
- Işlak–Özdemir are used for general iid random-word subsequence methods,
  not as a substitute for the closer fair-inversion owners.
- Diaconis–Hough delimit broad Heisenberg/unitriangular random-walk theory.
- P70 uses finite Heisenberg quotients and convolution nullities; P93 uses
  a reflected push-pop stack cocycle; P99 uses a deterministic shear on
  finite-index sublattices; P104 uses contracting monomial matrices and
  n-scale singular-value pressure. None has P111's update rule or observable.

## Exact-control replay

Fresh command:

    python3 code/verify.py

Result: **PASS, 421,285 assertions**, byte-for-byte identical to
code/verify.out.

- 131,071 literal binary words through length 16.
- 262,142 normal-form assertions and 131,071 norm identities.
- 153 histogram slices and 306 Gaussian-recurrence assertions.
- 231 biased rational cases, 693 biased-moment assertions, and 231
  independent pair-covariance assertions.
- 24,573 words in the centered-decomposition lane, totaling 24,612 lane
  assertions.
- 300 asymptotic-algebra identities, 600 endpoint checks, 430 extremal
  checks, and 594 pressure-bound checks.

The verifier uses exact integer/Fraction arithmetic and no sampling. Its
literal matrix, word scanner, recurrence, and pair-covariance routes are
useful independent falsification lanes inside one program; they are not a
formal proof and do not establish asymptotic convergence or novelty.

## Build and visual audit

The complete sequence

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

exited zero. The final main.log/main.blg scan has no warning, undefined
citation/reference, overfull or underfull box, multiply-defined label, or
error. An additional deterministic pass reproduced the same PDF hash.

    pages=7
    bytes=316032
    sha256=b8e12c56d072ef7e3fa7fe6c478256f6fbeb6da2dc37126453e079174c5c4476
    pdftotext_layout=25570 bytes, 397 lines
    fonts=21, all embedded/subsetted/Unicode-mapped

All seven pages were freshly rendered at 150 dpi and inspected. There is no
clipping, overlap, orphaned heading, broken citation, malformed display, or
illegible reference. References start and finish on page 7.

## Residual risks and release gate

1. A specialist search for direct treatment of the arbitrary-p Bernoulli
   inversion law and of the exact n^2 pressure should precede any external
   claim. Search absence is not evidence of priority.
2. Much of the finite-word law and fair-law asymptotics is classical. The
   contribution density therefore rests on the owner-subtracted conjunction,
   not on the individual inversion formulas.
3. The probabilistic limits fix p in (0,1); no uniform-in-p or varying-p
   theorem is stated.
4. The exact verifier is finite and single-language. It strongly attacks
   transcription/orientation errors but cannot certify the asymptotic
   arguments or literature completeness.

Accordingly, the mathematical and reproducibility gate is
**GO_INTERNAL**, while posting, submission, specialist contact, and any
novelty or priority statement remain **HOLD_EXTERNAL**.
