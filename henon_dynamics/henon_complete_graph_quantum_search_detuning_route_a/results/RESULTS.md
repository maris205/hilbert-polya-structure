# C323 results

| object | audited size | result |
|---|---:|---|
| interior parameter rows | 3,472 | full bright/dark multiplicities, exact splitting, peak law, and resonance flag pass |
| driver values | 7 | `0,1/4,1/2,1,3/2,2,4` reconstructed exactly |
| critical-window rows | 28 | four integer `k` values and seven signed detunings pass |
| boundary rows | 256 | `M=0`, `M=N`, `N=1`, and `g=0` faces pass without negative multiplicities |
| audited scalar leaves | 75,296 | exact enumeration and content hash pass |

Evidence payload SHA-256:
`62eb673eebbc522e5bd3efbe0fd1c61d0bb1f98a415ebfbcc5a068ccda7b5bac`.

Evidence file SHA-256:
`7ff0d9d8b6d61a62ed8b5c6694894f82e2302c0261355def61110240d4087714`.

The analytic interior domain is every `N>=2`, `0<M<N`, and `g>=0`; the
declared faces cover every `N>=1` and `0<=M<=N`.  Finite rows are regression
and hostile-boundary evidence, not the domain of the theorem.
