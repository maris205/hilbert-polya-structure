# Source audit — HCS-C248

The two primary sources were checked by publisher/DOI landing pages on
2026-08-30.

* Walter Rudin, “Some theorems on Fourier coefficients,” *Proceedings of the
  American Mathematical Society* 10 (1959), 855–859,
  DOI [10.1090/S0002-9939-1959-0116184-5](https://doi.org/10.1090/S0002-9939-1959-0116184-5).
  This is the primary Fourier-analytic source for the Rudin–Shapiro polynomial
  construction and square-root estimate.
* Michael Baake and Uwe Grimm, “Kinematic diffraction is insufficient to
  distinguish order from disorder,” *Physical Review B* 79, 020203(R) (2009),
  DOI [10.1103/PhysRevB.79.020203](https://doi.org/10.1103/PhysRevB.79.020203).
  Its Rudin–Shapiro example derives the pair-correlation recursion,
  \(\gamma_{RS}=\delta_0\), and Lebesgue diffraction.
* Michael Baake and Uwe Grimm, “Erratum: Kinematic diffraction is insufficient
  to distinguish order from disorder,” *Physical Review B* 80, 029903(E)
  (2009), DOI [10.1103/PhysRevB.80.029903](https://doi.org/10.1103/PhysRevB.80.029903).
  The manuscript uses the corrected \(a_{4m}\), \(a_{4m+3}\), and
  \(b_{4m+2}\) signs from this erratum; the checker locks all three strings.

The package does not claim that either source establishes a target arithmetic
correspondence.  Every numerical item in `results/c248_rs_evidence.json` is
generated with integer operations and is re-derived by a separate checker and
an exact SymPy program.  The frozen source commit is
`5f357e2d2b78604f6c286bfbd05da922e1d6791f`; evaluator authority is locked to
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
