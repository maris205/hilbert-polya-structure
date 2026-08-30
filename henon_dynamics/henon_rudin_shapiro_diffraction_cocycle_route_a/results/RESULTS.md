# Results — HCS-C248

The exact producer receipt contains 11 dyadic polynomial rows (depths
0–10; 4,094 coefficient cells), 9 substitution-frequency rows, 8 four-product
Laurent correlation rows, and 64 finite aperiodicity mismatch witnesses.  The
length-1024 fixed-point prefix is generated from the four-letter rules, and
the coded signs agree with every dyadic \(P_k\) prefix.

The substitution matrix has a positive third power.  Each dyadic row has
\(\|P_k\|_2^2=\|Q_k\|_2^2=2^k\), total energy \(2^{k+1}\), and the exact
unit-circle bound squared \(2^{k+1}\).  All four Laurent recurrences are
checked coefficient-by-coefficient.  Separately, the all-integer 4-adic
recursion for the infinite-volume coefficients \(a_m,b_m\) is stated and
proved in the paper; its unique solution is \(a=\delta_0,b=0\).  Hence
\(\gamma_{RS}=\delta_0\), \(\widehat\gamma_{RS}=\lambda\) under symmetric
Cesàro/van Hove averaging.

The receipt is not an orbit atlas: the hull is aperiodic.  Route A therefore
remains `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and is rejected.
