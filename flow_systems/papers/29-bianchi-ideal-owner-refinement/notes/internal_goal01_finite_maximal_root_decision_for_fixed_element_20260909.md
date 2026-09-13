# P29 内部论证：固定群元素的有限最大根判定

记录日期：2026-09-09 UTC。Goal 01 的有界纸面推进；只新增本笔记。
本篇给定一个实际 level-(3) Gaussian loxodromic 元素，证明其全部
正整数幂根可以在一个明确有限的候选集合内作精确判定，并从中得到
本原的最大指数根。这里描述并证明有限步骤，没有运行递推、枚举、
符号程序、census、实验或 producer。

本篇补的是原稿 [Gate Q][gate] 所列的逐元素 maximal-root 数学接口。
它不是完整子群共轭判定、无向 owner 商、规范 serializer 或执行证书；
不改任何 Gate、Route、Stage、旧稿、锁或失败状态。ARS 的 bounded
argument-builder 用于分开有限性证明、实际检验条件和未执行的关卡。

## 1. 输入、PSL 提升与根的精确定义

固定

\[
\Gamma(3)=\{B\in SL_2(\mathbb Z[i]):B\equiv I\pmod3\},
\qquad \bar\Gamma(3)\subset PSL_2(\mathbb C).
\tag{1}
\]

输入是一个具有精确 Gaussian 整数条目的矩阵 \(A\in\Gamma(3)\)，
其投影 [A] 为 loxodromic。所有群根均要求属于这个完整群，而非
某个词球、实子群或另选的候选子群。定义

\[
\mathcal R(A)=\{(m,B):m\in\mathbb Z_{\ge1},\ B\in\Gamma(3),\ B^m=A\}.
\tag{2}
\]

\(m=1,B=A\) 总是允许。所谓真幂是存在 \(m\ge2\) 的分解；若写成
负指数，换用根的逆便回到此定义，所以正指数约定不漏掉真幂。

首先固定 PSL 的中央符号。因为 \(-I\not\equiv I\pmod3\)，投影
\(\Gamma(3)\to\bar\Gamma(3)\) 的核平凡。每个 \(\bar\Gamma(3)\)
元素在两个 SL 提升中恰有一个满足 \(I\pmod3\)：存在性来自 (1)
的像定义，唯一性来自两者之差的中央符号。因此这里的“规范提升”
只指这个唯一的 \(I\pmod3\) 提升，不是共轭类或 owner 的规范代表。

若 \([B]^m=[A]\)，对上述唯一提升有 \(B^m=\pm A\)。约化模 3 后，
左侧为 I，而 \(-A\equiv-I\ne I\)；负号被排除，故

\[
[B]^m=[A]\quad\Longleftrightarrow\quad B^m=A.
\tag{3}
\]

所以 (2) 精确对应完整 PSL 群中的根问题。若 [A] 仅被写成共轭于
某个真幂，先把根用同一个群元素共轭回来，再应用 (3)，同样归入 (2)。

## 2. 迹同余、无挠性与 loxodromic 根

对任意 \(B=I+3D\in\Gamma(3)\)，二维行列式展开给

\[
1=\det(I+3D)=1+3\operatorname{tr}D+9\det D,
\qquad
\operatorname{tr}B=2-9\det D\in2+9\mathbb Z[i].
\tag{4}
\]

这个同余也见[自然振幅笔记，§2][amplitude]；本篇重新展开以便
后面的有限界自含。若 \(\operatorname{tr}B\ne2\)，则

\[
|\operatorname{tr}B|\ge7.
\tag{5}
\]

若 B 在 SL 中有限阶，它在特征零下可对角化，特征值为
\(\lambda,\lambda^{-1}\)，且 \(|\lambda|=1\)。于是
\(\operatorname{tr}B=2\operatorname{Re}\lambda\in[-2,2]\)。由 (4)
只能是 2，两个特征值均为 1，故 B=I。这证明 \(\Gamma(3)\) 无挠；
结合投影单射，\(\bar\Gamma(3)\) 亦无挠。此事实仅在 §6 的同指数
根唯一性中使用，不以未经证明的中心化子结构定理代替它。

现在设 \((m,B)\in\mathcal R(A)\)。B 与 A 交换，因为 A=B^m。
loxodromic A 具有不同的特征值 \(\lambda_A,\lambda_A^{-1}\)，
其中 \(|\lambda_A|>1\)。在 A 的特征基中，任何与 A 交换的矩阵
都是对角矩阵。因此 B 保持 A 的两条特征直线，即 PSL 作用的两个
不动点，并可在同一基中写为

\[
A=\begin{pmatrix}\lambda_A&0\\0&\lambda_A^{-1}\end{pmatrix},
\qquad
B=\begin{pmatrix}\lambda_B&0\\0&\lambda_B^{-1}\end{pmatrix},
\qquad \lambda_B^m=\lambda_A.
\tag{6}
\]

于是 B 也为 loxodromic。记

