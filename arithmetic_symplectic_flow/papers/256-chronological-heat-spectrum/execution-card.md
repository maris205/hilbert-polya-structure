# CS06 execution card v1 — frozen before execution

Scope ID: `ASFS-DISCOVERY-20260919-CS06`。
用户继续的本地实现/运行授权沿用；ARS默认逐命令确认不覆盖该明确授权。
工作目录为arithmetic_symplectic_flow；只运行以下一次：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/256-chronological-heat-spectrum/run_search.py
```

最多60成对训练调用/120训练传播，加1解析控制和4固定主赢家诊断传播。
完整预算含静态对照、参考生成、保存；异常不重试，不改算法/维度/精度。
超时由启动时安装的timeout终止；内存512MiB仅提示，非自动终止许可。
每约30秒监控进程存活、RSS、输出增长，仅监控本包evidence/run-1。
存在输出即拒绝覆盖。资源预计≤512MiB/1GiB，不把预算当实际完成量。

输入锁含两张冻结卡、原Hénon solver、253-Q0103 NPZ/JSON、253 winner-S
基准、101–150/151–200/201–240/241–300旧参考。无旧solver导入执行。
运行manifest锁脚本和input-locks。纯语法/静态检查不执行前向、SVD或求零点。
四角色的全部预测与静态消融预测先保存，再生成301–320参考；新参考后不训练。
双训练网格都是选择数据。四个后验传播只解释不稳定性，不重选赢家。

收集PID、起止时间、真实退出码、事件/调用/缓存、数组及文件尺寸清单。
run Material Passport为UNVERIFIED；保存结果核对为ANALYZED，
没有独立重跑不得标VERIFIED。模型复核不是同行评审。
