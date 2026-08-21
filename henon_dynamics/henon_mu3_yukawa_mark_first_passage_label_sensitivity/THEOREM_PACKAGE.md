# C92 theorem package

Let (p_H(i,k)) be the number of uniform permutations whose first hit of
the target (H) occurs at time (k) and whose (k)-th label is (S_i).
Then

\[
p_H(i,k)=\#\{A:|A|=k,S_i\in A,H\le\Phi(A),
H\not\le\Phi(A\setminus\{S_i\})\}(k-1)!(16-k)!.
\]

Summing in (i,k) gives the C88 first-passage mass for every nontrivial
target.  Hence the pivotal probabilities sum to one, and the rank-weighted
and rank-square-weighted pivotal sums equal (mathbb E[T_H]) and
(mathbb E[T_H^2]).  The trivial target has zero sensitivity everywhere.

The evidence records all 320 label-target rows and all rank cells exactly.
