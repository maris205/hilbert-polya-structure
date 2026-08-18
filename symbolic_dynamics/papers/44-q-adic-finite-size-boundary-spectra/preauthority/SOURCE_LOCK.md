# Source lock

## Candidate identity

- Proposed candidate: `SD-C46` (provisional, unauthorized)
- Proposed position: `Paper 44`
- Family: symbolic dynamics / multiplicative integer systems
- Stage: temporary preauthority theory and source candidate
- Portable artifact base: the directory containing this file

## Frozen source object

Fix an integer $q\ge2$ and a finite $d\times d$ primitive matrix
$A\in\{0,1\}^{d\times d}$. Let the alphabet be
$\mathcal A=\{1,\ldots,d\}$ and define

$$
X_A^{(q)}
=\{x\in\mathcal A^{\mathbb N}:A_{x_n,x_{qn}}=1\text{ for all }n\ge1\}.
$$

For $N\ge1$, $Z_{A,q}(N)$ is the number of maps
$x:\{1,\ldots,N\}\to\mathcal A$ satisfying every constraint whose two
endpoints lie in $\{1,\ldots,N\}$. Set $Z(0)=1$.

For $\ell\ge1$ let

$$
W_\ell=\mathbf1^TA^{\ell-1}\mathbf1,
\qquad W_0=1.
$$

Thus $W_\ell$ counts ordinary $A$-admissible words of length $\ell$.
Define

$$
c_v=\log\frac{W_{v+1}}{W_v},\qquad
d_v=c_v-\log\rho(A),
$$

and

$$
h=\sum_{v\ge0}\frac{q-1}{q^{v+1}}c_v.
$$

For $N\ge1$, write

$$
E(N)=\log Z(N)-hN.
$$

The convention $E(0)=0$ is used only when forming the ordinary cutoff
generating function.

All logarithms are real logarithms of positive real numbers; the $W_\ell$
themselves are positive integers, whereas $\rho(A)$ need not be an integer.
Primitivity supplies the Perron spectral gap used in the proof.

## q-adic codomain lock

$\mathbb Z_q$ denotes the inverse limit of $\mathbb Z/q^v\mathbb Z$, even
when $q$ is composite. For $x\in\mathbb Z_q$, the notation

$$
x\bmod q^v\in\{0,1,\ldots,q^v-1\}
$$

means the canonical integer representative of its level-$v$ coordinate.
The boundary map is real-valued:

$$
E_{A,q}:\mathbb Z_q\longrightarrow\mathbb R.
$$

No $p$-adic-valued analytic function is asserted.

## Frozen golden control

The only control for which Cantor dimension and natural boundary are claimed
is

$$
q=2,\qquad
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
$$

Use $F_0=0,F_1=1$, so $W_\ell=F_{\ell+2}$. Put

$$
\varphi=\frac{1+\sqrt5}{2},\qquad
t=\varphi^{-2}=\frac{3-\sqrt5}{2},\qquad r=-t.
$$

The boundary coefficients $\gamma_k$ and the radial tails are defined in
`PROOF_PACKAGE.md`; their indexing may not be shifted silently.

## Frozen claim boundary

The strongest included scientific statement is:

> For every primitive zero-one $A$ and integer $q\ge2$, the exact order-one
> prefix remainder extends continuously to $\mathbb Z_q$ and its image is the
> complete accumulation set. For the frozen binary golden control, that image
> is a strongly separated Cantor set of dimension
> $\log2/(2\log\varphi)$, and the remainder generating function has a
> unit-circle natural boundary through dense nonzero radial singularities.

The following are excluded:

- ordinary Minkowski-content nonexistence or a continuous-scale content
  spectrum;
- nonprimitive adjacency matrices under the same theorem;
- an all-$q,A$ Cantor theorem;
- a meromorphic continuation or isolated-pole interpretation of $G$;
- determinant, orbit-zeta, or transfer-operator ownership for $G$.

## Prior-ownership lock

Zero novelty credit is assigned to:

- the multiplicative golden-mean and general multiplicative-SFT objects;
- the decomposition into $q$-adic chains;
- the product of ordinary word counts over those chains;
- Fibonacci word counts in the golden example;
- leading entropy and leading Hausdorff/Minkowski dimensions;
- boundary-complexity and surface-entropy terminology;
- Ban--Hu--Lin's direct admissible-chain pattern-count framework;
- every valid leading/boundary result of Ban--Hu--Lai, while explicitly
  correcting rather than inheriting the author manuscript's displayed
  one-dimensional $N=p^{kn}$ linear subleading formula; the
  version-of-record/erratum text is not represented as line-checked;
- Perron--Frobenius theory, elementary $q$-adic inverse limits, Binet's
  formula, and generic Cantor/Frostman arguments.

The nearest primary owners are recorded in
`LITERATURE_NOVELTY_AUDIT.md`. Absence of an exact hit is evidence grade
`B-` at best and does not establish priority.

## Allowed evidence

- the sealed Phase-2 package identified in `README.md`;
- the accepted Papers 1--43 tree only for collision and provenance checks;
- exact integer prefix enumeration and exact matrix powers;
- Perron--Frobenius spectral decomposition;
- exact modular arithmetic and inverse-limit topology;
- exact algebra in $\mathbb Q(\sqrt5)$;
- certified interval arithmetic used only as an evaluator, never as proof;
- primary arXiv, publisher, DOI, and author-manuscript sources.
- the neutral result-free `RAW_INPUT_MANIFEST.json`, independently expanded
  by each evaluator.

## Forbidden evidence and moves

- fitting $h$, $\gamma_k$, the dimension, or a pole coefficient from data;
- using one evaluator's expanded/generated fixtures, code, or expected-value
  table in the other; both may read only the neutral raw-input manifest;
- calling the known chain product or entropy a new theorem;
- treating finite numerical separation as proof of all-level separation;
- using ordinary floating point to certify a strict infinite-series bound;
- replacing $N\to\infty$ by a bounded cutoff and claiming the full image;
- calling $x\bmod q^v$ a real fractional part or a $p$-adic value;
- treating a radial singularity of the full $G$ as an isolated meromorphic
  pole;
- writing to authority, Git, mirrors, registries, or repository manifests.

## Source-integrity input

The active superseding Phase-2 manifest itself is not copied or rewritten
here. Its byte hash is

```text
d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181
```

and `sha256sum -c` returned `PASS 10/10` before candidate freeze. The earlier
`db00401b...` seal is explicitly superseded and is not accepted as a
controlling input. Any later byte change to the active input requires a fresh
provenance entry and proof replay.
