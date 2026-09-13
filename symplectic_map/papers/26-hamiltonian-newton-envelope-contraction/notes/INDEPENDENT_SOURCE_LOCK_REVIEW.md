# Independent source-lock review R1

## Verdict and zero-finding census

Verdict: PASS.

I independently find the repaired Paper 26 source lock complete, canonical,
mathematically faithful, inventory-exact, and authority-safe.  The final
finding census is:

- blocker: 0;
- major mathematical or lifecycle finding: 0;
- minor mathematical, evidentiary, canonical, citation, or inventory finding:
  0;
- wording ambiguity: 0;
- permission or authority expansion: 0.

I was not a candidate reviewer, source-design author, source-design repair
author, source-design R0/R1/R2 reviewer, source-lock author, or canonical-lock
repair author.  I had not previously listed or read this project.  I authored
none of the twelve objects under review.  My only filesystem write is this
review, after all checks below had passed.

The reviewed candidate identifier is
planar_newton_envelope_bidirectional_degree_v1.  Its exact title is:

Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector
Rigidity and Bidirectional Degree Growth

## Opening authority and stable external records

I read both current Batch 06 ledgers through EOF before inspecting the lock.
Their opening identities were:

| Record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| BATCH_06_STATUS.md | e5b037ee149549deeede0b3b58a2a2512e4fd53b72257bb888b921240d4362e6 | 373425 | 5260 |
| BATCH_06_IDEA_REPORT.md | 08fb4e0e16acdb5632cf3f59a9d37085cf00c9ac7995fc7141ff26f76ae78858 | 513901 | 9408 |

The controlling gate is the independent review of the repaired canonical
source lock.  It permits a zero-finding reviewer to create only this file and
does not permit the reviewer to open a successor gate.

I also read both immutable candidate reviews through EOF and reproduced their
identities and unique terminals:

| Record | SHA-256 | Bytes | LF | Terminal |
|---|---|---:|---:|---|
| BATCH_06_PAPER26_CANDIDATE_REVIEW_R1.md | cc81cc410d9122bdaf6ebf8b20e57bce3cbe4fcaed17c3cc0ed5f596d9844dbe | 29824 | 611 | PAPER26_CANDIDATE_GATE_PASS_R1 |
| BATCH_06_PAPER26_CANDIDATE_REVIEW_R2.md | 164273106733f611c0d35a60cb693d5ffbf8cf1300ffb658a00abb555fbda2e1 | 26605 | 1112 | PAPER26_CANDIDATE_GATE_PASS_R2 |

The final independent source-design review is SHA-256
974bcfea08dff87d359993839452eb271d2cf0edbbe2fb811abc17051aece92e,
17823 bytes / 449 LF, regular mode 0644/link one, and ends uniquely with
PAPER26_SOURCE_DESIGN_PASS.  I read it and all ten source-design files in
full.  I consumed the recorded R0 and R1 zero-write failures and checked the
final R2 repairs rather than treating an earlier snapshot as current.

## Repaired lock identity and byte hygiene

The reviewed object is experiments/source_lock.json.  Its exact current
identity is:

| Property | Value |
|---|---|
| SHA-256 | 226b90ec7367b73cbd481a67a08a38e5a471c0a9d9ac571e6905292587b59839 |
| Bytes | 11556 |
| LF | 1 |
| Mode | 0644 |
| Link count | 1 |
| Node type | ordinary regular file |
| Schema | paper26.source_lock.v1 |
| Logical terminal | PAPER26_SOURCE_LOCK_AUTHOR_STOP |

The file is valid UTF-8, has no BOM, CR, NUL, or invalid byte sequence, and
contains exactly one physical JSON line followed by exactly one terminal LF.
The file is neither a symlink nor a multiply linked regular file.

## Independent strict parsing and canonical reserialization

I used two independently implemented validation routes.

The Node route used a handwritten recursive-descent parser rather than
JSON.parse.  It rejects duplicate decoded keys at every nesting level, rejects
invalid number syntax and nonfinite values, checks string escapes and control
characters, and requires complete consumption of the single JSON record.  Its
canonical encoder recursively sorts object keys by Unicode code points,
preserves array order, uses compact separators, and emits one terminal LF.

