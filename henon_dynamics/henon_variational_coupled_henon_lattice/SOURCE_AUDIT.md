# Source and overlap audit (C106)

## 输入来源

本包没有读取外部数据集或论文数值；所有数值均由 `code/c106_variational_lattice.py` 从势函数的有理参数
\(a=7,\kappa=1/4\) 直接生成。SymPy 脚本是独立代数复核，不是 producer 的输出缓存。

## 项目内相邻工作

* 现有 `henon_time_ordered_ruelle_cocycle` 研究按时间排序的单站点 cocycle；C106 改为**自治的两站点变分耦合**，primitive object 是四维真实轨道，不使用外部时间字母。
* 现有有限标记/first-passage 批次（C64–C103）研究有限群或标记随机变量；C106 不读取这些证据，也不把标记数据当作周期轨道。
* 现有 operator/ownership 防火墙明确要求共同函数空间和独立 trace 公式；C106 只提交有限 monodromy witness，故 A2 保持 OPEN。

## 复核边界

本审计不宣称文献新颖性。正式立项前仍需对耦合 Hénon lattice、coupled map lattice、variational recurrence 和 open/holomorphic transfer operator 做检索；本包先作为可证伪候选保存。
