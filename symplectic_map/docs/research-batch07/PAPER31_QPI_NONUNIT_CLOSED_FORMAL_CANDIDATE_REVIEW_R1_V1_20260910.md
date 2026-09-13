# Paper31 闭合非单位时间完整候选：正式独立审查 R1 V1

日期：2026-09-10 UTC。审查席：`/root/p31_qpi_nonunit_closed_formal_v1_r1`。
对象：冻结的原 $q=1$、$R=\mathbb Z[\tau]$ 八吹起族，完整 C1–C3、全部 $n$ 与全部素数 $p$。
结论：**本席四门合取 FAIL；不是数学否决，也不是部分预审。**

| 固定门 | 本席独立判断 | 门槛 | 结果 |
|---|---:|---:|---|
| 新意 | 7.0 / 10 | 至少 7.5 | FAIL |
| 独立科学价值 | 7.2 / 10 | 至少 7.5 | FAIL |
| 完整证明信心 | 9.2 / 10 | 至少 9.0 | PASS |
| 自然完整实质正文 22–30 页 | 有可信写法，但上端风险较高 | 可信 PASS | PASS |

分数是本席对同一个完整候选的判断，不是平均、四舍五入或多席择优。容量的低／中／高预测为 **22.75／29.50／38.00 页**，不是实测或严格界。下面四门均已完成，未因前两门不通过而停止证明或容量审查。

## 1. 审查身份、方法与隔离

本席为本次 fresh 非作者正式审查上下文，未编写 C1、G、C、DET、A、来源报告或 CD 报告；未读取本轮 R2 报告、消息或内部记录，未与 R2 通信、校准，未再委派投票。共同包包含历史分数，所以不称对历史意见盲审。

本人先完整读取 `docs/WORKFLOW.md`（39 行）及 `/root/autodl-tmp/.codex/skills/skills-codex/research-review/SKILL.md`（102 行），按 research-review 的高强度证据核验、最强反对意见和不继承结论原则执行。指定 GPT-5.4 MCP 未配置，实际采用可用 Codex 新审查上下文；未声称该指定模型运行。技能只影响本报告的审查纪律，不产生新的科学主张或额外写权限。

`route_applicability: NOT_APPLICABLE`；`cross_model_verification: NOT_PERFORMED`；`score_calibration: NOT_CALIBRATED`。
这不是人类认证、形式化验证、期刊录用概率或 PDF 验收。正式研究评价与此前数学接受、编译成功及批次状态相互区别。

本席只创建本报告；创建前实际确认目标不存在。未改共同输入、冻结原稿、索引、锁或旧票，未创建论文项目、稿件、PDF 或测页稿；未运行数学脚本、扩大样本、重编译旧产物或构造替代证明。公开原文核对限于共同来源包已列的必要一手文献，无付费、认证绕过、对外联系或上传。

## 2. 输入身份和本人实际覆盖

唯一共同科学入口为 [manifest V1](PAPER31_QPI_NONUNIT_CLOSED_REVIEW_INPUT_MANIFEST_V1_20260910.md)，本人 FULL 读取至 EOF，共 193 行；SHA-256：
`2574134d896530e097bbebc1e9e855fea2f03aeabcba337ac98e8d2fb1404486`。

本人实际核对 manifest 所列 **46 件整文件**的存在性、字节数和 SHA；45 件文本的整文件行数亦与清单一致。没有重扫旧 build 树或间接历史链。哈希核对只证明对象身份，不替代以下内容阅读。

为使路径自足而不反复打印长前缀，以下使用精确定义：

- `D/` = `/root/autodl-tmp/symplectic_map/docs/research-batch07/`。
- `P18/` = `/root/autodl-tmp/symplectic_map/papers/18-marked-henon-scalar-boundary/paper/`。
- `P29/` = `/root/autodl-tmp/symplectic_map/papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/`。
- `P30/` = `/root/autodl-tmp/symplectic_map/papers/30-qpi-vertical-critical-ideals/paper/v4/sections/`。

### 2.1 本人 FULL 的 32 份文本

下面全部本人逐段读至 EOF，包含原证明及相应检查，不是仅读摘要、Claim、定位表或哈希。一次显示截断涉及 IC1 尾部和 IG 开头，已分别补读 IC1 第 154–177 行、IG 第 1–30 行，不留缺段。

