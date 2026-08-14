# HCS-C50 test report

Release-candidate runner result: **PASS**.

- Independent checker: 16/16 exact gates passed.
- Isolated mutation suite: 53/53 tests passed; every mutation forced its named
  gate to `FAIL`, and no mutation produced an `ERROR`.
- Literal chronology was independently replayed at p=7,13,19,31.
- Certificate SHA-256:
  `ef77b61758ccaf59e2e24e79dc535e2216d794843ff5f16ae0ca4ded12eb9dde`.
- Independent-check SHA-256:
  `c561c81e2dbacc37baaf4bed769ae635246b1dab0fa56f748666ba41f3e43fbb`.
- Canonical payload SHA-256:
  `d2d78b6992d97bada0119416171d9d091f6d04eb9bcf93d9a71427f2589aed6a`.

The final manifest is generated only after these provenance hashes are copied
into the integrity report.  It inventories the frozen root documentation,
Route-A root/archive pair, paper sources/PDF/compilation report, code, and
results.
