# Session 3 最终总结：冻结 Hénon 同伦的结构性边界

本 session 实际完成并封存的主候选只有一个二维 Hénon 同伦：

\[
H_{a,\rho}(x,y)=(1-a x^2-\rho y,x),\qquad
a=u_c=1.5436890126920763,\qquad 0\leq \rho\leq 1.
\]

其微分满足

\[
DH_{a,\rho}^{\mathsf T}\Omega DH_{a,\rho}=\rho\Omega,\qquad
\det DH_{a,\rho}=\rho.
\]

因此 \(\rho=0\) 是奇异的父映射参考，\(0<\rho<1\) 是耗散的共形辛对照，\(\rho=1\) 是二维辛端点。冻结候选的最终判定为
**A0_SHADOW_FAIL_CARRIER_UNAVAILABLE / ROUTE_A_REJECTED**：父映射上的声明性 mod-2
回归间隔 fixture 得到复现，但冻结的父映射派生 ensemble 在辛端点没有达到预注册的
carrier 可用性门槛，且邻参对照触发 **PROVES_TOO_MUCH**。这只否定当前 source lock
下的候选路径；它不是“所有有界不变集都不含算术结构”的定理，也不是对任何数论猜想
的反证。

权威的机器可读结论见
[最终 Route-A 评估](evaluations/route_a/henon_homotopy/2026-08-13-final.yaml)、
[结果记录](papers/1-symp-vs-diss/notes/RESULTS.md)和
[claim matrix](papers/1-symp-vs-diss/notes/CLAIM_MATRIX.md)。

## 对 proposal 第 14 节十二个问题的逐项回答

### 1. 探索了哪些辛映射族？

唯一被实现、冻结并做开发/验证/封存测试的族是上述二维
\(H_{a,\rho}\)。研究重点是同一公式内从奇异父映射
\(\rho=0\)，经过耗散共形辛区间 \(0<\rho<1\)，到面积保持端点
\(\rho=1\) 的匹配比较。

积分 cat map 只作为解析负控制被讨论：若
\(A\in SL(2,\mathbb Z)\) 的双曲不稳定乘子等于有理素数 \(p\)，则整数迹将等于
\(p+p^{-1}\)，矛盾。它没有被另行扩展为本 session 的数值主族。标准映射、耦合映射、
高维映射和量子映射均未开启。

### 2. 哪些保守/耗散比较是决定性的？

决定性比较有两组。

第一组是冻结 symbolic-transport test。对
\(L=\{x<0\}\) 的回归间隔定义

\[
P=\frac{N_{\rm even}-N_{\rm odd}}{N_{\rm even}+N_{\rm odd}}.
\]

封存测试中，\(\rho=0\) 给出 \(P=1\)、exposure \(=1\)；在
\(\rho=0.2\) 时仍有 \(P=0.998907\)、exposure \(=1\)。但在
\(\rho=1\) 时，exposure 只有 \(0.0117239952\)，完整 horizon survivor 为
0，只有 9,988 个可用回归间隔，低于预注册的 exposure \(0.8\) 和 10,000 gaps
门槛；逃逸前的条件统计量为
\(P=-0.70664798\)，trajectory-cluster bootstrap 95% CI 为
\([-0.71625339,-0.69678543]\)。所以端点结果按预注册优先级首先判为 carrier
unavailable，而不是把稀少逃逸前样本解释为 transport 成功或普遍失败。

第二组是机制对照。正固定点的 Jury 判据给出精确翻转阈值

\[
\rho_{\rm PD}=\sqrt{\frac{4a}{3}}-1,
\qquad
\rho_{\rm PD}(u_c)=0.434660941450198\ldots.
\]

独立的 post-validation attractor diagnostic 在 \(u_c\) 处观察到
unresolved/high-period \(\to 8\to 4\to 2\to\) positive fixed point 的普通
耗散分岔骨架，并在 \(0.43\) 与 \(0.44\) 之间跨过解析阈值。四个邻参也在各自阈值
相邻网格发生同样切换。到 \(\rho=1\)，所有周期 \(n\) 轨道均有
\(\det M_\gamma=1\)，因此不可能存在周期 sink；该诊断 ensemble 的 256/256 条轨道
均逃逸。这里的 256/256 只描述该冻结诊断 ensemble，不表示整个相空间没有有界轨道。

### 3. 哪些候选具有真实的算术相关性？

