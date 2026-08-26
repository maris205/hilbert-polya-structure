# Exact validation plan

This is a pure-theory package.  No GPU or stochastic pilot is relevant.
Computation is used only to reconstruct and attack the theorem package.

## Frozen inputs

- (X=(0,\infty)^2).
- (F(x,y)=(y,(1+y)/x)).
- One map application is one tick.
- (d\mu=dx\,dy/(xy)), (R(x,y)=(y,x)), and (Uf=f\circ F).
- Exact arithmetic only; no target data or fitted parameter.

## Gates

1. **Rational-iterate gate:** independently simplify every coordinate of
   (F^0,\ldots,F^5).
2. **Period gate:** solve the fixed-point equations in the positive quadrant
   and use the prime order five to classify all least periods.
3. **Zeta gate:** distinguish a singleton fixed set from the uncountable
   set (\operatorname{Fix}(F^5)=X); reject formal finite counts.
4. **Geometry gate:** reconstruct the Jacobian, invariant density, inverse,
   and reversor identity.
5. **Operator gate:** verify the cyclic projection sign and exact group
   algebra; prove infinite multiplicity by disjoint orbit tubes.
6. **Adversarial gate:** test repaired-hash semantic mutations, not only
   stale checksums.
7. **Release gate:** byte replay, deterministic double PDF compilation,
   embedded fonts, clean layout, and 27-file manifest closure.

## Finite sentinels

The producer records 100 rational initial points
((a/3,b/5)), (1\le a,b\le10), and the fixed-set classification through
(n=50).  These rows detect implementation drift but do not establish the
global rational identities.

## Success and pivot rule

Success means a complete theorem-backed decision, including a negative one.
If (F^5=I) failed symbolically or the operator obstruction could not be
proved, the candidate would be weakened or replaced.  It did not require a
pivot: the obstruction is exact, substantive progress.  It rejects this
model as a primary Route-A candidate while retaining its natural Koopman
lift as a controlled A4 example.
