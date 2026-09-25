## Material Passport

- Origin Skill: ars-codex:academic-research-suite / experiment-agent
- Origin Mode: validate
- Origin Date: 2026-09-19
- Verification Status: ANALYZED
- Version Label: DS03-validation-v1

## Validation Report

**Scope ID:** `ASFS-DISCOVERY-20260919-DS03`。  
**Source:** DS02-D/S 的已存矩阵、谱态和目标；没有新动力学实验。  
**Overall Confidence:** CAUTION — 有限描述性诊断，不提供概率置信等级。

### 数值发现

| 量 | 检验类型 | 观察 | 解释界限 |
| --- | --- | --- | --- |
| 共同 H、权重均值、动能/势能和 | 数组身份与代数交叉核对 | H相同；重构误差约1e−14 | 非无限算子认证 |
| 低三态能量方差 | 有限本征态诊断 | D 标准差约9，S约6.9–9.0 | 本征于 U 不等于本征于 H |
| 动态纯期望 MAPE | 原数组替代读出 | 2.40003%，原2.29046% | 继承同一 U 态及训练目标，非独立对照 |
| 动态纯期望 MSE | 同上 | 11.18609，原12.22891 | 与 MAPE 方向不同，不能称全面改善 |
| 交换子 | 有限矩阵乘法 | D/S相对Fro约0.826/0.812 | 原固定kick不是连续 H 对象 |

没有 p 值、CI、效应量检验、随机样本模型或多重显著性判定。
100 个排序目标不是 100 次独立重复，250 个本征态也不是独立实验。

### Warnings

历史动态参数已用全部百点目标选择；静态未重新优化。纯期望后处理
改变排序和自身首点尺度，且其诊断问题在看过原拟合结果后提出；
冻结卡保证执行透明，不把探索性问题变成事前盲测。
原始小取整误差可经小首间隙放大；原态的近正交误差、简并或近简并
敏感性和网格收敛未在本轮认证。

### Fallacy scan

**Coverage: 11/11 checked**。不适用项说明理由，不将其记成经验通过。

| 项 | 适用性 / 风险 | 本次处理 |
| --- | --- | --- |
| 1. Simpson's paradox | 无抽样分组推断；不同误差指标方向确实不同 | 同时报 MSE 和 MAPE，不用单指标宣称全面改善 |
| 2. Ecological fallacy | 平均误差可能被误读为逐点保证 | 保留第2点偏差、全态范围和低态表；不从均值推出所有态性质 |
| 3. Berkson's paradox | 无相应条件化关联检验；存在历史择参选择性 | 不称保留集或普适模型排名 |
| 4. Collider bias | N/A：无因果回归或中介变量条件化 | 不拟合因果图，不作独立性宣称 |
| 5. Base-rate neglect | N/A：无分类器或条件概率报告 | 不把拟合误差转为算术正确概率 |
| 6. Regression to the mean | N/A：无随机极端组前后重复测量 | 现有确定性数据不提供此类因果证据 |
| 7. Survivorship bias | 低十态展示可能遮蔽全体 | 同报250态汇总，原250态和100目标不删除；来源搜索偏差仍保留 |
| 8. Look-elsewhere effect | 探索性读出诊断，非显著性检验 | 不称显著性，不选择较有利的 MSE 遮蔽 MAPE |
| 9. Garden of forking paths | 后验提出诊断，排序/定标均可改变结果 | 固定并公开两种排序的读出，保留原结果；不作确认性优越结论 |
| 10. Correlation/causation | 权重不同与拟合不同不构成普遍机制 | 只定位计算链，不称“混合越多越接近零点” |
| 11. Reverse causality | 参数由目标选择，不能反称零点被自然预测 | 明示拟合方向与历史训练，不称内生算术 |

### Reproducibility

- Method: no forward re-run; saved-array checks only.
- Verdict: N/A for new dynamical reproduction; prior DS02 run remains separate.
- 两个只读后处理命令、输入/输出 hash 可供复查。
- ANALYZED 不升级为 VERIFIED；独立代理的代数核对不是外部同行评审。
