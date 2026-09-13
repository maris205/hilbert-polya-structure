# Paper29 下一候选：乘积剪切的多项式辛中心化子查新与可行性

日期：2026-09-05。性质：有界独立查新／作者侧可行性预检；不是正式
Route A/B 评价，不是独立数学验收，不是候选 PASS，不创建项目或科学锁。

## 结论

**建议：AUTHOR-PREFLIGHT STOP——淘汰其作为当前独立长文候选的定位。**

理由不是找到反例，也不是已有文献逐字包含全空间定理。准确判断是：
已知 Danielewski 自同构群结构使泛型约化曲面上的中心化子成为短的自由积
正规形推论；Cox 提升本身也有旧精确序列。后者不自动给出所有交换辛映射的
环面正规化，但已完整阅读的实际 ambient 推导用几个紧凑的引理补上此步。
扣除先前已获得的第一积分输入后，现有差额不足以诚实支撑本批次要求的
22–30 页实质性独立论文。

这不否认完整分类可能是正确、有用的局部命题。它否定的是把“数学正确”
自动兑换成“已通过选题／创新性／篇幅门槛”。本报告不建议追加逆转子、
全共轭分类或更广势函数来人为扩大当前候选。

## 1. 输入、边界与三个待查声明

令 $r\ge3$、互素整数 $2\le m<n$，并写
$$
Q=\prod_iq_i,\qquad P=\prod_ip_i,\qquad
S(q,p)=(q_i,p_i+mQ^m/q_i)_i,
$$
$$
T(q,p)=(q_i+nP^n/p_i,p_i)_i,
\qquad F=TS,
\qquad\omega=\sum_i dq_i\wedge dp_i.
$$
显示的商都是多项式。目标是对每个 $N\ge1$ 分类
$C_{\mathrm{SpPoly}}(F^N)$，预期答案为
$$
(\mathcal T\rtimes S_r)\times\langle F\rangle,
\qquad
\mathcal T=\{D_a:(q_i,p_i)\mapsto(a_iq_i,a_i^{-1}p_i),\ \prod_i a_i=1\}.
$$

实际阅读的本地输入：

- [保留的第一积分证明](PAPER29_CANDIDATE_PROOF_V1_20260905.md)：使用其全局固定环
  $\mathbb C[q,p]^{F^N}=\mathbb C[c_1,\ldots,c_{r-1}]$，
  $c_i=q_ip_i-q_rp_r$；不把已获得输入重新计入新差额。
- [实际 ambient 引理](PAPER29_CENTRALIZER_AMBIENT_LEMMAS_20260905.md)：完整阅读；
  本报告据此评价实际推导体量，不猜测它可能很长。
- 本地同名近邻 Paper10 的前三页：研究有限模上的 cat 矩阵中心化子及粗商，
  不是本题多项式辛自同构的分类，不能据标题视为直接重复。

| 声明 | 最接近的已知内容 | 本次判断 |
|---|---|---|
| A. 全空间中心化子恰为环面、同步置换与迭代 | Danielewski 群结构与 Cox 提升 | 未发现完全同式的已发表命题；实际剩余差额紧凑，独立长文价值不足 |
| B. 所有 $N$ 的中心化子相同，互素条件消灭额外有限伸缩 | 循环约化字的中心化子、有限对角对称与根 | LOW：正规形和两条幂条件的直接应用 |
| C. 从固定环恢复环面并排除非线性基底作用／全翻转／非恒定提升核 | 局部有限导子、环面权重与 Cox 分次 | 可辨认的 ambient 差额，但实际是数个短引理；不宣称历史首次 |

## 2. 一手来源及精确适用边界

以下链接直接指向作者预印本、作者机构或正式出版页面；搜索聚合与自动摘要
仅用于发现，不承担数学结论。日期用作者版本／正式出版日期，未将网页的
“最近抓取”当作发表时间。

