# Reproduce

From this package run Python with -B; requirements.txt freezes installed mathematical library versions. The release runner refuses -O/-OO.

```sh
python -B code/c398_wall_producer.py
python -B code/c398_wall_checker.py
python -B code/c398_wall_sympy_crosscheck.py
python -B code/c398_wall_replay.py
python -B code/c398_wall_mutation.py
python -B -m unittest tests/test_c398_smoke.py
python -B code/c398_release_manifest.py --build-pdfs
python -B code/c398_release_manifest.py --write
python -B code/c398_release_manifest.py
```

The first two commands replace only the package's generated evidence; the final nonwrite command reconstructs all checks and hashes without modifying the package. SOURCE_DATE_EPOCH1788566400 and two settled LuaLaTeX passes fix each build. Temporary directories are individually scoped. The manifest excludes itself and requires exact physical membership, not a loose hash prefix. Build logs are generated artifacts. No external data download is required for numerical reproduction.
