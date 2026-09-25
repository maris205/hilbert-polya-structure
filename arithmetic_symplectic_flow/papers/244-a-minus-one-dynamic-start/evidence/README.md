# Evidence — ASFS-DISCOVERY-20260918-DS01

**Status:** `SOURCE SYNC COMPLETE; H1 BASELINE REPRODUCED`。
第一阶段完成源码/版本/依赖核对；后续用户确认后，实际运行了一次
DS01-H1。所有上游 JSON、日志仍是输入资料，与本次输出明确区分。

- [H1 执行前冻结卡](h1-card.md)
- [H1 运行结果](h1-result.md)
- [H1 原样 stdout](h1-stdout.json)

## 来源锁与同步方法

- Logistic: `https://github.com/maris205/riemann_logistic.git`，HEAD
  `e3419dda3d5515afd91a5dd6e8d8b8398f359dde`。
- Hénon: `https://github.com/maris205/riemann_henon.git`，HEAD
  `6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4`。
- [本地代码快照说明](../../../docs/upstream_snapshots/20260918/README.md)。

2026-09-18 UTC，先用 `git ls-remote --symref <url> HEAD` 核对远端，
再 `git clone --depth 1` 至独立临时目录，检查 HEAD、工作树和有关
实现。随后 `git clone --no-checkout --no-hardlinks <local-clone>
<snapshot-path>`，设置 origin 为公开 URL，设置 sparse-checkout，
并 `git checkout --detach <pinned-commit>`。没有 pull/merge/push，
不依赖临时克隆的 alternates。两个锁定工作树检查均为空改动。

恢复到指定版本的源码记录应查 HEAD，而不是再次取一个不固定的 main。
浅克隆的 `git show HEAD` 缺少父历史，不用其新增统计断言最近改动；
这里的“算法未变”来自与本地旧归档的对应文件 byte comparison。

## 可复查位置

| 断言 | 位置 |
| --- | --- |
| Logistic 冷却、预热及测试重定标 | [task12](../../../docs/upstream_snapshots/20260918/riemann_logistic/task12_13_experiments_v2.py)，24–58、86–96、150–168 行 |
| 六点原编号 epsilon 留出 | [task26](../../../docs/upstream_snapshots/20260918/riemann_logistic/review_experiments/task26_epsilon_out_of_sample.py)，83–125、150–199 行 |
| 降规模单次 Logistic 来源 | [task27](../../../docs/upstream_snapshots/20260918/riemann_logistic/review_experiments/task27_de_seed_robustness_reduced.py)，44–105 行 |
| Hénon 首参数与有序乘积 | [微观扫描器](../../../docs/upstream_snapshots/20260918/riemann_henon/6-henon_micro_param_scan_100_zeros.py)，39–104 行 |
| 单次 Hénon 原参数前向 | [solve 函数](../../../docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py)，21–95 行 |
| Hénon CSR 归一化 | [宏观扫描器](../../../docs/upstream_snapshots/20260918/riemann_henon/6-henon_macro_param_scan_100_zeros.py)，168–171 行 |

两个独立代理分工只读核对 Logistic 与 Hénon；主代理核对关键公式与
测试实现后集成。Hénon 11 个根目录 `.py` 和 8 个 `.ipynb` 与旧
`docs/prior_work/legacy/5-riemann_henon/` 的对应文件字节一致。
没有把这种模型交叉读取称为同行评审或数值验证。

## SHA-256

| File | SHA-256 |
| --- | --- |
| 初始 v1 范围卡（追加状态栏前） | `cd441166e60fe114cc4e848de9f32e99aa7001085d5444f5c131e6865064d081` |
| Logistic task12_13_experiments_v2.py | `b8de95c02c3348264d4628db2c30cbd58711890229464162fba38239f1d3ef30` |
| Logistic task26_epsilon_out_of_sample.py | `0b8b3d9f30379f2dd64211c756736ba0ba2cc0d8f9374f8aed1f44b61bf5568d` |
| Hénon 9-robustness_sensitivity.py | `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb` |
| 未改 plan.md | `9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0` |
| 未改 Route-A 镜像 | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` |
| 未改 Route-B 镜像 | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` |
| 未改 gemini_report.md | `850890644ed08463b4fc2569606232eaaa0f6671405579869c3513006951540b` |
| 未改 243 paper.md | `3791e61f087905a1d3b53db3de983c83edd21546f8443315973c4ce3dc429b9c` |

## 环境诊断与尚缺条件

第一阶段只运行了 import/version 检查，未调用实验函数：默认解释器
`/root/miniconda3/bin/python` 为 3.12.3，NumPy 2.4.4、SciPy 1.16.1、
mpmath 1.3.0；首次同时 import numba 报 `ModuleNotFoundError`，随后
`find_spec("numba")` 确认不存在。`nproc` 返回 12。未安装依赖。
这不是数值实验失败；也没有因此自动替换计算方法。其后 H1 使用已
存在的 NumPy/Matplotlib 运行成功，不依赖 numba；没有安装依赖。

## 完成边界

链接/ID/状态/保护文件 hash 校验与快照 Git status 核对属于交付检查；
它们不产出拟合或无限维结论。H1 的数值来自实际独立命令调用，详见
上述结果，后续可执行边界见 [方案](../experiment-plan.md)。

第一阶段交付检查：Node 标准库逐文件读取并解析本包、两个总索引与快照
说明，共 9 个 Markdown 文件（本包 6 个）、498 个本地链接；核对
5 个保护文件 SHA-256、19 个 Hénon 源码/notebook 字节对照，错误数
均为 0。两个快照 `git status --porcelain` 均为空；总索引
`git diff --check` 通过。另以 `find_spec` 确认 matplotlib 可用，
未导入或执行上游实验模块。验证不涉及 sparse 上游文档的未展开图片
和出版物链接；那些来源链接的缺省范围已在快照说明中注明。

H1 完成后于 2026-09-18 15:40 UTC 再校验实际变更：本包 8 个
Markdown 加两个总索引共 10 文件、514 个本地链接、6 个冻结/保护
hash、5 个主状态字段，错误数 0；stdout JSON 字段有效，MSE 与
历史完整值相等。stdout 共 87 bytes，SHA-256 为
`e9762469697898ed0381719e5826e402ba048e6794745fad3dc8bfdf6c6b48c7`。
两个快照工作树干净，总索引 `git diff --check` 通过。

另由一个独立代理只读核对 H1 卡、运行结果及正文解释，未发现必须
修正的证据越界；随后将“两个独立模型”措辞明确为“两个独立代理”，
不暗示跨架构验证。该代理未重跑实验；只有一次实际 H1 前向。
