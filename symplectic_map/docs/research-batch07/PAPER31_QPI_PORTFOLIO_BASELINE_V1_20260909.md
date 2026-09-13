# Paper31 发现阶段：qPI 组合内数学基线 V1

日期：2026-09-09 UTC。执行者：`/root/p31_qpi_portfolio_baseline_v1`。
类型：`BOUNDED_PORTFOLIO_BASELINE`；`route_applicability: NOT_APPLICABLE`。
本件只盘点指定既有结果及开放出口，不生成或排名想法，不进行全球查新、候选评分、准入或旧数学复审。
当前 P30 已本地接受，Batch07 为 4/5；P31 仅发现阶段，未创建项目。历史处置中的“3/5／未立项”只是当时快照。
依据为已接受处置与实际接受稿 V4；两份已有接口盘点按其本人实读 V3 身份消费，不冒称它们读过 V4。

## 1. 先固定对象身份

qPI 一步为 $F_t(x,y)=(st/(sx-y),sx/y)$、$t\mapsto st$；单位时间部分固定原矩阵 $A$、降序词积 $M_{r,s}$ 与 $I_{r,s}=[z^r]\operatorname{tr}M_{r,s}$。
必须保留原八中心曲面、反典范八环 $D$、完整 $\mathcal U=S\setminus D$ 及四条末端线；谱等价矩阵、环面开集或另一归一化微分不自动是同一对象。
域上几何部分取 $r=\operatorname{ord}(s)$、$T=t^r$、$\varepsilon=(-1)^{r+1}$；正特征自动 $p\nmid r$。实际原能级和原域不得由无标记同构替换。
圆分部分取 $r=mp^a$、$p\nmid m$、$N=p^a$、$\pi_a=\zeta_{p^a}-1$，$\alpha_a=p^{-a}d_{\rm state}I_{mp^a,s_a}$；先在整数模型整除，再约化。
这里 $d$ 只微分两个相对状态方向，固定时间和基环；$J=I_{m,\eta}(x,y;\bar t_a)$，$H=H_p(\bar t_a^m,J;(-1)^{m+1})$，$\sigma=(N-1)/(p-1)$。
临界理想 $C_a=\mathfrak c(\alpha_a)$ 是自由秩二余切模中两个系数的理想；$C_a^{+2}=C_a+(\pi_a^2)$ 不是 $C_a$。对象定义见 [V4-I]；接口量词见 [IF] §1–2。
非单位时间必须另明说底环 $B=\mathbb Z[q^{\pm1},\tau]$、原有序中心四簇 $1+2+3+2$、$L=-K$；延续的是曲面与层，不声称 $\tau=0$ 时原映射仍双有理，见 [NU] §2。

## 2. 已知基线：已证结果不能因未独立成文而重记未知

下表“已接受”继承所列处置的数学合取，不表示本执行者重新阅读并复审所有上游作者证明；所有范围均保留。

