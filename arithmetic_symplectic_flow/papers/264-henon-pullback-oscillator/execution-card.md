# CS14 单次执行合同 v1

Scope ID: `ASFS-DISCOVERY-20260919-CS14`。

State: `FROZEN BEFORE IMPLEMENTATION AND COMPUTATION`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/264-henon-pullback-oscillator/run_search.py
```

定义/输入/阈值见[candidate-card.md](candidate-card.md)。至多30对训练，
68次完整实对称分解，零SVD；所有小控制包含在唯一科学进程中。
先完成形式/代码审查和SHA锁；root独占启动，evidence/run-1排他创建。
每30秒监控，RSS1GiB仅提示，输出1GiB硬限。失败不自动重跑，保留
计数/错误/退出码。既有自动执行授权有效；不安装/GPU/外传/新目标/
Git提交推送/PDF，241/242继续暂停。保存数组复核仅ANALYZED。