The Ruby route used JSON parsing with a custom object class whose insertion
operation rejects a repeated key.  A duplicate-key adversary was rejected.
Its separately written recursive encoder sorts keys by their Unicode code-point
arrays, preserves arrays, emits compact JSON, and adds one terminal LF.

Both routes reproduced every one of the 11556 committed bytes.  This
simultaneously verifies recursive key order, compact separators, valid
strings/numbers, declared array order, absence of duplicate keys and nonfinite
numbers, and the physical-line convention.

The top-level schema and terminal match the author contract.  The self path is
bound as experiments/source_lock.json, while its own byte count and SHA-256
are null.  That exclusion is necessary and sufficient to avoid recursive
self-reference; the current lock identity is instead bound by the parent
ledgers and this review.

## Exact three-pointer repair provenance

I treated the author's repair claim as unproved.  Starting from the current
parsed value, I performed exactly these reverse operations:

1. remove top-level /next_requires;
2. replace /permissions/authorized_write_paths from false by the empty array;
3. add /permissions/next_requires with value
   parent_consumption_and_distinct_independent_source_lock_review.

Recursive canonical serialization of the resulting value produced exactly
11553 bytes with SHA-256
4783ec2c5eaadd0aba4733bd9d504d7dff46078816f363d6c828e1e1bba07c08.
Node and Ruby agreed byte for byte.

Equivalently, the old-to-current semantic delta consists of exactly:

| Operation | JSON pointer | Old value | Current value |
|---|---|---|---|
| add | /next_requires | absent | parent_consumption_and_distinct_independent_source_lock_review |
| replace | /permissions/authorized_write_paths | empty array | false |
| remove | /permissions/next_requires | parent_consumption_and_distinct_independent_source_lock_review | absent |

A recursive semantic diff found no fourth changed pointer.  Every theorem,
file, aggregate, candidate, source-review, inventory, scientific-execution,
unresolved-state, and self-exclusion value is therefore identical to the
superseded lock.

The repaired permissions object has exactly 21 keys.  Every value has JSON
Boolean type and is false.  The top-level next_requires value is exactly
parent_consumption_and_distinct_independent_source_lock_review.  It is
lifecycle metadata, not a permission.

## Eleven bound file identities

I recomputed every file identity from the live regular file, without trusting
the lock table:

| Relative path | SHA-256 | Bytes | LF | Mode | Links |
|---|---|---:|---:|---:|---:|
| experiments/EXPERIMENT_PLAN.md | 7b543388f7c12220aee27605b6cef53df48b7c835798a90495b4706b98a8355f | 15201 | 394 | 0644 | 1 |
| experiments/EXPERIMENT_TRACKER.md | c35c8cfba39bf8634e11ee91173b6fb2c313babe347ff30fdf0c5f445b65562d | 7987 | 105 | 0644 | 1 |
| notes/CITATION_VERIFICATION.md | 8ebb74149ce7d1eb22151019cd5a868e941df1c78b787ae605794a1c64011d09 | 8311 | 153 | 0644 | 1 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 56853a22b9a89e4599cad40a017d659aa50a6ecbf2cb3d52df080bd14b18d6f4 | 9076 | 75 | 0644 | 1 |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 974bcfea08dff87d359993839452eb271d2cf0edbbe2fb811abc17051aece92e | 17823 | 449 | 0644 | 1 |
| notes/NOVELTY_ASSESSMENT.md | 150573d9fe3cbddac7e49bdefc51ca687bd3b7dc51bbd2651f65b8947f1088a3 | 11496 | 185 | 0644 | 1 |
| notes/PROOF_PACKAGE.md | e17c0a801e3b19b0c090e96d69562492465ef96ac39fe3219cdeb193b4cd8f7d | 40986 | 1431 | 0644 | 1 |
| notes/RESEARCH_QUESTION.md | bb539d56e60987180c362d7d4b076785b40def15408aef08bf8b58403ee81bb4 | 9878 | 209 | 0644 | 1 |
| refine-logs/FINAL_PROPOSAL.md | 56447f2b98d64dc9c97b70f3731f03aa1c41ed68a459c07a178e1166320611ba | 10528 | 241 | 0644 | 1 |
| refine-logs/INITIAL_PROPOSAL.md | 65d4e90de9a9db2ea652c26c43a8114ef61f658efca14cb23ce9dd9d8a309711 | 6789 | 159 | 0644 | 1 |
| refine-logs/REVIEW_SUMMARY.md | c0f1576dcc3cc3587bc5c726ac6e70fa87f06f3225cf6e6d381e34933f9ff138 | 14062 | 213 | 0644 | 1 |

