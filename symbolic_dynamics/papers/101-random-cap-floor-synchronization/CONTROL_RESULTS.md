# Exact Control Results

Status: refrozen exact run after independent internal cross-hostile repair,
29 August 2026.

Run from this directory:

```text
python3 code/verify_cap_floor.py
```

The program has four exact lanes:

1. exhaustive chronological composition and normal-form checks;
2. an independently organized fixed-type rank/spacing enumeration;
3. rational survival, PGF-coefficient, convolution, moment, critical, and
   off-critical checks;
4. exact `p=0,1` endpoint checks.

It also begins with a 13-assertion noncommuting composition sentinel:
floor `3/4` followed by cap `1/4` must collapse to `1/4`, whereas the
reversed word must collapse to `3/4`. This catches the most damaging
possible convention reversal before the exhaustive lane begins.

## Frozen stdout

```text
random cap-floor exact control: PASS
assertions=6948361
composition_sentinel_cases=13
normal_form_environments=695482
normal_form_evaluations=6204182
conditional_order_permutations=409112
law_cases=605
endpoint_cases=202
```

The same bytes are stored in `code/verify_cap_floor.out`.

## Coverage

- **Normal form:** all `2^n` type words and all `n!` strict rank orders for
  `1 <= n <= 7`; each direct chronological composition is evaluated at the
  endpoints and every rank breakpoint and compared with an independently
  updated interval/constant state.
- **Crossing and spacing totals:** for every floor count `j`, the program
  checks `C(n,j)n!` total labelled environments, `n!` surviving
  environments, and rank-gap sum `n!`.
- **Independent conditional lane:** a fixed full type word is used for each
  `(n,j)`, and all rank permutations are enumerated through `n=8`. This
  separately checks survival `1/C(n,j)` and conditional expected normalized
  gap `1/((n+1)C(n,j))`.
- **Law lane:** exact `Fraction` arithmetic at
  `p in {1/5,1/3,1/2,2/3,4/5}` through time 60 checks the finite sum, closed
  form, rational generating-function recurrence, tail-difference mass,
  independent-geometric convolution, mass-plus-tail closure, moments,
  critical identity, and off-critical identity.
- **Endpoints:** 202 exact cases through time 100 check survival one and
  uniform mean diameter `1/(n+1)` at `p=0,1`.

## Cross-hostile evidence repair

The previous script counted 305 assertions of the form
`s/(n+1) == survival_sum(n,p)/(n+1)`, where `s` had just been assigned
`survival_sum(n,p)`. Those self-comparisons were exact but tautological and
have been deleted rather than counted as evidence. The independent
rank-gap lanes, weighted diameter enumeration, and endpoint lane remain
unchanged. Accordingly the registered total decreased from 6,948,666 to
**6,948,361** without weakening any nontrivial control.

No pseudorandom numbers, floating-point comparisons, external packages, or
network resources are used. Exhaustive bounds are finite proof spikes, not
extrapolations; the paper's infinite statements rest on symbolic proofs.
