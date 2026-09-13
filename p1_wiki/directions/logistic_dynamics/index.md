# Session 1：Logistic Dynamics（离散 vs 连续）

[P1 Wiki](../../index.md) · [方向总览](../index.md) · [本页](index.md) · [结论](conclusions.md) · [路线图](roadmap.md) · [来源与阶段](sources.md)

## 这一页如何使用

这是第一阶段的 **Logistic-origin** 知识入口。它整理的是从 Logistic 映射及非自治 Logistic 构造出发、再转向物理首返与极坐标回归映射的 Route-A 探索；“离散 vs 连续”是本 Session 的组织视角，而不是已经完成的连续时间 Hilbert–Pólya 构造。

源档案当前冻结了 31 个阶段记录。其稳定主线是精确参数 `U_c` 上的 `LOG-0001` 极坐标 Fredholm 链，而早期数值匹配、控制实验和广度试探均保留为可追溯的历史材料。阶段状态、源锁和可复现边界以 [同步清单](../../../logistic_dynamics/sync_manifest.yaml) 与 [阶段索引](../../../logistic_dynamics/STAGE_INDEX.md) 为准。

> **跨方向边界。** 本页只编排顶层 `logistic_dynamics/` 档案。该档案内部确实保存了名为 Symbolic suspension、Hénon breadth pivot、Quantum graph 与 Renewal breadth pivot 的历史广度试探；它们在此仅是 Logistic-origin 路线的源绑定背景，**不与**顶层 `symbolic_dynamics/`、`henon_dynamics/` 或其他独立 Session 合并，也不替代它们各自的结论页。

## 建议阅读路径

1. 先读 [结论与边界](conclusions.md)，确认哪些是已归档的解析结论、哪些仍然缺失。
2. 再读 [路线图](roadmap.md)，了解从离散 Logistic 结构到极坐标传递算子的实际推进，以及唯一允许的重新开启门槛。
3. 需要定位论文、测试、源锁或阶段状态时，进入 [来源与阶段](sources.md)，再跳转到镜像中的原始材料。

## 一句话状态

`LOG-0001` 停放在 `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS` 的稳定解析检查点：已记录同一对象的核 Fredholm 行列式、带符号周期词迹账本及若干增长/阶数界；尚未得到素数原始轨道律、完成 ξ 恒等式、自然自伴量子化或 Route B 授权。

## 源档案入口

- [Logistic-origin 档案说明](../../../logistic_dynamics/README.md)
- [LOG-0001 稳定结果边界](../../../logistic_dynamics/LOG0001_STABLE_RESULTS.md)
- [探索关闭与交接](../../../logistic_dynamics/EXPLORATION_CLOSEOUT.md)
- [完整同步阶段索引](../../../logistic_dynamics/STAGE_INDEX.md)

本知识库只做导航和源绑定摘要；它不替代每个项目目录中的 `source_lock.yaml`、Route-A 评估、证书、测试或论文。
