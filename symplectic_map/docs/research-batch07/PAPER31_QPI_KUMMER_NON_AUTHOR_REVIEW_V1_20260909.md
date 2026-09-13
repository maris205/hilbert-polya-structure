# Paper31 I08：几何 Kummer 满像及有限域消费者非作者审查 V1

日期：2026-09-09 UTC。审查席：`/root/p31_qpi_kummer_non_author_review_v1`。
身份：全新非作者独立 Codex 审查席；依本次 xhigh 派发审查，未参与输入件撰写或修订。
模型披露：`gpt-5.4` 不可用，本次为独立 Codex 替代；不冒称该模型，也不声称跨模型双票。
范围：`MATHEMATICS_ONLY / GEOMETRIC_FULL_IMAGE_AND_SECTION_7 / NO_NOVELTY_OR_CANDIDATE_VOTE`。
`route_applicability: NOT_APPLICABLE`；本件不是 Route A/B、正式论文或 PDF 验收。

## 1. 输入身份、读取与总判定

唯一数学审查输入：[作者可行性 V1](PAPER31_QPI_KUMMER_FEASIBILITY_V1_20260909.md)，全文 **138 行**。
实际核对 SHA256：`d297f6219bbd0e17062cf6f20e245c96f37e0f54ba84cc834990e56ec3154b38`。
本席 FULL 读输入全部 138 行、`AGENTS.md`、`docs/WORKFLOW.md`、`proof-writer/SKILL.md` 与 `skills-codex/research-review/SKILL.md`。
批次入口仅定向读当前接续与 4/5 状态；未重开 Papers27–30、旧新意票或冻结构建。
技能影响：逐项列真实证明依赖、检验特征条件与量词，再独立给结论；不按技能模板扩写实验或准入评分。

**Overall：`PASS_BOUNDED`。技能三分法：几何主张 `PROVABLE AS STATED`。**
在作者明确的参数域内，没有发现阻断原几何满像结论或 §7 正确接口的硬缺口；不需要改科学门槛。
本票接受的是下列依赖链及有限层条件结论，不接受作者已标为开放的有效分布、统一尾界或完整论文贡献。

## 2. Claim、假设与记号

固定代数闭域 $k$，$\operatorname{char}k=p\ge5$，$T\in k\setminus\{0,-27/256\}$，$K=k(h)$。
考虑
$$E/K:\quad v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),\qquad O=\text{无穷远零点}.$$
固定素数 $\ell\ge5$、$\ell\ne p$；$M=T_\ell E$，$W_n=M/\ell^nM$，$W=W_1=E[\ell]$。
取 $Q_0=P$、$\ell Q_{n+1}=Q_n$；共同分点／挠点域是 $K(E[\ell^n],Q_n)$。
被核全称命题是对上述每个 $k,p,T,\ell$、每个 $n\ge1$，其像为
$$ (\mathbb Z/\ell^n)^2\rtimes\operatorname{SL}_2(\mathbb Z/\ell^n). $$
没有把某个一般 $T$、几乎所有 $\ell$ 或单个有限层偷偷替换上述全称量词。
作者 §7 的算术消费者另假设 $T\in\mathbb F_{q_0}$，取 $q=q_0^a$ 及光滑有理纤维；Frobenius 采用 $q$ 次幂的算术约定。
算术“全像”指 $\mathbb F_{q_0}(h)$ 的整条族覆盖，绝非某一个有限域纤维的循环 Galois 像。

## 3. 外源实际读取层级与适用性

全部下列来源已实际联网打开 PDF，并读取相关正文，不以搜索摘要代替定理检查。

