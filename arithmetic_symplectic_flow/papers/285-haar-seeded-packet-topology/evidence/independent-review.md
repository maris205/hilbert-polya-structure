# 285 同对象拓扑审计：独立内部三检查点

**Audit ID:** ASFS-AUDIT-20260920-HQT01  
**Unchanged candidate:** ANG-20260919-HWS01  
**Status:** CLOSED EMBEDDED PRIME CIRCLES; FULL QUOTIENT NON-HAUSDORFF — SCOPED ADVANCE / STOP  
**Verdict:** 三检查点完成，无待修正的数学阻断项。每个 prime packet 在完整商中是闭嵌入圆；完整商仍非 Hausdorff。两个结论的 owner 相同，适用范围不同。

## 1. 实际输入与检查顺序

| 输入 | 实际核验的 SHA-256 |
|---|---|
| 285 原始冻结卡 | 41ae89afb4f65e3f27151d388ee5b148a491023eb5f5b897fe54b6e134991041 |
| 未改的 278 完整卡，含既有 outcome | b5f1451a57afcbf7150c9f6afe1febf7c6c5673cbb3968d1c5485022be906a4a |
| 未改的 278 主文 | 9a53b0b5b0fa0648547d7a9d74404de16a5db82406ddec097ea97259e6d5605c |
| 首次完整比较的 285 主文 | 6b5a3aff43b98b150f49107e7a7221bfa5d2a3311028a8438ebb02f3019d4344 |
| 行政补充后最终绑定的 285 主文 | 9abd155a9595c7dcc97363a9371f2b5008ac35614ea13192b335d2ee16f67dfe |

检查点 1 先完整读取 285 卡与所需的 278 原定义／证明，未读未来 285 主稿；独立完成并向主控发送根上有限性、完整商中的圆以及指定双序列的 raw 结论。随后才完整读取 285 主稿，进入检查点 2/3。

278 的周期／clock ledger 是卡允许使用的同对象依赖，并非重新证明或从其他候选移植。285 卡后续若追加行政 outcome，本报告仍绑定原始冻结字节，不把事后结论当作 raw 输入。

本报告是审查者唯一写路径；没有修改 278、冻结卡、主稿、其他 evidence 或注册表。复核不涉及数值实验、外部文献扩展、一般轨道闭包或全局 \(T_1\) 分类。

## 2. 检查点 1：全部根上的有限返回种子

令 \(F_n(p)=\{x:(H_n,x)\in B_p\}\)。在素数 hub \(q\) 上，非零 residue 立即逃逸，零 residue 的完整循环把 seed 除以 \(q\)。有限次后到达零只能来自零，因此

\[
F_q(p)=\begin{cases}\{0\},&q=p,\\ \varnothing,&q\ne p.\end{cases}
\]

特别地，\(p=2\) 没有遗漏：零 port 是一步循环，非零 port 逃逸；始终走零 word 的非零 profinite seeds 不会有限步变成零。

对合数 \(n\)，令 \(\ell(n)\) 是最小真因子。原卡的完整 scan 从 2 开始，零 port 到 \(H_{\ell(n)}\)；每个非零 nonescaping port 到严格较小的 gcd hub。所以

\[
F_n(p)=nF_{\ell(n)}(p)\ \cup\
\bigcup_{\substack{1\le j<n\\d=\gcd(n,j)\ge2}}
\bigl(j+nF_d(p)\bigr).
\]

这是真实分支的等式，不只是必要条件；逆分支为 \(y\mapsto j+ny\)。强归纳给出有限性，并给出这些 seed 是嵌入的非负整数；不存在数值 cutoff 推断。

每个迟 scan \(S_{(n,d)}\) 只保持 seed 并在有限步到达第一个剩余真因子 hub，若没有则到 \(H_n\)。其 \(B_p\) fibre 就是相应已处理的 \(F_a(p)\)。剩余第一个因子本身可以是合数；归纳已覆盖它，不能擅自替换为从 2 开始的 scan。

例如保留的 \(S_{(6,3)}\) 直接到 \(H_3\)，不能用 \(H_6\) 的零 port 会下降到 \(H_2\) 来替代它。所有 escape 根的返回 fibre 为空。

