# DS07 数学证据

**Scope ID:** `ASFS-DISCOVERY-20260919-DS07`。  
**Current status:** `STRONG L2 LIMIT ESTABLISHED; ENERGY/SPECTRAL PROMOTION STOP`。

本包没有执行新的计算程序、FFT、前向或本征求解。证据为
[不可变证明前卡](../candidate-card.md)、[全文证明](../paper.md)与
[独立证明审查](independent-proof-review.md)。

证明输入：固定[-L,L)多项式代表元、同一300步动态起点规律、固定
hbar及L、偶数N模式[-N/2,N/2−1]、等距采样与三角插值。
来源关系已沿[249](../../249-periodic-kick-domain/candidate-card.md)
锁定原 sensitivity solver，不复制或修改上游代码。

独立代理从冻结卡重建证明，主集成者逐步核对。它们属于同一模型
家族协作，非跨模型或外部同行评议；不以代理赞同作为定理证明。
没有虚构实验运行或统计验证的 Material Passport。

关键控制：无踢自由步；固定Fourier输入；算子范数≥1反例；
L²收敛但动能发散例；循环移位近似的谱对应反例。
这些控制不改变原对象，也不转移其结果。新对象、参数、随N步数
及新读出需独立冻结，原247稳定性停止不被撤销。

## 集成检查回执

本轮248–250共19个Markdown文件（含两个根索引）核对545个本地
引用、9组当前编号/状态、16个SHA256锁和248的1600行CSV，错误0。
三个证明/分析前卡保持原字节；两脚本、四个旧NPZ、两个新结果、
原solver、plan、两Route镜像与243旧论文的锁均符合。
两份独立上游snapshot工作树保持clean，两个根索引git diff --check
通过。这里只核对文件完整性，不据此授予数学或Route信用。

250集成证明经只读复核无阻塞项：内积约定、原动态路径、踢后自由步
及固定乘积与声明范围一致；审查没有新运行或修改历史证据。
