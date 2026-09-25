# CS08 — execution card v1

Scope ID: `ASFS-DISCOVERY-20260919-CS08`。执行前冻结。
沿用用户继续的本地自动实现/运行授权，不追加逐命令批准门。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/258-shape-dispersion-heat-search/run_search.py
```

工作目录arithmetic_symplectic_flow，单次启动，最多345传播/10额外
保存态SVD/22静态分解；零优化回退、零新目标、零异常重试。
主候选卡规定9种子及maxfev24的五族预算，无效族省下预算不转移。
先形式审查新势全局最低值范围，再独立代码静态审查，之后才启动。
600秒硬限/10秒宽限由实际timeout执行，不由manifest字符串代替。

约30秒监控本进程PID/RSS与本包run-1增长；1GiB内存为提示，不因
异常提示擅自中止。输出≤1GiB；存在run-1拒绝覆盖，异常保留证据。
记录实际时间、计数、退出码、版本、runner/输入锁哈希与文件清单。
普通INVALID按候选卡保留并继续其余计划；求解或实现异常停止整次。

旧256/257代码与数组仅只读，允许导入锁定256的potential和cooling
数学函数，不修改其全局量，不执行旧main/propagate/readout。
新势必须用新最低值函数及独立缓存键。完整旧目标从原锁输入读取。
运行标签UNVERIFIED；保存结果分析ANALYZED，不冒称独立重跑、严格
误差认证或外部同行评审。241/242仍暂停；无外部写入或发布。
