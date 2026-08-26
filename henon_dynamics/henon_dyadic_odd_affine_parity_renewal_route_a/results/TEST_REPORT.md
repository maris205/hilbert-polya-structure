# Test report / 测试报告

All commands were executed from the C174 package directory on 2026-08-26. Every mathematical command exited zero.

所有命令均从 C174 包目录实际执行；全部数学检查退出码为零。

## Six-command release chain / 六命令发布链

1. `python3 code/c174_parity_renewal_producer.py`
   - `C174_PRODUCER_PASS`
   - 36 parameter pairs; 18,360 fixed words; 9,216 inverse prefixes; 432 return rows.
   - payload SHA-256 `4c4515bc863b83c7f5d20607658e25f14d9c60d4c6f533678f36f84ed3bfa9e2`.
2. `python3 code/c174_parity_renewal_checker.py`
   - `C174_CHECKER_PASS`
   - 272,693 independent assertions.
   - The checker imports no producer module.
3. `python3 code/c174_sympy_crosscheck.py`
   - `C174_SYMPY_PASS`
   - 911 symbolic checks.
4. `python3 code/c174_replay.py`
   - `C174_REPLAY_PASS`
   - 190,195 bytes reproduced byte-for-byte.
   - evidence file SHA-256 `9cdedc898e8624b00c73ccde4bd316fb4bb2cb948720d7201bed16e0bcd81004`.
5. `python3 code/c174_mutation.py`
   - `C174_MUTATION_PASS`
   - 25/25 repaired-hash semantic mutations rejected; 1/1 stale-hash mutation rejected.
6. `python3 code/c174_release_manifest.py`
   - `C174_MANIFEST_PASS` with exactly 27 payload files.
   - The manifest was run after all content and PDF bytes were frozen; its own SHA is reported in the handoff, not recursively embedded here.

## Independence / 独立性

The producer and checker independently define parity, branch iteration, fixed-word algebra, Möbius inversion, valuation checks, first returns, and all digests. The SymPy script is a third derivation path. Replay tests producer determinism; mutation tests checker sensitivity.

生产器与检查器分别实现奇偶性、分支迭代、固定词代数、Möbius 反演、赋值、首返和摘要；SymPy 是第三条推导路径。回放检验生产确定性，变异检验检查器敏感性。

## Build checks / 构建检查

- LuaLaTeX final builds A/B: identical SHA-256 `5d236849a52afa5d54d7f9d6423020754bf9d0565bd4b8fb7215a4eb0f886e24`.
- Pages: 3.
- Final log: zero warnings, undefined references, undefined citations, missing characters, overfull boxes, and underfull boxes.
- Fonts: every listed font embedded.
- Visual snapshots: 3/3 pages rendered and inspected; no clipping, collision, blank content, or broken glyph observed.

最终双次编译逐字节一致，3 页全部完成字体、日志和逐页视觉检查。

## Firewall grep / 防火墙检查

Claim-bearing documents consistently state that classical parity conjugacy is prior work, Route A is rejected, the \((3,1)\) result does not advance positive-integer Collatz, and no Euler/local/root-number/automorphy/Hilbert–Pólya claim is made.

所有承载主张的文档均明确：经典 parity 共轭属于先验；Route A 被拒绝；\((3,1)\) 不推进正整数 Collatz；不主张 Euler/局部/根数/自守/Hilbert–Pólya 结论。
