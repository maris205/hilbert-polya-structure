# C78 experiment plan

## Source binding

Read C73, C75, C76, and C77 authorities as raw bytes before deriving any
repair statistic.  Keep the fixed labels, point-set group law, and closure
convention unchanged.

## Exact computation

For each deletion set \(D\), retain \(A=L\setminus D\), enumerate restorations
\(R\subseteq D\) and record
\(\rho(D)=\min\{|R|:R\subseteq D,\Phi(A\cup R)=Q\}\).  The producer
accumulates the structural formula over all \(2^{16}\) masks; the independent
checker reconstructs the point-set closure and evaluates the minimum from the
complete set of 25 full-core minimal supports.  Both routes accumulate the
exact deleted-count by repair-distance table.

The checks are \(\rho\leq3\), \(P(x,1)=(1+x)^{16}\), and
\(P(1,y)=30400+32704y+2368y^2+64y^3\), with \(x\) marking deletions.

The independent checker, replay, hostile mutation test, and deterministic
paper builds are separate release gates.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
