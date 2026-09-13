# Paper31 I08：指定点 Kummer 满像的有界数学可行性核查 V1

日期：2026-09-09 UTC。执行席：`/root/p31_qpi_kummer_feasibility_v1`。
范围：`MATHEMATICAL_FEASIBILITY_ONLY / NO_CANDIDATE_VOTE / NO_NOVELTY_SCORE`；`route_applicability: NOT_APPLICABLE`。
只核 I08 的几何满像链及有限域消费者，不创建 Paper31 项目，不写 22–30 页论文，不改变 4/5 已接受状态。

## 1. Claim、假设与状态

固定代数闭域 $k$、$\operatorname{char}k=p\ge5$、常数 $T\in k\setminus\{0,-27/256\}$，令 $K=k(h)$。
曲线、零点及指定点为
$$E/K:\quad v^2+huv-Tv=u^3-Tu^2,\qquad O=\text{无穷远点},\qquad P=(0,T).$$
固定素数 $\ell\ge5$、$\ell\ne p$。选相容分点 $\ell Q_{n+1}=Q_n$、$Q_0=P$，令 $M=T_\ell E$。
几何主张是所有 $n\ge1$ 的共同分点／挠点域 Galois 像为
$$ (\mathbb Z/\ell^n)^2\rtimes\operatorname{SL}_2(\mathbb Z/\ell^n). $$
技能三分法结论：此**几何主张 `PROVABLE AS STATED`**；下文逐步给证明，外部基础定理明确列出。
记以上范围为 A1–A4：代数闭常数、$p\ge5$、排除两个 $T$、$\ell\ge5$ 且 $\ell\ne p$。

| 被核线索 | 本件判定 | 必须保留的限定 |
|---|---|---|
| 有理椭圆曲面，$I_8+4I_1$ | `PROVABLE_UNDER_A1_A4` | 四次判别式须无重根 |
| 素于 $p$ 的同源映射保持 Hodge 次数／$\chi$ | `PROVABLE_UNDER_A1_A4` | 不是任意含 Frobenius 的同源映射 |
| 无 $K$-有理 $\ell$-isogeny，线性全像 | `PROVABLE_UNDER_A1_A4` | 用 $\ell\nmid1,8$ |
| $P$ 非挠且不属于 $\ell E(K)$ | `PROVABLE_UNDER_A1_A4` | 先证非挠，不能只用高度上界 |
| 整个仿射塔满像 | `PROVABLE_UNDER_A1_A4` | 下面直接证 $\operatorname{SL}_2$ 情形 |
| $P\in\ell E(\mathbb F_q)\Leftrightarrow\ell\nmid\operatorname{ord}P$ | `FALSE` | §7 给同一族、同一指定点反例 |
| 有限层恢复 $\ell$-点阶 | `PROVABLE_UNDER_DET_VALUATION_LT_n` | 其余必须保留截断／尾项 |
| 完整有效分布及可用的统一尾界 | `OPEN_IN_THIS_BOUNDED_NOTE` | 没有把下列群论冒充完整计数论文 |

## 2. 本人读取及证明依赖

本人 FULL 读工作区 `AGENTS.md`、`docs/WORKFLOW.md`、`proof-writer/SKILL.md`，以及十项想法文档全文（含 I08）。
批次入口定向读当前 4/5 与 P31 发现状态；未全文重读旧组合的证明包、稿件或评审票。
采用 `proof-writer` 的动作是把非挠性缺步、有限层／无限层差异及外部定理条件显式补齐，不改变项目要求。
证明依赖顺序：判别式与局部 Tate 模型 → 同源映射反证得不可约性 → 两个完整根子群 → 线性全像；
另一路是相交数及 Shioda 高度 → 指定点不可除；最后以中心元 $-I$ 的余循环恒等式合并两路。
Tate 一致化、Néron 模型的延拓性质、Shioda 高度公式是明确调用的基础定理，不声称在此从零建立其理论。

## 3. Step 1：纤维、极小性与有理性

