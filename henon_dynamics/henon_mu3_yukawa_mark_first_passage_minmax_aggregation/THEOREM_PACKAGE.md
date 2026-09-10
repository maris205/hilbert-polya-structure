# C103 theorem package

Let $T_i,T_j$ be the C88 first-passage times and write
$S_{ij}(k,\ell)=\#\{T_i>k,T_j>\ell\}$. Two-dimensional finite differences
recover the joint PMF $N_{ij}(a,b)$. Therefore

\[
 \Pr(\min(T_i,T_j)>k)=S_{ij}(k,k),
\]

and inclusion--exclusion gives

\[
 \Pr(\max(T_i,T_j)\le k)=1-\Pr(T_i>k)-\Pr(T_j>k)+S_{ij}(k,k).
\]

The pointwise identity $\min(T_i,T_j)+\max(T_i,T_j)=T_i+T_j$ yields the exact
expectation check for all 400 ordered pairs. On the diagonal both aggregates
equal the original target time. All statements are finite probability
identities; no arithmetic or operator claim is made.
