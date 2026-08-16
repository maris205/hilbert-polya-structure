# HCS-P70: Orbit-resolved reflection Euler boundary

P70 restores one Euler factor for every primitive marked reflection word:

    Z_orb(z,q)=product_(n odd)product_(omega in A_n)
               (1-z^n q^(S_n chi(omega)))^(-1).

It proves the exact logarithmic derivative, the moving positive-weight radius

    R(q)=(1+q^2)^(-1/2),

and an exponential essential singularity at R(q). The mean-field radius is
(2q)^(-1/2), and their ratio is
1/sqrt((q+q^(-1))/2), strictly below one unless q=1.

**Status:** product, coefficient ledger, radius, and boundary type PROVED;
relative Lind determinant OPEN; arithmetic advance NO; Route B not
authorized. Reproduce with bash code/run_c70.sh and see paper/paper.pdf.
