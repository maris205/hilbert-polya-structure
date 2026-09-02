# Paper plan — parallel odd-vertex pruning

Target form: anonymous AMS short note, 4–5 pages, no decorative figure.

## Abstract

Define the labelled-subset carrier and simultaneous odd-degree deletion.
State the sharp clock, strict predecessor formula, all-time fibre transfer,
and image criterion.  Give the exhaustive-control count but say explicitly
that computation is falsification only.  End with `HOLD_EXTERNAL`-compatible
scope language and no novelty adjective.

## 1. System, notation, and complete theorem

- Define `X_n`, `F`, rank, even graph, entry time.
- Define `B_n(s,m)` and `e_s` before the theorem.
- State one theorem with five parts: recurrence/clock, strict inverse,
  iterated fibres, image layers, censuses.
- Put sequential parity games and Eulerian-deletion work in the first
  ownership paragraph; distinguish their rule from the simultaneous map.

## 2. Forward dynamics

- Handshaking gives even vertex loss.
- Strict loss rules out nontrivial cycles.
- Path endpoint deletion proves sharpness, including `n=0,1`.
- Keep this section short so the paper does not read as a pruning note.

## 3. The parity-extension theorem

- Fix target set `S` and deleted set `D`.
- Write the binary incidence equations explicitly.
- Prove consistency iff `|D|` is even.
- Prove rank `s+d-1` from connectivity and derive
  `2^[s(d-1)+binom(d-1,2)]`.
- Include the `s=0,d=2` boundary as a one-line check.

## 4. Transfer powers and the complete atlas

- Prove strict predecessors are non-even.
- Inductively identify `B_n^t` with strict inverse chains.
- Separate non-even target `B_n^t` from even target geometric sum.
- Derive exact image criterion and stable image.
- Sum using `e_s` to obtain fixed, image, CDF, and shell formulas.

## 5. Exact controls and scope

- Describe exhaustive state construction and independent formula lane.
- Report 1,350,807 assertions and canonical hash.
- Restate what computation cannot prove.
- Give the P114/P123/P141/P146/P148 firewall compactly.

## References

Minimum set: Nowakowski–Ottaway; Krüger; Cygan–Marx–Pilipczuk–Pilipczuk–
Schlotter; one standard graph-theory source for binary incidence/cycle space;
Artin–Mazur only if zeta is kept.  Every citation must have a specific role.
