# C373 executable lanes

The six scripts respectively produce evidence, independently reconstruct it,
check exact symbolic identities and Jacobi equations, replay two isolated
builds, attack repaired hashes and types, and close the release manifest.

```bash
python -B code/c373_higgs_oscillator_producer.py
python -B code/c373_higgs_oscillator_checker.py
python -B code/c373_higgs_oscillator_sympy_crosscheck.py
python -B code/c373_higgs_oscillator_replay.py
python -B code/c373_higgs_oscillator_mutation.py
python -B code/c373_release_manifest.py
```

All six refuse optimized Python. Python dependencies are PyYAML and SymPy.
The PDF lane additionally uses LuaLaTeX and Poppler tools.
The release source gate rejects unescaped `quad` or `qquad` TeX commands;
hostile tests cover both rejection and legal escaped-command controls.