All eleven are valid UTF-8 regular files with one terminal LF, no BOM, CR, or
NUL, mode 0644 and one link.  Their array order equals ascending raw UTF-8
relative-path byte order.  Every relative path is normalized and remains
inside the project.

## Independent L11 and L12 aggregate reconstruction

For each path in raw-byte order, both validators constructed

u64be(path byte length) || path bytes ||
u64be(content byte length) || content bytes.

The independently reconstructed L11 aggregate is:

| Quantity | Value |
|---|---:|
| Files | 11 |
| Content bytes | 152137 |
| Content LF | 3614 |
| Path bytes | 329 |
| Framing bytes | 176 |
| Framed stream bytes | 152642 |
| SHA-256 | ffc0fa233057d556ffb3efd11fb78220d1bf8e957d8b8d8646ac416c1777f5fa |

This matches every aggregate field in the lock.

Before this review write, the complete project tree was exactly:

- 12 regular files;
- 3 directories, each mode 0755/link two;
- 0 symbolic links;
- 0 other nodes.

The regular files totaled 163693 content bytes and 3615 LF.  Their paths
contributed 357 bytes and their frames 192 bytes.  The complete repaired L12
stream had 164242 bytes and SHA-256
2a5f6f61a0516aa62635e8b0e0f146154d2bb4fe1289638e34ceef4de8ebd7d1
in both implementations.

The expected review path and every required future path were absent before
the write: paper, bibliography, code, data, figures, build, release, and
submission.  No hidden regular file, symlink, socket, device, or other node
was present.

## Field-by-field hypothesis audit

The lock freezes every theorem hypothesis used by the final R2 proof:

1. The base field has characteristic zero.
2. The position support is finite, nonempty, collected, and contained in
   the lattice region with both exponents at least two.
3. Every collected position coefficient is nonzero, with no positivity or
   common-sign assumption.
4. The momentum Hamiltonian is exactly the sum of two separated pure powers,
   with nonzero alpha and beta and derivative exponents e,f at least two.
5. The lower shear is S(q,p)=(q,p+grad(V)(q)), the upper shear is
   T(q,p)=(q+grad(W)(p),p), and F applies S before T.
6. The degree is ordinary total degree in the four initial coordinates.
7. Both forward and inverse coordinate-degree seeds are (1,1), and the
   ordinary-seed condition is explicit.

No hypothesis is dropped, weakened, or silently replaced by genericity.

## Independent reconstruction of the mathematical conclusions

### Symplecticity and inverse order

The two derivative matrices are lower and upper unitriangular blocks with
symmetric Hessian off-diagonal blocks.  Direct multiplication by the standard
symplectic matrix gives the symplectic identities.  Each shear fixes the
variables on which its added gradient depends, so its inverse uses subtraction.
Since F applies S and then T, the inverse applies T inverse first and S inverse
second.  These conclusions match the lock.

### Full-face cancellation certificate

For a positive exposed face polynomial P, choose the unique support point
(x0,y0) of minimum first coordinate.  A contribution to the exponent
X^(2x0-2)Y^(2y0-2) in det Hess(P) must pair two first coordinates summing to
2x0.  Minimality forces both to be x0, and uniqueness then forces both second
coordinates to be y0.  The resulting coefficient is

c_(x0,y0)^2 x0 y0 (1-x0-y0),

which is nonzero under the frozen coefficient, support, and characteristic
hypotheses.  This argument includes multi-point ties.  The characteristic-zero
Jacobian criterion makes the two face derivatives algebraically independent.
Injective substitution, nonzero scalar/sign changes, and separated positive
powers preserve that independence.  Therefore the nominal leading forms
survive every forward and inverse half-step, including subtraction phases and
full Newton walls.

