#!/usr/bin/env python3
"""Separately allocated precision continuation; original script is unchanged.

Input remains only p=3,e=2. The first run certified delta=144 but
N=512 failed its N>4*delta+8 gate. This run uses exactly N=1024.
No other parameter or precision is attempted.
"""

import sys

import diagnostic_p3_e2 as core


def main():
    precision = 1024
    core.emit("START_PRECISION_CONTINUATION", p=3, e=2,
              precision=precision, previously_certified_delta=144,
              previous_result="INCONCLUSIVE_AT_ALLOCATED_CAP_exit_2",
              cpu_limit_s=60, wall_limit_s=120,
              address_space_limit_bytes=2147483648)
    q = core.build_q(precision)
    m, _ = core.hensel(q, precision)
    if core.certify(m, precision):
        core.emit("END_PRECISION_CONTINUATION", status="CERTIFIED_PAIR",
                  mathematical_parameter_pairs=1)
        return 0
    core.emit("END_PRECISION_CONTINUATION", status="INCONCLUSIVE_NO_FURTHER_PRECISION",
              mathematical_parameter_pairs=1)
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        core.emit("END_PRECISION_CONTINUATION", status="FAILED_NO_CONCLUSION",
                  exception=repr(exc))
        raise
