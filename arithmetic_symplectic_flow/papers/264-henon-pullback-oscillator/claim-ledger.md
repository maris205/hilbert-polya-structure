# CS14 主张台账

Scope ID: `ASFS-DISCOVERY-20260919-CS14`。

Current status: `COMPLETE; FINITE-320 FIT SIGNAL; JOINT AND ROBUSTNESS GATES FAIL`。

| 主张 | 当前证据 | 范围 / 不蕴含 |
| --- | --- | --- |
| 原F保面积且U酉 | ESTABLISHED；paper §2直接推导、形式审查 | 不是算术或自然量子化 |
| H同谱J、S；仅依赖h/κ | ESTABLISHED；paper §2剪切/傅里叶推导、形式审查 | 不保留a/η独立性或全部动力学 |
| 正闭形式、≥2h、紧预解 | ESTABLISHED；paper §2、形式审查 | 无目标谱身份 |
| 形式体积领先系数 | ESTABLISHED；paper §3、形式审查 | 不是N_J/N_K Weyl定理 |
| Hermite矩形Gram、固定指标Ritz收敛 | ESTABLISHED；paper §4、形式审查 | 非n52误差证书 |
| 固定主3/2读出有限拟合 | OBSERVED；n52全320 M1.149170%，低于旧3.525125% | 仅有限值，全部目标已知 |
| 联合训练门 | FAIL；J1.856056>1、W100约9.568466%、G1003.712112% | n24较低M不覆盖其它失败 |
| 三小控制及SOURCEOFF | 全部通过；SOURCEOFF主全320 M211.092935% | 不是素数消融或算术证据 |
| 细截断/宽度稳定性 | FAIL；全320 G12.534604%/2.314617%/3.025945% | 不能晋升连续320优势 |
| 原始J读出 | 固定诊断；n52全320 M61.840870% | 没有事后重选主读出 |
| 执行完整性 | 30调用/29独立点/66全分解，exit0；185文件保留 | 预算耗尽不称优化收敛 |
| 保存数组复核 | ANALYZED；68 NPZ/10态/16锁/184库存项一致 | 非独立科学重跑VERIFIED |
| 真实Weyl计数/系数/余项 | OPEN | 不由形式体积代替 |
| 内生算术、假目标等预算、PROVES_TOO_MUCH | OPEN | 所有目标已知 |
| A0/A1/A2/T0–T3 | NOT EVALUATED | formal UNASSIGNED |
| Route B | NOT INVOKED | 241/242暂停 |

定义/预算身份见[candidate-card.md](candidate-card.md)，完整论证见
[paper.md](paper.md)。[形式审查](evidence/preflight-form-review.md)未发现数学阻断，
但这不是外部同行评审或正确性认证。[保存输出报告](evidence/saved-output-review.md)
另检有限证据；当前决定为保留解析/数值信号、stop稳健增益晋升、fork。
本表随实际证据更新，不修改冻结输入。
