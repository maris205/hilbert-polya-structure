# Paper 9 — Packet separation

This project studies the inherited quotient topology of Deninger's
finite-kernel prime packet. It proves, by simultaneous real/profinite
approximation, that the genuine prime packet, its inherited periodic orbits,
and its time-orbit quotient are nontrivial indiscrete spaces, while the exact
restricted diagonal equivalence relation is not closed. It also separates
those actual topologies from the intrinsic Connes--Consani scaling circle and
from standard-circle or product proxies.

Current status: research, independent proof review, control reproduction,
manuscript review, citation audit, clean build, and visual audit complete.
The 21-page release is in [`paper/`](paper/README.md); the final PDF is
[`paper/paper.pdf`](paper/paper.pdf).

The deterministic control suite is reproduced with:

    ./experiments/reproduce.sh

The release passed all 20 controls over 240 generated rows. Its frozen
control-manifest SHA-256 is
`52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668`.

Public synchronization must exclude `notes/sources/*.pdf` unless a
redistribution licence is documented for the exact manifestation. Source
manifests, hashes, URLs, exact locators, and preflight sidecars may be
synchronized.
