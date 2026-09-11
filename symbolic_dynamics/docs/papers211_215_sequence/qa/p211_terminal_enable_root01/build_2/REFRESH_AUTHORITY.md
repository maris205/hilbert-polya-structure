# Build 2: one independent current-key refresh

Root separately authorizes exactly one build-2 refresh, after source02's
complete current pre-invocation guard. This is independent of build1's
successful capture; no enable, builder, science, view or acceptance follows
automatically. Preserve all native evidence and failures. HOLD_EXTERNAL.

```json
{
  "schema": "p211-terminal-controller-root-authority-v1",
  "issuer": "/root",
  "phase": "refresh",
  "build_number": 2,
  "decision": "AUTHORIZE_ONE_CURRENT_TERMINAL_KEY_REFRESH_ONLY",
  "controller": {
    "path": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_terminal_enable_preparation01/terminal_control.py",
    "pin": {
      "bytes": 41305,
      "sha256": "238369a33404a06ee4789af4bb7afd447213d70c21266b72cdca5d4a047ecea4"
    }
  },
  "preparation_seal": {
    "path": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_terminal_enable_preparation01/SHA256SUMS",
    "pin": {
      "bytes": 779,
      "sha256": "5c357f87ae19a7685539e9147e35bf8b32bccc5ba9c20aa2bf693e70c9ae33cd"
    }
  },
  "input_plan": {
    "path": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_terminal_enable_preparation01/INPUT_PLAN.json",
    "pin": {
      "bytes": 94596,
      "sha256": "4e41d0c20016e9d331a7faf22cc683dad3fbedd00288d935fbff55ad343394a3"
    }
  },
  "phase_output": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_terminal_enable_root01/build_2/refresh01",
  "cold_output": "/root/autodl-tmp/symbolic_dynamics/papers/211-kernel-image-projection-feedback/qa_final/cold_build_2",
  "controller_environment": {
    "PATH": "/usr/bin:/bin",
    "LANG": "C.UTF-8",
    "LC_ALL": "C.UTF-8",
    "TZ": "UTC"
  },
  "build_environment": {
    "PATH": "/usr/bin:/bin",
    "LANG": "C.UTF-8",
    "LC_ALL": "C.UTF-8",
    "TZ": "UTC",
    "SOURCE_DATE_EPOCH": "1788825600",
    "FORCE_SOURCE_DATE": "1",
    "openin_any": "p",
    "openout_any": "p"
  },
  "cwd": "/root/autodl-tmp/symbolic_dynamics",
  "required_receipts": {
    "whole_round2_root_reception": {
      "path": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_round2_original_root01/RECEPTION.md",
      "pin": {
        "bytes": 4280,
        "sha256": "d6819e54b56238e72c142cd25b8348ab2161ab9740130f500c87bfed7441dbde"
      }
    },
    "accepted_terminal_binding_source_reception": {
      "path": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_terminal_binding_source_root01/RECEPTION.md",
      "pin": {
        "bytes": 2955,
        "sha256": "36a236b937d553f1116a2ab47218c13ac62ce7eb7dce6648ba141465292c9d0c"
      }
    },
    "accepted_disabled_assembly_reception": {
      "path": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_terminal_binding_root01/ASSEMBLY_RECEPTION.md",
      "pin": {
        "bytes": 2073,
        "sha256": "4564a230f91ea7259021d4f739ab6dc3b12745524eb2150e3c1aadf23e10decb"
      }
    },
    "controller_source_reception": {
      "path": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_terminal_enable_root01/SOURCE_RECEPTION.md",
      "pin": {
        "bytes": 5765,
        "sha256": "a49d0145e184af65c976e2a199fb91c9ee560774a11482686fc93ce872e406f4"
      }
    }
  },
  "new_science": 0,
  "new_page_views": 0,
  "terminal_acceptance": false,
  "external": "OWNER_AMBER / HOLD_EXTERNAL"
}
```
