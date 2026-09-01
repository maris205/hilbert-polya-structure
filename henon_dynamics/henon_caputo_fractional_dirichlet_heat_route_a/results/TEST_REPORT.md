# C277 test report

The producer uses 90-digit defining-series values only on `x<=1`.  The
checker reconstructs them independently in double precision and separately
uses SciPy's scaled complementary error function for the large-argument
`beta=1/2` long-time ledger.  Exact rational comparisons audit the declared
`theta>=0` smoothing domain and the smoothing and Schatten endpoints; the
contract separately records the bounded out-of-domain `theta<0` case.  SymPy
rederives the sine eigenbasis, Caputo series
coefficient shift, and beta-half tail constant.

Release requires fresh byte replay, repaired-hash semantic mutations, three
substantively distinct and deterministic manuscript rounds, final=round2,
embedded/subset fonts, warning-free logs, and exact 27-payload manifest
closure.  Counts and hashes are recorded by the final manifest command.