没有候选达到“真实算术相关性”的证据门槛。冻结参数 \(u_c\) 是
\(u^3-2u^2+2u-2=0\) 的正实根，且父映射具有精确 post-critical itinerary，
但这只是动力系统上的精确来源，并不建立有理素数机制。上游可复现证据最多支持
mod-2/parity shadow，不能支持 rational-prime coding。

另一个反例式控制说明单个“素数乘子”不够：在 \(H_{a,1}\) 的负固定点上，可以通过
调节 \(a\) 令不稳定乘子等于任意选定的 \(m>1\)；特别地 \(a=1.56\) 可精确得到
乘子 5。因此 \(u_c\) 处约 \(4.98936\) 的单次近素数命中属于可调巧合，而非算术信号。
本 session 从未打开素数标签或黎曼零点数据。

### 4. 哪些 primitive-orbit 结构最强？

最强的是软件正控制，而不是算术候选：在 \((a,\rho)=(6,1)\) 上，orbit finder
逐周期恢复了

\[
2,1,2,3,6,9,18,30,56,99
\]

这一 period 1--10 的 primitive binary-necklace 计数。全部 226 条周期轨道通过
独立 80 位高精度 refinement，最大 residual 为
\(7.04\times10^{-61}\)。该审计不是 interval proof。

在主参数 \((u_c,1)\) 上，只找到 period 1--8 的
\(2,0,2,2,2,3,4,5\) 条轨道；找到的 20 条轨道均通过高精度 residual 审计，但
ledger 明确不完整。它不能被用于完整 cycle expansion、determinant 或算术匹配。

### 5. 哪些候选产生了自然 Zeta/Fredholm 对象？

没有候选产生经过本 session 验证的自然 Zeta/Fredholm 对象。对完整双曲
primitive ledger 可以形式上写出不稳定乘子 Euler product，但主候选在 A0
carrier 门槛失败，且 \(u_c\) ledger 不完整，因此 A2 被 STOP_SCOPED。没有计算
Ruelle determinant、Gutzwiller-type determinant、解析延拓、divisor 或 target
match；两类权重也没有被混用。

### 6. 找到了哪些 obstruction？

主要 obstruction 是：

1. **Critical-factor rank obstruction（标准、已证明）**：若
   \(\pi\) 是 \(C^1\) submersion、\(F\) 是局部微分同胚且
   \(\pi\circ F=f\circ\pi\)，则在 \(Df=0\) 的临界纤维上，链式法则两侧秩矛盾。
   因而临界二次映射不能在该临界纤维上成为正则有限维辛映射的光滑 submersion
   factor。该结论不排除 inverse-limit、branch extension 或 canonical relation。
