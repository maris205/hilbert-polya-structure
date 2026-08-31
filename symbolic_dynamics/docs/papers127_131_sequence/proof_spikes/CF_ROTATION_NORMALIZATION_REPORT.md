# Proof spike: cyclic normalization of finite continued fractions

**Candidate:** root X18.  **Status:** mathematical reserve; collision gate not
cleared and no paper number frozen.  **External status:** `HOLD_EXTERNAL`.

## Literal system

Let `R_N` be the rational numbers at subtractive-Euclidean cost `N`: write a
positive rational in its unique canonical finite regular continued fraction

```text
[a_1; a_2,...,a_k],   a_i>=1,   a_k>=2,
```

and require `a_1+...+a_k=N`.  Thus `R_N` is in transparent bijection with
positive compositions of `N` ending in a part at least two, and has
`2^(N-2)` elements.  This coordinate bijection is declared rather than used
to disguise the composition-carrier collision below.

Move `a_1` to the end of the quotient queue.  If the new last digit is one,
return to the unique rational expansion using the canonical identity

```text
(...,b,1) -> (...,b+1).
```

Equivalently, a leading quotient greater than one moves to the back, while a
leading one is deleted and contributes one to the current last quotient.  The
digit sum, and hence the Euclidean-cost stratum `R_N`, is preserved.

## Exact theorem contract supported by the spike

1. The entrance time is the one-based position of the last digit equal to one;
   the sharp global depth is `N-2`, witnessed by `(1,...,1,2)`.
2. The recurrent set is exactly the digit words with every part at least two.
   The terminal cyclic word is obtained by absorbing every run of ones into
   the preceding non-one digit, then starting immediately after the last one.
3. The eventual period is the primitive rotation period of that terminal word.
4. The exact-depth generating functions are

   ```text
   D_0(x) = x^2/(1-x-x^2),
   D_t(x) = x^(t+2)/((1-x)^(t-1)(1-x-x^2)),  t>=1.
   ```

5. A target has one rotation preimage when it has length one or penultimate
   digit at least two, and one deletion preimage when its last digit is at least
   three.  Thus every fibre has size `0,1,2`; the one-step image size is one for
   `N=2,3` and `3*2^(N-4)` for `N>=4`.
6. Recurrent cycles are weighted necklaces with parts at least two.  For fixed
   length `k`, Burnside gives

   ```text
   (1/k) sum_{d|gcd(N,k)} phi(d)
       binom(N/d-k/d-1, k/d-1),
   ```

   with the evident one-part convention.  Fixed points are the constant digit
   words, hence `tau(N)-1`.

## Evidence and collision posture

The exact verifier exhausts every canonical word through weight 18 and checks
the literal orbit normal form, every depth layer, every target fibre, image and
fixed counts, and the Burnside cycle formula.  This is a clean all-parameter
route, not merely an observed sequence.

The system nevertheless remains behind a strong internal firewall.  In its
quotient coordinates the phase space is literally a subset of integer
compositions, so the rational interpretation cannot by itself separate it
from P126.  P126, however, is an everywhere synchronous partwise refinement:
it has logarithmic absorption to a unique fixed state and its proof engine is
an all-iterate suffix-decodable kernel.  The present map is a one-place queue
rotation with canonical deletion: it has a sharp linear transient, many
necklace cycles, fibres at most two, and a run-absorption/rotation proof.
P122 and P117 also occupy reversal/run interfaces, which are subtracted.

Canonical finite-CF uniqueness, the trailing-one identity, continuants,
Euclidean-cost language, composition enumeration, and Burnside rotation
counting receive zero contribution credit.  The only proposed residual is the
conjunction of the literal quotient-queue map with its exact entrance layers,
terminal-core decoder, pointwise fibres, and weighted-necklace recurrent
census.  The bounded owner search found no literal iteration match; this is
not a novelty or priority claim.
