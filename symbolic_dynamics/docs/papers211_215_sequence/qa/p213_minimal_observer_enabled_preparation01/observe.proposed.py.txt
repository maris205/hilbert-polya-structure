"""P213 exact finite-permission observer; operational authority is external."""

# The preparation copy has an unconditional gate before its complete literal.
# Literal permissions only; never loaded from a file or predicted actual rows.
BINDING = {
  "id": "P213_MINIMAL_FINITE_PERMISSION_OBSERVER_ENABLED01",
  "interpreter": {
    "lexical": "/usr/bin/python3.10",
    "final": "/usr/bin/python3.10",
    "links": [],
    "optional": False,
    "absence_required": False,
    "earliest_phase": "early",
    "roles": [
      "mapped_file"
    ],
    "observed_presence": None,
    "observed_key": None
  },
  "observer": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py",
  "cwd": "/root/autodl-tmp/symbolic_dynamics",
  "launch_policy": {
    "implementation": "cpython",
    "release": [
      3,
      10,
      12,
      "final",
      0
    ],
    "cache_tag": "cpython-310",
    "platform": "linux",
    "argv": [
      "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py"
    ],
    "orig_argv": [
      "/usr/bin/python3.10",
      "-I",
      "-S",
      "-B",
      "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py"
    ],
    "sys_path": [
      "/usr/lib/python310.zip",
      "/usr/lib/python3.10",
      "/usr/lib/python3.10/lib-dynload"
    ],
    "prefixes_must_equal": "/usr",
    "pycache_prefix": None,
    "dont_write_bytecode": True,
    "flag_names": [
      "debug",
      "inspect",
      "interactive",
      "optimize",
      "dont_write_bytecode",
      "no_user_site",
      "no_site",
      "ignore_environment",
      "verbose",
      "bytes_warning",
      "quiet",
      "hash_randomization",
      "isolated",
      "dev_mode",
      "utf8_mode",
      "warn_default_encoding",
      "int_max_str_digits"
    ],
    "flag_requirements": {
      "debug": 0,
      "inspect": 0,
      "interactive": 0,
      "optimize": 0,
      "dont_write_bytecode": 1,
      "no_user_site": 1,
      "no_site": 1,
      "ignore_environment": 1,
      "verbose": 0,
      "bytes_warning": 0,
      "quiet": 0,
      "hash_randomization": 1,
      "isolated": 1,
      "dev_mode": False,
      "utf8_mode": 1,
      "warn_default_encoding": 0,
      "int_max_str_digits": -1
    },
    "encodings_allowed": [
      "utf-8",
      "UTF-8"
    ],
    "filesystem_errors": "surrogateescape",
    "stdout_errors": "surrogateescape",
    "stderr_errors": "backslashreplace",
    "full_actual_record": None,
    "unconstrained_but_bounded_recorded_fields": [
      "sys.version_build_text",
      "sys.byteorder",
      "sys.abiflags",
      "sys.hexversion",
      "sys.maxsize",
      "all_scalar_sys.implementation_members",
      "sys.builtin_module_names"
    ]
  },
  "flag_names": [
    "debug",
    "inspect",
    "interactive",
    "optimize",
    "dont_write_bytecode",
    "no_user_site",
    "no_site",
    "ignore_environment",
    "verbose",
    "bytes_warning",
    "quiet",
    "hash_randomization",
    "isolated",
    "dev_mode",
    "utf8_mode",
    "warn_default_encoding",
    "int_max_str_digits"
  ],
  "module_names": {
    "early": [
      "__main__",
      "_abc",
      "_codecs",
      "_frozen_importlib",
      "_frozen_importlib_external",
      "_imp",
      "_io",
      "_signal",
      "_thread",
      "_warnings",
      "_weakref",
      "abc",
      "builtins",
      "codecs",
      "encodings",
      "encodings.aliases",
      "encodings.utf_8",
      "io",
      "marshal",
      "posix",
      "sys",
      "time",
      "zipimport"
    ],
    "helper": [
      "__main__",
      "_abc",
      "_blake2",
      "_codecs",
      "_collections",
      "_collections_abc",
      "_frozen_importlib",
      "_frozen_importlib_external",
      "_functools",
      "_hashlib",
      "_imp",
      "_io",
      "_json",
      "_locale",
      "_md5",
      "_operator",
      "_sha1",
      "_sha256",
      "_sha3",
      "_sha512",
      "_signal",
      "_sre",
      "_stat",
      "_thread",
      "_warnings",
      "_weakref",
      "abc",
      "builtins",
      "codecs",
      "collections",
      "copyreg",
      "encodings",
      "encodings.aliases",
      "encodings.utf_8",
      "enum",
      "functools",
      "genericpath",
      "hashlib",
      "io",
      "itertools",
      "json",
      "json.decoder",
      "json.encoder",
      "json.scanner",
      "keyword",
      "marshal",
      "operator",
      "os",
      "os.path",
      "posix",
      "posixpath",
      "re",
      "reprlib",
      "sre_compile",
      "sre_constants",
      "sre_parse",
      "stat",
      "sys",
      "time",
      "types",
      "warnings",
      "zipimport"
    ],
    "closing": [
      "__main__",
      "_abc",
      "_blake2",
      "_codecs",
      "_collections",
      "_collections_abc",
      "_frozen_importlib",
      "_frozen_importlib_external",
      "_functools",
      "_hashlib",
      "_imp",
      "_io",
      "_json",
      "_locale",
      "_md5",
      "_operator",
      "_sha1",
      "_sha256",
      "_sha3",
      "_sha512",
      "_signal",
      "_sre",
      "_stat",
      "_thread",
      "_warnings",
      "_weakref",
      "abc",
      "builtins",
      "codecs",
      "collections",
      "copyreg",
      "encodings",
      "encodings.aliases",
      "encodings.utf_8",
      "enum",
      "functools",
      "genericpath",
      "hashlib",
      "io",
      "itertools",
      "json",
      "json.decoder",
      "json.encoder",
      "json.scanner",
      "keyword",
      "marshal",
      "operator",
      "os",
      "os.path",
      "posix",
      "posixpath",
      "re",
      "reprlib",
      "sre_compile",
      "sre_constants",
      "sre_parse",
      "stat",
      "sys",
      "time",
      "types",
      "warnings",
      "zipimport"
    ]
  },
  "required_module_names": {
    "early": [
      "__main__",
      "builtins",
      "sys"
    ],
    "helper": [
      "__main__",
      "builtins",
      "hashlib",
      "json",
      "os",
      "sys"
    ],
    "closing": [
      "__main__",
      "builtins",
      "hashlib",
      "json",
      "os",
      "sys"
    ]
  },
  "modules": {
    "__main__": {
      "mechanism": "direct_script",
      "file": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py",
      "file_roles": [
        {
          "path": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py",
          "role": "direct_script_source",
          "content_required": True
        }
      ],
      "provenance": "New prospective enabled01 path explicitly selected for this preparation; not a current presence or executed-source fact",
      "observed_row": None
    },
    "_abc": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_blake2": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_codecs": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_collections": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_collections_abc": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/_collections_abc.py",
      "file": "/usr/lib/python3.10/_collections_abc.py",
      "cache": "/usr/lib/python3.10/__pycache__/_collections_abc.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/_collections_abc.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/_collections_abc.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "os imports its mapping ABCs; collections imports it; not the separate collections.abc shim.",
      "observed_row": None
    },
    "_frozen_importlib": {
      "mechanism": "frozen",
      "nominal_file": "/usr/lib/python3.10/importlib/_bootstrap.py",
      "file_roles": [],
      "provenance": "POLICY.proposed.json frozen_nominal_names; nominal label only, no file read role",
      "observed_row": None
    },
    "_frozen_importlib_external": {
      "mechanism": "frozen",
      "nominal_file": "/usr/lib/python3.10/importlib/_bootstrap_external.py",
      "file_roles": [],
      "provenance": "POLICY.proposed.json frozen_nominal_names; nominal label only, no file read role",
      "observed_row": None
    },
    "_functools": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_hashlib": {
      "mechanism": "extension_file",
      "origin": "/usr/lib/python3.10/lib-dynload/_hashlib.cpython-310-x86_64-linux-gnu.so",
      "file": "/usr/lib/python3.10/lib-dynload/_hashlib.cpython-310-x86_64-linux-gnu.so",
      "cache": None,
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/lib-dynload/_hashlib.cpython-310-x86_64-linux-gnu.so",
          "role": "extension_origin",
          "content_required": True
        }
      ],
      "provenance": "hashlib attempts its OpenSSL extension; only this exact historical extension spelling is proposed.",
      "observed_row": None
    },
    "_imp": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_io": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_json": {
      "mechanism": "extension_file",
      "origin": "/usr/lib/python3.10/lib-dynload/_json.cpython-310-x86_64-linux-gnu.so",
      "file": "/usr/lib/python3.10/lib-dynload/_json.cpython-310-x86_64-linux-gnu.so",
      "cache": None,
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/lib-dynload/_json.cpython-310-x86_64-linux-gnu.so",
          "role": "extension_origin",
          "content_required": True
        }
      ],
      "provenance": "json encoder/decoder/scanner attempt the C accelerator; only this exact historical extension spelling is proposed.",
      "observed_row": None
    },
    "_locale": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_md5": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_operator": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_sha1": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_sha256": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_sha3": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_sha512": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_signal": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_sre": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_stat": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_thread": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_warnings": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "_weakref": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "abc": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/abc.py",
      "file": "/usr/lib/python3.10/abc.py",
      "cache": "/usr/lib/python3.10/__pycache__/abc.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/abc.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/abc.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "io startup and os/_collections_abc/functools require abc.",
      "observed_row": None
    },
    "builtins": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "codecs": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/codecs.py",
      "file": "/usr/lib/python3.10/codecs.py",
      "cache": "/usr/lib/python3.10/__pycache__/codecs.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/codecs.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/codecs.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "UTF-8 startup encodings and json import codecs.",
      "observed_row": None
    },
    "collections": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/collections/__init__.py",
      "file": "/usr/lib/python3.10/collections/__init__.py",
      "cache": "/usr/lib/python3.10/collections/__pycache__/__init__.cpython-310.pyc",
      "package_path": "/usr/lib/python3.10/collections",
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/collections/__init__.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/collections/__pycache__/__init__.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "functools imports namedtuple from collections.",
      "observed_row": None
    },
    "copyreg": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/copyreg.py",
      "file": "/usr/lib/python3.10/copyreg.py",
      "cache": "/usr/lib/python3.10/__pycache__/copyreg.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/copyreg.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/copyreg.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "re imports copyreg for its pattern support.",
      "observed_row": None
    },
    "encodings": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/encodings/__init__.py",
      "file": "/usr/lib/python3.10/encodings/__init__.py",
      "cache": "/usr/lib/python3.10/encodings/__pycache__/__init__.cpython-310.pyc",
      "package_path": "/usr/lib/python3.10/encodings",
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/encodings/__init__.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/encodings/__pycache__/__init__.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "CPython startup codec package for proposed UTF-8 mode.",
      "observed_row": None
    },
    "encodings.aliases": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/encodings/aliases.py",
      "file": "/usr/lib/python3.10/encodings/aliases.py",
      "cache": "/usr/lib/python3.10/encodings/__pycache__/aliases.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/encodings/aliases.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/encodings/__pycache__/aliases.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "encodings imports its alias table.",
      "observed_row": None
    },
    "encodings.utf_8": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/encodings/utf_8.py",
      "file": "/usr/lib/python3.10/encodings/utf_8.py",
      "cache": "/usr/lib/python3.10/encodings/__pycache__/utf_8.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/encodings/utf_8.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/encodings/__pycache__/utf_8.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "UTF-8 startup codec selected by the new LC_ALL=C/UTF-8-mode policy, not the old C.UTF-8 record.",
      "observed_row": None
    },
    "enum": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/enum.py",
      "file": "/usr/lib/python3.10/enum.py",
      "cache": "/usr/lib/python3.10/__pycache__/enum.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/enum.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/enum.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "re imports enum.",
      "observed_row": None
    },
    "functools": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/functools.py",
      "file": "/usr/lib/python3.10/functools.py",
      "cache": "/usr/lib/python3.10/__pycache__/functools.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/functools.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/functools.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "re imports functools.",
      "observed_row": None
    },
    "genericpath": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/genericpath.py",
      "file": "/usr/lib/python3.10/genericpath.py",
      "cache": "/usr/lib/python3.10/__pycache__/genericpath.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/genericpath.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/genericpath.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "posixpath imports genericpath.",
      "observed_row": None
    },
    "hashlib": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/hashlib.py",
      "file": "/usr/lib/python3.10/hashlib.py",
      "cache": "/usr/lib/python3.10/__pycache__/hashlib.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/hashlib.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/hashlib.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "One of exactly three post-earliest observer helper imports; whole-file SHA-256 acquisition.",
      "observed_row": None
    },
    "io": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/io.py",
      "file": "/usr/lib/python3.10/io.py",
      "cache": "/usr/lib/python3.10/__pycache__/io.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/io.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/io.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "CPython I/O bootstrap; built-in open and stream setup, not a new explicit observer import.",
      "observed_row": None
    },
    "itertools": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "json": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/json/__init__.py",
      "file": "/usr/lib/python3.10/json/__init__.py",
      "cache": "/usr/lib/python3.10/json/__pycache__/__init__.cpython-310.pyc",
      "package_path": "/usr/lib/python3.10/json",
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/json/__init__.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/json/__pycache__/__init__.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "One of exactly three post-earliest observer helper imports; ASCII JSON serialization.",
      "observed_row": None
    },
    "json.decoder": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/json/decoder.py",
      "file": "/usr/lib/python3.10/json/decoder.py",
      "cache": "/usr/lib/python3.10/json/__pycache__/decoder.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/json/decoder.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/json/__pycache__/decoder.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "json package imports its decoder even though observer only serializes.",
      "observed_row": None
    },
    "json.encoder": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/json/encoder.py",
      "file": "/usr/lib/python3.10/json/encoder.py",
      "cache": "/usr/lib/python3.10/json/__pycache__/encoder.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/json/encoder.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/json/__pycache__/encoder.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "json package imports its encoder for serialization.",
      "observed_row": None
    },
    "json.scanner": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/json/scanner.py",
      "file": "/usr/lib/python3.10/json/scanner.py",
      "cache": "/usr/lib/python3.10/json/__pycache__/scanner.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/json/scanner.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/json/__pycache__/scanner.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "json.decoder imports json.scanner.",
      "observed_row": None
    },
    "keyword": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/keyword.py",
      "file": "/usr/lib/python3.10/keyword.py",
      "cache": "/usr/lib/python3.10/__pycache__/keyword.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/keyword.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/keyword.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "collections imports iskeyword.",
      "observed_row": None
    },
    "marshal": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "operator": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/operator.py",
      "file": "/usr/lib/python3.10/operator.py",
      "cache": "/usr/lib/python3.10/__pycache__/operator.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/operator.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/operator.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "collections imports operator helpers; operator's native support is separately builtin-constrained.",
      "observed_row": None
    },
    "os": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/os.py",
      "file": "/usr/lib/python3.10/os.py",
      "cache": "/usr/lib/python3.10/__pycache__/os.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/os.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/os.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "One of exactly three post-earliest observer helper imports; bounded file/proc scalar operations.",
      "observed_row": None
    },
    "os.path": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/posixpath.py",
      "file": "/usr/lib/python3.10/posixpath.py",
      "cache": "/usr/lib/python3.10/__pycache__/posixpath.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/posixpath.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/posixpath.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "os installs the posixpath alias; same selected source/cache key, not a second source file.",
      "observed_row": None
    },
    "posix": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "posixpath": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/posixpath.py",
      "file": "/usr/lib/python3.10/posixpath.py",
      "cache": "/usr/lib/python3.10/__pycache__/posixpath.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/posixpath.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/posixpath.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "Linux os.path module and lexical path functions.",
      "observed_row": None
    },
    "re": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/re.py",
      "file": "/usr/lib/python3.10/re.py",
      "cache": "/usr/lib/python3.10/__pycache__/re.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/re.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/re.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "json encoder/decoder/scanner import re.",
      "observed_row": None
    },
    "reprlib": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/reprlib.py",
      "file": "/usr/lib/python3.10/reprlib.py",
      "cache": "/usr/lib/python3.10/__pycache__/reprlib.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/reprlib.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/reprlib.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "functools and collections import recursive_repr.",
      "observed_row": None
    },
    "sre_compile": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/sre_compile.py",
      "file": "/usr/lib/python3.10/sre_compile.py",
      "cache": "/usr/lib/python3.10/__pycache__/sre_compile.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/sre_compile.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/sre_compile.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "re imports its compiler.",
      "observed_row": None
    },
    "sre_constants": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/sre_constants.py",
      "file": "/usr/lib/python3.10/sre_constants.py",
      "cache": "/usr/lib/python3.10/__pycache__/sre_constants.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/sre_constants.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/sre_constants.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "sre_compile/sre_parse import their finite regex constants.",
      "observed_row": None
    },
    "sre_parse": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/sre_parse.py",
      "file": "/usr/lib/python3.10/sre_parse.py",
      "cache": "/usr/lib/python3.10/__pycache__/sre_parse.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/sre_parse.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/sre_parse.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "re/sre_compile import the parser; unicode-name lookups and warning-formatting expansions are excluded.",
      "observed_row": None
    },
    "stat": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/stat.py",
      "file": "/usr/lib/python3.10/stat.py",
      "cache": "/usr/lib/python3.10/__pycache__/stat.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/stat.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/stat.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "os and posixpath import stat; native _stat is separately builtin-constrained.",
      "observed_row": None
    },
    "sys": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "time": {
      "mechanism": "builtin",
      "nominal_file": None,
      "file_roles": [],
      "provenance": "POLICY.proposed.json module_policy builtin finite category; PROPOSAL.md and PRIMARY_NATIVE.json supply reasons",
      "observed_row": None
    },
    "types": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/types.py",
      "file": "/usr/lib/python3.10/types.py",
      "cache": "/usr/lib/python3.10/__pycache__/types.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/types.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/types.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "enum and functools import types members.",
      "observed_row": None
    },
    "warnings": {
      "mechanism": "source_file",
      "origin": "/usr/lib/python3.10/warnings.py",
      "file": "/usr/lib/python3.10/warnings.py",
      "cache": "/usr/lib/python3.10/__pycache__/warnings.cpython-310.pyc",
      "package_path": None,
      "file_roles": [
        {
          "path": "/usr/lib/python3.10/warnings.py",
          "role": "source_or_matching_source",
          "content_required": True
        },
        {
          "path": "/usr/lib/python3.10/__pycache__/warnings.cpython-310.pyc",
          "role": "eligible_nonoptimized_cache",
          "content_required": False
        }
      ],
      "provenance": "Conditional hashlib PBKDF2 fallback imports warnings; only initialization is admitted, not warning formatting/traceback expansion.",
      "observed_row": None
    },
    "zipimport": {
      "mechanism": "frozen",
      "nominal_file": "/usr/lib/python3.10/zipimport.py",
      "file_roles": [],
      "provenance": "POLICY.proposed.json frozen_nominal_names; nominal label only, no file read role",
      "observed_row": None
    }
  },
  "loader_ids": {
    "builtin": [
      "class",
      [
        "value",
        "_frozen_importlib"
      ],
      [
        "value",
        "BuiltinImporter"
      ]
    ],
    "frozen": [
      "class",
      [
        "value",
        "_frozen_importlib"
      ],
      [
        "value",
        "FrozenImporter"
      ]
    ],
    "source_file": [
      "instance",
      [
        "value",
        "_frozen_importlib_external"
      ],
      [
        "value",
        "SourceFileLoader"
      ]
    ],
    "extension_file": [
      "instance",
      [
        "value",
        "_frozen_importlib_external"
      ],
      [
        "value",
        "ExtensionFileLoader"
      ]
    ],
    "direct_script": [
      "instance",
      [
        "value",
        "_frozen_importlib_external"
      ],
      [
        "value",
        "SourceFileLoader"
      ]
    ]
  },
  "special_maps": [
    "",
    "[heap]",
    "[stack]",
    "[vvar]",
    "[vdso]",
    "[vsyscall]"
  ],
  "files": [
    {
      "lexical": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py",
      "final": "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py",
      "links": [],
      "optional": False,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "direct_script_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/bin/python3.10",
      "final": "/usr/bin/python3.10",
      "links": [],
      "optional": False,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/_collections_abc.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/_collections_abc.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/abc.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/abc.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/codecs.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/codecs.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/copyreg.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/copyreg.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/enum.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/enum.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/functools.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/functools.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/genericpath.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/genericpath.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/hashlib.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/hashlib.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/io.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/io.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/keyword.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/keyword.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/operator.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/operator.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/os.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/os.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/posixpath.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/posixpath.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/re.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/re.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/reprlib.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/reprlib.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/sre_compile.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/sre_compile.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/sre_constants.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/sre_constants.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/sre_parse.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/sre_parse.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/stat.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/stat.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/types.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/types.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/__pycache__/warnings.cpython-310.pyc",
      "final": "/usr/lib/python3.10/__pycache__/warnings.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/_collections_abc.py",
      "final": "/usr/lib/python3.10/_collections_abc.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/abc.py",
      "final": "/usr/lib/python3.10/abc.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/codecs.py",
      "final": "/usr/lib/python3.10/codecs.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/collections/__init__.py",
      "final": "/usr/lib/python3.10/collections/__init__.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/collections/__pycache__/__init__.cpython-310.pyc",
      "final": "/usr/lib/python3.10/collections/__pycache__/__init__.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/copyreg.py",
      "final": "/usr/lib/python3.10/copyreg.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/encodings/__init__.py",
      "final": "/usr/lib/python3.10/encodings/__init__.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/encodings/__pycache__/__init__.cpython-310.pyc",
      "final": "/usr/lib/python3.10/encodings/__pycache__/__init__.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/encodings/__pycache__/aliases.cpython-310.pyc",
      "final": "/usr/lib/python3.10/encodings/__pycache__/aliases.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/encodings/__pycache__/utf_8.cpython-310.pyc",
      "final": "/usr/lib/python3.10/encodings/__pycache__/utf_8.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/encodings/aliases.py",
      "final": "/usr/lib/python3.10/encodings/aliases.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/encodings/utf_8.py",
      "final": "/usr/lib/python3.10/encodings/utf_8.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/enum.py",
      "final": "/usr/lib/python3.10/enum.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/functools.py",
      "final": "/usr/lib/python3.10/functools.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/genericpath.py",
      "final": "/usr/lib/python3.10/genericpath.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/hashlib.py",
      "final": "/usr/lib/python3.10/hashlib.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/io.py",
      "final": "/usr/lib/python3.10/io.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/json/__init__.py",
      "final": "/usr/lib/python3.10/json/__init__.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/json/__pycache__/__init__.cpython-310.pyc",
      "final": "/usr/lib/python3.10/json/__pycache__/__init__.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/json/__pycache__/decoder.cpython-310.pyc",
      "final": "/usr/lib/python3.10/json/__pycache__/decoder.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/json/__pycache__/encoder.cpython-310.pyc",
      "final": "/usr/lib/python3.10/json/__pycache__/encoder.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/json/__pycache__/scanner.cpython-310.pyc",
      "final": "/usr/lib/python3.10/json/__pycache__/scanner.cpython-310.pyc",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "eligible_nonoptimized_cache"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/json/decoder.py",
      "final": "/usr/lib/python3.10/json/decoder.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/json/encoder.py",
      "final": "/usr/lib/python3.10/json/encoder.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/json/scanner.py",
      "final": "/usr/lib/python3.10/json/scanner.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/keyword.py",
      "final": "/usr/lib/python3.10/keyword.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/lib-dynload/_hashlib.cpython-310-x86_64-linux-gnu.so",
      "final": "/usr/lib/python3.10/lib-dynload/_hashlib.cpython-310-x86_64-linux-gnu.so",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "extension_origin",
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/lib-dynload/_json.cpython-310-x86_64-linux-gnu.so",
      "final": "/usr/lib/python3.10/lib-dynload/_json.cpython-310-x86_64-linux-gnu.so",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "extension_origin",
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/operator.py",
      "final": "/usr/lib/python3.10/operator.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/os.py",
      "final": "/usr/lib/python3.10/os.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/posixpath.py",
      "final": "/usr/lib/python3.10/posixpath.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/re.py",
      "final": "/usr/lib/python3.10/re.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/reprlib.py",
      "final": "/usr/lib/python3.10/reprlib.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/sre_compile.py",
      "final": "/usr/lib/python3.10/sre_compile.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/sre_constants.py",
      "final": "/usr/lib/python3.10/sre_constants.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/sre_parse.py",
      "final": "/usr/lib/python3.10/sre_parse.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/stat.py",
      "final": "/usr/lib/python3.10/stat.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/types.py",
      "final": "/usr/lib/python3.10/types.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python3.10/warnings.py",
      "final": "/usr/lib/python3.10/warnings.py",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "source_or_matching_source"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/python310.zip",
      "final": "/usr/lib/python310.zip",
      "links": [],
      "optional": True,
      "absence_required": True,
      "earliest_phase": "early",
      "roles": [
        "startup_zip_must_be_absent"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2",
      "final": "/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/x86_64-linux-gnu/libc.so.6",
      "final": "/usr/lib/x86_64-linux-gnu/libc.so.6",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/x86_64-linux-gnu/libcrypto.so.3",
      "final": "/usr/lib/x86_64-linux-gnu/libcrypto.so.3",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "helper",
      "roles": [
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/x86_64-linux-gnu/libexpat.so.1.8.7",
      "final": "/usr/lib/x86_64-linux-gnu/libexpat.so.1.8.7",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/x86_64-linux-gnu/libm.so.6",
      "final": "/usr/lib/x86_64-linux-gnu/libm.so.6",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    },
    {
      "lexical": "/usr/lib/x86_64-linux-gnu/libz.so.1.2.11",
      "final": "/usr/lib/x86_64-linux-gnu/libz.so.1.2.11",
      "links": [],
      "optional": True,
      "absence_required": False,
      "earliest_phase": "early",
      "roles": [
        "mapped_file"
      ],
      "observed_presence": None,
      "observed_key": None
    }
  ],
  "bounds": {
    "modules": 62,
    "maps_bytes": 65536,
    "files": 69,
    "file_bytes": 8388608,
    "total_bytes": 67108864,
    "scalar_chars": 1024,
    "sequence_items": 128,
    "link_hops": 1,
    "stdout_bytes": 16777216
  }
}
if BINDING is None:
    raise SystemExit("P213_OBSERVER_DISABLED_UNRESOLVED_BINDING")

import sys

MISSING = object()
OWNED_FAILURE = object()
FIELDS = ("st_dev", "st_ino", "st_mode", "st_nlink", "st_uid", "st_gid",
          "st_rdev", "st_size", "st_mtime_ns", "st_ctime_ns")
EARLY = []
SNAPSHOTS = []
FILES = []
USED_BYTES = 0
# FAILURE_CODES is the reviewed finite vocabulary; no runtime exception args enter it.
FAILURE_CODES = (
    "absence_binding_boolean",
    "absence_must_be_optional",
    "absolute_path",
    "builtin_filename_policy",
    "child_environment_mismatch",
    "closing_environment_mismatch",
    "closing_file_or_absence_changed",
    "closing_launch_change",
    "closing_removed_or_changed_module",
    "complete_flag_binding",
    "cwd_binding",
    "deleted_mapping",
    "direct_script_fields",
    "direct_script_spec",
    "early_map_path",
    "early_module_path",
    "exe_binding",
    "exe_file_identity",
    "exe_key_required",
    "extension_cache_policy",
    "file_binding_unique",
    "file_count_bound",
    "file_map_inode",
    "file_module_origin_policy",
    "file_phase_binding",
    "file_read_bound",
    "file_size_bound",
    "filesystem_encoding_policy",
    "flag_binding_names",
    "flag_policy_mismatch",
    "flag_record_names",
    "frozen_nominal_filename",
    "helper_launch_change",
    "helper_removed_or_changed_module",
    "implementation_bound",
    "implementation_name_bound",
    "implementation_policy_mismatch",
    "incomplete_file",
    "interpreter_key_required",
    "invalid_bound",
    "invalid_internal_code",
    "invalid_module_entry",
    "late_unkeyed_map",
    "late_unkeyed_module",
    "launch_policy_mismatch",
    "launch_text_bound",
    "lexical_path_form",
    "map_address_order",
    "map_field_count",
    "map_file_identity",
    "map_hex",
    "map_inode_decimal",
    "map_numeric_shape",
    "map_permissions",
    "maps_bound",
    "maps_incomplete",
    "mechanism_binding",
    "module_binding_bound",
    "module_bound",
    "module_membership_policy",
    "module_name_binding",
    "module_name_bound",
    "module_role_allowlist",
    "new_map_path",
    "no_leaf_link_binding",
    "nonfile_module_policy",
    "noninteger_stat",
    "nonpackage_path_policy",
    "nonregular_fd",
    "nonregular_path",
    "observer_key_required",
    "package_path_policy",
    "path_alias_facts",
    "path_bound",
    "path_changed_during_read",
    "path_fd_before",
    "postclosing_module_change",
    "prehelper_change",
    "process_changed_during_keys",
    "process_points_changed",
    "required_absence_not_observed",
    "required_module_missing",
    "same_fd_changed",
    "scalar_bound",
    "sequence_bound",
    "short_stdout_write",
    "source_cache_policy",
    "stdout_bound",
    "stream_encoding_policy",
    "total_read_bound",
    "unknown_module_name",
    "unknown_module_spec",
    "unsupported_module_loader",
    "unsupported_module_mechanism",
    "unsupported_path_encoding",
    "unsupported_scalar_type",
    "unsupported_spec_loader",
    "unsupported_special_map",
    "zip_absence_binding",
)

class ObserverFailure(Exception):
    __slots__ = ("owner", "code")

    def __init__(self, code):
        self.owner = OWNED_FAILURE
        self.code = code if type(code) is str and code in FAILURE_CODES else "invalid_internal_code"


def need(condition, code):
    if not condition:
        raise ObserverFailure(code)


ERRNO_TYPES = (OSError, BlockingIOError, ChildProcessError, ConnectionError,
               BrokenPipeError, ConnectionAbortedError, ConnectionRefusedError,
               ConnectionResetError, FileExistsError, FileNotFoundError,
               InterruptedError, IsADirectoryError, NotADirectoryError,
               PermissionError, ProcessLookupError, TimeoutError)
ERROR_CLASSES = (
    (ObserverFailure, "observer.owned_failure"),
    (RuntimeError, "builtins.RuntimeError"), (ValueError, "builtins.ValueError"),
    (TypeError, "builtins.TypeError"), (KeyError, "builtins.KeyError"),
    (IndexError, "builtins.IndexError"), (AttributeError, "builtins.AttributeError"),
    (ImportError, "builtins.ImportError"), (ModuleNotFoundError, "builtins.ModuleNotFoundError"),
    (MemoryError, "builtins.MemoryError"), (OverflowError, "builtins.OverflowError"),
    (UnicodeError, "builtins.UnicodeError"), (UnicodeDecodeError, "builtins.UnicodeDecodeError"),
    (UnicodeEncodeError, "builtins.UnicodeEncodeError"),
    (UnicodeTranslateError, "builtins.UnicodeTranslateError"),
    (AssertionError, "builtins.AssertionError"), (SystemError, "builtins.SystemError"),
    (KeyboardInterrupt, "builtins.KeyboardInterrupt"), (SystemExit, "builtins.SystemExit"),
    (OSError, "builtins.OSError"), (BlockingIOError, "builtins.BlockingIOError"),
    (ChildProcessError, "builtins.ChildProcessError"), (ConnectionError, "builtins.ConnectionError"),
    (BrokenPipeError, "builtins.BrokenPipeError"),
    (ConnectionAbortedError, "builtins.ConnectionAbortedError"),
    (ConnectionRefusedError, "builtins.ConnectionRefusedError"),
    (ConnectionResetError, "builtins.ConnectionResetError"),
    (FileExistsError, "builtins.FileExistsError"), (FileNotFoundError, "builtins.FileNotFoundError"),
    (InterruptedError, "builtins.InterruptedError"), (IsADirectoryError, "builtins.IsADirectoryError"),
    (NotADirectoryError, "builtins.NotADirectoryError"), (PermissionError, "builtins.PermissionError"),
    (ProcessLookupError, "builtins.ProcessLookupError"), (TimeoutError, "builtins.TimeoutError"),
)


def failure(exc):
    # Fixed labels only. Never read args, arbitrary class metadata or exception text.
    kind = type(exc)
    label = next((name for cls, name in ERROR_CLASSES if kind is cls), "other_exception")
    code = "operation_failed"
    if (kind is ObserverFailure and exc.owner is OWNED_FAILURE
            and type(exc.code) is str and exc.code in FAILURE_CODES):
        code = exc.code
    value = exc.errno if kind in ERRNO_TYPES else None
    return {"class": label, "errno": value if type(value) is int else None, "code": code}


def same_tree(left, right):
    # Do not collapse bool and int facts through Python's ordinary scalar equality.
    if type(left) is not type(right):
        return False
    if type(left) in (tuple, list):
        return len(left) == len(right) and all(same_tree(a, b) for a, b in zip(left, right))
    if type(left) is dict:
        return left.keys() == right.keys() and all(same_tree(left[k], right[k]) for k in left)
    return left == right


def tuple_tree(value):
    if type(value) in (tuple, list):
        return tuple(tuple_tree(x) for x in value)
    return value


def frozen(value):
    if value is MISSING:
        return ("missing",)
    if value is None:
        return ("null",)
    if type(value) in (str, int, bool):
        if type(value) is str:
            need(len(value) <= BINDING["bounds"]["scalar_chars"], "scalar_bound")
        return ("value", value)
    if isinstance(value, tuple) or type(value) is list:
        need(len(value) <= BINDING["bounds"]["sequence_items"], "sequence_bound")
        return ("sequence", tuple(frozen(x) for x in value))
    raise ObserverFailure("unsupported_scalar_type")


def attribute(obj, name):
    return frozen(getattr(obj, name, MISSING))


def loader_id(loader):
    if loader is MISSING or loader is None:
        return frozen(loader)
    is_class = isinstance(loader, type)
    kind = loader if is_class else type(loader)
    return ("class" if is_class else "instance",
            attribute(kind, "__module__"), attribute(kind, "__qualname__"))


def module_snapshot(phase):
    record = {"phase": phase, "rows": [], "complete": False}
    SNAPSHOTS.append(record)
    registry = tuple(sys.modules.copy().items())
    need(len(registry) <= BINDING["bounds"]["modules"], "module_bound")
    result = []
    for name, module in sorted(registry):
        need(type(name) is str and module is not None, "invalid_module_entry")
        spec = getattr(module, "__spec__", MISSING)
        spec_data = frozen(spec) if spec is MISSING or spec is None else (
            "spec", attribute(spec, "origin"),
            loader_id(getattr(spec, "loader", MISSING)),
            attribute(spec, "has_location"),
            attribute(spec, "submodule_search_locations"))
        result.append((name, True, name in sys.builtin_module_names, spec_data,
                       loader_id(getattr(module, "__loader__", MISSING)),
                       attribute(module, "__file__"), attribute(module, "__cached__"),
                       attribute(module, "__path__")))
        record["rows"] = tuple(result)
    record["complete"] = True
    return tuple(result)


def launch_snapshot():
    names = ("executable", "orig_argv", "argv", "version", "version_info",
             "path", "prefix", "base_prefix", "exec_prefix", "base_exec_prefix",
             "dont_write_bytecode", "pycache_prefix", "platform", "byteorder",
             "abiflags", "hexversion", "maxsize", "builtin_module_names")
    flags = tuple((n, attribute(sys.flags, n)) for n in BINDING["flag_names"])
    members = tuple(sorted(vars(sys.implementation).items()))
    need(len(members) <= BINDING["bounds"]["sequence_items"], "implementation_bound")
    implementation = tuple((n, frozen(v)) for n, v in members)
    need(all(type(n) is str and len(n) <= BINDING["bounds"]["scalar_chars"]
             for n, v in implementation), "implementation_name_bound")
    streams = tuple((n, attribute(getattr(sys, n), "encoding"),
                     attribute(getattr(sys, n), "errors")) for n in ("stdout", "stderr"))
    flag_text = str(sys.flags)
    fs_encoding = sys.getfilesystemencoding()
    fs_errors = sys.getfilesystemencodeerrors()
    for text in (flag_text, fs_encoding, fs_errors):
        need(type(text) is str and len(text) <= BINDING["bounds"]["scalar_chars"], "launch_text_bound")
    return (tuple((n, attribute(sys, n)) for n in names), flags, flag_text,
            implementation, streams, fs_encoding, fs_errors)


def path_ok(path):
    # Pure lexical checks: usable before os/path helper imports and no traversal.
    need(type(path) is str and path.startswith("/") and path != "/", "absolute_path")
    need(len(path) <= BINDING["bounds"]["scalar_chars"], "path_bound")
    need(all(32 <= ord(c) <= 126 and c != "\\" for c in path), "unsupported_path_encoding")
    need(all(part not in ("", ".", "..") for part in path.split("/")[1:]), "lexical_path_form")


def launch_allowed(record):
    values, flags, flag_text, implementation, streams, fs_encoding, fs_errors = record
    actual = dict(values)
    policy = BINDING["launch_policy"]
    expected = {
        "executable": BINDING["interpreter"]["lexical"],
        "orig_argv": policy["orig_argv"], "argv": policy["argv"],
        "version_info": policy["release"], "path": policy["sys_path"],
        "prefix": policy["prefixes_must_equal"], "base_prefix": policy["prefixes_must_equal"],
        "exec_prefix": policy["prefixes_must_equal"], "base_exec_prefix": policy["prefixes_must_equal"],
        "dont_write_bytecode": policy["dont_write_bytecode"],
        "pycache_prefix": policy["pycache_prefix"], "platform": policy["platform"],
    }
    for name, value in expected.items():
        need(same_tree(actual[name], frozen(value)), "launch_policy_mismatch")
    need(tuple(name for name, value in flags) == tuple(BINDING["flag_names"]), "flag_record_names")
    for name, value in flags:
        need(same_tree(value, frozen(policy["flag_requirements"][name])), "flag_policy_mismatch")
    impl = dict(implementation)
    need(same_tree(impl.get("name"), frozen(policy["implementation"]))
         and same_tree(impl.get("cache_tag"), frozen(policy["cache_tag"]))
         and same_tree(impl.get("version"), frozen(policy["release"])), "implementation_policy_mismatch")
    need(fs_encoding in policy["encodings_allowed"]
         and fs_errors == policy["filesystem_errors"], "filesystem_encoding_policy")
    for name, encoding, errors in streams:
        need(any(same_tree(encoding, frozen(x)) for x in policy["encodings_allowed"])
             and same_tree(errors, frozen(policy[name + "_errors"])), "stream_encoding_policy")
    # Remaining actual fields, full flag text and all implementation members stay
    # immutable, bounded and cross-phase compared; they are not fabricated expectations.


def binding_entries():
    for limit in BINDING["bounds"].values():
        need(type(limit) is int and limit > 0, "invalid_bound")
    need(BINDING["launch_policy"]["flag_names"] == BINDING["flag_names"], "flag_binding_names")
    need(set(BINDING["flag_names"]) == set(BINDING["launch_policy"]["flag_requirements"])
         and len(BINDING["flag_names"]) == 17, "complete_flag_binding")
    need(len(BINDING["files"]) <= BINDING["bounds"]["files"], "file_count_bound")
    entries = {}
    for entry in BINDING["files"]:
        path_ok(entry["lexical"])
        path_ok(entry["final"])
        need(entry["lexical"] not in entries and type(entry["optional"]) is bool, "file_binding_unique")
        need(type(entry["absence_required"]) is bool, "absence_binding_boolean")
        need(entry["links"] == [] and entry["final"] == entry["lexical"], "no_leaf_link_binding")
        need(entry["earliest_phase"] in ("early", "helper"), "file_phase_binding")
        need(not entry["absence_required"] or entry["optional"], "absence_must_be_optional")
        need(entry["absence_required"] == ("startup_zip_must_be_absent" in entry["roles"]),
             "zip_absence_binding")
        entries[entry["lexical"]] = entry
    path_ok(BINDING["cwd"])
    need(BINDING["observer"] in entries and not entries[BINDING["observer"]]["optional"], "observer_key_required")
    interpreter = BINDING["interpreter"]
    need(interpreter["lexical"] in entries and not entries[interpreter["lexical"]]["optional"]
         and same_tree(interpreter, entries[interpreter["lexical"]]), "interpreter_key_required")
    need(len(BINDING["modules"]) <= BINDING["bounds"]["modules"], "module_binding_bound")
    for phase in ("early", "helper", "closing"):
        allowed = BINDING["module_names"][phase]
        required = BINDING["required_module_names"][phase]
        need(len(set(allowed)) == len(allowed) and set(allowed) <= BINDING["modules"].keys()
             and set(required) <= set(allowed), "module_name_binding")
    for name, policy in BINDING["modules"].items():
        need(type(name) is str and len(name) <= BINDING["bounds"]["scalar_chars"], "module_name_bound")
        need(policy["mechanism"] in BINDING["loader_ids"], "mechanism_binding")
        for role in policy["file_roles"]:
            path_ok(role["path"])
            need(role["path"] in entries and role["role"] in entries[role["path"]]["roles"]
                 and type(role["content_required"]) is bool, "module_role_allowlist")
    return entries


def module_delta(before, after):
    left = {row[0]: row for row in before}
    right = {row[0]: row for row in after}
    return {"added": sorted(right.keys() - left.keys()), "removed": sorted(left.keys() - right.keys()),
            "changed": sorted(name for name in left.keys() & right.keys()
                              if not same_tree(left[name], right[name]))}


def mapped_paths(record):
    return {row["path"] for row in record["parsed"] if row["path"].startswith("/")}


def missing_or_null(value):
    return value in (("missing",), ("null",))


def module_roles(snapshot, phase, entries, keyed=None):
    roles = []
    names = {row[0] for row in snapshot}
    need(names <= set(BINDING["module_names"][phase]), "unknown_module_name")
    need(set(BINDING["required_module_names"][phase]) <= names, "required_module_missing")
    for row in snapshot:
        name, present, builtin, spec, loader, filename, cached, search = row
        policy = BINDING["modules"][name]
        mechanism = policy["mechanism"]
        expected_loader = tuple_tree(BINDING["loader_ids"][mechanism])
        need(present is True and builtin is (mechanism == "builtin"), "module_membership_policy")
        need(same_tree(loader, expected_loader), "unsupported_module_loader")
        if mechanism == "direct_script":
            need(name == "__main__" and spec == ("null",), "direct_script_spec")
            need(same_tree(filename, frozen(BINDING["observer"]))
                 and cached == ("null",) and missing_or_null(search), "direct_script_fields")
        else:
            need(type(spec) is tuple and len(spec) == 5 and spec[0] == "spec", "unknown_module_spec")
            need(same_tree(spec[2], expected_loader), "unsupported_spec_loader")
            if mechanism in ("builtin", "frozen"):
                need(same_tree(spec[1], frozen("built-in" if mechanism == "builtin" else "frozen"))
                     and same_tree(spec[3], frozen(False))
                     and spec[4] == ("null",) and missing_or_null(search)
                     and missing_or_null(cached), "nonfile_module_policy")
                if mechanism == "builtin":
                    need(missing_or_null(filename), "builtin_filename_policy")
                else:
                    need(missing_or_null(filename) or same_tree(filename, frozen(policy["nominal_file"])),
                         "frozen_nominal_filename")
            elif mechanism in ("source_file", "extension_file"):
                need(same_tree(spec[1], frozen(policy["origin"]))
                     and same_tree(filename, frozen(policy["file"]))
                     and same_tree(spec[3], frozen(True)), "file_module_origin_policy")
                if mechanism == "source_file":
                    need(same_tree(cached, frozen(policy["cache"])), "source_cache_policy")
                else:
                    need(missing_or_null(cached), "extension_cache_policy")
                if policy["package_path"] is None:
                    need(spec[4] == ("null",) and missing_or_null(search), "nonpackage_path_policy")
                else:
                    need(same_tree(spec[4], frozen([policy["package_path"]]))
                         and same_tree(search, frozen([policy["package_path"]])), "package_path_policy")
            else:
                raise ObserverFailure("unsupported_module_mechanism")
        for role in policy["file_roles"]:
            path = role["path"]
            need(path in entries and role["role"] in entries[path]["roles"], "module_role_allowlist")
            need(phase != "early" or entries[path]["earliest_phase"] == "early", "early_module_path")
            if keyed is not None:
                need(path in keyed and (keyed[path]["complete"] or (not role["content_required"]
                     and entries[path]["optional"] and keyed[path].get("absent") is True)),
                     "late_unkeyed_module")
            roles.append({"phase": phase, "module": name, "mechanism": mechanism,
                          "path": path, "role": role["role"]})
    rows = {row[0]: row for row in snapshot}
    if "os.path" in rows and "posixpath" in rows:
        need(same_tree(rows["os.path"][1:], rows["posixpath"][1:]), "path_alias_facts")
    return roles


def raw_maps(phase):
    record = {"phase": phase, "raw_hex": "", "byte_count": 0, "eof": False}
    EARLY.append(record)
    chunks = []
    limit = BINDING["bounds"]["maps_bytes"]
    try:
        with open("/proc/self/maps", "rb", buffering=0) as stream:
            while True:
                block = stream.read(min(65536, limit + 1 - record["byte_count"]))
                if not block:
                    record["eof"] = True
                    break
                chunks.append(block)
                record["byte_count"] += len(block)
                need(record["byte_count"] <= limit, "maps_bound")
    finally:
        record["raw_hex"] = b"".join(chunks).hex()
    return record


def map_roles(record, phase, entries, keyed=None):
    raw = bytes.fromhex(record["raw_hex"])
    need(record["eof"] and len(raw) == record["byte_count"] and raw.endswith(b"\n"), "maps_incomplete")
    parsed = []
    record["parsed"] = parsed
    for line in raw.splitlines():
        fields = line.split(None, 5)
        need(len(fields) in (5, 6), "map_field_count")
        interval, permissions, offset, device, inode = (x.decode("ascii") for x in fields[:5])
        addresses = interval.split("-")
        dev = device.split(":")
        need(len(addresses) == 2 and len(dev) == 2, "map_numeric_shape")
        need(all(x and all(c in "0123456789abcdefABCDEF" for c in x)
                 for x in addresses + dev + [offset]), "map_hex")
        need(inode.isascii() and inode.isdecimal(), "map_inode_decimal")
        need(len(permissions) == 4 and permissions[0] in "r-" and permissions[1] in "w-"
             and permissions[2] in "x-" and permissions[3] in "ps", "map_permissions")
        path = fields[5].decode("ascii") if len(fields) == 6 else ""
        item = {"start": int(addresses[0], 16), "end": int(addresses[1], 16),
                "perms": permissions, "offset": int(offset, 16),
                "device": [int(x, 16) for x in dev], "inode": int(inode), "path": path,
                "phase": phase}
        parsed.append(item)
        need(item["start"] < item["end"], "map_address_order")
        need(not path.endswith(" (deleted)"), "deleted_mapping")
        if path.startswith("/"):
            path_ok(path)
            need(path in entries and "mapped_file" in entries[path]["roles"], "new_map_path")
            need(phase != "early" or entries[path]["earliest_phase"] == "early", "early_map_path")
            need(item["inode"] > 0, "file_map_inode")
            if keyed is not None:
                need(keyed[path]["complete"], "late_unkeyed_map")
                stat = keyed[path]["fd_before"]
                need([os.major(stat["st_dev"]), os.minor(stat["st_dev"])] == item["device"]
                     and stat["st_ino"] == item["inode"], "map_file_identity")
        else:
            need(path in BINDING["special_maps"] and item["inode"] == 0
                 and item["device"] == [0, 0], "unsupported_special_map")
    return parsed


try:
    ENTRIES = binding_entries()
    EARLY_MODULES = module_snapshot("early")
    EARLY_LAUNCH = launch_snapshot()
    EARLY_ROLES = module_roles(EARLY_MODULES, "early", ENTRIES)
    launch_allowed(EARLY_LAUNCH)
    # Unknown copied rows/launch invariants HOLD before further explicit access.
    EARLY_MAPS = raw_maps("early_pre_helpers")
    map_roles(EARLY_MAPS, "early", ENTRIES)
    SECOND_MODULES = module_snapshot("second_prehelper")
    SECOND_LAUNCH = launch_snapshot()
    module_roles(SECOND_MODULES, "early", ENTRIES)
    launch_allowed(SECOND_LAUNCH)
    need(same_tree(EARLY_MODULES, SECOND_MODULES) and same_tree(EARLY_LAUNCH, SECOND_LAUNCH),
         "prehelper_change")
except BaseException as exc:
    # This failed ASCII envelope is not JSON PASS. No serializer is imported.
    sys.stdout.write(ascii({"status": "HOLD_PREHELPER", "failure": failure(exc),
                           "early_modules": globals().get("EARLY_MODULES"),
                           "early_launch": globals().get("EARLY_LAUNCH"),
                           "second_modules": globals().get("SECOND_MODULES"),
                           "second_launch": globals().get("SECOND_LAUNCH"),
                           "module_snapshots": SNAPSHOTS, "maps": EARLY}) + "\n")
    raise SystemExit(78)

try:
    import os
    import hashlib
    import json
except BaseException as exc:
    sys.stdout.write(ascii({"status": "HOLD_HELPER_IMPORT", "failure": failure(exc),
                           "early_modules": EARLY_MODULES, "early_launch": EARLY_LAUNCH,
                           "second_modules": SECOND_MODULES, "second_launch": SECOND_LAUNCH,
                           "module_snapshots": SNAPSHOTS, "maps": EARLY}) + "\n")
    raise SystemExit(78)


def canonical(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def full_stat(value):
    result = {name: getattr(value, name) for name in FIELDS}
    need(all(type(v) is int for v in result.values()), "noninteger_stat")
    return result


def points(entry, result):
    # The finite policy has no leaf aliases; trusted ancestors are not scanned.
    result.update({"lexical": entry["lexical"], "links": [], "absence": None})
    first = entry["lexical"]
    need(entry["links"] == [] and first == entry["final"], "no_leaf_link_binding")
    try:
        result["final_lstat"] = full_stat(os.lstat(first))
    except OSError as exc:
        # Only actual ENOENT, never ENOTDIR/permissions/dangling-link success.
        if exc.errno == 2 and entry["optional"]:
            result["absence"] = {"operation": "lstat", "path": first, "errno": 2}
            return result
        raise
    need(not entry["absence_required"], "required_absence_not_observed")
    need(result["final_lstat"]["st_mode"] & 0o170000 == 0o100000, "nonregular_path")
    return result


def key_file(entry):
    global USED_BYTES
    record = {"lexical": entry["lexical"], "roles": entry["roles"],
              "byte_count": 0, "eof": False, "complete": False}
    FILES.append(record)
    fd = None
    digest = hashlib.sha256()
    try:
        record["begin"] = {}
        points(entry, record["begin"])
        if record["begin"]["absence"] is not None:
            record["absent"] = True
            return record
        fd = os.open(entry["final"], os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC)
        record["fd_before"] = full_stat(os.fstat(fd))
        need(record["fd_before"]["st_mode"] & 0o170000 == 0o100000, "nonregular_fd")
        need(record["fd_before"] == record["begin"]["final_lstat"], "path_fd_before")
        limit = BINDING["bounds"]["file_bytes"]
        need(0 <= record["fd_before"]["st_size"] <= limit, "file_size_bound")
        while True:
            block = os.read(fd, min(65536, limit + 1 - record["byte_count"],
                                   BINDING["bounds"]["total_bytes"] + 1 - USED_BYTES))
            if not block:
                record["eof"] = True
                break
            digest.update(block)
            record["byte_count"] += len(block)
            USED_BYTES += len(block)
            need(record["byte_count"] <= limit, "file_read_bound")
            need(USED_BYTES <= BINDING["bounds"]["total_bytes"], "total_read_bound")
        record["fd_after"] = full_stat(os.fstat(fd))
        record["after_read"] = {}
        points(entry, record["after_read"])
        need(record["fd_before"] == record["fd_after"], "same_fd_changed")
        need(record["begin"] == record["after_read"], "path_changed_during_read")
        need(record["byte_count"] == record["fd_before"]["st_size"], "incomplete_file")
        record["complete"] = True
        return record
    except BaseException as exc:
        record["failure"] = failure(exc)
        raise
    finally:
        record["sha256_of_read_bytes"] = digest.hexdigest()
        if fd is not None:
            try:
                os.close(fd)
            except BaseException as exc:
                record["complete"] = False
                record["close_failure"] = failure(exc)
                raise


def process_points(keyed, record):
    record["cwd"] = os.getcwd()
    record["proc_cwd"] = os.readlink("/proc/self/cwd")
    record["proc_exe"] = os.readlink("/proc/self/exe")
    need(record["cwd"] == record["proc_cwd"] == BINDING["cwd"], "cwd_binding")
    entry = BINDING["interpreter"]
    need(record["proc_exe"] == entry["final"], "exe_binding")
    # F01: do not follow proc-exe metadata until both path/cwd checks have passed.
    record["exe_stat"] = full_stat(os.stat("/proc/self/exe"))
    if keyed is not None:
        need(keyed[entry["lexical"]]["complete"], "exe_key_required")
        need(record["exe_stat"] == keyed[entry["lexical"]]["fd_before"], "exe_file_identity")
    return record


RESULT = {"schema": "P213_FINITE_PERMISSION_OBSERVER_V2", "status": "HOLD", "binding_id": BINDING["id"],
          "early_modules": EARLY_MODULES, "early_launch": EARLY_LAUNCH,
          "second_modules": SECOND_MODULES, "second_launch": SECOND_LAUNCH,
          "module_snapshots": SNAPSHOTS, "maps": EARLY, "files": FILES, "runtime_accepted": False}
try:
    entries = ENTRIES
    RESULT["early_roles"] = EARLY_ROLES
    helper_modules = module_snapshot("helper")
    RESULT["helper_modules"] = helper_modules
    RESULT["helper_launch"] = launch_snapshot()
    RESULT["helper_roles"] = module_roles(helper_modules, "helper", entries)
    launch_allowed(RESULT["helper_launch"])
    RESULT["helper_module_delta"] = module_delta(EARLY_MODULES, helper_modules)
    need(not RESULT["helper_module_delta"]["removed"] and not RESULT["helper_module_delta"]["changed"],
         "helper_removed_or_changed_module")
    need(same_tree(RESULT["helper_launch"], EARLY_LAUNCH), "helper_launch_change")
    # Trusted helper imports are not sandboxed; the checks above precede further
    # explicit proc/path access. No helper-added row is relabelled as startup.
    helper_maps = raw_maps("helper")
    map_roles(helper_maps, "helper", entries)
    RESULT["helper_observed_map_additions"] = sorted(mapped_paths(helper_maps) - mapped_paths(EARLY_MAPS))
    # Python-level cached mapping only; no reload, dump, or unexpected names/values.
    RESULT["environment"] = {"scope": "os.environ_cached_mapping", "expected": {"LANG": "C", "LC_ALL": "C"}}
    RESULT["environment"]["matches"] = dict(os.environ) == {"LANG": "C", "LC_ALL": "C"}
    need(RESULT["environment"]["matches"], "child_environment_mismatch")
    RESULT["process_begin"] = {}
    process_points(None, RESULT["process_begin"])
    # One fixed finite pass, including preapproved optional late candidates.
    keyed = {entry["lexical"]: key_file(entry) for entry in BINDING["files"]}
    RESULT["process_after_keys"] = {}
    process_points(keyed, RESULT["process_after_keys"])
    need(same_tree(RESULT["process_begin"], RESULT["process_after_keys"]), "process_changed_during_keys")
    map_roles(EARLY_MAPS, "early", entries, keyed)
    map_roles(helper_maps, "helper", entries, keyed)
    module_roles(EARLY_MODULES, "early", entries, keyed)
    module_roles(helper_modules, "helper", entries, keyed)
    closing_modules = module_snapshot("closing")
    RESULT["closing_modules"] = closing_modules
    RESULT["closing_launch"] = launch_snapshot()
    RESULT["closing_module_delta"] = module_delta(helper_modules, closing_modules)
    need(not RESULT["closing_module_delta"]["removed"] and not RESULT["closing_module_delta"]["changed"],
         "closing_removed_or_changed_module")
    RESULT["closing_roles"] = module_roles(closing_modules, "closing", entries, keyed)
    launch_allowed(RESULT["closing_launch"])
    need(same_tree(RESULT["closing_launch"], EARLY_LAUNCH), "closing_launch_change")
    # No key_file calls below this closing boundary.
    closing_maps = raw_maps("closing")
    map_roles(closing_maps, "closing", entries, keyed)
    RESULT["closing_observed_map_additions"] = sorted(mapped_paths(closing_maps) - mapped_paths(helper_maps))
    RESULT["process_closing"] = {}
    process_points(keyed, RESULT["process_closing"])
    need(same_tree(RESULT["process_after_keys"], RESULT["process_closing"]), "process_points_changed")
    for entry in BINDING["files"]:
        record = keyed[entry["lexical"]]
        record["closing"] = {}
        points(entry, record["closing"])
        need(same_tree(record["closing"], record["begin"]), "closing_file_or_absence_changed")
    RESULT["environment"]["closing_matches"] = dict(os.environ) == {"LANG": "C", "LC_ALL": "C"}
    need(RESULT["environment"]["closing_matches"], "closing_environment_mismatch")
    need(same_tree(module_snapshot("postclosing_check"), closing_modules), "postclosing_module_change")
    RESULT["total_file_read_bytes"] = USED_BYTES
    RESULT["status"] = "OBSERVED_PENDING_INDEPENDENT_RECEPTION"
except BaseException as exc:
    RESULT["failure"] = failure(exc)

try:
    output = (canonical(RESULT) + "\n").encode("ascii")
    need(len(output) <= BINDING["bounds"]["stdout_bytes"], "stdout_bound")
    written = sys.stdout.buffer.write(output)
    need(written == len(output), "short_stdout_write")
    sys.stdout.buffer.flush()
except BaseException:
    # Preserve actual capture; serialization/transport can leave no complete receipt.
    raise SystemExit(79)
raise SystemExit(0 if RESULT["status"] == "OBSERVED_PENDING_INDEPENDENT_RECEPTION" else 78)
