# Paper31：Manin 局部阶与准确接触重数的来源审计 V1

日期：2026-09-12 UTC；来源席：`/root/p31_manin_contact_order_sources_v1`。
状态：`BOUNDED_PRIMARY_SOURCE_AUDIT_COMPLETE`；`route_applicability: NOT_APPLICABLE`。
不授数学 PASS、正式候选分数或新颖性保证；不改变旧接受、失败及 P31 准入要求。

## 1. 结论与审计对象

已有一手来源确实处理高接触阶，不能将“从支持推进到重数”本身描述成无人研究。
最接近的直接先例是 UV Remark 2.4 的含交数下界、Ulmer 的 Cartier 像条件，
以及 Naskręcki 的初始交数到其他倍点交数的形式群传播。
本次实际读取没有得到一个可直接引用的定理，统一从原指定截面的 Manin 值恢复所有准确交数。
这是有界覆盖判断；“未找到直接定理”不等于已经证明新颖或有长文中心。

原对象固定为

$$
W_h:v^2+huv-Tv=u^3-Tu^2,
\quad P=(0,T),\quad i_n=(nP.O)_{h_*}.
$$

交数沿原基参数 $z=h-h_*$；不通过分歧重标掩盖阶的变化。
既有素域充要支持判据和固定理想已接受，本件不重复审查这两项。
特别不将 $N_p(h_*)=0$、$\operatorname{ord}N_p$、$i_n$ 或某个最优局部接触量混为一物。

## 2. 一手来源及准确竞争层次

| 来源 | 已直接覆盖 | 本问题仍须保留的限制 |
|---|---|---|
| [Ulmer–Voloch，arXiv:2508.06680v1][UV]，预印本 | §2 Proposition 2.3 的消去、Remark 2.4 的含 $i_n$ 下界；§3 更一般的局部接触 | 正特征给下界而非统一等式；Igusa 例子不是原 qPI |
| [Voloch 1990][V90]，Compositio 74，247–258 | §3 Theorem 3.1 核为 $pE(K)$，§4 形式群局部分析，§6 Tate 表达式 | 有普通泛曲线、Hasse 规范和 $p$-挠点假设；未逐式覆盖原族所有接触阶 |
| [Ulmer 1991 作者版][U91]，对应 Duke Math. J. 62，237–265 | §5 Cartier 像与完整局部 Selmer 描述 | 作者重排版47页，页号不等于期刊页号；不是指定截面阶分类 |
| [Broumas 1997][B97]，Compositio 107，125–141 | §4 显式同态与规范，§4.6 明确处理 $p>3$ | 一般闭式公式及消去属于来源，不等于原 $N_p$ 根重数定理 |
| [Naskręcki 2016][N16]，NYJM 22，989–1020 | §8 Lemma 8.2 的准确倍点赋值传播 | 初始出现指标及初始交数仍作输入；泛 ordinary 不代表处处 ordinary 特化 |

来源层次为“直接机制／一般传播”，不是发现这些作者已经研究同一带标记 $W_h,P$。
UV 的参考文献还指向 Manin 1963、Ulmer–Urzúa 2021 及经典椭圆曲面资料；
本次没有追加这些全文，亦不借其题名扩大覆盖面。

## 3. UV 实际论证中已经存在什么

§2取代数闭常数域、$p>3$、$j\notin K^p$；§3另限定 Igusa 普遍族。
在其半稳定设置、$p\nmid n$、$i=(nP.O)_t>0$ 下，Remark 2.4 已给

$$
\operatorname{ord}_t\nu(P)\ge
\min\{p(i-1)-\operatorname{ord}_tD,
       i-1+\operatorname{ord}_tA\}.
$$

Proposition 2.3 的好约化证明先作极项消去，再估计微分项；它没有把所有不等号换成等号。
§3 Proposition 3.3 按 ordinary／supersingular 及 $i<p$ 分支估计。
Definition 3.4 定义 $I(P,t)=\sup_R(pR,P)_t$，随后仅说明 $I\ge i_n$，并未给严格不等式实例。
因此，UV 是准确相关先例，但“最优局部 $p$-可除逼近”仍不是“指定扭截面接触”。

据此，后继原证明若要主张 equality，需要逐项找出非零首系数，而不是再次引用这一 min 下界。
若主张 $2\le i<p$，至少仍须指定 $A$、$\lambda$ 的局部阶以及模型单位规范。
若主张覆盖 $p\mid i$，还须处理导数无法看到 $z^p$ 的现象。
这些是准确等式的检查事项，不是本报告替主控证明了任何新公式。

## 4. Cartier 条件：有真实阶限制，但须先核对规范

Ulmer §5 的设置为有限域上一元函数域或其完备化，泛 ordinary，且 $E^{(p)}$ 有指定 $K$-有理 $p$-阶点。
令 $\delta=dq/q\ne0$、$df=\theta(f)\delta$，给出

$$
K^0=\operatorname{Im}\theta
=\{f:C(f\delta)=0\},\qquad H^1(K,E[p])\simeq K^0.
$$

