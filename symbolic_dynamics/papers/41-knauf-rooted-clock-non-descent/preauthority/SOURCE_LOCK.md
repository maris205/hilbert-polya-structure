# Source lock

## Identity

- Phase: Paper 41 Phase 1, preauthority research only.
- Proposed candidate: `SD-C43`.
- Parent historical object: `SD-C06`.
- Freeze date: 2026-08-17 UTC.
- Portable package namespace:
  `papers/41-knauf-rooted-clock-non-descent/preauthority` relative to the
  `symbolic_dynamics` root at release; the staging location is not sealed.
- Authority, mirror, Git, root README, registries, and manifests: read only.
- Chronology: six cards, results, and exact witnesses were already known when
  the retrospective selector and this contract were written.  Only corrected
  final input bytes are frozen before independent DA.

## Portable source-ID resolution contract

`SOURCE_HASHES.sha256` is a two-column SHA-256/source-ID manifest, sorted by
source ID in C byte order.  It deliberately contains no host path.  Its IDs
resolve as follows:

- `repo:<path>` resolves `<path>` from the repository root that contains
  `.git`; the resolver must reject an absolute path, `..`, a symlink escape,
  or a result outside that root.
- `dependency:P40_DA_REPORT` resolves the byte-stable Paper-40 independent-DA
  report supplied by the release dependency map.
- `dependency:P40_DA_REPORT_SIDECAR` resolves that report's byte-stable
  SHA-256 sidecar from the same dependency map.

The dependency map is an integration input, not a sealed machine path.  A
verifier must reject an unknown or duplicate ID, a missing dependency,
non-C-sorted IDs, or any SHA-256 mismatch.  Because the second column contains
typed IDs rather than filesystem paths, direct `sha256sum -c` is not the
source-verification procedure; the typed resolver must report 22/22 matches.

## Frozen mathematical source

Let `W={0,1}*`, with empty word `epsilon`.  Define

\[
 L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
 M_w=M_{w_1}\cdots M_{w_k},
\]

where `M_0=L`, `M_1=R`, and

\[
 h(w)=\mathbf 1^{\mathsf T}M_we_1.
\]

This is locked to the exact convention in the `SD-C06` implementation.  It
reproduces

\[
 h(u0)=h(u),\qquad h(u1)=h(u)+h(\bar u).
\]

The finite object is `W_k={0,1}^k`; its partition trace is

\[
 Z_k(s)=\sum_{w\in W_k}h(w)^{-s}.
\]

The source-owned direct limit uses the embeddings `i_k(w)=w0`.  No compact
one-sided shift, autonomous limiting self-map, primitive orbit map, or
limiting transfer-operator function space is imported.

## Source-owned analytic fact

Only the following analytic identity is inherited, with attribution and its
original domain:

\[
 Z(s)=\lim_k Z_k(s)
 =\sum_{n\ge1}\varphi(n)n^{-s}
 =\frac{\zeta(s-1)}{\zeta(s)},\qquad \Re s>2.
\]

Meromorphic continuation of the displayed quotient is not finite-depth
convergence.  The signed critical-half-plane convergence remains open.  No
completed-xi or Riemann-zero statement is claimed.

## Locked target properties

A same-object scalar primitive ledger with clock `T(w)=log h(w)` would need:

1. **state autonomy:** every declared one-step successor descends to the
   direct-limit state;
2. **cyclic descent:** `T(uv)=T(vu)` for cyclic representatives;
3. **temporal powers:** `T(w^r)=rT(w)`;
4. **sign descent:** a scalar orbit phase is cyclic and satisfies
   `chi(w^r)=chi(w)^r`;
5. **operator ownership:** any credited determinant acts on the same object
   with its own marker, not on an unrelated diagonal inventory.

The package tests exactly these necessary properties for the declared
objects.  It does not assume they are sufficient for a global determinant.

## Allowed operations

- exact products of `L` and `R`;
- exact evaluation of `h` and Liouville values at generated integers;
- trailing-zero, cyclic-rotation, and word-power relations;
- the source theorem for full multiplicities `phi(n)`;
- standard trace-class diagonal Fredholm identities on `Re(s)>2`;
- primary-source literature search and internal Route collision audit;
- independent DA of this sealed package.

## Forbidden operations

- target-zero tables, fitting, validation ordinates, or post-result tuning;
- an external prime table or prime-indexed component;
- treating `lambda(h(w))` as endogenous merely because `h(w)` is endogenous;
- replacing `h(w)` by `tr(M_w)`, an eigenvalue, a spectral radius, a
  geodesic norm, or a transfer-operator derivative while retaining `SD-C06`
  ownership;
- identifying word depth, a Fredholm marker degree, and orbit repetition;
- importing Paper-40 corrections as novelty or authorization;
- describing the retrospective selector as prospective, outcome-independent,
  preregistered, novelty-bearing, or priority-bearing;
- presenting Paper-35's general trace/determinant firewall as a new theorem;
- universal claims about all Knauf, Farey, Gauss, Selberg, or adelic models;
- any authority/mirror/Git/README/manifest write by this Phase-1 worker.

## Stop rules

Stop the positive primitive-ledger branch immediately if any one of the exact
descent witnesses holds.  All four do.  Therefore no numerical determinant
or zero comparison is authorized.

Stop the paper itself if independent DA shows that the exact witness theorem
is already explicitly in the primary literature, that the source convention
is wrong, or that the claim silently changes type.
