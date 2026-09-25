# CS11 — 单次有界执行卡 v1

Scope ID: `ASFS-DISCOVERY-20260919-CS11`。  
State: `FROZEN BEFORE COMPUTATION`。

[候选卡](candidate-card.md)规定44对调用、六控制、八固定后检/消融上限；
总102传播/full SVD、54动能eigh与12静态eigh。主控独占启动。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/261-position-mobility-heat-search/run_search.py
```

工作目录arithmetic_symplectic_flow；只写本包evidence/run-1，存在即拒绝。
新输出1GiB硬限、RSS1GiB提示；形式及代码审查通过后执行一次，失败不重试。
没有GPU/安装/新目标/外传/提交/发布。结束后只核对保存数据，不重分解或优化。
