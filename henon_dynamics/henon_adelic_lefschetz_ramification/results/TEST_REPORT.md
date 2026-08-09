# Test report

Command:

```bash
./code/run_c23.sh
```

Environment:

- Python 3.12.3
- NumPy 2.3.5
- SymPy 1.14.0
- no random seed or floating-point gate

Results:

- exact producer: pass;
- nonimporting checker with an independent rank backend: 12/12 checks pass;
- structural mutation suite: 11/11 tests pass.

Independent recomputation uses SymPy finite-field `DomainMatrix` ranks,
whereas the producer uses its own exact modular Gauss--Jordan elimination.
Direct rational-point enumeration independently verifies the two explicit
nontransverse fixed points.

Mutations rejected:

- chronological averaging;
- reversal quotienting;
- replacement of a certified word pair;
- false identification of a dihedrally equivalent pair;
- deletion of a decisive packet event;
- premature Zsigmondy and Euler-product claims;
- deletion of the cyclic-resultant baseline;
- an unfocused continuation to the cancelled large ledger;
- conflation of modular kernel dimension with norm valuation.
