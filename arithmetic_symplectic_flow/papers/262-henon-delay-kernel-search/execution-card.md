# CS12 单次执行合同 v1

Scope ID: `ASFS-DISCOVERY-20260919-CS12`。

State: `FROZEN BEFORE IMPLEMENTATION AND COMPUTATION`。

在ASFS根目录按以下命令执行一次：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/262-henon-delay-kernel-search/run_search.py
```

对象和全部算法约束见[candidate-card.md](candidate-card.md)。A/D均两参数；
8种子+20优化调用/族，最多56对训练。训练n23/n27，后检n31/n39/n47，
六小控制与最多四项D的END/ZERO消融，合计最多128前向/full real SVD。
无动能/静态eigh、求根、额外保存态SVD或新目标生成。
旧输入锁定，新runner在形式及独立代码审查完成后单独锁SHA。

仅本包evidence/run-1为科学输出及监控路径，排他创建；30秒查看事件与
资源。RSS1GiB仅提示，输出1GiB硬限；600秒timeout及10秒终止宽限。
任何科学控制失败、异常或超时保留实际输出并停止，不修复重试。
依既有本地自动执行授权，不重复索要逐命令许可。无GPU/安装、外传、
提交/推送/出版/PDF；241/242仍暂停。预审允许纯导入/AST/日志/元数据测试，
不允许未登记的前向、分解、优化或预算预演。

父进程记录实际退出码、开始/结束与输出清单。执行护照UNVERIFIED；
另做保存数组分析时记ANALYZED，不回写为独立复现VERIFIED。
所有Route坐标未评价，B NOT INVOKED；不把工作流完成当数学成功。
