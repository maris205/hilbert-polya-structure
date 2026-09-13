# Paper31 闭合非单位时间完整候选：第二席正式完整审查 V1

任务日期：2026-09-10 UTC。审查席：`/root/p31_qpi_nonunit_closed_formal_v1_r2`。
状态：`FORMAL_COMPLETE_REVIEW / OWN_CONJUNCTION_FAIL / NO_ADMISSION`。
`route_applicability: NOT_APPLICABLE`。

## 1. 结论

我不建议这份固定完整候选按当前四门进入 Paper31 正式论文阶段。
理由不是发现了新的硬数学缺口，也不是认为完整证明只能写成短注；
而是在扣除实际最强先例及组合内既有结果后，本席的新意和独立科学价值判断仍低于各自的 7.5 门槛。

| 本席完整评价 | 分数／判定 | 固定门槛 | 本席结果 |
|---|---:|---:|---|
| 新意 | 7.2/10 | ≥7.5 | FAIL |
| 独立科学价值 | 7.3/10 | ≥7.5 | FAIL |
| 完整证明信心 | 9.3/10 | ≥9 | PASS |
| 自然完整实质正文容量 | PASS；预测低／中／高为 21.5／26.8／34.0 页 | 自然 22–30 页可信 | PASS |
| 本席四门合取 | `FAIL ∧ FAIL ∧ PASS ∧ PASS` | 四门同时通过 | **FAIL** |

容量的 PASS 是完整证明自然组织在约 25–29 页的可信判断，不是实测、保证或额外的中心值门。
低、高情景越窗风险见 §7。没有把低于门槛的分数四舍五入，没有与另一席平均或拼接。
这张正式候选票不撤销原数学的既有接受，也不改变冻结的旧失败、旧评分或候选范围。

## 2. 身份、权限与实际读取

我是本轮新上下文非作者第二席，未编写 C1/G/C/DET/A、来源盘点、组合比较或本次 CD 报告。
本轮没有读取第一席报告、消息或私有记录，没有与第一席通信、校准或再委派投票。
共同包包含历史公开评分，因此不称对历史分数盲审。
实际采用可用 Codex 独立审查上下文，并使用 `research-review` 的 xhigh 审查纪律、证据锚定和最强反对意见要求。
指定 GPT-5.4 MCP 未运行；`cross_model_verification: NOT_PERFORMED`，`score_calibration: NOT_CALIBRATED`。
本件不称人类审稿、形式化验证或期刊接受概率预测。

本人先全文读取 `docs/WORKFLOW.md` 1–39 和指定的
`/root/autodl-tmp/.codex/skills/skills-codex/research-review/SKILL.md` 1–102，
再按共同 manifest 逐件阅读。技能影响是保持完整四门及方法／发现分拆，不产生外部评审、实验或写稿权限。
唯一写入对象是本报告；没有修改共同输入、科学源、旧票、锁、索引或项目，没有生成稿件/PDF、试排或运行数学脚本。

### 2.1 共同输入身份与本人覆盖

以下 SHA-256 均绑定整文件。本人实际核对 46 件被绑定对象的字节数、SHA 以及 45 份文本行数，全部与 manifest 一致；
manifest 自身 SHA 亦与派发身份一致。PDF 的文本行数不作为 PDF 身份或阅读凭证。
读取与字节验明分开：32 份必读文本及 manifest 均实际 FULL 至 EOF；13 份旧基线明确为 PARTIAL；GR 为指定六页完整读取。
首次显示截断的部分已补读，不以哈希、清单、作者摘要或既有检查者的阅读标签替代本人阅读。

