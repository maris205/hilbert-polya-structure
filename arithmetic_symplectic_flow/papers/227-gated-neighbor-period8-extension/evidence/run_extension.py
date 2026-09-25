#!/usr/bin/env python3
"""Exact finite T=8 prefix extension for ANG-20260918-GNS02.

The CPU path uses NumPy uint8 arrays; the CUDA path uses PyTorch uint8
integer/Boolean kernels.  Both paths use the same row-major submask order and
the same global per-stage cap.  A cap hit stores only the first CAP rows and
reports the first un-stored extension as CAP+1, exactly as specified by this
version's frozen stop-before-storage contract.  No finite output is
interpreted as an infinite periodic state.
"""

from __future__ import annotations

import argparse
import platform
import sys
from dataclasses import dataclass
from math import isqrt

import numpy as np


T = 8
MASK = (1 << T) - 1
WIDTH = 15  # coordinates 2,...,16
CHUNK = 8192
CAP = 2_000_000


def temporal_table_np() -> np.ndarray:
    out = np.empty(MASK + 1, dtype=np.uint8)
    for w in range(MASK + 1):
        out[w] = (((w << 1) & MASK) | (w >> (T - 1))) ^ (
            (w >> 1) | ((w & 1) << (T - 1))
        )
    return out


TEMP_NP = temporal_table_np()
POPC_NP = np.array([int(i).bit_count() for i in range(256)], dtype=np.uint8)
# Match 139's exact forced/free enumeration: for each free mask, enumerate
# `subset=free, (subset-1)&free, ..., 0`.  Filtering this global descending
# list gives that order for every free mask, including the cap-stop prefix.
SUB_NP = np.arange(255, -1, -1, dtype=np.uint8)


def divisors_for(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(2, isqrt(n) + 1) if n % d == 0)


DIVS = {n: divisors_for(n) for n in range(2, WIDTH + 3)}


@dataclass
class Stage:
    n: int
    input_prefixes: int
    admissible: int
    extensions_seen: int
    stored_extensions: int
    max_free_bits: int
    capped: bool
    free_boundary_existential: bool

    def line(self) -> str:
        return (
            f"equation_n {self.n} input_prefixes {self.input_prefixes} "
            f"admissible {self.admissible} extensions_seen {self.extensions_seen} "
            f"stored_extensions {self.stored_extensions} "
            f"max_free_bits {self.max_free_bits} capped {self.capped} "
            f"free_boundary_existential {self.free_boundary_existential}"
        )


def roots_np() -> np.ndarray:
    return np.array([w for w in range(256) if TEMP_NP[w] == MASK], dtype=np.uint8)


def initial_np() -> np.ndarray:
    roots = roots_np()
    # Keep a fixed WIDTH-column record; columns after 3 are zero until filled.
    st = np.zeros((len(roots) * 256, WIDTH), dtype=np.uint8)
    st[:, 0] = np.repeat(roots, 256)
    st[:, 1] = np.tile(np.arange(256, dtype=np.uint8), len(roots))
    return st


