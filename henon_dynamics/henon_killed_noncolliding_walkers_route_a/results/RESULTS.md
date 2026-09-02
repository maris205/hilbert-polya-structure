# Results

The finite regression covers all 36 parameter pairs `1<=k<=L<=8`:

- 502 chamber-state rows and 502 analytic modes;
- 273 survival/density time-state probes;
- every direct integer-generator spectrum agrees with the exterior-power
  energy multiset;
- all tested direct matrix exponentials agree with Karlin--McGregor minors;
- ground vectors are strictly positive and normalized;
- all Doob rows are conservative and detailed balance holds with `h^2`;
- all full-occupancy rows have ground energy `2L` and a null relaxation-gap
  field.

The independent checker records 5,803 explicit assertions in the full lane.
The exact SymPy lane verifies 15 characteristic polynomials, 72 polynomial
coefficient identities, 114 resolvent-moment cells, and 20 full-occupancy
trigonometric identities.  The mutation suite kills 68 of 68 hostile cases.

Evidence file SHA-256:
`9f9cd4bc19881165321750845302541ead2b9ac13399da52807335148ab54560`.
Payload self-hash:
`d826567d757e89ad74d0369929bdca92867eb99bdb0c454361889f7a398b0faf`.
