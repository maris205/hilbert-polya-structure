# Harmonic delta-comb: bounded broader-source ownership check

Date: 2026-09-05. Independent current-team source check, not a proof review,
external referee report, novelty certificate, or Route-A evaluation.

## Outcome

**Zero matching high-energy counting theorems were confirmed in this bounded
source set.** The inspected results directly own self-adjointness, discreteness,
and the connection with Jacobi operators; they do not provide the candidate's
explicit two-term count with its logarithmic error. The complete text of the
Albeverio–Kostenko–Malamud 2010 form paper was not retrieved. Its authors' later
review supplies the precise reproduced discreteness theorem, but this is not a
claim that the inaccessible original paper has been checked line by line.

Thus the existing audit's conclusion remains: the counting law is a proposed
increment not found in the inspected literature, not certified globally new.
The broader-source gap is narrowed, not eliminated universally.

## Frozen question

The candidate uses Dirichlet boundary condition at zero,
$x_n=\pi H_n$, $d_n=x_n-x_{n-1}=\pi/n$, and constant finite
$\alpha_n=\kappa>0$ in

\[
q_\kappa[f]=\int_0^\infty |f'|^2\,dx+
\kappa\sum_{n\ge1}|f(x_n)|^2.
\]

The specific ownership target is, for each fixed $\kappa$ and every sufficiently
large real $k$, with inclusive eigenvalue counting,

\[
N_\kappa(k^2)=2k\log k+
\bigl[\log(4\pi/\kappa)+\gamma-2\bigr]k+O_\kappa(\log k).
\]

Inputs read: `delta_comb/SOURCE_AUDIT.md` in full and only the claim, assumptions,
and definitions at the start of `delta_comb/PROOF_PACKAGE.md`, not its proof.
At the check their SHA256 values were, respectively,

```text
e631d63a54436d5ab93baab30a04ccd6304d977e59b44e04b517eec0a23b9373
7a63727caee39ba2926e2fe93dd249df17ea9ec4ba5ddf7b760432f02898b0af
```

## Three-work access ledger

The budget was kept to two original research papers and one same-author review
used to recover the inaccessible form theorem; the review is not mislabelled as
a third original result. All mathematical source statements below use primary
author/publisher material, not third-party summaries.

| Work | Actual access and locator | Effect on the counting claim |
|---|---|---|
| Kostenko–Malamud, *1-D Schrödinger operators with local point interactions on a discrete set*, JDE **249** (2010), 253–304, DOI `10.1016/j.jde.2010.02.011` | Actual 54-page arXiv PDF text: contents/introduction; Proposition 2.4, Theorem 5.4, Example 5.12, Theorem 5.17, Proposition 5.18 | Direct shrinking-spacing and Jacobi/discreteness owner; no matching counting formula in inspected statements |
| Albeverio–Kostenko–Malamud, *Spectral theory of semibounded Sturm–Liouville operators with local interactions on a discrete set*, JMP **51** (2010), 102102, DOI `10.1063/1.3490672` | Official repository metadata and publisher abstract/reference page; publisher PDF request redirected to an abstract-only page | Original full-text exclusion is **not** complete; exact reproduced criterion checked in next row |
| Kostenko–Malamud, *1-D Schrödinger operators with local point interactions: a review*, PSPM **87** (2013), 235–262 | Actual 27-page arXiv v1 text: §2.4–§2.5, Theorems 2.13/2.20, Corollary 2.21, equations (2.24), (2.27)–(2.29), reference [6] | Explicitly reproduces the form paper's discreteness criterion; no high-energy two-term assertion in these passages |

### 1. What the Jacobi paper actually says

