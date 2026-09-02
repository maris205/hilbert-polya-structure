# Test report

The strict checker uses duplicate-rejecting JSON and YAML loaders, exact nested schemas and primitive types, a fixed YAML semantic hash, unique complete grids, independent bisection, both triangular Hessian signs, raw Jacobian characteristic data, and all four exact critical ranks.  Expected signatures are 781 checker assertions, 46 SymPy checks, and 65/65 rejected mutations.

The release gate regenerates evidence, runs all five evidence lanes, verifies the exact Route-A YAML semantics and the 27-payload/28-physical ledger, and builds each substantive revision twice in fresh directories with two LuaLaTeX passes.  Settled logs, text extraction, page counts, embedded subset fonts, and byte determinism are hard gates.
