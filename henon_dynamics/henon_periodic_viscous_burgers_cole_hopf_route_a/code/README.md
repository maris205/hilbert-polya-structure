# C195 executable certificate

Run from the package root:

```bash
python3 code/c195_burgers_producer.py
python3 code/c195_burgers_checker.py
python3 code/c195_burgers_sympy_crosscheck.py
python3 code/c195_burgers_replay.py
python3 code/c195_burgers_mutation.py
python3 code/c195_release_manifest.py
```

- The producer uses exact `Fraction` complex Laurent arithmetic and writes canonical
  evidence.
- The checker does not import the producer. It regenerates the 24 cases using a
  separately implemented series algebra and checks all stored cells and metadata.
- The SymPy program separately expands nine representative nonlinear identities.
- Replay imports only the producer and demands byte identity.
- Mutation testing sends repaired-hash semantic attacks and a stale-hash attack
  through the independent checker.
- The release script inventories 27 payloads and writes the self-excluded manifest.

The normalized \(L=2\pi\) finite census is a regression oracle only. The analytic
proof for every \(\nu>0,L>0,m\in\mathbb R,s>3/2\) is in `THEOREM_PACKAGE.md`.
