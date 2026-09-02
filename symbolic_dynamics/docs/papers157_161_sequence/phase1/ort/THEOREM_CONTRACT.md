# Frozen theorem contract — finite-field orthocenter sliding window

External status: **HOLD_EXTERNAL**.  Selection status:
**PASS_FOCUSED_AMBER / NUMBERING NOT YET FROZEN**.  The classical
orthocentric-system identity is direct background and receives zero credit.

Let `p` be a prime with `p=3 (mod 4)`.  In `F_p^2`, use the dot product
`(x,y) dot (u,v)=xu+yv`.  The carrier consists of every ordered
noncollinear triangle and a sink `dagger`.  If `H(A,B,C)` is the orthocenter,
define

```text
F(A,B,C)=(B,C,H(A,B,C))  when this target is noncollinear,
F(A,B,C)=dagger          otherwise,
F(dagger)=dagger.
```

Put

```text
T=p^2(p^2-1)(p^2-p),
R=p^2(p^2-1)(p-1),
Q=T-3R=p^2(p^2-1)(p-1)(p-3).
```

The paper must prove the following conjunction.

1. There are `R` triangles right-angled at each specified coordinate, and
   the three classes are disjoint.  The remaining `Q` triangles have exact
   period four.
2. A triangle right at its first coordinate has depth two.  A triangle
   right at its second or third coordinate has depth one.  The sink is
   fixed.  Thus the sharp stable image at time two has size `1+Q`, and

   ```text
   zeta_F(q)=(1-q)^(-1)(1-q^4)^(-Q/4).
   ```

3. The sink has `1+2R` one-step predecessors.  A target triangle right at
   its first or second coordinate has none; one right at its third coordinate
   or a nonright target has exactly one.  Consequently the one-step image has
   size `1+T-2R`.
4. The depth CDF at thresholds `0,1,2` is respectively
   `1+Q`, `1+T-R`, and `1+T`.  At the boundary prime `p=3`, `Q=0`: the sink
   is the only recurrent state although the height remains two.

The orthocenter, the orthocentric quartet, finite-field metric geometry,
elementary perpendicular-vector counting, and generic zeta conversion are
zero-credit background.  The only retained residual is the anisotropic
finite-field singular totalization, its orientation-sensitive depth split,
and the complete target-resolved fibre/image atlas.