| ID | 完整实际路径 | 本人覆盖 | SHA-256 |
|---|---|---|---|
| BRIEF | `D/PAPER31_QPI_NONUNIT_CLOSED_CANDIDATE_BRIEF_V1_20260910.md` | FULL 1–205 | `568b4b829b60c8dc6ce5129a984ae7e593db22d2bad9ff2e6ebebfbda63063fb` |
| MAP | `D/PAPER31_QPI_NONUNIT_CLOSED_CURRENT_PROOF_MAP_V1_20260910.md` | FULL 1–281 | `ca7cb9068456288783cd2c06874d5cc8656035e9f3f6888c39ecacdff200701e` |
| PRE | `D/PAPER31_QPI_NONUNIT_CLOSED_PREFLIGHT_DISPOSITION_V1_20260910.md` | FULL 1–87 | `0f27d8c43b88a04052d22f349861f56a96925f271529a979eb7134b3db1c5ef5` |
| INV | `D/PAPER31_QPI_NONUNIT_CLOSED_SHARED_INPUT_INVENTORY_V1_20260910.md` | FULL 1–144 | `d607eec2d33daf89210911a9965ed9498f1ef10af83d8faa3ecb7cd04a76794c` |
| IC1 | `D/PAPER31_QPI_NONUNIT_C1_PROOF_CONSUMER_INVENTORY_V1_20260910.md` | FULL 1–177 | `ca5fe99e671cedaf7ae5f92115a5fe346eea648390ed1dbc0cef2a17fabb19a2` |
| IG | `D/PAPER31_QPI_NONUNIT_G_PROOF_CONSUMER_INVENTORY_V1_20260910.md` | FULL 1–185 | `6b75b13ee4421fd55b2ed93e11cc89945d53d7eed5952afb10c62531baf38801` |
| PA | `D/PAPER31_QPI_NONUNIT_CLOSED_ARITHMETIC_PHASE_A_V1_20260909.md` | FULL 1–83 | `07b658e0e6a07fece0db86d85face58a852646760a6e8d185f7715800dd2ae5f` |
| MATH | `D/PAPER31_QPI_NONUNIT_ALL_DEGREE_MATHEMATICS_DISPOSITION_V1_20260910.md` | FULL 1–117 | `a0d1c880f45462721f78366234d0d5796d04f95c46428c05caacdb90ce75fdd3` |
| PB | `D/PAPER31_QPI_NONUNIT_CLOSED_PHASE_B_DISPOSITION_V1_20260910.md` | FULL 1–64 | `5bfb95183689687b53fd1656896b64847605c362d260b1b68e999d7cee4b28ee` |
| CD | `D/PAPER31_QPI_NONUNIT_CLOSED_NOVELTY_CD_V1_20260910.md` | FULL 1–236 | `4f3f186d7e2c2b4dc8d1d733358d6c849d03c6ba3542b287d8207a4c5bb62737` |
| BASE | `D/PAPER31_QPI_TWO_DIAGNOSTICS_DISPOSITION_V1_20260909.md` | FULL 1–96 | `3a3d3444e5237af5dab971d488fa1d513d5fcc4bdb32d3c4cd1a008e0d19ee59` |
| JET | `D/PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md` | FULL 1–358 | `0acbfc4866b0cf944c84f88c8db3e7c535fdbff366ead4f166c3d8f01e3e2005` |
| JC | `D/PAPER30_QPI_NONUNIT_TAU_JET_AND_MIXED_INDEPENDENT_CHECK_V1_20260909.md` | FULL 1–327 | `b3b68ac29e95c2db273ad83a528c131a4fdca63a94e6fb7e5abc8235eede4eb7` |
| EXT | `D/PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_DIAGNOSTIC_V1_20260909.md` | FULL 1–318 | `9c87c8570065deba6dd14e33e7a27382a2d3d6ba34f01a883ee7faff92fb60d0` |
| EC | `D/PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_INDEPENDENT_CHECK_V1_20260909.md` | FULL 1–179 | `12b9ce4f6b6e485c8457478821eb3c2cc8afca74807aa98daf17240b586d4370` |
| G | `D/PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md` | FULL 1–429 | `d872b731423107412631a9834b639229b2578e0084afef752c6a94d6e90f7c6a` |
| GC | `D/PAPER31_QPI_NONUNIT_LATTICE_CONTROL_INDEPENDENT_CHECK_V1_20260909.md` | FULL 1–262 | `f1ce1a0f70ac536a38dcfcfdac064e3468615807f4ba820c6befae6d5f7121b6` |
| C | `D/PAPER31_QPI_NONUNIT_BINOMIAL_CONSUMERS_LEMMA_V1_20260909.md` | FULL 1–176 | `25bb87a365eaf5a9d37c192a47f99d454007aa14e265668c34465cc3e2154e10` |
| DET | `D/PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md` | FULL 1–297 | `913e701986e540a59476a9f64bf890bf3bbdc300596ef9db9514ebe784dcb250` |
| TC | `D/PAPER31_QPI_NONUNIT_LATTICE_TOOLS_INDEPENDENT_CHECK_V1_20260909.md` | FULL 1–193 | `076e030cdb20cee50ec9cba9578146c61641fdbbb68c3db9839cc94dd8b2188b` |
| A | `D/PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_THEOREM_V1_20260909.md` | FULL 1–180 | `f214e2e14d065e778d752f15855995d0a66df4c115d7aa72e14af5695e153260` |
| AC | `D/PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_INDEPENDENT_CHECK_V1_20260909.md` | FULL 1–180 | `6aa3dfbec7172da44b328f8baef318488e56a8150536cf0bfdd0eaddf28d61a3` |
| S13 | `D/PAPER31_QPI_NONUNIT_CLOSED_SOURCES_C1_C3_V1_20260909.md` | FULL 1–181 | `afc7c9b54044c25df82cfcaad62563e4d53f6c810be2eb785beb51f9eb7f294a` |
| S2 | `D/PAPER31_QPI_NONUNIT_CLOSED_SOURCES_C2_V1_20260909.md` | FULL 1–228 | `01bc654082a21736c7af0e7494382d7f321d1c1b2b23492f6782d27c305b3d94` |
| FS | `D/PAPER31_QPI_NONUNIT_FITTING_SOURCE_SUPPLEMENT_V1_20260909.md` | FULL 1–102 | `60e972d287f5cf3d234826acd3caa4532f62e50a6578415c6942f4c0a19c2f36` |
| PD | `D/PAPER31_QPI_NONUNIT_CLOSED_PORTFOLIO_DELTA_V1_20260909.md` | FULL 1–221 | `766bbefd7df8918759101a543ff9f0635289cc77e24c5a18364ed065770eec7f` |
| PORT | `D/PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md` | FULL 1–121 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| LIMIT | `D/PAPER29_30_EXISTING_INTERFACE_LIMITS_V1_20260909.md` | FULL 1–121 | `bbcc282cad6a78da92500b21ee91ed892f1152bbfc339f2ad860468c27af593c` |
| NU | `D/PAPER30_QPI_NONUNIT_TAU_MATHEMATICS_AND_SCREEN_DISPOSITION_V1_20260909.md` | FULL 1–146 | `cf438f313d34c70f8dc7d775894524164460ba8a69d16c01c712a174a8200de0` |
| INT | `D/PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md` | FULL 1–162 | `1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af` |
| M4 | `D/PAPER31_QPI_NONUNIT_M4_INTEGRAL_BLOCK_LEMMA_V1_20260909.md` | FULL 1–127 | `1161e63f35fa07ac401d9fc21fe58167f2cad39b0a810e37638b663f3ed8f663` |
| M4C | `D/PAPER31_QPI_NONUNIT_M4_INTEGRAL_BLOCK_INDEPENDENT_CHECK_V1_20260909.md` | FULL 1–149 | `6bef85adcd0708abd00af14704413645351e803aaa03d0aa94a77d46f46286f6` |

### 2.2 本人 PARTIAL 的 13 份旧比较／基线文本

以下 SHA 仍绑定整文件；读取范围只限明确责任，不冒称整篇旧稿已重审。P302 额外读取了清单允许的 1–29 行，用于核对原中心和单位底环；其余没有超出规定的必要范围。

