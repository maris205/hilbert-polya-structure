# CS15 单次执行合同 v1

Scope ID: `ASFS-DISCOVERY-20260919-CS15`。

State: `FROZEN BEFORE IMPLEMENTATION AND COMPUTATION`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/265-pullback-cutoff-audit/run_audit.py
```

依[candidate-card.md](candidate-card.md)固定对象、24次完整分解及控制；
零优化/新目标。先形式/代码预审和输入/源码锁，root独占启动，输出目录
排他创建，每30秒监控。RSS2GiB提示，输出1GiB硬限，失败不自动重跑。
沿用本地自动实现/有界执行授权；ARS逐命令确认模板不覆盖用户既有授权。
无安装/GPU/外传/提交推送/PDF；264只读，241/242暂停。保存证据分析不
冒充独立重跑VERIFIED。源码及锁以实际SHA记录，命令不允许执行中修改。
