# CAPD dependency lock for R401-VAL-V2

The local validated-flow producer uses the external CAPD::DynSys library.
CAPD is not vendored in this repository.

- CAPD version: 6.1.0
- pinned commit: `731079217a9254ea2948d742df2b170895effe7f`
- interval arithmetic: MPFR-backed `MpInterval`
- build option: `-DCAPD_ENABLE_MULTIPRECISION=ON`
- required development libraries on the reference host:
  `libmpfr-dev`, `libgmp-dev`
- compiler contract: C++17 with `-frounding-math`

Reference build:

```bash
git clone --depth 1 https://github.com/CAPDGroup/CAPD.git /tmp/capd-r401
git -C /tmp/capd-r401 fetch --depth 1 origin 731079217a9254ea2948d742df2b170895effe7f
git -C /tmp/capd-r401 checkout 731079217a9254ea2948d742df2b170895effe7f

cmake \
  -S /tmp/capd-r401 \
  -B /tmp/capd-r401/build-mp \
  -DCMAKE_BUILD_TYPE=Release \
  -DCAPD_ENABLE_MULTIPRECISION=ON \
  -DCAPD_BUILD_TESTS=OFF \
  -DCAPD_BUILD_EXAMPLES=OFF

cmake --build /tmp/capd-r401/build-mp -j 16
```

The experiment runner must be given both the source checkout and the
multiprecision build directory.  It refuses a commit mismatch and checks for
the MPFR, GMP, and directed-rounding compiler flags before compiling the local
producer.

CAPD is distributed under GPLv3.  The project archives source, hashes, and
plain-text certificates; redistribution of linked binaries must comply with
CAPD's license.

