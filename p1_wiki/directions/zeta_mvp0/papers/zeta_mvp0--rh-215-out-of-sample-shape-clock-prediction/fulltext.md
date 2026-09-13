---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-215-out-of-sample-shape-clock-prediction"
canonical_tex: "zeta_mvp0/papers/RH-215-out-of-sample-shape-clock-prediction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-215-out-of-sample-shape-clock-prediction/main.pdf"
source_sha256: "05b0c3bf78d6c7af2364b161e8ca5695ea2c040468a1eb929c011394acd91782"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Out-of-Sample Prediction of the Finite Shape Clock Affine, Logistic, and Power-Gap Laws on Two Physical Channels

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-215-out-of-sample-shape-clock-prediction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-215-out-of-sample-shape-clock-prediction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-215-out-of-sample-shape-clock-prediction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-215-out-of-sample-shape-clock-prediction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-215-out-of-sample-shape-clock-prediction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The sixteen-level audit of RH-214 finds a strictly increasing axial quartet coordinate $u$ and a narrow mature asymmetry corridor. This paper asks whether that finite clock supports a simple predictive law. Before scoring the finest two levels, we fit three predeclared models on seven scales from $\sigma=0.008$ through $0.002$: an affine law in $\log(1/\sigma)$, an affine logit law, and a power law for the gap $1-u$.

  All three fit the training segment well. On the left channel their direct $u$-scale training $R^2$ values are $0.99266$, $0.99272$, and $0.98716$. The held-out levels $0.0016$ and $0.00125$ reverse the in-sample ranking. The power-gap model has two-point RMS error $0.00989$ on the left and $0.01003$ on the right; logistic errors are about $0.0206$ and affine errors about $0.0305$. Power-gap wins each held-out point on each channel, but it still overpredicts $u$ by roughly $0.01$.

  A constant predictor for mature $\eta$ misses the holdouts by at most $0.00218$, consistent with a corridor but not a limit. The strict conclusion is a finite model-selection result. No asymptotic power law, value $\lim u=1$, or determinant limit is established.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Out-of-Sample Prediction of the Finite Shape Clock\
  Affine, Logistic, and Power-Gap Laws on Two Physical Channels
