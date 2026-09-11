# Exact no-generation environment/request delta

Baseline: ../p213_initial_build_preparation01/NATIVE_REQUESTS.proposed.json
SHA256 de4c6365b1ca0da1e1d79963d161affcac1135111545a1cfb34b14f85b5b25d7.

Unchanged build source:
../p213_initial_build_preparation01/BUILD_REQUEST.sh
SHA256 b0cd46485d5f22aebd5edc7fa14d37902e627a19ed441b0dfdb54d52a629cfa4.

Only differences in this packet's complete NATIVE_REQUESTS.proposed.json:

1. Add controlled_environment.MKTEXFMT, MKTEXPK, MKTEXTFM, MKTEXMF,
   MKTEXTEX, each the string "0".
2. Add exactly the literal assignment sequence below before the existing
   /bin/bash --noprofile --norc segment of request.cmd:

       MKTEXFMT=0 MKTEXPK=0 MKTEXTFM=0 MKTEXMF=0 MKTEXTEX=0

Every other JSON field/value, native request setting, source path, future
binding/output, four-pass order, failure behavior and continuation rule is
unchanged. No script or source edit, source staging, runtime invocation or
grant is carried by the proposed build envelope. The separate actual
resolution calls used this revised environment and are in RUNTIME_NATIVE.

The original environment had undefined MKTEXFMT/PK/TFM query results; the
installed texmf.cnf explains that program defaults may enable helpers.
Root agreed the five explicit zero values. Existing format/map and all
selected package/font candidates resolve under the revised environment.
This is a no-generation policy, not an installation or successful-build
claim. Preserve failures; a missing input under this policy is not repaired.

## Important unchanged-script capture boundary

The frozen shell's REQUEST_AND_BINDING.sha256 still hashes the original
NATIVE_REQUESTS.proposed.json, because that is its literal unchanged code.
That original hash is preparation provenance, not the newly effective
invocation. Root must separately preserve and pin this packet's replacement
native envelope and the actual product launch/continuations in its binding
and execution receipt. Do not label the old internal request hash as a
capture of the five changed environment fields. The build's runtime checks
still use the exact later root-bound absolute-path RUNTIME_INPUTS.sha256.

The proposal retains all original null root/grant fields and false
execution_authorized. Source/read reception and the parent's environment
policy decision are not a build grant.