由此 \(B_p\) 在每个 clopen 根上有限，故在拓扑 coproduct \(Y\) 中闭且具有离散子空间拓扑。它仍可全局无限；全部有限前像均保留。其 saturation 来自实际共同尾，等价于 278 已确立的单一完整 \(G\)-轨道。

## 3. 原卡的完整商比较与圆

记 \(M=Y\times\mathbb R\)、\(Q=M/G_c\)，只 quotient 实际扩张箭头，不再 quotient 实时间平移。令 \(A_p=B_p\times\mathbb R\)。实际箭头与全部实坐标给出

\[
\pi^{-1}(P_p)=A_p.
\]

主审 raw 证明使用了 open quotient：扩张群胚 étale，开集的 saturation 为开集，故 \(\pi\) 开。对 saturated \(A_p\)，
\(\pi(A_p\cap O)=P_p\cap\pi(O)\)，因而 \(\pi|_{A_p}\) 是到完整 \(Q\) 实际子空间 \(P_p\) 的 open quotient。

另由 \(A_p\) 闭及 quotient topology，\(P_p\) 闭。此处不声称任意闭集在 \(\pi\) 下都有闭像；关键是 \(A_p\) 为所考察集合的完整逆像。

选一个实际箭头 \(g_z:z_p\to z\)，令 \(c_z=c(g_z)\)。在 \(A_p\) 定义

\[
\Theta(z,u)=[u-c_z]\in\mathbb R/(\log p)\mathbb Z.
\]

换选箭头只使 \(c_z\) 改变 \(\log p\) 的整数倍。\(B_p\) 的离散子空间拓扑保证此相位映射连续；全部有限前像不是被删除后再选代表。

对 \(g:w\to z\)，有 \(c(g)=c_z-c_w+k\log p\)，故扩张箭头保持相位。反之相位相等可用 \(g_w^{-1}\)、真实 isotropy 的整数次幂、\(g_z\) 复合实现。相位 fibres 恰为完整扩张等价类。

借助实际子空间的 quotient 比较，得到连续诱导逆映射 \(P_p\to\mathbb R/(\log p)\mathbb Z\)。它与 canonical \(\kappa_p([t])=\pi(z_p,t)\) 互逆，证明 homeomorphism onto subspace，而非仅连续双射。

于是 \(P_p\) 是完整 \(Q\) 中的闭嵌入圆。实平移在相位上加 \([t]\)，其最小正周期与正重复仍为 \(\log p\)、\(r\log p\)；这些来自完整 clock isotropy，不是另加 roof。

## 4. 指定的 \(H_3\) 全商分离测试

令 \(N=k!\)，取实坐标均为零的两个 source seeds \(3^N\)、\(2\cdot3^N\)。各经过 \(N\) 次零 port 循环，再分别以 residues 1、2 在第 \(2N+1\) 步到达同一个 \((E_0,0)\)。

两个实际逆前缀的 affine formulas 是

\[
\theta_\alpha(t)=3^N+3^{N+1}t,\qquad
\theta_\beta(t)=2\cdot3^N+3^{N+1}t.
\]

所以 retained lag 为 0，两侧 \(D\) 相等，clock 为 0。这确实使两扩张点逐项等价，不需加仿射箭头或把实时间也 quotient 掉。

对任意有限模数 \(m=3^a b\)，其中 \((3,b)=1\)，充分大 \(k\) 使 \(3^{k!}\) 在 \(3^a\) 分量为 0，并在 \(b\) 分量为 1：有限单位群中 3 的阶最终整除 \(k!\)。CRT 给出全部模数下的兼容极限 \(e\)。

因此极限 seeds 是 \(e,2e\)，其中 \(e\) 的 3-primary 分量为零、其他 primary 分量为 1。它非零，两个 seed 都保留在 \(D_3\) 中，始终遵循零 port 的周期根 word。

主审 raw 排除连接箭头的方法是 mod-2：除以 3 和 scan 保持 seed parity，而 \(e\) 为奇、\(2e\) 为偶，所以任意前向共同尾都不可能相等。它们甚至没有基础 \(G\) 箭头，更不扩张等价。