### Exact transports and block visibility

With H and mathcal_A defined exactly as in the lock, the support lower bound
gives both components of mathcal_A(u) above every component of u.

The final R2 proof also supplies the cross-coordinate upper-phase step.  For
A=mathcal_A(u),

2A_1-A_2 = H-2u_1+u_2 >= 3u_2 > 0,

2A_2-A_1 = H+u_1-2u_2 >= 3u_1 > 0.

Since e,f are at least two, both components of BA exceed both components of
A.  Thus the fresh momentum block is visible after S and the fresh position
block is visible after T.  This proves the exact forward transport and
forward maximum in the lock.

In reverse order, Bv first dominates every carried position degree.  The next
full-face transform mathcal_A(Bv) dominates the whole fresh position block
and the old momentum block.  Its leading pair survives subtraction.  This
proves the exact inverse transport and inverse maximum separately.  The lock
does not infer inverse exactness from a fixed AB/BA spectral observation.

### Shifted bridge and rate boundary

For c_star=H((1,1))-1, homogeneity gives the stated base case and induction

u^+_(n+1)=c_star B v^-_n.

Diagonal norm comparison gives exactly the two-sided inequality recorded in
the lock and hence equality of first dynamical degrees.  The shift, ordinary
seed, scalar, and diagonal factor are all retained.  The lock also explicitly
states that this bridge proves vector and exponential-rate comparison, not
termwise degree equality and not a scalar-maximum recurrence.

### Uniform projective contraction

Projectivizing the forward transport gives the exact phi, Phi, and kappa
formulas in the lock.  On an active branch, differentiation gives a negative
derivative and logarithmic slope magnitude

r(x+y-1) /
(((x-1)r+y)(xr+y-1)).

The denominator gap is exactly the positive quadratic recorded by the lock.
For each support point the slope tends to zero at both logarithmic ends and
has supremum strictly below one.  Finiteness of the support gives one common
constant.  Continuity of the envelope and interval splitting patch the bound
across every wall.  Thus there is one fixed ray and no nontrivial numerical
periodic orbit.

The inverse ratio is evaluated after diagonal scaling: its Newton coordinate
is kappa times the inverse state ratio.  The displayed L-conjugacy in the lock
is exact.

### Selector and spectral rigidity

If the fixed ray lies inside a chamber, convergence eventually fixes that
selector.  If it is on a wall, strict decrease swaps sides while contraction
forces convergence; a strict orbit therefore alternates only the adjacent
chambers.  Injectivity prevents delayed landing.  A trajectory on the wall
uses the full tied face.  At a multiple tie, the two extreme active exponents
control the open sides.  The lock correctly distinguishes selector
alternation from a numerical two-cycle.

In an interior chamber the positive integral 2 by 2 selector matrix has the
fixed ray as its Perron ray, so its characteristic polynomial bounds the
algebraic degree by two.  At a wall, the primitive positive integral wall
ray is common to both adjacent integral matrices.  Their common multiplier is
rational and an algebraic integer, hence a positive integer.  The monodromy
Perron root is its square and the per-step value is the multiplier.  This
proves the lock's uniform quadratic cap and sharper wall statement.

### Forward and inverse scalar recurrences

For a forward interior tail, Cayley-Hamilton for C_xi=B A_xi gives the
coordinate law; convergence fixes the visible coordinate unless the ordinary
seed is the fixed ray, when the sequence is geometric.

The inverse proof is independent.  Its chamber matrix is

D_xi=A_xi B=B^(-1) C_xi B.

The active exponent is selected by the ratio of Bv.  Cayley-Hamilton for D_xi
and convergence of the inverse state ratio give the order-at-most-two scalar
law when the limiting inverse ratio is not one.  If it is one, the ordinary
seed is fixed from time zero and the degree is geometric.

For an inverse fixed-wall seed, the exact wall condition is that kappa times
the inverse ratio lies on the Newton wall, and Bv stays on the tied ray.  For a
strict inverse wall tail the limiting inverse ratio cannot be one.  The two
parity products

