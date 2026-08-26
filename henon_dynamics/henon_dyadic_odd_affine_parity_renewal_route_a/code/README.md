# C174 code / C174 代码

The six scripts have distinct roles:

- `c174_parity_renewal_producer.py` creates the canonical exact JSON evidence.
- `c174_parity_renewal_checker.py` independently reimplements and checks the mathematics; it imports no producer code.
- `c174_sympy_crosscheck.py` supplies a separate symbolic algebra derivation.
- `c174_replay.py` requires byte-identical regeneration in a temporary directory.
- `c174_mutation.py` requires rejection of repaired-hash semantic mutations and a stale-hash mutation.
- `c174_release_manifest.py` closes exactly 27 payload files while excluding its own output.

六个脚本分别承担证据生成、独立数学检查、SymPy 交叉推导、逐字节回放、语义变异拒绝和 27 文件发布闭合。独立检查器不导入生产器。

All arithmetic is exact. There are no floating-point tolerances, random seeds, network calls, target tables, or training data.

全部计算使用精确整数、分数、形式级数和二进赋值；没有浮点容差、随机种子、网络调用、目标表或训练数据。
