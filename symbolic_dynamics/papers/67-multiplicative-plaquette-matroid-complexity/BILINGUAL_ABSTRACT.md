# Bilingual abstract

## English

Let `a,b>=2` be coprime and let `F_q` be a finite field.  We study the compact
linear multiplicative constraint space

```text
X={x in F_q^N:x_n-x_an-x_bn+x_abn=0 for every n>=1}.
```

Every integer has unique coordinates `r a^i b^j`, and on each root component
the rule integrates to `x_(r a^i b^j)=u_i+v_j`.  This gives an explicit
topological-group isomorphism between `X` and the unrestricted coordinates
whose indices are not divisible by `ab`.  More generally, we calculate every
finite projection.  A finite coordinate `r a^i b^j` is viewed as an edge from
row vertex `i` to column vertex `j`; the projection dimension is the sum of
`|V|-components` over the resulting root-wise bipartite graphs.  Thus the
coordinate-dependence matroid is a direct sum of graphic matroids, and the
only finite compatibility conditions are alternating cycle sums.  Under Haar
measure, forests are exactly the jointly independent coordinate families and
each cycle-rank unit contributes `log q` of total correlation.  As
specializations, arithmetic prefixes have
`q^(N-floor(N/(ab)))` patterns, whereas an `M x N` exponent rectangle has
`q^(M+N-1)` patterns.  We keep these two geometries and their normalizations
explicitly separate.

## 中文

设 `a,b>=2` 互素，`F_q` 为有限域。本文研究紧致线性乘法约束空间

```text
X={x in F_q^N:x_n-x_an-x_bn+x_abn=0, n>=1}。
```

每个正整数均可唯一写成 `r a^i b^j`，其中 `a`、`b` 均不整除 `r`；在每个根分量上，
约束可完全积分为 `x_(r a^i b^j)=u_i+v_j`。由此得到一个显式拓扑群同构：`X` 的自由
坐标恰为指标不被 `ab` 整除的坐标。更一般地，本文精确计算任意有限坐标集的投影。
把坐标 `r a^i b^j` 看成连接行顶点 `i` 与列顶点 `j` 的边，则投影维数等于各根分量二部图
的 `|V|-连通分支数` 之和。因此，坐标依赖拟阵是这些图拟阵的直和，而全部有限相容条件
恰由圈上的交错和给出。在 Haar 测度下，森林恰对应联合独立的坐标族；每增加一个圈秩，
总相关增加 `log q`。作为推论，算术前缀 `[1,N]` 的图样数为
`q^(N-floor(N/(ab)))`，而单个根分量中的 `M x N` 指数矩形图样数为
`q^(M+N-1)`。本文明确区分这两种几何及其归一化，不把前缀复杂度与乘法 Følner 熵混同。