直接代入 Weierstrass 不变量得
$$c_4=(h^2-4T)^2+24hT,\qquad \Delta=T^3D(h),$$
$$D(h)=h^4-h^3-8Th^2+36Th+16T^2-27T.$$
在 $\mathbb Z[T]$ 上的 Sylvester 行列式恒等式为
$$\operatorname{Disc}_hD=-T^2(256T+27)^3,\qquad \operatorname{Res}_h(D,c_4)=T^4(256T+27)^2.$$
本轮实际作精确 SymPy 展开／因式分解核验；这些是整数多项式恒等式，不是有限样本推断。
所以 A1–A4 下有四个互异有限根，每处 $\operatorname{ord}\Delta=1$、$c_4$ 为单位；极小约化类型为 $I_1$。
在 $t=h^{-1}$ 处令 $U=t^2u,V=t^3v$，方程成为
$$V^2+UV-Tt^3V=U^3-Tt^2U^2.$$
这里 $c_4$ 为单位，$\operatorname{ord}_t\Delta=12-4=8$，故极小约化类型为 $I_8$。
没有其他坏纤维，$j=c_4^3/\Delta$ 在无穷远有八阶极点，故曲线非等常数。
总曲面在 $uv\ne0$ 的开集上可解出 $h=(u^3-Tu^2-v^2+Tv)/(uv)$，其函数域为 $k(u,v)$。
因此光滑相对极小模型 $S$ 是有理曲面，$\chi(\mathcal O_S)=1$；亦有 $\deg\Delta_{\min}=12$。
这同时给出 Hodge 线丛 $\omega$ 次数为一；此处 $\chi$ 是算术 Euler 特征，不是拓扑 Euler 数十二。

## 4. Step 2：同源映射反证与线性全像

设 $E[\ell]$ 有 Galois 稳定直线 $L$；其循环子群定义一个 $K$ 上次数 $\ell$ 的商同源映射 $\phi:E\to E'$。
在任一 $I_m$ 处，完备域为 $k((s))$，Tate 参数 $q_s$ 满足 $v_s(q_s)=m$，$m\in\{1,8\}$。
Tate 一致化 $E\simeq\mathbb G_m/q_s^{\mathbb Z}$ 给出模 $\ell$ 惯性矩阵 $\left(\begin{smallmatrix}1&m\tau\\0&1\end{smallmatrix}\right)$。
因为 $\ell\nmid m$，其中有非平凡幺幂元；其唯一稳定直线是 $\mu_\ell$ 所在直线。
故局部 $L=\mu_\ell$，商由 $z\mapsto z^\ell$ 给出，Tate 参数成为 $q_s^\ell$，类型变为 $I_{\ell m}$。
在好约化处，$\ell$ 可逆，有限 étale 挠子群的商仍是椭圆概形，故 $E'$ 没有新坏约化。
因此 $E'$ 半稳定且 $\deg\Delta'_{\min}=\ell(8+4)=12\ell$，即 $\deg\omega'=\ell$。
另一方面，$\phi$ 及对偶 $\widehat\phi$ 延到 Néron 模型，在零截面的微分上线性映射复合为乘 $\ell$。
局部自由秩一模中两个乘子均整，乘积是单位 $\ell$，所以两乘子均为单位；全局 $\phi^*:\omega'\simeq\omega$。
故 $\deg\omega'=\deg\omega=1$，与 $\ell>1$ 矛盾；$E[\ell]$ 不可约。这是 [GP §5.1](https://math.richardgriffon.me/articles/GriffonPazuki_Isogenies_V2.pdf) 的同一微分机制。

记 $G\subset\operatorname{SL}(M)$ 为线性像；包含在特殊线性群是因为所有素于 $p$ 的单位根都在 $k$ 中，Weil 配对行列式为一。
在一个 $I_1$ 处，$q_s=s\cdot\text{单位}$ 的单位部分在 $k[[s]]$ 有相容 $\ell$-幂根，惯性在 $M$ 上给出完整 $U(\mathbb Z_\ell)$。
令其固定本原向量为 $e$。不可约性保证存在 $g\in G$，使 $e,ge$ 模 $\ell$ 独立，因而构成 $M$ 的一组基。
在这组基中，$U(\mathbb Z_\ell)$ 和其 $g$-共轭分别是全部上、下三角根子群，系数单位不改变其取值集合。
这两个根子群生成 $\operatorname{SL}_2(\mathbb Z_\ell)$：任意行列式一矩阵第一列有单位，交换两行后可作消元化为对角矩阵。
交换和对角矩阵也由根子群生成：若 $U(a),L(b)$ 为两类初等矩阵，$w(a)=U(a)L(-a^{-1})U(a)$，则 $w(a)w(-1)=\operatorname{diag}(a,a^{-1})$。
因此 $G=\operatorname{SL}_2(\mathbb Z_\ell)$；这直接处理整个塔，没有把模 $\ell$ 结论未经论证地提升。

## 5. Step 3：指定点的高度与不可除性

