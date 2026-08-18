# Exact Witness Ledger

## Support and valuation witnesses

| Witness | Sum | Valuations | Result |
|---|---:|---:|---|
| \((1,1)\) | \(2\) | \(0,0\) | loop |
| \((1,3)\) | \(4\) | \(0,0\) | edge |
| \((2,2)\) | \(4\) | \(1,1\) | loop |
| \((2,6)\) | \(8\) | \(1,1\) | edge |
| \((3,5)\) | \(8\) | \(0,0\) | edge |
| \((4,4)\) | \(8\) | \(2,2\) | loop |
| \((1,5)\) | \(6\) | \(0,0\) | nonedge |
| \((1,7)\) | \(8\) | \(0,0\) | edge |

Every loop is \(m=m=2^k\); there are no other diagonal entries.

## Odd-cycle witnesses

For labels \((2,4,4)\),

$$
n_1=(2-4+4)/2=1,\quad n_2=1,\quad n_3=3.
$$

The resulting odd-block closed walk is \(1,1,3,1\).

For labels \((4,8,8)\), the unique positive cycle is \((2,2,6)\), lying in
the valuation-one block.

## Even-cycle witnesses

For labels \((4,8,8,4)\), the alternating sum is zero. With \(n_1=t\),

$$
(n_1,n_2,n_3,n_4)=(t,4-t,4+t,4-t),
$$

and positivity gives exactly \(t\in\{1,2,3\}\). The odd-block solutions are
the cases \(t=1,3\).

For labels \((4,4,8,4)\), the alternating sum is \(4\), so no cyclic
solution exists.

## Endpoint witnesses

For \(N=2^a\),

$$
L_a(\sigma)=\sum_{m=1}^{N-1}[m(N-m)]^{-\sigma}.
$$

- At \(\sigma=1/2\), the central half of the sum is bounded below by a
  positive constant independent of \(a\); hence \(\sum_aL_a(1/2)\) diverges.
- At \(\sigma=1\),
  \(L_a(1)=2H_{N-1}/N\), so the Hilbert–Schmidt level sum converges.
- For the trace norm lower bound, \(Q_j=4^j\) and
  \(I_j=[Q_j/4,Q_j/3]\cap\mathbb Z\) give matching mass comparable to
  \(Q_j^{1-\sigma}\), including a nondecaying mass at \(\sigma=1\).

## Trace witnesses

The diagonal ledger is

$$
\operatorname{Tr}(H_s)=\sum_{k\ge0}2^{-ks}
$$

only in the trace-class domain \(\Re s>1\). The same formal diagonal series
outside that domain is not authorization to call \(H_s\) trace class.

For every \(r\ge2\) in the Hilbert–Schmidt domain, the valuation-\(k\) block
contributes \(2^{-krs}\operatorname{Tr}(A_s^r)\). This is an exact direct
sum identity, not a fitted geometric ratio.

## Ledger status

EXACT_PREAUTHORITY_WITNESSES / RESULTS_NOT_RUN

