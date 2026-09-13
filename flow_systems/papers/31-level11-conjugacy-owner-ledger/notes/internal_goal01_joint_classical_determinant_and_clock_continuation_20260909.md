# P31 Goal01：联合经典 transfer determinant 与实际时钟 Euler 函数的全平面延拓

日期：2026-09-09 UTC。本页是持续目标内的新内部纸面证明，承接已读审的
[cusp 与双参数右域][cusp]和[共同核算子族][nuclear]。只新增本文件，
不修改历史、锁定输入、稿件、Route、Gate 或 Stage。

**结论。** 在本案已固定的 cuspform 时钟、正密度区间及酉局部系下，
实际时钟的 Euler 函数有全平面亚纯延拓：
\[
D_\varepsilon(s)=
\frac{\Delta(s,s)}{\Delta(s+1,s)},\qquad
\zeta_\varepsilon(s)=
\frac{\Delta(s+1,s)}{\Delta(s,s)},
\tag{1}
\]
右侧来自一个固定 Banach 模型上的联合经典核 transfer determinant
\(\Delta(z,w)=\det(I-\mathcal L(z,w))\)。两式先在明确右半平面等于
原闭轨道乘积，再由本页证明的合法曲线限制延拓。

这里是**经典、通常非自伴且依赖参数的 transfer operator**。
本页没有构造固定自伴量子算子，也没有证明量子／谱行列式的
全局等式、Hilbert–Pólya 实现或任何 Route 晋升。已有时钟不下降
反例仍成立；本结果通过诱导纤维保存时钟，而不是恢复已失败的标量下降。

## 1. 固定对象与已经证明的输入

保持
\[
G=\mathrm{PSL}_2(\mathbb Z),\quad
\Gamma=\Gamma_0(11)/\{\pm I\},\quad [G:\Gamma]=12,
\]
\[
\alpha=\operatorname{Re}(2\pi i f(z)\,dz),\quad
f(z)=\eta(z)^2\eta(11z)^2,\quad
\rho_\varepsilon=1+\varepsilon\alpha(X_{\rm geo})\ge c_0>0,
\quad 0<c_0\le1.
\tag{2}
\]
\(\varepsilon\) 是固定实数，\(c_0\) 是该固定正时钟的下界；两者不随
复参数 \(z,w,s\) 拟合。令 \(\nu:\Gamma\to U(m)\) 为固定酉表示，
\[
I(P)=\int_P\alpha,\qquad
T_\varepsilon(P)=\ell(P)+\varepsilon I(P)\ge c_0\ell(P),
\]
\[
\chi_w(P)=\nu(P)e^{-w\varepsilon I(P)},\qquad
\eta_w=\operatorname{Ind}_\Gamma^G\chi_w,\qquad d:=\dim\eta_w=12m.
\tag{3}
\]
按各群真实共轭类计有向 primitive hyperbolic 轨道，不额外作取逆商。
本文没有重新选方向、cover index 或 transverse 整数索引。

[cusp][cusp] 已证明 \(I(p)=0\) 对所有 \(\Gamma\)-parabolic 成立，
并在 ambient 的两条实际 parabolic branches 上给出
\[
\eta_w(p_i)=D_i(w)J_iD_i(w)^{-1},\qquad
J_i=\eta_0(p_i),\quad i=1,2,
\tag{4}
\]
其中 \(D_i^{\pm1}\) 整，\(J_i\) 固定酉。两条 \(D_i\) 不必相同。

