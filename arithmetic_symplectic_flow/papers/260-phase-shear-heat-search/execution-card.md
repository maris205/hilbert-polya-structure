# CS10 — 单次有界执行卡 v1

Scope ID: `ASFS-DISCOVERY-20260919-CS10`。  
State: `FROZEN BEFORE COMPUTATION`。

[候选卡](candidate-card.md)唯一规定对象、54对训练调用、六控制、固定后检/
探针、124传播/full SVD和11静态分解上限。主控独占启动权。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/260-phase-shear-heat-search/run_search.py
```

工作目录arithmetic_symplectic_flow；排他输出evidence/run-1，新输出1GiB硬限，
RSS1GiB提示。执行前形式/代码审查、日志真实测试、输入锁与脚本哈希冻结。
不安装、GPU、网络科学调用、重试、增网格或后检选优。退出后只复核保存数据，
不重新传播/分解/求根/优化。保留全部负结果，241/242暂停，Route未评价。
