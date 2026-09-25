# DS04 执行许可与输入冻结

**Scope ID:** `ASFS-DISCOVERY-20260919-DS04`。  
**Freeze state:** `EXECUTION AUTHORIZED; NOT YET RUN`。  
**Date:** 2026-09-19（用户当前日期）。

用户明确答复“按此执行”，批准新增独立采集脚本并按前述完整命令
运行。本卡先于脚本和前向创建；执行后不修改。原协议及完整对象
定义见 [candidate-card-frozen-v1.md](candidate-card-frozen-v1.md)。

仅一次 N260、N280、N300 原 solve 调用；原 N250 数据只读复用。
原非自治路径、hbar、L、quartic、S、c、目标和首点规则均不改。
无 GPU、无调参、无安装、无自动重试、无原文件覆盖。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/247-grid-readout-stability/run_grid.py
```

cwd 为项目根目录，唯一新输出为本包 `evidence/run-1/`。
源码/旧 helper/N250 NPZ/旧比较 JSON 使用原卡指定 hash；运行
manifest 另保存本卡、冻结原卡、新脚本、环境的实际 hash 与身份。
执行前语法检查不运行脚本顶层，不算新增前向。

每个 N 各自拥有矩阵、态、分支、排序和尺度，完整保留原输出。
只比较排序输出，不跨维度自动配准态。A0/A1/A2/T0–T3 未评价，
formal UNASSIGNED，B NOT INVOKED。
