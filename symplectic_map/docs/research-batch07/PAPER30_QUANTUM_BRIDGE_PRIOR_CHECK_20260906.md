# Paper 30：量子周期桥的专门一手先例核查

日期：2026-09-06（UTC）  
状态：限定 Q1–Q3 的 prior 扣除与剩余不确定性；不作候选 PASS、论文容量判断或独立数学验收。  
唯一新建文件：本补记；先前 171 行 landscape 与作者证明均保持冻结。

## 1. 冻结输入与结论

已完整读取 419 行 [量子周期迹作者证明探针](PAPER30_QUANTUM_PERIOD_TRACE_PROBE_20260906.md)，SHA256：

    058cd7eaae3b5e1c19a2ca97a0beaafd7623fee9f67ff3a9e33d5117aaf95af2

本次只对下列精确主张做文献比较，独立数学检查由其他任务负责：

| 核心 | 本次比较对象 |
|---|---|
| Q1 | 相对基环 \(R=K[\hbar]\) 或任意固定 \(\hbar\in K\) 上，非线性 Hénon 图双模的 \(HH_\bullet(A,A_{\sigma^n})\) 与循环离散作用量的 \(D_i=\partial_iS_N-\hbar\partial_i\) Koszul 复形比较；显式 chronological 映射、标准基、正次同调消失及全部参数特殊化。 |
| Q2 | \(\sigma\) 在周期商上恰好置换该标准基，不带低阶 \(\hbar\) 修正；其角色为 \(\delta^{\gcd(n,r)}\)。 |
| Q3 | 若 \(N=kn\ge3\)、\(N>2L(g)\)，则周期和在完整 twisted-trace 模中为零等价于 \(g\in(\sigma-1)A\)，对所有 \(\hbar\) 精确成立；不是单个 scalar trace，也不是量子点值。 |

结论：**找到了必须新增扣除的实质方法 prior，但没有核到一步覆盖完整 Q1–Q3 的定理。**

- Gunningham–Safronov 的 Theorem 5.9 已直接比较 Lagrangian DQ 模的导出张量积与扭曲 de Rham 复形；不能再将“量子图交对应振荡复形”当作一般新桥。
- Krause–McCandless–Nikolaus 的 Theorem 6.26 已给双模 trace theory；\(HH(A,M^{\otimes_A n})\) 上的循环 \(C_n\) 作用是一般结构，不是 Hénon 独有发现。
- 本证明的全局 \(K[\hbar]\) 格、所有 \(\hbar\) 与系数特殊化、具体 chronological 基和 exact wrapping，尚未由这些已读定理一步推出。此处是有确切假设依据的区别，不等于已确认世界新颖。
- Fornæss–Weickert 2000 与 Weickert 2004 两个目标全文均未成功取得；不能以未读全文声称它们没有更强结果。可读的同作者 2003 原始论文重述了早期 exact shear/Egorov 结果，基础量子剪切亦必须扣除。

使用 research-lit 流程；并行子任务只负责两篇早期量子 Hénon 的公开原文获取与定位，未写文件。主任务自行完整读作者证明及下列一般桥接来源相关节，亦复核 2003 重述正文。没有重开几何/B-formal/旧 Paper 29 查新，没有保存 PDF 语料、外部记录或付费访问。

## 2. 实际查询覆盖

本轮复用 landscape 中已完成的精确 Hénon/Brieskorn 查询，不机械重跑。下表至少列出每个核心的三种实际查询角度；无关结果仅排除，不充当证据。

| 核心 | 本轮实际查询 | 结果 |
|---|---|---|
| Q1：Weyl/图双模 | "Weyl algebra" "bimodule" "exponential" "Hochschild"；"quantization" "graph" "bimodule" "trace" symplectic | 检查图双模与指数核入口；未命中完整全参数 Hénon 命题。 |
| Q1：Brieskorn 比较 | "Hochschild" "Brieskorn" "automorphism"；"Hochschild" "Brieskorn" "quantization"；"Hochschild homology" "oscillatory" integrals | 没有直接非线性周期命中；后续追到 DQ 模—扭曲 de Rham 的精确先例。 |
| Q1：D-module/FIO/固定点 | "D-module" "trace" "generating function" symplectic；deformation quantization Lefschetz trace formula automorphism fixed points Hochschild；"Hochschild" "twisted" "symplectomorphism" fixed points | 定位 Petit、Charles 与 Gunningham–Safronov，读具体定理而非仅摘要。 |
| Q2：旋转 | "Hochschild" "cyclic" "bimodules" "rotation" | 指向双模 trace 与循环旋转。 |
| Q2：迹的循环不变性 | "trace" "bimodule" "cyclic invariance" Ponto Shulman | 定位一般 trace-theory 路线。 |
| Q2：张量幂 | "Hochschild" "cyclic action" "tensor powers" bimodule | 定位 Krause–McCandless–Nikolaus，并读 Theorem 6.26 的实际构造。 |
| Q3：量子周期余边界 | "Weyl" "coboundary" "periodic"；"quantum" "twisted traces" "periodic" coboundary | 未命中全 \(\hbar\)、有限长度阈值的本题检测。 |
| Q3：映射专门形式 | "twisted trace" "periodic" "Hénon" | 未命中精确原始定理。 |
| Q3：有限检测/同调 | "Hochschild" "finite" "coboundary" automorphism；"quantum" "Livsic" polynomial | 结果主要是无关 Hochschild coboundary 或另一位 Livšic 的算子理论，均排除；不能当作数学 Livšic 先例。 |