```

## Markdown 正文

# Prediction rather than retrospective fit

RH-214 shows that $u$ is ordered across sixteen scales [@WangRH214]. A smooth curve can fit such a finite monotone list almost arbitrarily well, so in-sample residuals alone have little force. We instead freeze $$\label{eq:train}
 \sigma\in\{0.008,0.00625,0.005,0.004,0.0032,0.0025,0.002\}$$ for training and reserve $$\label{eq:holdout}
 \sigma\in\{0.0016,0.00125\}$$ for scoring. Both channels use the same split and model classes.

This is a deterministic numerical experiment, not an independent random sample. "Out of sample" means only that the held-out coordinates are not used in estimating the reported coefficients.

# Three predeclared laws

Let $$t=\log(1/\sigma).$$ For each channel we estimate an ordinary least-squares line after one of three transforms.

## Affine-log model

$$\label{eq:affine}
 u(t)=at+b.$$ This is the least constrained local model. It cannot be globally valid with $a>0$, because it eventually exceeds one.

## Logistic-log model

$$\label{eq:logistic}
 \log\frac{u(t)}{1-u(t)}=at+b,
 \qquad
 u(t)=\frac{1}{1+e^{-at-b}}.$$ For $a>0$, it enforces $0<u<1$ and approaches one.

## Power-gap model

$$\label{eq:power}
 \log(1-u(t))=at+b,
 \qquad
 1-u=e^b\sigma^{-a}.$$ The fitted $a$ is negative, so $-a$ is the candidate gap exponent.

The logistic model also has a power-gap leading asymptotic when its logit is large, but the two forms weight the finite training region differently.

# Training fit

For the left channel:

  model            direct-$u$ $R^2$   max training error   RMS training error
  -------------- ------------------ -------------------- --------------------
  affine-log             $0.992663$           $0.008231$           $0.005895$
  logistic-log           $0.992719$           $0.008117$           $0.005872$
  power-gap              $0.987164$           $0.012233$           $0.007797$

The right channel gives the same qualitative ranking, with $R^2$ between $0.98725$ and $0.99285$. If the analysis stopped here, one would select affine or logistic and might infer an overly rapid advance.

The fitted left formulas are approximately $$\begin{aligned}
 u_{\rm aff}(t)&=0.149086t-0.242734,\\
 \operatorname{logit}u_{\rm log}(t)&=0.619923t-3.091628,\\
 \log(1-u_{\rm gap}(t))&=-0.361228t+1.112179.\end{aligned}$$

# Held-out verdict

The actual left coordinates are $$u(0.0016)=0.692811,qquad u(0.00125)=0.718352.$$ The predictions are:

  model            prediction at $0.0016$   prediction at $0.00125$   two-point RMS
  -------------- ------------------------ ------------------------- ---------------
  affine-log                   $0.717047$                $0.753850$      $0.030393$
  logistic-log                 $0.710802$                $0.741220$      $0.020574$
  power-gap                    $0.702790$                $0.728146$      $0.009886$

On the right, the actual values are $0.692310$ and $0.717501$. The corresponding RMS errors are $0.030639$, $0.020825$, and $0.010031$.

[\[prop:winner\]]{#prop:winner label="prop:winner"} On both physical channels, the power-gap model has the smallest absolute error at each of the two held-out scales and the smallest two-point RMS error among the three predeclared models.

The assertion is the direct numerical comparison of the frozen predictions and held-out coordinates above. The right-channel inequalities are archived with the same ordering.

The power-gap model nevertheless overpredicts both left holdouts by $0.00998$ and $0.00979$, and both right holdouts by about $0.010$. Its win is relative, not an adequate asymptotic residual bound.

# What the holdout teaches

The ordering of training and holdout errors contains more information than the winning label:

1.  the affine and logistic curves extrapolate the recent rise too aggressively;

2.  the power-gap transform tolerates more curvature in the observed finite window;

3.  high $R^2$ on seven correlated deterministic anchors does not select a tail law;

4.  both channels fail in nearly the same direction and magnitude, so the effect is unlikely to be explained solely by channel mismatch.

It would be inappropriate to attach conventional independent-sample $p$-values to these points. The relevant next evidence would be further predeclared scales or an analytic estimate from the underlying operator.

# Transverse holdout

The training means of $\eta$ are $$\bar\eta_L=-0.090859,qquad \bar\eta_R=-0.092405.$$ Using these constants for both held-out levels gives maximum errors $0.002171$ and $0.002039$. This supports RH-214's finite corridor language. It does not distinguish convergence to a constant from bounded slow drift or oscillation.

# Conditional asymptotic readings

If [\[eq:power\]](#eq:power){reference-type="eqref" reference="eq:power"} held for all sufficiently small $\sigma$ with $a<0$, then $$1-u_\sigma\sim C\sigma^{\beta},\qquad \beta=-a>0,$$ and hence $u_\sigma\to1$. The fitted exponents are approximately $0.3612$ on both channels. This implication is mathematically correct but its premise is unproved. We therefore use the power-gap law only as a finite candidate coordinate for subsequent falsification.

RH-216 takes a different route: it proves exactly what $u\to1$ would imply for the quartet roots and discriminant, without asserting that the physical sequence satisfies the premise.

# Claim boundary

This paper establishes no asymptotic regression consistency, no error bars uniform in $\sigma$, and no value of $\lim u$. Two held-out points cannot differentiate a true power law from a slowly varying correction, a crossover, or another smooth monotone curve.

The strict result is the protocol and finite ranking in Proposition [\[prop:winner\]](#prop:winner){reference-type="ref" reference="prop:winner"}. Gate A remains open. No growing determinant, Hilbert--Pólya operator, zeta-zero identification, or RH implication is claimed.