在有限处 $P=(0,T)$ 是整截面，且原方程关于 $v$ 的偏导在 $P$ 处为 $T\ne0$；它不经过有限节点。
在无穷远上述模型中 $P=(U,V)=(0,Tt^3)$，其特殊化是仿射节点，与零截面所在光滑无穷远点不同。
最小消解只吹起节点及其后继点，全部远离 $O$，故在 $S$ 上 $P\cdot O=0$。
对任一非零截面 $R$，设它在 $I_8$ 的分量编号为 $j\in\mathbb Z/8$，取 $0\le j\le7$。
[Shioda 高度公式](https://arxiv.org/pdf/0907.0298) 给
$$H(R)=2+2(R\cdot O)-\frac{j(8-j)}8,\qquad H(nR)=n^2H(R).$$
高度非负，零高度恰为挠点；相交数是非负整数，故所有正高度属于 $\tfrac18\mathbb Z$，至少 $1/8$。
若非零 $R$ 是挠点，则 $j(8-j)\le16$ 强制 $R\cdot O=0,j=4$。
若再有 $2R\ne O$，它的分量编号为零，公式给 $H(2R)=2+2(2R\cdot O)>0$，与挠性矛盾。
所以此配置中所有非零挠点均为二阶；这一步补上了原高度上界推理遗漏的前提。
原点的切线 $v=T-hu$ 与曲线的第三交点为 $(T,T-hT)$，取负得到 $2P=(T,0)\ne O$。
故 $P$ 非挠，而且 $0<H(P)\le2$。若 $P=\ell R$，则 $R$ 非挠并有
$$\frac18\le H(R)=\frac{H(P)}{\ell^2}\le\frac2{25}<\frac18,$$
矛盾。因此对范围内每个 $T,p,\ell$ 均有 $P\notin\ell E(K)$；不需要计算 $P$ 的准确分量编号或准确高度。

## 6. Step 4：从线性像到仿射满像

令 $K_{\rm tor}=K(E[\ell^\infty])$，$\Gamma=\operatorname{Gal}(K_{\rm tor}/K)=\operatorname{SL}_2(\mathbb Z_\ell)$。
记仿射像为 $H\subset M\rtimes\Gamma$，平移核为闭子模 $N=H\cap M$。
对 $W=E[\ell]$，任一连续一余循环 $c:\Gamma\to W$ 与中心元 $z=-I$ 满足
$$c(z)+z c(g)=c(g)+g c(z),\qquad c(g)=(g-1)(-c(z)/2).$$
因为 $2$ 可逆，每个余循环都是余边界，即 $H^1(\Gamma,W)=0$；这是直接写出的 Sah 型论证。
若 $N$ 在 $M/\ell M$ 中像为零，则所有固定挠点塔的 Galois 元都固定 $Q_1$，所以 $Q_1\in E(K_{\rm tor})$。
于是 $\sigma\mapsto\sigma Q_1-Q_1$ 降为 $\Gamma$ 上的余循环；由上式它是余边界，可平移一个 $W$ 中点使 $Q_1$ 成为 $K$-有理点。
这给 $P\in\ell E(K)$，违反 Step 3。因此 $\bar N\ne0$。
仿射共轭满足 $(b,A)(v,I)(b,A)^{-1}=(Av,I)$，故 $\bar N$ 是不可约模 $W$ 的子模，必为 $W$。
闭子群 $N$ 自动是 $\mathbb Z_\ell$ 子模；模 $\ell$ 满射使任意 $x\in M$ 可逐次近似为 $n_0+\ell n_1+\ell^2n_2+\cdots$，$n_i\in N$。
闭性给 $x\in N$，所以 $N=M$。又 $H\to\Gamma$ 满射，乘以平移可把每个 $(b,A)\in H$ 化为 $(0,A)$。
故 $H=M\rtimes\Gamma$；约化模 $\ell^n$ 得 §1 的全部有限层结论。证毕。
一般“挠点塔上不可除性加不可约性推出 Kummer 全像”的机制已在 [Jones–Rouse Theorem 3.4](https://arxiv.org/pdf/0706.2384) 中提供；本件不把该机制另计新贡献。

## 7. 有限域消费者：实际反例与正确有限层接口

同一原族取 $p=19,T=3,h=17,\ell=5$；此时 $-27/256=16$，$D(h)=3$，所以属于本件光滑参数范围。
指定点 $P=(0,3)$ 满足 $2P=(3,0)$、$3P=(3,9)=-2P$，故 $\operatorname{ord}P=5$。
但 $Q=(1,15)$ 满足 $2Q=(17,7),3Q=(10,3),4Q=(7,10),5Q=P$。
所有等式可用原广义 Weierstrass 加法逐项核验；本轮做了精确模十九核验，故原指定点确有 $P\in5E(\mathbb F_{19})$ 而 $5\mid\operatorname{ord}P$。

设 $T$ 定义在有限域、$h$ 为光滑有理纤维，Frobenius 在共同第 $n$ 层数据上为 $(b_n,A_n)$。
Kummer 正合列把 $P$ 在 $E(\mathbb F_q)/\ell^nE(\mathbb F_q)$ 的像对应到
$$[b_n]\in (\mathbb Z/\ell^n)^2/(A_n-I)(\mathbb Z/\ell^n)^2.$$
这里 $H^1(\mathbb F_q,E)=0$：Lang 映射 $F-1$ 是非零可分同源映射，因而在代数闭点上满射；由此正合列确实给出上述同构。
若 $r=v_\ell\#E(\mathbb F_q)<n$，则 $\ell^n$ 杀死整个 $\ell$-主分量，而在素于 $\ell$ 部分上可逆。
故商恰是 $E(\mathbb F_q)[\ell^\infty]$，$[b_n]$ 的加法阶就是 $\ell^{v_\ell\operatorname{ord}P}$。
条件可从挠点层识别：$\#E(\mathbb F_q)=\det(I-A)$，所以 $\det(I-A_n)\not\equiv0\pmod{\ell^n}$ 等价于 $r<n$。
若行列式模 $\ell^n$ 为零，只得到商中的截断点阶；例如循环群 $\mathbb Z/\ell^{n+1}$ 中的 $\ell^n$ 倍生成元，其商像为零但阶为 $\ell$。
改变分点或 Tate 基分别改变 $b_n$ 一个 $(A_n-I)$ 像或作线性同构，故该商中点阶是共轭不变量。
算术像的行列式不是任意单位：若常数域为 $\mathbb F_{q_0}$，第 $n$ 层全像为平移群半直积 $\det^{-1}\langle q_0\bmod\ell^n\rangle$；$q=q_0^a$ 时 $\mathbb F_q$ 点落在行列式 $q$ 的陪集中。
证明是几何群已含全部平移及 $\operatorname{SL}_2$，算术像商只剩 Weil 配对的行列式，后者由常数 Frobenius 生成。
固定 $\ell,n$ 的有限域 Chebotarev 可作用于这些有限陪集事件；本件没有核定具体有效常数、各层覆盖亏格或统一尾界，因此完整分布定理仍记 `OPEN_IN_THIS_BOUNDED_NOTE`。
尤其不能把全 $\operatorname{GL}_2$ Haar 平均直接替换固定行列式陪集比例，也不能把某一固定层的计数说成无截断点阶分布。

## 8. Sources、读取层级及开放边界

- [Griffon–Pazuki, Isogenies of elliptic curves over function fields，作者 PDF](https://math.richardgriffon.me/articles/GriffonPazuki_Isogenies_V2.pdf)：实读导言 Theorem A、§2.3 的 Tate 一致化段、§5.1 Theorem 5.1 及完整证明（印刷页 11–12）。后者条件为非等常数、双可分同源映射；次数 $\ell\ne p$ 满足。未称 FULL 全文阅读；Parshin 原始论文未读。
- [Schütt–Shioda, Elliptic Surfaces, arXiv:0907.0298](https://arxiv.org/pdf/0907.0298)：实读 §8.2–8.4、§11.4–11.8 的映射／高度公式、Theorem 11.5、Table 4 以及 §11.11.1 的 $I_8+4I_1$ 两种格情形。所需公式及其适用的代数闭特征设定已核；非 FULL 全文阅读。
- [Jones–Rouse, Iterated endomorphisms and abelian algebraic groups, arXiv:0706.2384](https://arxiv.org/pdf/0706.2384)：实读 Theorem 3.4 及完整证明、Theorem 5.2 及完整证明（分别印刷页 11–13、21）；Lemma 3.6/3.7 的声明及邻近段。5.2 原条件是 $\operatorname{GL}_2$ 全像，不能原字套给本件代数闭常数的 $\operatorname{SL}_2$；§6 已直接修补这一接口。

本件说明：原满像猜式在明确排除范围内有一条短闭合证明，主要由已知同源映射／高度／Kummer 工具及少量本族代数核验组成；这是可行性结果，不是全球查新、容量或候选准入结论。
没有扩大到 $T=-27/256$、$p=2,3$、$\ell=2,3,p$；没有把泛不可除性外推成每个闭纤维不可除性。
实际新增仅本文件；实际 GPU 0，CPU 仅秒级精确代数及小域加法诊断，无大型枚举、无实验部署、无旧稿／锁／接受记录改写。