\[
\rho_A=|\lambda_A|>1,\qquad \rho_B=|\lambda_B|>1,
\qquad \rho_A=\rho_B^m.
\tag{7}
\]

这里没有选择复数根的数值分支；(6) 只是对任何真实群根必然满足的
特征直线与模长关系作证明。若 \(\operatorname{tr}B=2\)，其两个
特征值均为 1，与 (7) 矛盾，故 (5) 适用于每个真实根。

## 3. 完整有限范围：指数与 Gaussian 迹

写

\[
\tau_A:=\operatorname{tr}A=a+bi,\qquad
a,b\in\mathbb Z,\qquad N:=|a|+|b|.
\tag{8}
\]

由 (5)–(7)，

\[
7\le|\operatorname{tr}B|
\le\rho_B+\rho_B^{-1}<\rho_B+1,
\qquad \rho_B>6.
\tag{9}
\]

另一方面，\(\lambda_A=\tau_A-\lambda_A^{-1}\)，所以

\[
\rho_A\le|\tau_A|+\rho_A^{-1}
<|\tau_A|+1\le N+1.
\tag{10}
\]

对全部真实根，(7)、(9)、(10) 给出严格整数界

\[
\boxed{6^m<N+1.}
\tag{11}
\]

此外，\(m\ge1\) 使 \(\rho_B\le\rho_A\)，故

\[
|\operatorname{tr}B|
\le\rho_B+\rho_B^{-1}<\rho_B+1
\le\rho_A+1<N+2.
\tag{12}
\]

因此取有限集合

\[
\mathcal M_A:=\{m\in\mathbb Z_{\ge2}:6^m<N+1\},
\]
\[
\mathcal T_A:=\{t\in2+9\mathbb Z[i]:
|\operatorname{Re}t|\le N+2,\quad|\operatorname{Im}t|\le N+2\}.
\tag{13}
\]

闭整数盒可能含有不能成为根迹的多余点，这不影响完备性。
\(\mathcal M_A\) 有限，因为 \(6^m\) 严格趋于无穷；判断其边界
只需整数比较，不用近似对数或浮点长度。\(\mathcal T_A\) 是有限
整数盒与一个 Gaussian 同余类的交。每个真幂根的
\((m,\operatorname{tr}B)\) 必在 (13) 中；等号 \(6^m=N+1\) 不会
对应真根，可安全排除。若 \(\mathcal M_A\) 为空，已经排除所有真幂。

## 4. 固定指数与迹后的唯一代数候选

对符号变量 t 定义整系数多项式

\[
F_0(t)=0,\qquad F_1(t)=1,\qquad
F_{j+1}(t)=tF_j(t)-F_{j-1}(t)\quad(j\ge1).
\tag{14}
\]

对任何 \(B\in SL_2(\mathbb C)\)、\(\operatorname{tr}B=t\)，
Cayley–Hamilton 恒等式为 \(B^2=tB-I\)。由归纳法，

\[
B^m=F_m(t)B-F_{m-1}(t)I\qquad(m\ge1).
\tag{15}
\]

具体地，m=1 由 (14) 成立；将 m 的表达乘 B，再代入
\(B^2=tB-I\)，B 的系数成为 \(tF_m-F_{m-1}=F_{m+1}\)，
I 的系数成为 \(-F_m\)，正是 m+1 的表达。

若真实根满足 \(B^m=A\)，但 \(F_m(t)=0\)，(15) 会迫使
\(A=-F_{m-1}(t)I\) 为标量，与 loxodromic 输入矛盾。因此真实根
必满足 \(F_m(t)\ne0\)，并且

\[
\boxed{B_{m,t}:=\frac{A+F_{m-1}(t)I}{F_m(t)}.}
\tag{16}
\]

对给定 \((m,t)\)，这至多是一个矩阵候选，而不是一个复根分支族。
因为 \(t\in\mathbb Z[i]\)，分子、分母的条目均为 Gaussian 整数，
故 \(B_{m,t}\in M_2(\mathbb Q(i))\)。后续检验可全部用精确
Gaussian 有理运算与整数整除表述，不需代数数根求值。

## 5. 有限判定步骤及完备性

下面是纸面规定的有限过程；本篇没有实际执行任何一步候选枚举。
先保留基准根 \((1,A)\)。对 (13) 中每个 \((m,t)\)，取 (14)
的有限递推值；若 \(F_m(t)=0\) 就跳过，否则构造 (16)，并实际
检查下列全部等式或包含关系：

1. \(B_{m,t}\in M_2(\mathbb Z[i])\)；
2. \(\operatorname{tr}B_{m,t}=t\)；
3. \(\det B_{m,t}=1\)；
4. \(B_{m,t}\equiv I\pmod3\)；
5. \(B_{m,t}^{\,m}=A\)，作为字面的矩阵等式。

