# C108 字面返回映射的二周期证据缺陷

日期：2026-09-05。状态：**精确反例已确认；历史包未修改。**
本短记从本轮已冻结的 [CONTRACT_SCOUT.md §5](CONTRACT_SCOUT.md)
和已保存的 [EXACT_CHECK_OUTPUT.json](EXACT_CHECK_OUTPUT.json) 摘出；
本次拆分没有重跑计算，没有运行旧 producer 或更新旧 payload。

## 缺陷与正确对象

旧 [THEOREM_PACKAGE.md](../../henon_holomorphic_complex_transfer/THEOREM_PACKAGE.md)
声明字面映射

$$F(z,w)=(w,w^2-z/4).$$

因此 $F^2(z,w)=(z,w)$ 的正确方程是

$$w^2=\tfrac54z,\qquad z^2=\tfrac54w,$$

而非旧 [producer](../../henon_holomorphic_complex_transfer/code/c108_holomorphic_producer.py)
实际使用的 $y=x^2-x/4$、$x=y^2-y/4$。后者把不同时间位置的变量放错。
正确的首一消去多项式为 $z^4-125z/64$。令
$\omega=(-1+i\sqrt3)/2$，正确四点为

$$
(0,0),\quad(\tfrac54,\tfrac54),\quad
(\tfrac54\omega,\tfrac54\omega^2),\quad
(\tfrac54\omega^2,\tfrac54\omega).
$$

四个 $1/\det(I-DF^2)$ 依次为
$16/25,-16/75,-16/75,-16/75$，故 **正确的 $\tau_2=0$**，
不是旧记录的 $-1664/1725$。
旧列出的非实点
$P_*=((-3-i\sqrt{39})/8,(-3+i\sqrt{39})/8)$ 更直接满足

$$F^2(P_*)-P_*=(i\sqrt{39}/16,\,117/256-7i\sqrt{39}/64)\ne0.$$

旧 [crosscheck](../../henon_holomorphic_complex_transfer/code/c108_sympy_crosscheck.py)
沿用同一错误 resultant 并比较已有 payload，未从字面 $F^2-I$ 独立重建，
因此不能消除此反例。

## 依赖隔离边界与证据锚点

应隔离旧 $\tau_2=-1664/1725$ 及直接依赖它的 determinant 前缀，
不能将这些条目继续用作字面映射的通过证据。此记录**不自动判定整个旧包
所有其他命题无效**；更广泛修复或历史状态变更需另行确定范围。
这个程序纠错也不是本轮保留新数学合同的增量。

已有 JSON 的 `historical_literal_map_counterexample` 字段记录正确方程、
四个权重、返回残差和迹零；其 `historical_files_read_by_this_script` 为空。
新检验 [exact_check.py](exact_check.py) 当轮从字面映射重建，已保存运行的
环境为 Python 3.12.3、SymPy 1.14.0，退出状态为 0；不冒称本次又运行一次。

冻结来源 SHA-256：

- `CONTRACT_SCOUT.md`：`b8780f67d4a9a23e66d2d0fe3f5a2c3c77a50c53a5930697baa00b23e8c28dfb`
- `exact_check.py`：`f84450460221084ec5a19bead703872105d8d6b6532a4274d8b9c5e25519fe9f`
- `EXACT_CHECK_OUTPUT.json`：`ba0911e8be0ef4de0a50fee2b6079db8844809fa03ad5743ad1a40eb871f94af`

未改旧包、共享索引、Git 或目标状态；保持 `NO_BAD_EULER_OR_ROOT_NUMBER`。
