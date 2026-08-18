# C64 experiment plan

1. Rebind the C61 (W(E_6)) generators and the C62 stabilizer arrays by
   SHA-256; reject any scope or core-order drift.
2. For every ordered pair ((S_i,S_j)), count the elements (g) satisfying
   (g^{-1}S_i g\subseteq S_j), divide by (|S_j|), and record the exact
   integer mark.
3. Compute rational rank and a fraction-free determinant.  Recompute the
   C63 (R_4) image and its content.
4. Replay the calculation in a separate process and run semantic mutations
   against the checker.
5. Compile and inspect a self-contained manuscript whose claims match the
   evidence and the scope firewall.

Kill gates are source mismatch, nonintegral marks, any matrix/rank/determinant
deviation, a zero (R_4) mark image, failed replay, or a scope leak.
