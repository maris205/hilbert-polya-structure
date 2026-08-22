# Experiment plan (C106)

1. 固定变分势、参数、坐标顺序和 \(\Omega\)，以有理数实现梯度、Hessian、Jacobian。
2. 独立核验 \(DF^T\Omega DF=\Omega\)、\(\det DF=1\)、\(RFR=F^{-1}\)。
3. 解析指定的两个同步不动点和同步二周期，检查周期闭合及非重复性。
4. 计算二周期 monodromy、迹和 \(\det(I-zM)\)，与完全解耦的 \(\kappa=0\) 控制逐系数比较。
5. 使用独立 checker、SymPy 交叉核验、canonical replay 和十项 hostile mutation。
6. 仅在这些低周期结果稳定后，才进入 A1 的完整分割/漏轨道审计；A2 需要另行构造共同函数空间上的 transfer operator，不能从本包推断。

停止条件：若耦合差异消失、周期闭合失败、辛/可逆恒等式失败，或结果依赖浮点舍入，则不继续声称该候选具有 Route-A 价值。
