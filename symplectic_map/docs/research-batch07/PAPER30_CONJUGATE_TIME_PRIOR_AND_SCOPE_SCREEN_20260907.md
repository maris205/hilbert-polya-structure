# Paper30：首失正时间面积律的一手预核与作者范围处置

日期：2026-09-07。作者范围筛选，不是独立候选四门评分。
输入为[证明 V1](PAPER30_CONJUGATE_TIME_SCALING_PROOF_V1_20260907.md)。
采用 research-lit 的一手内容核对与结论分层；证明整理采用 proof-writer。
不使用 Route A/B，不建立论文项目，不申请或沿用容量实测例外。

## 1. 结论

一手预核：`PARTIAL_MATCH / GLOBAL_NOVELTY_UNCERTAIN`。
作者范围：`AUTHOR_SCOPE_NOT_SELECTED`。

当前完整证明有一个清楚的实际映射结论：正弦标准映射的首次 Dirichlet Hessian
失去正定时间，在固定 $c/\sqrt\varepsilon$ 步内的全环面面积为
$\sqrt\varepsilon A(c)+o(\sqrt\varepsilon)$。证明还描述极限分布的阈值、
起始系数和极限总质量。它不是只在预选小邻域中取连续极限。

但是，扣除生成函数/Jacobi 字典、离散化继承共轭行为的观念、Euler 有限时
$C^1$ 收敛、摆的能量与周期公式、Sturm/隐函数/解析零集工具后，非重复证明
仍属一个紧凑包。作者自然正文估计为 **9／12／16 页（低／中心／高）**。
三档均低于锁定的22–30页，因此本轮不进入正式双独立候选评价，不试写测页，
不把未来一般势、长时间极限或高阶误差承诺计入当前内容。
这不是新意已获认证，也不是伪造的正式四门 FAIL。

## 2. 已读一手来源及最强扣除

### 2.1 Bialy–MacKay：同类标准映射、变分框架与离散化观念

