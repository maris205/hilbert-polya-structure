#!/usr/bin/env python3
"""HCS-C61 independent resolver producer for G3--G6.

This file is the sole producer-side mathematical implementation for the C61
resolver component.  It reads released P60/C59/C60 authority and the frozen
C61 target/formal inputs, but it never reads a target-selection pilot.  The
output is one canonical ``c61_resolvent_evidence.json`` document.  A separate
``c61_checker_resolvent.py`` process is invoked twice before final output; no
producer theorem helper is imported by that checker.

Lifecycle: COMPONENT_PASS candidate only / PAPER_PENDING / NOT_RELEASED.
Scope: NO_BAD_EULER_OR_ROOT_NUMBER.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import time
from typing import Any, Iterable, Iterator, Sequence


sys.dont_write_bytecode = True

P = 692717
DEGREE = 27
IDENTITY = tuple(range(DEGREE))
RELEASE_COMMIT = "fe1217810b72840619efdf40a2af31b8b80d96f6"
RELEASE_PARENT = "f3b3726c40519cdd8ac7832f9f22df16d451b890"
RELEASE_TREE = "22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a"
FORMAL13_SHA256 = "c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28"
FORMAL_ROUTE_SHA256 = "c773812c949bc4197b4ad5e9e2076ddd5a5d4594d5fb8884ba7109812c3fb40b"
FORMAL_BATCH_SHA256 = "13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814"
FORMAL15_SHA256 = "61984f2a06fcd8f57c50ec28e1a557107e551fa0e2b82edc936321507ead37b5"
FORMAL15_COUNT = 15
FORMAL15_BYTES = 199565
FORMAL15_LINES = 5094

C60_ROOT = Path("henon_dynamics/henon_mu3_yukawa_biquadratic_envelope")
C59_ROOT = Path("henon_dynamics/henon_mu3_yukawa_gassmann_twins")
C60_PINS = {
    "certificate": (C60_ROOT / "results/c60_certificate.json", "d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518"),
    "group_evidence": (C60_ROOT / "results/c60_group_evidence.json", "dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2"),
    "resolvent_evidence": (C60_ROOT / "results/c60_resolvent_evidence.json", "f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da"),
    "group_module": (C60_ROOT / "code/c60_group.py", "fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b"),
    "schema": (C60_ROOT / "results/c60_schema.json", "c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5"),
    "check_report": (C60_ROOT / "results/c60_check_report.json", "25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44"),
    "scoped_manifest": (C60_ROOT / "results/scoped_hash_manifest.json", "f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7"),
    "full_manifest": (C60_ROOT / "FULL_PROJECT_HASHES.sha256", "37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4"),
    "route": (C60_ROOT / "route_a_evaluation.yaml", "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872"),
    "route_archive": (C60_ROOT / "evaluations/route_a/HCS-C60/20260817T000000Z.yaml", "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872"),
}
TARGET_GUARD_REL = Path("henon_dynamics/codex_prompt.md")
TARGET_GUARD_SHA256 = "24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead"
C59_RESOLVENT_REL = C59_ROOT / "results/c59_resolvent_evidence.json"
C59_RESOLVENT_SHA256 = "667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6"
C60_PAYLOAD_SHA256 = "dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead"
FROZEN_ARRAYS_SHA256 = "0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5"
LAMBDA_SHA256 = "fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5"

FORMAL_MD = [
    "DERIVATION.md", "EXPERIMENT_PLAN.md", "EXPERIMENT_TRACKER.md",
    "IMPLEMENTATION_CHECKLIST.md", "INTEGRITY_REPORT.md",
    "METHODOLOGY_BLUEPRINT.md", "NARRATIVE_REPORT.md", "PAPER_PLAN.md",
    "PROOF_PACKAGE.md", "README.md", "RESEARCH_QUESTION.md",
    "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
]
PROJECT_BASENAME = "henon_mu3_yukawa_tensor_fourier_descent"
EVIDENCE_BASENAME = "c61_resolvent_evidence.json"
STAGE_PATTERN = re.compile(r"^\.c61-stage-[A-Za-z0-9]{8}$")

QUOTIENT_REPS_ONE = {
    "1": list(range(1, 28)),
    "Hplus": [1,18,12,5,4,15,7,11,25,26,8,3,14,13,6,21,20,2,22,17,16,19,23,27,9,10,24],
    "H0": [1,14,4,6,12,17,8,27,25,10,7,16,18,2,5,22,19,13,21,15,3,20,24,11,9,26,23],
    "H3": [1,13,5,15,3,20,11,24,9,26,7,21,2,18,4,19,22,14,16,6,12,17,27,8,25,10,23],
}

SPLUS_GENS_ONE = [
    [1,2,3,5,4,6,7,8,10,9,11,12,14,13,15,17,16,18,19,21,20,22,23,24,26,25,27],
    [1,2,3,20,21,19,24,23,10,9,11,22,14,13,15,17,16,18,6,4,5,12,8,7,26,25,27],
    [1,2,6,4,5,3,7,11,9,10,8,15,13,14,12,20,21,18,19,16,17,22,23,27,25,26,24],
    [1,18,12,4,5,15,7,11,26,25,8,3,13,14,6,20,21,2,22,16,17,19,23,27,10,9,24],
    [2,1,3,4,5,6,7,12,13,14,15,8,9,10,11,16,17,18,19,20,21,23,22,24,25,26,27],
    [3,6,4,1,2,5,18,16,8,12,17,20,11,15,21,9,13,19,7,10,14,24,27,25,22,23,26],
]
TPLUS_GENS_ONE = [
    SPLUS_GENS_ONE[0], SPLUS_GENS_ONE[1], SPLUS_GENS_ONE[2],
    [1,13,5,3,15,20,11,24,26,9,7,21,18,2,4,22,19,14,16,12,6,17,27,8,10,25,23],
    SPLUS_GENS_ONE[4], SPLUS_GENS_ONE[5],
]
SPLUS_GENERATOR_SHA256 = "75185d7d653b094bcc6ec67d8fde12fe84b065775e485301eba496114fe2e434"
TPLUS_GENERATOR_SHA256 = "40f03e3dc7c2b44c82a6ae6d1b79708bd7f36115921299ebb85522e07c010006"
SPLUS_SHA256 = "1df969ee447989751850d36d7af50ce219daff3dbc830c56df04d93e9c512871"
TPLUS_SHA256 = "55d7f2df8abc6709489e9bf632c45d620b9b570e6a295a82ee6f941c24c2c6bc"
G149_ONE = [1,3,13,14,19,6,27,10,9,7,24,17,16,12,22,2,4,21,5,20,15,18,11,26,25,23,8]

GLOBAL_LOCAL_ARRAYS_ONE = {
    "I5": [
        [16,23,27,8,26,9,7,11,24,10,25,5,13,6,12,20,2,18,19,22,17,1,21,14,4,15,3],
        [16,2,23,8,18,17,25,4,21,10,11,12,22,27,26,1,6,5,19,20,9,13,3,24,7,15,14],
    ],
    "P5": [[10,7,3,14,4,6,1,12,5,13,15,17,2,19,21,8,27,25,9,11,24,23,26,20,22,18,16]],
    "C3": [[23,25,18,22,17,21,1,14,4,15,12,19,2,20,16,10,24,27,11,8,26,9,7,5,13,6,3]],
    "C2": [[1,2,3,6,5,4,7,8,11,10,9,12,15,14,13,18,17,16,21,20,19,22,23,24,27,26,25]],
    "Cinf": [[6,13,16,12,5,1,18,15,20,22,26,4,2,17,8,3,14,7,19,9,27,10,24,23,25,11,21]],
}

MIXED_TYPE_BY_SEED = {148:1,24:2,178:2,149:3,2:4,3:4,12:5,169:5,0:6,1:6,7:7,4:8}
MIXED_REP_SEED = {1:148,2:24,3:149,4:2,5:12,6:0,7:7,8:4}
# The first coordinate below is the orbit size for the left H+ action on
# W/H-, hence the twelve rows partition 320 tensor cosets.  This is distinct
# from the eight-type conjugate-position atlas, whose orbit sizes partition
# the 160 conjugates of H- in W.
MIXED_CONJUGATE_POSITION_ORBIT_SIZE = {1:1,2:3,3:3,4:9,5:9,6:27,7:27,8:81}
MIXED_EXPECTED = {
    1:(2,81,640,"80f5ac65a18777d49696ef6984295ab079f0cc22e9d6f0f714206ab982f264c2",324,160,"8fd5fa5d8dce47de3abde3c22a1009fc14d4783fca365d2690f206145400e7b0"),
    2:(3,54,960,"0a46cb2019e7081ad7b9824694b74b8934838adbfbb0562b1cd48fb364b39b4f",1296,40,"263f31237e6f5111f76fd3470b6936a1a314020255c22eab55cece395c2adeb5"),
    3:(6,27,1920,"b4ddf19696979fba9969b33ee0c1930a4e2fb5fb08e1c07975b4769d1e29297b",1296,40,TPLUS_SHA256),
    4:(9,18,2880,"5d939a688629fd6974e7f4e0a4b2f09c448a083281daeea8f7559e226ffbb4cc",51840,1,"f447fdf7677c795b034f567bcc259b6cfbb476d386b19a4a1f0275963eca034e"),
    5:(9,18,2880,"4300a90fbb4ce30b53883363976eab87bfb2fcb140d4350dcdf9bc093774ac22",51840,1,"f447fdf7677c795b034f567bcc259b6cfbb476d386b19a4a1f0275963eca034e"),
    6:(27,6,8640,"8265cf248b7d0f5e1f85ee4a7308b1e34233dd0386c94884235fb8102ac7c941",51840,1,"f447fdf7677c795b034f567bcc259b6cfbb476d386b19a4a1f0275963eca034e"),
    7:(54,3,17280,"c3c2a97cf3dca0c8713e78d25cfd1b468b076996c3257c308315d6683b1a13ae",51840,1,"f447fdf7677c795b034f567bcc259b6cfbb476d386b19a4a1f0275963eca034e"),
    8:(162,1,51840,"481e7c7f6f7b34318ede4b559b57c7d901fe78e607e27f6d9d22dba13beb4b22",51840,1,"f447fdf7677c795b034f567bcc259b6cfbb476d386b19a4a1f0275963eca034e"),
}

FOURIER_EXPECTED = {
    "Trace": (2,243,[[2,54],[4,189]],"a7398d36cea0c83ace64466a579e21666731d1e3c8e8641df4ce036c79de2bd7",581739),
    "rplus": (2,54,[[-1,27],[1,27]],"2edfe1e8f952faf2ddbfae3af135da4509f3f40e4175e188e240a5f09b785a96",643771),
    "r3": (2,162,[[-1,81],[1,81]],"b9c21c9fc7060d4e52630a75d6ec0c10305ac33946f78c2c93e33fad68df8c7e",119649),
    "r0": (4,7560,[[-3,54],[-2,324],[-1,3402],[1,3402],[2,324],[3,54]],"a26813d1b2874ee700ececba786af55391dacc2a30a0d4da0390ecb871f63382",582281),
    "delta_plus": (4,1458,[[-2,729],[1,54],[2,648],[4,27]],"1b5927b4d213dfd5af490067a9a551ae0942791a5221e2fb2f9f826440b040c3",None),
    "delta3": (4,10125,[[-4,729],[-2,4131],[1,162],[2,4698],[4,405]],"5f8baf7254f5c27478afce45b5667c62d13a35b205739bbf20ebd36651a144e7",None),
}
ORBIT_EXPECTED = {
    "rplus": (80,"ce3e5dc81b4b902eaaa4cc0edf34daaccea64c94262774bf9c4f5561f80ede31","37042b8b829035a921be14a4360c11073450b025fe3d2af451b412192f84aff4"),
    "delta_plus": (40,"eb3a6df8d4b172f906c8bb968501bd0dad5989b02c160efba75a7739d3791e13","a70e4e7fdad54cd3f5c68f10ee382baa6237b64847e8889129d7d69ee30ff878"),
    "r3": (320,"9eb456211f8841c7968d83140cad9f5103f6ffadabf979184df4bc69c400b725","5e37b4d0f662281feaa5616768b3173d62078a05f69c81b95f29d94415434ec9"),
    "delta3": (160,"d8f1099368ad68c9f3961d2d21f70bd553b5fab9058ce25936a2856c408f77c2","bd98f2356fcc0476dbd44c253343e2851de5121d77f8c852d30017307c24489c"),
    "r0": (320,"6eec729eeb002432f0a36866e041ebeb3cddf9e1a2eb9226922975bb13bacba5","9f7f845af3b92151c004d894bb150ed9db51ac7281ea9f4af32ab8f31ed25118"),
    "delta0": (160,"0fe6b00526627175b2d83621c85da1c4c1c01eb12cf3ddee7b106f4154a02e22","5c7b8802fa76fa3c67d22616369a56d526541ce0d1476f299dd40e00b0321004"),
}

GLOBAL_EXPECTED = {
    "E1":(640,[0,320],1,[1264,992,384,320],[32,0,0,0]),
    "E2":(960,[16,472],1,[1944,1488,624,480],[312,0,192,0]),
    "E3":(1920,[0,960],1,[3808,2976,1152,960],[208,48,0,240]),
    "E4":(2880,[16,1432],1,[5872,4464,1872,1440],[5872,4464,1872,1440]),
    "E5":(2880,[48,1416],1,[5856,4464,1872,1440],[5856,4464,1872,1440]),
    "E6":(8640,[48,4296],1,[17640,13392,5616,4320],[17640,13392,5616,4320]),
    "E7":(17280,[0,8640],1,[35504,26784,11520,8640],[35504,26784,11520,8640]),
    "E8":(51840,[0,25920],1,[106560,80352,34560,25920],[106560,80352,34560,25920]),
    "C1":(160,[16,72],1,[308,248,96,80],None),
    "C2":(40,[8,16],1,[68,62,18,20],None),
    "C3":(40,[6,17],-1,[75,61,24,15],None),
    "C4":(1,[1,0],1,[0,0,0,0],None),
    "B80":(80,[4,38],1,[154,122,48,30],None),
}

SCOPE_KEYS = [
    "artin_holomorphy_claimed","automorphy_claimed","bad_artin_euler_claimed",
    "brauer_manin_claimed","characteristic_zero_coefficient_hash_claimed",
    "class_number_claimed","d3_branch_selected","decomposition_frobenius_claimed",
    "expanded_characteristic_zero_resolvent_claimed",
    "finite_g_sets_isomorphic_from_character_relation",
    "formal_invariant_statement_after_root_relations","global_root_number_claimed",
    "hasse_principle_claimed","hilbert_polya_operator_claimed",
    "integral_basis_claimed","local_epsilon_factor_claimed",
    "local_fields_classified_by_nefd_rows","local_root_number_claimed",
    "maximal_order_claimed","monogenicity_claimed","motive_claimed",
    "paper_complete_claimed","rational_point_claimed","raw_tom_defines_fields",
    "regulator_claimed","release_claimed","rh_claimed",
    "target_selection_pilot_is_theorem_authority","trace_form_claimed",
    "weak_approximation_claimed",
]

TOP_KEYS = [
    "schema_id","schema_sha256","authority","conventions",
    "GAF0_released_authority_rebind","GAF1_fourier_carrier_dag",
    "GAF2_orbit_span_and_nonnormality","GAF3_stabilizers_and_noncollision",
    "GAF4_mixed_type3_exact_bridge","GAF5_fixed_field_diamond",
    "GAF6_global_arithmetic","GAF7_both_local_branches_and_ideal_laws",
    "independence_contract","scope_nonclaims","status","payload_sha256",
]
SCHEMA_SPEC = {
    "schema_id":"hcs-c61-resolvent-evidence-v1",
    "top_level_keys":TOP_KEYS,
    "strict_json":True,
    "unknown_or_missing_fields_rejected_by_independent_full_rebuild":True,
    "duplicate_keys_rejected":True,
    "floats_rejected":True,
    "booleans_rejected_in_integer_slots":True,
    "non_utf8_rejected":True,
    "noncanonical_json_rejected":True,
    "max_evidence_bytes":25000000,
    "scope_false_leaf_count":30,
}


class Failure(RuntimeError):
    pass


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def strict_json(raw: bytes) -> Any:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in items:
            if type(key) is not str or key in out:
                raise Failure(f"duplicate or non-string JSON key: {key!r}")
            out[key] = value
        return out
    try:
        return json.loads(
            raw.decode("utf-8"), object_pairs_hook=pairs,
            parse_float=lambda token: (_ for _ in ()).throw(Failure(f"float forbidden: {token}")),
            parse_constant=lambda token: (_ for _ in ()).throw(Failure(f"constant forbidden: {token}")),
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Failure("invalid strict JSON") from exc


def stable_read(path: Path, max_bytes: int = 30_000_000) -> tuple[bytes, dict[str, Any]]:
    path = path.absolute()
    before = os.lstat(path)
    if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1 or before.st_size > max_bytes:
        raise Failure(f"non-regular, symlink, hardlink, or oversized input: {path}")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags)
    try:
        first = os.fstat(fd)
        chunks: list[bytes] = []
        while True:
            chunk = os.read(fd, 1 << 20)
            if not chunk:
                break
            chunks.append(chunk)
        last = os.fstat(fd)
    finally:
        os.close(fd)
    snap = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns, s.st_mode, s.st_nlink)
    after = os.lstat(path)
    if snap(before) != snap(first) or snap(first) != snap(last) or snap(last) != snap(after):
        raise Failure(f"TOCTOU snapshot drift: {path}")
    raw = b"".join(chunks)
    if len(raw) != before.st_size:
        raise Failure(f"short read: {path}")
    return raw, {
        "path":str(path),"sha256":sha256_bytes(raw),"size_bytes":len(raw),
        "lines":len(raw.splitlines()),
        "filesystem_identity":{
            "dev":after.st_dev,"ino":after.st_ino,"mode":after.st_mode,
            "mtime_ns":after.st_mtime_ns,"ctime_ns":after.st_ctime_ns,
            "nlink":after.st_nlink,
        },
    }


def canonical_layout() -> tuple[Path,Path,Path]:
    invoked=Path(__file__).absolute()
    source=invoked.resolve(strict=True)
    project=source.parent.parent
    if source.name!="c61_resolvent.py" or source.parent.name!="code" or project.name!=PROJECT_BASENAME:
        raise Failure("resolver is not installed at canonical PROJECT/code basename")
    repo=project.parent.parent
    if project.parent.name!="henon_dynamics" or not stat.S_ISDIR(os.lstat(repo).st_mode):
        raise Failure("cannot derive canonical repository from installed resolver")
    if invoked!=source or project.resolve(strict=True)!=project or repo.resolve(strict=True)!=repo:
        raise Failure("canonical repository/project path is not real")
    source_info=os.lstat(source)
    if not stat.S_ISREG(source_info.st_mode) or source_info.st_nlink!=1:
        raise Failure("resolver source is not one real regular file")
    return repo,project,source


def directory_snapshot(path:Path)->tuple[int,int,int,int]:
    info=os.lstat(path)
    if not stat.S_ISDIR(info.st_mode) or stat.S_ISLNK(info.st_mode) or path.resolve(strict=True)!=path:
        raise Failure("stage/results directory is not one real directory")
    return (info.st_dev,info.st_ino,info.st_mode,info.st_mtime_ns)


def staged_evidence_path(value:str,must_exist:bool)->tuple[Path,Path,tuple[int,int,int,int]]:
    _repo,project,_source=canonical_layout()
    results=project/"results"
    directory_snapshot(results)
    path=Path(value).absolute();stage=path.parent
    if path.name!=EVIDENCE_BASENAME or STAGE_PATTERN.fullmatch(stage.name) is None or stage.parent!=results:
        raise Failure("evidence must use fixed basename in a direct canonical C61 stage")
    identity=directory_snapshot(stage)
    if must_exist:
        _raw,record=stable_read(path,25_000_000)
        if stat.S_IMODE(record["filesystem_identity"]["mode"])!=0o644:
            raise Failure("existing evidence mode must be 0644")
    elif os.path.lexists(path):
        raise Failure("write mode requires an absent evidence leaf; use check-existing for replay")
    return path,stage,identity


def runtime_input_snapshot() -> dict[str,dict[str,int|str]]:
    """Bind every mutable installed authority/source leaf outside the evidence stage.

    Immutable released inputs are independently rebound from the pinned P60 Git
    objects by ``bind_authority``.  This snapshot closes the mutable worktree
    layer across checker children and the final write without putting inode or
    timestamp accidents into deterministic theorem evidence.
    """
    repo,project,producer=canonical_layout()
    rels=[Path("henon_dynamics/BATCH_PLAN_C57_C61.md")]
    rels += [Path("henon_dynamics")/PROJECT_BASENAME/name for name in FORMAL_MD]
    rels += [Path("henon_dynamics")/PROJECT_BASENAME/"route_a_evaluation.yaml",TARGET_GUARD_REL]
    paths={rel.as_posix():safe_repo_path(repo,rel) for rel in rels}
    paths["henon_dynamics/"+PROJECT_BASENAME+"/code/c61_resolvent.py"]=producer
    paths["henon_dynamics/"+PROJECT_BASENAME+"/code/c61_checker_resolvent.py"]=producer.with_name("c61_checker_resolvent.py")
    snapshot:dict[str,dict[str,int|str]]={}
    for label,path in sorted(paths.items()):
        _raw,record=stable_read(path,2_000_000)
        snapshot[label]={"sha256":record["sha256"],"size_bytes":record["size_bytes"],**record["filesystem_identity"]}
    snapshot["henon_dynamics/"+PROJECT_BASENAME+"/results"]={
        "sha256":"DIRECTORY_IDENTITY","size_bytes":0,
        **dict(zip(("dev","ino","mode","mtime_ns"),directory_snapshot(project/"results"))),
        "ctime_ns":0,"nlink":0,
    }
    return snapshot


def assert_stage(stage:Path,identity:tuple[int,int,int,int],allow_mtime_change:bool=False)->tuple[int,int,int,int]:
    now=directory_snapshot(stage)
    if now[:3]!=identity[:3] or (not allow_mtime_change and now[3]!=identity[3]):
        raise Failure("canonical C61 stage changed or was substituted during replay")
    return now


def safe_repo_path(root: Path, relative: Path) -> Path:
    if relative.is_absolute() or ".." in relative.parts:
        raise Failure("unsafe authority path")
    root_abs = root.absolute()
    candidate = (root_abs / relative).absolute()
    if os.path.commonpath([str(root_abs), str(candidate)]) != str(root_abs):
        raise Failure("authority path escaped repository")
    return candidate


Permutation = tuple[int, ...]
Poly = dict[tuple[int, ...], int]


def one_to_zero(rows: Sequence[Sequence[int]]) -> list[Permutation]:
    out: list[Permutation] = []
    for row in rows:
        if type(row) is not list or len(row) != DEGREE or sorted(row) != list(range(1, 28)):
            raise Failure("invalid one-based permutation")
        out.append(tuple(int(x)-1 for x in row))
    return out


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[i]] for i in range(DEGREE))


def inverse(value: Permutation) -> Permutation:
    out = [0] * DEGREE
    for i, j in enumerate(value):
        out[j] = i
    return tuple(out)


def conjugate(carrier: Permutation, element: Permutation) -> Permutation:
    return compose(carrier, compose(element, inverse(carrier)))


def generated(gens: Iterable[Permutation]) -> frozenset[Permutation]:
    generators = tuple(gens)
    seen = {IDENTITY}
    queue: deque[Permutation] = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for generator in generators:
            nxt = compose(generator, current)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return frozenset(seen)


def group_arrays(group: Iterable[Permutation]) -> list[list[int]]:
    return [[v+1 for v in g] for g in sorted(group)]


def group_sha(group: Iterable[Permutation]) -> str:
    return digest(group_arrays(group))


def normalizer(ambient: Iterable[Permutation], subgroup: frozenset[Permutation], gens: Sequence[Permutation]) -> frozenset[Permutation]:
    return frozenset(g for g in ambient if all(conjugate(g, h) in subgroup for h in gens))


def core(ambient_gens: Sequence[Permutation], subgroup: frozenset[Permutation]) -> frozenset[Permutation]:
    current = subgroup
    carriers = tuple(ambient_gens) + tuple(inverse(g) for g in ambient_gens)
    while True:
        old = current
        for g in carriers:
            current = frozenset(set(current).intersection(conjugate(g, h) for h in current))
        if current == old:
            return current


def poly_serial(poly: Poly) -> list[list[Any]]:
    return [[list(mon), coeff] for mon, coeff in sorted(poly.items()) if coeff]


def poly_sha(poly: Poly) -> str:
    return digest(poly_serial(poly))


def add_scaled(target: Poly, source: Poly, scale: int) -> None:
    for mon, coeff in source.items():
        value = target.get(mon, 0) + scale*coeff
        if value:
            target[mon] = value
        else:
            target.pop(mon, None)


def poly_image(perm: Permutation, poly: Poly) -> Poly:
    return {tuple(sorted(perm[i] for i in mon)): coeff for mon, coeff in poly.items()}


def poly_mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            mon = tuple(sorted(lm + rm))
            out[mon] = out.get(mon, 0) + lc*rc
    return {m:c for m,c in out.items() if c}


def poly_div_exact(poly: Poly, divisor: int) -> Poly:
    if divisor <= 0 or any(c % divisor for c in poly.values()):
        raise Failure("coefficientwise exact division failed")
    return {m:c//divisor for m,c in poly.items()}


def poly_eval(poly: Poly, alpha: Sequence[int]) -> int:
    answer = 0
    for mon, coeff in poly.items():
        value = coeff % P
        for i in mon:
            value = value * alpha[i] % P
        answer = (answer + value) % P
    return answer


def coefficient_histogram(poly: Poly) -> list[list[int]]:
    return [[k,v] for k,v in sorted(Counter(poly.values()).items())]


def frozen_poly(poly: Poly) -> tuple[tuple[tuple[int, ...], int], ...]:
    return tuple(sorted(poly.items()))


def canonical_sign(value: tuple[tuple[tuple[int, ...], int], ...]) -> tuple[tuple[tuple[int, ...], int], ...]:
    neg = tuple((mon,-coeff) for mon,coeff in value)
    return min(value, neg)


def poly_orbit(poly: Poly, generators: Sequence[Permutation], modulo_sign: bool = False) -> list[tuple[tuple[tuple[int, ...], int], ...]]:
    first = frozen_poly(poly)
    if modulo_sign:
        first = canonical_sign(first)
    seen = {first}
    queue = deque([first])
    while queue:
        current = dict(queue.popleft())
        for generator in generators:
            nxt = frozen_poly(poly_image(generator, current))
            if modulo_sign:
                nxt = canonical_sign(nxt)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(seen)


def polynomial_from_roots(roots: Sequence[int]) -> list[int]:
    coeffs = [1]
    for root in roots:
        nxt = [0] * (len(coeffs)+1)
        for i, coeff in enumerate(coeffs):
            nxt[i] = (nxt[i] - root*coeff) % P
            nxt[i+1] = (nxt[i+1] + coeff) % P
        coeffs = nxt
    return coeffs


def orbit_record(poly: Poly, w_gens: Sequence[Permutation], alpha: Sequence[int], square: bool = False) -> dict[str, Any]:
    orbit = poly_orbit(poly, w_gens, modulo_sign=square)
    values = sorted({pow(poly_eval(dict(item), alpha), 2 if square else 1, P) for item in orbit})
    coeffs = polynomial_from_roots(values)
    return {
        "formal_orbit_size":len(orbit),
        "modular_distinct_value_count":len(values),
        "sorted_values_sha256":digest(values),
        "modular_minimal_polynomial_coefficient_count":len(coeffs),
        "modular_minimal_polynomial_sha256":digest(coeffs),
        "complete_noncollision":len(values)==len(orbit),
    }


class CosetAction:
    """Left action on canonical right H-cosets gH."""
    def __init__(self, ambient: frozenset[Permutation], subgroup: frozenset[Permutation], identity_first: bool = False) -> None:
        unseen = set(ambient)
        reps: list[Permutation] = []
        mapping: dict[Permutation,int] = {}
        ordered = sorted(ambient)
        if identity_first:
            ordered = [IDENTITY] + [item for item in ordered if item != IDENTITY]
        # Scanning a pre-sorted ambient list is exactly the same least-unseen
        # enumeration, without the quadratic repeated min(set) cost for the
        # trivial-subgroup 51,840-coset carrier.
        for rep in ordered:
            if rep not in unseen:
                continue
            coset = {compose(rep,h) for h in subgroup}
            if not coset <= unseen:
                raise Failure("right cosets overlap")
            idx = len(reps)
            reps.append(rep)
            for item in coset:
                mapping[item] = idx
            unseen.difference_update(coset)
        if unseen:
            raise Failure("right coset enumeration incomplete")
        self.representatives = reps
        self.mapping = mapping
        self.degree = len(reps)

    def image(self, element: Permutation, index: int) -> int:
        return self.mapping[compose(element, self.representatives[index])]

    def orbits(self, subgroup: frozenset[Permutation], domain: Iterable[int] | None = None) -> list[list[int]]:
        unseen = set(range(self.degree) if domain is None else domain)
        answer: list[list[int]] = []
        # Again preserve least-unseen order by one sorted scan instead of
        # repeatedly taking min on a large shrinking set.
        for seed in sorted(unseen):
            if seed not in unseen:
                continue
            block = {self.image(g,seed) for g in subgroup}
            if not block <= unseen:
                raise Failure("coset orbit overlap")
            unseen.difference_update(block)
            answer.append(sorted(block))
        if unseen:
            raise Failure("coset orbit enumeration incomplete")
        return answer


def canonical_output(value: Any) -> bytes:
    return canonical(value) + b"\n"


def atomic_write(path:Path,raw:bytes,stage:Path,identity:tuple[int,int,int,int])->tuple[int,int,int,int]:
    assert_stage(stage,identity)
    if os.path.lexists(path):raise Failure("atomic write target appeared")
    fd,temp_name=tempfile.mkstemp(prefix=f".{path.name}.",dir=stage)
    temp=Path(temp_name)
    try:
        meta=os.fstat(fd)
        if not stat.S_ISREG(meta.st_mode) or meta.st_nlink!=1:raise Failure("unsafe atomic temporary")
        os.fchmod(fd,0o644)
        view = memoryview(raw)
        while view:
            written = os.write(fd, view)
            view = view[written:]
        os.fsync(fd)
        written_meta=os.fstat(fd)
        if not stat.S_ISREG(written_meta.st_mode) or stat.S_IMODE(written_meta.st_mode)!=0o644 or written_meta.st_nlink!=1 or written_meta.st_size!=len(raw):
            raise Failure("atomic temporary identity changed during write")
        os.close(fd)
        fd=-1
        assert_stage(stage,identity,allow_mtime_change=True)
        if os.path.lexists(path):raise Failure("atomic target raced into existence")
        os.replace(temp,path)
        directory=os.open(stage,os.O_RDONLY|getattr(os,"O_DIRECTORY",0))
        os.fsync(directory)
        os.close(directory)
        rebound=assert_stage(stage,identity,allow_mtime_change=True)
        rebound_raw,rebound_record=stable_read(path,25_000_000)
        if rebound_raw!=raw or stat.S_IMODE(rebound_record["filesystem_identity"]["mode"])!=0o644 or rebound_record["filesystem_identity"]["nlink"]!=1:
            raise Failure("atomic evidence bytes/mode/link count did not rebind")
        return rebound
    finally:
        if fd>=0:os.close(fd)
        if os.path.lexists(temp):os.unlink(temp)


def git_value(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=repo, stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        env={"PATH":os.environ.get("PATH", "")},
    )
    if completed.returncode or completed.stderr:
        raise Failure(f"git {' '.join(args)} failed closed")
    return completed.stdout.decode("ascii").strip()


def parse_hash_ledger(raw: bytes) -> list[tuple[str,str]]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise Failure("manifest is not UTF-8") from exc
    rows: list[tuple[str,str]] = []
    seen: set[str] = set()
    for line in text.splitlines():
        if not line:
            continue
        if len(line) < 67 or line[64:66] != "  ":
            raise Failure("malformed sha256sum ledger")
        h, name = line[:64], line[66:]
        if len(h) != 64 or any(c not in "0123456789abcdef" for c in h):
            raise Failure("malformed ledger digest")
        if name.startswith("./"):
            name = name[2:]
        rel = Path(name)
        if rel.is_absolute() or ".." in rel.parts or name in seen:
            raise Failure("unsafe or duplicate ledger path")
        seen.add(name)
        rows.append((h,name))
    if [name for _,name in rows] != sorted(name for _,name in rows):
        raise Failure("manifest paths not sorted")
    return rows


def git_blob(repo: Path, relative: Path) -> bytes:
    if relative.is_absolute() or ".." in relative.parts:
        raise Failure("unsafe Git-object path")
    run=subprocess.run(
        ["git","show",f"{RELEASE_COMMIT}:{relative.as_posix()}"],cwd=repo,
        stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
        check=False,env={"PATH":os.environ.get("PATH","")},
    )
    if run.returncode or run.stderr:
        raise Failure(f"cannot read released Git object: {relative}")
    return run.stdout


def verify_full_manifest(repo: Path, raw: bytes) -> dict[str, Any]:
    rows = parse_hash_ledger(raw)
    root = safe_repo_path(repo, C60_ROOT)
    total = 0
    for expected, name in rows:
        # Resolve every manifested leaf from immutable P60, never from a dirty
        # worktree.  safe_repo_path remains an independent traversal check.
        safe_repo_path(root,Path(name))
        leaf=git_blob(repo,C60_ROOT/Path(name))
        if sha256_bytes(leaf) != expected:
            raise Failure(f"C60 full-manifest leaf drift: {name}")
        total += len(leaf)
    if len(rows) != 88:
        raise Failure("C60 full-manifest entry count changed")
    return {"entry_count":len(rows),"verified_leaf_total_bytes":total,"all_entries_rebound":True}


def installed_formal_bind(repo: Path) -> dict[str, Any]:
    target_root=Path("henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent")
    expected = [Path("BATCH_PLAN_C57_C61.md")]
    expected += [Path("henon_mu3_yukawa_tensor_fourier_descent")/name for name in FORMAL_MD]
    expected += [Path("henon_mu3_yukawa_tensor_fourier_descent/route_a_evaluation.yaml")]
    records: list[dict[str,Any]] = []
    raw_by_rel: dict[str,bytes] = {}
    for rel in sorted(expected,key=lambda x:x.as_posix()):
        repo_rel=Path("henon_dynamics")/rel
        raw, record = stable_read(safe_repo_path(repo,repo_rel),1_000_000)
        raw_by_rel[rel.as_posix()] = raw
        records.append({"path":rel.as_posix(),"sha256":record["sha256"],"size_bytes":record["size_bytes"],"lines":record["lines"]})
    formal_lines = b"".join(
        f"{sha256_bytes(raw_by_rel['henon_mu3_yukawa_tensor_fourier_descent/'+name])}  {name}\n".encode("ascii")
        for name in FORMAL_MD
    )
    ledger_lines = b"".join(
        f"{record['sha256']}  {record['path']}\n".encode("ascii") for record in records
    )
    total_bytes = sum(r["size_bytes"] for r in records)
    total_lines = sum(r["lines"] for r in records)
    if (
        sha256_bytes(formal_lines) != FORMAL13_SHA256
        or sha256_bytes(raw_by_rel["henon_mu3_yukawa_tensor_fourier_descent/route_a_evaluation.yaml"]) != FORMAL_ROUTE_SHA256
        or sha256_bytes(raw_by_rel["BATCH_PLAN_C57_C61.md"]) != FORMAL_BATCH_SHA256
        or sha256_bytes(ledger_lines) != FORMAL15_SHA256
        or len(records) != FORMAL15_COUNT or total_bytes != FORMAL15_BYTES or total_lines != FORMAL15_LINES
    ):
        raise Failure("frozen formal tuple changed")
    return {
        "installed_root":target_root.as_posix(),
        "formal_root_count":13,"formal_root_aggregate_sha256":FORMAL13_SHA256,
        "route_sha256":FORMAL_ROUTE_SHA256,"batch_sha256":FORMAL_BATCH_SHA256,
        "exact15_ledger_sha256":FORMAL15_SHA256,"exact15_count":len(records),
        "exact15_bytes":total_bytes,"exact15_lines":total_lines,"entries":records,
    }


def bind_authority() -> tuple[dict[str,Any], dict[str,Any]]:
    if not __debug__:
        raise Failure("optimized Python forbidden")
    repo,_project,producer_path = canonical_layout()
    if not stat.S_ISDIR(os.lstat(repo).st_mode):
        raise Failure("repository root is not a real directory")
    head = git_value(repo,"rev-parse","HEAD")
    parent = git_value(repo,"rev-parse","HEAD^")
    tree = git_value(repo,"rev-parse","HEAD^{tree}")
    if (head,parent,tree) != (RELEASE_COMMIT,RELEASE_PARENT,RELEASE_TREE):
        raise Failure("released P60 identity changed")

    inputs: dict[str,bytes] = {}
    records: dict[str,Any] = {}
    for label,(relative,expected) in C60_PINS.items():
        safe_repo_path(repo,relative)
        raw=git_blob(repo,relative)
        if sha256_bytes(raw) != expected:
            raise Failure(f"released input drift: {label}")
        inputs[label] = raw
        records[label] = {"git_object":f"{RELEASE_COMMIT}:{relative.as_posix()}","sha256":expected,"size_bytes":len(raw)}
    if inputs["route"] != inputs["route_archive"]:
        raise Failure("C60 live/archive Route differ")
    released_batch=git_blob(repo,Path("henon_dynamics/BATCH_PLAN_C57_C61.md"))
    if sha256_bytes(released_batch)!="d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5":
        raise Failure("released P60 Batch object changed")
    records["released_batch"]={"git_object":f"{RELEASE_COMMIT}:henon_dynamics/BATCH_PLAN_C57_C61.md","sha256":"d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5","size_bytes":len(released_batch)}
    manifest_record = verify_full_manifest(repo,inputs["full_manifest"])

    safe_repo_path(repo,C59_RESOLVENT_REL)
    c59_raw=git_blob(repo,C59_RESOLVENT_REL)
    if sha256_bytes(c59_raw) != C59_RESOLVENT_SHA256:
        raise Failure("C59 resolver evidence drift")
    c59 = strict_json(c59_raw)
    cert = strict_json(inputs["certificate"])
    group_ev = strict_json(inputs["group_evidence"])
    resolvent_ev = strict_json(inputs["resolvent_evidence"])
    if digest(cert["payload"]) != cert["payload_sha256"] or cert["payload_sha256"] != C60_PAYLOAD_SHA256:
        raise Failure("C60 canonical payload drift")
    arrays = group_ev["frozen_permutation_arrays"]["arrays"]
    if digest(arrays) != FROZEN_ARRAYS_SHA256 or group_ev["frozen_permutation_arrays"]["canonical_sha256"] != FROZEN_ARRAYS_SHA256:
        raise Failure("C60 frozen arrays drift")
    lam = cert["payload"]["G2_primitive_integral_carriers"]["carriers"]["L"]
    if lam["carrier_sha256"] != LAMBDA_SHA256 or digest(lam["carrier"]) != LAMBDA_SHA256:
        raise Failure("C60 lambda carrier drift")
    if resolvent_ev["payload"]["carriers"]["L"]["carrier_sha256"] != LAMBDA_SHA256:
        raise Failure("C60 resolver lambda bridge drift")

    formal = installed_formal_bind(repo)
    guard_raw,guard_rec=stable_read(safe_repo_path(repo,TARGET_GUARD_REL),1_000_000)
    if guard_rec["sha256"] != TARGET_GUARD_SHA256:
        raise Failure("installed protected guard drift")

    checker_path=producer_path.with_name("c61_checker_resolvent.py")
    producer_raw, producer_rec = stable_read(producer_path,2_000_000)
    checker_raw, checker_rec = stable_read(checker_path,2_000_000)
    if b"c61_resolvent" not in producer_raw or b"c61_checker_resolvent" not in checker_raw:
        raise Failure("resolver source identities changed")
    alpha = c59["payload"]["line_configuration"]["alpha_by_standard_label"]
    if type(alpha) is not list or len(alpha) != 27 or any(type(v) is not int or not 0 <= v < P for v in alpha) or len(set(alpha)) != 27:
        raise Failure("labelled split roots invalid")
    finite=c59["payload"]["finite_field"]
    if c59["payload"]["constants"]["prime"]!=P or finite["prime_proven"] is not True or finite["factor_degrees"]!=[[1,27]] or c59["payload"]["G1_primitive_orbit_resolvents"]["factor_degrees"]!=[[1,27]] or c59["payload"]["line_configuration"]["all_equation_residues_zero"] is not True:
        raise Failure("released C59 completely-split labelled-root certificate changed")

    authority = {
        "release":{"commit":head,"parent":parent,"tree":tree,"worktree_layer_included":False},
        "released_c60":records,
        "c60_payload_sha256":C60_PAYLOAD_SHA256,
        "c60_full_manifest_replay":manifest_record,
        "c59_resolvent":{"git_object":f"{RELEASE_COMMIT}:{C59_RESOLVENT_REL.as_posix()}","sha256":C59_RESOLVENT_SHA256,"size_bytes":len(c59_raw)},
        "released_C59_completely_split_prime_certificate":{
            "source_git_object":f"{RELEASE_COMMIT}:{C59_RESOLVENT_REL.as_posix()}",
            "prime_locator":"payload.constants.prime","prime":P,
            "prime_proven_locator":"payload.finite_field.prime_proven","prime_proven":True,
            "factor_degrees_locator":"payload.finite_field.factor_degrees","factor_degrees":[[1,27]],
            "G1_factor_degrees_locator":"payload.G1_primitive_orbit_resolvents.factor_degrees","G1_factor_degrees":[[1,27]],
            "labelled_roots_locator":"payload.line_configuration.alpha_by_standard_label","labelled_root_count":27,
            "labelled_roots_sha256":digest(alpha),"labelled_roots_pairwise_distinct":True,
            "all_equation_residues_zero_locator":"payload.line_configuration.all_equation_residues_zero","all_equation_residues_zero":True,
            "K_completely_split_at_prime":True,
        },
        "frozen_permutation_arrays_sha256":FROZEN_ARRAYS_SHA256,
        "lambda_carrier_sha256":LAMBDA_SHA256,
        "formal_target":formal,
        "installed_protected_guard":{"path":TARGET_GUARD_REL.as_posix(),"sha256":guard_rec["sha256"],"size_bytes":len(guard_raw)},
        "whole_project_inventory_owner":"release runner",
        "resolver_replay_contract":{"builder_basename":"c61_resolvent.py","checker_basename":"c61_checker_resolvent.py","evidence_basename":EVIDENCE_BASENAME,"canonical_stage_pattern":".c61-stage-XXXXXXXX","repository_and_project_derived_from_installed_source":True,"write_requires_absent_leaf":True,"existing_bytes_require_check_existing":True},
        "source_files":{
            "producer":{"sha256":producer_rec["sha256"],"size_bytes":producer_rec["size_bytes"]},
            "checker":{"sha256":checker_rec["sha256"],"size_bytes":checker_rec["size_bytes"]},
        },
        "runtime_pilot_dependencies":[],
    }
    docs = {"certificate":cert,"group_evidence":group_ev,"c59_resolvent":c59,"arrays":arrays,"lambda_record":lam,"alpha":alpha}
    return authority,docs


def build_groups(arrays: dict[str,Any]) -> dict[str,Any]:
    gens = {key:one_to_zero(value) for key,value in arrays.items() if key.endswith("_generators")}
    W = generated(gens["W27_generators"])
    N = generated(gens["N_generators"])
    J = generated(gens["J_generators"])
    Hplus = generated(gens["H301_generators"])
    H0 = generated(gens["H302_generators"])
    Hminus = generated(gens["H303_generators"])
    x = one_to_zero([arrays["normalizer_conjugator"]])[0]
    H3 = generated(conjugate(x,h) for h in gens["H303_generators"])
    Splus_gens = one_to_zero(SPLUS_GENS_ONE)
    Tplus_gens = one_to_zero(TPLUS_GENS_ONE)
    Splus = generated(Splus_gens)
    Tplus = generated(Tplus_gens)
    groups = {
        "W":W,"N":N,"J":J,"Hplus":Hplus,"H0":H0,"Hminus":Hminus,
        "H3":H3,"Splus":Splus,"Tplus":Tplus,
    }
    orders = {key:len(value) for key,value in groups.items()}
    expected = {"W":51840,"N":324,"J":81,"Hplus":162,"H0":162,"Hminus":162,"H3":162,"Splus":648,"Tplus":1296}
    if orders != expected:
        raise Failure(f"group orders changed: {orders}")
    if not (J < Hplus < N < W and J < H0 < N and J < H3 < N):
        raise Failure("released V4 subgroup lattice changed")
    if digest(SPLUS_GENS_ONE) != SPLUS_GENERATOR_SHA256 or digest(TPLUS_GENS_ONE) != TPLUS_GENERATOR_SHA256:
        raise Failure("source-owned S/T generator digest changed")
    if group_sha(Splus) != SPLUS_SHA256 or group_sha(Tplus) != TPLUS_SHA256:
        raise Failure("source-owned S/T complete group changed")
    q_expected = {k:one_to_zero([v])[0] for k,v in QUOTIENT_REPS_ONE.items()}
    q_rebuilt = {
        "1":IDENTITY,
        "Hplus":min(Hplus-J),
        "H0":min(H0-J),
        "H3":min(H3-J),
    }
    if q_expected != q_rebuilt:
        raise Failure("canonical V4 quotient representatives changed")
    quotient_cosets = {frozenset(compose(q,j) for j in J) for q in q_rebuilt.values()}
    if len(quotient_cosets) != 4 or set().union(*quotient_cosets) != set(N):
        raise Failure("quotient representatives do not partition N/J")
    return {
        "groups":groups,"generators":gens,"Splus_generators":Splus_gens,
        "Tplus_generators":Tplus_gens,"quotient_reps":q_rebuilt,
        "normalizer_conjugator":x,"orders":orders,
    }


def enumerate_mixed(context: dict[str,Any]) -> tuple[list[dict[str,Any]],dict[int,tuple[frozenset[Permutation],frozenset[Permutation]]]]:
    groups = context["groups"]
    gens = context["generators"]
    W,Hplus,Hminus = groups["W"],groups["Hplus"],groups["Hminus"]
    hp_gens,hm_gens = gens["H301_generators"],gens["H303_generators"]
    action = CosetAction(W,Hminus)
    unseen = set(range(action.degree))
    rows: list[dict[str,Any]] = []
    type_groups: dict[int,tuple[frozenset[Permutation],frozenset[Permutation]]] = {}
    while unseen:
        seed = min(unseen)
        g = action.representatives[seed]
        orbit = {action.image(h,seed) for h in Hplus}
        if not orbit <= unseen:
            raise Failure("mixed double-coset orbits overlap")
        unseen.difference_update(orbit)
        conjugate_group = frozenset(conjugate(g,h) for h in Hminus)
        conjugate_gens = tuple(conjugate(g,h) for h in hm_gens)
        inter = frozenset(Hplus.intersection(conjugate_group))
        join = generated(tuple(hp_gens)+conjugate_gens)
        if seed not in MIXED_TYPE_BY_SEED:
            raise Failure(f"unexpected mixed seed {seed}")
        kind = MIXED_TYPE_BY_SEED[seed]
        if len(orbit) != len(Hplus)//len(inter):
            raise Failure("mixed orbit-stabilizer failed")
        row = {
            "seed":seed,"representative_one_based":[x+1 for x in g],
            "tensor_right_coset_orbit_size":len(orbit),
            "conjugate_position_orbit_size":MIXED_CONJUGATE_POSITION_ORBIT_SIZE[kind],
            "q_isomorphism_type":kind,
            "intersection_order":len(inter),"intersection_sha256":group_sha(inter),
            "simple_factor_degree":len(W)//len(inter),
            "join_order":len(join),"join_sha256":group_sha(join),
            "intersection_field_degree":len(W)//len(join),
        }
        rows.append(row)
        if seed == MIXED_REP_SEED[kind]:
            type_groups[kind] = (inter,join)
            raw,iorder,edeg,isha,jorder,cdeg,jsha = MIXED_EXPECTED[kind]
            actual = (len(orbit),len(inter),len(W)//len(inter),group_sha(inter),len(join),len(W)//len(join),group_sha(join))
            if actual != (raw,iorder,edeg,isha,jorder,cdeg,jsha):
                raise Failure(f"mixed representative type {kind} changed")
    rows.sort(key=lambda r:r["seed"])
    if len(rows) != 12 or set(MIXED_TYPE_BY_SEED) != {r["seed"] for r in rows} or len(type_groups) != 8:
        raise Failure("mixed 12/8 inventory changed")
    multiplicities = Counter(r["q_isomorphism_type"] for r in rows)
    if [multiplicities[i] for i in range(1,9)] != [1,2,1,2,2,2,1,1]:
        raise Failure("mixed multiplicities changed")
    if sum(r["simple_factor_degree"] for r in rows) != 102400:
        raise Failure("mixed tensor dimension changed")
    if sum(r["tensor_right_coset_orbit_size"] for r in rows) != 320:
        raise Failure("mixed tensor right-coset count changed")
    if sum(MIXED_CONJUGATE_POSITION_ORBIT_SIZE.values()) != 160:
        raise Failure("mixed conjugate-position atlas count changed")
    return rows,type_groups


def multiply_integer_polynomials(left: Sequence[int],right: Sequence[int]) -> list[int]:
    answer = [0]*(len(left)+len(right)-1)
    for i,a in enumerate(left):
        for j,b in enumerate(right):
            answer[i+j] += a*b
    return answer


def multiply_mod_polynomials(left: Sequence[int],right: Sequence[int]) -> list[int]:
    answer = [0]*(len(left)+len(right)-1)
    for i,a in enumerate(left):
        for j,b in enumerate(right):
            answer[i+j] = (answer[i+j]+a*b) % P
    return answer


def lagrange_basis(alpha: Sequence[int]) -> tuple[list[list[int]],list[int]]:
    basis: list[list[int]] = []
    for j,a in enumerate(alpha):
        numerator = [1]
        denominator = 1
        for k,b in enumerate(alpha):
            if k == j:
                continue
            numerator = multiply_mod_polynomials(numerator,[(-b)%P,1])
            denominator = denominator*(a-b) % P
        scale = pow(denominator,-1,P)
        basis.append([(x*scale)%P for x in numerator])
    for j,coeffs in enumerate(basis):
        for k,a in enumerate(alpha):
            value = 0
            for coeff in reversed(coeffs):
                value = (value*a+coeff)%P
            if value != (1 if j==k else 0):
                raise Failure("Lagrange basis evaluation matrix is not identity")
    vanish = [1]
    for a in alpha:
        vanish = multiply_integer_polynomials(vanish,[-a,1])
    if len(vanish) != 28 or vanish[-1] != 1:
        raise Failure("integer vanishing polynomial is not monic degree 27")
    return basis,vanish


def product_form_carrier(
    name: str, ambient: frozenset[Permutation], subgroup: frozenset[Permutation],
    basis: list[list[int]], vanish: list[int], alpha: Sequence[int], alias_of: str | None = None,
) -> dict[str,Any]:
    action = CosetAction(ambient,subgroup,identity_first=True)
    sorted_ambient = sorted(ambient)
    labels = [action.mapping[g]+1 for g in sorted_ambient]
    degree = action.degree
    if action.mapping[IDENTITY] != 0 or sorted(set(labels)) != list(range(1,degree+1)):
        raise Failure("canonical right-coset labels invalid")
    counts = Counter(labels)
    if set(counts.values()) != {len(subgroup)}:
        raise Failure("right-coset label multiplicities invalid")
    values = list(range(1,degree+1))
    factors = [[(-v)%P,1] for v in values]
    spec = {
        "version":"c61-regular-lagrange-marker-v1",
        "action":"p(X_i)=X_{p(i)}; k(Delta_g_tilde)=Delta_tilde_(g*k^-1)",
        "coefficient_rule":"coefficient of Delta_g_tilde is the one-based canonical right-coset label of gH; H is coset 1",
        "basis_sha256":digest(basis),"integer_vanishing_polynomial_sha256":digest(vanish),
        "ambient_complete_group_sha256":group_sha(ambient),
        "subgroup_complete_group_sha256":group_sha(subgroup),
        "right_coset_label_vector_sha256":digest(labels),
        "marker":"Delta_g_tilde=Delta_g+Z*M_g; Z=product_i V(X_i); M_g=product_i X_i^g(i)",
    }
    # Exact content proof: the leading exponent (27+g(i))_i of Z*M_g can
    # occur in no Z*M_h with h!=g (coordinatewise h>=g and equal sums forces
    # h=g), and never in a Delta term (all coordinate degrees <=26).  Every
    # g in the first coset H has label 1, so an actual expanded monomial has
    # coefficient exactly 1.  Thus integral monomial content is exactly one.
    hostile_indices = sorted({0,len(sorted_ambient)//7,len(sorted_ambient)//3,len(sorted_ambient)//2,len(sorted_ambient)-1})
    samples = [{"ambient_index":i,"permutation_one_based":[v+1 for v in sorted_ambient[i]],"right_coset_label":labels[i]} for i in hostile_indices]
    return {
        "field":name,"alias_of":alias_of,"degree":degree,
        "subgroup_order":len(subgroup),"subgroup_complete_group_sha256":group_sha(subgroup),
        "carrier_spec_sha256":digest(spec),"carrier_spec":spec,
        "regular_basis_vector_count":len(labels),"right_coset_label_vector_sha256":digest(labels),
        "coefficient_range":[1,degree],"each_coefficient_multiplicity":len(subgroup),
        "hostile_label_samples":samples,
        "factorized_expression_terms":{"Delta_summands":len(ambient),"marker_summands":len(ambient),"expanded_coefficients_stored":False},
        "formal_total_degree":1080,"integral":True,"exact_monomial_content":1,
        "content_proof":"unique monic Z*M_g leading marker for every g; a label-1 marker coefficient is exactly 1",
        "delta_basis_Q_linear_independence":"the full mod-p orbit evaluation matrix is the 51840-by-51840 identity on the G-indexed subset; primitive integer relations reduce injectively",
        "formal_stabilizer_equals_embedded_subgroup":True,
        "stabilizer_side_proof":"k*c has coefficient label(u*k*H) at Delta_u_tilde; equality for every u iff k is in H",
        "identity_value_mod_p":1,"modular_distinct_value_count":degree,
        "sorted_values_sha256":digest(values),"complete_noncollision":True,
        "product_form_orbit_polynomial_factor_count":degree,
        "product_form_orbit_polynomial_sha256":digest(factors),
        "characteristic_zero_expanded_coefficients_claimed":False,
    }


def build_product_form_resolvents(
    context: dict[str,Any], type_groups: dict[int,tuple[frozenset[Permutation],frozenset[Permutation]]], alpha: Sequence[int]
) -> dict[str,Any]:
    W = context["groups"]["W"]
    basis,vanish = lagrange_basis(alpha)
    carriers: dict[str,Any] = {}
    for kind in range(1,9):
        carriers[f"E{kind}"] = product_form_carrier(f"E{kind}",W,type_groups[kind][0],basis,vanish,alpha)
    base_groups = {1:type_groups[1][1],2:type_groups[2][1],3:type_groups[3][1],4:W}
    for kind in range(1,5):
        carriers[f"C{kind}"] = product_form_carrier(f"C{kind}",W,base_groups[kind],basis,vanish,alpha)
    carriers["A40"] = product_form_carrier("A40",W,context["groups"]["Tplus"],basis,vanish,alpha,alias_of="C3")
    carriers["B80"] = product_form_carrier("B80",W,context["groups"]["Splus"],basis,vanish,alpha)
    if carriers["A40"]["carrier_spec_sha256"] != carriers["C3"]["carrier_spec_sha256"]:
        raise Failure("A40/C3 product-form carrier identity failed")
    expected_degrees = {**{f"E{i}":MIXED_EXPECTED[i][2] for i in range(1,9)},"C1":160,"C2":40,"C3":40,"C4":1,"A40":40,"B80":80}
    if {k:v["degree"] for k,v in carriers.items()} != expected_degrees:
        raise Failure("product-form carrier degrees changed")
    return {
        "construction":"source-owned regular Lagrange basis with invariant primitive-content marker",
        "split_prime":P,"labelled_root_count":27,"labelled_roots_sha256":digest(list(alpha)),
        "univariate_lagrange_basis_sha256":digest(basis),
        "integer_vanishing_polynomial_sha256":digest(vanish),
        "full_mod_p_orbit_evaluation_matrix":"identity",
        "all_14_advertised_carriers_reconstructed":len(carriers)==14,
        "carriers":carriers,
        "runtime_pilot_dependency":False,
    }


def verify_poly_record(name: str, poly: Poly) -> dict[str,Any]:
    degree,terms,hist,expected_sha,expected_value = FOURIER_EXPECTED[name]
    actual = {
        "degree":len(next(iter(poly))) if poly else 0,
        "term_count":len(poly),"coefficient_histogram":coefficient_histogram(poly),
        "carrier_sha256":poly_sha(poly),
    }
    if (actual["degree"],actual["term_count"],actual["coefficient_histogram"],actual["carrier_sha256"]) != (degree,terms,hist,expected_sha):
        raise Failure(f"Fourier carrier fingerprint changed: {name}")
    if expected_value is not None:
        actual["expected_identity_value_mod_p"] = expected_value
    return actual


def build_fourier(context: dict[str,Any], docs: dict[str,Any]) -> tuple[dict[str,Any],dict[str,Any],dict[str,Any]]:
    groups = context["groups"]
    w_gens = context["generators"]["W27_generators"]
    n_gens = context["generators"]["N_generators"]
    q = context["quotient_reps"]
    lam: Poly = {tuple(mon):int(coeff) for mon,coeff in docs["lambda_record"]["carrier"]}
    if poly_sha(lam) != LAMBDA_SHA256:
        raise Failure("lambda sparse carrier changed after parse")
    images = {label:poly_image(rep,lam) for label,rep in q.items()}
    if len({frozen_poly(v) for v in images.values()}) != 4:
        raise Failure("lambda quotient orbit is not four")
    chars = {
        "Hplus":{"1":1,"Hplus":1,"H0":-1,"H3":-1},
        "H0":{"1":1,"Hplus":-1,"H0":1,"H3":-1},
        "H3":{"1":1,"Hplus":-1,"H0":-1,"H3":1},
    }
    trace: Poly = {}
    raw: dict[str,Poly] = {key:{} for key in chars}
    for label,value in images.items():
        add_scaled(trace,value,1)
        for key,sign in chars.items():
            add_scaled(raw[key],value,sign[label])
    if raw["H0"]:
        raise Failure("R0 is nonzero")
    rplus = poly_div_exact(raw["Hplus"],2)
    r3 = poly_div_exact(raw["H3"],4)
    reconstruction = dict(trace)
    add_scaled(reconstruction,rplus,2)
    add_scaled(reconstruction,r3,4)
    if reconstruction != {m:4*c for m,c in lam.items()}:
        raise Failure("normalized Fourier reconstruction failed")
    r0 = poly_mul(rplus,r3)
    delta_plus = poly_mul(rplus,rplus)
    delta3 = poly_mul(r3,r3)
    dag = {"op":"mul","args":[poly_sha(delta_plus),poly_sha(delta3)]}
    if digest(dag) != "ed8974824f48cc65299443609c94db5ceab06efb8bed36f44b99ead311d28a66":
        raise Failure("delta0 factorized DAG changed")
    polynomials = {"Trace":trace,"rplus":rplus,"r3":r3,"r0":r0,"delta_plus":delta_plus,"delta3":delta3}
    records = {name:verify_poly_record(name,poly) for name,poly in polynomials.items()}
    alpha = docs["alpha"]
    values = {name:poly_eval(poly,alpha) for name,poly in polynomials.items()}
    for name in ("Trace","rplus","r3","r0"):
        if values[name] != FOURIER_EXPECTED[name][4]:
            raise Failure(f"identity split value changed: {name}")
    if not all(values[name] for name in ("Trace","rplus","r3")):
        raise Failure("rank-three component vanished")

    # Exact N-eigenrules.  Hplus/H0/H3 are the three index-two kernels in N.
    eigen = [("rplus",rplus,groups["Hplus"]),("r3",r3,groups["H3"]),("r0",r0,groups["H0"])]
    eigen_checks: list[dict[str,Any]] = []
    for label,poly,kernel in eigen:
        target = frozen_poly(poly)
        negative = tuple((mon,-coeff) for mon,coeff in target)
        signs: list[int] = []
        for generator in n_gens:
            expected = 1 if generator in kernel else -1
            image = frozen_poly(poly_image(generator,poly))
            if image != (target if expected==1 else negative):
                raise Failure(f"N eigenrule failed: {label}")
            signs.append(expected)
        eigen_checks.append({"carrier":label,"kernel":label.replace("rplus","Hplus").replace("r3","H3").replace("r0","H0"),"N_generator_signs":signs})
    if any(poly_image(g,trace) != trace for g in n_gens):
        raise Failure("Trace is not N-invariant")
    if any(poly_image(g,delta_plus) != delta_plus or poly_image(g,delta3) != delta3 for g in n_gens):
        raise Failure("Fourier radicands are not N-invariant")

    orbit_records = {
        "rplus":orbit_record(rplus,w_gens,alpha),
        "delta_plus":orbit_record(rplus,w_gens,alpha,square=True),
        "r3":orbit_record(r3,w_gens,alpha),
        "delta3":orbit_record(r3,w_gens,alpha,square=True),
        "r0":orbit_record(r0,w_gens,alpha),
        "delta0":orbit_record(r0,w_gens,alpha,square=True),
    }
    for name,record in orbit_records.items():
        count,value_sha,minpoly_sha = ORBIT_EXPECTED[name]
        if (
            record["formal_orbit_size"] != count
            or record["modular_distinct_value_count"] != count
            or record["sorted_values_sha256"] != value_sha
            or record["modular_minimal_polynomial_sha256"] != minpoly_sha
        ):
            raise Failure(f"Fourier orbit/noncollision changed: {name}")

    target = frozen_poly(rplus)
    negative = tuple((m,-c) for m,c in target)
    if any(frozen_poly(poly_image(element,rplus)) != target for element in groups["Splus"]):
        raise Failure("source-owned Splus does not fix rplus")
    if any(frozen_poly(poly_image(element,rplus)) not in (target,negative) for element in groups["Tplus"]):
        raise Failure("source-owned Tplus does not stabilize the rplus line")
    exact_orbit=len(poly_orbit(rplus,w_gens))
    sign_orbit=len(poly_orbit(rplus,w_gens,True))
    if exact_orbit != 80 or sign_orbit != 40:
        raise Failure("rplus orbit-stabilizer mismatch")
    if len(groups["Splus"])*exact_orbit != len(groups["W"]) or len(groups["Tplus"])*sign_orbit != len(groups["W"]):
        raise Failure("S/T containment plus orbit-size equality failed")

    fourier = {
        "lambda":{"carrier_sha256":LAMBDA_SHA256,"term_count":len(lam),"degree":len(next(iter(lam)))},
        "quotient_representatives_one_based":{k:[v+1 for v in item] for k,item in q.items()},
        "character_sign_table":chars,
        "raw_components":{
            "R0":{"zero":True,"term_count":0,"carrier_sha256":poly_sha(raw["H0"])},
            "Rplus":{"term_count":len(raw["Hplus"]),"carrier_sha256":poly_sha(raw["Hplus"]),"exact_content_divisor":2},
            "R3":{"term_count":len(raw["H3"]),"carrier_sha256":poly_sha(raw["H3"]),"exact_content_divisor":4},
        },
        "normalized_carriers":records,
        "delta0_factorized_dag":dag,"delta0_factorized_dag_sha256":digest(dag),
        "formal_identities":{
            "R0_equals_zero":True,"four_lambda_equals_Trace_plus_2rplus_plus_4r3":True,
            "r0_equals_rplus_times_r3":True,
            "delta0_equals_r0_squared_equals_delta_plus_times_delta3":True,
            "coefficientwise_division_by_2_and_4_exact":True,
        },
        "eigenrules":eigen_checks,
        "identity_values_mod_p":values,
    }
    span = {
        "split_prime":P,"component_order":["Trace","rplus","r3"],
        "identity_values":[values["Trace"],values["rplus"],values["r3"]],
        "all_three_components_nonzero":True,"three_distinct_V4_character_eigenspaces":True,
        "rational_character_idempotents_prove_independence":True,
        "orbit_span_dimension_over_M":3,
        "lambda_quotient_orbit_size":4,"lambda_stabilizer_in_N":"J",
        "lambda_generates_L_over_M":True,"lambda_is_normal_basis_generator_over_M":False,
        "normal_integral_basis_claimed":False,
    }
    extra = {"orbit_records":orbit_records,"Splus_exact_by_containment_and_orbit_stabilizer":True,"Tplus_exact_by_containment_and_orbit_stabilizer":True}
    return fourier,span,polynomials | {"lambda":lam,"raw_Rplus":raw["Hplus"],"raw_R3":raw["H3"]} | {"_extra":extra}  # type: ignore[dict-item]


def local_subgroups(context: dict[str,Any]) -> dict[str,Any]:
    gens = context["generators"]
    extra_gens = {key:one_to_zero(value) for key,value in GLOBAL_LOCAL_ARRAYS_ONE.items()}
    groups = {
        "I3":generated(gens["branch140_D_generators"]),
        "P3":generated(gens["branch140_P_generators"]),
        "Q3":generated(gens["branch140_Q_generators"]),
        "I5":generated(extra_gens["I5"]),"P5":generated(extra_gens["P5"]),
        "C3":generated(extra_gens["C3"]),"C2":generated(extra_gens["C2"]),
        "Cinf":generated(extra_gens["Cinf"]),
        "D140":generated(gens["branch140_D_generators"]),
        "I140":generated(gens["branch140_D_generators"]),
        "P140":generated(gens["branch140_P_generators"]),
        "Q140":generated(gens["branch140_Q_generators"]),
        "D206":generated(gens["branch206_D_generators"]),
        "I206":generated(gens["branch206_I_generators"]),
        "P206":generated(gens["branch206_P_generators"]),
        "Q206":generated(gens["branch206_Q_generators"]),
    }
    orders = {key:len(value) for key,value in groups.items()}
    expected = {"I3":18,"P3":9,"Q3":3,"I5":20,"P5":5,"C3":3,"C2":2,"Cinf":2,"D140":18,"I140":18,"P140":9,"Q140":3,"D206":36,"I206":18,"P206":9,"Q206":3}
    if orders != expected:
        raise Failure(f"local subgroup orders changed: {orders}")
    return {"groups":groups,"generators":extra_gens,"orders":orders}


def arithmetic_row(W: frozenset[Permutation], subgroup: frozenset[Permutation], locals_: dict[str,frozenset[Permutation]]) -> dict[str,Any]:
    action = CosetAction(W,subgroup)
    order = ["I3","P3","Q3","I5","P5","C3","C2","Cinf"]
    counts = [len(action.orbits(locals_[key])) for key in order]
    n = action.degree
    i3,p3,q3,i5,p5,c3,c2,cinf = counts
    v3_twice = 2*(n-i3)+(n-p3)+2*(n-q3)
    v5_four = 4*(n-i5)+3*(n-p5)
    if v3_twice%2 or v5_four%4:
        raise Failure("nonintegral conductor formula")
    exponents = [v3_twice//2,v5_four//4,n-c3,n-c2]
    signature = [2*cinf-n,n-cinf]
    if signature[0]+2*signature[1] != n or min(signature)<0:
        raise Failure("invalid signature")
    return {
        "degree":n,"orbit_vector_I3_P3_Q3_I5_P5_C3_C2_Cinf":counts,
        "signature_r1_r2":signature,"discriminant_sign":-1 if signature[1]%2 else 1,
        "absolute_exponents_3_5_PiA_PiB":exponents,
    }


def local_prime_rows(action: CosetAction,D: frozenset[Permutation],I: frozenset[Permutation],Pgroup: frozenset[Permutation],Q: frozenset[Permutation]) -> list[dict[str,Any]]:
    rows: list[dict[str,Any]] = []
    for prime_index,orbit in enumerate(action.orbits(D)):
        n = len(orbit)
        f = len(action.orbits(I,orbit))
        p_count = len(action.orbits(Pgroup,orbit))
        q_count = len(action.orbits(Q,orbit))
        if n%f:
            raise Failure("local e not integral")
        e = n//f
        numerator = 2*(n-f)+(n-p_count)+2*(n-q_count)
        if numerator%(2*f):
            raise Failure("local different not integral")
        d = numerator//(2*f)
        rows.append({"prime_index":prime_index,"coset_seed":min(orbit),"row_n_e_f_d":[n,e,f,d]})
    return rows


def collected_rows(rows: Sequence[dict[str,Any]]) -> list[dict[str,Any]]:
    counts = Counter(tuple(item["row_n_e_f_d"]) for item in rows)
    return [{"row_n_e_f_d":list(row),"multiplicity":counts[row]} for row in sorted(counts)]


def local_table_full(action: CosetAction,D: frozenset[Permutation],I: frozenset[Permutation],Pgroup: frozenset[Permutation],Q: frozenset[Permutation]) -> dict[str,Any]:
    rows = local_prime_rows(action,D,I,Pgroup,Q)
    collected = collected_rows(rows)
    degree_total = sum(item["multiplicity"]*item["row_n_e_f_d"][0] for item in collected)
    different_total = sum(item["multiplicity"]*item["row_n_e_f_d"][2]*item["row_n_e_f_d"][3] for item in collected)
    if degree_total != action.degree or len(rows) != sum(item["multiplicity"] for item in collected):
        raise Failure("local table totals failed")
    return {
        "degree_total":degree_total,"different_total":different_total,"factor_count":len(rows),
        "uncollected_prime_rows":rows,"collected_rows_with_multiplicity":collected,
    }


def relative_tower_full(
    action_N: CosetAction, field_actions: dict[str,CosetAction],
    D: frozenset[Permutation],I: frozenset[Permutation],Pgroup: frozenset[Permutation],Q: frozenset[Permutation],
) -> dict[str,Any]:
    field_order = ["Fplus","F0","F3","L"]
    quotient_degree = {"Fplus":2,"F0":2,"F3":2,"L":4}
    base_orbits = action_N.orbits(D)
    base_rows_raw = local_prime_rows(action_N,D,I,Pgroup,Q)
    coset_to_base: dict[int,int] = {}
    for index,orbit in enumerate(base_orbits):
        for coset in orbit:
            coset_to_base[coset] = index
    absolute_orbits = {name:field_actions[name].orbits(D) for name in field_order}
    absolute_rows = {name:local_prime_rows(field_actions[name],D,I,Pgroup,Q) for name in field_order}
    rows: list[dict[str,Any]] = []
    type_counts: Counter[str] = Counter()
    residue_mass: Counter[str] = Counter()
    norm_exp = Counter({name:0 for name in field_order})
    for base_index,(base_orbit,base_item) in enumerate(zip(base_orbits,base_rows_raw)):
        base = base_item["row_n_e_f_d"]
        relative: dict[str,list[int]] = {}
        for name in field_order:
            action = field_actions[name]
            selected: list[list[int]] = []
            for orbit,item in zip(absolute_orbits[name],absolute_rows[name]):
                images = {coset_to_base[action_N.mapping[action.representatives[c]]] for c in orbit}
                if len(images) != 1:
                    raise Failure("field prime maps to multiple base primes")
                if next(iter(images)) == base_index:
                    selected.append(item["row_n_e_f_d"])
            if not selected:
                raise Failure("base prime has no field prime above")
            rels: list[list[int]] = []
            for absolute in selected:
                if absolute[1]%base[1] or absolute[2]%base[2]:
                    raise Failure("relative e/f not integral")
                e_rel = absolute[1]//base[1]
                f_rel = absolute[2]//base[2]
                d_rel = absolute[3]-e_rel*base[3]
                rels.append([len(selected),e_rel,f_rel,d_rel])
            if any(r != rels[0] for r in rels):
                raise Failure("relative rows above base prime differ")
            if rels[0][0]*rels[0][1]*rels[0][2] != quotient_degree[name] or rels[0][3] < 0:
                raise Failure("relative degree/different failed")
            relative[name] = rels[0]
        exp = {name:relative[name][0]*relative[name][2]*relative[name][3] for name in field_order}
        ramified = {name for name in ("Fplus","F0","F3") if exp[name]>0}
        if not ramified:
            dtype = "trivial"
        else:
            if len(ramified)!=2:
                raise Failure("V4 row has wrong ramification population")
            split = ({"Fplus","F0","F3"}-ramified).pop()
            dtype = {"Fplus":"Hplus","F0":"H0","F3":"H3"}[split]
        checks = {
            "Fplus_F3_coprime":min(exp["Fplus"],exp["F3"])==0,
            "F0_product_law":exp["F0"]==exp["Fplus"]+exp["F3"],
            "L_square_law":exp["L"]==2*exp["F0"],
            "conductor_discriminant_law":exp["L"]==exp["Fplus"]+exp["F0"]+exp["F3"],
        }
        if not all(checks.values()):
            raise Failure("primewise ideal complementarity failed")
        multiplicity_weight = 1
        type_counts[dtype] += multiplicity_weight
        residue_mass[dtype] += base[2]
        for name in field_order:
            norm_exp[name] += base[2]*exp[name]
        rows.append({
            "base_prime_index":base_index,"base_coset_seed":min(base_orbit),
            "base_row_n_e_f_d":base,"relative_rows_g_e_f_d":relative,
            "relative_discriminant_exponents":exp,"V4_decomposition_inertia_type":dtype,
            **checks,
        })
    collected_counter = Counter(canonical({"base":r["base_row_n_e_f_d"],"relative":r["relative_rows_g_e_f_d"]}).decode("ascii") for r in rows)
    collected = [{"row":strict_json(key.encode("ascii")),"multiplicity":count} for key,count in sorted(collected_counter.items())]
    return {
        "base_prime_count":len(rows),"uncollected_base_prime_rows":rows,
        "collected_rows_with_multiplicity":collected,
        "V4_type_counts":{k:type_counts.get(k,0) for k in ["Hplus","H3","trivial","H0"]},
        "residue_degree_masses":{k:residue_mass.get(k,0) for k in ["Hplus","H3","trivial","H0"]},
        "relative_norm_exponents_Fplus_F0_F3_L":[norm_exp[name] for name in field_order],
        "all_rows_verify_ideal_laws":True,
    }


def build_diamond(context: dict[str,Any], mixed_rows: list[dict[str,Any]], type_groups: dict[int,tuple[frozenset[Permutation],frozenset[Permutation]]], polynomials: dict[str,Any]) -> tuple[dict[str,Any],dict[str,Any]]:
    groups=context["groups"];gens=context["generators"]
    W,N,Hplus,S,T = groups["W"],groups["N"],groups["Hplus"],groups["Splus"],groups["Tplus"]
    if not (Hplus < S < T and N < T and S.intersection(N)==Hplus):
        raise Failure("diamond subgroup containments/intersection failed")
    join = generated(tuple(context["Splus_generators"])+tuple(gens["N_generators"]))
    set_product = {compose(s,n) for s in S for n in N}
    if join != T or set_product != set(T):
        raise Failure("diamond join/set-product failed")
    normS = normalizer(W,S,context["Splus_generators"])
    normT = normalizer(W,T,context["Tplus_generators"])
    coreS = core(gens["W27_generators"],S)
    coreT = core(gens["W27_generators"],T)
    if normS != T or normT != T or len(coreS)!=1 or len(coreT)!=1:
        raise Failure("diamond normalizer/core failed")
    seed149 = next(r for r in mixed_rows if r["seed"]==149)
    if seed149["representative_one_based"] != G149_ONE:
        raise Failure("canonical seed-149 representative changed")
    inter149,join149 = type_groups[3]
    if join149 != T or group_sha(join149)!=TPLUS_SHA256 or len(inter149)!=27:
        raise Failure("Tmix is not exact embedded Tplus")
    if sum(r["simple_factor_degree"]==1920 for r in mixed_rows)!=1:
        raise Failure("mixed degree-1920 factor not unique")
    diamond = {
        "subgroup_orders":{"Hplus":len(Hplus),"N":len(N),"Splus":len(S),"Tplus":len(T)},
        "subgroup_hashes":{"Hplus":group_sha(Hplus),"N":group_sha(N),"Splus":group_sha(S),"Tplus":group_sha(T)},
        "containments":{"Hplus_strict_Splus":True,"Splus_strict_Tplus":True,"N_strict_Tplus":True},
        "Splus_intersection_N_equals_Hplus":True,
        "generated_Splus_N_equals_Tplus":True,"set_product_Splus_N_equals_Tplus":True,
        "normalizers":{"N_G_Splus_order":len(normS),"N_G_Splus_sha256":group_sha(normS),"N_G_Tplus_order":len(normT),"N_G_Tplus_sha256":group_sha(normT)},
        "cores":{"Splus_order":len(coreS),"Tplus_order":len(coreT)},
        "fixed_fields":{"A40":"Q(delta_plus)=K^Tplus","B80":"Q(rplus)=K^Splus","M160":"K^N","Fplus320":"K^Hplus"},
        "degrees_A40_B80_M160_Fplus320":[40,80,160,320],
        "B80_intersection_M160_equals_A40":True,"B80_compositum_M160_equals_Fplus320":True,
        "Gal_B80_over_A40_order":2,"Aut_Q_A40_order":len(normT)//len(T),"Aut_Q_B80_order":len(normS)//len(S),
        "all_four_normal_closures_equal_K":all(len(core(gens["W27_generators"],h))==1 for h in [T,S,N,Hplus]),
        "negative_gates":{"Q_rplus_is_Fplus":False,"Q_delta_plus_is_M":False,"M_rplus_equals_Fplus":True},
        "other_characters":{"F3":"M(r3)=M(sqrt(delta3))","F0":"M(r0)=M(sqrt(delta0))","square_class_relation":"[delta0]=[delta_plus][delta3]"},
    }
    bridge = {
        "canonical_enumeration":"lexicographically sorted W, least unseen right Hminus cosets, Hplus left orbits",
        "mixed_rows":mixed_rows,"mixed_row_count":len(mixed_rows),
        "seed149":149,"g149_one_based":G149_ONE,
        "intersection_order":len(inter149),"intersection_sha256":group_sha(inter149),"factor_degree":len(W)//len(inter149),
        "Tmix_order":len(join149),"Tmix_sha256":group_sha(join149),
        "Tplus_order":len(T),"Tplus_sha256":group_sha(T),
        "exact_embedded_element_set_equality_Tmix_Tplus":join149==T,
        "order_hash_or_conjugacy_alone_used":False,
        "unique_mixed_degree1920_row":True,
        "self_P3_substitute_hash_rejected":"263f31237e6f5111f76fd3470b6936a1a314020255c22eab55cece395c2adeb5",
    }
    return bridge,diamond


def build_global_and_local(context: dict[str,Any], type_groups: dict[int,tuple[frozenset[Permutation],frozenset[Permutation]]]) -> tuple[dict[str,Any],dict[str,Any]]:
    W=context["groups"]["W"]
    local_context=local_subgroups(context);lg=local_context["groups"]
    field_groups: dict[str,frozenset[Permutation]] = {f"E{i}":type_groups[i][0] for i in range(1,9)}
    field_groups.update({"C1":type_groups[1][1],"C2":type_groups[2][1],"C3":type_groups[3][1],"C4":W,"B80":context["groups"]["Splus"]})
    arithmetic = {name:arithmetic_row(W,subgroup,lg) for name,subgroup in field_groups.items()}
    for name,expected in GLOBAL_EXPECTED.items():
        degree,signature,sign,exponents,_relative=expected
        row=arithmetic[name]
        if (row["degree"],row["signature_r1_r2"],row["discriminant_sign"],row["absolute_exponents_3_5_PiA_PiB"]) != (degree,signature,sign,exponents):
            raise Failure(f"global arithmetic changed: {name}")
    relative: dict[str,list[int]]={}
    base_for={1:"C1",2:"C2",3:"C3",4:"C4",5:"C4",6:"C4",7:"C4",8:"C4"}
    for i in range(1,9):
        upper=arithmetic[f"E{i}"];lower=arithmetic[base_for[i]]
        q=upper["degree"]//lower["degree"]
        vector=[a-q*b for a,b in zip(upper["absolute_exponents_3_5_PiA_PiB"],lower["absolute_exponents_3_5_PiA_PiB"])]
        if vector != GLOBAL_EXPECTED[f"E{i}"][4] or min(vector)<0:
            raise Failure(f"mixed relative discriminant changed: E{i}")
        relative[f"E{i}_over_{base_for[i]}"]=vector

    # Recompute the remaining diamond fields from their embedded groups.
    A=arithmetic["C3"];B=arithmetic["B80"]
    M=arithmetic_row(W,context["groups"]["N"],lg)
    Fplus=arithmetic_row(W,context["groups"]["Hplus"],lg)
    def relvec(upper:dict[str,Any],lower:dict[str,Any])->list[int]:
        q=upper["degree"]//lower["degree"]
        return [a-q*b for a,b in zip(upper["absolute_exponents_3_5_PiA_PiB"],lower["absolute_exponents_3_5_PiA_PiB"])]
    diamond_vectors={
        "d_B80_over_A40":relvec(B,A),"d_M160_over_A40":relvec(M,A),
        "d_Fplus320_over_B80":relvec(Fplus,B),"d_Fplus320_over_A40":relvec(Fplus,A),
        "d_Fplus320_over_M160":relvec(Fplus,M),
    }
    expected_diamond={"d_B80_over_A40":[4,0,0,0],"d_M160_over_A40":[8,4,0,20],"d_Fplus320_over_B80":[8,8,0,40],"d_Fplus320_over_A40":[24,8,0,40],"d_Fplus320_over_M160":[8,0,0,0]}
    if diamond_vectors != expected_diamond:
        raise Failure("diamond relative discriminants changed")
    via_B=[4*x+y for x,y in zip(diamond_vectors["d_B80_over_A40"],diamond_vectors["d_Fplus320_over_B80"])]
    via_M=[2*x+y for x,y in zip(diamond_vectors["d_M160_over_A40"],diamond_vectors["d_Fplus320_over_M160"])]
    if via_B != via_M or via_B != diamond_vectors["d_Fplus320_over_A40"]:
        raise Failure("diamond discriminant routes disagree")
    global_evidence={
        "filtration_order":["I3","P3","Q3","I5","P5","C3","C2","Cinf"],
        "filtration_tom_locators":[140,72,7,147,23,6,2,5],
        "filtration_group_orders":local_context["orders"],
        "prime_products":{"PiA":"181*997*2346241","PiB":"283*1801*14932047182473291995860108491583652133938007263719"},
        "exact_ramified_support":[3,5,181,283,997,1801,2346241,"14932047182473291995860108491583652133938007263719"],
        "fields":arithmetic,"mixed_relative_discriminant_norm_vectors":relative,
        "diamond_fields":{"A40":A,"B80":B,"M160":M,"Fplus320":Fplus},
        "diamond_relative_discriminant_norm_vectors":diamond_vectors,
        "diamond_route_via_B80":via_B,"diamond_route_via_M160":via_M,
        "field_discriminants_distinct_from_product_form_polynomial_and_order_discriminants":True,
        "maximal_order_claimed":False,
    }

    branches={"ToM140":(lg["D140"],lg["I140"],lg["P140"],lg["Q140"]),"ToM206":(lg["D206"],lg["I206"],lg["P206"],lg["Q206"])}
    local_fields: dict[str,Any]={}
    actions={name:CosetAction(W,subgroup) for name,subgroup in field_groups.items()}
    for branch,(D,I,Pgroup,Q) in branches.items():
        local_fields[branch]={name:local_table_full(action,D,I,Pgroup,Q) for name,action in actions.items()}
        for name,table in local_fields[branch].items():
            if table["different_total"] != arithmetic[name]["absolute_exponents_3_5_PiA_PiB"][0]:
                raise Failure(f"local/global p3 mismatch {branch} {name}")
    expected_factor_counts={
        "ToM140":{"E":[56,72,160,188,204,552,968,2880],"C":[22,10,7,1],"B80":10},
        "ToM206":{"E":[28,36,80,94,102,276,484,1440],"C":[11,5,5,1],"B80":8},
    }
    for branch in branches:
        actual={"E":[local_fields[branch][f"E{i}"]["factor_count"] for i in range(1,9)],"C":[local_fields[branch][f"C{i}"]["factor_count"] for i in range(1,5)],"B80":local_fields[branch]["B80"]["factor_count"]}
        if actual != expected_factor_counts[branch]:
            raise Failure(f"local factor counts changed: {branch}")

    # C60 V4 relative tower, reconstructed from released arrays and both branches.
    v4_groups={"Fplus":context["groups"]["Hplus"],"F0":context["groups"]["H0"],"F3":context["groups"]["H3"],"L":context["groups"]["J"]}
    action_N=CosetAction(W,context["groups"]["N"])
    v4_actions={name:CosetAction(W,h) for name,h in v4_groups.items()}
    relative_towers={branch:relative_tower_full(action_N,v4_actions,*groups4) for branch,groups4 in branches.items()}
    expected_types={"ToM140":{"Hplus":8,"H3":8,"trivial":6,"H0":0},"ToM206":{"Hplus":4,"H3":4,"trivial":3,"H0":0}}
    for branch,tower in relative_towers.items():
        if tower["V4_type_counts"] != expected_types[branch] or tower["residue_degree_masses"] != {"Hplus":8,"H3":8,"trivial":6,"H0":0} or tower["relative_norm_exponents_Fplus_F0_F3_L"] != [8,16,8,32]:
            raise Failure(f"relative V4 branch summary changed: {branch}")
        for row in tower["uncollected_base_prime_rows"]:
            for rel in row["relative_rows_g_e_f_d"].values():
                if rel[3]>0 and (rel[1],rel[3])!=(2,1):
                    raise Failure("ramified relative row is not tame e2 d1")

    real_M=M["signature_r1_r2"][0]
    abs_F={name:arithmetic_row(W,h,lg) for name,h in v4_groups.items()}
    infinity={
        "real_places_of_M":real_M,
        "V4_type_counts":{"Hplus":abs_F["Fplus"]["signature_r1_r2"][0]//2,"H3":abs_F["F3"]["signature_r1_r2"][0]//2,"H0":abs_F["F0"]["signature_r1_r2"][0]//2},
        "Fplus_F3_real_splitting_sets_complementary":True,
        "every_real_completion_of_L_is_C_times_C":abs_F["L"]["signature_r1_r2"][0]==0,
    }
    if infinity["V4_type_counts"] != {"Hplus":8,"H3":8,"H0":0} or real_M!=16:
        raise Failure("archimedean complementarity changed")
    local_evidence={
        "retained_branches":["ToM140","ToM206"],"branch_selected":False,
        "absolute_local_tables":local_fields,"expected_factor_counts":expected_factor_counts,
        "V4_relative_towers_over_M":relative_towers,
        "ideal_equalities":["gcd(d_Fplus/M,d_F3/M)=1","d_F0/M=d_Fplus/M*d_F3/M","d_L/M=d_Fplus/M*d_F0/M*d_F3/M=(d_F0/M)^2"],
        "all_primewise_ideal_laws":True,"all_ramified_relative_rows_tame_e2_d1":True,
        "archimedean_complementarity":infinity,
        "local_fields_classified_by_nefd_rows":False,
    }
    return global_evidence,local_evidence


def payload_hash(document: dict[str,Any]) -> str:
    projection = {key:value for key,value in document.items() if key != "payload_sha256"}
    return digest(projection)


def exact_top_keys(document: dict[str,Any]) -> None:
    if type(document) is not dict or set(document) != set(TOP_KEYS):
        raise Failure("evidence top-level keys changed")


def build_candidate() -> dict[str,Any]:
    authority,docs=bind_authority()
    context=build_groups(docs["arrays"])
    mixed_rows,type_groups=enumerate_mixed(context)
    product_resolvents=build_product_form_resolvents(context,type_groups,docs["alpha"])
    fourier,span,poly=build_fourier(context,docs)
    bridge,diamond=build_diamond(context,mixed_rows,type_groups,poly)
    global_evidence,local_evidence=build_global_and_local(context,type_groups)
    orbit_records=poly["_extra"]["orbit_records"]
    scope={"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER"}
    scope.update({key:False for key in SCOPE_KEYS})
    evidence: dict[str,Any]={
        "schema_id":"hcs-c61-resolvent-evidence-v1",
        "schema_sha256":digest(SCHEMA_SPEC),
        "authority":authority,
        "conventions":{
            "group_arrays":"one-based images on 27 labels; internal permutations zero-based",
            "sparse_monomials":"zero-based sorted tuples; zero coefficients deleted",
            "composition":"left after right",
            "polynomial_action":"p(X_i)=X_p(i)",
            "tensor_cosets":"canonical right cosets gH with left Hplus action",
            "product_form_cosets":"right cosets gH; identity coset first then least unseen element",
            "canonical_json":"UTF-8/ASCII, sorted keys, compact separators, one trailing newline for files",
            "exact_arithmetic_only":True,"split_prime":P,
        },
        "GAF0_released_authority_rebind":{
            "status":"PASS","all_released_and_formal_inputs_byte_rebound":True,
            "released_P60_bytes_from_immutable_git_objects":True,
            "installed_formal_target_tuple_reconstructed":True,
            "external_nonproject_files_read_at_runtime":False,
            "group_orders":context["orders"],"source_owned_quotient_Splus_Tplus_literals_reconstructed":True,
            "target_selection_pilots_read_at_runtime":False,
        },
        "GAF1_fourier_carrier_dag":fourier,
        "GAF2_orbit_span_and_nonnormality":span,
        "GAF3_stabilizers_and_noncollision":{
            "product_form_mixed_base_A_B_resolvents":product_resolvents,
            "fourier_formal_and_evaluated_orbits":orbit_records,
            "Splus":{"order":len(context["groups"]["Splus"]),"complete_group_sha256":group_sha(context["groups"]["Splus"]),"contained_in_exact_stabilizer_and_equal_by_orbit_stabilizer":True},
            "Tplus":{"order":len(context["groups"]["Tplus"]),"complete_group_sha256":group_sha(context["groups"]["Tplus"]),"contained_in_line_stabilizer_and_equal_by_sign_orbit_stabilizer":True},
            "all_product_form_carriers_true_expanded_monomial_content_one":True,
            "all_advertised_product_form_carriers_complete_noncollision":True,
            "expanded_characteristic_zero_coefficients_claimed":False,
        },
        "GAF4_mixed_type3_exact_bridge":bridge,
        "GAF5_fixed_field_diamond":diamond,
        "GAF6_global_arithmetic":global_evidence,
        "GAF7_both_local_branches_and_ideal_laws":local_evidence,
        "independence_contract":{
            "producer_source_sha256":authority["source_files"]["producer"]["sha256"],
            "checker_source_sha256":authority["source_files"]["checker"]["sha256"],
            "checker_imports_producer":False,"shared_mathematical_helpers":False,
            "shared_inputs":"released authority and independently duplicated expected literals only",
            "producer_two_run_replay":True,"checker_attestation_two_run_equal":False,
            "checker_attestation":None,
        },
        "scope_nonclaims":scope,
        "status":{
            "resolver_component_status":"PRODUCER_PASS_CHECKER_PENDING",
            "G3_product_form_resolvents":"PASS","G4_fourier_diamond":"PASS",
            "G5_global_arithmetic":"PASS","G6_both_local_branches":"PASS",
            "integrated_C61_status":"IMPLEMENTATION_PENDING","paper_status":"PAPER_PENDING",
            "release_status":"NOT_RELEASED","promotion_authorized":False,
        },
        "payload_sha256":"",
    }
    exact_top_keys(evidence)
    if len(scope)!=31 or any(scope[key] is not False for key in SCOPE_KEYS):
        raise Failure("scope firewall changed")
    evidence["payload_sha256"]=payload_hash(evidence)
    return evidence


def build_resolver_candidate() -> dict[str,Any]:
    """Public integration API: build the unattested deterministic component."""
    return build_candidate()


def checker_command(evidence_path:Path) -> list[str]:
    _repo,_project,source=canonical_layout();checker=source.with_name("c61_checker_resolvent.py")
    return [
        sys.executable,"-B",str(checker),"--attest-for",str(evidence_path),
    ]


def invoke_checker(candidate:dict[str,Any],evidence_path:Path) -> dict[str,Any]:
    completed=subprocess.run(
        checker_command(evidence_path),input=canonical_output(candidate),stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,check=False,
        env={"PATH":os.environ.get("PATH", ""),"PYTHONDONTWRITEBYTECODE":"1"},
    )
    if completed.returncode or completed.stderr:
        raise Failure("independent checker attestation failed: "+completed.stderr.decode("utf-8","replace")[:1000])
    attestation=strict_json(completed.stdout)
    expected_keys={"schema_id","candidate_payload_sha256","checker_source_sha256","independent_semantic_checks","hostile_mutations_rejected","targeted_semantic_mutations_rejected","strict_parser_cases_rejected","path_toctou_cases_rejected","no_producer_import","status"}
    if type(attestation) is not dict or set(attestation)!=expected_keys:
        raise Failure("checker attestation shape changed")
    if (
        attestation["schema_id"]!="hcs-c61-resolvent-checker-attestation-v1"
        or attestation["candidate_payload_sha256"]!=candidate["payload_sha256"]
        or attestation["checker_source_sha256"]!=candidate["authority"]["source_files"]["checker"]["sha256"]
        or attestation["no_producer_import"] is not True or attestation["status"]!="PASS"
    ):
        raise Failure("checker attestation semantics changed")
    return attestation


def finalize(candidate: dict[str,Any],attestation: dict[str,Any]) -> dict[str,Any]:
    final=copy.deepcopy(candidate)
    final["independence_contract"]["checker_attestation_two_run_equal"]=True
    final["independence_contract"]["checker_attestation"]=attestation
    final["status"]["resolver_component_status"]="RESOLVER_COMPONENT_PASS"
    final["payload_sha256"]=payload_hash(final)
    return final


def validate_evidence_document(document:dict[str,Any])->dict[str,Any]:
    """Public object validator for integration after neutral JSON parsing.

    No checker module is imported: this producer source reconstructs its fresh
    candidate, validates the embedded checker-attestation contract, finalizes
    it, and requires exact object equality.
    """
    exact_top_keys(document)
    if document.get("schema_id")!="hcs-c61-resolvent-evidence-v1" or document.get("schema_sha256")!=digest(SCHEMA_SPEC) or document.get("payload_sha256")!=payload_hash(document):
        raise Failure("resolver evidence schema/payload invalid")
    contract=document.get("independence_contract")
    if type(contract) is not dict or contract.get("checker_attestation_two_run_equal") is not True:
        raise Failure("resolver final independence contract invalid")
    attestation=contract.get("checker_attestation")
    candidate=build_candidate()
    expected_keys={"schema_id","candidate_payload_sha256","checker_source_sha256","independent_semantic_checks","hostile_mutations_rejected","targeted_semantic_mutations_rejected","strict_parser_cases_rejected","path_toctou_cases_rejected","no_producer_import","status"}
    if type(attestation) is not dict or set(attestation)!=expected_keys or attestation.get("schema_id")!="hcs-c61-resolvent-checker-attestation-v1" or attestation.get("candidate_payload_sha256")!=candidate["payload_sha256"] or attestation.get("checker_source_sha256")!=candidate["authority"]["source_files"]["checker"]["sha256"] or attestation.get("no_producer_import") is not True or attestation.get("status")!="PASS":
        raise Failure("resolver checker attestation invalid")
    expected=finalize(candidate,attestation)
    if canonical(document)!=canonical(expected):
        raise Failure("resolver evidence differs from fresh source reconstruction")
    return {"schema_id":"hcs-c61-resolvent-object-validation-v1","payload_sha256":document["payload_sha256"],"candidate_payload_sha256":candidate["payload_sha256"],"status":"PASS","release_status":"NOT_RELEASED"}


def parser() -> argparse.ArgumentParser:
    p=argparse.ArgumentParser(description="Build the exact C61 resolver component evidence")
    destination=p.add_mutually_exclusive_group(required=True)
    destination.add_argument("--output",help="new canonical staged evidence")
    destination.add_argument("--check-existing",help="byte-identical canonical staged replay")
    return p


def main() -> None:
    args=parser().parse_args()
    writing=args.output is not None
    selected=args.output if writing else args.check_existing
    output,stage,stage_identity=staged_evidence_path(selected,must_exist=not writing)
    evidence_before=stable_read(output,25_000_000) if not writing else None
    runtime_before=runtime_input_snapshot()
    authority_before,_=bind_authority()
    started=time.perf_counter()
    assert_stage(stage,stage_identity)
    first=build_candidate()
    assert_stage(stage,stage_identity)
    second=build_candidate()
    if canonical(first)!=canonical(second):
        raise Failure("producer two-run replay differs")
    if first["authority"]!=authority_before:raise Failure("authority changed around producer replay")
    assert_stage(stage,stage_identity)
    attest1=invoke_checker(first,output)
    assert_stage(stage,stage_identity)
    attest2=invoke_checker(first,output)
    if canonical(attest1)!=canonical(attest2):
        raise Failure("checker two-run attestation differs")
    final=finalize(first,attest1)
    final_bytes=canonical_output(final)
    authority_after,_=bind_authority()
    if authority_after!=authority_before or final["authority"]!=authority_after:raise Failure("authority/source/formal bytes changed around children")
    if runtime_input_snapshot()!=runtime_before:raise Failure("installed authority/source/results identity changed around children")
    assert_stage(stage,stage_identity)
    if writing:
        stage_identity=atomic_write(output,final_bytes,stage,stage_identity);mode="write"
    else:
        assert evidence_before is not None
        evidence_after=stable_read(output,25_000_000)
        if evidence_after!=evidence_before or evidence_after[0]!=final_bytes:raise Failure("existing evidence changed or differs from fresh replay")
        mode="check-existing"
    if runtime_input_snapshot()!=runtime_before:raise Failure("installed authority/source/results identity changed around final write/replay")
    assert_stage(stage,stage_identity)
    print(json.dumps({
        "output":str(output),"output_sha256":sha256_bytes(canonical_output(final)),
        "payload_sha256":final["payload_sha256"],"status":final["status"]["resolver_component_status"],
        "independent_checker":attest1["status"],"release_status":"NOT_RELEASED","mode":mode,
        "elapsed_seconds":round(time.perf_counter()-started,6),
    },sort_keys=True))


if __name__=="__main__":
    main()
