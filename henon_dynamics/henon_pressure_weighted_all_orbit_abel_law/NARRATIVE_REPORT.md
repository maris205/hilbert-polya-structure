# Narrative report

P52 showed that one exact H6 packet has a totient-controlled Abel boundary,
but it could not pass the boundary through the all-orbit pressure sum.  The
apparent problem was the lack of a remainder estimate uniform in the orbit.

P53 separates two tasks.  First, for each frozen orbit it identifies the
correct coefficient: the logarithmic Mahler measure of the complete signed
multiplier polynomial.  Conjugates outside the unit circle give a bounded
cyclotomic correction.  Unit-circle conjugates are controlled by a
two-logarithm estimate, giving an orbit-dependent
\(O(\sqrt n\log^2 n)\) remainder.  This is enough for the one-orbit Abel
limit.

Second, the proof does not attempt to make that remainder uniform in the
orbit.  It instead normalizes the whole positive packet by \(\tau^2\) and
uses the much cruder P51 bound \(b_{\gamma,n}\le K_m n\).  The normalized
sum of \(ne^{-\tau n}\) is uniformly bounded, and the remaining period
majorant is exactly the convergent P51 pressure series.  Dominated
convergence therefore closes the full all-orbit exchange.

The resulting boundary has two natural scalar descriptions.  Its analytic
amplitude is the pressure Dirichlet series of Mahler heights.  Its
probabilistic compactification is a product of the pressure-height orbit law
and \(\Gamma(2,1)\) on the blown-up cyclotomic index.  Neither is a
source-tagged divisor vector: the positive tagged vectors still escape every
norm and weak boundary.

The next major object is now sharply isolated: the thermodynamic analytic
behavior of the Mahler-height orbit series as \(s\) approaches a pressure
boundary.
