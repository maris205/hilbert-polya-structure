# C305 test report

The release command runs producer, producer-independent checker, SymPy,
isolated replay, and hostile mutation lanes. It then verifies:

- exact provenance, scope, evaluator, evidence self-hash, and YAML semantics;
- all 29 ordered unique cases and 744 evidence leaves;
- weak/critical/strong root signs, every time interval, speed saturation,
  HJB, scaling, and boundary rows;
- rejection of 85/85 repaired-hash or parser/type mutations;
- three substantively distinct rounds and final PDF;
- two fresh double-pass fixed-epoch builds per round;
- warning-free settled logs, embedded/subset fonts, PDF text sentinels,
  rasterization, and exact 27-payload / 28-physical-file closure.

The checker explicitly rejects `python -O`. The released commands use
ordinary `python -B`.
