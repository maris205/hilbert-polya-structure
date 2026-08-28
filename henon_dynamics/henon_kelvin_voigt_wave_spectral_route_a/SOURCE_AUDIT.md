# Source audit

Primary source metadata checked against publisher records:

- B. Z. Guo, J. M. Wang, and G. D. Zhang, “Spectral analysis of a wave equation with
  Kelvin--Voigt damping,” *ZAMM* 90 (2010), 323--342, DOI
  `10.1002/zamm.200900275`.
- Jing Wang and Jun-Min Wang, “Spectral analysis and exponential stability of
  one-dimensional wave equation with viscoelastic damping,” *J. Math. Anal.
  Appl.* 410 (2014), 499--512, DOI `10.1016/j.jmaa.2013.08.034`.
- S. Cox and E. Zuazua, “The rate at which energy decays in a damped string,”
  *Comm. PDE* 19 (1994), 213--243, DOI `10.1080/03605309408821015`.
- P. Freitas and J. Lipovský, “Spectral determinant for the damped wave
  equation on an interval,” *Acta Phys. Pol. A* 136 (2019), 817--823, DOI
  `10.12693/APhysPolA.136.817`.

The cited papers provide spectral and damping context.  Here “essential
spectrum” means the Weyl singular-sequence spectrum: normalized vectors
converging weakly to zero whose residual under the generator minus the
candidate point tends to zero.  The present package proves its normalized
sine-mode root, essential-accumulation, gap, and energy claims directly, makes
no priority assertion, and does not import a uniform operator-norm estimate at
a Jordan boundary.
