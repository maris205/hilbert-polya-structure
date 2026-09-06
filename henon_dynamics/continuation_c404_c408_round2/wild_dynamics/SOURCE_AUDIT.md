# Source ownership and bounded novelty audit

2026-09-06. Primary-source body checks only. This is not an exhaustive
2026 priority certification and not a claim to have performed human peer
review. arXiv bodies and official publication metadata are distinguished.

## Sources actually used

| ID | Source and stable publication identity | Body passage actually checked | Owned input and applicability boundary |
|---|---|---|---|
| S1 | Andrew Bridy, *Transcendence of the Artin–Mazur zeta function for polynomial maps of A¹(F̄_p)*, Acta Arith. 156 (2012), 293–300, DOI 10.4064/aa156-3-6 | [arXiv:1202.0362](https://arxiv.org/pdf/1202.0362), Theorem 1 and power-map count proof; [publisher metadata](https://www.impan.pl/shop/en/publication/transaction/download/product/83489) | Separable power-map zeta transcendence is already owned. Applies to A's exact conjugacy curve, not automatically to its complement. |
| S2 | Andrew Bridy, *The Artin-Mazur Zeta Function of a Dynamically Affine Rational Map in Positive Characteristic*, J. Théor. Nombres Bordeaux 28 (2016), 301–324, DOI 10.5802/jtnb.941 | [arXiv:1306.5267v2](https://arxiv.org/pdf/1306.5267), Theorems 1.2/1.3, Definition 2.2, §§2–5; [official published article](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.941/) | The five dynamically affine families and their ordinary zeta results are classical inputs. We independently exclude them for B's H=1+x, p odd. |
| S3 | Jonas Nordqvist and Juan Rivera-Letelier, *Residue fixed point index and wildly ramified power series*, J. London Math. Soc. 102 (2020), 470–497, DOI 10.1112/jlms.12325 | [arXiv:1904.04494](https://arxiv.org/pdf/1904.04494), Definition 1, §1.2, equation (1.5), Theorem 2, proof at §3.2, §6 Example 2; [official metadata](https://doi.org/10.1112/jlms.12325) | Odd p, 1≤i0≤p−1 and resit≠0. Applied to q=p−1 only. The q in this theorem is multiplicity minus 1, not the order of an unrelated multiplier. |
| S4 | Jonas Nordqvist, *Wildly ramified power series with large multiplicity*, J. Number Theory 225 (2021), 174–197, DOI 10.1016/j.jnt.2021.01.019 | [arXiv:1909.10782](https://arxiv.org/pdf/1909.10782), Definition 2.2, Proposition 2.5, §2.2 and Theorem A; [official metadata](https://www.sciencedirect.com/science/article/pii/S0022314X21000548) | For q>p, p∤q, lowest second-residue nonzero forces the specified full ramification sequence. Applied to q=mp−1 with m≥2. This is not a newly proved general ramification theorem. |
| S5 | Shankar Sen, *On automorphisms of local fields*, Ann. of Math. 90 (1969), 33–46, DOI 10.2307/1970680 | [official publication metadata](https://annals.math.princeton.edu/1969/90-1/p04); the p|i0 identity is actually read in S3 §1.2 and S4 §2.2 | Do not claim to have read Sen's full original article. Classical identity i_r=p^r i0 when p|i0 is used at 0 with i0=p m0. |
| S6 | Alon Levy, *The McMullen Map in Positive Characteristic*, arXiv:1304.2834 | [author's arXiv body](https://arxiv.org/pdf/1304.2834), introduction and Example 1.4 | Constant-derivative families ψ(x^p)+a x have constant finite periodic multipliers a^n. This observation for C is already owned; large-characteristic generic finiteness does not apply to degree 2p in characteristic p. No unverified journal metadata supplied. |
| S7 | Jakub Byszewski, Gunther Cornelissen, Marc Houben, with Appendix B by the authors and Lois van der Meijden, *Dynamically affine maps in positive characteristic*, Contemp. Math. 744 (2020), 125–156, DOI 10.1090/conm/744/14982 | [arXiv:1904.04942](https://arxiv.org/pdf/1904.04942), §§1.2–1.4, Theorem A, §2 Proposition 2.1 and holonomic discussion; [institutional published PDF](https://dspace.library.uu.nl/bitstream/handle/1874/411518/Dynamically_affine_maps_in_positive_characteristic.pdf?isAllowed=y&sequence=1) | Tame zeta means restrict the ordinary time sum to p∤n. It does not mean first-return intersection weights. Non-holonomic dynamically affine zeta results and p-primary generating-function decomposition are established precedent, not ours. |

Version caution: Bridy arXiv:1306.5267v2 numbers the ordinary-count conjecture
1.6; the published PDF numbers it 1.4. No silent theorem-number transfer
between versions is made. S7's author line distinguishes the main authors
from the appendix collaboration. Publication volume year is not inferred
from a web indexing or repository crawl date.

## Claim ownership matrix

| Proposed statement | What the sources already supply | What is calculated here | Audit status |
|---|---|---|---|
| A's power-conjugacy boundary | S1/S2 cover power maps | Critical-point calculation gives exact a^p=b^{p−1} curve | Valid exclusion, not a paper claim |
| A's original fixed point has mult p^{v_p(n)+1} | S3 Theorem 2 | index=−b^{p−1}/a^p | Direct local corollary; no independent retention |
| B's every nonzero return has p-primary multiplicity growth | S3 for q=p−1; S4 for q=mp−1>p | The logarithmic form forces iota_1=−(ac)^{−p} regardless of all higher terms | Full derivation supplied; scientific novelty still requires non-author judgment |
| B's global first-return weighted W_n | Degree of f^n−id and classical cycle decompositions | Exact triangular p-primary inversion with the origin contribution removed | A proposed full-family corollary, not read directly in the checked sources |
| B's Z_w and its analytic nature | S7 is precedent for tame/full decomposition and natural-boundary methods | Own explicit product and noninteger residues at d^{−1/p^j} μ_{p^j} | Mathematically derived; not evidence of priority merely because formula differs |
| B's H=1+x is genuinely non-dynamically-affine | S2 classification | Degree, local critical degree/count, and totally invariant point arguments | Proof provided, p=2 explicitly excluded |
| W_n equals ordinary nonzero count throughout the H-family | No source used to justify this | Exact counterexample p=3,H=1+x+x²,n=2 gives 15 versus 13 | REJECTED claim; must never silently import |
| C's multiplier spectrum is constantly 1 | S6 Example 1.4 | g is the specialization ψ(t)=t²,a=1 | Existing mechanism; not new |
| C inherits B's p-multiplier law | No such source theorem | Lowest second residue vanishes; exact origin multiplicities contradict that extension | REJECTED extension |

## Literature-search scope and stop rule

Searches included the Bridy ordinary-zeta conjecture and non-affine maps,
q-ramified series, residue/second-residue criteria, log-differential
preservation, first-return multiplicity weighted zeta, and the exact
polynomials x+x^{p+1} and x+x^{2p}. Body evidence is supplied above for the
claims actually used. Weak search hits, textbooks mirrored without verified
ownership, ResearchGate snippets, and unrelated finite-field permutation
problems are not treated as proofs or as novelty clearance.

S3's q-ramified criterion must not be confused with the multiplier-order q
in Lindahl–Rivera-Letelier, *Generic parabolic points are isolated in
positive characteristic*, arXiv:1501.03965. That paper was consulted during
routing but is not used for the mp−1 local formula here. S4 was found
specifically to close the large-multiplicity case instead of extrapolating
S3 beyond its q≤p−1 range.

No checked source states this exact first-return weighted theorem for all
f=xH(x)^p, H(0)=1, and no direct known result was found that identifies its
W_n with ordinary periodic counting. These are bounded observations about
the search, not a universal claim of novelty. The strongest remaining
scientific risk is that the full result is an immediate, useful but
paper-insufficient corollary of S3/S4 plus standard divisor inversion.

## Required non-author review questions

1. Are all local hypotheses, especially odd p and the m=1/m≥2 split,
   correctly matched to S3/S4?
2. Does the residue and first-return inversion genuinely define one natural
   full-period observable rather than disguising scheme length as point
   count? The explicit 13/15 example must remain visible.
3. Does the weighting theorem already exist under another name such as a
   ramification-weighted or local-intersection dynamical zeta?
4. Is the calculation enough to merit an independent paper under this
   batch's substantive-novelty threshold, or should it remain a research
   lemma without a C-number?

Until that review, formal retained paper count is zero. No arithmetic
prime-local Euler factors, bad-prime data, root numbers, or target-zero
correspondences are licensed by this audit.