| 对象／量词 | 已证且须扣除的输出 | 不得误读的边界 | 依据 |
|---|---|---|---|
| 原 pencil；任意精确有限阶、每个固定非零时间、全部允许特征含 2、3 | $(I_r)_\infty=rD$、法丛精确阶 $r$、最小完整亏格一 pencil；每个有限概形纤维射影、几何整、约化、算术亏格一 | 奇异纤维唯一几何奇点、正规化 $\mathbb P^1$，并无尚待排除的可约／有限重纤维；无穷纤维是 $rD$ | [DG] §2.1 |
| 原泛动力曲线 $X/K$，$K=k(c)$；下降至原定义域 | 实际 Jacobian 为循环谱商 $E:\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0$，原域 $E$-torsor 身份准确，无隐藏核／不可分次数 | 不假设 $X(K)\ne\varnothing$；$z$ 谱曲线的亏格 $2r-1$ 不是 $X$ 的亏格；无核识别不是未知同源 | [DG] §2.2 |
| 原 $U$ 上约化域模型的完整临界概形 | $Z(dI_r)$ 长度四；原能级乘法特征多项式等于 $\delta(c,T)=c^4-\varepsilon c^3-8Tc^2+36\varepsilon Tc+16T^2-27\varepsilon^2T$，覆盖碰撞与非约化重数 | $\delta\ne0$ 正好是全部有限光滑层；不是只同零集。原底保持的局部模型与有限 Artin 块已识别 | [DG] §2.3 |
| 同一完整临界代数的纯 W 描述 | $k[z]/((T-z^2)^2-\varepsilon Tz)$，能级作用 $c=\varepsilon-z-z^3/T$；$W:v^2+cuv-\varepsilon Tv=u^3-Tu^2$，$\Delta_W=T^3\delta$ | 该已证域上奇异结构不是混合特征 $\alpha_a$ 的完整垂直厚度；不得把二者统称“奇异临界问题未做” | [DG] §2.3 |
| 原完整回返及全部合法有限域状态 | 一步在完整曲面／开放模型延为同构；回返泛非挠平移、各光滑有限层为平移；原 Hasse 上界与全部 ceiling 分箱含奇异状态 | 函数域非挠不意味着有限域无限轨道；奇异幺幂阶是 $p$，不是 $q$ | [DG] §2.4 |
| 准确回返点与原域完整闭纤维 | 在固定实际 torsor 作用后，$P=(0,\varepsilon T)$；任意底域中附“纤维有光滑原域点”条件的完整 $X_c\simeq W_\varepsilon(c,T)$ 将原回返送为加 $P$；有限域全部纤维自动满足该条件 | 原域条件不能被有限域特例删掉；局部选点只改平凡化，不改指定平移点 | [FP] §3.1；[FV2] §3 |
| 全有限域同族自治识别 | $\mathcal R_{s,t}\sim\mathcal A_{t^r}$，逐完整闭纤维同构拼为全合法有限点集双射，四末端线与奇点均覆盖 | 不是曲面双有理共轭、随能级有理变动的共轭，也不是泛 torsor 平凡化 | [FP] §3.1 |
| 完整循环清单与时间悬挂 | 指定点精确阶 $d_h$、光滑群大小 $N_h$ 给 $a_{T,q}(n)=\lvert\mathcal B_{T,q}\rvert\mathbf1_{n=1}+\sum_h(N_h/d_h)\mathbf1_{n=d_h}$；$d_h\ge4$；回归 $n$ 变完整一步 $rn$，循环数不乘 $r$；状态权重分母 $(q+1)^2$ | 节点指定元素与尖点加法元素已算，含 2、3；坏值按不同根加单点，不按重数加；清单仍以椭圆点数／点阶为输入，不给其统一闭式或跨素数极限分布 | [FP] §3.2–3.3 |
| 单位时间整数全次数层上同调 | $R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$ 上全 $n\ge0$：$R\Gamma(L_n)\simeq R[0]\oplus\bigoplus_{j=1}^n[R\xrightarrow{1-q^j}R]$，真实常数项保留；选择一次分裂后任意交换 $R$-代数逐项张量 | 含非平坦／非约化／非 Noetherian 基变换；分裂非典范，不是乘法或动力兼容的典范比较；普通 $H^0$ 基变换未被误称总同构 | [INT] §3.1 |
| 全圆分坏素参数的原 pencil 与扭子 | 原 $1,I_r$ 生成射影平坦 pencil，剩余是 $\operatorname{Pow}_N\circ f_m$；有限剩余纤维为小阶纤维 $N$ 倍；扭子过滤逐级分裂且全部初等因子已得，长度 $ae$、最少生成元 $N-1$、$\operatorname{Fitt}_0=(r)$ | $e=v_\pi(p)$；原线性系剩余像 $\kappa\langle1,J^N\rangle$ 与全部 $\kappa\langle1,J,\ldots,J^N\rangle$ 不同；幂态射不等于绝对 Frobenius | [INT] §3.2 |
| 所有素数／高度原整除微分 | $\alpha_a$ 在全部 $\mathcal U$ 正则，$\bar\alpha_a=H^\sigma dJ$，含四末端线；原 $dI_r$ 泛公共阶准确 $ae$，光滑闭能级 Hasse 身份已证 | 公共阶不是逐状态阶；除公共因子不是 $\pi$-饱和；公共阶恰等扭子长度不提供典范模同构 | [INT] §3.3；[FI] §3 |
| P30 首层全部素数、全部 tame $m$、完美剩余域 | 全部完整光滑有限层的原完整理想 $C_1=(\pi_1,\widetilde H)$；根重数 $e_h$ 给完成式 $(\pi_1,z^{e_h})$；实际 $\partial\nu=\mathrm{Fr}_*\kappa_J\ne0$ 在 $H^1(\mathcal O_X^p)$ | 第二方向已证明，不能重包装为未知；不是超奇异 $H^1(\mathcal O_X)$ 上可逆 Frobenius；无需 Hasse 根简单 | [V4-I] 首层定理；[IF] I1–I4 |
| P30 奇素全高层，有限剩余域 | 全图首 jet 因式分解；光滑层 $C_a^{+2}=(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1})$，含根重数完成式 | 共同双数商参数和完整时间 jet 必须匹配；不是自然塔嵌入，也不是 $C_a$ | [V4-I] 奇素定理；[IF] I3–I4 |
| P30 特征二全部奇 $m$、$a\ge2$ | 完美域全图 $\alpha_a^{[2]}=J^{\langle N-4\rangle}\alpha_2^{[2]}$；有限域光滑层 $C_a^{+2}=(\pi_a^2,j^{N-1}+\pi_a\widetilde Tj^{N-4},\pi_a j^{N-2})$ | 高度二为基准；首层商特征四与高层商特征二不可混同；实际桥是首切向类身份，不是高度一全形式替换 | [V4-I] 特征二定理；[IF] I5–I8 |
| 特征二高度二截断商与允许光滑超奇异状态 | 横向长度五且原基作用 $\pi_2\mapsto z^3/T$；首层超奇异 $v(\alpha)=1$，特征二 $a=2$ 也是 1；其余已述高层只 $\ge2$ | 五不是闭点总 Artin 长度或原完整商长度；$T$ 的单位可在允许扩张下正规化，非新形式模量；状态只取规定无分歧扩张 | [V4-I] 状态表；[IF] I9–I11 |
| 非单位时间的一阶及零时间全次数 | 实际一阶 $B[0]\oplus[B\xrightarrow{\tau(q-1)}B]$；零时间十环固定部 $\lceil n/2\rceil F$、去固定无基点；全 $n$ 的 $h^0=1+n(n+1)/2,h^1=n(n+1)/2,h^2=0$ | 这不是有限样本外推；曲面／层有效，原离散映射在零时间塌缩仍保留 | [NU] §2A |
| 非单位时间全次数实际呈示 | 原整数二项式矩阵 $J_n$ 给每个 $n\ge0$、任意 $B$-代数上的完整两项复形；与原八组评价矩阵只差可缩单位块；二阶完整整数分解亦已接受 | 全次数几何呈示已证，不等于全次数整数模规范形；冻结代码零阶接口不完整不撤销另证的数学零阶 | [NU] §2B、§3 |
| 非单位时间精确 $q=1,n=3$，此处 $R=\mathbb Z[\tau]$ | 真实混合块 $[R\xrightarrow{(\tau^2,2\tau)^t}R^2]$、不分裂扩张、首非零 $\operatorname{Fitt}_3H^1=\tau^5(\tau,2)$；特征非二／二扭子长度 5／6，但最底纤维维数相同 | 全标量整数对角呈示已被非主 Fitting 阻止；“首次三阶”仅在 $q=1,n\le3$ 已完整比较范围 | [NU] §2C |

