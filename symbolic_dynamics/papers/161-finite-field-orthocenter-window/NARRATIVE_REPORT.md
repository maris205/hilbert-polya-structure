# Narrative report — P161

**Status:** `ROUND-2 / REVIEW B ACCEPTED / HOLD_EXTERNAL`.

## One-sentence result

After subtracting the classical orthocentric quartet and established
finite-field triangle geometry, totalizing the orthocenter sliding window by
a singular sink yields an exact orientation-sensitive depth, image, and
every-target fibre atlas.

## Literal dynamics

For a prime `p=3 mod 4`, take every ordered noncollinear triangle in
`F_p^2` and add a sink.  The update slides the triangle window:

~~~text
(A,B,C) -> (B,C,H(A,B,C)),
~~~

unless that next triple is collinear, in which case it goes to the sink.  The
sink is fixed.

The anisotropic dot product makes the singular boundary clean.  There are

~~~text
T=p^2(p^2-1)(p^2-p)
~~~

ordered triangles and

~~~text
R=p^2(p^2-1)(p-1)
~~~

right triangles at each of the three listed coordinates.  The three classes
are disjoint.  Their complement has size
`Q=p^2(p^2-1)(p-1)(p-3)`.

## The signal beyond the classical core

The `Q` nonright triangles follow the classical orthocentric quartet and form
exact four-cycles.  The residual signal is the orientation of the singular
strata:

- right at coordinate one: depth two;
- right at coordinate two or three: depth one;
- sink: fixed.

A reverse window is forced to be `(H(A,B,C),A,B)`.  It is invalid exactly for
targets right at their first or second coordinate, and valid for a nonright
target or one right at its third coordinate.  This gives the complete
`0/1/(1+2R)` fibre law without dividing orbit counts, the one-step image, and
the stable image after two steps.

## Ownership boundary

Kocik–Solecki own the orthocentric-system identity.  Wildberger owns the
finite-field metrical triangle setting and orthocenter constructions.  Guy
also uses the orthocentric-quadrangle viewpoint, but his trisequence iterates
Steiner-line reflections and circumcircle intersections; it is not this
window map.  All of those objects receive zero contribution credit.

## Exact evidence and boundary

The paper-local verifier exhausts all 433 states for `p=3` and all 98,785
states for `p=7`, totaling 1,317,843 assertions.  Its transcript SHA-256 is
`26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c`.
At `p=3`, `Q=0`: the sink is the only recurrent state, yet 144 states remain
at depth two.

The paper makes no claim for isotropic primes, other quadratic forms, higher
dimensions, novelty, priority, or external release.
