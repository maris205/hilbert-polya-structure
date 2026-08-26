# Hostile mathematical audit

This audit was performed before release drafting and repeated after the
round-two manuscript.

## Attacks and resolutions

1. **Could (F^5=I) be a sample-only coincidence?**  No.  Every coordinate
   of (F^1,\ldots,F^5) was simplified as a rational function, ending
   identically at ((x,y)) on the full positive domain.
2. **Could there be a second fixed point?**  Algebraically there are two
   roots of (x^2-x-1=0), but the negative root is outside (X).  The
   positive root (\phi) is unique.
3. **Could an intermediate least period occur?**  No.  Least periods divide
   five, which is prime; hence only one or five occur.
4. **Could one write (\#\operatorname{Fix}(F^5)=1) by counting connected
   components or quotient orbits?**  No.  The Artin--Mazur definition counts
   fixed points, and (F^5) fixes every point of an uncountable continuum.
   No substitute count is introduced.
5. **Could the primitive period-five orbits still form a finite Euler
   product?**  No.  Removing one point and quotienting by finite orbits
   leaves an uncountable family.
6. **Is (dx\,dy/(xy)) really invariant?**  Yes.  The exact identity
   (|\det DF|/(F_1F_2)=1/(xy)) was reconstructed independently.
7. **Is the projection sign correct for (Uf=f\circ F)?**  Yes.
   (P_j=5^{-1}\sum_r\omega^{-jr}U^r) satisfies
   (UP_j=\omega^jP_j); the opposite sign selects the conjugate eigenspace.
8. **Does infinite-dimensional (H) alone prove infinite multiplicity of
   every eigenvalue?**  No.  The proof instead constructs countably many
   disjoint positive-measure orbit tubes and localizes each cyclic Fourier
   projection on them.
9. **Could (U) nevertheless be compact or trace class?**  No.  Each
   nonzero fifth root has infinite multiplicity, violating compactness;
   every finite Schatten class is compact.
10. **Could (U) be self-adjoint?**  A self-adjoint unitary satisfies
    (U^2=I); combined with (U^5=I) this forces (U=I), contradicted by
    the nontrivial map on a positive-measure neighborhood.
11. **Does a natural Koopman lift establish Hilbert--Pólya?**  No.  It is an
    order-five unitary with infinite root-of-unity multiplicities, not a
    self-adjoint target-spectrum Hamiltonian.
12. **Do finite sentinels prove the theorem?**  No.  Their only role is
    regression detection for the separate exact proof.

## Verdict

The paper survives as a complete obstruction theorem.  The model is
rejected as a primary Route-A candidate but records a natural, precisely
delimited A4 Koopman lift.  No dynamics pivot was needed because this
negative theorem is itself decisive subtype progress.
