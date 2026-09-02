# HCS-C299 research question

For the planar vorticity equation

\[
\partial_t\omega+u\!\cdot\!\nabla\omega=\nu\Delta\omega,
\qquad \nabla\!\cdot u=0,\qquad \operatorname{curl}u=\omega,
\]

classify every radial forward-self-similar solution of the form
\(\omega(x,t)=\tau^{-1}F(|x|/\sqrt\tau)\), \(\tau=t+\tau _0>0\), in the explicitly declared class
\(F\in C^2([0,\infty))\), bounded at the origin, with
\(\int_0^\infty |F(\xi)|\xi\,d\xi<\infty\).  Then determine, over the full parameter set
\(\Gamma\in\mathbb R\), \(\nu>0\), \(\tau_0\ge0\):

1. the velocity and every positive-radius Lagrangian trajectory;
2. all even radial moments and finite \(L^p\) norms;
3. the exact enstrophy--palinstrophy dissipation law;
4. the zero-circulation, zero-age, inviscid, origin-particle, long-time, recurrence, and energy boundaries;
5. the resulting Route-A tuple under `NO_BAD_EULER_OR_ROOT_NUMBER`.

The question does **not** ask for uniqueness among arbitrary vorticity solutions or arbitrary vortex filaments.  It asks for a complete theorem within the stated radial similarity class.
