PLAN_READY

总分：55/60

六轴评分：
- 逻辑主线：9/10
- claim-evidence 对齐：10/10
- 数学精度 / 合法域：9/10
- 来源 / ownership：10/10
- 页预算：8/10
- front matter / figures：9/10

核验结论：
我已对 `/tmp/paper47_writer_candidate/PAPER_PLAN.md`、`CLAIMS_EVIDENCE.md`、`evidence/SOURCE_VERIFICATION.md`、`figures/data/canonical_summary.json` 与 authority 的 `PROOF_PACKAGE.md`、`DERIVATION_PACKAGE.md`、`OBJECT_MARKER_OPERATOR_CONTRACT.md`、`LITERATURE_NOVELTY_AUDIT.md`、`EXPERIMENT_PLAN.md`、`SOURCE_LOCK.md` 逐项交叉。核心边界全部守住：复相位只作左右酉乘而非共轭；compactness 走 row-Schur tail + finite-rank cross terms；`S_1` 必要性来自标准基偶对角；ordered edge 第二迹无额外 2；有限 cutoff 不抽无限 `zeta(2s)`；MT 的 gcd 因子与绝对收敛域分离；`det/det_2` 只声明局部对数；primitive 只指 gcd-one edge coordinate；无 priority / PSD / Hilbert–Pólya 夸大。`canonical_summary.json` 的 cutoffs、12 个 PASS、Route A rejected / Route B forbidden、以及写死的 summary/replay/result-ledger hashes 也与候选件一致。

CRITICAL
- 无。

MAJOR
- 无。

MINOR

1. `PAPER_PLAN.md:21-25`
   一句话贡献里“the coprime `(s,s;2s)` Mordell--Tornheim sum multiplied by `zeta(2s)`”对第一次见到的读者略有歧义：这里说的是 coprime kernel `P(s)`，不是直接说 full `\zeta_MT` 本体。
   最小修复：改成更显式的首次触达表述，例如“`zeta(2s)P(s)` with `P(s)=\sum_{(a,b)=1} a^{-s}b^{-s}(a+b)^{-2s}`, equivalently `zeta(2s)\zeta_MT(s,s;2s)/\zeta(4s)`”。

2. `PAPER_PLAN.md:255-258, 284-290, 273-276`
   Section 8 说要报告“twelve exact comparison PASS fields”，但当前 Table 2 只计划放 cutoff / edge / loop counts；12 个 PASS 名称本身没有明确落位。
   最小修复：在 Table 2 增加第二 panel，或在 Appendix D 明写“一张 compact checklist 列出 12 个 PASS key names”，这样 evidence 绑定更可审计。

3. `PAPER_PLAN.md:213-214, 269-270`
   compactness 证明路线是对的，但计划文本若能点名 finite-compression 对象会更稳。
   最小修复：把 “tail Schur estimates plus finite-rank cross terms” 收紧成一句含对象的表述，例如“prove `||E_s-P_N E_s P_N||->0` via tail Schur bounds plus finite-rank cross terms”。

4. `SOURCE_VERIFICATION.md:27-33`
   Bradley–Zhou 这一条目前主要依赖 arXiv record 与其中 journal reference；若最终 bibliography 采用期刊条目，最好把期刊元数据再直接核一遍，避免 reviewer 抓“journal form was not independently checked”。
   最小修复：要么最终 bib 明确用 arXiv primary record，要么在此条补一句“journal metadata independently checked against the journal record”。

简评：
这份 plan 的强项非常明确：主线干净，central theorem 没被 shared infrastructure 稀释，claim-evidence firewall 写得扎实，authority 边界意识很强。尤其值得肯定的是：`PAPER_PLAN.md:118-124` 的 complex-parameter firewall、`80-103` 的迹与 determinant 合法域、`231-239` 的“无限 scale 才抽 `zeta(2s)`”提示、以及 `245-250` 的 primitive/type/sign 防误读，全部与 authority 完整一致。

唯一稍弱的是页预算：`§2` 的 ownership synthesis 与 `§6` 的 second-trace + determinant corollary 都比较密，所以我给 8/10。但这仍是可执行的压缩，不构成 major。

结论：
这版可以进入 `paper-figure` / `paper-write`。建议先吸收以上 4 个 MINOR 打磨点，但它们都不是阻塞项。