| ID | 完整实际路径 | 本人实际行范围（均 PARTIAL） | SHA-256 |
|---|---|---|---|
| OLDCD | `D/PAPER31_QPI_NOVELTY_CD_I05_I09_V1_20260909.md` | 1–109、160–174、187–216 | `4b1d3fdbb51f7b1e1250dfea393133ff3b409bc2bc5e130f7d8b55f703ef7fd4` |
| P18 | `P18/main.tex` | 525–618、1053–1295 | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` |
| P29I | `P29/1_introduction.tex` | 19–39 | `7a93eba84684809c101dd6d4500c0c97702d816da7d3821603b2ac79805289d8` |
| P293 | `P29/3_filtered_primitives.tex` | 1–244 | `e8e5410a2df50f5591da6a4eacaebbe350fad7c4c179911d39f259fc176e4bf1` |
| P294 | `P29/4_hilbert_series.tex` | 53–100 | `e62e02e9511c77e2a739cde7d36e659cf9ff666f536af5346dd9d0d7c6a93884` |
| P302 | `P30/02-surface-pencil.tex` | 1–29、228–338 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| P305 | `P30/05-integral-trace.tex` | 84–161 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |
| UNIT | `D/PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md` | 1–108 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| FIRST | `D/PAPER30_QPI_NONUNIT_TAU_FIRST_LAYER_PROOF_V1_20260909.md` | 7–64、84–114、171–219 | `ef975ded12f7263842e208f6eda87df213e210e9dbf7ef3c08fbd8724fe6270d` |
| FIBRE | `D/PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_FIBRE_PROOF_V1_20260909.md` | 7–59 | `dd9cc251bed71eeca5e0063b8dd67c83d820cbedd49dcec43322001840e6b620` |
| FC | `D/PAPER30_QPI_NONUNIT_TAU_FIRST_AND_FIBRE_INDEPENDENT_CHECK_V1_20260909.md` | 1–68 | `cc21bf738c64136b6f2842a1ba60e7407208126feed6566b5ddef6802fa5f5bc` |
| M3 | `D/PAPER30_QPI_NONUNIT_TAU_DEGREE3_MIXED_OBSTRUCTION_PROOF_V1_20260909.md` | 1–64、193–252 | `fe9f9f1c70b20eea4d587d57959eafd9dd8ab42cc128119c32ac6714c77470e8` |
| W | `D/PAPER30_QPI_NONUNIT_TAU_FIRST_PRIME_OBSTRUCTION_PROBE_V1_20260909.md` | 1–107、199–242、252–279 | `360741298e0a3478586031eb7ef19b18e0a36ce899b78c856cd3473c8671249a` |

FC 的既往材料接触／非 fresh 身份和旧作者件的 pending 原文均保留；其后接受状态由 BASE、MATH 等记录定位，不通过改写历史来制造一致。

### 2.3 必要原 PDF 及本席公开一手核对

GR 的完整实际路径为 `D/primary-sources/griffiths-1976-variations-on-a-theorem-of-abel.pdf`，整文件 70 页、3,193,217 字节，SHA-256：`517692faba4fb281bb78b2f129fde7dabe6a3625e5dcb4f75cfdad37fc521fb1`。本人完整读取 PDF 第 48–53 页（印刷 368–373）的文本，并因公式提取不完整实际查看这六张页面。覆盖 §III(a) 的局部定义、坐标变换、定理 (3.7) 全声明及其 Stokes 证明；记为 **PDF_PARTIAL_REQUIRED_RANGE_COMPLETE**，绝非全文 70 页 FULL。只生成该六页的临时阅读图，没有改 PDF 或生成论文产物。该原文是 [Griffiths 的 IAS 机构版本](https://publications.ias.edu/sites/default/files/variationsonatheorem.pdf)。

另外只对已列来源作了以下定向公开核对；没有另起无界查新或引入清单外本地科学文件：

| 来源 | 本席亲读而非继承的范围 | 明确未覆盖 |
|---|---|---|
| Maakestad, *Principal parts on the projective line over arbitrary rings*, arXiv `math/0402279v4` | 官方 PDF 的 Theorem 3.1 全声明及实际写出的 (3.1.1) 证明；§4 的 (4.0.1)–(4.0.4)、线性系统及 Theorem 4.1 声明。文本可辨认二项式系数、负幂展开和单位条件 | 没有完整读取 Theorem 4.1 的矩阵证明或全篇；正文把 (3.1.2)–(3.1.4) 的证明留作练习，不能声称读到了它们的完整作者证明。截图请求没有得到可用页面，部分返回 Internal Error／TimeoutError；未将其记为视觉核验成功。[官方 PDF](https://arxiv.org/pdf/math/0402279v4) |
| Kyomuhangi–Marangone–Raicu–Reed, arXiv `2411.13450v1` | 官方 HTML 中 §2 局部上同调／双次数乘法接口，§3 定义 (3.1)–(3.5)、Remark 3.1、Theorem 3.2 四种情形完整声明、Corollary 3.3 及其证明、Lemma 3.4 的负二项式基与完整证明 | 未完整读取 Theorem 3.2 的其余证明，也未读全篇。版本头为 2024-11-20，渲染正文另显示内部 Date 2026-08-24；本席按所访问的明确 v1 身份记录，不凭 HTML 日期另算一篇新成果。[官方 v1 正文](https://arxiv.org/html/2411.13450v1) |

S13、S2、FS 中其余论文的 FULL／部分正文／预览／失败标签是那些报告的实际观察，不自动变成本席亲读原文。本席 FULL 读的是三份来源报告及其中证据；对其他来源的判断下文明确按报告证据层级使用。尤其未取得 Ohm 2008、Hadjirezaei 2026 全文，未补齐 Perkinson 交换图或 Guardo 后段，不声称重新成功访问 Scholar／Semantic Scholar。

## 3. 固定完整主张：评价的不是删减版

原模型保持四簇 $1+2+3+2$ 次有序吹起。在 $q=1$ 后仍有八个相对正则中心，两个取值为 $\tau$ 的中心在不同分量上，不因 $\tau=0$ 而被合并或删除。$Y$ 是完成四次节点吹起后的中间 toric 曲面，$S$ 是完成全部八次吹起后的曲面；留数在 $Y$，被识别的上同调在 $S$。

记 $\mathscr L=\omega_{S/R}^{-1}$，$M_n=H^1(S,\mathscr L^n)$，$T_n=\ker(M_n\to M_n[1/\tau])$，$L_n=M_n/T_n$，$E_n=L_n^{**}/L_n$。JET 的实际复形是
$$R\Gamma(S,\mathscr L^n)\simeq[V_n\xrightarrow{J_n}W_n],\quad
\operatorname{rank}V_n=2n(n+1)+1,\quad W_n=(R[u,v]/(u,v)^n)^4.$$
其原受限单项式域和四个 $Q_{r,n}$ 必须保留；仅有相同维数的另一个矩阵不能替代。复形兼容任意基变换不等于所有后续短正合列自动兼容非平坦基变换。

### C1：完整标记扩张与恢复

固定 $s_0=xy$、$s_1=x^2-x^2y+xy^2-\tau y$。对所有 $n\ge0$，完整核是 $s_0^{n-i}s_1^i$（$0\le i\le n$）的自由张成，且原乘 $s_0$ 给
$$0\to M_n\xrightarrow{\iota_n}M_{n+1}\to
R\oplus\bigoplus_{r=2,3}\bigoplus_{a=1}^n R/(\tau^{n+1-a})\to0.$$
令 $m=n+1-a$，每个指定新生成元 $y_{r,a}^{(n+1)}=[u^a]_{r,n+1}$ 的关系是
$$\tau^m y_{r,a}^{(n+1)}=\iota_n(e_{r,a}^{(n)}),\qquad
e_{r,a}^{(n)}=\left[u^{a-1}\sum_{b=0}^{m-1}(-1)^b\tau^{m-1-b}v^b\right]_{r,n}.$$
在 $M_n/\tau^mM_n$ 中保留这些完整标记 Ext 值，不只保留商模或非分裂性。所有 $n\ge1$ 的整列非分裂，$n=0$ 单独作为基例。

恢复包括先提取并扣除全部指定商坐标提升，再处理共享顶点兼容条件、提升原四边源、扣除实际 $J$ 像、精确除以原乘法并降次数。不能删恢复或只写 Ext 的几何级数恒等式。此结构不是全部原模的规范块分类，也不赋予 $M_n$ 一个未经证明的 $R[u,v]$-模结构。

### C2：原整数留数格、全部系数层与真实移位

令 $N=n-1$、$I_{n,a}=(\binom{N-b}{a}\tau^b:0\le b\le N-a)$。对所有 $n\ge1$，实际留数识别满足
$$\rho_n:M_n[1/\tau]\simeq R[1/\tau]^n,\quad
\rho_n(M_n)=\tau^{-n}\bigoplus_{a=0}^{n-1}I_{n,a},\quad \ker(\rho_n|_{M_n})=T_n.$$
归一化 $\widetilde\rho_n=\tau^n\rho_n$ 后 $L_n\simeq\bigoplus_a I_{n,a}$、指定 $I_{n,a}^{**}=R$、$E_n\simeq\bigoplus_aR/I_{n,a}$。未归一化坐标的原 $s_0$ 为右移，归一化后为 **$\tau$ 倍右移**；$(-1)^{n-1}\tau^n\rho_{n,0}=\Psi_n$ 锁定与 C1 的兼容坐标。

在 $A_p=R_{(p,\tau)}$ 上，令 $d=N-a$、$e_b=\min_{0\le j\le b}v_p\binom{N-j}{a}$，则
$$A_p/I_{n,a}A_p\simeq\bigoplus_{b=0}^{d-1}\mathbb Z_{(p)}/(p^{e_b})\,\tau^b.$$
这是加法系数层分解，$\tau$ 作用为相邻自然投影并杀死末层，不是各层作为 $A_p$-模的独立直和，也不缩成模 $p$ 维数。

### C3：整个基环首 Fitting、所有特征扭长与数字规则

设 $B_n=\sum_{j=1}^{n-1}j^2$（$n\ge1$）、$B_0=0$，$d_p(N,a)=\min\{0\le b\le N-a:p\nmid\binom{N-b}{a}\}$，$D_n(p)=\sum_{a=0}^{n-1}d_p(n-1,a)$。完整结论为
$$\operatorname{Fitt}_j(M_n)=0\ (j<n),\qquad
\operatorname{Fitt}_n(M_n)=\tau^{B_n}\prod_a I_{n,a}\quad\text{在整个 }R\text{ 上},$$
$$\ell_{k[[\tau]]}\operatorname{tors}_\tau(M_n\otimes_R k[[\tau]])=
\begin{cases}B_n,&\operatorname{char}k=0,\\ B_n+D_n(p),&\operatorname{char}k=p>0.\end{cases}$$
自由秩为 $n$。同次数特征比较首次增加恰在 $n=p+1$、增加 $p-1$，该处局部首 Fitting 是 $\tau^{\sum_{j=1}^p j^2}(p,\tau)^{p-1}$。
对所有 $n\ge1$，有
$$D_n(p)=0\iff n/p^{v_p(n)}<p\iff E_n\otimes_R A_p=0\iff L_n\otimes_R A_p\text{ 自由}.$$
令 $H_p(N)=D_{N+1}(p)$、$H_p(-1)=0$、$Z_p(h)=\prod_i(h_i+1)$、$Z_p(0)=1$。所有后续长度缺陷用
$$H_p(ph+r)=p(r+1)H_p(h)+p(p-1-r)H_p(h-1)
+(r+1)(p-1-r)(Z_p(h)-1),\quad0\le r<p$$
及 $0\le N<p$ 的零基例终止计算。$p=2$、$h=0$、$n=0,1$ 不排除。$M_0=T_0=L_0=E_0=0$，但 $V_0=H^0(S,\mathcal O_S)=R$；$\operatorname{Fitt}_0(0)=R$。

原强 (P)、全部 Smith 型、更高 Fitting、一般 $q$、非加法结构及零时间可逆动力都不在这张票内；不能拿它们的潜在价值给现候选加分。完整 C1 不因 C3 只消费其正合列而删掉；同样，不能伪称 C3 单独消费每个标记 Ext 值。

## 4. PM1–PM11 完整责任与本席证明核验

MAP、IC1、IG 用来定位，以下判断来自相应原证明本身；独立检查件用于检查已记录风险及修正，未把其 PASS 直接作为本席信心。

| 模块与主来源 | 本席检查的必要推理，不是只看结论 | 实际消费者与结论 |
|---|---|---|
| PM1：JET Steps 1–4；FIRST 91–95 | 分簇重排不改原曲面；所有中心包括 $\tau=0$ 都是相对正则截面；canonical Jacobian 给例外因子。单次吹起的 $\mathcal O(-nE)$ 推前用 $\mathcal O(-1)$ 总空间和两图 Čech 得到真实 $I^n$，不是从核猜余核。四个被删单项式集合不重叠且有单位右逆；末四点以全 fat jets 给实际 cone 和基变换 | 全部 C1–C3 的同一原对象。通过；没有把旧八组脚本和二阶分解加入必要主干 |
| PM2：EXT Steps 1–5 | 原乘法在坏图为 $u(\tau+v)$，利用最低齐次层及 $\tau$ 非零因子证明单射。完整目标商有两坏图的 $R/(\tau^m)$；原源是四条共享顶点的边。整数插值把唯一兼容式从必要推进到充分，第三图常数给单位分裂；$s_1^k$ 提升商核，归纳得到全部核与真实短列 | C1；PM4 的原逆 $\tau$ 自由秩、PM6 的全核、PM8 的原 H1。通过 |
| PM3：EXT Steps 6–8 | 几何级数乘积的末项恰在新截断总次数消失，给全部标记 Ext。商生成与旧单射共同保证递归呈示没有遗漏关系。$n=1$ 基例和一般旧商中的非零像证明每层不分裂。恢复必须先扣指定新提升，再用共享边插值及精确除法降次数 | 完整 C1；不拿 $L_n$、Fitting 或长度反推。通过，全部关系／恢复均保留 |
| PM4：G Steps 1–4；GR 规定六页 | 区分 $Y$ 与 $S$；八条 toric 射线的最低面、四根 $1,\tau,\tau,1$ 和顶点单位排除遗漏共同零点。核对 $F_r,G_r$ Jacobian 常数 $(-1,\tau,\tau,1)$，canonical $\kappa=(-1,1,-1,-1)$、$\epsilon=-\kappa$。紧复曲面留数消失经整数 Laurent 条目身份给 $\rho J=0$。第三图截断 $\Delta_3F_3^aG_3^{N-a}$ 命中标准基，同秩自由源才给全开集同构 | C2 的原局部化识别；不是仅给 $n$ 个泛函。通过 |
| PM5：G Steps 5–8 | 坏图 $\lambda=1+u^2(u-1)(\tau+v)$、$U=u/\lambda$、$V=v+u^2(u-1)(\tau+v)^2$ 为完整形式自同构；$\tau+V=(\tau+v)\lambda$，故 $F=U(\tau+V),G=V$。保留并吸收全目标上的体积 Jacobian 单位；独立单项式才给直和格像。好图像包含在坏图像中。原乘 $F$ 在同一留数坐标中给移位；最后核对自然 $I^{**}=R$ | 完整 C2；C 的 H2–H3、DET 的自然归一化。通过 |
| PM6：A Step 1 | $P_k=s_0^{n-k}s_1^k$ 的最高 $y$ 项准确为系数 1 的 $x^ny^{n+k}$，且这些系数行都在原 $\Lambda_n$。单位三角 minor 把完整核补成源基，不用“核自由则商自由”的错误推理；删完整 $n+1$ 个零列 | 得实际 $0\to R^{n(2n+1)}\to R^{2n(n+1)}\to M_n\to0$；是 PM9 的真实前提。通过 |
| PM7：C Steps 1–3 | 各 $\tau^b$ 系数理想为前 $b+1$ 个二项式系数的整数 gcd；商局部化和逐层 $\tau$ 投影准确。$p$-核计数是正指数层数，不是指数和。Lucas 由 Frobenius 多项式恒等式给出；$N=p$ 端点单位、中间 $p-1$ 个 $(p,\tau)$ 包括 $p=2$ | C2 的完整厚度，C3 首现及 PM11 数字输入。通过 |
| PM8：C Steps 4–6 | 原相邻商无整数 $p$-扭子，故相应 Tor 消失。定义专门化原模在 Laurent 空间的真实像，不假设 $L_n\otimes k[[\tau]]$ 自身无扭。实际右移给格商扭长 $\kappa_n=(n-1)+D_{n-1}-D_n$；蛇形列的后两模自由秩一，其满射在无扭商上乘单位，才可扣去 $\kappa_n$ | 原所有特征长度增量 $(n-1)^2+D_n-D_{n-1}$，望远镜和为 $B_n+D_n$。通过 |
| PM9：DET 全部当前引理 | 矩阵 $P$ 的像是自然 $L\subset L^{**}$，在基环上 $\ker P/\operatorname{im}\Phi$ 仍有扭子，不能置零；只在分式域取互补顶次形式。全部互补最大子式由同一 $\delta$ 相连。高度一 DVR 算其赋值，整个逆 $\tau$ 开集自由排除其他因子，再用 UFD 回到准确理想，而不是只保留除子 | 条件性首 Fitting 因子式含高度二自然行列式理想。通过；旧未归一化推论不复活 |
| PM10：A Steps 1–3 | C 的 H1–H3、DET 的真实分辨率、全开集自由、有限 $E$、指定 $I^{**}=R$ 和特征零 $B_n$ 都由同一原模供给。逐一覆盖不含 $\tau$ 的所有素点、$(\tau)$ 和所有 $(p,\tau)$；较低 Fitting 用实际矩阵阶数给零 | C3 的整个 $\mathbb Z[\tau]$ 理想及全素数首现，非只选一个局部点。通过 |
| PM11：A Steps 4–5 | 无缺陷等价于 $N$ 最高位以下皆为 $p-1$，再准确转成 $n/p^{v_p(n)}<p$。将 $N=ph+r,a=pb+s$ 按 $s\le r$ 与 $s>r$ 分支，零距离项数为 $Z_p(h)$；核对常数项、$h=0$ 和递归参数严格下降 | 完整 C3 消失充要条件和所有后续长度缺陷递推。通过，不输出所有块 |

### 4.1 两处最容易失真的连接

**C1 的真正源约束与恢复。** 若把共享顶点的四边当作四个任意单变量多项式，兼容条件的充分性会被跳过。本席核对 EXT 的整数式：取 $k=n+1$、$e=(-1)^k$，其消去条件为
$$\Psi=g_3(-\tau)-g_2(-\tau)+e\tau^k g_1(-1)+\tau^k g_4(-1)=0.$$
四个边的末项系数由共享端点联立决定，剩下恰这一条件，第三常数项给单位满射；并非仅从秩得出。恢复中坏图的 $P(v)$ 满足 $P(-\tau)$ 可被 $\tau^m$ 整除，选 $c=(-1)^{m+1}P(-\tau)/\tau^m$ 后 $P(v)+cv^m$ 可被首一 $v+\tau$ 整除。该除法在整数环中完成；这解释了恢复为何不偷偷反演 $\tau$。这些核验是对已有证明的检查，未另写替代定理。

**原格、实际移位与首 Fitting 不能分对象拼接。** G 的满射在 $R[1/\tau]$ 上成立；PM2 已给整个该开集上的自由源，所以不是“泛点秩相同”替代同构。正规形使用整个 fat-jet 目标，Jacobian 单位可吸收到任意目标系数，不能只对原受限源这样做。随后 C 专门化的是原模，算的是其真实像；DET 的 $L^{**}$ 是自然双对偶。三者恰匹配，才允许把 $I_{n,a}$、$B_n$ 和全局 Fitting 写在一起。

DET 的历史修正不是可忽略的字面细节：抽象 $A\simeq(p)$ 已说明任意理想表达不能直接相乘。当前实际输入给指定 $I_{n,a}^{**}=A_p$，故修正后的乘积适用；本席没有发现旧错误在现应用中残留。

### 4.2 标准外部工具的适用性

GR (3.7) 要求紧复流形、适当分组的极除子以及有限共同交点，允许交点重数；本应用在 $\tau\ne0$ 的光滑紧复曲面 $Y_\tau$ 上核对了这些条件。局部取向和 $(2\pi i)^{-2}$ 的标准归一化不影响零和，但原四图相对符号仍必须保留。正性／ample 只出现在另外的逆方向命题，不被本应用借入。GR 给消失，不给整数格；从复数纤维到整数 Laurent 恒等式的提升以及整数像都由 G 的实际计算承担。

局部吹起 Čech、平坦域扩张和完成、Ext 的长度一分解、UFD／DVR、互补子式及 Lucas 属于标准机制。本席核对其实际使用条件，不额外要求把所有一般文献的全文证明搬进正文。没有发现一个尚未读取的清单外本地科学对象是当前必要消费者。

## 5. 新意：7.0 / 10，FAIL

这不是“只剩一串样本”的候选。完整 marked Ext 与精确格确实关闭了此前缺失的同对象识别，C3 也已由原链推出全称结果。新意不足的判断来自扣除之后的研究差额，而不是数学未完成或历史分数的机械继承。

### 5.1 最强先例和准确扣除

| 先例／既有基线与证据入口 | 必须扣除的内容 | 尚未由所读证据直接包含的差额 |
|---|---|---|
| Callan 的 Pascal/Jordan/Smith；证据为 S13 §S1 和 W 的已读比较段 | 完整 Pascal 平移的整数可逆性、相关二项式矩阵结构不是新方法 | 原四簇受限源、截断和共享顶点不能由一个完整 Pascal 矩阵直接替代。没有现成原标记 Ext 识别被提供 |
| Maakestad 的整数主部丛坐标；本席亲读范围见 §2.3 | 二项式 Laurent 过渡与负幂展开是已有机制；任意环分裂有系统可解和单位条件，不是无条件整数分裂 | 现原 $J_n$ 与完整 $\rho_n$ 的识别仍须证明，不因正文里有二项式就完成包含 |
| K24/K25 主部丛和正特征上同调递推；K24 有本席亲读，K25 依 S2 的 §3 证据 | 全次数正特征分裂递推、局部负二项式基、双次数乘法接口已是强先例，不能称“全 $n,p$ 的数字规律”本身新 | 需要同时匹配原整数源／商、截断、$\tau$ 作用和 $s_0$，不能只用“一个在域上”就排除潜在包含。当前证据没有给这张完整识别图，也没有证明不存在 |
| GR 及 CCD 的 toric/global residue；前者本席六页原文，后者依 S2 | 全局留数和为零、局部残差对偶、形式逆坐标都不新 | 四中心穷尽、canonical 标架、原自由余核与整数像的绑定是对象特有计算 |
| Perkinson、Galuppi、Guardo 的主部丛／fat points／separator；依 S2、S13 | 插值、降低重数、碰撞和限制映射框架应扣除 | 原整数连接和厚度仍需匹配；Perkinson 关键图、Guardo 后段缺口使更强包含仍未排除 |
| Rowland 的 Lucas/Fine／数字计数；依 S13 §S3 | Frobenius 数字支配、非零二项式计数与数字递推方法不新 | 现距离和 $D_n(p)$ 绑定到原长度及其准确公式是本对象发现，不能单独当新的数字理论 |
| Stacks Fitting；Ohm 2008、Hadjirezaei–Hedayat 2013、Hadjirezaei 2026；依 S13、FS | 首 Fitting、去扭商、自然双对偶缺陷及行列式机制不计方法新意 | 原全局 $\tau^{B_n}\prod I_{n,a}$ 的具体绑定尚未由这些有限范围直接包含；全文缺失绝不成为排除先例或加分证据 |
| JET、FIRST、FIBRE、M3、M4 及 W3；本席覆盖见 §2 | 原模型、实际全次复形、零时间维数、低阶混合块、首次 $p=2$ 非主理想和单位补基机制均是既有基线 | 新候选是闭合的整个相邻标记系统及原全次格／长度／Fitting，不是首次发现非自由或某个有限素数异常 |

Maakestad 的坐标公式和 K24 的递推分别提供经典机制与近期强理论压力；本席据实际段落作上述方法扣除，而没有把相关论文题名当作整包包含定理。[Maakestad 原文](https://arxiv.org/pdf/math/0402279v4)、[K24 原文](https://arxiv.org/html/2411.13450v1)。

FS 保留的 2026 可见 Theorem 1.3 有“首 Fitting 准素且高度一”的额外假设。在本对象首次理想 $Q=\tau^B(p,\tau)^s$ 中，$p^s\tau^B\in Q$、$\tau^B\notin Q$ 而 $p\notin\sqrt Q=(\tau)$，所以这条可见定理不能直接替代本非主理想。但这只排除了**该条**直接套用，没排除整篇 2026 论文或 Ohm 全文的其他因子式。该判断依 FS 的可见声明，不冒称本席取得了它们的完整原证明。[FS 的来源与缺口记录](PAPER31_QPI_NONUNIT_FITTING_SOURCE_SUPPLEMENT_V1_20260909.md)。

### 5.2 最强包含压力不是“都有 Pascal”

S2 §2 给出的明确比较映射，比术语相似性更强。对 $a+b\le N$，
$$\mathcal T_N(U^aV^b)=(-1)^{N-a-b}\binom{N-b}{a}\tau^b e_a.$$
因为不同 $a$ 的源单项式独立，像就是 $\bigoplus I_{N+1,a}$。乘 $F=U(\tau+V)$ 后的截断经 Pascal 恒等式给
$$\mathcal T_{N+1}m_F=\tau\,\mathrm{sh}\,\mathcal T_N.$$
边界截断项对应的二项式系数为零；本席已核对这点。$I^{**}=R$ 又是常数与 $\tau$ 幂互素的短推论。因此一旦原正规形和全目标识别建立，“格像＋移位＋双对偶”是同一标准计算的三个输出，不是三个独立方法创新。

反方向也不能误判：行内容相同一般不推出整个像为各行内容的直和，源系数独立性在这里由 PM5 提供；任意四组边数据也不等于原源，PM2 提供共享顶点兼容。故剩余不是零：C1 给实际受限连接的完整标记信息，G 给经典局部模型和原几何余核的完整整系数比较。这是可信的对象识别新发现。

### 5.3 与已有论文的实际差额

P18 的所比较结论研究标记 Hénon 边界上的相对 Kähler/Fitting、完成和基变换及泛长度；它并未在这些命题中给原非单位曲面的秩 $n$ 上同调格。Fitting 和基变换方法应扣除，不能把不同模的 Fitting 当相同对象。

P29 的所比较对象是特征零域上 $K[x,y]/(\sigma-1)K[x,y]$。其完整轨道障碍、累加原函数和保次数证明，以及混合进位相位重编码，已经提供“数字编码＋余核结构”方法先例；但这不是当前原四簇 $H^1$，其相位数字不等于本二项式 $p$-进位规则。没有现成源、商和作用兼容同构被提供。

P30 `geom:constants` 在单位 $q,\tau$ 上用节点帧及传播比给边界复形；部分比值明确用 $\tau^{-1}$。UNIT 的底环也反演 $\tau$，环同态不能把单位送到零，所以它的任意基变换不包括现非单位闭点。P30 的 rank-two／`trace:residue` 属于原谱迹和 Frobenius 系数选择，须扣其整数与数字机制，但其模不是当前 $M_n$。上述区别说明现题不是旧稿的同一句重述；不单凭对象不同判定已经达到独立论文门槛。

### 5.4 新意评分理由

最正面的增量是：把旧的有限阶混合现象、条件性目标和未识别格，变成同一个原族上的完整标记递归及其自然算术输出；尤其 C1 不是由 C2/C3 可逆恢复的粗不变量。它应获得实质研究信用。

最强反对意见是：两坏图都归入同一 $F=U(\tau+V)$ 标准局部模型后，主要新算术图景由既有 Taylor 行内容、Lucas 和行列式机制控制；原全局识别虽然认真且必要，所展示的是固定 $q=1$ 族的一套精确计算，尚未显示同等力度的新结构原理。这里不要求每篇论文必须发明一般方法，但现具体发现的概念推进仍偏窄，且强来源的整包包含尚未排除。

据此本席给 **7.0**，与 CD 的 7.0 数值一致但依据为本轮完整阅读和独立扣除，不是复制 CD 的票。OLDCD 的 I05 **6.5／CAUTION** 和最新 CD **7.0／7.0、CAUTION** 原样保留；闭合了数学不意味着必须再加到 7.5。外文访问缺口降低断言“没有先例”的强度，不作为新意加分。

## 6. 独立科学价值：7.2 / 10，FAIL

本候选有一个可以清楚表述的完整问题：原初值曲面跨越非单位时间时，各次反典范上同调如何以整数连接、无扭格及混合特征缺陷组织起来。它不是彼此无关的 C1、C2、C3 三篇拼接；C1 提供结构，C2 给自然可计算投影，C3 把其译成整个基上的理想和域上长度。

其独立价值最强的四点是：

1. 它展示局部化与单个零纤维维数都会丢失的厚度和非分裂信息，现全系数层和实际 $\tau$ 作用保留这些区别。
2. 首次坏素数次数、缺陷消失次数和后续长度都不依赖有限扫描；它们回答同一原族上的准确、可检验结构问题。
3. 首 Fitting 保留高度二非主因子而不只给垂直除子，概念上区分“扭长”与“自然格缺陷”，不把两者混为一谈。
4. 完整标记 Ext 与恢复是比一张理想表更丰富的研究产物；无需伪造其每个值都有独立下游应用，仍可承认这份结构信息的价值。

但完整候选在本固定独立长文标准下仍有不足。低阶非主性、特征长度不同和零时间几何早已在基线中成立；本次最鲜明的后果主要是把同一标准局部机制的影响完整展开。当前包没有展示一种此前无法由该局部模型预见的额外全局几何或动力后果，也没有证明其计算原则可转移到其他原族。后两者不是强制新增的验收条件，而是衡量本固定族发现是否已经足够重要时缺乏的正面支撑。

C1 的完整性支持其作为研究结果保存，但“数据比粗不变量多”本身并不保证独立长文价值；C3 的消费者只使用 C1 的正合列和 C2 的真实作用，这限制了把全部 Ext 信息再计作多项应用的理由。全称量词和证明难度说明结果完整，不自动说明研究影响高。旧投入、文件数、批次还缺第五篇以及未来强 (P) 都不计分。

本席给 **7.2**：高于“孤立低阶算例／仅计算验证”的层级，确有凝聚的结构价值；但在扣去已接受基线和标准局部模型后，尚不足以跨过本次 **7.5** 的独立科学价值门。新意和价值评分可以相关但不是同一门，故后者单独解释并独立判定。

## 7. 完整证明信心：9.2 / 10，PASS

本席未发现需要修改原 C1–C3 声明、缩小量词、增加科学假设或补造证明的新硬数学缺口。这个结论覆盖 PM1–PM11，包括完整 C1 的所有标记关系和恢复，不只是 C3 的短公式；没有沿用“此前接受”来免除当前必要链检查。

信心超过 9.0 的主要理由是核心危险点都有实际可检查的整数接口：几何 cone 真实而非猜测；共享顶点的充分性明确；Ext 呈示有无额外关系的论证；坏图正规形的全 fat-jet 作用明确；局部化自由秩和留数满射分别证明；格坐标的 $\tau$ 因子未丢；专门化 Tor 与取真实像被分开；DET 的归一化及高度二因子已在同对象应用中落实；全素点覆盖和数字递归终止都不是有限数据外推。

未给 10 分的原因是这是跨几何、形式坐标和交换代数的长静态证明链；截断下的指标／符号、恢复的选择相容和未来英文转录仍有通常的人为差错风险。没有形式化证明器核验，未运行新数学实验；后者也不能代替全称证明。GR 的必要原定理及应用已核对，其他作为新意压力的外文全文缺口不等于原证明调用一个未明前提；不能把来源查新不完整机械降成数学错误。

保留风险是范围内的剩余不确定性，不是要求重开已通过且未变的数学阶段。若未来出现具体失败，应定位原主张、前提和失效推理再作最小处理，本报告不预先授予新科学修改权限。

## 8. 正文容量：可信 PASS，存在明显上端风险

评价固定为匿名英文、单栏 11pt `article`、letter、四边 1 inch、标准行距和正常段落。摘要、引言、结论及**全部题目特有必要证明**在正文；参考文献另起页另计。不沿用 P30 的单篇 40 页例外，不移必要证明至附录，不删完整 Ext／恢复，不缩量词、拆篇、灌水、压字距或试写试排。

下面是按实际论证责任估计的自然占用，不按 Markdown／TeX 行数、证明文件数、投入量或旧 PDF 页数换算。三个数分别表示紧凑但完整、通常清楚表达、较充分解释时的预测，不是三个不同科学范围。表中模块已去除重复引入同一四图和同一短列的占用。

| 必要正文模块 | 必须保留的实质 | 低 | 中 | 高 |
|---|---|---:|---:|---:|
| 摘要、问题与最强先例定位、记号和完整主定理 | 原族问题、C1–C3、限制与来源扣除；不能只列标题 | 2.50 | 3.25 | 4.00 |
| PM1 原几何与实际复形 | 八中心及四图、canonical 因子、任意 fat 推前、四节点右逆、cone／基变换 | 3.00 | 3.75 | 4.75 |
| PM2 相邻商和全部核 | 单射、两坏图循环商、共享顶点、整数兼容的充要性和核归纳 | 2.25 | 2.75 | 3.50 |
| PM3 完整 marked Ext 和恢复 | 所有统一关系、呈示充分性、全层非分裂、商提升扣除及精确降次算法 | 2.50 | 3.25 | 4.25 |
| PM4 原留数识别 | $Y/S$、全部边界共同零点、canonical 符号、GR 适用及 Laurent 提升、原满射／秩 | 2.75 | 3.50 | 4.50 |
| PM5 全 fat-jet 正规形和完整格 | 坐标／Jacobian 单位、独立单项式像、好图包含、实际移位、自然双对偶 | 2.00 | 2.50 | 3.25 |
| PM6 原全核单位补基 | 源基中单位三角证明和实际长度一分辨率 | 0.50 | 0.75 | 1.00 |
| PM7 系数层和 Lucas 首现 | gcd 层、参数作用、距离而非赋值和、全部素数首次 | 1.25 | 1.75 | 2.25 |
| PM8 专门化与全特征扭长 | Tor、真实像、原移位指数、蛇形单位满射及长度扣除 | 1.75 | 2.25 | 3.00 |
| PM9 归一化行列式引理 | 实际 $P$、互补子式、所有高度一赋值、自然理想及边界情况 | 2.00 | 2.50 | 3.25 |
| PM10 同对象和全局化 | 前提逐项落实、全部素点和较低 Fitting | 0.50 | 0.75 | 1.00 |
| PM11 所有数字规则 | 消失充要条件、两分支求和、常数项和终止基例 | 1.25 | 1.75 | 2.25 |
| 结论及准确边界 | 已解决与未解决、方法／发现区别；不添加新旁支 | 0.50 | 0.75 | 1.00 |
| **合计** | **同一个完整 C1–C3** | **22.75** | **29.50** | **38.00** |

**为什么存在自然入窗路径。** 各次／各素数责任由统一公式、一个完整四边插值论证、一个带参数的坏图正规形和两个数字分支承担，不需要逐次印出矩阵或逐素数例子。原中心／标架／$F_r,G_r$ 只定义一次，C1 短列只证明一次，PM10 引用本正文已经证明的接口，而不重复 C、G、DET 各自的整段前提。这样压掉的是原材料中的重复陈述，不是必要证明。低到中档都有符合正常论文写法的余地，约 26–30 页的完整写法可信，故给 PASS。

**下穿 22 页风险。** 有熟悉留数和交换代数的读者时，若把一般工具高度压缩、主定理格式紧凑，可能短于本低估计。维持完整 PM1、PM2 的四边充分性、PM3 恢复、PM4 全局识别和 PM8／PM9 的同对象证明，本席认为自然正文不会稳定落在极短的十余页；但 22.75 不是下界，不能靠增加 M3/M4、T3/Pm、旧 UNIT 或样本来补足页数。若真实未来稿少于 22，必须按实际合同判断，不以本预测冒充已达标。

**上穿 30 页风险。** 中档已靠近上限，最容易增长的是 PM1 的完整推前、PM3 恢复步骤、PM4 边界穷尽／符号，以及 PM9 的规范化行列式证明。若这些分别写成独立教学章节，或把检查报告、来源日志和旧旁支复印进正文，38 页的高档很容易出现。即使没有冗余，详尽解释也可能超窗；本席没有保证所有正常写法都在窗内。解决重复叙述是可用的写作组织，但不能通过删掉完整 C1、把证明扔附录或变更排版来兑现预测。

本门不是另设“中位数必须在窗内”；中档在窗内不是充分理由，高档在窗外也不自动否决。PASS 的依据是上面按统一证明实际压缩后的完整自然表达具有可信度，且明确保留必要论证。它不授权现在起草测页，也不能替未来 PDF 实质正文验收。

## 9. 最终合取和不外推事项

本席完整结论为
$$\text{FAIL}_{\rm novelty}\ \land\ \text{FAIL}_{\rm value}\ \land\
\text{PASS}_{\rm proof}\ \land\ \text{PASS}_{\rm capacity}
\quad\Longrightarrow\quad\boxed{\text{FORMAL CANDIDATE CONJUNCTION: FAIL}}.$$

这表示当前完整候选没有取得本席准入；不否定已闭合数学、不删除其产物，也不是要求为“凑到通过”修改分数或默默收缩范围。另一席应由主控按其**完整自身合取**处理，本席没有查看或推测其结果；不跨席拼门、不把两分平均。

仍未覆盖或未获得的事项明确如下：

- 公开来源检索非全球穷尽；Ohm／Hadjirezaei 全文、Perkinson 图及其他受限段落的强包含仍未排除，所有来源分数受此证据边界约束。
- 完整强 (P)、所有 Smith 型、更高 Fitting、一般 $q$、非加法结论及零时间可逆动力未在本票被证明或接受。
- 没有生成／编译英文稿或 PDF，没有实测正文容量，没有执行外部投稿或发布，也没有完成跨论文统一审计。
- M3/M4、固定 T3 和 Pm 已作为基线或旁支读取，不为本次全称证明供给量词，不作为新意或页数填充。
- 当前无须靠重开已通过不变阶段来解释前两门失败；本票的未过是新意和独立价值判断，不是可由格式化、增加脚本或重跑样本消除的技术故障。

本报告在提交前由本席全文读回并核对直接本地引用及输入身份。提交后冻结，不再修改自己的评分或报告；必要事实澄清不自动产生第二张或更高票。
