# 2026-09-18 upstream code snapshots

此次按用户要求同步 Logistic/Hénon 更新。原始 `docs/prior_work/legacy/`
归档未改动。研究解释与下一步试验见
[244 工作包](../../../papers/244-a-minus-one-dynamic-start/README.md)。

| Repository | Frozen HEAD | Upstream commit date |
| --- | --- | --- |
| [Logistic](https://github.com/maris205/riemann_logistic/tree/e3419dda3d5515afd91a5dd6e8d8b8398f359dde) | `e3419dda3d5515afd91a5dd6e8d8b8398f359dde` | 2026-09-03 +08:00 |
| [Hénon](https://github.com/maris205/riemann_henon/tree/6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4) | `6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4` | 2026-09-18 +08:00 |

两目录是独立、detached-HEAD 的浅 Git 快照，origin 指向对应公开上游；
没有推送。工作树使用 sparse checkout，仅展开 `.py/.md/.json/.npy/
.txt/.toml/.yaml/.yml/.csv/.ipynb/.log` 与许可证，不展开论文 PDF、TeX、
图片和投稿压缩包。Git 对象保留该提交的来源内容；这里没有生成或编译
出版物。上游 Markdown 中引用的未展开论文/图片链接可能在本地不可用，
这不是新论文包的证据链接。

不要在这些锁定快照内直接运行会覆盖既有结果的脚本，也不要对快照
执行 `git pull`。后续更新应另建日期/提交位置，或明确解锁并记录新版本。
本地初次准备使用临时完整克隆，再以 `git clone --no-checkout
--no-hardlinks` 制作独立副本；不依赖临时目录的 Git alternates。

已保存的 JSON、日志和笔记本输出是**上游已有结果**，不是 244 本次
重跑。来源核对不能代替数值复现或独立统计检验。

## 父仓库归档方式（2026-09-25）

父仓库另将这两个锁定快照中**本地已展开、且由上游 Git 跟踪的文件**
按普通文件归档，保留原始内容和文件模式，包括上游已跟踪的日志。
没有展开稀疏检出之外的文件，也没有改动上述来源提交或重跑实验。

本地两个独立仓库的 `.git` 元数据保留原位，但不纳入父仓库；父仓库
不使用 gitlink 或 submodule。因而，从父仓库新克隆得到的是可直接
浏览的普通文件快照，而不是独立的浅 Git 仓库，也不包含其提交历史。
上表的固定提交链接仍是核对完整上游来源的依据；需要独立 Git 历史时，
应在别处按该提交另行获取，不要修改这里的锁定副本。