def one_stage_np(states: np.ndarray, n: int) -> tuple[np.ndarray, Stage]:
    """Run one equation, preserving row-major exact extension order."""
    N = len(states)
    if n == 16:
        # Equation 16 is existential in coordinate 17; do not materialize it.
        valid_count = 0
        maxfree = -1
        for i0 in range(0, N, CHUNK):
            st = states[i0 : i0 + CHUNK]
            w = st[:, n - 2]
            A = st[:, n - 3] ^ w
            g = np.full(len(st), MASK, dtype=np.uint8)
            for d in DIVS[n]:
                g &= np.uint8(MASK) ^ st[:, d - 2]
            E = TEMP_NP[w] ^ g
            ok = (E & (np.uint8(MASK) ^ A)) == 0
            valid_count += int(ok.sum())
            if ok.any():
                maxfree = max(maxfree, int(POPC_NP[np.uint8(MASK) ^ A[ok]].max()))
        return states, Stage(n, N, valid_count, 0, 0, maxfree, False, True)

    out = np.empty((CAP, WIDTH), dtype=np.uint8)
    written = 0
    admissible = 0
    maxfree = -1
    extensions_seen = 0
    capped = False

    for i0 in range(0, N, CHUNK):
        st = states[i0 : i0 + CHUNK]
        w = st[:, n - 2]
        A = st[:, n - 3] ^ w
        g = np.full(len(st), MASK, dtype=np.uint8)
        for d in DIVS[n]:
            g &= np.uint8(MASK) ^ st[:, d - 2]
        E = TEMP_NP[w] ^ g
        ok = (E & (np.uint8(MASK) ^ A)) == 0
        if not ok.any():
            continue
        idx = np.flatnonzero(ok)
        base = ((w[idx] ^ E[idx]) & A[idx]).astype(np.uint8, copy=False)
        free = np.uint8(MASK) ^ A[idx]
        row_counts = (1 << POPC_NP[free].astype(np.int64)).astype(np.int64)
        total = int(row_counts.sum())
        room = CAP - written

        if total <= room:
            # Candidate tensor is at most CHUNK*256*WIDTH bytes.
            cand = np.broadcast_to(st[idx, None, :], (len(idx), 256, WIDTH)).copy()
            # Append u_{n+1}; coordinate u_k occupies column k-2.
            cand[:, :, n - 1] = base[:, None] | SUB_NP[None, :]
            allowed = (SUB_NP[None, :] & (free[:, None] ^ np.uint8(MASK))) == 0
            selected = cand.reshape(-1, WIDTH)[allowed.reshape(-1)]
            out[written : written + len(selected)] = selected
            written += len(selected)
            admissible += len(idx)
            maxfree = max(maxfree, int(POPC_NP[free].max()))
            extensions_seen += len(selected)
            continue

        # Locate the first row that creates extension CAP+1, then retain only
        # the first CAP row-major candidates.
        cumulative = np.cumsum(row_counts)
        stop = int(np.searchsorted(cumulative, room + 1, side="left"))
        use = stop + 1
        free_use = free[:use]
        cand = np.broadcast_to(st[idx[:use], None, :], (use, 256, WIDTH)).copy()
        cand[:, :, n - 1] = base[:use, None] | SUB_NP[None, :]
        allowed = (SUB_NP[None, :] & (free_use[:, None] ^ np.uint8(MASK))) == 0
        selected = cand.reshape(-1, WIDTH)[allowed.reshape(-1)]
        need = CAP - written
        out[written:CAP] = selected[:need]
        written = CAP
        admissible += use
        maxfree = max(maxfree, int(POPC_NP[free_use].max()))
        extensions_seen = CAP + 1
        capped = True
        break

    stage = Stage(n, N, admissible, extensions_seen, written, maxfree, capped, False)
    return out[:written].copy(), stage


def run_cpu() -> list[Stage]:
    states = initial_np()
    print("backend CPU-numpy", "numpy", np.__version__)
    print("T", T, "CAP", CAP, "CHUNK", CHUNK, "u2_words", roots_np().tolist(),
          "initial_prefixes_2_to_3", len(states))
    rows: list[Stage] = []
    for n in range(3, 17):
        states, row = one_stage_np(states, n)
        rows.append(row)
        print(row.line())
        if row.capped or row.admissible == 0 or n == 16:
            break
    return rows


