# Paper29：完整标记迹谱的内在微分秩与冗余固定点框架

日期：2026-09-06。任务范围：一个新的有界查新与体量预筛；不是对第五候选冻结 main+boundary 包的重新评价，不修改其新意、价值、证明或篇幅状态。

## 1. 结论先行

本轮优先核查的两篇原始文献没有给出所问的**固定参数邻域内、每一点、完整标记乘子谱微分均无核**结论。Cantat–Dujardin 的有限谱纤维不能直接升级为逐点 immersion；Bianchi–He 刻意区分半正定协方差型与非退化路径距离。因此，若能证明固定若干个宏周期为一的迹，在一个不随 \(\epsilon\) 缩小的 \(u\) 邻域内形成统一 frame，这会补上一个真实的局部定量结论，而非已被这两篇直接包含的重复命题。

但目前提供给本轮的只是正在检查的“全 plus + \(k\) 个 single minus + 两个 double minus”构造建议，尚无该新构造的完整作者证明输入。本报告不将 \(k+3\)、固定邻域或 \(\sigma_{\min}\ge c|\epsilon|^2\) 当作已证事实，也不沿用第五候选的任何分数。

体量预筛：它首先是**已知一、二阶 jet 的冗余观测强化问题**。若极化差分直接给出所需证书，新的负载主要是消项、剩余两方向的定量控制和固定邻域扰动；全谱微分无核、固定 tuple 临界非内在、协方差型逐点正定随后都是短推论。仅这些推论不足以宣告新长文或解除既有 22 页体量 STOP。建议限于完成并检查实际 frame 证明，之后按真正新增的数学内容评价；当前不评分、不创建 PASS。

采用 research-lit 与 novelty-check：完整读取技能后，仅做指定两篇原文的精确条款核查和五种定向查询。按本次有界授权，不重扫冻结本地论文，不重复旧模 6 查新，不下载 PDF，不调用不可用的 GPT-5.4 审稿接口，仅创建本文件。

## 2. 问题与量词

固定 \(6\mid k\)，仍在逐因子系数空间中研究
\[
H_c(x,y)=(x^2+c-y,x),\qquad
F_{\epsilon,u}=H_{c_k}\circ\cdots\circ H_{c_1},
\qquad c_j=\epsilon^{-2}(u_j-1).
\]
\(\epsilon\ne0\) 固定时的参数切空间是 \(\mathbb C^k\)；所有参数微分都在 \(u\) 中进行。
对各局部标记周期分支 \(\mathcal O\)，写 \(\rho_{\mathcal O}=\operatorname{tr}DF^{n(\mathcal O)}\)。完整标记迹微分的共同核是
\[
\mathcal I_{\epsilon,u}
=\bigcap_{\mathcal O}\ker d_u\rho_{\mathcal O}.
\]
“内在退化”在本报告中只表示这个共同核非零，不表示已处理无标记模空间的一切有限商奇点或共轭方向。

待证 frame 提案要求一组事先固定的 \(N\) 个宏固定点 \(\mathcal S\)，其矩阵
\[
R_{\mathcal S}(\epsilon,u)
=\left(\rho_{\mathcal O}^{-1}\partial_{u_j}\rho_{\mathcal O}\right)_
 {\mathcal O\in\mathcal S,\ 1\le j\le k}
\]
在某些 \(\eta,\epsilon_0,c>0\) 下满足
\[
0<|\epsilon|<\epsilon_0,\quad \|u\|_\infty<\eta
\quad\Longrightarrow\quad
\sigma_{\min}(R_{\mathcal S})\ge c|\epsilon|^2 .
\tag{F}
\]
这里 \(\eta,c,\epsilon_0\) 可以依赖固定的 \(k\)，但不能依赖 \(\epsilon,u\)；\(N=k+3\) 是正在检查的建议，不是最少观测数结论。不得把奇异重标度后的矩阵下界误报成原始迹 Jacobian 的同一下界。

三个不同层次不能混淆：

