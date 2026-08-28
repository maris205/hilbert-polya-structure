# HCS-C220 experiment and evidence plan

## Frozen theorem

Use the open continuous-time TASEP with \(L\geq0\), injection rate
\(\alpha\geq0\), unit bulk hopping, and extraction rate \(\beta\geq0\).
For \(\alpha,\beta>0\), certify the DEHP matrix-product measure, the
normalization \(Z_L\), the uniform stationary current, and the exact
finite-size ratio \(J_L=Z_{L-1}/Z_L\).  State the LD/HD/MC, coexistence, the
two critical faces, their multicritical corner \(\alpha=\beta=1/2\), and the
positive-rate coexistence line \(0<\alpha=\beta<1/2\) analytically.  Treat
the \((0,0)\) endpoint and all other zero-rate faces in the separate boundary
theorem, together with \(L=0,1\).

## Reproducibility ledger

The producer enumerates \(L=0,1,2,3,4,5,6,8\), five-by-five positive rational
rate pairs
\(\{1/4,1/2,3/4,1,3/2\}^2\), and five boundary pairs including
\((0,0)\).  Every interior configuration weight, exact normalization,
current on each bond, and stationary residual is serialized as a rational
string.  Larger rows use the irreducibility theorem for the nullity field;
the independent checker performs exact nullspace computations with SymPy for
all rows through \(L=4\), while independently checking residuals for every
row.

## Gates

1. Producer emits a content-hashed JSON payload.
2. Checker rebuilds the algebra, generator, currents, and nullspaces without
   importing producer code.
3. SymPy cross-check verifies every short-word DE relation, the closed
   normalization, the equal-rate limit, and symbolic stationarity/current
   identities.
4. Replay regenerates the JSON in a clean process byte-for-byte.
5. Repaired-hash, stale-hash, schema, scope, and overclaim mutations are all
   rejected.
6. LuaLaTeX is run at SOURCE_DATE_EPOCH=1787875200 for three content-changing
   revisions.  The final PDF is rebuilt twice and checked for page count,
   embedded fonts, text anchors, and sidecar cleanup.

The finite ledger is an audit sentinel.  It is not used as numerical proof of
the thermodynamic phase diagram and does not establish literature priority.
