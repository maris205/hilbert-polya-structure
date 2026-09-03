# Hostile stochastic/graph review — P180

**Reviewer process:** stochastic/graph lane, against repaired author Round 1.  
**Review mode:** read-only; no author file was modified.  
**Reviewed `main.tex` SHA-256:**
`529bd4c0c091d3932c35de0b1ac8a6d347b3c65a838738bccfc1167207929991`.  
**Reviewed PDF SHA-256:**
`d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59`.  
**Verdict:** `PROVABLE AS STATED / 0 CRITICAL / 0 MAJOR / 0 MINOR /
HOLD_EXTERNAL`.

## Independent extension-field reconstruction

The reviewer implemented finite fields as polynomial quotients and verified
the field identities for every declared modulus.  This directly attacks the
manuscript's arbitrary-prime-power quantifier, which the author verifier does
not enumerate.  The boxes include `GF(4), GF(8), GF(9)` in dimensions one and
two, `GF(16), GF(25), GF(64)` in dimension one, several prime fields, and
invertible identity, alternating, and nonsymmetric shear forms in dimension
two.  Functional graphs were classified by indegree peeling followed by
reverse dynamic programming, not by the author's per-start orbit walk.

The exact transcript contains **1,143,286 assertions** and fixes the arrow
digest
`2d37532ed94da3392e31a04a07683933e6fd478020a2f279a8acdf28b445b282`.
It includes characteristic two, `A=0`, `A=2` over `GF(64)`, and `A=3` over
`GF(109)`.  Every target is checked at `t=0,...,4`; in particular, the new
Round-1 time-zero fibre statement is independently verified as the identity
map.  Representative exact tail profiles are

\[
 \operatorname{GF}(64),m=1:\quad (442,1008,2646),
\]

and

\[
 q=109,m=1:\quad (433,1080,2592,7776).
\]

Two fresh processes run after the Round-1 byte freeze reproduced
`CANONICAL.txt` exactly (`PASS/PASS`).

## Claim-by-claim proof audit

| claim under attack | independent derivation | result |
|---|---|---|
| arbitrary finite fields/forms | only nondegeneracy of `v -> B(u,v)` for `u != 0` and the identity `B(lambda u,lambda v)=lambda^2B(u,v)` are used; symmetry is unnecessary | pass |
| level and null-cone counts | every nonzero `u` gives a surjective linear functional with fibres `q^(m-1)`; subtraction gives `Z` | pass |
| radial iterate | the exponent recursion is `a_(t+1)=a_t+3^t`, hence `a_t=(3^t-1)/2` as an integer | pass |
| exact tail | the 3-adic valuation of `3^t(3^ell-1)/2` is exactly `t`, so the first cyclic epoch is `a` | pass |
| pair period | after entering the cycle, pair equality is `s | (3^ell-1)/2`, equivalently `2s | 3^ell-1`; the factor two is essential | pass |
| every-time fibre | a root `c^(3^t)=d` forces the unique source `c^(-a_t)(x,y)`; cyclic-group root counts give `g_t` | pass |
| time-zero fibre | `Phi^0` is the identity, so every target has one source | pass |
| null exceptions | the entire null cone maps to zero, a nonzero null target is unreachable at positive time, and no nonzero level can map to zero | pass |
| census and image | scalar order classes times the common level size `Q` give all tails; cube-image values times `Q`, plus zero, give the image | pass |

The modulus `2s`, rather than `s`, is correct for the pair state.  For
example, an initial bilinear value of order two is fixed by cubing, but the
pair alternates by radial scale `-1` and therefore has period two.  In
characteristic two, `q-1` and hence `s` are odd; the integer orders modulo
`s` and `2s` agree, which the extension-field verifier checks.

## Findings and repaired-delta audit

No Critical, Major, or Minor defect remains in the reviewed Round-1 bytes.
The abstract now attributes the orbit data to the full decomposition of the
initial order into its 3-part and prime-to-3 part (`main.tex:38-39`).  The
body explicitly types `(3^t-1)/2` as an ordinary integer exponent and `2s`
as an ordinary integer modulus, including in characteristic two
(`main.tex:101-123`).  These edits match the proof and leave
`ord_(2s)(3)` unchanged.

## Ownership and remaining kill switches

The reviewed Round-1 text states `m>=1`, includes the `t=0` identity fibre, and
subtracts the internal scalar-power/formed-space neighbors P102, P103, P125,
and P171.  Direct inspection confirms that these are, respectively, an
involutive group-algebra norm map, double-adjugate dynamics, a quadratic
state shear over `F_2`, and Boolean-semiring Gram dynamics; none is the
literal bilinear radial map.  The proof survives nonsymmetric forms,
extension fields, `A=0`, characteristic two, nonzero null targets, and all
tested power-root fibres.  Direct ownership of the lifted pair atlas, a change to a
degenerate form, or replacement of pair period by scalar-value period would
reopen the result.  Exact computation is not novelty evidence;
`OWNER_AMBER / HOLD_EXTERNAL` remains mandatory.