[nuclear][nuclear] 已在一个共同、固定的几何 chart 中选定
\[
B=B_a\oplus B_b,\qquad
B_c=\mathcal B(\mathcal E_c;\mathbb C^d),
\tag{5}
\]
并证明
\[
\mathcal L(z,w)=
\begin{pmatrix}0&T_1(z,w)\\T_2(z,w)&0\end{pmatrix}
\tag{6}
\]
在每个 \(\mathcal N_q(B)\)、\(0<q\le1\)，均有明确的局部联合
核理想幂级数。初始域 \(\Re z>1/2\) 的两条分支恰为
\[
T_i(z,w)f(x)=\sum_{n\ge1}((p_i^{-n})'(x))^z
                  \eta_w(p_i)^n f(p_i^{-n}x).
\tag{7}
\]
这不是某个存在但未识别的 Fredholm 实现；(7) 就是
Fedosova–Pohl Example 4.1 式 (30) 的同一 strict 模型及同一表示。

若用共同 \(h\in\mathrm{PSL}_2(\mathbb R)\) 将几何域移到有限 affine
chart，则群、全部分支及表示一并共轭，表示定义为
\(\widetilde\eta_w(hgh^{-1})=\eta_w(g)\)。\(h\) 不依赖参数。
共轭保平移长度、primitive 共轭类及 coefficient trace，因而不改变
这里的 Selberg product。不能只改变量而漏掉导数权重。

唯一可能的核算子极点是固定离散集
\[
\mathscr P=\{z_k=(1-k)/2:k\in\mathbb N_0\}.
\tag{8}
\]
在 \(z=z_k\) 附近，
\[
\mathcal L(z,w)=(z-z_k)^{-1}A_k(w)+B_k(z,w),
\tag{9}
\]
\(B_k\) 联合核理想全纯，\(A_k\) 有限秩且在 \(w\) 上全纯。
这些是上游具体 Taylor–Lerch 展开与矩阵 gauge 的结论，
不是从逐个固定 \(w\) 的文献延拓猜出的联合性。

## 2. 所用 determinant 基础及其证据层次

固定一个 \(0<q\le2/3\)，例如 \(q=1/2\)。

本页使用 canonical \(\mathcal N_q(B)\) Fredholm determinant。
[Bandtlow–Jenkinson，§4 开头、Definition 4.1 前][bj] 明列：
此类核算子有唯一连续 trace 与 determinant，并给式 (8) 的
局部 trace-log 关系及其谱性。这是本页从 tensor kernel 到
operator determinant 的独立基础接口；不是一般 \(\mathcal N_1\)
空间上未经检验的断言。

[Grothendieck，Chapitre II §2 Proposition 1，pp.346–348][groth]
给 projective tensor kernel 的 determinant 为整函数，
并在式 (4) 给乘法恒等式。其随后 p.349 的 Remark 明确提醒：
一般 tensor kernel 与其 operator image 不能不加条件地混同。
本页以上述 \(q\le2/3\) 的 canonical 接口保持这个区别，
不另假设整个 \(B\) 具有 approximation property。

还需要联合全纯，而不能只用 determinant 的连续性。上游实际提供
比点态核性更强的局部展开：
\[
\mathcal L(z,w)=\sum_j v_j(z,w)\otimes\ell_j,\qquad
\sup_{(z,w)\in K}\|v_j(z,w)\|\|\ell_j\|\le C_K\vartheta^j,
\quad \vartheta<1,
\tag{10}
\]
这里可有有限组这样的序列及有限秩项，\(\ell_j\) 固定，
\(v_j\) 是输出 Banach 空间中的全纯函数；极点处先减去主部。
这里 \(v_j\otimes\ell_j\) 是 output-first 的秩一算子记号；
对应的 projective tensor 是 \(\ell_j\otimes v_j\)，使用自然 flip。
因此 (10) 在
\(B^*\widehat\otimes_\pi B\) 中局部正常收敛，直接给全纯的核提升。
与 Grothendieck 的整 determinant 复合，得到联合标量全纯函数。
不同局部提升在其共同域内给同一 canonical operator determinant，
故这些局部函数相容。

以下因此可用三项标准核 determinant 运算：联合全纯、
乘法性、identity 加有限秩算子的 determinant 等于其有限维 determinant。
每一项的具体用处会在下一节明写；不会把算子范数全纯直接当成
核 determinant 全纯，也不会在准 Banach 理想中偷用 Banach Cauchy 定理。

## 3. 移动的 residue range 仍有固定有限维分解

令
\[
r_i=\dim\ker(J_i-I),\qquad R=r_1+r_2\le2d=24m.
\tag{11}
\]
这不是声称实际 pole 阶为 \(R\)，只是统一的允许上界。

固定 \(z_k\)。上游单分支 residue 具有
\[
(R_{i,k}(w)f)(x)=
\phi_{i,k}(x)D_i(w)P_{i,1}D_i(w)^{-1}
                    \frac{f^{(k)}(x_i)}{k!},
\tag{12}
\]
其中 \(x_i\) 是该分支输入域中的 cusp，\(P_{i,1}\) 是 \(J_i\) 的
eigenvalue-1 投影，且
\[
\phi_{i,k}(x)=\tfrac12 c_i(x)^{z_k}\gamma_i^{-k}.
\tag{13}
\]
\(c_i,\gamma_i\) 是[nuclear][nuclear] §3.1 的固定 parabolic 正规形数据。
因 \(2z+k-1=2(z-z_k)\)，(13) 中的 \(1/2\) 不能遗漏。

选固定有限维分解
\[
P_{i,1}=E_iF_i,\quad
E_i:\mathbb C^{r_i}\to\mathbb C^d,\quad
F_i:\mathbb C^d\to\mathbb C^{r_i}.
\tag{14}
\]
\(r_i=0\) 时使用零维空间。定义
\[
\bigl(U_{i,k}(w)\xi\bigr)(x)=\phi_{i,k}(x)D_i(w)E_i\xi,
\]
\[
V_{i,k}(w)f=F_iD_i(w)^{-1}\frac{f^{(k)}(x_i)}{k!}.
\tag{15}
\]
输入点严格位于其域内，Cauchy 估计使导数求值为有界泛函。
因此 \(U_{i,k},V_{i,k}\) 是有界算子的全纯族，且
\(R_{i,k}=U_{i,k}V_{i,k}\)。

以 \(\iota_c,\pi_c\) 表示 (5) 的固定 injection 与 projection，
拼合为
\[
U_k(w)=\big[\iota_aU_{1,k}(w)\quad\iota_bU_{2,k}(w)\big]:
                    \mathbb C^R\to B,
\]
\[
V_k(w)=
\begin{bmatrix}V_{1,k}(w)\pi_b\\ V_{2,k}(w)\pi_a\end{bmatrix}:
                    B\to\mathbb C^R.
\tag{16}
\]
由 block 方向直接核对，
\[
A_k(w)=U_k(w)V_k(w).
\tag{17}
\]
这是**固定中间维数**，不要求所有 \(\operatorname{ran}A_k(w)\)
落在同一个固定 \(R\)-维子空间。一般 analytic rank-one 族的
range span 甚至可以随参数扫出无限维空间；不能以点态 rank
替代 (16) 的显式分解。此处 \(R\) 已等于两个 residue 分解维数之和，
不需要另用一个更大中间维数后猜测其极点阶。

## 4. 增广行列式：不要求 \(I-B_k\) 可逆

在 \((\mathbb C\setminus\mathscr P)\times\mathbb C\) 先定义
\[
\Delta(z,w)=\det_B(I-\mathcal L(z,w)).
\tag{18}
\]
§2 保证这是联合全纯函数。

固定 \(z_k\)，记 \(t=z-z_k\)、\(B_k(z,w)=B_0(t,w)\)，并省略
\(U_k,V_k\) 的下标。在固定空间 \(B\oplus\mathbb C^R\) 上令
\[
\mathcal H(t,w)=
\begin{pmatrix}I-B_0(t,w)&-U(w)\\-V(w)&tI_R\end{pmatrix}.
\tag{19}
\]
\(\mathcal H-I\) 是联合 \(\mathcal N_q\)-全纯族：除了 \(B_0\)，
其余各块均通过固定有限维空间分解。因此
\(F_k(t,w):=\det_{B\oplus\mathbb C^R}\mathcal H(t,w)\) 联合全纯。

对 \(t\ne0\)，直接块乘法给
\[
\mathcal H=
\begin{pmatrix}I&-U/t\\0&I_R\end{pmatrix}
\begin{pmatrix}I-B_0-t^{-1}UV&0\\0&tI_R\end{pmatrix}
\begin{pmatrix}I&0\\-V/t&I_R\end{pmatrix}.
\tag{20}
\]
两个外侧因子都是 identity 加有限秩幂零算子，其 determinant 为 1。
中间块的 determinant 等于两个对角块的乘积，由此
\[
\boxed{F_k(t,w)=t^R\Delta(z_k+t,w)\quad(t\ne0).}
\tag{21}
\]
整个分解没有用到 \(I-B_0\) 或 \(I-\mathcal L\) 的逆，
在这些算子奇异的参数点仍然有效。

于是
\[
\boxed{\Delta(z,w)=\frac{F_k(z-z_k,w)}{(z-z_k)^R}}
\tag{22}
\]
给出 \(z=z_k\) 附近的联合亚纯延拓，极点阶至多 \(R\)。
若 \(R=0\)，(9) 没有 residue，\(\Delta\) 全纯。

(8) 在每个有限复区域只有有限多个点；对所有 \(k\) 应用同一证明，
并在非极点处以 (18) 匹配，即得 \(\Delta\) 在 \(\mathbb C^2\)
联合亚纯，全部可能的 polar divisors 只在 \(z=z_k\)。
这是一个实际构造的固定垂直极点集合；没有使用一般多变量
亚纯函数都能限制到任意曲线的错误原则。

## 5. 同一固定表示切片与联合右域的乘积识别

[cusp][cusp] 已直接证明，域
\[
\Omega_+=\{(z,w):\Re w>0,\quad
       \Re z-(1-c_0)\Re w>2\}
\tag{23}
\]
上的非零联合全纯乘积
\[
\mathcal Z(z,w)=
\prod_{[R]\in\mathcal P_G}\prod_{j\ge0}
 \det(I_d-e^{-(z+j)\ell(R)}\eta_w(R))
\tag{24}
\]
等于同一 cover 乘积
\[
\mathcal Z(z,w)=
\prod_{[P]\in\mathcal P_\Gamma}\prod_{j\ge0}
 \det(I_m-e^{-(z+j)\ell(P)-w\varepsilon I(P)}\nu(P)).
\tag{25}
\]
本页用 \(j\) 标 transverse 非负整数，以免与 pole 标号 \(k\) 混淆。
所有乘积均由已证明绝对收敛的 trace-log 定义，不另选 principal-log
或未定 scalar factor。

对每个固定 \(w\)，(4) 保证 non-expanding cusp monodromy。
(7) 又识别了来源的**同一** strict transfer model。
故 [Fedosova–Pohl Theorem 4.2(iii)][fp] 对这个固定切片给出
\[
\Delta(z,w)=Z_G(z,\eta_w)\quad(\Re z>C(w))
\tag{26}
\]
的某个充分右半平面。\(C(w)\) 可以依赖 \(w\)，本页不假设其
跨参数一致。

固定任意 \(\Re w>0\)。在连通半平面
\[
\Omega_w=\{z:\Re z>2+(1-c_0)\Re w\}
\tag{27}
\]
上，\(\mathcal Z(\cdot,w)\) 全纯，\(\Delta(\cdot,w)\) 至少亚纯；
两者在 (27) 与 (26) 的共同充分右端相等。
单变量亚纯恒等定理给它们在全部 \(\Omega_w\) 相等。
逐个 \(w\) 应用这个论证即得
\[
\boxed{\Delta(z,w)=\mathcal Z(z,w)\quad((z,w)\in\Omega_+).}
\tag{28}
\]
没有把不存在的统一 \(C\) 放进证明，也没有以仅仅“某种固定切片
存在 Fredholm 表示”替代同一算子身份。

事实上 (27) 位于 \(\Re z>2\)，不遇 (8)；因此 (28) 还直接表明
\(\Delta\) 在 \(\Omega_+\) 非零。联合亚纯延拓以这个相同解析芽为准。

## 6. 对角线与平移对角线的合法限制

考虑两条曲线
\[
\iota_0(s)=(s,s),\qquad \iota_1(s)=(s+1,s).
\tag{29}
\]
离开 (8) 的逆像，(18) 的直接代入全纯。
在某个曲线与 \(z=z_k\) 相交处，(22) 给
\[
\Delta(s+a,s)=
\frac{F_k(s+a-z_k,s)}{(s+a-z_k)^R},\qquad a=0,1.
\tag{30}
\]
分母不是恒零函数，故 (30) 是合法的一变量亚纯芽。
候选交点只在 \(\mathscr P-a\)，是局部有限集；局部芽以
非极点区的同一代入相容。因此
\[
d_0(s):=\Delta(s,s),\qquad d_1(s):=\Delta(s+1,s)
\tag{31}
\]
都是全平面亚纯函数。即使交点处分子也为零，一变量零阶比较
即可处理相消，不产生沿整条曲线不可定义的问题。

当 \(\Re s>2/c_0\)，(29) 的两点均在 (23)，其
\(\Re z-(1-c_0)\Re w\) 分别为 \(c_0\Re s\) 与 \(c_0\Re s+1\)。
由 (28)，\(d_0,d_1\) 在这里均非零，故二者都不恒为零。
于是 \(d_0/d_1\) 及 \(d_1/d_0\) 是全平面亚纯函数。

在同一右域，(25) 对 \(j\) telescoping，给
\[
\frac{d_0(s)}{d_1(s)}
=\prod_{[P]\in\mathcal P_\Gamma}
      \det(I_m-e^{-s\ell(P)-s\varepsilon I(P)}\nu(P))
=\prod_{[P]\in\mathcal P_\Gamma}
      \det(I_m-e^{-sT_\varepsilon(P)}\nu(P)).
\tag{32}
\]
因此 (1) 恰是原 \(D_\varepsilon,\zeta_\varepsilon\) 的唯一亚纯延拓。

**分母始终用 coefficient parameter \(w=s\)，不是 \(w=s+1\)。**
\(z\) 的平移只消去 transverse \(j\) 索引；不能把时钟 holonomy
也跟着平移。已有 H31 标量下降失败不影响这个诱导纤维身份。

## 7. 极点、零点与算子结论的严格边界

- \(\Delta\) 的允许极点位于固定 \(z=z_k\)，阶数至多 (11)；
  本页不宣称这些极点全部实际出现，也不计算其留数或相消。
- \(d_a(s)\) 的允许极点位于 \(\mathscr P-a\)，局部阶数至多 \(R\)。
  **不能**把这条界搬成 \(D_\varepsilon=d_0/d_1\) 的全部极点界：
  \(d_1\) 的零点也会给 ratio 新极点，其位置、阶数本页未分类。
- 这里只识别了经典核 transfer determinant 与同一 closed-orbit
  Selberg product 的解析芽并建立全平面延拓，不给 Laplace 算子、
  scattering determinant、cusp 正则化或任何自伴谱问题的身份。
- \(\mathcal L(z,w)\) 本身依赖两个参数；\(\eta_w\) 通常非酉。
  不把此族的 Fredholm 构造称为一个固定自伴 Hilbert–Pólya 算子。
- 没有重新启用 Stage 5／6、改变 Route、复写 frozen 138-row ledger、
  prime／zero fitting、旧输入 replay 或新实验。全部失败历史保留。
- 本结果是 AI 辅助的内部证明与既有经典理论在本案的组合，
  不是新颖性认证、形式化证明或外部独立科学复现。

## 8. 实际核读、失败路径与检查

主代理完整读回 [cusp][cusp] 与 [nuclear][nuclear]，逐项核对共同
chart、实际两个 branches、Taylor–Lerch 系数、核理想局部界及
residue 的方向和秩；另直接核读 Fedosova–Pohl 的 Property 5、
§4.3、Example 4.1、Theorem 4.2 与 §4.7 的相关段落。

本页 bordered determinant 及曲线限制由上述块矩阵代数与一变量
恒等定理直接展开。同模型读审席另核查 moving range、无逆条件、
固定切片阈值和 ratio 的零点边界，其同意不算外部独立证据。

Grothendieck 的部分普通网页／PDF 请求及 Bandtlow–Jenkinson 的
网页读取出现 timeout；没有把失败请求记录为成功。
随后以只读的 curl（--fail --location --max-time 25 --silent --show-error）
将公开 PDF 流式传给 pdftotext - -，用 rg 返回相关段落，
未保存或改写本地 PDF。实际读到前者 Chapitre II §2 Proposition 1
及式 (4)、后一篇 §4 开头的 canonical \(q\le2/3\) 接口。
这只是来源文本读取，不是科学计算或 PDF 视觉核验。

ARS 的有界论证／反对意见规范具体用于分开：核族前提、canonical
determinant 基础、局部 finite-rank 分解、右域身份及合法限制。
没有启动完整研究到发表流程或正式 Route 审查。
初次写入调用因文本中的反引号造成 JavaScript 解析错误，未执行文件写入；
修正工具输入后只以 apply_patch 新增本文件。之后只进行新文件读回、
控制字元／本地引用等必要文本检查。没有运行数值、符号、枚举、
实验、producer、稿件 build 或正式验证器。文本完整性不证明数学成立性。

[cusp]: internal_goal01_cusp_monodromy_and_bivariate_selberg_interface_20260909.md
[nuclear]: internal_goal01_joint_parabolic_nuclear_family_20260909.md
[fp]: https://link.springer.com/article/10.1007/s00029-019-0534-3
[bj]: https://webspace.maths.qmul.ac.uk/o.m.jenkinson/ruelle2.pdf
[groth]: https://www.numdam.org/article/BSMF_1956__84__319_0.pdf