## 3. 后续出口应从哪里开始扣除

以下“未供给／OPEN”仅指本轮实读组合中的尚缺新输入，不是全球数学开放性证书，也不预授其价值或足够论文容量。

| 拟接续对象 | 已有起点必须全部扣除 | 仍需另证／准确范围边界 |
|---|---|---|
| 高层原完整 $C_a$、全临界厚度 | 首层完整理想；每个高度的完整全图首 jet；两分支准确 $C_a^{+2}$、根重数及特征二混合项 | 缺 $\pi_a^2$ 以上实际系数、消去和兼容性；不能删掉 $+(\pi_a^2)$ 或假定 $\pi_a^2\in C_a$。见 [IF] §3、[V4-O] 462–468、[V4-T] 657–666 |
| 更高超奇异精确状态阶及额外分歧态 | 准确 0／1 阶和已证至少二；$v(dI)=a\varphi(p^a)+v(\alpha)$ 是直接标量推论 | 截断评价只给 $\min(v(C_a),2)$；需首个非零高阶系数与指定状态抵消控制。额外分歧态先指定扩张和赋值归一化，不能沿用原状态表 |
| 自然圆分塔比较 | 当前匹配完整时间 jet 的人为共同双数商；低层与高层各自原形式 | 自然嵌入把低层参数模高层平方送至零，不送至 $\epsilon$；需真实环／时间／形式兼容公式。全高度首 jet 不自动构成自然塔系统，见 [IF] §3 |
| 混合特征奇异能级的 $C_a$ 或其 jet | 原域所有有限奇异纤维、准确长度四 Artin 结构／能级作用、小特征分类；全图残余式及高层形式因式分解均已证 | 尚缺奇异层实际两方向基准理想与提升；$dJ$ 可能消失，光滑层的非零微分处处不消失与局部参数论证不能照搬。不能仅重新计算 $\delta$ 或 W 临界代数充作新结果 |
| 跨高层的更广剩余域量词 | 首层完美域、特征二形式完美域；高层实际几何理想按现稿有限域声明 | 这是当前定理声明／消费者前提的边界，不据此宣称所有无限完美域的结论未知；扩大量词须给明确的新论证而非“矩阵通用”一句 |
| 整数上同调的乘法／动力／微分比较或更精细约化 | 全次数非典范对角复形、任意派生基变换、全部扭子因子、平坦幂退化、全开放 Hasse 桥 | 当前未供给与乘法或动力兼容的典范模同构、稳定约化或一般晶体／形式群比较；同长度 $ae$ 不能充作比较态射，见 [FI] §3、[LA] §3 |
| 非单位时间全次数整模结构、全素数首现 | 全次数几何 jet 呈示与零时间维数、全二阶分解、$q=1$ 三阶非标量块都已接受；标量全对角化已有障碍 | 允许非标量块的全次数结构、全素数首现与实际连接映射仍未证；$p=2,3,5,7$ 有限 Smith 样本不能升级全称。W1–W3 新 Koszul 等仅作者证明，不由旧检查代签，见 [NU] §3 |
| 精确周期的进一步算术 | 指定点、各奇异群元素、闭纤维共轭、完整循环清单和全部时间权重 | 现有清单不是点阶统一闭式或跨素数分布；这两类更强结论未由清单证明。不能重新把求和、$d,N/d$、时间悬挂当独立新论文，见 [FP] §3、§5 |

