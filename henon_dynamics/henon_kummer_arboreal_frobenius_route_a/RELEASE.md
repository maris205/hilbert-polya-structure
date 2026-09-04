# Release

The release object is closed by `C374_RELEASE_MANIFEST.json`, whose file ledger excludes only the manifest itself.  A release requires every analytic/source/scope lane, independent numerical lane, hostile mutation, smoke test, exact membership check, and deterministic PDF gate to pass.

Canonical command:

```bash
python -B code/c374_release_manifest.py --write --build-pdfs
python -B code/c374_release_manifest.py
```

No commit or push is performed by the package.
