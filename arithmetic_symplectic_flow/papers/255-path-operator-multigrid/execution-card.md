# CS05 execution card v1 — frozen before execution

Scope ID: `ASFS-DISCOVERY-20260919-CS05`。
本轮沿用当前用户的构造/本地自动运行授权，不改旧源码或结果，不请求外部执行。
ARS的逐命令确认默认不覆盖这个明确授权；仍先展示冻结命令与停止条件。

Working directory: arithmetic_symplectic_flow root.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/255-path-operator-multigrid/run_search.py
```

只运行一次，只监控本次进程与本包evidence/run-1；已有输出则拒绝覆盖。
125个成对调用上限、250训练前向上限，加1回归和2验证前向；缓存仍计调用。
600秒硬限由timeout在启动前装好。异常不重试，不自动换精度/算法/维度。
至少约30秒记录过程存活、内存及输出增长；预期资源以内不作无依据报警。
512MiB内存为提示线，不是自动杀进程许可；超时是唯一自动终止条件。

两冻结卡、251 helper、原Hénon solver、253-Q0103 NPZ/JSON、固定alpha
来源252 winner-A、三个旧参考101–150/151–200/201–240均进入input-locks。
manifest另锁脚本与input-locks文件。旧helper只导入函数，不执行其main。

N320/N352都是训练选择网格。五角色身份和每角色两网格完整数组，以及
其未另训练的静态H_ref对照预测都在新241–300参考生成之前保存。
之后不得训练、替换主赢家或以未声明角色扩大未来选型。
N384/N416仅主赢家参数冻结后诊断，不使用其成绩回改主目标。

收集实际PID/start/end/退出码、所有事件/数组/角色及静态点表、缓存和
实际前向次数、两个固定主赢家维度、文件尺寸清单。Material Passport
run标签UNVERIFIED，保存结果一致性审查ANALYZED不能冒称独立rerun认证。