## 4. 旧失败包和通用机制：不得复投或重复计功

| 保留对象 | 当前应继承的准确状态 | 对 P31 基线的约束 |
|---|---|---|
| 旧 qPI 完整 V1 的 T1–T4 | 数学接受；正式两席均仅新意未达门，旧失败保留；当时不含准确回返点／完整频数 | 后续 FP 已补全这些新数学，不可仍沿 V1 快照叫它们未证；也不回改 V1 原票，见 [FV1] §2–4、§7 |
| 旧 qPI 完整 V2 的 T1–T7 | 已含上述几何、原域 torsor、强临界式、准确回返点、全闭纤维与自治／全周期；两票完整合取因新意未同时达门而 FAIL | 不是只审增量或漏掉 T5–T7；没有新硬数学缺口。同包改题、重排、拆群论消费者或抽新票不产生新科学，见 [FV2] §1、§3、§5 |
| 整数完整 V1 的 C1–C3 及必要原对象链 | D/G/S/U 数学接受；两席均仅新意未过；完整原 Jacobian／闭 Hasse／末端责任已经读入 | 不能把旧源范围说明误报为缺对象证明，不以重组 C1–C3 为 P31，见 [FI] §1、§3、§6 |
| 非单位时间当前有界包 | 数学接受到指定范围；`BOUNDED_PROBE_CLOSED / NO_FORMAL_CANDIDATE_AT_CURRENT_SCOPE` | 非正式评分 FAIL，非全素数猜式反证；窄例实现不足与未证全素数结构必须分开，见 [NU] §1、§4 |
| P11 通用有限平移定理 | 对有限阿贝尔群 $C$、$X=\coprod_Kn_K(C/K)$、给定 $a$，周期 $d_K=[\langle a\rangle:\langle a\rangle\cap K]$、循环数 $[C:\langle a\rangle K]$ 已证 | 取 $C=\prod_hG_h$、投影核 $K_h$，再为奇点加 $C/C$，已经给整个模型识别后的循环求和；但不供应 qPI 原状态分解／真实群／指定点。见 [P11] 404–515、[PD] §3 |
| P18 的 Fitting／完成局部机制 | 复数 simple-exact-disjoint 标记 Hénon 的 $\rho_i=\lambda_i+bG_i$、Cartesian 微分与 $\operatorname{Fitt}_0$ 基变换、行列式限制和泛分量长度已证 | 一般 minor 基变换、单位消去、完成与长度规则扣除；P30 两系数是 $\operatorname{Fitt}_1(\Omega^1/\mathcal O\alpha)$，不是 P18 的单行列式，也不由 $G_i$ 的存在算出首系数。见 [P18]、[VD] §5.1 |
| P29 与已明确扣除的一般机制 | 差分累计／常数核／有支持界的数字选择可复用；原层 Bockstein、原有序谱迹和两个状态系数不是 Hénon 动力余核的改名 | 同时扣除已记录的 Hasse 迭代、Cartier／Frobenius 差商、标准局部消元及非单位时间 Harbourne／fat-jet／平移差分机制；不据“旧文未算该系数”授新意，见 [IL] §§2–5、[V4-I] 243–300、[NU] §4 |

