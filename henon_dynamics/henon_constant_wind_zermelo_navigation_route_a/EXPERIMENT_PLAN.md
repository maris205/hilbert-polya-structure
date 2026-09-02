# Evidence and validation plan

## Receipt atlas

- Use 29 exact rational cases spanning zero wind; generic weak wind;
  reachable and unreachable critical targets; strong-wind interior,
  Mach-cone boundary, exterior, and backward targets; zero cap; degenerate
  zero velocity; and the zero target in all chambers.
- Record rational invariants \(w^2,p,r^2,a,D\), chamber and reachability,
  72-digit minimum times, complete attainable-time intervals, constant
  controls, speed saturation, and terminal residuals.
- Independently audit 12 smooth-domain gradients, HJB residuals, target
  homogeneity, and common-velocity scaling.

## Release gates

1. Canonical producer with self-excluding payload SHA-256.
2. Independent checker with strict exact keys, types, lists, IDs, rational
   and decimal syntax, duplicate/nonfinite rejection, and full YAML tree.
3. Independent SymPy lane for the quadratic, both roots, scaling, HJB, and
   Mach-cone identities.
4. Two isolated byte-for-byte producer replays.
5. Repaired-hash semantic mutations plus hostile JSON/YAML parser attacks.
6. Three round variants built twice in fresh fixed-epoch directories, with
   `main.pdf` checked as the byte-identical round-2 alias, plus warning, page,
   font, text, raster, and exact-ledger audits.

Finite results are regression tests only; equation (1) proves every
dimension and parameter chamber.
