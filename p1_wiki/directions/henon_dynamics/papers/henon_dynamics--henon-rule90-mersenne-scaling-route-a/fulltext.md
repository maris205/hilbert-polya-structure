---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-rule90-mersenne-scaling-route-a"
canonical_tex: "henon_dynamics/henon_rule90_mersenne_scaling_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_rule90_mersenne_scaling_route_a/paper/main.pdf"
source_sha256: "095d93d771a30473344ec52e6bc0e0ab1391d47396f2541d731552523abfc485"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Mersenne Scaling in Cyclic Rule 90

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_rule90_mersenne_scaling_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_rule90_mersenne_scaling_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_rule90_mersenne_scaling_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_rule90_mersenne_scaling_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For Rule 90 on every binary ring of Mersenne circumference $L=2^r-1$, the local multiplier $a=x+x^{-1}$ satisfies $a^{L+1}=a$. Its image contains exactly half the state space, every state reaches it in one step, and all image points are periodic with periods dividing $L$. Polynomial gcd and Möbius inversion resolve primitive cycles. In contrast, power-of-two rings are nilpotent. This is an exact scaling theorem, not a target determinant.
author:
- 'Route-A structural certificate C150'
title: Mersenne Scaling in Cyclic Rule 90
```

## Markdown 正文

# Mersenne identity and image

Work in $R_L=\mathbb F_2[x,x^{-1}]/(x^L-1)$, where one Rule-90 update is multiplication by $a=x+x^{-1}$. If $L=2^r-1$, Frobenius gives $$a^{2^r}=x^{2^r}+x^{-2^r}=x+x^{-1}=a,\qquad a^{L+1}=a.\tag{1}$$ For monic $f$ and a multiplier $h$, writing $f=gf_1$, $h=gh_1$ with $g=\gcd(f,h)$ shows $f\mid hq$ exactly when $f_1\mid q$. Thus multiplication by $h$ on $k[x]/(f)$ has kernel dimension $\deg g$. Multiplication by $x$ is invertible and $xa=(x+1)^2$. Since odd $L$ makes $x^L+1$ squarefree and $x+1$ is a factor, $\gcd(x^L+1,(x+1)^2)=x+1$. Hence $\dim\ker a=1$ and $\dim\operatorname{im}a=L-1$.

For $y=au$ in the image, (1) yields $a^Ly=y$. Thus the restriction to the image is a permutation with order dividing $L$. Every state enters the image after one update. Conversely, if $a^nu=u$, then $u=a(a^{n-1}u)$ lies in the image. The periodic set is therefore exactly the image, with $2^{L-1}$ points: exactly half of all states.

# Exact periods

The standard multiplication-kernel calculation gives $$\operatorname{Fix}_L(n)=2^{\deg\gcd(x^L+1,(x^2+1)^n+x^n)}.\tag{2}$$ Consequently $$P_L(n)=\sum_{d\mid n}\mu(n/d)\operatorname{Fix}_L(d),\qquad
C_L(n)=P_L(n)/n.$$ All realized periods divide $L$. The converse is not asserted: a divisor of $L$ need not be realized. The division by $n$ occurs only after Möbius inversion, so fixed configurations, exact-period configurations, and primitive cycles remain distinct.

# Power-of-two control and boundary

For $L=2^s$, $a^{2^{s-1}}=x^{2^{s-1}}+x^{-2^{s-1}}=0$ because the two monomials coincide. Thus the map is nilpotent and only zero is periodic. Indeed, if $a^nu=u$, repeated use of this equality expresses $u$ as $a^{qn}u$ for every $q$; choosing $q$ beyond the nilpotency index forces $u=0$.

The structural statements above hold for every $r,s\geq1$; the exact ledgers through $r,s\leq8$ are implementation sentinels. They contain 27 divisor-period cells and pass 153 independent matrix assertions, 276 SymPy checks, byte replay, and 45 hostile cases. The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_FAIL})$. We claim no infinite-volume determinant or thermodynamic limit, target divisor, target functional equation or counting law, arithmetic/local factor, root number, automorphy, natural operator lift, Hilbert--Pólya operator, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
