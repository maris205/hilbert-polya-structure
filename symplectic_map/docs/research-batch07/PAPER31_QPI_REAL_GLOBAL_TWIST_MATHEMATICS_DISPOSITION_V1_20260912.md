# Paper31：原正时间全实正则旋转／twist 的数学接受

日期：2026-09-12 UTC，以本轮 clock 读数命名。主控：/root。
状态：GLOBAL_REGULAR_REAL_TWIST_MATHEMATICS_ACCEPTED / NOVELTY_NOT_YET_ASSESSED。
本件是本轮终态入口；科学证明、强来源核查、正式准入及论文产物四种状态分开。

## 1. 终态结论

接受固定全部 T>0、原完整有限实正则能级的真实分支回返旋转／twist 分类。
六份数学稿已冻结并由主控本人 FULL 读回；一位 fresh 非作者按两个增量阶段独查，两个终态报告也经主控 FULL 核准。
第一阶段检查实几何、acnode 锚定和中间区间；第二阶段只查新增上外回返、C¹ 无穷渐近及全局合成。
两阶段均为 PASS_BOUNDED_MATHEMATICS，无需要作者修正的错误；不是两个正式候选席位或跨模型票。
冻结作者稿中的 pending 标签保留为当时快照，由本终态处置覆盖，不回写旧稿。

这次接受的是全正则实能级上的完整 twist 表、六端点及积分确定的准确值域。
不声称节点全部奇异轨道、非自治扰动、每个有理角的最小周期清单或极大点逃逸速率已完成。
极大能量与极大值由具有唯一解的明确实积分确定，不声称存在初等闭式。
Paper31 未正式准入、未建项目／source locks／publication locks／稿件／PDF；未试排测页。
原22–30页及完整四门不变，整批仍4/5。数学接受不是新意分数、论文容量票或第五篇完成。

## 2. 全局表及实际对象

原映射 F_T(x,y)=(T/(x−y),x/y)，能量 h=−x+y+x/y−T/x。
四条合法 terminal 线保留；其交点在带点原 Weierstrass 模型上准确为 −2P、−P、O、P。
对 T=w±³(w±−1)，w−<0、w+>1，两个且仅两个实坏值为 h±=w±(3−2w±)，h−<h+<1。
以下统一按 ω=du/(2v+hu−T) 的正方向定向。
↑、↓ 是导数处处严格正／负；↑↓ 是准确一个非退化极大，先增后减。

| T | h<h−：F_T，分别保持两圆 | h−<h<h+：F_T，唯一圆 | h>h+：F_T²，两圆回返 |
|---|---|---|---|
| 0<T<3/16 | ↑ | ↑↓ | ↑ |
| T=3/16 | ↑ | ↓ | ↑ |
| 3/16<T<1 | ↑↓ | ↓ | ↑ |
| T=1 | ↓ | ↓ | ↑ |
| T>1 | ↓ | ↓ | ↑↓ |

因此除 T=3/16、1 外，准确存在一个有限实正则驻点能级；外区间该能级有两个圆，不是两个能级。
T=3/16 在奇异能级 h−=−2 的持续光滑圆上另有极大，不能混入正则计数。
上区间单步 F_T 交换两圆，其角不与其它区间的单步角混拼。

记 θ(T)=1/2+π⁻¹arctan(1/√(3−4w−))。三个区间的两端分别为
(5/8,θ)、(θ,1/2)、(0,3/4)；精确开闭值域及最大值的积分刻画见 [全局合成][S]。
θ=5/8 恰在 T=(1+√2)/4，只改变下外值域的较低端点，不是新的 twist 个数阈值。
h=1 的二次回返角正好1/2；h=9/8 的导数 H/(4δΩ)>0，均未从全局对象删除。

## 3. 新证明实际补齐了什么

