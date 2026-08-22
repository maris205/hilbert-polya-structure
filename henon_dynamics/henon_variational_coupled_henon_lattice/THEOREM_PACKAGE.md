# Theorem package (C106)

## Proposition 1 (variational symplecticity)

令 \(F(q,p)=(\nabla U(q)-p,q)\)，其中 \(U\) 为二阶可微函数。则
\[
 DF=\begin{pmatrix}D^2U&-I\\I&0\end{pmatrix},
 \qquad DF^T\Omega DF=\Omega,
 \qquad \det DF=1.
\]

**证明。** 直接块矩阵相乘；只使用 \(D^2U=(D^2U)^T\)。行列式可由交换块行或 Schur 补得到 \(1\)。C106 对具体有理 Hessian 在所有列出的点逐项计算。

## Proposition 1b (exact primitive)

用 \(\lambda=q\cdot dp\) 表示与本包 \(\Omega\) 一致的 canonical one-form，则
\[
 F^*\lambda-\lambda=d\bigl(U(q)-p\cdot q\bigr).
\]
这给出 exact symplectic primitive；producer 在三个独立有理样本、SymPy 在符号层面均复核该恒等式。

## Proposition 2 (reversor)

\(R(q,p)=(p,q)\) 满足
\[
 R\circ F\circ R=F^{-1},
 \qquad F^{-1}(q,p)=(p,\nabla U(p)-q).
\]

**证明。** 代入定义即可。producer 和 checker 还在三个非轨道有理样本上执行了逐坐标等式。

## Proposition 3 (coupled period-two witness)

当 \(a=7,\kappa=1/4\) 时，\((3,3;6,6)\leftrightarrow(6,6;3,3)\) 是一个非固定二周期。其 monodromy 满足
\[
\det M=1,\quad \operatorname{tr}M=-47/4,
\quad \det(I-zM)=1+(47/4)z+(141/4)z^2+(47/4)z^3+z^4.
\]

**证明。** 代入梯度方程可得 \(\nabla U(3,3)=(12,12)=2(6,6)\)，\(\nabla U(6,6)=(6,6)=2(3,3)\)。再将两个有理 Jacobian 相乘并按定义展开行列式。

## Scope note

这些命题是有限维代数命题。它们不提供完整 primitive-orbit completeness、Markov partition、transfer-operator nuclearity、trace formula 或 Fredholm determinant。