于是同一个商序列收敛到两个不同商点，完整 \(Q\) 非 Hausdorff。等价地，实际扩张等价关系在 \(M^2\) 中不闭。该序列是所有模数上的精确证明，不是数值试验。

极限点在所有 \(B_p\) 之外；有限项是被完整保留的逃逸点。该障碍不否定各 \(P_p\) 的闭嵌入圆性质，也不证明全局非 \(T_1\)。

## 5. 检查点 2：全文比较与证明校准

主文的有限 hub recursion、所有 late scans 与 escape roots 均与 raw 推导一致。没有用 root-word 周期冒充 full-state 周期，也没有把逐根有限误称全局有限。

Lemma 3 使用比 raw open-map 证明更直接的闭 saturated 论证：若 \(\pi_p^{-1}(C)\) 在 \(A_p\) 闭，因 \(A_p\) 闭便在 \(M\) 闭；又它等于 \(\pi^{-1}(C)\)，所以 \(C\) 在 \(Q\) 闭。反向由连续性得到。这个论证正确，不需要 \(Q\) Hausdorff。

Theorem 4 的选定箭头 \(a_z=(z,m_z,z_p)\) 从 \(z_p\) 到 \(z\)，clock 为正的 \(\log D_z\)；相位 \(u-\log D_z\) 因而方向正确。共轭式、相位等价的逆构造以及 canonical map 的双向连续性均通过。

Theorem 5 用 \((3^j-2\cdot3^i)e=0\) 排除极限共同尾，与 raw parity 方法等价。括号内整数非零，278 已证的非零整数乘法单射足够；不需要错误地把 \(K\) 当成整环。

完整读取的主文未发现数学修改要求。随后主控仅补入 Paper ID/result-type 两行及末尾 Reproducibility and disclosure 小节；主审定点读回这些行政补充，其内容与实际方法、输入和内部复核范围一致。去掉这两项补充后的字节 SHA 恢复为首次全文比较的哈希，证明正文未变；最终绑定更新如上。没有重做未改变的 278 ledger 或审计未授权的其他架构。

## 6. 检查点 3：最强反方与披露

- **约化 quotient 偷换完整子空间？** Lemma 3 明确解决了这一风险；圆不是只存在于换 owner 后的返回约化中。
- **连续双射冒充 embedding？** 证明提供连续相位逆，不依赖目标 Hausdorff 的紧性捷径。
- **同一 itinerary 被当成同一 seed？** terminal arithmetic topology 完整保留；\(e,2e\) 的不同有限 residue 正是负控所需。
- **“圈闭”与“全商非 Hausdorff”冲突？** 不冲突。闭 Hausdorff 子空间不使其周围空间 Hausdorff；反例位于非返回部分。
- **是否增加 geometric／naturalness 信用？** 只新增同对象 T2 拓扑事实，不关闭 scan 的自然性，不产生局部流形、contact、Hamiltonian、T3 或形式 Route 结论。
- **是否扩大负结论？** 只停止完整 coarse quotient 的 Hausdorff-ambient promotion；不称原 étale 群胚非 Hausdorff，不断言全局非 \(T_1\)，不分类全部 orbit closures。

采用 ARS academic-research-suite 三检查点。两个继承同模型设置的辅助只收到 raw 卡与许可的 278 输入：branch_return_controls 核对逐根有限性，haar_seed_branch_check 核对指定 \(H_3\) 序列。它们未读 285 主稿或其他审查答案，未写文件或开展额外普查；主审承担完整 quotient／embedding 证明与全文比较。

主审自己的 raw 全结论先于主稿读取发送；辅助 sector 结果与之吻合。这是原卡先行的内部执行，不是不同模型的独立误差保证。主控、主审共享项目上下文；本报告不是外部同行评审或机器形式验证。

最终建议维持 **scoped advance / stop**：保留完整 owner 中闭嵌入 prime circles 的正结果，同时停止其完整商作为 Hausdorff classical ambient flow 的提升。自然性 OPEN；T3 未供应／未开展；经典 A0/A1/A2 不适用，formal UNASSIGNED，Route B NOT INVOKED。278 未改，241/242 未触碰。