实几何从原 singular-point 消元、完整四 chart 与真实平移式出发，给全部 T 的组件和回返；不是只研究正象限。
acnode 的含 O、P 实圆有显式 RP¹ 参数化和双侧解析周期，因此旧 Wronskian 的积分常数准确为 J(h−)=0。
中间区间用短弧有界、完整周期在 split node 发散证明上端1/2，进而将“至多一个”收紧为准确个数。
上外区间改用真实2P实弧；通过解析 K=δΩ²ρ′ 延拓，证明表观极点处的准确非零导数。
两无穷端独立自证完整积分的 log4 常数与不完整短弧的两个移动尺度，给带导数余项，不对未控制 o(1) 求导。
实际加权常数为

$$J_-(-\infty)=\frac18\log T,\qquad J_+(+\infty)=-\frac14\log T.$$

误差均为 O_T(log|h|/|h|)，所以 T=1 的零极限亦真实成立；结合严格单调的 J 得全局表。
旧 forcing 计算保持原输入，不在本轮重复计为新定理；标准实椭圆群、积分与一阶符号工具不自动计高新意。

## 4. 终态输入身份及主控读取

下表九件均由主控本人 FULL 读取；分段读取已补至EOF，没有将摘要代替原文件。

| 输入 | 行数 / bytes | SHA256 |
|---|---|---|
| [来源审计][SRC] | 159 / 13101 | cf80d3e4e9567eaf15ac302bdafda1e25c3f0dd81501d0edd52ef2706ff51d92 |
| [G：实几何][G] | 208 / 11847 | f0c92b3d03bc1686deb63877777d36c6297efde779d2fc02f81cde4d86e8a196 |
| [B：acnode上界][B] | 144 / 7701 | 9c948e5a649754192e781aac8fdec3c2d313645290dd36686f4b8a8e004eb96d |
| [M：中间端点][M] | 115 / 6053 | 4b07925048eb416d431d1e924c7d54a46c90c1a9b08708b6647c4430a79860a3 |
| [U：上外有限段][U] | 112 / 5614 | beaff1ed89c8f99b71f241340c5833d74ab1debfebf0c408335d2e4ed3dd5bff |
| [I：C¹无穷端][I] | 215 / 11115 | a6949cdae36598dd7b6d607e32f172321edeb046ebb08d1fab63dd9fa23191f6 |
| [S：全局合成][S] | 133 / 6753 | 63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24 |
| [Math1：第一阶段][MA] | 212 / 14963 | e00f5e920b9a66213e22709e3a7379161d311ee2f735473ba597171ab8d305e8 |
| [Math2：第二阶段][MB] | 201 / 14712 | 5e99316e1e20caca644ffe76724d86a62e791e7276e2168bb8527e230f2c5320 |

G/I 作者为 /root/p31_real_components_and_return；B/M/U/S 作者为 /root。
Math1/Math2 均为未参与作者稿的 /root/p31_real_geometry_twist_fresh_check，按新增量分两阶段，未再委派。
来源作者为 /root/p31_real_twist_primary_sources，只执行有界来源任务，没有核准全局数学。
主控旧文件仅 PARTIAL 消费原 scope §3、brief §3 V1a、forcing 的坐标／规范／Gauss–Manin 所需段及 P30V4 原模型所需段；不声称重审整条旧链。
主控本人 FULL 读 proof-writer、research-lit 与 ARS router 及 fact-check 所需 workflow/source-verification/quality references。
ARS 仅用事实核验模式，区分正文、摘要、目录与失败；没有运行全研究流水线、Socratic 闸门或自动写论文。

## 5. 强来源仍不等于已排除先例

