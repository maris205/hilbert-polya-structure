# 287 独立内部复核：非线性时钟与完整不动核心重数

**Candidate ID:** ANG-20260920-NRF01  
**Status:** OWNED NONLINEAR CLOCK; UNCOUNTABLE PRIME-PACKET MULTIPLICITY — STOP / FORK  
**Verdict:** 三个有界检查点完成，无待修正的数学阻断项。完整联合 Haar 时钟成立；每个素数根的不可数不动核心已决定单包目标失败，不继续高周期分类。

## 1. 输入绑定与实际顺序

| 实际审阅输入 | SHA-256 |
|---|---|
| 原始 version-1 冻结卡 | 451eb56764544d77e21ece5458e2a465bdcec756d23aca37aaa4a9b0e5cfd362 |
| 完整比较的主文 | 1e47a06e6080d2f08e745c9c059ba86bbb344630f44078d72b9c2728adaa45dd |

检查点 1 仅读完整原卡，独立推导实际分支、联合 Haar、全 clock、不动状态、完整稳定子及 NONLINEAR-OFF 控制；先向主控发送 raw 结论，再读取主稿。

检查点 2 完整读取并比较上述主文；检查点 3 对零因子、null clock、重数、owner 与停止范围作反方核对。没有要求作者修改数学，也没有为了制造批评而扩大判据。

原卡若事后追加行政 outcome，仍以上述原始字节为 raw 输入。本审查者仅写本文件；旧包、主稿、卡和其他记录均未修改。没有科学计算、有限模数 census、参数搜索、外部文献扩展或高周期审计。

## 2. 检查点 1：真实分支与联合 Haar owner

本对象是全部 \(n\ge2\) 根及全部 \(K^2\)，而非单种子 radix 类、对角子空间或某个 prime-primary 因子。固定 \(n,j\) 时，真实源域为 \((j+nK)\times K\)，目标是完整的根 \(g(n+j)\) 上 \(K^2\)。

给定目标 \((u,v)\)，公式

\[
\theta_{n,j}(u,v)=\bigl(n,\ j+n(v-Q(u)),\ u\bigr)
\]

确实有源 digit \(j\)，且与原分支双向互逆；整数乘法的单射性保证确切除法。各分支是 compact-open 域到完整目标根的同胚，故 T 为 local homeomorphism。

主审 raw 的联合测度证明先考察 \(S(u,v)=(v-Q(u),u)\)。它在每个有限联合 residue 商上是置换，逆为 \((a,b)\mapsto(b,a+Q(b))\)；均匀联合圆柱生成 Borel 集，故 S 保存全部联合 Haar。

再用 \((a,b)\mapsto(j+na,b)\)，只有一个坐标被缩放，因此对任意 Borel \(E\subset K^2\)，

\[
\mu(\theta_{n,j}E)=\frac1n(h\otimes h)(E).
\]

这不是 \(1/n^2\)，也不是从形式行列式猜测的密度。主文改用等价的 fibre translation 加 Fubini 来证明 S 的联合 Haar 不变性，方法成立。

\(g\) 的值必为素数；每个素数根 \(p\) 又由 \(n=p,j=0\) 的完整分支覆盖。T 的像恰为所有 prime-root fibres，合数根无 incoming branch，但仍保留在完整源中。因此不能称 T onto。

有限实际逆前缀的 IMAGE 缩放为 \(1/D_\alpha\)，不要求复合前缀仍为 affine。对完整 retained-lag branch pair，

\[
J(g)=D_\beta/D_\alpha,\qquad
c(g)=\log D_\alpha-\log D_\beta.
\]

相同箭头的较长表示同步延长两前缀；同一实际 tail 的 index product 抵消，保证表示无关。实际 branch refinements 给出复合、逆与可数 compact-open 基；端点和 lag 分离不同箭头，得到所述 Hausdorff、局部紧、第二可数 étale owner。

clock 在 bisections 局部常值。全支撑排除两个连续 density 版本只在 null points 不同，故它覆盖所有不动核心，不需声明额外 null-point 版本。实扩张的全部实平移完整、联合连续；未证明 coarse quotient Hausdorff 或 circle embedding。

## 3. 完整不动状态：不能把 K 当整环

固定根要求 \(n=g(n+j)\)，所以 \(n=p\) 为素数。又 \(p\mid(p+j)\)、\(0\le j<p\)，故 \(j=0\)。两个 seed 相等为 \(x=y=z\)，剩余方程化为

\[
z=z/p+z(1-z)
\quad\Longleftrightarrow\quad
pz^2=z.
\]

后一个方程模 \(p\) 自动给出零 digit，故逆向没有引入不合法分支。不能在 \(z(pz-1)=0\) 中擅自约消 \(z\) 或把它当普通整环二根问题。

令 \(e=pz\)，完整参数化是

\[
E_p=\{e\in K:e^2=e,\ e\in pK\},\qquad
F_p=\{(p,e/p,e/p):e\in E_p\}.
\]

正向由 \(pz^2=z\) 得到幂等元；逆向将 \(e=pz\) 代入 \(e^2=e\)，得到 \(p(pz^2-z)=0\)，由非零整数乘法单射得回原方程。这是 \(K\) 内的唯一确切商，不是任意加入的有理缩放箭头。

