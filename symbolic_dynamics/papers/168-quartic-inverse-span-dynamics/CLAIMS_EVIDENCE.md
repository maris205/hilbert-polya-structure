# P168 claims and evidence ledger

**Freeze:** author Round 0  
**Lifecycle:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`  
**Evidence rule:** analytic proof establishes the theorem; exhaustive
computation is an independent falsification control.

## Claim ledger

| ID | Frozen statement | Proof dependency | Exact control | Status |
|---|---|---|---|---|
| C1 | `dim J(A)>=dim A`; equality implies `J^2(A)=A`; recurrence is equivalent to equality | finite cardinality and monotone rank | checked on every state for `p=2,3,5` | proved |
| C2 | Recurrent states are exactly `0`, `K`, all lines, and all `xi F_{p^2}` | C1 plus Kolomeec--Bykov's published patched-inverse classification; binary lines handled directly | exact recurrent set; scaled quadratic subfield constructed independently | proved, direct-owner-dependent |
| C3 | A non-subfield plane has image rank 3 at `p=2` and 4 at odd `p`; every hyperplane maps to `K` | denominator-clearing independence; C2 excludes rank-three equality | complete rank transition table | proved; inverse-line geometry assigned zero credit |
| C4 | Sharp maximum tail is 2 at `p=2` and 1 at every odd prime | C2--C3 and existence `P-Q>0` | depth histograms `22/15/30`, `52/160`, `184/936` | proved |
| C5 | `S=2+2L+P`, `R=2+L+Q`, `F=2+gcd(2,L)+gcd(2,Q)`; all other recurrent points form two-cycles | Gaussian coefficients; inversion on cyclic scalar quotients | exact state/recurrent/fixed/cycle counts | proved |
| C6 | The stated depth enumerator, image stabilization, fixed-iterate sequence, and zeta function hold | transition table and standard finite-cycle algebra | time powers and image counts | proved |
| C7 | At `p=2`, every hyperplane has exactly two one-step non-subfield-plane predecessors | twisted scalar law, trace-pairing transitivity, count `(P-Q)/L=2` | every one-step target fibre | proved |
| C8 | The fibre formulas cover every target and every positive time | C1--C3 exclusions, C7, stabilization after at most two steps | every target at times 1,2,3,4 | proved |
| C9 | All transient vertices lie in the one component rooted at `K`; every other recurrent cycle is bare | C7--C8 | all directed edges and component counts | proved |

## Frozen exact rows

```text
p=2: states 67, image 37, recurrent 22, fixed 4,
     cycles 1^4 2^9, depths 0:22/1:15/2:30,
     full-field fibres t=1,2: 16,46.

p=3: states 212, image=recurrent 52, fixed 6,
     cycles 1^6 2^23, depths 0:52/1:160,
     full-field fibres t=1,2: 161,161.

p=5: states 1120, image=recurrent 184, fixed 6,
     cycles 1^6 2^89, depths 0:184/1:936,
     full-field fibres t=1,2: 937,937.
```

Edge SHA-256 values are frozen in `verification_output.txt` and
`SHA256SUMS`.  The verifier performs 32,754 explicit assertions.

## Zero-credit inputs

- patched inverse images that remain affine/linear subspaces;
- inverse-closed additive-subgroup classifications;
- inverse projective lines as normal rational curves or independent tuples;
- Gaussian-binomial subspace counts;
- cyclic Singer actions and inversion on cyclic quotients;
- the general Artin--Mazur periodic-point zeta conversion.

## Statements not made

- no novelty, priority, first-proof, or freedom-to-operate assertion;
- no theorem for nonprime base fields or extension degree other than four;
- no claim that the recurrent classification or inverse-line geometry is a
  contribution;
- no claim that computation replaces any proof;
- no external-circulation authorization.

## Evidence acceptance

Round 0 is complete only if two fresh verifier processes match the frozen
transcript byte for byte; two source-only cold LaTeX builds match the canonical
PDF; all references resolve; all fonts embed; metadata and visible text remain
anonymous; and the lifecycle line remains `HOLD_EXTERNAL`.
