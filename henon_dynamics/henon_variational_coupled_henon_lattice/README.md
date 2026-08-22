# C106 — Exact two-site variational Hénon lattice

本包是 Route A 候选动力学扩展的第三个试验包。它研究一个**两站点、变分、可逆、辛**的耦合 Hénon 类映射，并把低周期计算和 operator 结论严格分开。

## 研究对象

令 (q=(x,y))、(p=(u,v))，取

\[
 U(x,y)=\frac a2(x^2+y^2)-\frac{x^3+y^3}{3}-\frac{\kappa}{2}(x-y)^2,
 \qquad (a,\kappa)=\left(7,\frac14\right).
\]

映射为

\[
 F(q,p)=(\nabla U(q)-p,q).
\]

取 canonical one-form \(\lambda=q\cdot dp\)，则精确恒等式为
\(F^*\lambda-\lambda=d(U(q)-p\cdot q)\)；这也是本包使用“变分/精确辛”术语的具体含义。

在坐标 ((q_1,q_2,p_1,p_2)) 上使用

\[
 \Omega=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix},
 \qquad R(q,p)=(p,q).
\]

代码以有理数 (\mathbb Q) 运算完成，不使用随机数。producer 对两个同步不动点

\[
 (0,0;0,0),\qquad (5,5;5,5)
\]

以及一个同步二周期

\[
 (3,3;6,6)\longleftrightarrow(6,6;3,3)
\]

进行精确核验。

## 主要精确结果

二周期的耦合 monodromy (M_\kappa=DF(z_1)DF(z_0)) 满足

\[
\det M_\kappa=1,\qquad \operatorname{tr}M_\kappa=-\frac{47}{4},
\]

且

\[
 \det(I-zM_\kappa)=1+\frac{47}{4}z+\frac{141}{4}z^2+
 \frac{47}{4}z^3+z^4.
\]

把耦合关掉（同样 (a=7)、同一同步二周期、\(\kappa=0\)）得到

\[
 \det(I-zM_0)=1+14z+51z^2+14z^3+z^4.
\]

这里的 $M_0$ 在交换为按站点排列的坐标后正是两个相同的一站点二周期块 $B_6B_3$ 的直和；因此对照是真正的 product/direct-sum control，而不是另选一条周期。

所以这一个低周期 witness 给出

\[
 \operatorname{tr}M_\kappa-\operatorname{tr}M_0=\frac94,
 \qquad [z^2]\det(I-zM_\kappa)-[z^2]\det(I-zM_0)=-\frac{63}{4}.
\]

这只是有限维 monodromy 多项式的耦合/非耦合对照，**不能称为 Fredholm determinant**。

## A1/A2 边界

* A1：`A1_WEAK`（qualification: `PARTIAL_CERTIFIED_LOW_PERIOD_ONLY`）。不动点和一个二周期经过独立有理数复算；周期的闭合、非退化的有限维 monodromy、重复周期的基本检查均通过。但没有证明完整 primitive-orbit atlas、没有建立全局 Markov 分割，也没有漏轨道上界。
* A2：`A2_FAIL`（qualification: `OPERATOR_OWNER_OPEN`）。包中只计算有限周期的 (det(I-zM))，尚未定义共同 Banach/Hilbert 空间上的转移算子，更没有核型性、迹公式、Fredholm determinant、零点 root-count 或 cutoff/precision 稳定性。
* A3：`A3_NOT_ADDRESSED`；A4：`A4_FAIL`；总体 `ROUTE_A_EXPLORATORY`。

## 可复现实验

```bash
python code/c106_variational_lattice.py
python code/c106_variational_lattice_checker.py
python code/c106_sympy_crosscheck.py
python code/c106_replay_checker.py
python code/c106_mutation_test.py
```

证据文件为 `results/c106_variational_lattice_evidence.json`。`paper/main.pdf` 是同一结果的论文输出；文件账本见 `C106_PREFREEZE_MANIFEST.json`。完整 hostile mutation 审计为 11/11 拒绝。

## 明确非声明

本包不声明完整 primitive-orbit 分类、动力学 zeta 的解析延拓、Fredholm determinant、算术局部因子、Euler factors、root numbers、automorphy、Hilbert–Pólya 算子或黎曼零点对应关系。`NO_BAD_EULER_OR_ROOT_NUMBER` 是证据和论文的 scope firewall。