2. **正则性与精确投影不可兼得**：奇异 cotangent/weak-noise lift 可在远离
   \(f'=0\) 处保持投影，但临界纤维奇异；光滑 Hénon memory 坐标避开奇异性，却失去
   对父映射的精确 projection semiconjugacy，所以任何继承的 symbolic/arithmetic
   信息必须重新测试。
3. **端点 carrier obstruction**：冻结 ensemble 在 \(\rho=1\) 的 exposure
   过低且没有 full-horizon survivor，禁止对稀有逃逸前片段作 survivor-conditioned
   算术解释。
4. **specificity obstruction**：\(a=1.50,1.52,1.56,1.58\) 四个邻参重现
   小 \(\rho\) 的近单位 parity，并在端点同样约 1% exposure、零 survivor、负
   polarity；四个 Holm-adjusted directional diagnostics 均为 1.0。该模式不是
   \(u_c\) 特异的。
5. **ledger completeness obstruction**：高 \(a\) 正控制完整，不推出混合动力学
   \(u_c\) ledger 完整；当前漏轨风险阻断所有 downstream determinant 结论。
6. **可调单轨道命中 obstruction**：单个固定点乘子可被参数调成 5，不能作为素数
   富集证据。

详细证明和证据边界见
[proof package](papers/1-symp-vs-diss/notes/PROOF_PACKAGE.md)与
[obstruction registry](docs/obstruction_registry.md)。

### 7. 高维是否有帮助？

没有证据回答“有帮助”。高维或耦合辛映射没有被开启，因为二维候选已在 A0
入口门槛停止；直接加维不会修复上游 arithmetic origin、carrier 或 specificity
问题。高维只保留为一个必须重新 source-lock 的未来候选方向。

### 8. 辛性是否提供了有用的 phase/sign 结构？

在几何层面提供了明确但有限的正结果：\(\rho=1\) 的乘子成倒数配对，且存在
type-1 generating function

\[
S_a(q,Q)=qQ-q+\frac a3 q^3,
\qquad
\mathcal A_\gamma=\sum_j S_a(q_j,q_{j+1}),
\]

所以周期作用量是同一辛映射的内禀对象。但没有建立与算术 trace formula 有关的
自然 sign、complex phase 或 Maslov-type 数据。观测到的 parity 反转不是已识别的
canonical phase。因此答案是“几何上有 phase-capable structure，算术上尚无有用
phase/sign 证据”。

### 9. 哪些候选具有自然量子化？

没有。生成函数只给出 A4 的 formal hint；非紧逃逸、冻结 carrier 失败以及缺少
完整算术 orbit ledger，使得自然 Hilbert space、边界条件、unitary map、
Fourier-integral operator 和 classical/quantum trace correspondence 都没有被
构造或测试。Route B 未获准开启。

### 10. 哪些 ROUND2_CLUE 应保留？

保留以下线索，但都必须作为新候选，而不是事后修补本次失败：

1. 带 branch label 的 natural extension 或 canonical relation，用显式分支信息
   处理临界点，同时重新定义并冻结其 arithmetic origin。
2. 真正紧致或具有独立证明之不变性的 carrier；算术来源必须独立于素数表和目标零点
   预先给出。
3. 有限/积分 cat-map arithmetic 作为精确负控制族，而不是用来 rescue 当前 Hénon
   候选。
4. 高维耦合辛 Hénon 仅作为低优先级的新族线索；它必须先说明新增自由度具体消除了
   哪个二维 obstruction，不能仅靠更复杂的 orbit growth 获得算术解释。

在同一 source lock 内重新挑选 survivor、参数、partition、seed 或 prime label
不属于 ROUND2_CLUE，而属于禁止的 post-hoc 修补。

### 11. 最强的正结果是什么？

最强正结果是一个可复现的“结构约束图”，而非算术对应：

- 精确建立 conformal-symplectic identity、monodromy determinant、\(\rho=1\)
  generating function/action 与 critical-factor rank obstruction；
- 30 项实现测试通过；
- \(a=6,\rho=1\) 的 period-10 primitive ledger 正控制完整恢复，并有独立 80 位
  residual 审计；
- 精确 Jury 阈值与五个 \(a\) 值上的独立 attractor diagnostic 相符，解释了
  dissipative side 的普通分岔机制。

它说明当前代码和几何诊断足以区分“数值实现失败”与“候选机制失败”。

### 12. 最强的负结果是什么？

最强负结果是：对预先冻结的 \(u_c\)、父映射派生初始化、partition、escape box、
统计量和门槛，弱 mod-2 shadow 没有以“充分暴露且 \(u_c\)-特异”的方式到达辛端点。
端点 carrier availability、polarity 和 neighbor-specificity 三类 gate 均失败，
而邻参与普通 Jury 分岔机制重现了整体图景。因此该候选的
prime-multiplier、Zeta/Fredholm、analytic/Weil-compression 与 quantization
分支依照 stop rule 全部关闭。

严格边界是：这是一个冻结 carrier 的受控否定结果；它不排除其他初始化、不变集、
branch extension、紧致化或其他辛映射族中存在算术结构。

## 关键 artifacts

- 候选定义与锁定：
  [source_lock.json](papers/1-symp-vs-diss/experiments/source_lock.json)、
  [confirmatory_manifest.json](papers/1-symp-vs-diss/experiments/confirmatory_manifest.json)
- 单次 test 访问与协议记录：
  [test_access_log.md](papers/1-symp-vs-diss/experiments/test_access_log.md)
- 封存 transport 原始结果：
  [transport_test_frozen_v2.json](papers/1-symp-vs-diss/results/transport/transport_test_frozen_v2.json)
- cluster-aware test 分析：
  [transport_test_analysis_v1.json](papers/1-symp-vs-diss/results/analysis/transport_test_analysis_v1.json)、
  [paired CSV](papers/1-symp-vs-diss/results/analysis/transport_test_analysis_v1_paired.csv)
- attractor 机制：
  [ATTRACTOR_ANALYSIS.md](papers/1-symp-vs-diss/notes/ATTRACTOR_ANALYSIS.md)、
  [attractor_diagnostics_v1.json](papers/1-symp-vs-diss/results/attractors/attractor_diagnostics_v1.json)
- primitive-orbit 正控制：
  [a=6 ledger](papers/1-symp-vs-diss/results/ledger_positive_a6_rho1_n10.json)、
  [80-digit audit](papers/1-symp-vs-diss/results/ledger_positive_a6_rho1_n10_audit80.json)
- 主参数探索性 ledger：
  [u_c ledger](papers/1-symp-vs-diss/results/ledger_uc_rho1_n8_exploratory.json)、
  [80-digit audit](papers/1-symp-vs-diss/results/ledger_uc_rho1_n8_audit80.json)
- 精确推导与证据分级：
  [DERIVATION_PACKAGE.md](papers/1-symp-vs-diss/notes/DERIVATION_PACKAGE.md)、
  [CLAIM_MATRIX.md](papers/1-symp-vs-diss/notes/CLAIM_MATRIX.md)

## 冻结哈希

    7d81c30863c0e27ba0e5494c9ad76b148a9e0edbdc213adbc233794b713d6d0e  papers/1-symp-vs-diss/experiments/source_lock.json
    b8186fcd6e323d2e6d2e7e5c05f5f18b98cdf92475675bce25d74e0d158e3cf8  papers/1-symp-vs-diss/experiments/confirmatory_manifest.json
    a8c272161bd38e37e140c0ad72511461e4fb837edf2bf7880ba21014b89705c5  papers/1-symp-vs-diss/results/analysis/transport_test_analysis_v1.json

test 原始结果及四个邻参文件的 SHA-256 逐项记录在
[test_access_log.md](papers/1-symp-vs-diss/experiments/test_access_log.md)。

## 复现命令

从 session 根目录运行：

    cd papers/1-symp-vs-diss/code
    PYTHONPATH=. pytest -q
    python scripts/run_ledger.py --preset positive-control --max-period 10 \
      --output /tmp/ledger_positive_a6_rho1_n10_reproduction.json
    python scripts/audit_ledger.py \
      /tmp/ledger_positive_a6_rho1_n10_reproduction.json \
      --output /tmp/ledger_positive_a6_rho1_n10_audit80_reproduction.json \
      --digits 80
    cd ..
    python code/scripts/analyze_transport.py --split test \
      --output-stem transport_test_analysis_reproduction_YYYYMMDD

这些命令分别复现实装测试、\(a=6\) 正控制 ledger、非区间的 80 位 residual audit，
以及从已封存原始数据在新文件名下重新生成 cluster-aware test 分析。attractor diagnostic 可在
不覆盖正式 artifact 的新输出目录中复现：

    python code/scripts/run_attractor_analysis.py \
      --run-label attractor_diagnostics_reproduction \
      --output-dir results/attractors-reproduction

不要重新运行 test trajectory generator。其 seed、五个并行 test arms、授权命令和
关闭状态已写入 manifest 与 test access log；改变 seed 或阈值将构成新的
post-confirmatory experiment，不能改变本次 formal decision。

## 协议偏差与解释限制

1. source-lock v2 是在 development-only smoke/full development 调试之后冻结的；
   development split 不支持 confirmatory language。
2. 在主代理要求暂停 validation 之前，一个实现代理曾以
   \(N=512,T=512\)、escape bound \(10^6\) 运行小型 validation smoke。文件只写入
   /tmp，未进入推断；其后 full frozen-v2 validation 只运行一次。
3. confirmatory manifest 在 validation 分析之后、任何 test artifact 产生之前
   追加冻结了 paired cluster-bootstrap/Holm 实现和四个已预注册邻参命令；五个
   test arms 随后作为一个 batch 打开。
4. 当前 session 根目录当时不是 Git worktree，因此 manifest 的
   workspace_commit 为 UNAVAILABLE_NON_GIT_WORKSPACE；可追溯性依赖逐文件 SHA-256
   和 single-use access log。
5. Holm 数量是 bootstrap sign-tail diagnostics，不是精确 randomized-treatment
   p-values；主要比较证据是 effect size 和 trajectory-cluster bootstrap CI。
6. 80 位 orbit audit 是高精度 refinement/residual check，不是 interval
   certification；它验证“找到的轨道”，不证明 \(u_c\) ledger 完整。
7. primes、Riemann zeros、Riemann-targeted Zeta/Fredholm、quantization 和
   Weil compression 从未开启。任何 downstream 说法都只能标记为未测试或
   STOP_SCOPED。
