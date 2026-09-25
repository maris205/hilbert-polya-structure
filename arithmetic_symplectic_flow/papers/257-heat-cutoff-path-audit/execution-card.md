# CS07 execution card v1

Scope ID: `ASFS-DISCOVERY-20260919-CS07`。执行前冻结。
沿用当前用户继续的本地实现/运行授权；ARS逐命令确认默认不覆盖该明确授权。
工作目录为arithmetic_symplectic_flow；精确命令：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/257-heat-cutoff-path-audit/run_audit.py
```

只运行一次，最多1解析控制+10固定诊断传播，不优化、不生成零点或新目标。
总预算包含所有SVD、5个静态特征分解、输出和评价。未知性能不冒称实测保证。
硬限在启动时由timeout安装，约30秒监控本进程与本包run-1输出，记录真实
PID、起止时间、峰值RSS、文件增长及退出码。1GiB内存为提示，不自动杀进程。
异常不重试，不临时缩小N、改变beta/r/次序或提高预算。

输入锁含本卡、候选卡、256脚本/卡、S角色冻结记录与N511完整数组、
N383/639/767旧输出、旧目标及五个开发参考；运行manifest再锁本脚本
和input-locks。只导入256的数学源函数，不执行其main或改变其全局常数。
所有旧对象/数组/源码只读，run-1存在即拒绝覆盖。

run标签UNVERIFIED；保存结果审查ANALYZED，不冒称独立重跑、严格误差认证
或外部同行评审。纸面证明、有限差异和正式门分开记录。