[来源审计][SRC] 完成16条实际查询，含2024–2026及最近六个月定向；不得冒称数据库原生全面覆盖或16篇实读。
Beukers–Cushman 原机构PDF及尝试的出版社文章入口本次明确403，相关入口已停止；旧轮unknown失败另保留，不互相改写。
Duistermaat 的 [ETH原书三页目录](https://toc.library.ethz.ch/objects/pdf/e01_978-1-4419-7116-6_01.pdf)已由来源席FULL读取，
定位§8.2（实周期）、§8.4（旋转函数奇性）、§11.4（Lyness），但定理正文仍缺读。
本轮来源席另实际核 GMX Theorem3/正常形证明、CGM主定理陈述及若干回返引理；其本人范围详见SRC，不冒称主控另全文实读外文。
因此固定T路径与固定Lyness参数不同，只阻止直接套用，不证明新意。

主控另做8条公开查询，定位三个近邻原文入口；这些是主控执行身份，与来源席16条分开：

1. "q-Painlevé I" "rotation number"
2. "QRT" "rotation number" "real"
3. "Lyness" "negative" "rotation"
4. "Bastien" "Rogalski" "QRT" "bifurcation" arxiv
5. "The Periodic Orbits of a Dynamical System Associated with a Family of QRT-Maps"
6. "Periods of the solutions" "special QRT-map"
7. "Bastien" "Rogalski" "case of bifurcation"
8. "Behavior of orbits and periods" "QRT"

主控消费范围如下，不将搜索摘要升级为完整证明排除：

| 一手入口 | 本人实际证据与局限 |
|---|---|
| [Bastien–Rogalski，DCDIS2013摘要件](https://online.watsci.org/abstract_pdf/2013v20/v20n6a-pdf/6.pdf) | 成功取得2页文本（摘要／参考文献），非19页原文；研究正参数特殊QRT及周期。截图另返回Cache miss，未称已视觉核图 |
| [Bastien–Rogalski，QTDS2020出版社页](https://link.springer.com/article/10.1007/s12346-020-00393-2) | 元数据／摘要与公开附录段；主文显示subscription preview。摘要族为 x²y²−dxy−1+K(x²+y²)=0；未证明与原族的非共轭或不包含 |
| [Bastien–Rogalski，DCDIS2020摘要入口](https://online.watsci.org/abstract_pdf/2020v27/v27n2a-pdf/2.pdf) | 搜索索引呈现摘要及起始式；直接open最后明确406 Not Acceptable，未取得主文。关于一般特殊QRT及对称实例的近邻，不据它授原族分类先例或新意 |

这些近邻需要后继逐定理比对，不改成跨族研究项目；与原族无关的搜索输出已丢弃。
未打开非作者整书镜像、未绕访问限制、未下载PDF／配置新API／提取凭据／上传／发信／付费。
不存在新的本地权限阻塞；强来源缺读不阻止已授权数学推进，但不能据缺读授准入。

## 6. 与旧状态及下一项的关系

上一轮 [指定b机制][OLD] 的限定数学接受及4.0/10 CAUTION原票保持；该分数不适用于本轮新全局实分类。
指定b全阶满群仍未证；不因本轮实结果更新它，不扩N≥10阶方程／群表或旧HOLD/STOP。
旧准确厚度完整候选的双FAIL保持；本轮不是以改名复投同一厚度包，也没有事后替换其科学输入。
下一项应以本轮真实全局新结论建立定向查新与组合内非碰撞，核强来源是否包含这些阈值、对象与全分支量词。
若仍有独立中心，再组完整brief及必要证明图；不先建稿件、锁或试排测页。
正式准入仍须两个fresh非作者分别完成全部四门：新意≥7.5、独立价值≥7.5、完整证明信心≥9、可信22–30页容量PASS。
本轮没有请求或产生正式分数；不得把六份数学接受和两阶段同席报告算成正式双票。
本轮属于实质科学进展，不是无进展等待、家族耗尽、整批完成或权限阻塞；目标保持active。

[SRC]: PAPER31_QPI_REAL_TWIST_STRONG_SOURCE_AUDIT_V1_20260912.md
[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[M]: PAPER31_QPI_REAL_MIDDLE_ENDPOINT_TWIST_V1_20260912.md
[U]: PAPER31_QPI_REAL_UPPER_RETURN_FINITE_TWIST_V1_20260912.md
[I]: PAPER31_QPI_REAL_INFINITY_C1_ASYMPTOTICS_V1_20260912.md
[S]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[MA]: PAPER31_QPI_REAL_GEOMETRY_TWIST_MATH_REVIEW_V1_20260912.md
[MB]: PAPER31_QPI_REAL_OUTER_GLOBAL_MATH_REVIEW_V1_20260912.md
[OLD]: PAPER31_QPI_B_ALL_N_MECHANISMS_PREFLIGHT_DISPOSITION_V1_20260912.md
