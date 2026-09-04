# HCS-C356 — QWZ Thouless Chern pump

This self-contained package proves the complete gapped-phase atlas for
\[
H_m(k,\tau)=\sin k\,\sigma_x+\sin\tau\,\sigma_y+(m+\cos k+\cos\tau)\sigma_z.
\]
It fixes the orientation and projector convention, derives the exact direct gap and lower-band Chern number, resolves every Dirac wall, and states charge quantization only in the filled-band adiabatic limit.

The source-local Chern integer is a natural quantization, but it carries no rational-prime data. Route A is therefore rejected with tuple `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route B remains locked. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Final paper: `paper/main.pdf`. Reproduction and release commands are in `code/README.md`.
