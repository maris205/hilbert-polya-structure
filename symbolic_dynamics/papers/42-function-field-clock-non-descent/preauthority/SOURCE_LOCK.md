# Source lock

## Identity

- Phase: Paper 42 Phase 1, preauthority research only.
- Proposed candidate: `SD-C44`.
- Historical parent: `SD-C01`.
- Freeze date: 2026-08-17 UTC.
- Portable namespace:
  `papers/42-function-field-clock-non-descent/preauthority` relative to the
  `symbolic_dynamics` root at release.
- Authority, mirror, Git, root README, registries, and paper manifests: read
  only.
- Chronology: the card outcomes, selector result, and theorem witnesses were
  known before this package was written. Only corrected final input bytes are
  frozen before independent DA.

## Portable source-ID resolution contract

`SOURCE_HASHES.sha256` is a two-column SHA-256/source-ID manifest sorted by
source ID in C byte order. It contains no host path.

- `repo:<path>` resolves `<path>` from the repository root containing `.git`.
  Reject an absolute path, `..`, symlink escape, missing file, or resolution
  outside that root.
- `dependency:P41_*` resolves the byte-stable file supplied by the Paper-41
  preauthority dependency map. Reject a missing or multiply resolved
  dependency.

The Paper-41 dependency map is:

| Source ID | Dependency-package relative file |
|---|---|
| `dependency:P41_DA_HANDOFF` | `DA_HANDOFF.md` |
| `dependency:P41_LITERATURE_NOVELTY_AUDIT` | `LITERATURE_NOVELTY_AUDIT.md` |
| `dependency:P41_PACKAGE_MANIFEST` | `SHA256SUMS.txt` |
| `dependency:P41_PROOF_PACKAGE` | `PROOF_PACKAGE.md` |
| `dependency:P41_RESEARCH_LOCK` | `RESEARCH_LOCK.json` |
| `dependency:P41_ROUTE_EXPECTATION` | `ROUTE_EXPECTATION.yaml` |
| `dependency:P41_SELECTION_AND_PROVENANCE` | `SELECTION_AND_PROVENANCE.md` |
| `dependency:P41_SOURCE_LOCK` | `SOURCE_LOCK.md` |

The dependency map is an integration input, not a sealed machine path. The
typed resolver must reject unknown or duplicate IDs, non-C-sorted IDs, and
hash mismatches. Direct `sha256sum -c` is insufficient for `SOURCE_HASHES`.

## Frozen source object

For `q` in `{2,3,5}`, let

\[
 \Sigma_q=\mathbb F_q^{\mathbb Z}
\]

with the left shift `sigma`. A primitive source object is an oriented cyclic
class of an aperiodic nonempty word over `F_q`. Cyclic rotations are identified;
reversal is not identified unless it lies in the same cyclic class. Ordinary
word powers are repetitions.

For a primitive class `gamma=[w]`, define

\[
 n(\gamma)=|w|,\qquad T_q(\gamma)=n(\gamma)\log q.
\]

The free marker `z` counts one original shift symbol. Thus the primitive
factor owned by `gamma` is

\[
 \left(1-z^{n(\gamma)}q^{-s n(\gamma)}\right)^{-1}.
\]

No marker specialization or first-return retyping may earn same-marker credit.

## Frozen source operator and determinant

The one-vertex `q`-loop weighted adjacency acts on `C` by

\[
 \mathcal L_{q,s,z}f=zq^{1-s}f.
\]

Its ordinary finite-dimensional determinant is

\[
 D_q(s,z)=\det(I-\mathcal L_{q,s,z})=1-zq^{1-s},
\]

and its reciprocal is the marked full-shift dynamical zeta. At `z=1` this is
the zeta function of the affine line over `F_q` under the standard norm
dictionary. This positive function-field ownership is not in dispute.

## Frozen rational-prime comparison

Let `P` be the set of positive rational primes. On `ell^2(P)` define the
separate diagonal comparison operator

\[
 Q_se_p=p^{-s}e_p.
\]

For `Re(s)>1`, it is trace class and

\[
 D_{\mathbb P}(s,z)=\det(I-zQ_s)
 =\prod_{p\in\mathbb P}(1-zp^{-s}).
\]

The reciprocal specializes to the rational Riemann Euler product at `z=1`.
This comparison operator is not owned by `SD-C01` and cannot transfer A0, A1,
or A2 credit.

## Locked target conditions

A credited factorwise descent from source primitive factors to rational-prime
factors must preserve simultaneously:

1. **totality:** every source primitive factor is accounted for;
2. **rational-prime support:** every image label is in `P`;
3. **clock/weight:** `log p=T_q(gamma)`, equivalently
   `p=q^n` for a length-`n` source primitive;
4. **marker:** source `z^n` equals the target primitive marker `z`;
5. **multiplicity:** exactly one source factor maps to each target prime
   factor, with no collision or deletion;
6. **repetition:** the `r`th traversal maps to `p^r` with marker `z^r` only
   after the primitive marker itself agrees;
7. **ownership:** the same source object and weighted adjacency own the
   determinant.

The no-go theorem needs only subsets of these necessary conditions. It does
not claim they are sufficient for a completed determinant.

## Allowed operations

- exact finite words, rotations, primitive-word checks, and word powers;
- exact Möbius formula for `N_q(n)`;
- exact finite-field norm `q^n` and elementary primality of `q^2`;
- exact formal power series in `z` and Dirichlet-series coefficient
  comparison on `Re(s)>1`;
- frozen primary and authoritative literature;
- strict Route-A audit and independent DA.

## Forbidden operations

- rational-prime or Riemann-zero tables in candidate definition or fitting;
- assigning arbitrary primes to source necklaces while retaining clock credit;
- replacing `z^n` by `z` and calling it the same marker;
- deleting all but selected source factors without declaring a projection;
- importing the rational-prime diagonal comparator as source-owned;
- transferring C04/P40 or C06/P41 object, marker, operator, or novelty credit;
- describing the selector as prospective, outcome-independent, preregistered,
  novelty-bearing, or priority-bearing;
- claiming a universal obstruction for all function-field/number-field maps,
  symbolic systems, codes, factors, or extensions;
- any authority, mirror, Git, root README, registry, or manifest write by this
  Phase-1 worker.

## Stop rules

Stop the same-clock rational-prime projection branch if one primitive source
orbit has forced image `q^n` composite. Stop the exact factor-identification
branch if marker, weight, or multiplicity fails. Stop the paper if independent
DA finds a convention error, invalid totality requirement, hidden object
change, or an exact published duplicate of the typed theorem.
