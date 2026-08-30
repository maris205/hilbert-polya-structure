# Narrative report

Between jumps the state rises linearly.  If (Y_n) is the value just before a
jump, the post-jump state is (beta Y_n); integrating the rate (rho X_t)
over a waiting time (T) gives

\[
 rho(beta Y_nT+aT^2/2)=E_{n+1},
 \qquad Y_{n+1}=beta Y_n+aT.
\]

Completing the square is the decisive step:
(Y_{n+1}^2=beta^2Y_n^2+2aE_{n+1}/rho).  The squared jump chain is therefore a
contractive affine perpetuity.  Its infinite product is a Laplace transform
of the source probability law; the release uses a finite rational prefix and
never calls it an Euler factor.

For (beta>0), common-noise coupling contracts two squared chains by
(beta^2) per jump, proving uniqueness and convergence of the stationary
jump-chain law; its finite mean \(E[Z_\infty]=(2a/rho)/(1-beta^2)\) gives
almost-sure finiteness.  Continuous-time moments satisfy the generator recurrence and
the Laplace identity \(\varphi'(s)-\varphi'(beta s)=(a/rho)s\varphi(s)\), and
are reconstructed from the stationary Markov-renewal/Palm occupation ratio.
The embedded sequence is Markov, not iid regenerative.  The six-step rational
hazard skeleton audits the reward integral independently of random sampling.

The faces (beta=0,beta=1,a=0,rho=0) are kept explicit.  Only the reset
face (beta=0) is genuinely regenerative; its Rayleigh pre-jump law and
half-normal continuous occupation density are explicit.  The absence of an arithmetic
carrier forces A0, A2, and A3 to fail, with only a formal A4 hint.
