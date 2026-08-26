# P22 Stage 4.5 Round 2：参考文献与引用语境独立审计

审计时间：**2026-08-25T15:05:27Z**  
模式：**Stage 4.5 / Mode 2 / authorized-correction 后从零全量复验**  
稿件 SHA-256：`e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed`  
参考文献库 SHA-256：`bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093`

## 结论

| 项目 | Round 2 结果 |
|---|---:|
| Phase A 来源存在性 | **3/3 VERIFIED** |
| 书目字段准确性 | **3/3 PASS** |
| Phase B 引用语境 | **21/21 SUPPORTED** |
| orphan references / dangling citations | **0 / 0** |
| SERIOUS / MEDIUM / MINOR | **0 / 0 / 0** |

本轮重新查询并读取一级来源；没有把 Round 1 的结论、缓存命中或此前
报告当作 Round 2 的验证证据。未配置或调用 cross-model。

## Phase A：逐条书目复验

| BibTeX key | 本轮一级来源 | 核验结果 |
|---|---|---|
| `Deninger2025Rational` | [arXiv 记录](https://arxiv.org/abs/2508.05329)、[v1 记录](https://arxiv.org/abs/2508.05329v1)、[v1 HTML](https://arxiv.org/html/2508.05329v1) | Christopher Deninger、题名、2025-08、arXiv `2508.05329`、主分类 `math.AC`、DOI `10.48550/arXiv.2508.05329`、v1 与 2025-08-07 提交日期均与 BibTeX 一致；当前 submission history 只列 v1。 |
| `DeningerMellit2019` | [EMS Press 出版页](https://ems.press/journals/rsmup/articles/16288)、[作者原始 arXiv 稿](https://arxiv.org/abs/1803.00812)、[Numdam 期刊档案](https://www.numdam.org/articles/10.4171/RSMUP/32/) | Christopher Deninger、Anton Mellit、题名、期刊、卷 142、页 93--102、2019、DOI `10.4171/RSMUP/32` 全部一致。原始论文 Theorem 1.1 确实计算局部化单子代数到截断 Witt 向量映射的核；全文未出现 `sheaf`、`fppf`、`finite flat` 或 `descent`，故稿件对其代数范围的限定准确。 |
| `StacksProject` | [官方引用说明](https://stacks.math.columbia.edu/tags)及稿件点名的官方 tag 页面 | 官方建议的作者、题名、URL 与年份字段均和 BibTeX 一致；根 URL 与全部点名 tag 可访问。 |

另对 Deninger v1 的第 3、14、19--25 页重新核对：稿件使用的 Eq. (4)、
Eq. (20)、Theorem 3.4、Propositions 4.3/4.5、Example 4.4、Corollaries
4.6/4.7 以及第 25 页 lifting question 的定位均准确。

## Phase B：21 个引用命令逐项复验

| # | 稿件定位 / 引用 | 本轮原始来源支持关系 | 结果 |
|---:|---|---|---|
| 1 | L125，Deninger p.25 | v1 第 25 页明确提出在 `fp` 或 `fppf` topology 上，sheafified Verschiebung 能否提升到 sheafified reduced monoid algebra。 | SUPPORTED |
| 2 | L134，Deninger §§3--4 | §3 引入 `NoethAffSch`，§4 说明 site 的底层范畴采用 small `AffSch` 或 `NoethAffSch`。 | SUPPORTED |
| 3 | L148，Theorem 3.4, p.19 | Theorem 3.4 断言 rational Witt presheaf 在 noetherian affine schemes 上满足 fpqc sheaf condition。 | SUPPORTED |
| 4 | L150，Proposition 4.3, p.21 | Proposition 4.3 给出 sheafification 后的 epimorphism。 | SUPPORTED |
| 5 | L170，Deninger §4 | 原文分别定义 `fp` covering 并在结尾分别提出 `fp`/`fppf` lifting question；稿件未混同两种 topology。 | SUPPORTED |
| 6 | L236，Corollary 4.6, p.23 | Corollary 4.6 确在 Dedekind rings 的 `fp` site 上写出 sectionwise equality；稿件用 citation 归属原命题，其后的修正由稿件自身 descent calculation 承担。 | SUPPORTED-AS-ATTRIBUTION |
| 7 | L250，Propositions 4.3/4.5, pp.21--23 | 4.3 提供 sheaf-level local preimages；4.5 在 covers 可由 integral domains refinement 时给出 injectivity。 | SUPPORTED |
| 8 | L253，Corollary 4.7, p.24 | 原文转向 suitable non-subcanonical topology，并给出 finer-than-`f` pretopology 下的 sheaf isomorphism。 | SUPPORTED |
| 9 | L256，Deninger--Mellit Theorem 1.1 | Theorem 1.1 给出目标为 truncated Witt vectors 的 kernel presentation，正是稿件所述较早代数结果。 | SUPPORTED |
| 10 | L260，Stacks Tags 03CN/010I/06XP | [03CN](https://stacks.math.columbia.edu/tag/03CN) 给出 abelian sheaves 的局部 exactness；[010I](https://stacks.math.columbia.edu/tag/010I) 给出 extension pullback/pushout；[06XP](https://stacks.math.columbia.edu/tag/06XP) 连接 Yoneda extensions 与 `Ext^1`。 | SUPPORTED |
| 11 | L339，Deninger Eq. (4), p.3；Eq. (20), p.14 | Eq. (4) 是 reduced monoid algebra 到 rational Witt vectors 的 `omega`；Eq. (20) 是 `V_N(f)(T)=f(T^N)`。 | SUPPORTED |
| 12 | L385，Stacks Tag 03CN | 03CN 以覆盖后的局部 lift 描述 exactness，支持 sheaf epimorphism 不必 objectwise surjective。 | SUPPORTED |
| 13 | L477，Deninger Example 4.4, p.22 | 原例通过 full big-Witt sheaf 检测 nilpotent Witt class 的非零性，与稿件调用的 detection principle 一致。 | SUPPORTED |
| 14 | L502，Deninger Proposition 4.5, pp.22--23 | 其假设是每个 covering 可 refinement 为 integral-domain covering，结论是相应 map injective。 | SUPPORTED |
| 15 | L511，Stacks Tag 00HS | [00HS](https://stacks.math.columbia.edu/tag/00HS) 是 flat maps 的 going-down lemma；稿件的 minimal-prime contraction 使用方向正确。 | SUPPORTED |
| 16 | L514，Stacks Tag 0AUW | [0AUW](https://stacks.math.columbia.edu/tag/0AUW) 断言 Dedekind domain 上 module flat 当且仅当 torsion-free。 | SUPPORTED |
| 17 | L774，Deninger Example 4.4, p.22 | 原例给出 dual-number 情形的相应非零控制。 | SUPPORTED |
| 18 | L811，Stacks Tag 010I | 010I 定义 extension 沿 quotient-side map 的 pullback 与沿 kernel-side map 的 pushout，并说明双变量函子性。 | SUPPORTED |
| 19 | L813，Stacks Tag 06XP | 06XP 将 Yoneda extension group 与 derived `Ext^1` 识别。 | SUPPORTED |
| 20 | L917，Deninger Corollary 4.6, p.23 | 准确归属原文的 Dedekind-ring sectionwise equality；稿件反例的正确性另属内部证明审计。 | SUPPORTED-AS-ATTRIBUTION |
| 21 | L975，Deninger Corollary 4.7, p.24 | 原文确对 finer non-subcanonical topology 给出正面 isomorphism comparator，与稿件限定的 subcanonical sites 不冲突。 | SUPPORTED |

## Ghost-citation 与格式检查

- `Deninger2025Rational`：14 个命令；`DeningerMellit2019`：1 个；
  `StacksProject`：6 个；合计 21。
- cited-key 集合与 3 个 BibTeX key 完全相等：orphan `[]`，dangling `[]`。
- 全文统一使用 `natbib` 数字制与 `plainnat`；21 个命令都是合法的
  `\cite[locator]{key}` 或 `\cite{key}`。
- `p./pp./Sec./Secs./Thm./Prop./Props./Cor./Tag/Tags` 的 locator 用法内部一致。
- 未发现 key、作者、年份、DOI、卷页、定位或引用语境错误。

因此，Round 2 可记录为：**Phase A 3/3 VERIFIED；Phase B 21/21
SUPPORTED；零引用问题。** 该结论只覆盖已列来源和已枚举 citation
surfaces，不是对全文数学正确性或未来版本变化的保证。
