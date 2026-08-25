# C167 source audit

Date: 2026-08-25

Source commit: `4342893ce5e2516924181744bfacc01c12e4959d`

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`

## Admitted source object

The sole analytic input is the Dirichlet Abel half-wave trace for the
rectangle (Q_\alpha=(0,1)\times(0,\alpha)),

```text
W_alpha(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2/alpha^2)), Re(s)>0.
```

Separation of variables and two-dimensional Poisson summation give the exact
principal-branch identity recorded in `THEOREM_PACKAGE.md`.  C157 and C162
are used only as source-side convention locks for the square trace and its
renormalized branch proof.  C167 rederives the aspect-dependent constants and
does not import any target data.

## Evidence boundary

- Exact algebra proves the all-α branch coefficient and the complete
  collision classification in β=α².
- The finite rational-fibre rows, the (\mathbb Q(\sqrt2)) enumeration, and
  four high-precision limits are regression sentinels only.
- No bibliography is needed because the paper makes no priority or
  literature-comparison claim.
- No target zero/prime table, target divisor/counting law, target functional
  equation, arithmetic local data, Euler factor, root number, automorphy
  input, or Hilbert--Pólya assumption is admitted.

## Recorded pivot

The tempting statement that irrational β provides a uniform shell gap is
false in this generality and is not used.  C167 retains only the exact
no-collision statement.  It also declines a general divisor formula for
rational fibres; the exact fibre equation is sufficient for the theorem.
