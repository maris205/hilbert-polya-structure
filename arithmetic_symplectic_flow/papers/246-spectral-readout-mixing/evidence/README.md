# DS03 证据、输入锁与执行记录

**Scope ID:** `ASFS-DISCOVERY-20260919-DS03`。  
**Status:** `READOUT DIAGNOSIS COMPLETE; EXPECTATION-BASED LOGARITHM IDENTIFIED`。

用户“继续”承接 245 的现有数组分析建议。本轮没有动力学实验、
新前向、优化、U_tot 特征分解或数据上传；仅一次共同 H_base 的
Hermitian 特征分解与保存数组的只读矩阵运算。

## 输入锁

| 输入 | SHA-256 |
| --- | --- |
| [执行前卡](../candidate-card-frozen-v1.md) | `9a922208218ee5eee60ba8b47ddf18537f531d24506560d29c6d9294329c7092` |
| [D NPZ](../../245-dynamic-start-ablation/evidence/run-1/DS02-D/spectrum.npz) | `e5817dc78833b35f1f4f4b234c2ed41d6f0b2c213f56bebe128b7f0136ef0833` |
| [S NPZ](../../245-dynamic-start-ablation/evidence/run-1/DS02-S/spectrum.npz) | `f7d89909a4f48381b8af9f6e39f029bad4a719fc2d9bafd2b936070de8f6b2aa` |
| [245 比较 JSON](../../245-dynamic-start-ablation/evidence/run-1/comparison.json) | `378d861f7d86fb1afdb400f512b21f86d34b5753d956bd0ada76395f56acf982` |
| [上游 solve 源码](../../../docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py) | `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb` |

上游固定提交仍为 `6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4`。
NPZ 的原 250 态、100 目标、300 步路径和全部参数归属 245；没有复制
后改写成新输入。当前 card 仅追加完成状态，原卡字节独立保留。

## 实际命令与输出

工作目录为项目根目录；使用现有 Python 3.12.3 / NumPy 2.4.4，
BLAS/OMP 线程环境为 1，双精度，无依赖安装或 GPU。

| 命令记录 | 内容 | 退出 / 终端耗时 | stdout |
| --- | --- | --- | --- |
| [主命令](analysis-command.md) | 一次共同 H 分解、权重/残差/读出诊断 | 0 / 约0.232秒 | [readout-analysis.json](readout-analysis.json) |
| [补充命令](variance-command.md) | 原数组方差与对角投影距离 | 0 / 约0.128秒 | [variance-analysis.json](variance-analysis.json) |

两条命令只输出 stdout；保存记录通过显式文档补丁完成。均有 60 秒
超时，进程在首次观察内完成，无重试、stderr 或停滞。上述耗时是终端
返回的 wall time，不是跨平台性能基准。第二条不重复特征分解。

输出 hash：主 JSON
`b7dc9e9338dbb43d61704b3ddaf519cc1484f78540056a38d5d9b6692e6d04cd`；
补充 JSON
`c1ea7d673aefa11e9f8aeaf465a6c1ffe9c10b9c5b890efb9c7ec64ad5562fbf`。

## 数据与解释控制

eigh 默认以下三角对应的 Hermitian 矩阵工作。原 H 的 Hermitian
相对残差约 2.55e−16（245），本次特征分解对原 H 的相对残差约
1.58e−15。没有通过平均 H/H*、正交化原 U 本征态或截去异常态来
改善输出。归一化权重只作诊断，与源码未显式归一的 ee 分开核对。

独立子代理只读核对源码代数及最终解释；与主代理共享任务背景，
不是跨模型、盲审或外部同行评审。它要求明确原 ee/归一化 mu、
简并基依赖、移零和首点尺度改变指数关系，这些均已写入正文。

数学恒等式仅在明确的精确有限矩阵假设下成立；数值输出是当前
N=250 固定对象的观察。全部谬误适用性和未重跑说明见
[validation.md](validation.md)。

交接校验：本包及两个入口共 11 个 Markdown 文件、506 个本地链接，
7 处身份/状态一致；13 项输入/输出/保护文件 hash 匹配；两组方差
分解及取整界数值检查通过，错误数为 0。两个上游快照工作树干净，
入口 diff 无空白错误。独立核对提出的迹括号、归一化 mu 标签、
交换充分条件与 Frobenius 分母表述已修正；未因此重复数值计算。
