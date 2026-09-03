# Paper plan — P177

**Working title:** Random Projective-Hyperplane Toggling Is a Disjoint Union
of Crown Walks  
**Format:** anonymous deterministic `amsart` short theory note  
**Target length:** 4–5 A4 pages including references  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## One-sentence contribution

The literal random projective-hyperplane toggle chain is conjugate on every
communicating class to one crown walk, which yields an exact endpoint kernel,
the correct parity-periodic TV statement, and the complete global spectrum
with multiplicities.

## Claims–evidence matrix

| ID | Frozen claim | Proof evidence | Author-side exact pressure | Manuscript location |
|---|---|---|---|---|
| C1 | The toggle masks generate `W=<1,C>`, `dim W=d+1`; the closed classes are its `K=2^(m-d-1)` cosets of size `2^(d+1)` | hyperplane indicator `h_ell=1+c_ell`, simplex-code injectivity, explicit spanning argument | literal masks, generated subgroup, and full coset partitions | main theorem (i); §2 code lemma |
| C2 | Every class is the degree-`N` crown graph `K_(q,q)` minus a perfect matching and has period two | coordinate map `epsilon 1+c_a <-> (epsilon,a)`; one step adds `(1,ell)` with `ell!=0` | every component neighborhood and parity edge through declared boxes | main theorem (i); §2 |
| C3 | Every-time/every-target history counts are `q^(-1)(N^t+N(-1)^t)` at `L=0` and `q^(-1)(N^t-(-1)^t)` otherwise, with explicit `t=0/1` zero-support cases | Fourier inversion on `V*` after identifying the unique endpoint sum `L` | dynamic convolution, literal ordered histories, and support sentinels | main theorem (ii); §3 |
| C4 | Phase-compatible TV is `1/(qN^(t-1))`; ordinary component-stationary TV does not vanish and equals `1/2` for `t>=2` | subtract uniform probability from the exceptional and ordinary endpoint masses; retain the unoccupied parity half | exact rational TV in both comparison spaces | main theorem (iii); §3 |
| C5 | Full spectrum is `{1,-1,1/N,-1/N}` with multiplicities `{K,K,NK,NK}`, with no Jordan blocks | Boolean-character diagonalization and rank `d+1` of `S -> (|S| mod 2, sigma(S))` | exhaustive Boolean characters and multiplicity fibres through `d=4` | main theorem (iv); §4 |
| C6 | Component degree recovers `d`, and total carrier size then recovers `K`, only within the stated family | `N=q-1=2^d-1` and class size `2q` | integer reconstruction boxes | main theorem (v); §4 |
| B1 | `d=1` is excluded because its only sampled mask is empty and the chain is the identity | direct boundary calculation | both states checked literally | §5 excluded-boundary prose; verifier boundary |

## Section and page budget

| Part | Purpose | Budget |
|---|---|---:|
| Abstract and title | literal object, crown reduction, kernel, four eigenvalues, periodicity warning | 0.30 page |
| 1. Model, claim boundary, and result | define the chain; subtract code/design/Cayley/Fourier/crown background; state the theorem | 1.15 pages |
| 2. Code coordinates and classes | prove `dim W=d+1`, component count, crown conjugacy, period | 0.85 page |
| 3. Histories and parity-phase convergence | prove the exact counts and both TV statements | 0.85 page |
| 4. Full spectrum and reconstruction | prove the Boolean-character multiplicities, no Jordan blocks, and the bounded inverse | 0.85 page |
| 5. Exact controls and limits | record falsifier scope and excluded variants | 0.35 page |
| References | four verified primary/authoritative controls only | 0.45 page |

The budget is a target rather than a license to compress proof steps.  If the
settled build reaches five pages, theorem completeness takes priority over a
four-page cosmetic target.

## Author-round obligations

- Use actual projective hyperplanes: `ell` is nonzero and the zero form is
  never sampled.
- Say “phase-compatible convergence” or “parity-periodic convergence,” never
  ordinary mixing.
- State the stationary comparison on the whole class so the period-two
  obstruction is visible quantitatively.
- Prove surjectivity/rank of the parity–vector-sum map, rather than inferring
  multiplicities from a dimension count without a spanning argument.
- Treat all simplex-code, incidence-design, Cayley/Fourier, crown-graph, and
  generic finite-chain material as zero-credit background.
- Keep `OWNER_AMBER / HOLD_EXTERNAL` visible and never turn a bounded search
  non-hit into a novelty statement.
- Preserve `d=1`, zero-form sampling, complement masks, and nonbinary variants
  as explicit out-of-scope boundaries.

After the author-side Round-0 package, the standing batch authorization
activated two process-separated hostile reviews.  Their support-boundary and
provenance findings were repaired and delta-accepted; Round 2 closes with zero
open findings while preserving `OWNER_AMBER / HOLD_EXTERNAL`.