其 Theorem 5.5 在普通好约化且 $v(\delta)=0$ 时给局部像 $R_v\cap K_v^0$。
这里的 $f$ 是来源的规范化 Kummer 坐标，不能不经辨识就替换成项目 $\mu$。
[2019 勘误][UERR]修正常值曲线 Proposition 3.3(a) 的遗漏项；未声称修改 §5。

以下是标准局部代数推论，不是该文逐字陈述的原 qPI 定理：
在完美剩余域与一致参数 $z$ 下，若 $C(f\delta)=0$，
则微分 $f\delta$ 的 Laurent 展开中指数 $\equiv-1\pmod p$ 的系数为零。
故非零 $f\delta$ 的首阶不能属于该同余类；这不规定一个唯一允许同余类。
当 $\delta=a(z)dz$ 且 $a$ 为单位，$f=z/a(z)$ 就显示 Cartier 条件允许一阶零。
因此，“Cartier 条件迫使所有零点简单”及“排除一阶零”均不能从上述来源推出。

对项目的规范转换，应明确检查下面的接口，而不是隐去它：
取 $\alpha^{p-1}=A$ 并将模型缩放到 Hasse 不变量1，则权重给出

$$
\mu_{\rm can}=\alpha^{-p}\mu,
\qquad \lambda_{\rm can}=\alpha^2\lambda.
$$

所以匹配 Ulmer 坐标时应跟踪 $\alpha^{2-p}\mu\lambda$，不是随意宣称 $C(\mu\lambda)=0$。
ordinary 点可以通过单位根的不分歧局部扩张处理 $\alpha$；supersingular 点则不可沿用此单位论证。
这些缩放及其与所选下降同态的一致性须由实际数学稿核对；本件不授予其项目应用数学接受。
即使单位情形导出 $\operatorname{ord}\mu\not\equiv-1\pmod p$，也没有因此求出 $i_n$。
另须保留 $N_p=(8h-9)^p\mu(P)$ 的乘子；在 $8h_*-9=0$ 处不能直接把二者的阶等同。

## 5. $p$ 次幂失明与形式群传播

Voloch Theorem 3.1 适用于所述一元函数域或幂级数域，并使 $pE(K)$ 成为核。
因此，$\mu(Q+pR)=\mu(Q)$ 是上游机制；加入局部 $p$ 倍点不改变 Manin 值。
把某个同态陪集代表的接触阶当成同态值本身的完整信息，原则上需要额外约束。
此处不从一般局部代表的可变性推断原固定 $P=(0,T)$ 已出现反例。

Naskręcki Lemma 8.2 令 $m=\min\{r:\operatorname{ord}_vD_{rP}>0\}$、
$h_v=\operatorname{ord}_vH(E,v)$；泛 ordinary 且 $h_v\le p-1$ 时，若 $m\mid n$，

$$
\operatorname{ord}_vD_{nP}
=p^e\operatorname{ord}_vD_{mP}
+\frac{p^e-1}{p-1}h_v,
\qquad e=v_p(n/m).
$$

$m\nmid n$ 时为零；其证明也明给 prime-to-$p$ 形式群乘法保持阶。
这必须扣除为准确传播先例，但它不提供原 $m$ 和 $i_m$ 的算术取值。
来源还讨论 $h_v\ge p$ 的分支；本报告不把该分支中依赖点的修正项包装成已知初始阶。
特别，“增加 $p$ 倍情形”若只迭代上述已知公式，不能自动成为新的原族理论中心。

## 6. 普通、超奇异与坏节点不可共用同一读阶规则

| 局部情形 | 必须分清的机制 | 对后继准确公式的要求 |
|---|---|---|
| 好 ordinary，$A,\lambda$ 单位 | 导数首项及 Artin–Schreier 的线性项可能给主项 | 实际验证接触首系数及其不消去，不能只看零值 |
| $p\mid i$ | $d(z^i)=0$；同态又杀局部 $p$ 倍点 | 需要原截面额外 jet／算术约束，不能由微分阶盲目反推 |
| 好 supersingular | $A$ 非单位，形式 Verschiebung 各项竞争 | 必须追踪 $v(A)$、$v(\lambda)$ 及可能分歧，不能套普通单位式 |
| 乘法坏约化 | Tate 参数与对数微分；组件群先决定何时进单位邻域 | 区分 $I_m$ 的 $p\mid m$ 与 $p\nmid m$；节点嵌入理想不替代标量交数 |

Voloch §6 在 Tate 曲线上明给 $\mu(u)=\wp(q\,du/(u\,dq))$，
并讨论特征零 Manin 映射约化后与 $\mu$ 的导数关系；这不是新的原族微分方程。
在 Tate 参数的规范下，$p\nmid m$ 的 $I_m$ 点满足 $\lambda=dq/q$ 有一阶极点。
因此，即便能够读出准确阶，也要先辨清读的是 $\mu$ 还是乘上微分的 $\nu$。
半稳定固定理想 $\tau^{i_n}(\xi,\eta)$ 已接受，但未知标量 $i_n$ 不由节点坐标自动消去。

