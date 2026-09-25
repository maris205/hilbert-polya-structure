# CS13 单次执行合同 v1

Scope ID: `ASFS-DISCOVERY-20260919-CS13`。

State: `FROZEN BEFORE IMPLEMENTATION AND COMPUTATION`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/263-factorized-drift-spectrum/run_search.py
```

对象、算法与全部停止条件见[candidate-card.md](candidate-card.md)。两族
各9种子+24优化调用，上限66对训练、149物理三对角全分解、零SVD；
另一次7点Gauss节点构造如实登记。小控制在唯一正式进程内完成。
主控独占启动；代码、输入和预审记录先SHA锁。独立审查只读，不另跑谱。
既有本地自动实现/执行授权有效，不重复索要命令许可。

科学输出只写本包evidence/run-1，排他创建。600秒+10秒终止宽限，
单BLAS线程、每30秒监控，RSS1GiB提示/输出1GiB硬限。失败不自动修复
重跑，保留实际执行计数、日志和退出码。不安装/GPU/生成新目标/外传/
Git提交/推送/PDF。241/242继续暂停。保存输出复核可到ANALYZED，不能
冒充独立重跑VERIFIED；工作流完成不等于数学成功。