模每个 \(\ell^a\) 的幂等元仅为 0、1：同一素数 \(\ell\) 不可能同时整除 \(e\) 与 \(e-1\)，所以积被 \(\ell^a\) 整除必由其中一因子承担。兼容性固定每个 prime tower 的一位选择。CRT 允许不同素数的选择相互独立。条件 \(e\in pK\) 固定 p-tower 为 0，其余无限多个位自由。

所以每个 \(F_p\) 恰有 \(2^{\aleph_0}\) 个完整状态；\(p=2\) 无例外。等价的 seed 描述是 p-primary 分量为零，其他 \(\ell\)-primary 分量各为 0 或 \(p^{-1}\)。

若只看嵌入整数，\(pz^2=z\) 的唯一整数解是 0；其余解全被这种限制遗漏。对角关系来自完整不动方程，不是对原 source 的事先约束。

每根的不动集位于联合 Haar 零测对角线中：单点 Haar 为零，可用 Fubini，或用模 \(m\) 的对角同余集质量 \(1/m\) 证明。可数根之并仍零测；不可数核心不能因此从 owner 中删除。

## 4. 完整稳定子与决定性停止

若 \(z_\ast\in F_p\)，全部前向迭代均为该点。retained-lag owner 中完整 isotropy 因而恰为每个整数 lag 一个箭头：

\[
G_{z_\ast}^{z_\ast}
=\{(z_\ast,k,z_\ast):k\in\mathbb Z\},\qquad
c(z_\ast,k,z_\ast)=k\log p.
\]

每次实际 branch 消耗根 \(p\)，所以完整时间返回群是 \((\log p)\mathbb Z\)，最小正值为 \(\log p\)，正重复为 \(r\log p\)。clock kernel 为零，fixed-object extension isotropy 平凡；它与非平凡 time-return group 不同。

两个不同不动核心绝不共享实际前向尾：\(T^m z=z\)、\(T^k w=w\) 强迫共同尾仅在 \(z=w\) 时存在。实时间平移不改变基础箭头不存在的事实。因此同根、同时长也不能合并这些包。

每个核心的全部有限前像由实际 prefix arrows 进入同一包，不增加或合并核心包。每个素数根因此已经提供连续统多个互异的 least-\(\log p\) fixed-core packets。

这是足够的重数反例，不是全部高周期／全 packet ledger。按原卡立即停止 prime-single-packet 晋升，未继续检查其他周期的个数、时间或闭包。

## 5. 独立 NONLINEAR-OFF 控制

Q identically zero 的控制是另一个完整 owner。其真实逆分支为 \((u,v)\mapsto(j+nv,u)\)，由 scale/swap 同样得到 IMAGE factor \(1/n\)，并非直接借用主对象结论。

固定根与 digit 仍为 \(p,j=0\)，但 seed 方程现在是 \(x=y=z=z/p\)，即 \((p-1)z=0\)。整数乘法单射迫使 \(z=0\)，故控制的完整 fixed set 恰为 \(\{(p,0,0):p\ {\rm prime}\}\)。

每个这样的固定核心具有自己的 \(\mathbb Z\) lag isotropy 与 \((\log p)\mathbb Z\) time group。这里只确认每素数一个固定核心及其包，不确认没有其他高周期包，也不把控制当作修复后的 main candidate。

## 6. 检查点 2/3：全文比较与反方边界

主文 Lemma 1、Proposition 2、Lemmas 3／Proposition 4、Theorem 5 与控制段均符合 raw 推导，无需数学修改。尤其：idempotent 逆向、zero digit、clock sign、联合 Borel 缩放及所有 fixed-core 稳定子均闭合。

- 最强的反方质疑是 null 不动核心可否忽略。原卡保留完整源且连续 clock 已确定这些点；conull reduction 会换 owner，不能用于修复重数。
- “二次式至多两根”不适用于完整 \(K\)。逐 prime-power 的两个选择经 CRT 独立组合，正是额外解的来源。
- 联合 shear 可逆，不受不同 owner 上单坐标 Q 像奇异性的结论支配；也不因此变成保体积的经典 Hénon map。
- prime-valued root readout 不等于 prime-single-packet selection。有限可执行的 divisibility 算法不自动解决结构选择的自然性。
- fixed-core 重数失败不需要也不许可高周期 census。Qoff 的一个固定核心不能被升级成其完整目标通过。
- 不将抽象 cyclic packets 称作已证明的闭嵌入圆，不借用 285 的不同对象拓扑；不把 286 的单种子类定理应用到本 nonlinear two-register owner。

## 7. Provenance、内部复核与交付

本轮只按原卡记录 283 E-lane 的 division／swap／quadratic 模板先例；该旧提案未准入，未读其结果来替代当前证明，也不声称本轮首次提出该模板。greatest-factor 的其他旧 owner 同样未提供本轮时钟或返回定理。

采用 ARS academic-research-suite 三检查点。主审的 raw 全结论先于主稿读取。辅助 affine_stabilizer_scope 仅 raw-card 独立核对全部 fixed states、p=2、稳定子、重数与 Qoff；未读主稿或他人答案、未证明 joint Haar、未写文件或检查高周期。主审完成完整 owner 与全文比较。

这是同模型、共享项目上下文的内部审查，不是外部同行评审、不同模型的独立误差保证或机器形式验证。没有数值实验、旧包重评分或外部发布。

最终维持 **STOP / FORK**：保留已建立的 nonlinear joint-Haar clock，同时保留 fixed-core 额外重数的决定性失败。自然性 OPEN；T3 未供应／未开展，经典几何字段不适用，formal UNASSIGNED、Route B NOT INVOKED；241/242 未触碰。