P11/P18 的源由 [PD]、[VD] 所记录的接受入口定位；本轮所读源 SHA 与其接受身份相同，仅复核上述准确命题出口，不重开旧接受或扫描构建树。
一般机制属于基础来源，不能为了增加依赖条目虚构“P30 由 P11/P18 证明”的箭头；跨 Hénon/cat 与 qPI 的任何新桥只记 `ROUND2_CLUE`。
已读处置中的旧外部来源访问缺口不在本任务关闭；本件不联网，不把有限来源范围转成“全族尚未知”或“全球首创”。

## 5. 本次实读范围与 SHA-256

FULL 表示本执行者实际读完全文件；局部 SHA 绑定整文件，但不冒称全文。所列上游报告的作者／审查全文读取属于其原主控，不继承为本次本人读取。
另读 `docs/WORKFLOW.md` FULL、`BATCH_07_CONTEXT.md` 1–160 仅作流程与状态入口；关键词定位行不当作额外全文。

| ID／实际文件链接 | 本次读范围 | 本次实际 SHA-256 |
|---|---|---|
| [IF] | FULL 1–103 | `e5033d678872970d5018f007fa18c15e4cf0085980f26eb0ba0a616fdab4036d` |
| [IL] | FULL 1–121 | `bbcc282cad6a78da92500b21ee91ed892f1152bbfc339f2ad860468c27af593c` |
| [DG] | FULL 1–224 | `0bfbde8003d049d80523a2001d410dfa4f38ab2f14838d2dbbe4c1363f7155a7` |
| [FP] | FULL 1–167 | `9a70cd2dd9656689dfeb26a6890e35ab1bf5dd10a5eab28a38306578b2767fce` |
| [INT] | FULL 1–162 | `1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af` |
| [NU] | FULL 1–146 | `cf438f313d34c70f8dc7d775894524164460ba8a69d16c01c712a174a8200de0` |
| [LA] | FULL 1–108 | `cfb2f9e034716545fd22d9e7024d7b9b62d89350c3eecc97852870b17f094a52` |
| [V4-I] | FULL 1–300 | `9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e` |
| [V4-O] | 局部 450–468；另范围词定位 | `046f8cf808cc64de570605b316bcb5b0c6970f52492a585f97f97597ae2d74f5` |
| [V4-T] | 局部 653–666；另范围词定位 | `5cfee2a607e6ff1ab52192bb5c9b1a73cef6635c3e5dcfe26aa73fe1192b42a9` |
| [FV1] | 局部 38–88、118–132；另标题／边界定位 | `0452b7aa8f28107ae65f3fa840647806b50eab2502340d1c609a0ca6c545ce90` |
| [FV2] | 局部 1–21、54–89、102–116；另标题／边界定位 | `fb490d26321a3077b839d1e3505979150b7ad02bf59c6f5beba93a9977003584` |
| [FI] | 局部 1–21、48–72、110–123；另标题／边界定位 | `da3b7365053cbf7a1e4ab5817aac45ce9baee8f6162307ce25f0875b3cea6b6c` |
| [PD] | 局部 70–95、106–143；另 P11 定位 | `7216525bf1226d4d0512eb7ca0e7b94a8573a4c18520e27afa6f0fefaa28c65d` |
| [VD] | 局部 64–81、100–128、264–299；另 P11/P18 定位 | `03219910add96d998bb3636f1d77e830be688d8852b437da7c8d01be9f3e6499` |
| [P11] | 局部 390–518：相关完整定理与证明 | `2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958` |
| [P18] | 局部 188–251、507–615、940–980、1076–1128、1273–1295、1468–1494；另命题／限制定位 | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` |

[IF]: PAPER30_EXISTING_QPI_INTERFACE_INVENTORY_V1_20260909.md
[IL]: PAPER29_30_EXISTING_INTERFACE_LIMITS_V1_20260909.md
[DG]: PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md
[FP]: PAPER30_QPI_FULL_PERIOD_DISPOSITION_V1_20260909.md
[INT]: PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md
[NU]: PAPER30_QPI_NONUNIT_TAU_MATHEMATICS_AND_SCREEN_DISPOSITION_V1_20260909.md
[LA]: ../../papers/30-qpi-vertical-critical-ideals/notes/LOCAL_ACCEPTANCE_20260909.md
[V4-I]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/01-introduction.tex
[V4-O]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/07-odd-jets.tex
[V4-T]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/08-two-jets.tex
[FV1]: PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V1_20260908.md
[FV2]: PAPER30_QPI_FORMAL_CANDIDATE_DISPOSITION_V2_20260909.md
[FI]: PAPER30_QPI_INTEGRAL_FORMAL_CANDIDATE_DISPOSITION_V1_20260909.md
[PD]: PAPER30_QPI_POINT_PERIOD_PORTFOLIO_DELTA_V1_20260908.md
[VD]: PAPER30_QPI_VERTICAL_ALPHA_PORTFOLIO_DELTA_V1_20260909.md
[P11]: ../../papers/11-cat-equivariant-clock/paper/manuscript.tex
[P18]: ../../papers/18-marked-henon-scalar-boundary/paper/main.tex

## 6. 终态边界

唯一新增本文件；未改接受源、旧证明／旧票／锁、README、批次入口或其他索引，未读取旧 55／69 件共同包全文，未扫描旧构建树。
未编译、运行实验、联网、外传或建立 `papers/31*`。终态提交前全文自读并检查直接链接与 17 个输入 SHA；终态 SHA 随交付单独报告，不新增数学接受或候选分数。