M. L. Bialy, R. S. MacKay，*Symplectic twist maps without conjugate points*。
实际读[作者 arXiv:math/0309470v1 全文](https://arxiv.org/pdf/math/0309470)
的 §1–4（正文1–11页），不冒称已读期刊定稿。

Example 1 包含 Frenkel–Kontorova 生成函数与广义标准映射；§2 给出
Dirichlet 二次变分和 Jacobi 递推。Theorem 3 是非恒定势必有共轭点的刚性
结论。尤其 §4 问题5已明确提出跨整数时间的扩展共轭定义，并说明连续轨道
离散化时继承共轭点的意义。[作者全文，Example 1、§2、§4(5)](https://arxiv.org/pdf/math/0309470)

**本次对象比较的推断：** 不能将 Hessian 字典、整数间失正的观念或连续
极限继承本身宣称新机制。已读正文没有给出本题的固定时间尺度全环面面积律、
正弦分布函数或起始系数；这只是对该文本的未匹配，不是全领域无先例证明。

还有一项重要定义区别：本文证明 V1 的时间是第一次非正定的整数端点，
不是第一次某个整数端点恰有非零 Jacobi 场为零。该区别已在 V1 明示，不能
用新名称遮盖两者，也不能将本结果不经说明地贴到旧严格整数共轭定义上。

### 2.2 Florio–Le Calvez：正测度与可积性是已有定性结果

A. Florio, P. Le Calvez，*Torsion of instability zones for conservative twist
maps on the annulus*，实际读2020-06-08
[作者公开全文](https://annafloriomath.wordpress.com/wp-content/uploads/2020/06/florio-lecalvez-final-8-6.pdf)
的定义1.2、命题1.1、定理1.1–1.2、推论1.1–1.2与命题2.1（第3–5页），
并核对§4的可积性结论末段；没有声称全文每个证明都重新验证。

该文证明合适不稳定区域内非零渐近 torsion 点具有正测度，并给出无共轭点
与 $C^0$ 可积性的几何刻画；问题1.1还区分正测度与满测度。
[作者全文，第3–4页](https://annafloriomath.wordpress.com/wp-content/uploads/2020/06/florio-lecalvez-final-8-6.pdf)

**本次对象比较的推断：** 存在共轭/过共轭行为、非零扭转正测度及可积性
判据已被强覆盖，不能计为本题新贡献。所读定理没有给出本题的小参数有限时
面积函数；反过来，V1 也没有证明固定离散参数下的全时间面积或回答满测度问题。
两个极限的顺序不能调换。

### 2.3 未完成的查新边界

没有授予全球新意 PASS。MacKay–Meiss–Stark 的 converse-KAM 框架以及
更广的定量无共轭点/非极小轨道研究，仍可能包含直接推论或更强结果；本轮没有
取得并逐项核对其全部准确文本。鉴于作者容量已经确定不够，不再为此未入选
紧凑包启动无限文献追踪。该剩余不确定性被保存，不伪称已排除。

本次所有内容证据来自作者/官方全文；没有用搜索摘要、百科、AI网页或不相关
检索命中来证明一个定理不存在。网页 PDF 阅读不等于本地下载或实验。

## 3. 非重复的当前证明内容与页数估计

以下是同一个问题的自然叙述，不是为版面预分配的写作任务。页数是作者估计，
没有编译、没有双独立评分，也不计参考文献、审计记录或重复附录。

| 统一正文部分 | 当前实质 | 低 | 中心 | 高 |
| --- | --- | ---: | ---: | ---: |
| 问题、旧结果区别、精确定义与主定理 | 解释有限时全环面面积而非定性存在；明确失正 convention | 1.5 | 2 | 2.5 |
| 全域非共振正定性 | 有漂移动量的 Abel 求和、Dirichlet 控制、所有其他旋转带排除 | 2 | 2.5 | 3.5 |
| 缩放与首次时间/面积极限 | Jacobi minors、初始零点防护、$C^1$ 误差、零边界、积分换元 | 2 | 2.75 | 3.5 |
| 摆数据分类和整个极限分布 | 旋转/分离曲线/转向点/平衡点、连续性及严格增长 | 2 | 2.75 | 3.5 |
| 阈值精确系数和结论边界 | 唯一等号、局部化、四阶余项控制、极限顺序 | 1.5 | 2 | 3 |
| 合计 | 不加入新科学模块 | 9 | 12 | 16 |

这里最需要作者证明的部分是全域带宽控制与所指定面积读出的闭合；其余部分
虽须写严谨，不能通过扩写经典事实人为提升新增研究量。完整已有证明仅约
四百行 Markdown，分七步已闭合全部量词，不隐藏一项尚可自然占十页的主定理。

## 4. 不用于补篇幅的事项

- 一般三角多项式势的多个主共振带是另一个需新精确命题的问题，本轮没有证明，
  不当作已有模块计页，也不为凑页自动扩成附篇。
- 固定 $\varepsilon$ 后所有时间的非极小面积、交换双极限、随 $c$ 一致的
  速率、对数时间/分离曲线尾部均不由本定理自动得到。
- 不把先前 AS、链谱、Ruelle 或双谐波共振树结果拼到这个正文。
- 不增加数值拟合、任意参数扫描、绘图或长背景章节来填充22页。
- 证明和独立数学检查须保留；不把“未立项”写成“定理失败”。

## 5. 本轮一手检索账单

主控本轮围绕该线及其初期动力背景共作17条查询；最初一条 Lindstedt 查询
为同时评估的另一旧问题，实际不支持本结果。另有独立双谐波代理的八条查询，
只计入其自己的报告，不合并为本题新意证据。

1. `symplectic map first conjugate time standard map measure small perturbation pendulum`
2. `"twist maps" "conjugate points" "measure"`
3. `site:arxiv.org "standard map" "resonance" "Lindstedt"`
4. `"standard map" "conjugate" "measure" Bialy`
5. `"first conjugate" "pendulum" distribution`
6. `"standard map" "non-minimizing" measure`
7. `"twist maps" "measure of" "minimizing"`
8. `Bialy "standard map" "measure"`
9. `"twist maps" "quantitative" "conjugate"`
10. `"conjugate points" "small" "standard map"`
11. `"standard map" "conjugate points" measure estimate`
12. `"twist maps" "Hopf" measure quantitative`
13. `"pendulum" "conjugate time" "Jacobi"`
14. `"Bialy" "twist" "measure"`
15. `"standard map" "minimizing" "measure" small`
16. `"conjugate" "standard map" epsilon`
17. `"Bialy" "twist maps"`

准确一手链接的打开、页/定理阅读不计为新查询。没有扩大为新的研究族、
收费审查、外部发信、上传、托管或投稿。本报告为本地保存和后续非重复接续服务。
