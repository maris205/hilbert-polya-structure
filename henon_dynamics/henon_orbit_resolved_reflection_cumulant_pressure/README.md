# HCS-P69: Orbit-resolved reflection cumulant pressure

For P65's natural defect chi=1{s[-1]=s[1]}, P69 proves

    F_(2m+1)(q)=2q(1+q^2)^m

for the full odd reflection packet and the exact primitive law

    E_n(q)=sum_(k|n) mu(k) F_(n/k)(q^k).

Consequently the orbit-resolved primitive pressure is

    P_orb(s)=(1/2)log(1+exp(-2s)).

P68's aggregate-mean pressure is (1/2)log2-s/2, so the exact gap is
(1/2)log cosh(s), strictly positive for s nonzero. Thus P69 recovers the full
cumulant information erased by mean-field averaging.

**Status:** packet polynomial, primitive law, pressure, and gap PROVED;
arithmetic trace OPEN; Route A exploratory; Route B not authorized. Reproduce
with bash code/run_c69.sh and see paper/paper.pdf.
