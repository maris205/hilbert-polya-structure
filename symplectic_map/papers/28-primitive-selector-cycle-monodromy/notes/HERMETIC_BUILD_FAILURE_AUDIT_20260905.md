# Paper28 one-shot build failure: independent evidence audit

Date: 2026-09-05. Reviewer: `/root/p28_profile_review`.

Decision: `FAILURE_RECORDING_INTEGRITY_PASS`; the build remains `BUILD_FAILED_PRESERVED_NO_RETRY`. This audit does not convert the failed build into a PDF pass, grant a retry, or change the prospective scope of the earlier executable-profile review.

## Exact failure and seal

The only inspected execution namespace was the explicitly authorized new `build-capsule-20260905/evidence` directory and its sealed `r0-01-latex` evidence child. No other build root, resource subtree or old failure root was scanned.

`evidence/failure.json` has 5,142 bytes and SHA256:

`eb3814163d9ebac4e58b60dc75f637b685b0f17fa0872c8509e924b2f5962afd`

Its decision is `BUILD_FAILED_PRESERVED_NO_RETRY`, stage `r0/01-latex`, error `child failed at r0/01-latex`, with no completed roots. The actual process status records pid903265, spawned=true, returncode1, reaped=true, timeout=false and elapsed0.17036886513233185seconds. These are recorded observations, not estimated success or a timeout classification.

The reviewer independently verified all **16 preceding sealed regular evidence files**, their exact bytes/SHA256/mode/uid/gid, and both sealed evidence directory member sets. The only expected extra top-level member after sealing is `failure.json` itself. Thus there are **17 regular evidence files including the failure record**; the failure record is not incorrectly treated as self-hashed by its own preceding-evidence seal. Both evidence directories are0700. The stdout/stderr files are0644 as recorded, inside the private0700 directory; the other sealed regular evidence files are0600. No unexplained member, hash or metadata mismatch was found.

The copied four controls match the exact final prospective review, and opening-contract source/control bindings match the copied independent review. Its SHA256 is the required `fe49cec6d57a1d678c59eb593397e01be71650777a2c90211f64510c4f3d8d2a`. The command intent uses the reviewed captured loader, fixed system library path, pdftex/pdflatex program and format, original determinism header, environment, cwd/work and uid/gid65534 with no supplementary groups.

## Input preservation

The sealed `r0-inputs-before.json` and `r0-failure-inputs.json` are byte-identical: each has1,801,218bytes, SHA256 `44a030aa74e5f84e01d0d283fc72bbbcd38255bbe8dac034f5be6b856b907984`. The failure record correspondingly reports `r0_readonly_unchanged=true`.

This is an independent check of the sealed before/failure snapshot evidence, not a claim that the reviewer separately rescanned every materialized dependency. The actual source trio was independently reread and still matches its frozen bindings:

| Source | Bytes | LF | SHA256 |
|---|---:|---:|---|
| main.tex | 73733 | 1605 | `bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e` |
| math_commands.tex | 444 | 14 | `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5` |
| references.bib | 6104 | 204 | `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e` |

## Narrow observed cause

The preserved log and stdout agree: at `fontenc.sty:112`, selecting `T1/cmr/m/n/10.95` requests the metric `ecrm1095` at10.95pt, and TeX reports that the TFM file is not found. It then stops with a fatal error and explicitly reports that no output PDF was produced.

The reviewer verified the exact CAPTURE2 manifest SHA256 `6107892d5f9750e91ae48292a68117d490876b8a3164758dfdc3442e04eebb8d` and checked all recorded entry names and aliases for the exact basename `ecrm1095.tfm`. There are **zero matching entries and zero matching aliases**. This is a missing captured metric, not merely evidence that the current lookup failed to reach a metric already present under another recorded alias.

The frozen source loads T1 fontenc before lmodern. Consequently the initial Computer Modern T1 font selection is reached before lmodern can replace the default family; the captured Latin Modern resources do not by themselves supply this bootstrap request. This explanation follows the frozen source order and the actual failing log. The audit does not inspect any live host font directory, assert that a particular host path exists, fetch the missing file, change package order, or claim that adding this one metric will establish complete downstream dependency closure.

The first-command work snapshot contains only `main.log`, `main.fls` and the five still-empty cache/tmp directories. There is no PDF, aux, bbl, completed root or later-stage evidence. The fatal log and work snapshot agree on the lack of a PDF.

## What runtime evidence now establishes—and what it does not

The reviewed control flow requires chroot, identity/capability drop, no-new-privileges, parent ownership checks and limits to complete before a publication exec can occur. The observed process reached real pdfTeX execution and produced a recorder/log rather than a preexec setup error. Within the trusted-controller/kernel assumptions already stated in the prospective profile, this establishes that the initial isolated child startup, captured loader/system selection and captured pdflatex format worked far enough to read the manuscript, article class, size11 and fontenc. It is not an independent syscall trace or a general sandbox proof.

The recorder explicitly lists `/var/lib/texmf/web2c/pdftex/pdflatex.fmt`, `/source/main.tex`, the two captured texmf.cnf files and the early class/font inputs. Every one of its nine distinct input paths is either a manifest member/alias or the frozen source. The log reports pdfTeX1.40.22 and the loaded pdflatex format. This is genuine bounded runtime progress beyond the earlier static-only loader review.

There is **no** demonstrated full LaTeX pass, BibTeX run, auxiliary convergence, second root, cross-root identity, PDF parsing, page-count/font/link/anonymity acceptance, page rendering, visual review or local Paper28 acceptance. None of those downstream stages is inferred from successful initial setup.

## Preservation and next boundary

Keep this failed root and every old failure unchanged. Any dependency repair must be a separately authorized narrow capture/successor with fresh evidence and build roots, not an in-place addition, host fallback or rerun of this root. The exact next dependency need established here is the absent `ecrm1095.tfm` bootstrap metric; later needs remain untested.

The reviewer performed read-only evidence/source/manifest checks and authored only this new audit note. No compiler, parser, materialization, chroot, device creation, dependency capture, host resource read, network operation, source edit or root reuse occurred during this audit. The `paper-compile` skill was read fully and used for diagnosis and preserved-log discipline; its generic installation/retry advice was not applied because the immutable captured-only no-retry contract controls this failure.