| ID／实际文件链接 | 本人实际覆盖 | 整文件 SHA-256 |
|---|---|---|
| [MAN][MAN] | FULL 1–193 | `2574134d896530e097bbebc1e9e855fea2f03aeabcba337ac98e8d2fb1404486` |
| [BRIEF][BRIEF] | FULL 1–205 | `568b4b829b60c8dc6ce5129a984ae7e593db22d2bad9ff2e6ebebfbda63063fb` |
| [MAP][MAP] | FULL 1–281 | `ca7cb9068456288783cd2c06874d5cc8656035e9f3f6888c39ecacdff200701e` |
| [PRE][PRE] | FULL 1–87 | `0f27d8c43b88a04052d22f349861f56a96925f271529a979eb7134b3db1c5ef5` |
| [INV][INV] | FULL 1–144 | `d607eec2d33daf89210911a9965ed9498f1ef10af83d8faa3ecb7cd04a76794c` |
| [IC1][IC1] | FULL 1–177 | `ca5fe99e671cedaf7ae5f92115a5fe346eea648390ed1dbc0cef2a17fabb19a2` |
| [IG][IG] | FULL 1–185 | `6b75b13ee4421fd55b2ed93e11cc89945d53d7eed5952afb10c62531baf38801` |
| [PA][PA] | FULL 1–83 | `07b658e0e6a07fece0db86d85face58a852646760a6e8d185f7715800dd2ae5f` |
| [MATH][MATH] | FULL 1–117 | `a0d1c880f45462721f78366234d0d5796d04f95c46428c05caacdb90ce75fdd3` |
| [PB][PB] | FULL 1–64 | `5bfb95183689687b53fd1656896b64847605c362d260b1b68e999d7cee4b28ee` |
| [CD][CD] | FULL 1–236 | `4f3f186d7e2c2b4dc8d1d733358d6c849d03c6ba3542b287d8207a4c5bb62737` |
| [BASE][BASE] | FULL 1–96 | `3a3d3444e5237af5dab971d488fa1d513d5fcc4bdb32d3c4cd1a008e0d19ee59` |
| [JET][JET] | FULL 1–358 | `0acbfc4866b0cf944c84f88c8db3e7c535fdbff366ead4f166c3d8f01e3e2005` |
| [JC][JC] | FULL 1–327 | `b3b68ac29e95c2db273ad83a528c131a4fdca63a94e6fb7e5abc8235eede4eb7` |
| [EXT][EXT] | FULL 1–318 | `9c87c8570065deba6dd14e33e7a27382a2d3d6ba34f01a883ee7faff92fb60d0` |
| [EC][EC] | FULL 1–179 | `12b9ce4f6b6e485c8457478821eb3c2cc8afca74807aa98daf17240b586d4370` |
| [G][G] | FULL 1–429 | `d872b731423107412631a9834b639229b2578e0084afef752c6a94d6e90f7c6a` |
| [GC][GC] | FULL 1–262 | `f1ce1a0f70ac536a38dcfcfdac064e3468615807f4ba820c6befae6d5f7121b6` |
| [C][C] | FULL 1–176 | `25bb87a365eaf5a9d37c192a47f99d454007aa14e265668c34465cc3e2154e10` |
| [DET][DET] | FULL 1–297 | `913e701986e540a59476a9f64bf890bf3bbdc300596ef9db9514ebe784dcb250` |
| [TC][TC] | FULL 1–193 | `076e030cdb20cee50ec9cba9578146c61641fdbbb68c3db9839cc94dd8b2188b` |
| [A][A] | FULL 1–180 | `f214e2e14d065e778d752f15855995d0a66df4c115d7aa72e14af5695e153260` |
| [AC][AC] | FULL 1–180 | `6aa3dfbec7172da44b328f8baef318488e56a8150536cf0bfdd0eaddf28d61a3` |
| [S13][S13] | FULL 1–181 | `afc7c9b54044c25df82cfcaad62563e4d53f6c810be2eb785beb51f9eb7f294a` |
| [S2][S2] | FULL 1–228 | `01bc654082a21736c7af0e7494382d7f321d1c1b2b23492f6782d27c305b3d94` |
| [FS][FS] | FULL 1–102 | `60e972d287f5cf3d234826acd3caa4532f62e50a6578415c6942f4c0a19c2f36` |
| [PD][PD] | FULL 1–221 | `766bbefd7df8918759101a543ff9f0635289cc77e24c5a18364ed065770eec7f` |
| [PORT][PORT] | FULL 1–121 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| [LIMIT][LIMIT] | FULL 1–121 | `bbcc282cad6a78da92500b21ee91ed892f1152bbfc339f2ad860468c27af593c` |
| [NU][NU] | FULL 1–146 | `cf438f313d34c70f8dc7d775894524164460ba8a69d16c01c712a174a8200de0` |
| [INT][INT] | FULL 1–162 | `1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af` |
| [M4][M4] | FULL 1–127 | `1161e63f35fa07ac401d9fc21fe58167f2cad39b0a810e37638b663f3ed8f663` |
| [M4C][M4C] | FULL 1–149 | `6bef85adcd0708abd00af14704413645351e803aaa03d0aa94a77d46f46286f6` |
| [OLDCD][OLDCD] | PARTIAL 1–109、160–174、187–216 | `4b1d3fdbb51f7b1e1250dfea393133ff3b409bc2bc5e130f7d8b55f703ef7fd4` |
| [P18][P18] | PARTIAL 525–618、1053–1295 | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` |
| [P29I][P29I] | PARTIAL 19–39 | `7a93eba84684809c101dd6d4500c0c97702d816da7d3821603b2ac79805289d8` |
| [P293][P293] | PARTIAL 1–244 | `e8e5410a2df50f5591da6a4eacaebbe350fad7c4c179911d39f259fc176e4bf1` |
| [P294][P294] | PARTIAL 53–100 | `e62e02e9511c77e2a739cde7d36e659cf9ff666f536af5346dd9d0d7c6a93884` |
| [P302][P302] | PARTIAL 1–29、228–338；1–29 为同文件补读中心定义 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| [P305][P305] | PARTIAL 84–161 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |
| [UNIT][UNIT] | PARTIAL 1–108 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| [FIRST][FIRST] | PARTIAL 7–64、84–114、171–219 | `ef975ded12f7263842e208f6eda87df213e210e9dbf7ef3c08fbd8724fe6270d` |
| [FIBRE][FIBRE] | PARTIAL 7–59 | `dd9cc251bed71eeca5e0063b8dd67c83d820cbedd49dcec43322001840e6b620` |
| [FC][FC] | PARTIAL 1–68 | `cc21bf738c64136b6f2842a1ba60e7407208126feed6566b5ddef6802fa5f5bc` |
| [M3][M3] | PARTIAL 1–64、193–252 | `fe9f9f1c70b20eea4d587d57959eafd9dd8ab42cc128119c32ac6714c77470e8` |
| [W][W] | PARTIAL 1–107、199–242、252–279 | `360741298e0a3478586031eb7ef19b18e0a36ce899b78c856cd3473c8671249a` |
| [GR][GR] | `PDF_PARTIAL_REQUIRED_RANGE_COMPLETE`：PDF 48–53 页，印刷 368–373 页，文本及六张实际页面均读 | `517692faba4fb281bb78b2f129fde7dabe6a3625e5dcb4f75cfdad37fc521fb1` |

没有把任一 PARTIAL 文件冒称全文重审。GR 的全文为 70 页；我没有读取其余 64 页。
GR 的公开网页截图尝试未返回可直接辨认的页面图像；随后用同 SHA 本地原 PDF 的实际六页渲染补足视觉读取，未写临时摘抄或替代 PDF。
没有消费清单外本地科学文件；各来源报告间接引用的旧证明不因出现在报告中便递归成为本席输入。

### 2.2 本席额外公开一手核对和未覆盖来源

本轮只作定向原文核对，不另起无界查新。以下是我的阅读范围，不继承来源席的 FULL 标签。
网页行号是此次显示的定位辅助，不替代版本身份。

| 一手来源 | 本席实际阅读 | 允许的比较结论 |
|---|---|---|
| [Callan，arXiv:math/0209356v1][CALLAN] | 数学正文 §§1–5，网页 34–113，含三定理及其证明；另核元数据与参考文献 | 完整 Pascal 方阵及其差分幂的整数等价／模 p Jordan 机制已知；原受限共享源仍须单独识别 |
| [Maakestad，arXiv:math/0402279v4][MAAKESTAD] | PARTIAL：Thm 3.1 与负二项证明，Thm 3.2 声明及证明尾；§4 从任意环设置到 Thm 4.1 全证明；随后 4.2 等邻段；§5 特征零设置、Lemma 5.1 与 Thm 5.2 声明 | 任意底环的主部转换矩阵、整数线性方程和单位条件早已存在；特征零分裂不能未经检验就作整数分裂 |
| [Kyomuhangi–Marangone–Raicu–Reed，arXiv:2411.13450v1][KMRR] | PARTIAL：引言；§2 的局部上同调模型 (2.7)–(2.8)；§3 设置、Thm 3.2 四种情形全部声明；Lemma 3.4 全证明及邻段；未审完整递推证明 | 已有主部的全次数正特征递推，且不只有维数表：存在双分次乘法及显式负二项局部基接口 |
| [Griffiths 1976 机构原文][GRWEB] | 本地 GR 指定六页；公开入口作身份核对 | §3 局部留数与紧复流形定理 (3.7) 的完整适用条件、Stokes 证明；不声称阅读全文 |

Callan 与 KMRR 的所读 HTML 题头另显示 2026-08-24；不将该排版显示日期冒充各 arXiv 版本的首发日期，亦未因此声称核对了更新版本。
Maakestad 是指定 v4 入口，不把它当 2026 年新成果。

[S13][S13]、[S2][S2]、[FS][FS] 的作者阅读记录和检索失败均完整保留，但不是我的外文全文阅读。
特别是 Ohm 2008 的全文缺口、Hadjirezaei 2026 仅官方预览定理的范围、2013 UFD 文献的摘要层限制，
以及 Perkinson 1996 的关键图未核、Guardo 2010 后段访问缺口，均没有在本席转化成“已排除所有先例”。
2025 principal-parts 计算接口、Rowland 的数字分布、Galuppi 的碰撞工作、toric residue 文献及 Stacks 的其他条目，
本席的具体比较证据来自已经 FULL 读取的来源报告；不声称又完成它们的原文全文审计。
没有联系作者、付费、绕过认证或上传任何输入。

## 3. 被评价的完整数学对象

对象严格是原四簇 $1+2+3+2$ 截面吹起在 $q=1$、$R=\mathbb Z[\tau]$ 上的曲面 $S$，
$\mathscr L=\omega_{S/R}^{-1}$，$M_n=H^1(S,\mathscr L^n)$。
$T_n=\ker(M_n\to M_n[1/\tau])$、$L_n=M_n/T_n$、$E_n=L_n^{**}/L_n$。
留数计算在四次 node blowup 后的中间曲面 $Y$ 上，不能与最终 $S$ 混同。
原 $J_n:V_n\to W_n$ 及其受限二维单项式源、四个 fat-jet 截断均保留。[BRIEF §§2–5][BRIEF]

我按三个完整输出评价，而非只看它们最后的数值式：

1. C1：真实 $s_0=xy$ 链映射、整个 $H^0$ 核、所有次数的相邻短列，所有标记循环商分量的 Ext 类、每个 $n\ge1$ 的非分裂及整数恢复；$n=0$ 是单独基例。
   对 $m=n+1-a$，必须保留实际关系
   $\tau^m y_{r,a}^{(n+1)}=\iota_n(e_{r,a}^{(n)})$ 及
   $e_{r,a}^{(n)}=[u^{a-1}\sum_{b=0}^{m-1}(-1)^b\tau^{m-1-b}v^b]_{r,n}$，
   不能以“商模已知”代替这些标记关系。
2. C2：由原几何构造 $\rho_n$，识别整个 $M_n[1/\tau]$、整数像和自然双对偶。
   写 $N=n-1$，$I_{n,a}=(\binom{N-b}{a}\tau^b:0\le b\le N-a)$，
   则 $\rho_n(M_n)=\tau^{-n}\bigoplus_a I_{n,a}$，$E_n=\bigoplus_aR/I_{n,a}$。
   标准化坐标中的原映射是 $\tau$ 倍右移，完整系数层连同 $\tau$ 作用都是输出。
3. C3：同一个原 $M_n$ 的全局首个非零 Fitting 理想
   $\operatorname{Fitt}_n(M_n)=\tau^{B_n}\prod_aI_{n,a}$、$j<n$ 的消失、任意域上的实际扭长 $B_n$ 或 $B_n+D_n(p)$，
   以及首现 $n=p+1$、全次数零缺陷判别和终止数字递推。

其中 $B_n=\sum_{j=1}^{n-1}j^2$；$D_n(p)$ 是首个模 p 非零系数位置之和，不是 $E_n$ 的全部 p-群阶。
必须保留 $n=0,1$ 和 $p=2$：$M_0=T_0=L_0=E_0=0$，但 $V_0=H^0(S,\mathcal O_S)=R$。
完整强 (P)、所有 Smith 型、更高 Fitting、一般 q、非加法结构、零时间可逆动力均不在票内。
没有把完整标记递推误称为典范块分类，也没有为 $M_n$ 虚构 $R[u,v]$-模结构。

## 4. 完整证明审查：PM1–PM11 与同对象前提

下表是实际证明责任核对，不把十一模块计为十一项创新或十一张独立证据。
MAP、IC1、IG 用于定位；接受判断来自实际 JET/EXT/G/C/DET/A 及其指定必要输入的阅读。

| 模块 | 原证明与消费者 | 本席核对的实质；判断 |
|---|---|---|
| PM1 | JET Steps 1–4；支撑 C1–C3 | 不相交原簇可重排为四 node 吹起加末四点；任意底环的吹起推前、canonical Jacobian、四次 toric 评价的单位右逆、$V_n$ 与最终评价 cone 共同证明这是实际 $R\Gamma$，不是只算截面核。PASS |
| PM2 | EXT Steps 1–5；C1、G 的逆 τ 秩及 C 的相邻商 | 靶乘 $u(1+v)$ 或 $u(\tau+v)$ 在原整数截断间确实单射；商的好／坏图数据与共享四边源一起计算；兼容条件有充分性插值，$s_1^{n+1}$ 真正提升商核。PASS |
| PM3 | EXT Steps 6–8；完整 C1 的独立结构输出 | 每个标记 Ext 的实际 jet 代表、模 $\tau^mM_n$ 的完整类、逐级关系的完备性、每个 $n\ge1$ 的非分裂及严格降次数恢复均保留；$n=0$ 单独处理。并未因为 C3 不使用每个类值而删去它们。PASS |
| PM4 | G Steps 1–4、JET/EXT、GR；C2 的原对象识别 | 原 Y 的边界面项和顶点排除给全部四个共同零点；四图 canonical 符号、紧曲面留数适用、整系数恒等式回传、逆 τ 全秩和第三图实际满射共同给 $\rho_n$。PASS |
| PM5 | G Steps 5–8；C2、C 的实际格及移位、DET 的自然归一化 | 全 fat-jet 的整数形式坐标变换及 Jacobian 单位，不只作用于源；精确坏图像、好图包含、原乘法移位、$I^{**}=R$ 与有限自然缺陷。PASS |
| PM6 | A Step 1、EXT 全核；DET 的实际分辨率 | $s_0^{n-k}s_1^k$ 的最高 $y$ 项构成原受限源中的单位三角 minor；已知其为整个核后，删去这 $n+1$ 列才获得长度一自由分辨率。旧 W3 单独不够。PASS |
| PM7 | C Steps 1–3；C2 全系数层、C3 的数字参数 | 系数理想的逐层最小 p-赋值、加法直和与相邻 $\tau$ 投影；首个单位位置的 Lucas 描述及 $n=p+1$ 首现。没有把加法分解误作 $A_p$-模对角分解。PASS |
| PM8 | C Steps 4–6、A 的 H1–H3 匹配；C3 全特征扭长 | 真实相邻商的整数 p 无扭给 Tor 消失；先求专门化原模到 Laurent 空间的实际像，再算移位格指数，蛇形引理扣除指数后求扭长。PASS |
| PM9 | DET 当前完整归一化版本；首个 Fitting | 实际 pd≤1 呈示、整个逆 τ 开集自由、自然 $L^{**}$，共同进入互补子式论证；得到等式的是分式理想而非仅其高度一除子。历史抽象理想归一化错误没有重现。PASS |
| PM10 | A Steps 2–3；全局 C3a | 同一个原 $M_n$ 同时满足 C/DET 的前提；高度二 $(p,\tau)$、高度一 $(\tau)$ 及不含 τ 的全部素点共同给全局理想等式；不是只检查有限素数或 DVR。PASS |
| PM11 | A Steps 4–5、C；C3c–d | 零缺陷的双向数字判别与局部自由性等价；按最低位分情形得到全部长度缺陷递推，$h=0$ 及边界均有基例，递归自变量严格下降。PASS |

### 4.1 为什么实际 cone 和完整标记扩张可信

JET 的关键不是把八个消失条件写在纸上，而是先给任意基环的
$Rb_*\mathcal O(-nE)=\mathcal I^n[0]$，再证明前四次 toric 条件真的逐次满射。
各被截掉的单项式区有单位系数右逆，故后四点的 jet 评价 cone 的余核才是原 $H^1$。
其任意基变换声明适用于这个有限自由复形；本审查未把它偷换成以后每一条短列都自动保正合。[JET Steps 1–4][JET]

EXT 保留四条边的共享顶点。兼容泛函并非只必要：边多项式的插值允许自由选取相应系数，给出反向提升。
由 $s_1^{n+1}$ 提升完整商核，才同时得到整个截面核和 $M_n\hookrightarrow M_{n+1}$。
标记类的公式来自实际靶中的等式，不是从商模类型猜 Ext；扩张的生成关系无遗漏又由短列的正合性验证。
恢复先扣指定循环及自由商坐标的提升，再处理相容四边，最后作原乘法的确切整数除法，避免对尚不在像中的 jet 强行相除。[EXT Steps 3–8][EXT]

### 4.2 留数的原几何接口没有被标准工具名称掩盖

我检查了 G 用于排除额外共同零点的面与顶点分析：在 $\tau\ne0$ 上有关顶点系数为单位，
四条相关边的二项式零点正是 $1,\tau,\tau,1$，分别处在原不同分量。
canonical 因子 $(-1,1,-1,-1)$ 与留数求和采用的符号对应，不能任意选成四个同号。

GR 定理 (3.7) 要求紧复流形及合适的有限共同极点集；G 先对非零复数时间的光滑射影 $Y$ 应用它。
分母对应 $(a+1)\operatorname{div}(s_0)$ 和 $(n-a)\operatorname{div}(s_1)$，两者总次数与 numerator 的 canonical 权重相配。
所用的“总留数为零”方向不需要把后来逆命题 (3.8) 的正性条件塞入这里。
局部公式为整系数 Laurent 恒等式，因而从复参数恒等式回到原 $R[1/\tau]$；并非在正特征中无说明地搬用复分析。
第三图给每一坐标的实际 jet 原像，结合 EXT 提供的整个逆 τ 自由秩 n，排除了“仅函数域同构”的缺口。[G Steps 1–4][G]、[GR pp.368–373][GR]

坏图的 $\lambda=1+u^2(u-1)(\tau+v)$ 给 $U=u/\lambda$、
$V=v+u^2(u-1)(\tau+v)^2$。这在完整截断靶上是线性项为恒等的形式自同构，Jacobian 为单位；
于是 $F=U(\tau+V)$、$G=V$ 的单项式计算确能遍历全部靶，而非一个未证明足够大的源子集。
好图像先被纳入坏图的精确像，才可断言整格等式。
$\Psi_n=(-1)^{n-1}\tau^n\rho_{n,0}$ 以及标准化后多出的 $\tau$ 因子均已核对；移位不靠类比猜出。[G Steps 5–8][G]

### 4.3 混合特征、Fitting 和自然双对偶是同一条链

$A_p/I_{n,a}A_p$ 的系数层 $e_b$ 给的是完整加法 p-群及参数作用；
$d_p(N,a)$ 则是首次出现模 p 单位系数的位置。
把二者混用会错误地把完整 p-群阶与特征 p 的额外 τ 长度当作同一不变量；当前证明没有这样做。
专门化时使用真实相邻商无整数 p 扭的 Tor 消失，随后取实际像格
$\bigoplus_a\tau^{-n+d_p(N,a)}k[[\tau]]$，
并由真实移位得到指数。它不要求“原扭子专门化等于专门化后的扭子”，也不预设“无扭商与非平坦基变换交换”。[C Steps 1–6][C]

DET 的旧归一化风险是真风险：抽象 $L\simeq\bigoplus I_a$ 本身不足以指定嵌入，$A\simeq(p)$ 就说明这种写法可掺入假因子。
当前 G 给每个 $I_{n,a}$ 的自然双对偶准确为 $R$：首项是非零整数、末项为 τ 幂，两者在 UFD 中无公共非单位因子。
A 又给原呈示的整个核及单位补基；DET 的互补子式于是恢复完整首个理想，保留 $(p,\tau)$ 的高度二信息。
只算特征零总扭长 $B_n$ 或高度一赋值绝不能替代这个步骤。[DET 当前引理及修正说明][DET]、[A Steps 1–3][A]

数字部分的退出判据也不是只在 $n\le p$ 检查：
$D_n(p)=0\iff n/p^{v_p(n)}<p$，其反向使用有缺口的低位构造违反数字支配的 a。
递推在 $N=ph+r$ 上保留两类末位，$H_p(-1)=0$、$Z_p(0)=1$ 并处理 $h=0$，所以覆盖所有次数。[A Steps 4–5][A]

结论：在规定静态完整阅读范围内，未发现需要改命题、增假设、补新的桥或改科学对象的硬缺口。
证明信心 **9.3/10** 是针对这份完整链，而非把既有 PASS 票计数后继承。
剩余不确定性主要是未形式化检查和未来长文转录风险；数学置信分不等于零错误保证或 PDF 验收。

## 5. 新意：真实差额及最强包含压力

### 5.1 组合内必须先扣除的内容

| 既有结果 | 本席原文核对后扣除的部分 | 当前候选真正不同的对象 |
|---|---|---|
| Paper18 | 相对 Kähler 微分的 Fitting 基变换、完成坐标、标量边界泛点长度都是既有；保留其简单标记与 Cartier 范围 | 不能据此取得整数反典范 $H^1$ 的高度二格缺陷与全次数 Ext |
| Paper29 | 特征零向量空间余核、混合进位数字基、有限轨道障碍与保次数原函数已存在 | 其底环、差分算子与普通次数过滤都不是原四簇的 $J_n$；“数字”一词不供应 Lucas 模 p 结论 |
| Paper30 / UNIT | 原八中心、单位底环的全部反典范幂上同调和标量分解、既有 trace 数字系数机制均扣除 | 单位 τ 环不能令 τ=0；原 node 传播的逆 τ 公式不是非单位扩张计算 |
| 非单位已接受基线 | 首层、全次数实际 jet 呈示、零时间全 n 维数、二阶、三阶混合块与 $\tau^5(2,\tau)$ 均扣除；M4 原整数块亦扣除 | 现在多出完整相邻标记系统、原留数整数格、全部缺陷及同对象全局/全特征消费者 |

Paper18–30 的不同底环不是“绝对不可能包含”的证明；上述结论是对所比较命题实际对象和映射的核对。
零时间 $h^1=n(n+1)/2$ 不是混合特征 τ 扭长。
M3/M4、D05 的固定低阶拉回/推出实例及指定 P 旁支没有另获新意或容量信用。

### 5.2 方法与发现必须分开

| 完整输出 | 方法差额 | 发现差额及限制 |
|---|---|---|
| C1 | 中低：短正合列、边插值与 Ext 代表计算本身是标准代数 | 中高：原受限四簇的全部标记类和整数恢复确已算出，超出旧等规模矩阵重写；但不是通用分类或新的 Ext 理论 |
| C2 | 低：留数定理、形式逆坐标、负二项展开、双对偶是标准工具 | 中高：原余核到这个整数格的完整识别有实质内容；识别后的抽象格、移位与自然缺陷明显受已有主部/Taylor 机制压缩 |
| C3 | 低：系数理想、Lucas/Fine 数字、Tor/蛇形、互补子式均已有 | 中：给原同一个模的完整首个 Fitting、各特征长度与局部自由性规则；它们是统一消费者，不是若干独立新方法 |

本席最强反对意见是：这是一次做得完整的固定族算术识别与计算，但是否已经形成足够独立的研究贡献，
不能由“每个步骤都必要”“所有 n 和 p”或“比逐域维数精细”自动推出。

这个压力可以具体化，而不只是列标准工具名称。
[S2][S2] 已核出的抽象 Taylor 映射
$$\mathcal T_N(U^aV^b)=(-1)^{N-a-b}\binom{N-b}{a}\tau^b e_a\qquad(a+b\le N)$$
逐行独立，像就是 $\bigoplus_aI_{n,a}$；其与乘 $U(\tau+V)$ 的兼容性已经把标准化 τ 右移编码进去。
因此，完成 G 的原几何正规形后，不能再把同一个抽象像公式、双对偶、有限缺陷及数字推论分别宣称为新机制。
真正剩余的是到这个标准对象的保信息识别，以及 C1 的原共享源标记扩张。

外部压力也不是只有 Callan 的完整方阵。
Maakestad 已有任意环主部矩阵和单位判据；KMRR 的正特征结果已有全次数递推和双分次局部上同调乘法接口。
只说“他们在域上，我们在整数环上”，不足以保证识别工作很深。
另一方面，本轮所读原文和共享来源报告尚未给出一个同时匹配原 $V_n$、四簇商、截断、τ 作用及 $s_0$ 的已发表比较定理。
我没有断言候选已被某一条定理直接包含，也没有把未找到该比较当作高新意证书。[Maakestad][MAAKESTAD]、[KMRR][KMRR]

[FS][FS] 指出的排除范围同样必须收窄：Ohm 的主/可逆首个 Fitting 情形不能直接覆盖这里的非主理想；
Hadjirezaei 预览中需要 primary 高度一理想的那一条命题，不能直接用于
本文首现处的 $\tau^{B_{p+1}}(p,\tau)^{p-1}$，因为后者存在高度二耦合且不是所需 primary 理想。
这仅排除该特定适用方式，不是排除整篇论文、所有既有行列式公式或一切 UFD 先例。
互补子式本身仍属标准工具；精确自然归一化和本对象前提核对才是这里的应用责任。

### 5.3 独立新意分

最新 CD 的 **7.0/7.0、CAUTION** 与旧 I05 的 **6.5、CAUTION** 原样保留，未回写或要求提分。
相较旧 I05 时尚未展示的连接，本次完整标记类、恢复及原格识别确已存在；不能仍把它评价为“只得到新矩阵”。
但传统主部、留数和数字机制的压缩压力也变得更具体，不能因为桥已经补齐就把方法新意升级为新理论。

综合实际剩余，本席新意为 **7.2/10，FAIL**。
这个分数肯定了非平凡对象识别，却仍未达到固定 7.5 的独立长文新意门。
它不是旧分的平均，也不是以相同关键词、访问失败或没有反例作证明。

## 6. 独立科学价值

这份完整问题有真实价值，最有说服力的不是定理数量，而是如下两点。

第一，同一整数族中，域上纤维维数可以完全掩盖高度二非自由性和额外厚度。
原留数格、完整 $E_n$ 与全局 Fitting 给出可检查的区别；所有 n 的局部自由性判别说明障碍不是仅在首现之后单调累积。
这比再列几行 Smith 数值或重复三阶非主例子更有解释力。

第二，C1 不只提供末端不变量：它保留指定原截面诱导的标记扩张及恢复过程。
对这个固定整数几何对象，这确是能够重建信息的结构结果，不应因 C3 没逐个消费标记值而删掉。

限制也很具体。
格识别一旦完成，主要算术输出集中为一个标准二项系数对象的消费者；它们没有各自独立的新科学动机。
完整 C1 所保存的精细标记，在当前候选中主要仍以自身结构输出结束；不应虚构 trace、谱理论、一般 q 或可逆零时间动力作为额外应用。
当前固定切片的识别虽然细致，但现有材料尚不足以表明其解释力超出了一个专门族的完整算术计算，
达到本批次设定的高独立论文门槛。

这不是新加“必须一般 q”“必须强 (P)”或“必须新算其他族”的硬门，也不要求扩大已锁命题才能算正确。
固定族论文可以达到 7.5；本席只是认为这份已完成结果在当前先例压力和可见消费者下尚未达到。
没有用缺第五篇、投入时间、文档数量或未来未做的工作抬分。

本席独立科学价值为 **7.3/10，FAIL**。
保留为已接受的完整算术结构成果是合理的；以本张票直接授予当前 Paper31 正式论文准入则不合理。

## 7. 完整正文自然容量

固定合同：匿名英文、单栏 11pt `article`、letter、四边 1 inch、标准行距及正常段落；
摘要、引言、结论和全部题目特有必要证明在正文，参考文献另起页另计。
没有试写、试排、改字号边距行距、转移必要证明到附录、拆篇、缩量词或借用 Paper30 的 40 页例外。

下表根据数学证明责任和合理叙述密度估计，不按原文件数、源码行数、投入量或旧 PDF 页数换算。
正文中共用一套原对象、记号及相邻图；各独立备忘录重复的定义和结论不重复计页，实际证明步骤均保留。
一般标准工具准确陈述假设和应用，不把它们所引用的整篇外文证明搬入正文；题目特有的所有检查仍计入。

| 实际必要正文模块 | 低 | 中 | 高 | 容量依据与不能删去的内容 |
|---|---:|---:|---:|---|
| 摘要、动机、对象、完整主定理及范围 | 2.7 | 3.2 | 3.8 | 三个输出、真实对象与既有结果差额；避免把完整 Ext 与系数作用藏在术语中 |
| PM1：原曲面到实际 jet cone | 3.0 | 3.5 | 4.4 | 吹起/反典范引理、四 node 单位右逆、受限源和秩、末四点原标架、cone 与任意基变换 |
| PM2：实际相邻商及完整核 | 2.4 | 2.9 | 3.7 | 好坏靶商、四边共享顶点、兼容条件的双向插值、真实商核提升及短列 |
| PM3：全部标记 Ext、非分裂、恢复 | 1.8 | 2.3 | 3.0 | 类公式和关系完备性、每个 $n\ge1$ 的非分裂、零次基例、先扣提升再确切除法的恢复步骤 |
| PM4：原留数与逆 τ 余核 | 3.1 | 3.7 | 4.7 | Y/S 区别、边/顶点穷尽、四图和 canonical 符号、GR 适用、Laurent 回传、第三图满射与全秩 |
| PM5：完整整数正规形、格、原移位、双对偶 | 2.0 | 2.6 | 3.3 | 全靶形式逆及 Jacobian、精确二项像、好图包含、两种标准化、自然缺陷 |
| PM7：完整系数层及首现 | 1.1 | 1.5 | 1.9 | 系数理想和 τ 作用、Lucas 位置、任意素数首现；不是只写模 p 维数 |
| PM8：实际专门化像和扭长 | 1.5 | 2.0 | 2.6 | Tor、格像、移位指数、蛇形长度差及求和，同对象前提逐项说明 |
| PM6/PM9/PM10：原分辨率、完整首个 Fitting、全局化 | 2.1 | 2.7 | 3.5 | 整个核单位补基、归一化互补子式证明、高度一和高度二区别、全部素点覆盖 |
| PM11：全次数零缺陷和终止数字递推 | 1.5 | 2.0 | 2.6 | 双向数字判别、局部自由性、两类末位求和、边界与终止 |
| 简短结论与准确限制 | 0.3 | 0.4 | 0.5 | 不再添加未证应用或额外低阶材料 |
| 合计（参考文献不计） | **21.5** | **26.8** | **34.0** | 情景预测，不是实测或严格上下界 |

**本席容量判定：PASS。** 依据是完整四边插值、标记关系/恢复、四图留数识别以及专门化/行列式两条算术链，
存在约 25–29 页的自然连贯正文组织，不必增添未消费旁支或填充低阶实例。
这不是仅因为表的中值落窗；即使不用“中值必须落窗”这种未授权门，也能指出每一页区间所承担的完整实质证明。
C1 的精细 Ext 全部保留，JET 的旧而必要几何仍完整计入；“旧结果不算新意”不意味着它可以从必要正文证明中消失。

低端 21.5 页说明极紧叙述有下穿 22 页风险，不能靠背景堆积或重复命题补齐。
不过完整插值的充分性、恢复的输入处理、canonical/GR 假设和非平坦基变换区分，都有正常展开的实质空间。
高端 34.0 页说明若把各桥各自重新设置记号、逐图完全分散展示或把一般工具讲成独立教程，可能超出 30 页；
高端风险并未被一个“以后可压缩”的空许诺消除，而是在表中明确保留。
目前共享记号与共同图式足以支持窗内组织，但未来稿件仍需实际完整性及 PDF 验收；本票不预授那两项通过。

## 8. 交付和未覆盖边界

本席已本人完成四门；新意失败没有导致证明或容量部分提前停止。
未发现新的硬数学缺口，因此没有提出原数学必须返修项、修改任何原命题或新造替代证明。
来源包含范围未穷尽，精确先例比较仍受 §2.2 的实际读取与访问缺口限制；这不被解释为新意正证据。
所有结论仅针对上述固定 C1–C3，不触及强 (P)、全 Smith、一般 q 或完整动力学分类。

本报告提交前全文读回，直接本地引用与共同输入身份核对；最终行数和 SHA 在交付消息给出。
提交后冻结本报告，不因另一席结果或合取需要修改分数。
最终处置只有：**本席正式完整候选合取 FAIL；既有数学接受保持；没有 Paper31 新项目/稿件/PDF 准入。**

[MAN]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_REVIEW_INPUT_MANIFEST_V1_20260910.md
[BRIEF]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_CANDIDATE_BRIEF_V1_20260910.md
[MAP]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_CURRENT_PROOF_MAP_V1_20260910.md
[PRE]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_PREFLIGHT_DISPOSITION_V1_20260910.md
[INV]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_SHARED_INPUT_INVENTORY_V1_20260910.md
[IC1]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_C1_PROOF_CONSUMER_INVENTORY_V1_20260910.md
[IG]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_G_PROOF_CONSUMER_INVENTORY_V1_20260910.md
[PA]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_ARITHMETIC_PHASE_A_V1_20260909.md
[MATH]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_ALL_DEGREE_MATHEMATICS_DISPOSITION_V1_20260910.md
[PB]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_PHASE_B_DISPOSITION_V1_20260910.md
[CD]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_NOVELTY_CD_V1_20260910.md
[BASE]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_TWO_DIAGNOSTICS_DISPOSITION_V1_20260909.md
[JET]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md
[JC]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_JET_AND_MIXED_INDEPENDENT_CHECK_V1_20260909.md
[EXT]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_DIAGNOSTIC_V1_20260909.md
[EC]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_INDEPENDENT_CHECK_V1_20260909.md
[G]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md
[GC]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_LATTICE_CONTROL_INDEPENDENT_CHECK_V1_20260909.md
[C]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_BINOMIAL_CONSUMERS_LEMMA_V1_20260909.md
[DET]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md
[TC]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_LATTICE_TOOLS_INDEPENDENT_CHECK_V1_20260909.md
[A]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_THEOREM_V1_20260909.md
[AC]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_INDEPENDENT_CHECK_V1_20260909.md
[S13]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_SOURCES_C1_C3_V1_20260909.md
[S2]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_SOURCES_C2_V1_20260909.md
[FS]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_FITTING_SOURCE_SUPPLEMENT_V1_20260909.md
[PD]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_CLOSED_PORTFOLIO_DELTA_V1_20260909.md
[PORT]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md
[LIMIT]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER29_30_EXISTING_INTERFACE_LIMITS_V1_20260909.md
[NU]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_MATHEMATICS_AND_SCREEN_DISPOSITION_V1_20260909.md
[INT]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md
[M4]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_M4_INTEGRAL_BLOCK_LEMMA_V1_20260909.md
[M4C]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NONUNIT_M4_INTEGRAL_BLOCK_INDEPENDENT_CHECK_V1_20260909.md
[OLDCD]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER31_QPI_NOVELTY_CD_I05_I09_V1_20260909.md
[P18]: /root/autodl-tmp/symplectic_map/papers/18-marked-henon-scalar-boundary/paper/main.tex
[P29I]: /root/autodl-tmp/symplectic_map/papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/1_introduction.tex
[P293]: /root/autodl-tmp/symplectic_map/papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/3_filtered_primitives.tex
[P294]: /root/autodl-tmp/symplectic_map/papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/4_hilbert_series.tex
[P302]: /root/autodl-tmp/symplectic_map/papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[P305]: /root/autodl-tmp/symplectic_map/papers/30-qpi-vertical-critical-ideals/paper/v4/sections/05-integral-trace.tex
[UNIT]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md
[FIRST]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_FIRST_LAYER_PROOF_V1_20260909.md
[FIBRE]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_FIBRE_PROOF_V1_20260909.md
[FC]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_FIRST_AND_FIBRE_INDEPENDENT_CHECK_V1_20260909.md
[M3]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_DEGREE3_MIXED_OBSTRUCTION_PROOF_V1_20260909.md
[W]: /root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_NONUNIT_TAU_FIRST_PRIME_OBSTRUCTION_PROBE_V1_20260909.md
[GR]: /root/autodl-tmp/symplectic_map/docs/research-batch07/primary-sources/griffiths-1976-variations-on-a-theorem-of-abel.pdf
[CALLAN]: https://arxiv.org/html/math/0209356v1
[MAAKESTAD]: https://arxiv.org/html/math/0402279v4
[KMRR]: https://arxiv.org/html/2411.13450v1
[GRWEB]: https://publications.ias.edu/sites/default/files/variationsonatheorem.pdf
