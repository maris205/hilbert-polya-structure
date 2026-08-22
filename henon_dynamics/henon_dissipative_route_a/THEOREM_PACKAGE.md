# Theorem package

Let
\[
F(x,y)=(x^2-91/16-y,x/2).
\]

1. The fixed-point polynomial is
   \[
   x^2-\frac32x-\frac{91}{16}
   =\frac{(4x-13)(4x+7)}{16}.
   \]
   Thus the fixed points are \((13/4,13/8)\) and
   \((-7/4,-7/8)\).

2. Eliminating (y) from (F^2(x,y)=(x,y)) gives
   \[
   \operatorname{Res}_y=\frac{(4x-13)(4x-5)(4x+7)(4x+11)}{256}.
   \]
   Removing the fixed factors leaves \((4x-5)(4x+11)), and the associated
   primitive two-cycle is
   \((5/4,-11/8)\leftrightarrow(-11/4,5/8)).

3. At the four witnesses, the local weights
   \(\omega(p)=1/\det(I-DF(p))\) are
   \(-1/5,1/5,-1,1/7\), in the state order
   \(p_+,p_-,q_+,q_-\).

4. The weighted transition matrix (source weight on each outgoing edge) is
   \[
   M=\begin{pmatrix}
   -1/5&0&0&0\\0&1/5&0&0\\0&0&0&-1\\0&0&1/7&0
   \end{pmatrix},
   \]
   and therefore
   \[
   \det(I-zM)=1+\frac{18}{175}z^2-\frac1{175}z^4.
   \]

The statements are finite exact identities.  They do not identify this
polynomial with a global dynamical Fredholm determinant.