## 7. 检索边界、实际读取与可追溯性

本席 FULL：AGENTS.md、WORKFLOW.md、research-lit 技能及以下三个本地输入。
BATCH 仅读取当前入口1–20行；不加载历史账本全文，不扫描论文 PDF 库。

| 输入文件 | 行数／本人读取 | SHA-256 |
|---|---|---|
| [数学接受][D] | 176／FULL | `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a` |
| [增量批评][CR] | 101／FULL | `cb94ad908083fda9418cb681985c079d5cdc09636944569c7bdf8e0b9d3a8943` |
| [旧来源边界][S] | 85／FULL | `5004d141f21699d01499ef428c585a9eda364fba4ecf4d50fe4c17160108d33c` |

外文本人：UV 官方 HTML §2 FULL、§3 FULL，并核对参考文献；不称全篇 FULL。
Voloch：pp.247–254 的可提取正文及 §6 pp.257–258；p.257 另经内存渲染逐式视觉核定，前段扫描漏式不报逐式 FULL。
Ulmer：作者重排版 §5 pp.18–25 全节及完整 Theorem 5.5 proof；一页2019勘误 FULL。
Broumas：pp.125–127前段、pp.131–137所列 §4.2–4.6／§5前段；公式提取符号不稳处只消费可核部分，不称全篇 FULL。
Naskręcki：期刊网页书目信息，pp.1003–1005（§8开头、Lemmas8.1–8.2完整陈述证明、Definition8.3）。
UV 页头2025-08-08与正文2026-08-24日期并存，保持该差异，不补造刊物状态。
Ulmer 作者索引明确 local version 可能与印刷版略异，本报告使用作者页码并注明这一身份。

只读辅助 `/ulmer_cartier_readonly` 另核定 Ulmer §§2–3、§5 与勘误，无文件写入、无额外搜索。
本席没有继承其 §§2–3 为本人 FULL；关键 §5 已本人复读。辅助不计独立数学票。
Zotero／Obsidian 未配置；arxiv_fetch.py 定向查找未得，按技能回退官方网页／arXiv 定向查询。
公开 PDF 只经网页解析或内存管道阅读；未保存论文库存。网页 screenshot 超时不计成功视觉阅读。

实际11条查询（打开已知 URL 不另计；不追加原有限表）：

1. `site:arxiv.org "Manin" "tangencies" "multiplicities"`
2. `"Voloch" "Cartier" "p-descent" local`
3. `"QRT" "contact" "multiplicities" elliptic`
4. `Douglas Ulmer "p-descent in characteristic p" pdf`
5. `"elliptic divisibility sequences" "ordinary" "valuation" "characteristic" Naskrecki`
6. `"q-Painlevé I" "Manin" contact`
7. `"Manin" "Cartier" "zeroes" characteristic`
8. `"QRT" "elliptic" "multiplicities" "characteristic"`
9. `"Effective p-descent" "differential" "image"`
10. `"\"qPI\"" "\"Manin\"" elliptic`
11. `site:arxiv.org "tangencies" "Manin" "2026"`

部分 QRT／qPI 查询返回异义词及无关结果，未作为科学证据；当代核查以实际 UV 官方正文为准。
没有发现足以核定为同一 $W_h,P$ 准确接触阶分类的直接命中；不据此断言不存在。
Duistermaat 周期纤维与其他 QRT 文献仍保留既有候选来源身份，本轮未读正文，不重新计功。
本轮不另选跨族例子，不将 Igusa 或 Legendre 接触移植为原 qPI 新结论。

## 8. 对下一动作的有限建议

继续准确首项证明是合理的有界研究动作；但来源扣除应先固定，而不是等结果后再定义“新”。
最值得区分的是：普通低阶等式属于何种标准局部后果，以及原指定截面另供应了什么可确定的新算术事实。
若最终只得到一般消去、Cartier 同余限制或已知形式群传播，本报告不将其升级成新长文中心。
若得到原截面实际排除不可见 $p$ 次幂、确定初始接触阶或另一非标准输出，应按实际断言另评，不预判其真伪或价值。
仅新增本件；未改索引、锁、论文、源库、旧报告或接受记录。无编译、GPU、外发、上传或付费操作。

[D]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[CR]: PAPER31_QPI_MANIN_INTERFACE_INCREMENT_CRITIQUE_V1_20260912.md
[S]: PAPER31_QPI_MANIN_PRIMEFIELD_SOURCE_BOUNDARY_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1#S2
[V90]: https://www.numdam.org/article/CM_1990__74_3_247_0.pdf
[U91]: https://dlulmer.github.io/research/papers/1991.pdf
[UERR]: https://dlulmer.github.io/research/papers/1991-correction.pdf
[B97]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/95814903A024FCB1B2C13CA8778759DA/S0010437X97000365a.pdf/effective-p-descent.pdf
[N16]: https://nyjm.albany.edu/j/2016/22-46v.pdf
