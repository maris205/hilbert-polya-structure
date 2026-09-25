# Scope card — ASFS-SCOUT-20260914-83

| Field | State |
| --- | --- |
| Frozen rule | \(a_1=1\), \(a_n=a_{n-1}+\operatorname{lcm}(n,a_{n-1})\) for \(n\ge2\); \(b_n=a_n/a_{n-1}-1\) | one fixed arithmetic recurrence |
| Equivalent increment | \(b_n=n/\gcd(n,a_{n-1})\) | exact source identity; hence \(b_n\mid n\) |
| Faithful action | \((n,a)\mapsto(n+1,a+\operatorname{lcm}(n+1,a))\) after the harmless indexing convention is fixed | step coordinate strictly advances |
| Prime claim | every \(b_n\) is \(1\) or prime | conjectural; source ties it to an unproved strong Linnik-type condition |
| Prime-symbolic lineage | arithmetic divisibility recurrence only | no documented sieve/admissibility-to-Logistic/Hénon/conservative deformation |
| Recurrent packet | none in the faithful forward action | exact nonreturn from the step coordinate |
| Symplectic base, roof, suspension, analytic owner | none | PRE-P0 stop |
| Route state | A0 `NOT_TESTABLE` as a full prime generator; A1 scoped FAIL; Route B `NOT INVOKED` | no transfer |