N_+=D_+D_- and N_-=D_-D_+

are respectively similar through B to the matching forward products.  Both
parities share trace tau and determinant Delta.  Visible-coordinate
stabilization on both parity tails then gives

d^-_(n+4)=tau d^-_(n+2)-Delta d^-_n

for all sufficiently large indices.  The same argument applies forward.
Every order is an upper bound.  These fields close the recorded R0
scalar-recurrence issue without using the bridge as the scalar proof.

### Exact fixtures

For E={(2,2)} and B=diag(3,2), the selector matrix is
[[3,6],[4,2]], with characteristic polynomial t^2-5t-18 and Perron value
(5+sqrt(97))/2.  The small-index vectors also reproduce the shifted bridge.

For E={(2,8),(4,5),(5,3)} and B=diag(24,11), the exact walls are 3/2 and 2.
The low, middle, and high matrices in the proof reproduce the stated transient
and the eventual middle/high selector alternation.  Both adjacent matrices
map (2,1) to 132(2,1).  Their ordered product has trace 17648, determinant
3902976, and eigenvalues 17424=132^2 and 224.  These are hand-checkable proof
fixtures, not numerical evidence.

## Anti-claim equivalence

The lock's 20 anti-claims jointly preserve every live boundary in the proof,
research question, claims matrix, proposal, and source-design review:

1. no axis-support extension;
2. no exponent-one extension;
3. no zero or uncollected coefficient extension;
4. no mixed momentum-Hamiltonian extension;
5. no positive-characteristic extension;
6. no dimension-at-least-three extension;
7. no unchanged bridge claim after altering phase order or seed;
8. no nontrivial numerical projective cycle;
9. no termwise forward/inverse degree equality;
10. no scalar-recurrence transfer from the bridge alone;
11. no minimal recurrence-order claim;
12. no higher dynamical-degree claim;
13. no entropy claim;
14. no compactification claim;
15. no integrability or nonintegrability claim;
16. no periodic or arithmetic point-orbit claim;
17. no classification or nonconjugacy claim;
18. no genericity substitute;
19. no optimal-support or dimension-free global quadratic-sharpness claim;
20. no global priority or firstness claim.

Nothing excluded by the source package is reopened by a conclusion string,
fixture, lifecycle field, or permission.

## Citation, novelty, lifecycle, and zero-authority audit

The citation ledger is contextual local metadata only.  It supplies no proof
step, incomplete metadata cannot enter a bibliography, and every record still
requires primary-record verification before publication.  The lock correctly
leaves final primary citation metadata unresolved.

The novelty assessment is local to Papers 1--25.  It does not establish an
external noncollision or priority result.  The lock correctly leaves global
novelty unresolved.

The lock binds the exact candidate identifier and title, both candidate
review identities and terminals, the source-design review identity and
terminal, the source-lock author gate, project path, sole author write, and
historical opening-ledger snapshots.  Those opening snapshots are author-time
provenance and are not incorrectly asserted to be the mutable current-ledger
identities.

All scientific-execution counters are zero.  Every permission is false,
including browse, network, CAS, numerics, scientific execution, source-lock
review, paper directory, manuscript, source trio, compilation, build,
temporary roots, release, submission, and external effect.  The current
review authority comes only from the later parent-ledger transition; the lock
does not self-authorize its review.

This review used no network, browser, CAS, numerical or scientific run,
compilation, build, temporary root, prohibited root, release action, or other
external effect.  It did not inspect or create paper, plan, bibliography,
source-trio, code, data, figure, build, or release artifacts.

## Final review conclusion

The source lock is a faithful canonical binding of the exact L11 theorem
package.  Its repaired field placement is exact, its inventory and aggregate
are reproducible, its theorem and anti-claim language neither omits nor
enlarges the current source design, and its permissions grant no successor
authority.  The proof status remains PROVABLE AS STATED under the frozen
hypotheses.

This artifact records only the independent lock-review result.  It does not
itself authorize manuscript planning or any later action; separate parent
consumption is mandatory.

PAPER26_SOURCE_LOCK_PASS
