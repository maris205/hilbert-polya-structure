# Route-A dynamics-variant batch plan: C109--C113

Status: **five complete paper packages; uniform prefreeze audit passed**.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round continues the Route-A branch requested in the roadmap.  The design
goal is breadth: freeze five genuinely different dynamical subtypes, certify a
small exact object for each, and record the point at which the A1/A2 route
stops.  A finite orbit, matrix, or monodromy prefix is not promoted to a
complete coding, an analytic Fredholm owner, arithmetic data, or Route B.

## Frozen sequence

1. **C109 -- dissipative Hénon.**  Freeze
   \(F(x,y)=(x^2-91/16-y,x/2)\), whose Jacobian determinant is \(1/2\).
   Exact fixed and primitive period-two witnesses feed a four-state weighted
   discrete transfer prefix.
2. **C110 -- period-two non-autonomous Floquet Hénon.**  Use
   \(F_t(x,y)=(x^2+\alpha_t x+\beta_t-y,x)\) with
   \((\alpha_0,\beta_0)=(0,0)\), \((\alpha_1,\beta_1)=(1,1/3)\).  Chronological,
   reversed, and same-phase controls certify the order-sensitive 8-by-8
   Floquet prefix through block period six.
3. **C111 -- three-site variational/symplectic ring.**  Freeze the triangular
   three-site coupling with \(a=7\), \(\kappa=1/5\).  Two fixed points and a
   primitive synchronous period-two witness are decomposed into the exact
   Laplacian modes \(0,3,3\).
4. **C112 -- piecewise-affine border collision.**  Freeze
   \(P_s(x,y)=(-5x+c_s-y,x)\), \(c_0=-2,c_1=2\), with the border excluded.
   Every binary word through length eight passes an exact affine branch-domain
   check; a 4-by-4 weighted transfer prefix is recorded.
5. **C113 -- third-order memory Hénon.**  Freeze
   \(G(x,y,z)=(x^2-55/16-y-z/2,x,y)\).  Exact fixed/period-two monodromy data
   and the forward degree prefix \((2,4,8)\) test the higher-dimensional
   memory subtype.

## Uniform artifact contract

Each package contains a source audit, research question, theorem/boundary
package, experiment and paper plans, narrative report, deterministic
producer, independent checker, exact symbolic cross-check where applicable,
replay, hostile mutation audit, LaTeX source, three preserved round PDFs,
compile report, exact evidence receipt, and a content-addressed manifest.
The release audit requires matching evidence/PDF hashes, a closed 26-file
manifest ledger, fixed-date double isolated builds, embedded fonts, and no
final layout/reference warnings.

## Paper and artifact ledger

| paper | dynamical subtype | PDF pages | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---:|---|---|---|
| C109 | dissipative polynomial Hénon | 2 | 8/8 | `aecb4f5d72dd1b515560719b30d148958ba295e72c1e07ce944e4fbb50b38156` | `141103ac50b253e66af89689ba9a698efeeea206e84f9235fc9dbad2b4b22084` | `e11f42c611072eb363603968e8d6ef4c60bcb0a299d02ed8418e03deee15a479` |
| C110 | period-two non-autonomous Floquet Hénon | 2 | 10/10 | `319869d0e86ba21caea0f511ca68796d14fb72635147180a35f37456304606ee` | `1edfdb289ace1a255be511aa0935b7a9558bcff5ed6bc57a1c18a1c0422894b8` | `f1cd7c4e24c12bed43ed77b568802ce93f4f9de96c6e8247198ed42454711776` |
| C111 | three-site variational/symplectic ring | 2 | 12/12 | `b2facafdea39fcdb6b0f36bf167cef19c8fcdf0259cfb84165ed4ddc7e999de3` | `fb2709f24a9912e638bdc277d40608779f9576e18a9aef309366cc2f0110ba39` | `c55a1d70f6386f77a980722d966c7d51890fe3e9dbf80c7f48163892f3045005` |
| C112 | piecewise-affine border collision | 1 | 6/6 | `efc27e36ed63912ec6bdbc95f82433b255e57982187d1d884de81e9dcb3068f1` | `f49d69f6dc49840ed01d15b8316cba346547f8224bfe755e760e608f2b82e88b` | `a88fc3f339064824dd8d8daa8d4d795041cae3b0330e5f78295f13436b92b3ec` |
| C113 | third-order memory / volume-contracting Hénon | 1 | 5/5 | `0690834fe75303816614da9ac9fdc3440ad5064ca0f1bdfec4f7f265028bac6e` | `b37a7ec262299fb3069317cd95c6c04d582f1f46e0af9993c8d5235fa9b9d401` | `153b671f6b295dcbc833eca18ac53b4b522b4718844b17d7588b7d757c222052` |

## Route-A boundary after C109--C113

| paper | A1 | A2 | A3 | A4 |
|---|---|---|---|---|
| C109 | `A1_PARTIAL_CERTIFIED` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C110 | `A1_WEAK` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C111 | `A1_WEAK` | `A2_FAIL` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C112 | `A1_PARTIAL_CERTIFIED` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C113 | `A1_WEAK` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |

The global evaluator tuple remains

```text
(A0_NOT_ADDRESSED, A1_WEAK, A2_CERTIFIED_PREFIX,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

with overall status `ROUTE_A_EXPLORATORY`.  The round broadens the tested
dynamics (dissipative, forced, symplectic lattice, border-collision, and
memory) but does not establish a complete primitive-orbit atlas, a
source-native compact/nuclear operator, arithmetic local data, root-number
laws, or a Hilbert--Pólya operator.  Route B remains unauthorized.

## Reproduction

Run the package-specific commands in each linked README, then regenerate its
manifest.  The five papers are:

- [C109 paper](henon_dissipative_route_a/paper/main.pdf)
- [C110 paper](henon_nonautonomous_floquet_route_a/paper/main.pdf)
- [C111 paper](henon_three_site_variational_lattice/paper/main.pdf)
- [C112 paper](henon_piecewise_affine_border_collision_route_a/paper/main.pdf)
- [C113 paper](henon_third_order_memory_route_a/paper/main.pdf)