两篇早期 Hénon 的精确标题、作者、副本与 DOI 查询另列在第 3 节。新命中 Gunningham–Safronov 的作者版 v3 为 2026-06-13，期刊出版为 2026-04-15，均在此前定义的最近六个月窗口内；不能只把它标成 2023 旧稿而漏掉当前正式版本。

## 3. 两篇指定 Hénon 原文的真实访问状态

### 3.1 Fornæss–Weickert 2000：原文任何节均未读

John Erik Fornæss, Brendan Weickert, *A quantized henon map*, DCDS **6** (2000), 723–740，DOI 10.3934/dcds.2000.6.723。[出版社页](https://www.aimsciences.org/article/doi/10.3934/dcds.2000.6.723)的摘要确认：将实平面 Hénon 映射量子化为 \(L^2(\mathbb R)\) 上的酉算子并研究动力学。

公开页面给出的 [PDF 导出](https://www.aimsciences.org/data/article/export-pdf?id=db1677d1-2edd-421d-ba19-7b51cc86dee9) 实际返回 HTTP 200 但 content-length 为 0；页面内 [旧 PDF 路径](https://data.aimsciences.org/aimsmath-upload/DCDS/2000/3/PDF/1078-0947_2000_3_723.pdf) 返回非 PDF。公开作者副本检索未补足全文。此为读取失败，不伪装成已读原文，也不推断具体定理不存在。

### 3.2 Weickert 2004：原文任何节均未读

Brendan Weickert, *Spectral properties and dynamics of quantized Henon maps*, Trans. Amer. Math. Soc. **356** (2004), 4951–4968，DOI **10.1090/S0002-9947-04-03475-0**。[出版社页面](https://www.ams.org/tran/2004-356-12/S0002-9947-04-03475-0/)返回 403 Forbidden，已停止该访问路径；[出版社 PDF](https://www.ams.org/tran/2004-356-12/S0002-9947-04-03475-0/S0002-9947-04-03475-0.pdf)未得到正文，没有尝试绕过。

读取的是 [出版社存入 Crossref 的元数据与完整摘要](https://api.crossref.org/works/10.1090/S0002-9947-04-03475-0)。摘要讨论 Fourier transform 与多项式相位构成的 \(U_c\)，使用广义 Airy 函数研究谱/动力学，并陈述某些充分大参数下纯连续谱。不能据摘要补写主定理编号、完整假设或 Q1–Q3 覆盖结论。

### 3.3 已取得的同作者一手正文：准确补强而非冒充全文

Brendan Weickert, *Quantizations of linear self-maps of \(\mathbb R^2\)*, Acta Sci. Math. (Szeged) **69** (2003), 619–631。[出版社公开 PDF](https://www.acta.hu/download.phtml?id=2742)。实际读取印刷页 621–623、626 的 Lemma 3；未将整篇线性理论当作本题先例。

- 页 622–623 明确重述 Fornæss–Weickert 的 Theorem 4：简化量子 Hénon 的某个 Fourier 特征态不能按所述参数解析扰动成相应特征态；这是谱 perturbation 障碍，不是 Q3 的多项式余边界。
- 页 626 Lemma 3 明确称为 Fornæss–Weickert Theorem 5.1 的轻微重述，给
  \[
  e^{-if(x)}ye^{if(x)}=y+f'(x),\qquad
  e^{-if(y)}xe^{if(y)}=x-f'(y).
  \]
  因而 exact nonlinear shear/Egorov 及基础量子轨道递推已有明确 prior。此重述段没有 Q1 的周期 Hochschild—作用量同构、Q2 指定基旋转或 Q3 检测；这句话只描述已读段落，不排除两篇未读全文。

## 4. 四篇最接近的一般桥接原始文献

### P1. Gunningham–Safronov：真正接近 Q1 的实质 prior

Sam Gunningham, Pavel Safronov, *Deformation quantization and perverse sheaves*, Duke Math. J. **175**(6) (2026), 1067–1161，DOI 10.1215/00127094-2025-0041。读取 [作者版 arXiv:2312.07595v3](https://arxiv.org/html/2312.07595v3)；[版本与期刊元数据](https://arxiv.org/abs/2312.07595)。Read level：引言 Theorems A/D、Example 1.1、§5.2 Theorem 5.9 及其证明、§7.1 Theorem 7.1 与相邻假设；不是全文精读。

Theorem 5.9 将零截面与 \(df\) 图的规范量子化模导出张量积识别为
\[
(\Omega_X^\bullet((\hbar)),d+\hbar^{-1}df)
\]
及其 \(\hbar\)-connection；证明使用 de Rham resolution。Theorem 7.1 扩展到带 orientation/contactification 数据的 Lagrangian 交，并与 vanishing-cycle/DT sheaf 比较。它不是只处理 Morse 点，因此“允许非 Morse 交”本身亦不能笼统主张新颖。

不能一步推出本题的理由是确切的：该文处于解析/微局部的 \(\mathbb C((\hbar))\) 环境，给规范 DQ 模及局部临界模型；本题指定全局代数图双模、\(K[\hbar]\) 格、chronological 乘法基、\(\hbar=0\) 及任意非零值特殊化。还需证明代数图双模与规范解析量子化的识别、全局与基环下降，并跟踪循环及 wrapping。原文引言亦明确区分代数 DQ tensor product 与规范解析版本，不能静默抹平。

### P2. Petit：kernel trace/diagonal intersection 的成熟一般框架

François Petit, *The Lefschetz–Lunts formula for deformation quantization modules*, Math. Z. **273** (2013), 1119–1138，DOI 10.1007/s00209-012-1046-4。[作者原文](https://arxiv.org/html/1112.2191)。Read level：§§3.1–3.2 的 Hochschild 定义、composition 与 proper-support 条件；§4.2 Theorem 4.1、Corollaries 3–4；§4.3 Proposition 11 及相关表述。

原文把 DQ kernel 的 trace 与其同对角核的 derived tensor / Euler characteristic 联系，并给 Hochschild composition。故“图核与对角求交表达 trace”“kernel composition 与 Hochschild 相容”都是一般 prior，不是本题的新原则。

Theorem 4.1 与 Corollary 4 要求紧复流形，工作于形式 DQ 基环；本题是非紧仿射平面的全局多项式相对同调和显式模。即使具体图复合满足部分 proper-support 条件，标量 Euler characteristic 公式也不自动给整个模的 chronological 基、正次消失、全特殊化或 Q3。不能因有“trace formula”同名就判整个本题被覆盖，也不能忽略它对方法论的扣除。

### P3. Charles：FIO 复合与固定点 trace 并非全 \(\hbar\) 模计算

Laurent Charles, *A Lefschetz fixed point formula for symplectomorphisms*, arXiv:1005.3443 (2010)。本轮使用 [作者原文](https://arxiv.org/html/1005.3443)。Read level：§4.1–4.3 的 Hilbert 空间/FIO 定义与 Theorems 4.2.1–4.2.2、4.3.1；§5.3 Theorem 5.3.1。

这里有紧 Kähler 流形的 FIO 复合、主符号及固定点 trace 渐近。Theorem 5.3.1 在图与对角横截下给固定点贡献和及 \(O(k^{-1})\) 误差。

这直接扣除“量子映射 trace 来自周期相位/驻相”的一般想法，但既不是非线性 Weyl 图双模的相对 \(HH_\bullet\)，也不是包含 \(\hbar=0\) 的精确代数格。横截与渐近条件亦不能用来处理本题任意非约化经典周期碰撞。因此没有一步适用到 Q1–Q3；它限定的是 FIO 类比应有的谦逊表述。

### P4. Krause–McCandless–Nikolaus：Q2 抽象循环作用的直接 prior

Achim Krause, Jonas McCandless, Thomas Nikolaus, *Polygonic spectra and TR with coefficients*, arXiv:2302.07686v1 (2023-02-15)。本轮使用 [作者原文 PDF](https://arxiv.org/pdf/2302.07686v1)。Read level：§1.4 Theorem E 及其后 \(C_n\)-action 说明；§6.2 Definition 6.25、Theorem 6.26 与证明，尤其印刷页 56–58。

Theorem 6.26 在适当对称幺半范畴给 Hochschild trace theory，包含双模 tensor 的循环不变性。原文明确构造 \(HH(A,M^{\otimes_A n})\) 上由旋转产生的 \(C_n\) 作用。取导出 \(R\)-模范畴与自同构双模 \(M=A_\sigma\)，即得到本题相关的一般结构（循环生成元可能随右/左 twist 约定取逆）。

故“在 \(HH(A,A_{\sigma^n})\) 上存在周期旋转”是一项直接的标准适用，不应作为独立新主张。但原文不识别本题的 \(\delta^n\) 个具体 chronological 基向量，也不证明它们在未完成的多项式 \(R\) 上被无修正置换。角色公式一旦这种基置换建立，就是普通有限字旋转计数的短推论。

## 5. 对 Q1–Q3 的逐项 prior 扣除

| 本证明组成 | 判定 | 需要保留的精确区别 |
|---|---|---|
| 基础 Weyl shear、量子 Hénon 本身 | 已有明确 prior：2000 摘要、2003 同作者 Lemma 3 重述 | 不可用量子化本身作新颖性。 |
| 相对 Weyl Koszul resolution、正则首项导致消失/标准基 | 标准工具；作者证明已自述为基础事实 | 本轮不重做数学验收，也不将这些工具改记号算新理论。 |
| tame Brieskorn 自由性/经典 Jacobian 纤维 | 复用冻结 landscape 的已读 Douai–Sabbah 等扣除，不重搜 | 本题的单项首项给 universal coefficient 的直接证明；“自由性”一般原则非新。 |
| 图量子化/零截面 tensor 对应 twisted de Rham | P1 Theorem 5.9 是实质方法 prior；P2 给 kernel/diagonal trace 框架 | 未直接覆盖指定全局 \(R\)-图双模与 \(Q_N\) 的 chronological 同构及所有特殊化。 |
| exact cyclic action 的存在 | P4 的一般 trace theory 可直接适用 | 本题要验证的是该作用对应指定轨道基的精确置换，而非抽象群作用存在。 |
| \(\delta^{\gcd(n,r)}\) 角色 | 在 Q2 基置换成立后是标准组合短推论 | 不能将角色计算包装成第二套新 trace 理论。 |
| exact wrapping (18) 与有限阈值 (5) | 已读来源未直接给出本题条件和结论 | 仍需明确扣除 Paper 29 已有 no-alias lemma；新增比较焦点是它与非交换周期商的精确、全 \(\hbar\) 相容性。 |

### 是否只是“标准核复合的短算”？

能够成立的文献判断是：**框架及不少局部操作确为标准；还不能从已读定理直接宣布整条 Q1–Q3 是一步推论。**

例如，一个 elementary shear 的指数核、kernel 复合时相位相加、对角 trace 给循环作用量、以积分分部/Spencer–de Rham resolution 得 \(\partial S-\hbar\partial\)，都属于已有方法的自然使用。P1 已提供实际复形比较，而不只是物理启发。作者 §§3–4 的内部消元与端点 Koszul 可视为该方法的一种显式代数实现，应说明这种联系。

不过，若要仅引用这些文献取代作者证明，必须补齐至少三处而非只写“标准”：

1. 把图双模的全局代数对象识别成所用规范 kernel，并确认 twist 与左右作用约定；
2. 将局部解析/\(\mathbb C((\hbar))\) 比较下降到 \(K[\hbar]\) 的指定格且兼容所有参数特殊化；局部化会丢失格与特殊化信息，不能逆推；
3. 证明所得比较是 chronological 映射，并将一般循环 trace 对称性落实为该有限基上的精确置换及短字 wrapping。

在这三项之后，Q3 的剩余组合部分主要由本地旧 no-alias 与系数轨道和论证承担，不应重新称为量子组合理论。本报告不对这些实质增量的长度或投稿价值作裁决。

## 6. 未关闭风险与允许使用的结论

已完成的三核心定向查询没有命中“对该 Hénon 族、全 \(K[\hbar]\)、指定 chronological 基、exact finite detection”的直接一手定理。最接近的实际 prior 是 P1 与 P4；它们已足以要求缩窄任何新颖性措辞。应说“本轮已读来源尚未直接覆盖全参数精确比较与有限检测”，不说“现有理论仅处理线性”——后一句已被 P1 的非线性 Lagrangian 理论否定。

仍未关闭的风险只有与本题直接有关的两类：

- 两篇早期 Hénon 目标全文未读。2003 一手重述补强 shear prior，但不能替代 2000/2004 全文核查。
- 一般图 kernel/DQ 方法可能使某些作者论证成为标准专门化；本轮已经定位并扣除具体命题，但没有穷尽所有代数量子化 kernel 文献，也没有证明不存在更直接的全局 Rees 版本。

没有因为访问失败扩大权限或绕过限制。没有将这些阅读限制混同于数学失败，也没有改变冻结作者稿的证明状态。可将本补记交给后续独立新意评价，连同作者证明一起核对；本报告本身不发出 PASS。