Theorem 5.4 identifies deficiency indices, not the positive eigenvalues of the
two operators. Theorem 5.17 says that, in the self-adjoint case, discreteness of
$H_{X,\alpha}$ is equivalent to $d_n\to0$ plus discreteness of the associated
Jacobi operator. Proposition 5.18 gives sufficient discreteness conditions
$|\alpha_n|/d_n\to\infty$ and
$\lim 1/(d_n\alpha_n)>-1/4$. Example 5.12 explicitly studies $d_n=1/n$,
including positive couplings. These are not merely title-level matches.
[Actual primary PDF](https://arxiv.org/pdf/0908.3542)

The preprint uses a Neumann condition at zero, whereas the candidate is
Dirichlet. This difference must be stated; changing one regular separated
endpoint condition preserves discreteness and changes counts by at most one
through interlacing. It cannot turn a discreteness criterion into an asymptotic.

The general spectral correspondence in Proposition 2.4 involves the
energy-dependent operator $\Theta-M(z)$, not an identification
$E_j(H)=E_j(B)$. Consequently an asymptotic for a fixed Jacobi matrix cannot
silently be transferred to the candidate. This is the checker's applicability
inference, not a new theorem claimed by that paper.

### 2. Original form-paper access limitation

The [TU Dublin repository item](https://arrow.tudublin.ie/scschmatart/94/)
states that the document is currently unavailable there. Its metadata and the
[publisher-provided page reached by the PDF link](https://pubs.aip.org/aip/jmp/article-pdf/doi/10.1063/1.3490672/15605418/102102_1_online.pdf)
describe form methods, self-adjointness, Molchanov discreteness, continuous
spectrum stability, negative spectrum, and Jacobi applications. The retrieved
publisher page contains the abstract and references, **not** the body.

Crossref's publisher-deposited metadata was successfully read over HTTPS and
provided that exact version-of-record PDF link. A direct browser request for
the article failed; the PDF link redirected to the publisher's abstract page.
Neither this redirect nor the page's length is counted as full-text access.
No original-paper theorem number is invented from the later review's numbering.

### 3. Exact form criterion and application to this model

In the [authors' arXiv review](https://arxiv.org/pdf/1303.4055), printed p.11,
Theorem 2.20 credits reference [6], the AKM 2010 paper. Assuming uniformly
bounded unit-interval mass of both negative parts as in (2.24), the lower
semibounded operator has discrete spectrum precisely when, for every
$\varepsilon>0$,

\[
\int_x^{x+\varepsilon}q(t)\,dt+
\sum_{x_n\in[x,x+\varepsilon]}\alpha_n\longrightarrow+\infty.
\]

Corollary 2.21 gives the sufficient condition
$d_n\to0$ and $\alpha_n/d_n\to+\infty$ when $q$ is bounded.
Here $q=0$, both negative parts vanish, and
$\alpha_n/d_n=\kappa n/\pi\to\infty$. Thus this criterion genuinely applies
and owns compact-resolvent/discreteness information for the harmonic chain.
The review's definition (2.3) uses the candidate's Dirichlet condition.

This is a qualitative compactness test, not a phase integral or eigenvalue
asymptotic with a remainder. In particular its statement has no energy scale,
no second counting coefficient, and no error term to specialize. The finite
positive constant $\kappa$ must not be confused with a strong-coupling limit
or with a negative-eigenvalue counting parameter used elsewhere in the review.

## What remains necessary for a direct collision

A directly owning general theorem would need hypotheses valid for the atomic
positive measure $\kappa\sum_n\delta_{\pi H_n}$ and a conclusion strong enough
to recover both the displayed linear coefficient and the $O_\kappa(\log k)$
error. Merely proving $N(E)\to\infty$, compactness, comparable growth rates,
a Schatten condition, or an energy-dependent Jacobi reduction does not do this.
No such statement was confirmed here. The candidate's own quantitative
comparison argument was not reviewed or reproduced in this source check.

## Search and scope receipt

Used the `research-lit` skill. No Zotero/Obsidian tool was available; local
filename filtering found no relevant named AKM/KM PDF in `papers/`, and
`literature/` is absent. No `arxiv_fetch.py` was present in the checked project
tools/installed arXiv skill locations, so the skill's web-search fallback was
used. Actual arXiv metadata and relevant PDF text were then accessed online;
no PDFs or other source files were written to the worktree.

Queries combined author names with `dense`, `1/n`, `point interactions`,
`eigenvalue asymptotics`, `counting function`, and the exact 2010 form-paper
title/DOI. Discovery snippets about finite-center resonances, delta-prime
operators, and other dimensions were not treated as applicable theorems and
were not expanded into additional paper reviews. Full-text token searches for
`asymptot` in the two retrieved arXiv texts returned no match; this is only
auxiliary search evidence, not a proof of absence.

No unrestricted citation descent, target proof review, numerical rerun, Git
operation, paid access, external review, or additional file edit was performed.
The result does not establish a target Euler product, root number,
zero/divisor correspondence, or Hilbert–Pólya realization.