| 层次 | 量词 | 本轮判断 |
|---|---|---|
| 泛型全谱秩 | 除去某个真退化集后可取足够谱微分 | 与现有完整谱刚性及一般特征零论证相容，不能当作从零开始的新主张 |
| 逐点全谱秩 | 目标域内每个 \((\epsilon,u)\) 都有 \(\mathcal I_{\epsilon,u}=0\) | 指定两篇原文没有直接保证该整个固定 \(u\) 域 |
| 固定有限定量 frame | 同一组有限固定点、同一 \(u\) 域，对所有小非零 \(\epsilon\) 满足 (F) | 比逐点存在选择更强，是当前构造真正需要承担的证明义务 |

## 3. 两篇原文的精确覆盖

### 3.1 Cantat–Dujardin

[Cantat–Dujardin, *Multiplier rigidity for complex Hénon maps*, arXiv:2603.09445v1，2026 预印本](https://arxiv.org/html/2603.09445v1)：
§3.2 定义谱；Proposition 3.3、Theorem 3.5 给固定 multidegree/multi-Jacobian 族的谱纤维刚性；Theorem 3.7 给有限周期截断。证明通过排除正维常谱族进行，不声称每个参数点的标记谱微分单射。全文对 infinitesimal、tangent、differential 的定向检查也未找到一个可替代本问题的逐点微分定理。

因此可用的链是“全谱信息足以排除实际连续常谱变形”，不是“任意一阶常谱切向量都为零”。有限纤维加特征零可支持某个有限谱映射的泛型满秩；它不消除分歧点，也不给只用固定点的统一 frame。这是从该结果作出的标准推断，非原文声称的额外定理。

以下简单反例说明逻辑差距：\(\Phi(z)=(z^2,z^3)\) 的纤维都是单点，没有非平凡常值路径，但 \(d\Phi_0=0\)。故即使把“有限纤维”增强为“集合层面的单射”，仍不能推出逐点 immersion。

### 3.2 Bianchi–He

[Bianchi–He, *A thermodynamic path metric for complex Hénon maps*, arXiv:2606.29363v1，2026 预印本](https://arxiv.org/html/2606.29363v1)：
Proposition 3.4/Corollary 3.5 将协方差零方向联系到标记不稳定乘子的零微分；Corollary 4.3 要求沿整条路径处处零范数，才推出乘子沿路径常值。Theorem 1.1 的结论是路径距离非退化，不是 Hermitian 型逐点正定。

更直接地，Lemma 5.1 的证明只得到局部协方差矩阵行列式不恒零，从而在真解析集之外正定；Introduction 亦说明本场景缺少所需的逐点非退化控制。不能把“没有非恒定零长度路径”误写成“没有孤立或低维零切向量”。

例如一维实解析型 \(Q(z;\xi)=|z|^2|\xi|^2\) 在 \(z=0\) 退化，却不产生非恒定零长度路径。这个示例只是解释量词差异，不是 Hénon 反例，也不判定实际 Hénon 谱是否存在这样的点。

## 4. 真正可用的定理链

在本题所有周期均处于双曲区、\(\det DF^n=1\)、相关迹非零的域中，令 \(\lambda_{\mathcal O}\) 为不稳定乘子。直接计算给出
\[
\rho_{\mathcal O}=\lambda_{\mathcal O}+\lambda_{\mathcal O}^{-1},
\qquad
d\log\rho_{\mathcal O}
=\frac{\lambda_{\mathcal O}-\lambda_{\mathcal O}^{-1}}
       {\lambda_{\mathcal O}+\lambda_{\mathcal O}^{-1}}
  d\log\lambda_{\mathcal O}.
\tag{T}
\]
因子非零，所以两种微分的核相同。以下是条件性推论链，不是把 frame 提案预先视为已证：

1. 若 (F) 成立，则选中固定点的共同微分核为零。
2. 完整标记谱包含这些固定点，故 \(\mathcal I_{\epsilon,u}=0\)。
3. 若原来某一个 \(k\)-tuple 的行列式在该域某处为零，这只说明该次选取不足，不能说明完整谱有非零共同核。
4. 若 Bianchi–He 的协方差型在某向量上为零，则其 Corollary 3.5 使所有标记不稳定乘子微分为零；由 (T) 及第 1 步，向量只能为零。因此该型在此域逐点正定。

第 4 步不需要重新建立热力学形式，也不需要证明一个全新的全谱刚性定理。它不能反过来冒充 (F) 的证明。
此外，(F) **不自动推出**
\[
Q_{\epsilon,u}(\xi)\ge c'|\epsilon|^4\|\xi\|^2
\]
这类协方差范数定量下界：有限周期观测的欧氏范数与渐近协方差范数之间还缺统一比较。逐点正定及固定 \(\epsilon\) 的紧集最小值也不能补足 \(\epsilon\to0\) 的阶数。

有限维线性代数还给出另一条容易被过度使用的事实：在某一个点，\(\mathcal I_{\epsilon,u}=0\) 等价于能从全谱中取出 \(k\) 个独立微分；这些周期和标记可以依赖该点。在固定 \(\epsilon\) 的紧参数集上，若已知处处无核，可用局部开性和有限覆盖取有限多个观测。但这不控制观测数量，也不保证全是固定点，更不保证同一组观测对趋向零的所有 \(\epsilon\) 都适用。

## 5. 冗余构造相对于既有 jet 的增量与待证义务

不重查冻结包，只将其已验收的一、二阶 trace jet 作为当前提案明确打算使用的输入。新提案是对符号取离散差分，例如
\[
\kappa_{\{i,j\}}-\kappa_{\{i\}}-\kappa_{\{j\}}+\kappa_{\varnothing},
\]
其中花括号是负号相位集合，\(\kappa=d\log\rho\)。需要注意：消息中的“二阶极化”是待验证路径，而非本报告发现的新公式。

实际新增证明至少应交付以下内容：

- **确切消项。** 公共零阶及相位线性的一阶项须在整个固定 \(u\) 邻域中被消掉，不能只在 \(u=0\) 消掉后留下除以 \(\epsilon^2\) 会发散的 \(O(u/\epsilon)\) 项。
- **确切选字与二阶分离。** 说明两种 double minus 的相位选择，证明其二阶差分在相关两维 kernel 上线性独立；不以 \(k=6\) 数值样例替代每个固定 \(6\mid k\) 的论证。
- **矩形矩阵的下界。** 区分原始 \(R_{\mathcal S}\)、有界行组合、除以 \(\epsilon\) 或 \(\epsilon^2\) 的行与移动列基，给出从重标度证书返回 (F) 的正确不等式。
- **共同域。** 非共振方向与剩余 kernel 的补空间、投影及逆界必须在固定 \(u\) 域内受控；利用已有全纯余项，而非重新叙述整个周期轨道存在理论。
- **数据合法性。** 同一组标记确为互异、简单、迹非零的宏固定点；\(k+3\) 只是上界，不含最小性、全局注入或全部临界 scheme 分类。

若这五项直接由冻结的一、二阶 jet 加有限维扰动证明完成，则新命题虽有信息增量，独立证明负载仍很可能是一个有界补充：它把“某 tuple 的可逆性区域”升级为“少量冗余观测的固定区域可观测性”。不能把重复的反可积输入、已有共振计算、全谱核推论和协方差推论各包装成一份新的长证明。

相反，如果实际构造暴露了一个新的全谱共同核、需要更高阶/更多周期的机制，或得到当前两阶输入不能解释的结构，那才是重新估量独立体量的具体依据。本轮既未证明此类额外现象，也不为了篇幅要求假定它们存在。

## 6. 有界检索记录与交付状态

除指定两篇原文的 find/open 定位外，仅用了以下五种检索，没有再开一般综述：

1. Hénon + infinitesimal + multiplier + rigidity。
2. Hénon + marked + multipliers + immersion。
3. Hénon + multiplier covariance + degenerate + 2026。
4. marked multiplier + infinitesimal rigidity + polynomial automorphisms，限定 arXiv。
5. Hénon + fixed + traces + rank + differential，限定 arXiv 与 2026-03-06 至 2026-09-06。

没有新增可核实、精确覆盖所问 frame 的原始来源。相关返回主要仍是上述两篇；半抛物 Hénon 的 infinitesimal metric、Hénon–Heiles 和数值稳定性结果不回答本问题，未作为证据。有限检索没有找到重复，不是不存在 prior 的证明，更不是高分证书。

状态：文献边界与逻辑链已核清；新 frame 的构造和估计尚待实际证明；最少观测数未解决且不是当前提案承诺；独立长文体量未获支持。唯一新产物是本报告，没有新项目、锁、外部写入或 PASS。