def run_gpu() -> list[Stage]:
    import torch

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA backend requested but torch.cuda.is_available() is false")
    device = torch.device("cuda")
    temp = torch.as_tensor(TEMP_NP, dtype=torch.uint8, device=device)
    sub = torch.arange(255, -1, -1, dtype=torch.uint8, device=device)
    popc = torch.as_tensor(POPC_NP, dtype=torch.uint8, device=device)
    states = torch.as_tensor(initial_np(), dtype=torch.uint8)
    print("backend GPU-torch", "torch", torch.__version__, "cuda", torch.version.cuda,
          "device", torch.cuda.get_device_name(device))
    print("T", T, "CAP", CAP, "CHUNK", CHUNK, "u2_words", roots_np().tolist(),
          "initial_prefixes_2_to_3", len(states))
    rows: list[Stage] = []

    for n in range(3, 17):
        N = len(states)
        if n == 16:
            valid_count = 0
            maxfree = -1
            for i0 in range(0, N, CHUNK):
                st = states[i0 : i0 + CHUNK].to(device, non_blocking=False)
                w = st[:, n - 2]
                A = st[:, n - 3] ^ w
                g = torch.full((len(st),), MASK, dtype=torch.uint8, device=device)
                for d in DIVS[n]:
                    g &= torch.tensor(MASK, dtype=torch.uint8, device=device) ^ st[:, d - 2]
                E = temp[w.long()] ^ g
                ok = (E & (torch.tensor(MASK, dtype=torch.uint8, device=device) ^ A)) == 0
                valid_count += int(ok.sum().item())
                if bool(ok.any()):
                    maxfree = max(maxfree, int(popc[(torch.tensor(MASK, dtype=torch.uint8, device=device) ^ A[ok]).long()].max().item()))
            row = Stage(n, N, valid_count, 0, 0, maxfree, False, True)
            rows.append(row)
            print(row.line())
            break

        out = np.empty((CAP, WIDTH), dtype=np.uint8)
        written = 0
        admissible = 0
        maxfree = -1
        extensions_seen = 0
        capped = False
        mask_t = torch.tensor(MASK, dtype=torch.uint8, device=device)
        for i0 in range(0, N, CHUNK):
            # A hard 1-GiB free-memory guard is part of the frozen contract.
            free_mem, _total_mem = torch.cuda.mem_get_info(device)
            if free_mem < 1 << 30:
                raise MemoryError(f"GPU free-memory guard: {free_mem} bytes")
            st = states[i0 : i0 + CHUNK].to(device, non_blocking=False)
            w = st[:, n - 2]
            A = st[:, n - 3] ^ w
            g = torch.full((len(st),), MASK, dtype=torch.uint8, device=device)
            for d in DIVS[n]:
                g &= mask_t ^ st[:, d - 2]
            E = temp[w.long()] ^ g
            ok = (E & (mask_t ^ A)) == 0
            if not bool(ok.any()):
                continue
            idx = torch.nonzero(ok, as_tuple=False).flatten()
            base = (w[idx] ^ E[idx]) & A[idx]
            free = mask_t ^ A[idx]
            row_counts = (1 << popc[free.long()].long()).cpu().numpy()
            total = int(row_counts.sum())
            room = CAP - written

            if total <= room:
                stv = st[idx]
                cand = stv[:, None, :].expand(-1, 256, -1).clone()
                # Append u_{n+1}; coordinate u_k occupies column k-2.
                cand[:, :, n - 1] = base[:, None] | sub[None, :]
                allowed = (sub[None, :] & (free[:, None] ^ mask_t)) == 0
                selected = cand.reshape(-1, WIDTH)[allowed.reshape(-1)].cpu().numpy()
                out[written : written + len(selected)] = selected
                written += len(selected)
                admissible += len(idx)
                maxfree = max(maxfree, int(popc[free.long()].max().item()))
                extensions_seen += len(selected)
                continue

            cumulative = np.cumsum(row_counts)
            stop = int(np.searchsorted(cumulative, room + 1, side="left"))
            use = stop + 1
            free_use = free[:use]
            cand = st[idx[:use], None, :].expand(-1, 256, -1).clone()
            cand[:, :, n - 1] = base[:use, None] | sub[None, :]
            allowed = (sub[None, :] & (free_use[:, None] ^ mask_t)) == 0
            selected = cand.reshape(-1, WIDTH)[allowed.reshape(-1)].cpu().numpy()
            need = CAP - written
            out[written:CAP] = selected[:need]
            written = CAP
            admissible += use
            maxfree = max(maxfree, int(popc[free_use.long()].max().item()))
            extensions_seen = CAP + 1
            capped = True
            break

        # Keep the authoritative prefix ledger on host as compact uint8; the
        # next chunk is copied explicitly to CUDA at the stage boundary.
        states = torch.as_tensor(out[:written], dtype=torch.uint8)
        row = Stage(n, N, admissible, extensions_seen, written, maxfree, capped, False)
        rows.append(row)
        print(row.line())
        if capped or admissible == 0:
            break
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=("cpu", "gpu", "both"), default="both")
    args = ap.parse_args()
    print("python", sys.version.split()[0], "platform", platform.platform())
    result = {}
    if args.backend in ("cpu", "both"):
        result["cpu"] = run_cpu()
    if args.backend in ("gpu", "both"):
        result["gpu"] = run_gpu()
    if "cpu" in result and "gpu" in result:
        c = [r.__dict__ for r in result["cpu"]]
        g = [r.__dict__ for r in result["gpu"]]
        # Backend equality is required for every reported field.
        if c != g:
            raise AssertionError(f"CPU/GPU stage mismatch:\nCPU={c}\nGPU={g}")
        print("BACKEND_AGREEMENT exact_stage_records", len(c))


if __name__ == "__main__":
    main()
