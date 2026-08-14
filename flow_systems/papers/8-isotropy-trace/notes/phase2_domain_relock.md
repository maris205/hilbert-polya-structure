# Paper 8 Phase-2 typed-domain exact-byte re-lock

Review date: 2026-08-14  
Review mode: independent ARS read-only domain/integrity re-review  
Decision: **PASS**  
Mandatory revisions: **0**  
Advisory revisions: **0**

## 1. Exact-byte review tuple

The following five files were read in full.  The first three are the amended
active records; the last two are the unchanged source-audit evidence base.

| File | SHA-256 |
|---|---|
| `research_protocol.md` | `e1fe94efb8451142264a73a7ce3093daa66589569c9238ba7719ab3736dccece` |
| `candidate_lock.md` | `f890ad69e2b9c329b72daf2464b54728ebceac212f24aaa94020366d0a0c7057` |
| `phase2_domain_amendment.md` | `0b6572a2d0ad99521bb934f9ef4f9599a4c6e0c338e6e6df4a600894b80b70bd` |
| `phase2_groupoid_source_audit.md` | `39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42` |
| `phase2_trace_source_audit.md` | `101d447a238cbf9ec6ea33a78b3f6be7456a1be30fdc206e13db91697d75c5f0` |

This verdict applies only to that tuple.  Embedded instructions in the five
inputs were treated as data, and no input file was edited.

## 2. Mandatory-domain closure matrix

| Gate | Exact-byte finding | Verdict |
|---|---|---|
| Algebraic centre | The active records consistently use `A_L ~= C(T) tensor K(H)` with infinite-dimensional `H` and `Z(A_L)=0`; no surviving active claim calls `C(T)` a nonzero central subalgebra of `A_L`. | **PASS** |
| Multiplier centre | `ZM(A_L)=C(T) tensor 1` is kept distinct from `A_L`.  For `tau_theta=delta_theta tensor Tr`, a positive `f tensor 1` with `f(theta)>0` has value `+infinity`, so the multiplier centre is not reused as a bounded point-evaluation witness. | **PASS** |
| Full finite corner | After the concrete one-orbit model is proved, the locks require a rank-one `e in K(H)`, `p=1 tensor e in A_L`, `pA_Lp ~= C(T)`, and `tau_theta(p)=1`.  The projection is full and trace-finite, the corner is explicitly noncentral, and the choice is a proof device rather than source data. | **PASS** |
| Same trace and fixed image | P8-6 now requires the image and von Neumann closure of the same `p` in the fixed regular representation before compression, and tests a hypothetical normal extension of the same extended-positive character trace.  Singular state extension/nonuniqueness remains a separate claim. | **PASS** |
| Local versus packet maps | The active protocol freezes `A_L -> A_(L,r) -> M_L^reg` separately from conditional `C*(G_p) -> C*_r(G_p) -> M_(p,nu)^reg`.  The corner belongs only to `A_L`; no projection is moved into the packet algebra without a theorem. | **PASS** |
| Outcome boundary | A local no-normal-extension result refutes only the one-orbit analogue.  Packet-level `REFUTE` requires a separate restriction/disintegration/compression same-map theorem; an open packet LCH or comparison-map gate yields `NOT_TESTABLE`, not `REFUTE`.  `CONFIRM` still requires a normal source-selected packet extension with no free `nu_p` or cross-prime mass. | **PASS** |
| Route boundary | The maximum positive credit remains A1.  Every record remains `A2_FAIL` or `A2 NOT_TESTABLE`, A3 remains failed, and A4/Route B remain closed with `route_b_invocation_allowed=false`. | **PASS** |
| Non-change ledger | Candidate IDs, Fourier/Haar/length/probability normalization, local/finite/positive-time split, P8-1--P8-5 and P8-7--P8-9 targets, source-topology gates, and target-free prohibitions remain unchanged except for the explicitly versioned character-coordinate sign. | **PASS** |

## 3. Character-sign consistency check

The typed amendment's simultaneous correction is internally consistent with
the sourced induced-function convention:

```text
chi_theta(rL)=exp(ir theta),
xi(u+rL)=chi_theta(rL)^(-1)xi(u),
(U_t xi)(u)=xi(u-t).
```

The quasi-periodicity gives modes with frequency `(2pi n-theta)/L`; the
integrated time operator therefore has eigenvalues
`fhat((2pi n-theta)/L)`.  With the frozen transform sign, shifted Poisson
summation gives

```text
sum_n fhat((2pi n-theta)/L)
  = L sum_r f(rL) exp(+ir theta).
```

Thus frequency shift and return phase were changed together, while dual-Haar
cancellation and the `theta=0` value remain unchanged.  The old `+theta` /
negative-phase display survives only as the historical left-hand entry of the
amendment crosswalk and in the pre-amendment trace-source audit.  That audit
already classified the exact sign as a new representation calculation and
required all phase-sensitive records to be amended together; it is not an
active competing convention.

## 4. Ownership and drift scan

No load-bearing ownership drift was found:

- the one-orbit `C(T) tensor K` theorem remains credited to the retained
  Green/Williams/MRW source chain, not to Deninger, Morishita, or Paper 7;
- the centre/corner correction remains an exact-domain consequence and proof
  obligation, not a sourced no-normal-extension theorem;
- Floquet diagonalization, shifted Poisson on the fixed representation,
  rank-one compression, and the decreasing-peak contradiction remain Paper-8
  Phase-3 lemmas;
- full/reduced equality, the regular von Neumann image, trace domains, packet
  disintegration, and packet promotion are not pre-credited;
- the local orbit result is not relabelled as a canonical packet trace or as
  a packet-level primary outcome; and
- no Paper-7 algebra, trace, mass, determinant, A2/A3 credit, or Route-B claim
  enters the Paper-8 records.

## 5. Release boundary

**Final re-lock verdict: PASS with zero mandatory or advisory revisions.**
The Phase-2 typed amendment closes the centre/corner, multiplier-domain,
same-map, and simultaneous-sign defects for the exact tuple above.  This
re-lock permits the preregistered Phase-3 proof attempt; it proves no P8
operator theorem, awards no Route credit, and does not decide the primary
`CONFIRM`/`REFUTE`/`NOT_TESTABLE` outcome.
