# Exact Control Results

Status: author-stage exact run, 29 August 2026; external release **HOLD**.

Run from this directory:

```text
python3 code/verify_monomial_toggle.py
```

The verifier uses only the Python standard library. All matrix entries,
probabilities, moment weights, and transfer coefficients are represented by
`fractions.Fraction`. It uses no pseudorandom numbers, floating-point
comparisons, network access, or external package.

## Stored stdout

```text
monomial-toggle exact control: PASS
assertions=741486
normal_form_words=122865
signed_transform_words=61425
occupation_distributions=195
signed_transfer_parameter_cases=180
signed_recurrence_steps=375
occupation_moment_times=405
endpoint_times=162
lane_assertions=clt_variance:30,endpoint:162,normal_form:737190,occupation_dp:975,occupation_moments:1620,recurrence:429,signed_transfer:1080
```

The same bytes are stored in `code/verify_monomial_toggle.out`.

## Coverage

1. **Literal normal form and spectrum.** For
   `a in {1/2,2/3,3/4}`, `q in {0,1/4,1/2,3/4,1}`, and every binary word
   through length 12, the script left-multiplies the rational matrices. It
   independently records pre-update occupation and terminal orientation,
   then checks the full matrix normal form. The literal determinant, column
   orthogonality, and Gram eigenvalues are separate assertions.
2. **Occupation law and singular moments.** For 195 `(a,q,n)` triples, a
   two-state dynamic program is compared with the weighted literal word law.
   Normalization and singular moments of orders 1, 2, and 3 are checked.
3. **Signed and absolute transforms.** For five toggle probabilities, three
   rational positive tilt variables, and times through 11, literal word sums
   are compared with independently coded positive and negative tilted
   transfers. A third DP checks the absolute transform and both sides of the
   deterministic squeeze used in the proof.
4. **Cayley–Hamilton and strict gap.** Exact trace and determinant
   coefficients drive 375 recurrence checks. Evaluating the characteristic
   polynomial at one gives an exact negative rational sentinel at every
   interior parameter.
5. **CLT variance algebra.** Conditional martingale means and variances are
   checked directly. Exact signed-occupation means and second moments are
   compared with their correlation-sum formulas through time 80 at five
   interior probabilities.
6. **Endpoints.** At `q=0`, the absolute tilt is exactly `t^n`; at `q=1`, it
   is `t^(n mod 2)`. These are checked independently through time 26.

The rational tilt `t` stands for `exp(theta)` in the transfer identities.
The code checks the algebra for several exact positive rational values;
the paper proves the formulas for every real `theta>0`.

## Evidence boundary

The exhaustive ranges are finite proof spikes, not extrapolations. The
normal form, ergodic limit, martingale CLT, and Perron asymptotic rest on the
symbolic proofs in `main.tex`. No assertion is a direct comparison of a
quantity with an immediately identical reassignment.
