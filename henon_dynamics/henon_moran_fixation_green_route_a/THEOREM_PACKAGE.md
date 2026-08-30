# Theorem package

For N>=2, rho>0, beta>0, let X_t in {0,...,N} have transient rates
lambda_i=beta rho i(N-i)/N and mu_i=beta i(N-i)/N.  States 0 and N absorb.

**Theorem (Moran atlas).** Absorption at 0 or N occurs almost surely.  The
fixation probability from i is
u_i=(1-rho^(-i))/(1-rho^(-N)) for rho != 1 and u_i=i/N for rho=1.
Writing Q for the (N-1)-by-(N-1) transient generator,
G=(-Q)^(-1) is the exact occupation Green matrix and
t_i=sum_j G_ij is the expected absorption time.  The killed chain is
reversible after diagonal symmetrization with
w_{i+1}/w_i=rho*i(N-i)/((i+1)(N-i-1)).
The beta=0 face is frozen and has infinite absorption time; N=1 has no
transient state and is already absorbed.

The receipt contains eight parameter rows, full Green matrices up to N=10,
four boundary faces, and ten exact identities.  The checker, SymPy, replay,
and hostile mutation suite are independent of the producer.