| 来源 | 阅读位置与有效结论 | 与当前候选的关系 |
|---|---|---|
| Leuenberger–Regeta, *Automorphism Groups of Danielewski Surfaces*, arXiv:1710.06045 (2017；预印本标题) | 引言、Remark 2、Proposition 3(a)–(d)：光滑 $QP=h(x)$、$\deg h\ge3$ 的恒等分支为 $(U_Q*U_P)\rtimes\mathbb G_m$；一般根集时再添交换 $Q,P$ 的阶二分支 | 最直接结构碰撞；文中把相关群结构归于 Makar-Limanov 1990。 [作者全文](https://arxiv.org/html/1710.06045v1) |
| Arzhantsev–Gaifullin, *Cox rings, semigroups and automorphisms of affine algebraic varieties*, Sb. Math. 201:1 (2010), 1–21 | §5, Theorem 5.1：$1\to N\to\widetilde{\mathrm{Aut}}(R(X))\to\mathrm{Aut}(X)\to1$；波浪号限于正规化分次的自同构 | 给出提升及核，不给任意 ambient 交换元自动正规化环面。 [作者全文](https://arxiv.org/html/0810.1148v1)、[出版记录](https://www.mathnet.ru/eng/sm7370) |
| Gómez–Meiss, *Reversors and symmetries for polynomial automorphisms of the complex plane*, Nonlinearity 17 (2004), 975–1000 | §3 Theorem 7、Corollary 9：Hénon 正规形的对称由循环约化根及有限对角部分控制 | “迭代根＋有限伸缩”是旧的结构范式；不是本题 $2r$ 维全空间定理。 [作者机构 PDF](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf) |
| Bisi, *On commuting polynomial automorphisms of $\mathbb C^k$, $k\ge3$*, Math. Z. 258 (2008), 875–891 | 官方摘要及可检索正文 Definition 1.1、Main Lemma 1.3：主要严格分类针对正则 $\mathbb C^3$ 自同构，高维有附加假设问题 | 不能套用“所有高维多项式自同构中心化子已知”。 [机构记录](https://sfera.unife.it/handle/11392/1383640)、[作者 PDF](https://docente.unife.it/cinzia.bisi/MZ.pdf) |
| Gaifullin, *Automorphisms of Danielewski varieties*, arXiv:1709.09237 (2017), Journal of Algebra 573 (2021), 364–392 | §7 定义及 Theorem 7.15 的主类含 $xy_1^{k_1}\cdots y_s^{k_s}-P(y,z)$，$k_i\ge2$；自同构由典范群与大幺幂群描述 | 不是随意可替换为本题 $QP=\prod(x+c_i)$ 或整个辛仿射空间的结论。 [作者全文](https://arxiv.org/html/1709.09237v1) |
| Abboud, *Intersection of orbits of loxodromic automorphisms of affine surfaces*, arXiv:2409.07826 (2024) | 摘要与引言：两个 loxodromic 自同构的轨道无限相交时共有迭代 | 轨道无限相交不是单纯交换关系自动满足的条件；不能拿它直接计算本中心化子。 [作者全文](https://arxiv.org/html/2409.07826v1) |
| Arzhantsev–Zaidenberg, *Borel subgroups of the automorphism groups of affine toric surfaces*, arXiv:2507.09679 (2025) | §2–3 的树作用结构、Proposition 2.6；§6 有有限对角元素中心化子的显式算式 | 近期文献再次表明轴、椭圆核、有限对称须分别控制；不是当前高维辛结果。 [作者全文](https://arxiv.org/html/2507.09679v1) |
| Ahouita–Baltazar–El Kahoui–Gaifullin, *The isotropy group of a derivation on a Danielewski-type algebra*, arXiv:2510.07059v2 (2025-10-11) | Theorem 8：指定 Danielewski 型代数上的非局部幂零导子，其稳定子是维数至多三的代数群 | 导子的稳定子不同于正熵离散映射的中心化子；也有 $\deg c\ge2$ 的类限制。 [作者全文](https://arxiv.org/html/2510.07059v2) |
| Baltazar, *Simple derivations and isotropy on Danielewski-type algebras*, arXiv:2606.16810 (2026-06-15) | 摘要、引言与 §2：一般参数下 simple derivation 的稳定子平凡，但有特殊反例 | 最近六个月的真实近邻；不是有 $r-1$ 个多项式第一积分的离散辛映射。 [作者全文](https://arxiv.org/html/2606.16810v1) |
| Selin, *Automorphism groups of non-normal affine toric surfaces*, arXiv:2606.14234v2 (2026-07-16) | 摘要：非正规 toric 曲面的自同构恒等分支不总由作用环面及根子群生成 | 说明不能无条件泛化 toric 生成元论；本题正规商及泛型光滑曲面不在其反例类。 [作者摘要](https://arxiv.org/abs/2606.14234) |

另核对 Silverman, arXiv:2410.10598v2 的作者摘要：其标题 *Automorphism Groups
of Commuting Polynomial Maps of the Affine Plane* 实际研究 Lie 代数相关 folding
maps 的仿射对称，映射拓扑次数为 $n^2$，不是多项式自同构中心化子的全分类。
[作者摘要](https://arxiv.org/abs/2410.10598)

## 3. 有限因子与显然反例检查

### 3.1 已确证的显然子群及对角因子

同步置换与 $\mathcal T$ 分别保持 $Q,P$，因此与每个剪切以及 $F^N$ 交换。
不应把同步置换写成与环面直积：它置换环面的 $a_i$，所以是半直积。
$F$ 则与二者交换。

令 $D_a$ 是任意常系数对角辛变换，$A=\prod_i a_i$，不先假设 $A=1$。
共轭把两个剪切系数分别乘以 $A^{-m}$ 与 $A^n$。对 $F^N$ 的最低非线性
齐次项比较先给 $A^m=1$。此时 $D_a$ 已与 $S$ 交换，比较两字
$(T_{A^n}S)^N$ 与 $(TS)^N$ 在次数 $rn-1$ 的首次 $T$ 项，差为
$N(A^n-1)$ 倍该非零齐次项；所有只来自 $S$ 的项在两边相同。
特征零遂给 $A^n=1$。反向包含显然，故
$$
C_{\mathrm{SpPoly}}(F^N)\cap\{\text{常系数对角辛变换}\}
=\{D_a:A^{\gcd(m,n)}=1\}.
$$
因此当前互素假设下，这类额外根单位因子确实没有遗漏。若取消互素条件，
单写 $A=1$ 就会漏掉有限分支；该点不是一个需要长期研究的新现象。

### 3.2 泛型曲面上的短正规形计算

令 $K=\mathbb C(c_1,\ldots,c_{r-1})$，$c_r=0$，
$h(x)=\prod_i(x+c_i)$。约化映射是 $w=\tau\sigma$，其中两类剪切对 $x$
的增量分别为 $mQ^m$、$nP^n$。一般根集没有非平凡仿射自对称。

利用上述既有群结构，在 $U_Q*U_P$ 中 $w$ 是长度二的循环约化字，不是真幂；
它的非零次幂的中心化子由 $w$ 生成。加入约化环面后，写候选交换元为 $u a$。
自由积共轭正规形要求 $a w^N a^{-1}$ 与 $w^N$ 的循环 syllable 匹配；
同类因子的匹配迫使 $a^m=a^n=1$。互素时 $a=1$，又回到前一个自由积
中心化子计算。交换 $Q,P$ 的分支若出现，循环移位后的两种单项式次数必须
匹配为 $m=n$，与本题相反。

这是从已知结构出发的本次短推导，不是文献中发现了本题全文定理。
正式数学稿仍应写明从复数版本到 $\overline K$ 的特征零版本及下降步骤，
而不能只引用一个没有说明基域的“Bass–Serre 定理”。但这些是可明确列出的
正规形技术核对，不构成有理由期待的大段新理论。

### 3.3 未发现的东西不等于已经证明不存在

本次未发现当前互素、非等次数设定下的显然反例。也不能仅凭未搜到反例，
宣布所有多项式辛交换元都已分类。尤其必须分别排除：非线性基底变换、
不正规化环面的交换元、动量依赖的有理环面乘子，以及只在稠密开集成立的提升。
实际 ambient 文件正面处理了前三种相关问题，并用全空间 UFD 处理最后的核，
不诉诸错误的“所有碰撞纤维都是环面 torsor”。

## 4. 实际 ambient 差额：存在，但短

下面是对已经写出的证明的体量分析，不是额外补写的论文计划。

1. 固定环使 $G^*c_i=\phi_i(c)$。辛性使 $D_{\phi_i}$ 与对角 Euler 型
   $D_{c_i}$ 共轭，故局部有限；而
   $D_{\phi_i}^k(q_j)=(\partial_j\phi_i)^kq_j$。
   若偏导非常数，这些多项式线性无关，直接矛盾。因而 $\phi$ 仿射。
2. 导子张成的 Lie 代数被保持，故 $G$ 正规化 $\mathcal T$。
   环面共同不动点只有原点，于是 $G(0)=0$，仿射平移项消失。
3. 切空间权重是 $\{\pm e_1,\ldots,\pm e_{r-1},\pm\sum e_i\}$；
   唯一 simplex 关系把可能作用压缩为同步置换或全翻转。
4. $rm-1<rn-1$ 的最低非线性项只有动量分量，故全翻转不能与之交换。
   去掉置换后便同时固定基底、与环面交换。
5. 若商上作用恒等，则 $G^*q_iG^*p_i=q_ip_i$。
   多项式 UFD 中不可约因子只可能为常数倍的 $q_i,p_i$；权重排除交换，
   保持 $Q$ 再给乘积一。因此提升核恰为常系数 $\mathcal T$。

这五步把既有固定环和既有曲面中心化子接起来，确实比直接引用 Cox 定理多做了
实质性检查；但每一步现在都有短而透明的实际理由，不能再用“高维提升可能困难”
为其虚增篇幅或价值。Cox 定理在此主要提供背景和核结构的对照，甚至不是完成
上述 UFD 版本提升所必需的重型工具。

保守篇幅判断：新增 ambient 部分按普通数学排版是数页，约化字及下降又是
很短的补充；即使加上必要背景与例子，也没有当前证据支持 22–30 页的独立
实质内容。这里不是编译测量，更不是允许用重复第一积分证明、重述自由积教材、
放大版式或附加未授权问题补足页数。

## 5. 检索可复核记录

使用 `research-lit` 与 `novelty-check`：按声明拆分、每项至少三个不同查询，
再做 2024–2026 与最近六个月的查询。下表列出实际执行的代表性原查询；
日期窗口为 2026-03-05 至 2026-09-05。无 Zotero、Obsidian 或指定 Codex MCP
审查工具；没有伪造跨模型审查。未找到可用 `arxiv_fetch.py`，按技能退回公开
arXiv 作者页和全文；未下载文献、未发外信、未开新项目。

| 组 | 实际查询 |
|---|---|
| A1 | `"polynomial automorphism" "centralizer" "torus" "symplectic"` |
| A2 | `"polynomial symplectomorphisms" normalizer torus moment map` |
| A3 | `"centralizers" "Hamiltonian" "polynomial automorphisms" 2024 2025 2026` |
| B1 | `"centralizer" "Danielewski" automorphisms` |
| B2 | `"centralizer" "affine surfaces" loxodromic` |
| B3 | `"Danielewski" automorphism centralizers roots Bass Serre` |
| C1 | `"Cox rings" "automorphisms" "lifting" affine variety Arzhantsev Gaifullin` |
| C2 | `"xy" "Cox ring" "Danielewski"` |
| C3 | `"Cox" "lift" "centralizers" automorphisms` |
| 近期 A | `"symplectic polynomial automorphism" centralizer torus 2024 2025 2026` |
| 近期 B | `"Danielewski" "commuting automorphisms" 2024 2025 2026` |
| 近期 C | `"Cox lift" "symplectic" automorphisms 2024 2025 2026` |
| 六个月 A | `"polynomial automorphism" "centralizer" after:2026-03-05 before:2026-09-06` |
| 六个月 B | `"centralizer" "Danielewski" after:2026-03-05 before:2026-09-06` |
| 六个月 C | `"centralizer" "Cox" automorphism after:2026-03-05 before:2026-09-06` |

另对具体命中题名做作者页核查，涵盖 2026-06 的 Baltazar 与 Selin 预印本。
机器学习会议目录与当前纯代数动力系统问题无实质联系，不把空查这些目录当作
额外查新证据。公开检索可能漏掉未索引论文，因此本报告不颁发唯一性或历史
首次保证，也不提供虚假的定量 novelty 分数。

## 6. 交付决定

本候选的合理保留方式是本地短结构记录；当前独立长文定位应停止。
中心化子最终精确等式尚须独立核对泛型曲面正规形及下降，不因本查新文件而
自动转为数学 PASS。即便这些核对全部通过，也不改变本次作者侧的长文预选
停止建议。不得据此跳到 Paper30，亦不得将前一取消族重新打开扩写。