条件 2 必须保留。构造时把 t 放入递推，并不保证重建矩阵的迹
真的等于 t；不允许在此循环论证。条件 5 同样是实际检查，不把
一个未经验证的候选公式当成幂等式。Gaussian 整性可逐条目检测
分母整除分子；其余也是有限个精确等式或同余式。无需规定具体
软件、serializer、运行资源或证书格式，便可证明这些有限操作
在数学意义上可判定。

**可靠性。** 通过全部检查的候选属于 \(\Gamma(3)\)，且其 m 次幂
就是 A，因此它确属 (2)，不是群外的矩阵根或仅近似成立的根。

**完备性。** 对任意 \((m,B)\in\mathcal R(A)\)，若 m=1 已在基准
项中；若 m≥2，§3 证明其 \((m,t)\) 在 (13) 内，§4 证明分母非零
且 (16) 恰等于 B。所以该真实根不会被遗漏，并必通过全部检查。
有限过程得到的恰是 \(\mathcal R(A)\)，没有预设一个未证完备的
词长截断、矩阵高度截断或最大幂次。

## 6. 同一指数的唯一性与最大根的本原性

先证明不同迹候选不能给同一指数的两个真实根。若
\(B^m=C^m=A\)，则 B、C 均与 A 交换。由 A 的两个特征值不同，
二者在同一个 A 特征基中均为对角矩阵，因此 BC=CB。于是

\[
(BC^{-1})^m=B^mC^{-m}=I.
\tag{17}
\]

\(BC^{-1}\in\Gamma(3)\)，§2 的无挠性给 \(BC^{-1}=I\)，即 B=C。
此处需要无挠性；仅有矩阵可对角化或交换性还不足以排除单位根倍数。
该证明没有预先调用“完整 loxodromic 中心化子为无限循环群”的定理。

由 §5 的有限性与基准项，存在最大成功指数

\[
m_*:=\max\{m:(m,B)\in\mathcal R(A)\},
\qquad B_*^{m_*}=A,
\tag{18}
\]

且对这个 m_*，根 B_* 由 (17) 唯一。若
\(B_*=D^k\)、\(D\in\Gamma(3)\)、\(k\ge2\)，则

\[
A=D^{km_*}.
\tag{19}
\]

这是真实根，必由有限过程的完备性收录，却有 \(km_*>m_*\)，
与最大性矛盾。所以 B_* 在完整 \(\Gamma(3)\) 中不是真幂。
结合 (3)，[B_*] 在完整 \(\bar\Gamma(3)\) 中也为本原。
若 [B_*] 只被表示成共轭于真幂，把根共轭回来仍得到同一矛盾。
因此这不是“候选盒内未找到更深根”，而是完整群中的本原性结论。

特别地，\(m_*=1\) 当且仅当 [A] 本原；否则 (18) 给一个真实的
本原最大根及其重复指数。本篇不另声称所有不同指数的根之间具有
某个已排序的中心化子参数化，也不需要这种额外结论完成判定。

## 7. 已关闭的数学接口与仍缺的商集义务

已证明的内容限于：给定一个精确、实际群内的 loxodromic 输入，
其群根问题有上述有限完备判定；最大指数根存在、唯一且本原。
其输入范围不依赖旧笔记中三交换子或另一个无限族的特选形式。

[实际有限包笔记，§8][packets] 明确未提供 primitive-root 程序；
本篇给出的是这一逐元素问题的数学判定构造，不改写旧笔记的历史
边界，也不声称现在已存在经过执行和独立重播的软件实现。

以下仍未完成：两个不同输入在 level-(3) 子群中的共轭判定及其
完整否定证书；取逆关系与传递闭包；全部输入行、排除和重复的覆盖；
canonical unoriented owner ID；规范序列化、冻结 fixtures 和独立
实现的 replay。原稿 [B0061–B0068][gate] 要求这些共同组成 Gate Q，
一个最大根定理不等于该关卡已经完成。它也不提供 Gate M 的具体
字面素理想机制、机制登记、owner law、性能值或新的算术周期结论。

## 8. 来源分工、实际动作与保全

本篇读取[自然振幅][amplitude]中的实际迹同余与长度背景、
[有限返回包][packets]的未解 root 边界和[原稿 Gate Q 接口][gate]。
§1–6 的提升、特征值模界、Cayley–Hamilton 递推、检验完备性及
最大根证明均在本文展开，不把这些本案推导归为外部来源的原结论。
不依赖新的 Selberg、Ruelle、scattering 或任意角色延拓定理。

这是 AI 辅助内部纸面论证，不是正式证明认证。同模型的有界逻辑
校对不构成独立科学证据。实际只以 apply_patch 新增本文件，随后
作一次完整只读静态回读；未运行递推、枚举、科学／符号程序、实验、
producer、census、稿件 build 或正式 gate validator。旧文件、锁、
回执、失败证据、Route 与 Stage 状态均不由本篇改变。

[amplitude]: internal_goal01_geometric_return_amplitude_and_laplace_bound_20260909.md
[packets]: internal_goal01_actual_finite_period_packets_20260909.md
[gate]: stage4_prime_revision_round6.tex
