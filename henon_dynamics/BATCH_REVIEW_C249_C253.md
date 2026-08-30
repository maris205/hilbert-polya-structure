# Route-A batch review: C249--C253

Status: **RELEASE_COMPLETE**

Evaluation date: 2026-08-30

Source/code baseline: `3ff451e904f8f063e88c40ef87f4697a6586b1a5`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md`, v0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

This round changes the dynamical owner in every slot and takes one independent
theorem-scale step per manuscript.  The finite receipts are regression
controls; all-parameter statements are the displayed source-local theorems.

## Theorem advances

| ID | dynamical owner | closed advance | finite receipt |
|---|---|---|---:|
| C249 | smooth Van der Pol/Liénard oscillator | Complete sign and parameter-boundary atlas; unique attracting cycle for μ>0 and repelling time-reversal for μ<0; center face at μ=0; energy/divergence identities and transverse Floquet receipt. | 8 parameter + 5 cycle rows |
| C250 | Ermakov--Pinney/isotonic Hamiltonian | Explicit linear-pair superposition (x^2=au^2+2buz+cz^2) with (ac-b^2=\kappa); exact turning radii, primitive period, isotonic action, invariant and singular faces. | 9 rows + 4 boundaries |
| C251 | radius-one synchronous majority CA rule 232 | Exact wall law (w'_i=w_i(1\oplus w_{i-1}\oplus w_{i+1})); finite erosion to the fixed language, unique even alternating 2-cycle, and transfer-matrix fixed/depth counts. | 14 finite-state + 216 wall-run rows; traces through n=64 |
| C252 | two-threshold hysteretic relay phase oscillator | Exact switching/Poincaré map: leg duration (2h), full period (4h), multiplier (e^{-4\gamma h}), unique attracting level for γ>0, neutral γ=0 continuum, and no-Zeno/grazing boundary policy. | 8 rows + 4 boundaries |
| C253 | finite Moran birth--death process | Exact fixation probability for all selection ratios, rational Green matrix and absorption-time solution, reversible killed-chain weights, and neutral/zero-rate/singleton faces. | 8 rows + 4 boundaries |

The five owners are independent; no result is presented as five installments of
one calculation.

## Independent audit and release hashes

Each package contains 27 manifest-listed payload files plus one self-excluded
release manifest (28 physical files), with no Python bytecode or LaTeX
sidecars.  Producer, independent checker, symbolic reconstruction, replay,
hostile mutation suite, and release manifest were rerun with `python3 -B`.
All papers have two substantive revisions, fixed epoch
`SOURCE_DATE_EPOCH=1788048000`, embedded/subset fonts, and successful text
extraction.  The final settled LuaLaTeX passes have no unresolved references,
overfull boxes, or float-placement warnings; fixed trailer IDs make the PDFs
byte-reproducible across independent build directories.

| ID | checker assertions | SymPy identities | hostile rejects | final pages / fonts | evidence payload SHA-256 | evidence file SHA-256 | final PDF SHA-256 | manifest SHA-256 |
|---|---:|---:|---:|---:|---|---|---|---|
| C249 | 264 | 81 | 40/40 | 2 / 22 | `791aaadd6235f0f79761d85ea99e3b3914b25ede8378b56d9ed3a6e1adc16062` | `814c2375c8052c37536134248cc6a15ae111ae939e72f351a68c67589e592b7c` | `c83472c2c75850e23c9035661afe7bd58bad60b2936dbc44f783dc9f69131dab` | `90733a33a541a7537b964055db423a7dc8dde1ad7c186dbb84f0acb6ac2e86c4` |
| C250 | 215 | 10 | 26/26 | 2 / 24 | `441c7a92ec607a958c0341689565da17d74470558ed3a78fb21d0042d2e183b1` | `2d9fead6f92d64d8cb4125e28b94a05bf4876196704905c9be821ba6e465d544` | `8e79456a5dd340cd6755d2db9c3809656f25e9d181d9c74b87a80bbd2dff99fc` | `dd2bad4eb385d443e940d681767b46b828638d45ade80c442b4abad3efb39521` |
| C251 | 1,855 | 569 | 40/40 | 2 / 24 | `d683f8fa3c81ea83e2ed9c702f0f694248c1145aa4796c3c39305b66ea4f1b49` | `5a1f57f663216fc8fd5b2581141bbde80f620ef284abcb74fa340b47927ff317` | `a44589bc7f25d8576c337f916db772cedef8bf0e8c4e89b10356a2a540bea555` | `a139ab49cb4d657d865a6d43980b03c4d34bf7228889a3cb4d0f578a8390f3c2` |
| C252 | 189 | 10 | 21/21 | 2 / 19 | `79ec4b08df525a36b52af36da807ce2213ebb5ff9e9622bef3827ab71211ccc4` | `6981642b0cd4df6cfb831a67eeebe646b802efe9657993d4196bee5509cf244b` | `624451ea83a7623cfae7c880a13703a54aecbafe9a9be8a96a8caf6137794ff4` | `9fffe1943bc2042cc016dfb7fdef443612fb668b4d4b26d588f44151edcb332c` |
| C253 | 220 | 10 | 23/23 | 2 / 17 | `4b036b426bbb0ccf8106a5a65cb8240ba8a97aae9dc0a9a4b7d223a61677def4` | `663f90dccc2917248b3fc8acbf91a85ab0684ee654a12311a9a1f6e0bced28ca` | `5fd7a31f51d35ad0f356df8ba87fd09671cf0b7d5889dbf5ed181e9df671fffe` | `b49e3306bb3e842ed37906251642c2d1f2c2bae61d2f6b8eaf405a258a239f81` |

The aggregate is **2,743** independent-checker assertions, **680** symbolic
identities, **150** hostile rejections, **135** payload files (140 physical
files), **10** final-paper pages, and **106** embedded/subset font entries.

## Route-A decision and scope boundary

| ID | strict tuple | overall | Route B |
|---|---|---|---|
| C249 | (A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT) | ROUTE_A_REJECTED | false |
| C250 | (A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION) | ROUTE_A_REJECTED | false |
| C251 | (A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT) | ROUTE_A_REJECTED | false |
| C252 | (A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT) | ROUTE_A_REJECTED | false |
| C253 | (A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT) | ROUTE_A_REJECTED | false |

The Liénard cycle, isotonic action, wall erosion, relay multiplier, and Moran
Green data are source-local dynamical/probabilistic structures.  No package
introduces a target prime/zero table, arithmetic local datum, Euler factor,
root number, automorphy statement, target divisor/counting law, target
functional equation, Hilbert--Pólya operator, or Route-B input.

The five package READMEs and PDFs are indexed in
[`henon_dynamics/README.md`](README.md); candidate and obstruction registries
record the same source-local stopping boundaries.
