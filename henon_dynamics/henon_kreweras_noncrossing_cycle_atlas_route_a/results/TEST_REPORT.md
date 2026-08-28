# Test report

| Test | Scope | Expected |
|---|---|---|
| producer | closed formula ledger, `n<=24` | `C209_PRODUCER_PASS` |
| checker | independent formulas and direct NC enumeration, `n<=8` | `C209_CHECK_PASS` |
| SymPy | q-Catalan roots, `n<=12`; period/spectrum, `n<=24` | `C209_SYMPY_PASS` |
| replay | byte identity | `C209_REPLAY_PASS` |
| mutation | 32 repaired-hash + 1 stale-hash payloads | `C209_MUTATION_PASS` |

The checker verifies K^2=rotation by -1, all polygon-reflection reversors,
rank complement, fixed counts, Möbius populations, cycle factors, spectra, and
all coordinate ledgers.  No numerical fitting or target data are used.