| 来源与实际读取范围 | 本轮核对的用途与边界 |
|---|---|
| [Griffon–Pazuki 作者 PDF](https://math.richardgriffon.me/articles/GriffonPazuki_Isogenies_V2.pdf)：导言 Theorem A；§2.3 全节；§5.1 Theorem 5.1 及完整证明（印刷页 11–12） | 完备赋值域上的 Tate 描述，以及双可分同源映射保持微分高度。代数闭 $k$ 完美；次数 $\ell\ne p$ 保证同源及对偶均可分。未读 Parshin 原始论文。 |
| [Schütt–Shioda, Elliptic Surfaces](https://arxiv.org/pdf/0907.0298)：§3.1、3.3 设定；§8.2–8.4；§11.4–11.8 完整相关正文；Theorem 11.5、Table 4；§11.11.1 全段 | 代数闭常数、带截面且存在奇异纤维的代数曲面框架；核对高度核、二次性与 $I_n$ 修正项。两种 $I_8+4I_1$ 格情形均保留，不预先选择其中一种。 |
| [Jones–Rouse, Iterated endomorphisms and abelian algebraic groups](https://arxiv.org/pdf/0706.2384)：Theorem 3.4 与完整证明；Theorem 5.2 与完整证明（印刷页 11–13、21） | 3.4 要求挠点扩张上的不可除性；5.2 写的是 $\operatorname{GL}_2$ 全像，不能直接套成 $\operatorname{SL}_2$。本件依作者直接余循环证明核验，未拿来源替代该步骤。 |

以上均是 `TARGETED_THEOREM_AND_PROOF_READ`，不是三篇 `FULL_TEXT_READ`，也不是全球查新。
外源提供基础理论；以下本族代数、局部矛盾及群论过桥均逐步复核，而非仅接受作者“已读”的声明。

## 4. Proof Strategy 与 Dependency Map

1. 整数多项式恒等式及极小模型，给出 $I_8+4I_1$、非等常数、有理性及 $\deg\omega=1$。
2. 假设稳定直线，逐坏处识别唯一局部核，使所有 $I_m$ 变为 $I_{\ell m}$；双同源微分保持 $\deg\omega$，矛盾。
3. 模 $\ell$ 不可约性加一个 $I_1$ 的完整惯性根子群，产生两个横截根子群，得整个 $\operatorname{SL}_2(\mathbb Z_\ell)$。
4. 相交数、Shioda 高度及 $2P=(T,0)$，先证明非挠，再证明 $P\notin\ell E(K)$。
5. 中心元 $-I$ 消去 $H^1(\Gamma,W)$；平移核模 $\ell$ 非零、不可约、闭性，逐级得到完整平移群。
6. 有限域 Kummer 正合列及行列式阈值给出截断接口；算术行列式陪集从 Weil 配对确定。

## 5. Proof Check A：纤维、极小性、有理性

独立使用广义 Weierstrass 的 $b_i,c_4,\Delta$ 公式，从 $a_1=h,a_2=-T,a_3=-T,a_4=a_6=0$ 重算。
实际 SymPy 精确运算给出
$$c_4=h^4-8Th^2+24Th+16T^2,\qquad\Delta=T^3D(h),$$
$$D(h)=h^4-h^3-8Th^2+36Th+16T^2-27T,$$
$$\operatorname{Disc}_hD=-T^2(256T+27)^3,\qquad\operatorname{Res}_h(D,c_4)=T^4(256T+27)^2.$$
这是整系数恒等式核验，不是样本搜索；故约化到每个允许特征仍成立。
排除 $T=0,-27/256$ 正好确保四根互异且不与 $c_4$ 共零；每处为极小 $I_1$。
在 $t=h^{-1}$ 处，$U=t^2u,V=t^3v$ 给 $V^2+UV-Tt^3V=U^3-Tt^2U^2$。
其 $c_4$ 常数项为一，$\operatorname{ord}_t\Delta=8$；单位 $c_4$ 同时排除进一步缩小模型，类型为 $I_8$。
所有有限好处与无穷远已覆盖；$j$ 在无穷远有八阶极点，故非等常数，不存在隐含常数迹问题。
总曲面的稠密开集由 $h=(u^3-Tu^2-v^2+Tv)/(uv)$ 解出，函数域确为 $k(u,v)$。
因此光滑模型是有理曲面，$\chi(\mathcal O_S)=1$；极小判别式次数十二与 $\deg\omega=1$ 一致。
结论：`PASS`；没有使用复拓扑或特征零分类替代正特征证明。

## 6. Proof Check B：同源反证与完整线性塔

一个 Galois 稳定 $\mathbb F_\ell$ 直线对应 $K$ 上有限 étale 循环子群，可形成次数 $\ell$ 商同源映射。
每个坏处的剩余域为代数闭 $k$，乘法约化分裂；在 $k((s))$ 可用 Tate 参数 $q_s$，$v(q_s)=m\in\{1,8\}$。
单位部分有相容 $\ell$ 次幂根，而参数的赋值给惯性矩阵的上右项 $m\tau$。
因为 $\ell\nmid m$，模 $\ell$ 有非平凡幺幂元，其唯一稳定直线就是 $\mu_\ell$ 线。
因此假想全局核在每个坏处都必须是该线；商 $z\mapsto z^\ell$ 的目标参数是 $q_s^\ell$，不是 $q_s^{1/\ell}$。
所以五个坏处全部变成 $I_{\ell m}$。好处的有限 étale 子群延至椭圆概形，商仍光滑，不会新增坏处。
于是目标半稳定曲面的极小判别式次数是 $12\ell$，其 Hodge 次数为 $\ell$；不需要假设目标曲面也有理。
另一方面，两方向同源映射都由 Néron 延拓性质延伸；在零截面微分上，复合是乘 $\ell$。
每个 DVR 上这给两个整乘子的乘积为单位，故各乘子均为单位，得到全局 $\omega'\simeq\omega$。
这里使用的是零截面的秩一微分模；不要求商映射在特殊纤维的全部分量上双射。
此结论与 $\deg\omega'=\ell\ne1$ 矛盾，故 $W$ 不可约。正特征中若允许 $\ell=p$，单位论证失效，不能外推。

Weil 配对及代数闭常数使线性像 $G\subset\operatorname{SL}_2(\mathbb Z_\ell)$。
任一个 $I_1$ 的参数赋值为一，所以惯性含完整 $U(\mathbb Z_\ell)$，不是只有某个有限指数上三角子群。
若 $e$ 为其本原固定向量，不可约性给 $g\in G$ 使 $e,ge$ 模 $\ell$ 独立；二者因此是整 Tate 模的一组基。
在此基中，原根子群与共轭根子群固定两条坐标轴，非零系数都是单位，分别等于全部 $U$ 与 $L$。
两根子群以消元生成所有行列式一矩阵；第一列至少一个元素为单位，换行与对角缩放也由根元实现。
作者的 $w(a)=U(a)L(-a^{-1})U(a)$ 满足 $w(a)w(-1)=\operatorname{diag}(a,a^{-1})$，符号正确。
结论：`PASS`；整塔满像已直接证明，不依赖“模 $\ell$ 满像自动提升”的未述定理。

## 7. Proof Check C：非挠性与指定点不可除

有限处 $P=(0,T)$ 是整截面，关于 $v$ 的偏导在该点为 $T\ne0$；无穷远极小模型中 $P=(0,Tt^3)$。
其仿射特殊化与 $O$ 不同；节点消解不接触 $O$，故严格变换仍满足 $P\cdot O=0$。
对非零截面 $R$，只需 $I_8$ 分量编号 $j\in\{0,\ldots,7\}$；$I_1$ 不贡献修正项，公式是
$$H(R)=2+2(R\cdot O)-j(8-j)/8.$$
所用高度是 Mordell–Weil 配对自身；无需另约定与其他规范高度的二倍归一化。
Theorem 11.5 给二次性、非负性及零核恰为挠点；不同截面的相交数为非负整数，故正高度至少 $1/8$。
若 $R\ne O$ 为挠点，高度零迫使 $R\cdot O=0,j=4$。
分量映射是群同态，故 $2R$ 在零分量；如果 $2R\ne O$，则 $H(2R)=2+2(2R\cdot O)>0$，矛盾。
所以非零挠点只能二阶；未假设曲面一定有二阶挠点，也未将 $I_8$ 两种可能格混为一种。
将切线 $v=T-hu$ 代入原方程，实际精确结果为 $-u^2(u-T)$；第三交点取负确为 $2P=(T,0)\ne O$。
于是 $P$ 非挠，且 $0<H(P)\le2$。若 $P=\ell R$，则
$$1/8\le H(R)=H(P)/\ell^2\le2/25<1/8,$$
矛盾。结论：`PASS`；非挠性前提已经补齐，不是仅靠高度上界推出不可除。

## 8. Proof Check D：平移核与仿射塔

令 $\Gamma=\operatorname{SL}_2(\mathbb Z_\ell)$、$H\subset M\rtimes\Gamma$，$N=H\cap M$；这些像由紧性而闭。
对任意连续余循环 $c:\Gamma\to W$，中心元 $z=-I$ 给
$$c(z)-c(g)=c(g)+g c(z),\qquad c(g)=(g-1)(-c(z)/2).$$
故 $H^1(\Gamma,W)=0$；该计算直接适用于此 $\operatorname{SL}_2$，没有误用 Jones–Rouse 的 $\operatorname{GL}_2$ 假设。
若 $N$ 在 $M/\ell M$ 的像为零，固定整个挠点塔的 Galois 群就固定 $Q_1$，从而 $Q_1\in E(K_{\rm tor})$。
其下降余循环因上式成为余边界；减去一个 $W$ 中点可使 $Q_1$ 为 $K$-有理，同时仍为 $P$ 的 $\ell$ 分点。
这与 §7 的不可除性矛盾，所以 $\bar N\ne0$。仿射共轭公式使 $\bar N$ 为 $W$ 的 $\Gamma$ 子模，故 $\bar N=W$。
闭加法子群 $N$ 是 $\mathbb Z_\ell$ 子模；逐次选模 $\ell$ 代表元并取收敛和，得到 $N=M$。
线性投影已经满射，消去任意提升的平移部分即得 $H=M\rtimes\Gamma$；约化到所有有限层结论成立。
结论：`PASS`；不需要额外假设在挠点塔上不可除，此性质已通过余循环反证获得。

## 9. Proof Check E：§7 反例、有限层点阶、算术陪集

独立运行广义 Weierstrass 精确模十九加法，且逐次检验输出点在曲线上，得到以下结果。
参数 $p=19,T=3,h=17,\ell=5$ 满足 $-27/256=16,D(17)=3$，故不是坏参数或奇异纤维。
$$P=(0,3),\quad2P=(3,0),\quad3P=(3,9),\quad4P=(0,0),\quad5P=O.$$
$$Q=(1,15),\quad2Q=(17,7),\quad3Q=(10,3),\quad4Q=(7,10),\quad5Q=P.$$
另核到 $25Q=O$；由 $5Q=P\ne O$ 和 $\operatorname{ord}P=5$ 知 $\operatorname{ord}Q=25$。
这确为“指定点五可除但点阶被五整除”的同族反例，不是换点或泛群反例。

对光滑有限域纤维，记算术 Frobenius 为 $F$，Tate 模作用为 $A$，第 $n$ 层共同作用为 $(b_n,A_n)$。
$F-1$ 微分为 $-1$，是非零可分同源映射；故在代数闭点上满射，$H^1(\mathbb F_q,E)=0$。
Kummer 正合列和有限模的连续循环群上同调因此给
$$E(\mathbb F_q)/\ell^nE(\mathbb F_q)\simeq W_n/(A_n-I)W_n,\qquad P\longmapsto[b_n].$$
记 $r=v_\ell\#E(\mathbb F_q)$。若 $r<n$，$\ell^n$ 杀死全部 $\ell$-主分量且在其余部分可逆，所以 $[b_n]$ 的阶恢复 $\ell^{v_\ell\operatorname{ord}P}$。
恒等式 $\#E(\mathbb F_q)=\det(I-A)$ 使该条件恰等价于 $\det(I-A_n)\not\equiv0\pmod{\ell^n}$。
这是充分且可识别的阈值；行列式为零的层仍只交付截断类，不承诺完整点阶。
作者循环群例子有效：$\mathbb Z/\ell^{n+1}$ 中 $\ell^n$ 倍生成元在模 $\ell^n$ 倍群的商中为零，但自身阶为 $\ell$。
分点平移改变 $b_n$ 一个 $(A_n-I)$ 像；换基诱导商同构，故商中类的阶是仿射共轭不变量。

族在 $\mathbb F_{q_0}(h)$ 的算术像包含全部几何平移及 $\operatorname{SL}_2$，商仅由行列式决定。
Weil 配对给该行列式像为 $\langle q_0\bmod\ell^n\rangle$，因此完整算术像正是
$$W_n\rtimes\det^{-1}\langle q_0\bmod\ell^n\rangle.$$
$\mathbb F_{q_0^a}$ 有理点的 Frobenius 落在行列式 $q_0^a$ 的陪集中；一般不能用全 $\operatorname{GL}_2$ 平均代替。
在光滑开集上，挠点覆盖和拉回的分点覆盖均为有限 étale；固定层陪集事件可作为有限域 Chebotarev 的输入。
结论：`PASS_BOUNDED`；这里只核合法事件与覆盖接口，没有证明某个具体误差式或无限层分布。

## 10. Corrections、Open Risks 与交付界线

必须修订项：**无**。建议正式写作时明写本件 §2 的算术 Frobenius 约定及“全像属于族覆盖”，属消歧，不是改变假设或降门槛。
保持开放：有效常数、各层覆盖亏格、层间控制、固定行列式尾事件的可用统一界，以及完整无截断点阶分布。
不接受的外推：$T=0,-27/256$，$p=2,3$，$\ell=2,3,p$，每个闭纤维都不可除，或全 $\operatorname{GL}_2$ Haar 比例。
本票不判断 I08 的新意、与组合碰撞、正文容量、是否值得独立成篇或 Paper31 准入；4/5 状态不改变。
实际诊断为精确代数与两个点的有限次加法，CPU 秒级、GPU 0；计算用于排错，不替代上述一般证明。
唯一持久新增为本审查文件；作者件、索引、项目目录、旧稿、锁和已接受记录均未改写。
终态：`PASS_BOUNDED / ORIGINAL_GEOMETRIC_QUANTIFIERS_PRESERVED / EFFECTIVE_DISTRIBUTION_OPEN`。
