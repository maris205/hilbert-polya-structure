# Research question

For a finite open network of single-server exponential queues, with positive
external Poisson rates and a substochastic routing matrix \(P\) satisfying
\(\rho(P)<1\), can one prove in one convention-locked theorem:

1. the exact necessary-and-sufficient positive-recurrence condition;
2. the unique product-geometric stationary distribution;
3. the exact parameters of the stationary time-reversed network; and
4. the joint Poisson law of external departure streams, including the correct
   independence direction relative to the present queue state?

Yes. With row-vector traffic convention
\(\lambda=\alpha+\lambda P\), positive recurrence is equivalent to
\(\lambda_i<\mu_i\) for every node. In that chamber the invariant law is
\(\prod_i(1-\lambda_i/\mu_i)(\lambda_i/\mu_i)^{x_i}\), and stationary reversal
is again Jackson with the parameters stated in the theorem package, using the
natural extended convention that permits zero reverse exogenous rates. The
rate calculation concerns the visible marked-jump path; state-preserving
phantom self-routing marks can be restored at their conditional rates but are
irrelevant to external outputs. Reversal turns external departures before the
present time into future exogenous arrivals, proving their joint Poisson law
and independence from the present state. The theorem deliberately makes no
joint-independence assertion about all internal routed flows.
