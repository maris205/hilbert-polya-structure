# Narrative report

The elephant walk looks non-Markovian because each new increment recalls the entire past. Summing over the uniformly selected memory index nevertheless collapses the next-step law to the current position: its conditional drift is `(2p-1)S_n/n`. That reduction produces exact recurrences, but it does not erase the phase transition.

Writing `a=2p-1` and `G_n(c)=prod_{j=1}^{n-1}(1+c/j)`, the mean is `(2q-1)G_n(a)`. The second moment is a product quotient away from `a=1/2` and becomes `n H_n` exactly at the critical point. The usual martingale `S_n/G_n(a)` is valid only for `p>0`; at `p=0`, `G_n(-1)` vanishes after the first step, while `(n-1)S_n` is the correct martingale from time two.

The same threshold appears in the asymptotics. Below `p=3/4`, fluctuations are Gaussian on the square-root scale with variance `1/(3-4p)`. At the threshold the missing factor is `sqrt(log n)`. Above it, `S_n/n^(2p-1)` converges almost surely and in fourth mean. At `p=1` the limit is simply the initial sign, so the word “nondegenerate” must be qualified by `q`.

The exact computation closes finite identities and parser integrity. The asymptotic conclusions rest on analytic martingale arguments and the cited literature, not on the finite grid. Route A fails at every branch because no prime carrier, orbit ledger, zeta/divisor bridge, global arithmetic symmetry, or natural quantization is present.
