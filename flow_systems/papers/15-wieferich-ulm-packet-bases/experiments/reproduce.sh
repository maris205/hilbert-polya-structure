#!/bin/sh
# Sole eventual Paper 15R entry.  Source creation is not an execution receipt.
set -eu

fail_entry() {
    printf '%s\n' "$1" >&2
    exit "$2"
}

CURRENT_RUN_PROFILE_ACCEPTED=false
PROFILE_HASH_IS_EVIDENCE=false
[ "$CURRENT_RUN_PROFILE_ACCEPTED:$PROFILE_HASH_IS_EVIDENCE" = true:false ] || fail_entry E_POSSESSION_UNAVAILABLE 1

[ "${P15R_REPRO_ACTIVE-}" != 1 ] || fail_entry E_RECURSIVE_ENTRY 73
[ ! -L "$0" ] || fail_entry E_SYMLINK 1

case "$0" in
    /*) entry_path=$0 ;;
    */*) entry_path=$PWD/$0 ;;
    *) fail_entry E_USAGE 2 ;;
esac

entry_parent=${entry_path%/*}
[ "$entry_parent" != "$entry_path" ] || fail_entry E_USAGE 2
script_dir=$(CDPATH= cd -P -- "$entry_parent" && pwd -P) || fail_entry E_USAGE 2
package_root=$(CDPATH= cd -P -- "$script_dir/.." && pwd -P) || fail_entry E_USAGE 2
repository_root=$(CDPATH= cd -P -- "$package_root/../.." && pwd -P) || fail_entry E_USAGE 2

case "${P15R_TEST_CONTEXT-}:${P15R_TEST_CREATE_POST_CACHE-}:${P15R_TEST_ABORT_AFTER_FRESH_A-}:${P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN-}:${P15R_TEST_REPLACE_CANONICAL_ROOT-}:${P15R_TEST_REPLACE_MUTATION_ROOT-}:${P15R_TEST_REPLACE_P25_ROOT-}:${P15R_TEST_REPLACE_LOCK_ACQUIRING-}:${P15R_TEST_REPLACE_LOCK_CLEANING-}" in
    :::::::: ) ;;
    *) fail_entry E_USAGE 2 ;;
esac

export P15R_REPRO_ACTIVE=1 LC_ALL=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
cd -- "$package_root" || fail_entry E_USAGE 2

exec python3 -B - "$package_root" "$repository_root" "$entry_path" <<'P15R_POSSESSION_PY_V2_END'
from __future__ import annotations

import array
import ctypes
import errno
import fcntl
import hashlib
import json
import os
import re
import resource
import select
import signal
import socket
import stat
import struct
import sys
import time
from dataclasses import dataclass, field, replace
from typing import Callable, Iterable, Mapping, Sequence


PACKAGE_PATH = sys.argv[1]
REPOSITORY_PATH = sys.argv[2]
ENTRY_PATH = sys.argv[3]
E_POSSESSION = "E_POSSESSION_UNAVAILABLE"
MAX_FRAME = 4096
WORKER_STREAM_BYTE_CEILING = 16_777_216
CARRIER_SCOPE_ID = "P15R_V14_BIDIRECTIONAL_LAUNCHER_REAPED_PRIVILEGE_DROP_RELEASE_GUARDIAN_READY_GUARDIAN_READY_ACK_BOOTSTRAP_SEALED_AND_PRE_DIRECTIONAL_CUT_OLD_FORM_EXTRA_WITNESSES"
C14_COORDINATES = ("RE","YE","AE","SS","E_PG","E_GP")
OLD_BOUNDARY_FORMS = ("LAUNCHER_REAPED","PRIVILEGE_DROP_RELEASE","GUARDIAN_READY")
C14_VECTORS = (
    (0,0,0,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1),(0,0,0,0,1,1),
    (1,0,0,0,0,0),(1,0,0,0,1,0),(1,0,0,0,0,1),(1,0,0,0,1,1),
    (1,1,0,0,0,0),(1,1,0,0,1,0),(1,1,0,0,0,1),(1,1,0,0,1,1),
    (1,1,1,0,0,0),(1,1,1,0,0,1),(1,1,1,1,0,0),
)
C14_CLASSES = (
    ("PRE_RELEASE_COMMIT_FAILURE",)*4
    + ("RELEASE_COMMITTED_PRE_READY_COMMIT_FAILURE",)*4
    + ("READY_COMMITTED_PRE_ACK_COMMIT_FAILURE",)*4
    + ("ACK_COMMITTED_PRE_SEAL_COMMIT_FAILURE",)*2
    + ("BOOTSTRAP_SEALED_COMMIT",)
)
C14_ROWS = tuple(zip(C14_VECTORS,C14_CLASSES))
RAW17_LABELS = ("MISSING","MALFORMED","DUPLICATE","REPLAY","WRONG_SESSION","WRONG_G_IDENTITY","WRONG_CGROUP","WRONG_ATTESTATION","WRONG_DIRECTION","WRONG_STATE","REORDERED","PARTIAL","EOF","TIMEOUT","P_CRASH","G_CRASH","TRANSPORT_ERROR")
RAW17_PRECEDENCE = ("PARTIAL","DUPLICATE","REPLAY","WRONG_DIRECTION","REORDERED","WRONG_STATE","MALFORMED","WRONG_SESSION","WRONG_G_IDENTITY","WRONG_CGROUP","WRONG_ATTESTATION","TRANSPORT_ERROR","EOF","P_CRASH","G_CRASH","TIMEOUT","MISSING")
Q_PHASES = ("PRE_RE","POST_RE_PRE_YE","POST_YE_PRE_AE","POST_AE_PRE_SS")
HOOK_CUSTODY_PROFILE_SHA256 = "1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1"
HOOK_CUSTODY_PROFILE_LINES = (
    "claim_kind=UNVERIFIED_TRUSTED_DEPLOYMENT_MODEL_AXIOM","evidence_effect=NONE","runtime_self_attestation=FORBIDDEN","claim_effect=NARROW_PLATFORM_MODEL_ONLY",
    "kernel_git_commit=8bb7eca972ad531c9b149c0a51ab43a417385813","kernel_tree=EXACT_UPSTREAM_UNPATCHED","abi=LINUX_X86_64_LITTLE_ENDIAN_LP64","config_security_network=N","config_cgroup_bpf=N","config_bpf_syscall=N","config_modules=N","config_livepatch=N","config_kprobes=N","config_ftrace=N",
    "kernel_text_or_data_mutation=FORBIDDEN_FOR_WINDOW","module_load=IMPOSSIBLE_FOR_WINDOW","livepatch=IMPOSSIBLE_FOR_WINDOW","kprobe_ftrace_bpf_tracing=IMPOSSIBLE_FOR_WINDOW","classic_socket_filter_claim=DELEGATED_TO_MECHANICAL_ENDPOINT_RECEIPT","cgroup_inet_ingress_af_unix=RETURN_ZERO_NO_REJECT_NO_TRIM","security_sock_rcv_skb=STUB_RETURN_ZERO_NO_TRIM","security_socket_recvmsg=STUB_ALLOW_SOLE_RECEIVER","security_socket_getsockopt_setsockopt=STUB_ALLOW_NO_REWRITE","cgroup_getsockopt_setsockopt=ABSENT_NO_SHORT_CIRCUIT_NO_REWRITE","other_receive_reject_or_trim_hook=ABSENT_FOR_WINDOW","ptrace_or_process_vm_control_of_p_or_g=ABSENT_FOR_WINDOW","seccomp_user_notif_of_p_or_g=ABSENT_FOR_WINDOW","syscall_emulation_of_p_or_g=ABSENT_FOR_WINDOW","sender_skb_pfmemalloc=0","endpoint_hidden_or_pending_references_at_holder_freeze=NONE",
    "endpoint_additional_reference_policy_after_respective_holder_freeze=EP_P_NONE_UNTIL_WINDOW_END_EP_G_NONE_UNTIL_G_EXACT_BOOTSTRAP_SEALED_FULL_RETURN_THEN_ONLY_TRUSTED_CHILD_TRANSIENT_ALIAS_CLOSED_BEFORE_ANY_ENDPOINT_IO_DUPLICATION_SHUTDOWN_TRANSFER_REGISTRATION_OR_BARRIER_RELEASE","endpoint_other_reader_sender_peeker_drainer_or_shutdown=ABSENT_FOR_WINDOW","initial_userns_admin_custody=EXCLUSIVE_TRUSTED_INITIAL_ROOT_P_FOR_WINDOW","owner_behavior=TRUSTED_NON_BYZANTINE_P_G_AND_FIXED_FIRST_INSTRUCTION_CHILD_ENDPOINT_CLOSE_STUB",f"carrier_scope_id={CARRIER_SCOPE_ID}","profile_window_begin=BEFORE_FIRST_ACTUAL_ENDPOINT_FILTER_OR_IDENTITY_SYSCALL","carrier_window_begin=AFTER_BOTH_ENDPOINT_FILTER_LOCK_AND_HOLDER_FREEZE_BEFORE_FIRST_IN_SCOPE_SEND","window_end=AFTER_BOTH_G_EXACT_BOOTSTRAP_SEALED_FULL_RETURN_AND_P_EXACT_BOOTSTRAP_SEALED_RECEIPT_VALIDATION_OR_AFTER_TERMINAL_DRAIN_CLASSIFICATION_NO_FURTHER_IN_SCOPE_SEND_AND_BOTH_ACTUAL_ENDPOINTS_CLOSED","future_acceptance_authority=SEPARATE_SUCCESSOR_EXECUTION_GATE_ONLY","future_acceptance_binding=EXACT_PROFILE_AND_EXECUTION_WINDOW_CLASS_BEFORE_PROFILE_WINDOW_BEGIN","failure_if_not_externally_pinned_and_accepted=E_POSSESSION_UNAVAILABLE",
)


def u16be(value: int) -> bytes:
    if type(value) is not int or not 0<=value<2**16: fail("U16BE domain")
    return value.to_bytes(2,"big")


def u32be(value: int) -> bytes:
    if type(value) is not int or not 0<=value<2**32: fail("U32BE domain")
    return value.to_bytes(4,"big")


def u64be(value: int) -> bytes:
    if type(value) is not int or not 0<=value<2**64: fail("U64BE domain")
    return value.to_bytes(8,"big")


def tagged_preimage(domain: str, values: Sequence[bytes]) -> bytes:
    if not domain or not domain.isascii() or any(type(value) is not bytes for value in values): fail("tagged preimage")
    return domain.encode("ascii")+u32be(len(values))+b"".join(u16be(index)+u64be(len(value))+value for index,value in enumerate(values,1))


def exact_frame(payload: bytes) -> bytes:
    if not payload or len(payload)>MAX_FRAME or not payload.isascii() or b"\x00" in payload or b"\n" in payload: fail("boundary frame")
    return u32be(len(payload))+payload


def hook_custody_profile_preimage() -> bytes:
    if len(HOOK_CUSTODY_PROFILE_LINES)!=41: fail("HC41 cardinality")
    preimage=tagged_preimage("P15R-HOOK-CUSTODY-PROFILE-v1",tuple(line.encode("ascii") for line in HOOK_CUSTODY_PROFILE_LINES))
    if len(preimage)!=2928 or hashlib.sha256(preimage).hexdigest()!=HOOK_CUSTODY_PROFILE_SHA256: fail("HC41 literal")
    return preimage


@dataclass(frozen=True)
class EndpointEnqueueReceipt:
    owner: str
    direction: str
    form: str
    framed_bytes: bytes
    full_return_count: int
    endpoint_dev: int
    endpoint_ino: int

    def complete(self) -> bool:
        return self.owner in ("P","G") and self.direction in ("P_TO_G","G_TO_P") and self.full_return_count==len(self.framed_bytes) and len(self.framed_bytes)>=5 and self.framed_bytes==exact_frame(self.framed_bytes[4:]) and self.endpoint_dev>=0 and self.endpoint_ino>0


@dataclass(frozen=True)
class ExternalProfileAcceptance:
    authority: str
    profile_sha256: str
    window_class: str
    accepted_before_profile_window: bool
    execution_gate_sha256: str
    lease_id: str
    revocation_epoch: int
    currently_unrevoked: bool


def validate_external_profile_acceptance(acceptance: ExternalProfileAcceptance|None) -> None:
    if type(acceptance) is not ExternalProfileAcceptance or acceptance.authority!="SEPARATE_SUCCESSOR_EXECUTION_GATE_ONLY" or acceptance.profile_sha256!=HOOK_CUSTODY_PROFILE_SHA256 or acceptance.window_class!="EXACT_PROFILE_AND_EXECUTION_WINDOW_CLASS" or not acceptance.accepted_before_profile_window or re.fullmatch(r"[0-9a-f]{64}",acceptance.execution_gate_sha256) is None or re.fullmatch(r"[0-9a-f]{64}",acceptance.lease_id) is None or type(acceptance.revocation_epoch) is not int or acceptance.revocation_epoch<0 or not acceptance.currently_unrevoked:
        fail("current profile unaccepted")


@dataclass
class BoundaryLedger:
    session: int
    bits: list[int]=field(default_factory=lambda:[0,0,0,0])
    extras: list[int]=field(default_factory=lambda:[0,0])
    frames: dict[str,bytes]=field(default_factory=dict)
    expected_frames: dict[str,bytes]=field(default_factory=dict)
    launcher_frame: bytes=b""
    stopped: bool=False
    reconciling: bool=False

    def retain_launcher(self, frame: bytes) -> None:
        if self.launcher_frame or frame!=exact_frame(frame[4:]): boundary_fail("WRONG_STATE","Launcher predecessor")
        try: payload=frame[4:].decode("ascii")
        except UnicodeDecodeError: boundary_fail("MALFORMED","Launcher ASCII")
        spec=WIRE_SPECS.get("LAUNCHER_REAPED")
        if spec is None or spec.pattern.fullmatch(payload) is None: boundary_fail("MALFORMED","Launcher grammar")
        self.launcher_frame=bytes(frame)

    def expect_carrier(self, form: str, frame: bytes) -> None:
        sequence=("PRIVILEGE_DROP_RELEASE","GUARDIAN_READY","GUARDIAN_READY_ACK","BOOTSTRAP_SEALED")
        if form not in sequence or form in self.expected_frames or frame!=exact_frame(frame[4:]): boundary_fail("WRONG_STATE","boundary expected frame")
        try: payload=frame[4:].decode("ascii")
        except UnicodeDecodeError: boundary_fail("MALFORMED","boundary expected ASCII")
        spec=WIRE_SPECS.get(form); session_match=re.search(r"(?:^| )session=([1-9][0-9]*)(?: |$)",payload)
        if payload.partition(" ")[0]!=form or spec is None or spec.pattern.fullmatch(payload) is None or session_match is None or int(session_match.group(1))!=self.session: boundary_fail("MALFORMED","boundary expected grammar")
        self.expected_frames[form]=bytes(frame)

    def commit_carrier(self, receipt: EndpointEnqueueReceipt) -> None:
        sequence=(("PRIVILEGE_DROP_RELEASE","P","P_TO_G"),("GUARDIAN_READY","G","G_TO_P"),("GUARDIAN_READY_ACK","P","P_TO_G"),("BOOTSTRAP_SEALED","G","G_TO_P"))
        index=sum(self.bits)
        try: payload=receipt.framed_bytes[4:].decode("ascii")
        except UnicodeDecodeError: fail("boundary carrier ASCII")
        spec=WIRE_SPECS.get(receipt.form); session_match=re.search(r"(?:^| )session=([1-9][0-9]*)(?: |$)",payload)
        if self.expected_frames.get(receipt.form)!=receipt.framed_bytes: boundary_fail("WRONG_ATTESTATION","boundary expected bytes")
        if self.stopped and not self.reconciling or index>=4 or (receipt.form,receipt.owner,receipt.direction)!=sequence[index] or not receipt.complete() or receipt.form in self.frames or payload.partition(" ")[0]!=receipt.form or spec is None or spec.direction!=receipt.direction or spec.pattern.fullmatch(payload) is None or session_match is None or int(session_match.group(1))!=self.session: boundary_fail("WRONG_STATE","boundary carrier commit")
        if index==2 and self.extras[0] or index==3 and any(self.extras): boundary_fail("WRONG_STATE","boundary extra cut")
        self.frames[receipt.form]=receipt.framed_bytes; self.bits[index]=1
        if index==3: self.stopped=True

    def record_old_form_extra(self, owner: str, direction: str, complete_frame: bytes, event_bits: tuple[int,int,int,int]) -> bool:
        try: payload=complete_frame[4:].decode("ascii")
        except UnicodeDecodeError: fail("boundary extra ASCII")
        form=payload.partition(" ")[0]; spec=WIRE_SPECS.get(form)
        valid_prefixes=((0,0,0,0),(1,0,0,0),(1,1,0,0),(1,1,1,0),(1,1,1,1))
        if event_bits not in valid_prefixes or complete_frame!=exact_frame(complete_frame[4:]) or form not in OLD_BOUNDARY_FORMS or spec is None or spec.pattern.fullmatch(payload) is None or owner!=("P" if direction=="P_TO_G" else "G"): fail("boundary extra evidence")
        cut_index=2 if direction=="P_TO_G" else 3
        if event_bits[cut_index]: return False
        if self.bits[cut_index]: fail("late discovery before directional cut")
        self.extras[0 if direction=="P_TO_G" else 1]=1
        return True

    def c14(self) -> tuple[tuple[int,int,int,int,int,int],str]:
        vector=tuple(self.bits+self.extras)
        matches=[row for row in C14_ROWS if row[0]==vector]
        if len(matches)!=1: fail("C14 closure")
        return matches[0]

    def failure_q(self) -> str:
        prefix=sum(self.bits)
        if prefix>=4: fail("sealed row has no failure Q")
        return Q_PHASES[prefix]


def classify_raw17(facts: Mapping[str,bool]) -> tuple[tuple[int,...],str]:
    if set(facts)!=set(RAW17_LABELS) or any(type(value) is not bool for value in facts.values()): fail("raw17 facts")
    bitmap=tuple(int(facts[label]) for label in RAW17_LABELS)
    winners=[label for label in RAW17_PRECEDENCE if facts[label]]
    if not winners: fail("raw17 empty")
    return bitmap,winners[0]


@dataclass(frozen=True)
class BoundaryFailureReceipt:
    session: int
    owners: tuple[str,...]
    primary_owner: str
    q_phase: str
    c14_vector: tuple[int,int,int,int,int,int]
    c14_class: str
    raw17_bitmap: tuple[int,...]
    primary_label: str
    expected_form: str
    expected_direction: str
    owner_evidence: tuple[tuple[str,BoundaryRawEvidence],...]
    secondary_observations: tuple[BoundaryFrameObservation,...]
    exact_frames: tuple[tuple[str,bytes,str],...]
    endpoint_identity: tuple[int,int]
    hp: str
    hg: str
    hm: str
    mech: str
    contract: str
    profile: str
    exact_eof: bool
    no_alternate_reader: bool
    no_future_producer: bool
    peer_death_reaped: bool
    endpoints_closed: bool


@dataclass(frozen=True)
class BoundaryTerminalSuccessReceipt:
    session: int
    c14_vector: tuple[int,int,int,int,int,int]
    c14_class: str
    exact_frames: tuple[tuple[str,bytes,str],...]
    endpoint_identity: tuple[int,int]
    hp: str
    hg: str
    hm: str
    mech: str
    contract: str
    profile: str
    exact_eof: bool
    endpoints_closed: bool
    non_c14_observations: tuple[BoundaryFrameObservation,...]


@dataclass(frozen=True)
class BoundaryFrameObservation:
    direction: str
    source: str
    packet: bytes
    send_return: int
    transport_errno: int
    intended_length: int
    message_flags: int
    ancillary_count: int
    carrier_bits: tuple[int,int,int,int]
    semantic_label: str

    def parsed(self) -> tuple[int,bytes,str,bool,bool]:
        declared=int.from_bytes(self.packet[:4],"big") if len(self.packet)>=4 else -1
        payload=self.packet[4:] if len(self.packet)>=4 else b""
        complete=declared>0 and declared<=MAX_FRAME and declared==len(payload)
        ascii_valid=complete and payload.isascii() and b"\x00" not in payload and b"\n" not in payload
        if not payload: form=""
        else:
            try: form=payload.partition(b" ")[0].decode("ascii")
            except UnicodeDecodeError: form=""
        spec=WIRE_SPECS.get(form) if ascii_valid else None
        grammar=spec is not None and spec.pattern.fullmatch(payload.decode("ascii")) is not None
        return declared,payload,form,complete,grammar


def boundary_observation(direction: str, source: str, packet: bytes, send_return: int=-1, transport_errno: int=0, intended_length: int=-1, message_flags: int=0, ancillary_count: int=0, *, carrier_bits: tuple[int,int,int,int], semantic_label: str="NONE") -> BoundaryFrameObservation:
    valid_prefixes=((0,0,0,0),(1,0,0,0),(1,1,0,0),(1,1,1,0),(1,1,1,1))
    if direction not in ("P_TO_G","G_TO_P") or source not in ("SEND_PREFIX","SEND_FULL_RETURN","RECEIVE","TERMINAL_DRAIN") or type(packet) is not bytes or send_return< -1 or transport_errno<0 or intended_length< -1 or message_flags<0 or ancillary_count<0 or carrier_bits not in valid_prefixes or semantic_label not in ("NONE",)+RAW17_LABELS: fail("boundary observation")
    return BoundaryFrameObservation(direction,source,bytes(packet),send_return,transport_errno,intended_length,message_flags,ancillary_count,carrier_bits,semantic_label)


@dataclass(frozen=True)
class BoundaryRawEvidence:
    expected_frame_present: bool
    grammar_valid: bool
    complete_count: int
    duplicate_observed: bool
    replay_observed: bool
    session_matches: bool
    guardian_identity_matches: bool
    guardian_cgroup_matches: bool
    attestation_matches: bool
    direction_matches: bool
    state_matches: bool
    order_matches: bool
    actual_length: int
    expected_length: int
    partial_observed: bool
    eof_observed: bool
    timeout_expired: bool
    p_alive: bool
    g_alive: bool
    transport_errno: int
    checkpoint_closed: bool

    def facts(self) -> dict[str,bool]:
        if self.complete_count<0 or self.actual_length<0 or self.expected_length<0 or self.transport_errno<0: fail("raw17 evidence domain")
        facts={
            "MISSING":self.checkpoint_closed,
            "MALFORMED":not self.grammar_valid,
            "DUPLICATE":self.duplicate_observed,
            "REPLAY":self.replay_observed,
            "WRONG_SESSION":not self.session_matches,
            "WRONG_G_IDENTITY":not self.guardian_identity_matches,
            "WRONG_CGROUP":not self.guardian_cgroup_matches,
            "WRONG_ATTESTATION":not self.attestation_matches,
            "WRONG_DIRECTION":not self.direction_matches,
            "WRONG_STATE":not self.state_matches,
            "REORDERED":not self.order_matches,
            "PARTIAL":self.partial_observed,
            "EOF":self.eof_observed,
            "TIMEOUT":self.timeout_expired,
            "P_CRASH":not self.p_alive,
            "G_CRASH":not self.g_alive,
            "TRANSPORT_ERROR":self.transport_errno>0,
        }
        if set(facts)!=set(RAW17_LABELS): fail("raw17 detector coverage")
        return facts


def derive_boundary_raw_evidence(*, observations: Sequence[BoundaryFrameObservation], canonical_predecessors: Mapping[str,bytes], expected_frames: Mapping[str,bytes], expected_form: str, expected_direction: str, session: int, guardian: tuple[int,int,int,int,int], guardian_cgroup_valid: bool, semantic_label: str, eof_observed: bool, timeout_expired: bool, p_alive: bool, g_alive: bool, checkpoint_closed: bool) -> BoundaryRawEvidence:
    if expected_form not in ("PRIVILEGE_DROP_RELEASE","GUARDIAN_READY","GUARDIAN_READY_ACK","BOOTSTRAP_SEALED") or expected_direction not in ("P_TO_G","G_TO_P") or session<=0 or semantic_label not in ("NONE",)+RAW17_LABELS: fail("raw17 derivation coordinate")
    allowed_predecessors=("LAUNCHER_REAPED","PRIVILEGE_DROP_RELEASE","GUARDIAN_READY","GUARDIAN_READY_ACK","BOOTSTRAP_SEALED")
    def bound_frame(form: str, frame: bytes, allowed: tuple[str,...]) -> bool:
        if form not in allowed or type(frame) is not bytes or len(frame)<5 or frame!=exact_frame(frame[4:]) or not frame[4:].isascii(): return False
        return frame[4:].partition(b" ")[0].decode("ascii")==form
    if any(not bound_frame(form,frame,allowed_predecessors) for form,frame in canonical_predecessors.items()): fail("raw17 predecessor baseline")
    if any(not bound_frame(form,frame,allowed_predecessors[1:]) for form,frame in expected_frames.items()): fail("raw17 expected-frame baseline")
    parsed=tuple((item,item.parsed()) for item in observations)
    relevant=parsed
    truncation_mask=socket.MSG_TRUNC|socket.MSG_CTRUNC
    semantic_labels={semantic_label}|{item.semantic_label for item in observations}

    def partial(item: BoundaryFrameObservation, parts: tuple[int,bytes,str,bool,bool]) -> bool:
        if item.message_flags&truncation_mask: return True
        if item.source=="SEND_PREFIX": return item.intended_length>0 and 0<item.send_return<item.intended_length
        if item.source in ("RECEIVE","TERMINAL_DRAIN") and item.packet:
            if len(item.packet)<4: return True
            return parts[0]>0 and len(item.packet)<4+parts[0]
        return False

    partial_observed=any(partial(item,parts) for item,parts in relevant)

    def recognizable(item: BoundaryFrameObservation, parts: tuple[int,bytes,str,bool,bool]) -> bool:
        return item.source!="SEND_PREFIX" and parts[3] and parts[4]

    def completed(item: BoundaryFrameObservation, parts: tuple[int,bytes,str,bool,bool]) -> bool:
        return recognizable(item,parts) and parts[2]==expected_form and item.direction==expected_direction and not item.message_flags and item.ancillary_count==0

    expected_frame_present=any(bool(item.packet) and parts[2] in ("",expected_form) for item,parts in relevant)
    malformed_observed="MALFORMED" in semantic_labels or any((item.packet or item.ancillary_count or item.message_flags) and item.source!="SEND_PREFIX" and not partial(item,parts) and (item.ancillary_count>0 or item.message_flags!=0 or not parts[3] or not parts[4]) for item,parts in relevant)
    grammar_valid=not malformed_observed
    repeated=[(item.direction,item.packet) for item,parts in relevant if completed(item,parts)]
    complete_count=len(repeated)
    baseline_bytes=set(canonical_predecessors.values()); observed_complete=[item.packet for item,parts in relevant if recognizable(item,parts)]
    duplicate_observed=any(packet in baseline_bytes for packet in observed_complete) or len(observed_complete)!=len(set(observed_complete))
    replay_observed=False
    session_matches=True; guardian_identity_matches=True
    form_index={"PRIVILEGE_DROP_RELEASE":0,"GUARDIAN_READY":1,"GUARDIAN_READY_ACK":2,"BOOTSTRAP_SEALED":3}; expected_index=form_index[expected_form]
    wrong_state=False; reordered=False; attestation_failure=False
    for _item,parts in relevant:
        if _item.source=="SEND_PREFIX" or not parts[3] or not parts[1].isascii(): continue
        record=parts[1].decode("ascii")
        coordinate=re.search(r"(?:^| )session=([0-9]+)(?: |$)",record)
        if coordinate is not None and coordinate.group(1)!=str(session):
            session_matches=False
        values={name:value for name,value in re.findall(r"(?:^| )(g_outer_pid|outer_pid|g_inner_pid|inner_pid|g_starttime|guardian_dev|guardian_ino)=([0-9]+)(?= |$)",record)}
        identity_fields=() if parts[2]=="LAUNCHER_REAPED" else (("outer_pid",guardian[0]),("inner_pid",1)) if parts[2]=="GUARDIAN_READY" else (("g_outer_pid",guardian[0]),("g_inner_pid",1),("g_starttime",guardian[2]),("guardian_dev",guardian[3]),("guardian_ino",guardian[4]))
        for name,wanted in identity_fields:
            if name in values and values[name]!=str(wanted): guardian_identity_matches=False
        if parts[4]:
            if parts[2]=="LAUNCHER_REAPED": wrong_state=True
            elif parts[2] in form_index:
                observed_index=form_index[parts[2]]
                if observed_index>expected_index: reordered=True
                if observed_index!=expected_index: wrong_state=True
                attestation_baseline=expected_frames.get(parts[2],canonical_predecessors.get(parts[2]))
                if attestation_baseline is not None and _item.packet!=attestation_baseline: attestation_failure=True
    direction_matches="WRONG_DIRECTION" not in semantic_labels and all(WIRE_SPECS[parts[2]].direction==item.direction for item,parts in relevant if recognizable(item,parts))
    state_matches="WRONG_STATE" not in semantic_labels and not wrong_state
    order_matches="REORDERED" not in semantic_labels and not reordered
    attestation_matches="WRONG_ATTESTATION" not in semantic_labels and not attestation_failure
    if "WRONG_SESSION" in semantic_labels: session_matches=False
    if "WRONG_G_IDENTITY" in semantic_labels: guardian_identity_matches=False
    if "WRONG_CGROUP" in semantic_labels: guardian_cgroup_valid=False
    expected_lengths=[]; actual_lengths=[]; transport_errno=0
    for item,parts in relevant:
        declared=parts[0]
        actual_lengths.append(item.send_return if item.source=="SEND_PREFIX" and item.send_return>=0 else len(item.packet))
        if item.intended_length>=0: expected_lengths.append(item.intended_length)
        elif declared>0: expected_lengths.append(4+declared)
        transport_errno=max(transport_errno,item.transport_errno)
    actual_length=max(actual_lengths,default=0); expected_length=max(expected_lengths,default=actual_length)
    return BoundaryRawEvidence(expected_frame_present,grammar_valid,complete_count,duplicate_observed,replay_observed,session_matches,guardian_identity_matches,guardian_cgroup_valid,attestation_matches,direction_matches,state_matches,order_matches,actual_length,expected_length,partial_observed,eof_observed,timeout_expired,p_alive,g_alive,transport_errno,checkpoint_closed)


@dataclass(frozen=True)
class BoundaryFailureTombstone:
    session: int
    owner: str
    endpoint_identity: tuple[int,int]
    c14_prefix: tuple[int,int,int,int,int,int]|None
    raw17_bitmap: tuple[int,...]|None
    primary_label: str
    exact_row_claimed: bool=False


class TerminalBoundaryReconciler:
    """Symmetric in-memory failure freeze; it is neither wire nor manifest."""
    def __init__(self, ledger: BoundaryLedger) -> None:
        self.ledger=ledger; self.scope_stopped=False; self.frozen: BoundaryFailureReceipt|None=None

    def stop_scope(self) -> None:
        if self.scope_stopped or self.frozen is not None: fail("terminal scope stop")
        self.scope_stopped=True; self.ledger.stopped=True; self.ledger.reconciling=True

    def freeze(self, *, owners: tuple[str,...], owner_evidence: Mapping[str,BoundaryRawEvidence], expected_form: str, expected_direction: str, endpoint_identity: tuple[int,int], exact_eof: bool, no_alternate_reader: bool, no_future_producer: bool, survivor_close_receipt: tuple[int,int], peer_death_reaped: bool, receipts: Mapping[str,str], secondary_observations: Sequence[BoundaryFrameObservation]=()) -> BoundaryFailureReceipt:
        if not self.scope_stopped or self.frozen is not None or owners not in (("P",),("G",),("P","G")) or set(owner_evidence)!=set(owners): fail("terminal freeze state")
        if not (exact_eof and no_alternate_reader and no_future_producer and peer_death_reaped) or survivor_close_receipt!=(0,errno.EBADF) or endpoint_identity[0]<0 or endpoint_identity[1]<=0: fail("terminal freeze ceiling")
        owner_facts={owner:owner_evidence[owner].facts() for owner in owners}; classified={owner:classify_raw17(owner_facts[owner]) for owner in owners}; precedence_index={label:index for index,label in enumerate(RAW17_PRECEDENCE)}
        minimum=min(precedence_index[value[1]] for value in classified.values()); tied=tuple(owner for owner in ("P","G") if owner in classified and precedence_index[classified[owner][1]]==minimum); primary=tied[0]
        aggregate={label:any(owner_facts[owner][label] for owner in owners) for label in RAW17_LABELS}; bitmap,label=classify_raw17(aggregate)
        vector,row_class=self.ledger.c14(); q=self.ledger.failure_q()
        required=("hp","hg","hm","mech","contract","profile")
        if set(receipts)!=set(required) or any(value!="NONE" and re.fullmatch(r"[0-9a-f]{64}",value) is None for value in receipts.values()) or receipts["profile"]!=HOOK_CUSTODY_PROFILE_SHA256: fail("terminal receipt hashes")
        frames=(("LAUNCHER_REAPED",self.ledger.launcher_frame,sha256(self.ledger.launcher_frame)),)+tuple((form,frame,sha256(frame)) for form,frame in self.ledger.frames.items()) if self.ledger.launcher_frame else tuple((form,frame,sha256(frame)) for form,frame in self.ledger.frames.items())
        owner_rows=tuple((owner,owner_evidence[owner]) for owner in ("P","G") if owner in owner_evidence)
        self.frozen=BoundaryFailureReceipt(self.ledger.session,owners,primary,q,vector,row_class,bitmap,label,expected_form,expected_direction,owner_rows,tuple(secondary_observations),frames,endpoint_identity,receipts["hp"],receipts["hg"],receipts["hm"],receipts["mech"],receipts["contract"],receipts["profile"],exact_eof,no_alternate_reader,no_future_producer,peer_death_reaped,True)
        self.ledger.reconciling=False
        return self.frozen

    def retain_unreconciled(self, owner: str, endpoint_identity: tuple[int,int], evidence: BoundaryRawEvidence) -> BoundaryFailureTombstone:
        if not self.scope_stopped or owner not in ("P","G") or endpoint_identity[0]<0 or endpoint_identity[1]<=0: fail("failure tombstone")
        try: vector=self.ledger.c14()[0]
        except PossessionFailure: vector=None
        facts=evidence.facts()
        try: bitmap,label=classify_raw17(facts)
        except PossessionFailure: bitmap,label=None,"UNRECONCILED"
        return BoundaryFailureTombstone(self.ledger.session,owner,endpoint_identity,vector,bitmap,label,False)


@dataclass
class BoundaryTerminalContext:
    owner: str
    reconciler: TerminalBoundaryReconciler
    evidence: BoundaryRawEvidence
    endpoint_identity: tuple[int,int]
    expected_form: str
    expected_direction: str
    holder_ceiling: bool
    observations: list[BoundaryFrameObservation]
    secondary_observations: list[BoundaryFrameObservation]
    semantic_label: str
    guardian: tuple[int,int,int,int,int]
    guardian_cgroup_valid: bool
    p_alive: bool
    g_alive: bool
    timeout_expired: bool

SYS_GETRANDOM = 318
SYS_RENAMEAT2 = 316
SYS_SECCOMP = 317
SYS_PIDFD_SEND_SIGNAL = 424
SYS_PIDFD_OPEN = 434
SYS_CLONE3 = 435
SYS_CLOSE_RANGE = 436
SYS_OPENAT2 = 437
SYS_PIDFD_GETFD = 438
SYS_FACCESSAT2 = 439
SYS_UNSHARE = 272
SYS_MOUNT = 165
SYS_UMOUNT2 = 166
SYS_PIVOT_ROOT = 155
SYS_GETDENTS64 = 217
SYS_READLINKAT = 267
SYS_SIGNALFD4 = 289
SYS_SETFSUID = 122
SYS_SETFSGID = 123

CLONE_NEWNS = 0x00020000
CLONE_NEWUSER = 0x10000000
CLONE_NEWPID = 0x20000000
CLONE_PIDFD = 0x00001000
CLONE_INTO_CGROUP = 0x200000000
MS_REC = 0x4000
MS_PRIVATE = 1 << 18
MS_NODEV = 4
MS_NOSUID = 2
MS_NOEXEC = 8
MNT_DETACH = 2
AT_EMPTY_PATH = 0x1000
AT_REMOVEDIR = 0x200
AT_EACCESS = 0x200
AT_SYMLINK_NOFOLLOW = 0x100
AT_FDCWD = -100
RENAME_NOREPLACE = 1
RENAME_EXCHANGE = 2
RESOLVE_NO_MAGICLINKS = 0x02
RESOLVE_NO_SYMLINKS = 0x04
RESOLVE_BENEATH = 0x08
FD_CLOEXEC = 1
CGROUP2_SUPER_MAGIC = 0x63677270
CLOSE_RANGE_UNSHARE = 1 << 1

NETLINK_SOCK_DIAG = 4
SOCK_DIAG_BY_FAMILY = 20
UNIX_DIAG_PEER = 2
UNIX_DIAG_SHUTDOWN = 6
P15R_UNIX_DIAG_QUERY_TIMEOUT_NS = 30000000000
AUDIT_ARCH_X86_64 = 0xC000003E
X32_SYSCALL_BIT = 0x40000000

HANDLED_SIGNALS = (signal.SIGHUP,signal.SIGINT,signal.SIGQUIT,signal.SIGPIPE,signal.SIGALRM,signal.SIGTERM,signal.SIGUSR1,signal.SIGUSR2)
OPEN_DIR = os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW|os.O_CLOEXEC
OPEN_PATH_DIR = getattr(os,"O_PATH",os.O_RDONLY)|os.O_DIRECTORY|os.O_NOFOLLOW|os.O_CLOEXEC
OPEN_REGULAR = os.O_RDONLY|os.O_NOFOLLOW|os.O_CLOEXEC

FDSETS = {
    "STDIO_BARRIER":(frozenset((0,1,2,8)),frozenset((0,1,2,8)),frozenset((0,1,2))),
    "STDIO_SOURCE_BARRIER":(frozenset((0,1,2,3,8)),frozenset((0,1,2,8)),frozenset((0,1,2))),
    "STDIO_SOURCE_ROOT_BARRIER":(frozenset((0,1,2,3,8,9)),frozenset((0,1,2,8,9)),frozenset((0,1,2,9))),
    "STDIO_SOURCE_RPC_AUDIT_BARRIER":(frozenset((0,1,2,3,4,5,8)),frozenset((0,1,2,4,5,8)),frozenset((0,1,2,4,5))),
}

@dataclass(frozen=True)
class RegistryRow:
    child: int
    phase: str
    target: str
    session: int
    owner: str
    role: str
    purpose: str
    admission: str
    fdset: str


PRE_SUITE_CHILDREN = (
    RegistryRow(1,"CGROUP_PREFLIGHT_E1","CGROUP_PROBE_CHILD epoch=1",0,"BOOTSTRAP_G","PROBE","NONE","BOOTSTRAP_FREEZE_THAW_E1","STDIO_BARRIER"),
    RegistryRow(2,"CGROUP_PREFLIGHT_E2","CGROUP_PROBE_CHILD epoch=2",0,"BOOTSTRAP_G","PROBE","NONE","BOOTSTRAP_KILL_E2","STDIO_BARRIER"),
    RegistryRow(3,"PRE_SUITE_VERIFY","VERIFY_ONLY_GENERATOR",0,"REPRO_COORDINATOR","GENERATOR","NONE","PRE_SUITE_VERIFY_ONLY","STDIO_SOURCE_BARRIER"),
    RegistryRow(4,"PRE_SUITE_A","GENERATE_CANONICAL_A",0,"REPRO_COORDINATOR","GENERATOR","CANONICAL_A","PRE_SUITE_CANONICAL_A","STDIO_SOURCE_ROOT_BARRIER"),
    RegistryRow(5,"PRE_SUITE_B","GENERATE_CANONICAL_B",0,"REPRO_COORDINATOR","GENERATOR","CANONICAL_B","PRE_SUITE_CANONICAL_B","STDIO_SOURCE_ROOT_BARRIER"),
    RegistryRow(6,"SUITE_ENTRY","TOP_TEST_CONTROLS",0,"SUITE_173","TOP_TEST_RUNNER","NONE","SUITE_173_TOP_RUNNER","STDIO_SOURCE_RPC_AUDIT_BARRIER"),
)

FD5_FORMS = (
    "SESSION_AUTH_OPEN","SESSION_AUTH_CHALLENGE","SESSION_AUTH_REGISTERED","SESSION_AUTH_RECEIPT",
    "SESSION_AUTH_ACTIVATED","SESSION_AUTH_ACTIVE_RECEIPT","SESSION_AUTH_TERMINAL_OBSERVED","SESSION_AUTH_TERMINAL_RECEIPT",
    "AUDIT_OPEN","AUDIT_CHALLENGE","AUDITED_SPAWN","AUDIT_RECEIPT",
)
D_M1_FORMS = (
    "SESSION_AUTH_CREATE_GRANTED","SESSION_AUTH_CREATE_ACCEPTED","SESSION_AUTH_COMMIT","SESSION_AUTH_COMMITTED",
    "SESSION_AUTH_ACTIVE","SESSION_AUTH_ACTIVE_ACK","SESSION_AUTH_ABORT","SESSION_AUTH_ABORTED",
    "SESSION_AUTH_TERMINAL_PREPARED","SESSION_AUTH_TERMINAL_GRANTED","SESSION_AUTH_FINALIZE","SESSION_AUTH_FINALIZED_ACK",
)
D_M2_FORMS = ("FD_AUDIT_QUIESCE_ENTER","FD_AUDIT_QUIESCE_ACK","FD_AUDIT_QUIESCE_EXIT","FD_AUDIT_QUIESCE_EXIT_ACK")
BASE_CONTROL_FORMS = (
    "PID1_READY","WORKERS_CGROUP_FD","WORKERS_CGROUP_FD_ACK","CGROUP_PROBE_CHILD","CGROUP_PROBE_FROZEN","CGROUP_PROBE_THAWED","CGROUP_PROBE_REAPED","CGROUP_PROBE_KILLED",
    "LAUNCHER_REAPED","PRIVILEGE_DROP_RELEASE","GUARDIAN_READY","GUARDIAN_READY_ACK","BOOTSTRAP_SEALED","AUDIT_FD_REQUEST","AUDIT_FD_GRANTED","AUDITED_RPC_ACCEPTED","AUDITED_RPC_CONFIRMED","CHILD_REGISTERED","CHILD_REGISTERED_AUDITED","CHILD_ADMITTED","SOURCE_READY","START","CHILD_REAPED","CHILD_REAPED_ACK",
    "OBJECT_REGISTERED","OBJECT_REGISTERED_ACK","OBJECT_RELEASED","MEMBER_CREATE_AUTHORIZED","MEMBER_CREATE_ACK","MEMBER_LEDGER_CLOSED","MEMBER_LEDGER_ACK","LOCK_BOUND","FREEZE_REQUEST","FROZEN_NOREFS","FROZEN_FINAL","CLEANUP_COMMITTED","THAWED",
    "KILL_REQUEST","KILL_ISSUED","REAPED","CGROUP_EMPTY","CLEANUP_RESULT","SIGNAL_PENDING","SIGNAL_CLEANED","EXIT",
)
OBJECT_KINDS = frozenset(("ROOT_PARENT","ROOT","ROOT_MEMBER","LOCK_PARENT","LOCK","LOCK_MEMBER"))
TARGETS = frozenset(("TOP_TEST_CONTROLS","VERIFY_ONLY_GENERATOR","GENERATE_CANONICAL_A","GENERATE_CANONICAL_B","GENERATE_MUTATION","COPIED_REPRODUCE","LOCK_HOLDER","LOCK_CONTENDER","REPLACEMENT_ACTOR"))
ROLE_BY_TARGET = {
    "CGROUP_PROBE_CHILD":"PROBE","TOP_TEST_CONTROLS":"TOP_TEST_RUNNER","COPIED_REPRODUCE":"REQUESTER",
    "VERIFY_ONLY_GENERATOR":"GENERATOR","GENERATE_CANONICAL_A":"GENERATOR","GENERATE_CANONICAL_B":"GENERATOR","GENERATE_MUTATION":"GENERATOR",
    "REPLACEMENT_ACTOR":"REPLACEMENT_ACTOR","LOCK_HOLDER":"LOCK_HOLDER","LOCK_CONTENDER":"CONTENDER",
}
TRIGGERS = frozenset(("NONE","P15R_TEST_CREATE_POST_CACHE","P15R_TEST_ABORT_AFTER_FRESH_A","P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN","P15R_TEST_REPLACE_CANONICAL_ROOT","P15R_TEST_REPLACE_MUTATION_ROOT","P15R_TEST_REPLACE_P25_ROOT","P15R_TEST_REPLACE_LOCK_ACQUIRING","P15R_TEST_REPLACE_LOCK_CLEANING"))
AUDIT_KINDS = frozenset(("PREFLIGHT_PROBE","RUNTIME_CHILD"))
AUDIT_SLOTS = frozenset(("FD4","FD5","FD8"))
AUDIT_OUTCOMES = frozenset(("PASS","ABORT"))
OUTCOMES = frozenset(("UNSET","ABSENT","DISPLACED_OWNED","DISPLACED_CLEANED","FOREIGN_RETAINED","ERROR","CRASH_TEARDOWN"))
OUTCOME_RE = r"(?:UNSET|ABSENT|DISPLACED_OWNED|DISPLACED_CLEANED|FOREIGN_RETAINED|ERROR|CRASH_TEARDOWN)"
OUTCOME_PRECEDENCE = {"UNSET":0,"ABSENT":1,"DISPLACED_OWNED":2,"DISPLACED_CLEANED":3,"FOREIGN_RETAINED":4,"CRASH_TEARDOWN":5,"ERROR":6}
AUTH_PHASES = frozenset(("REGISTERED","CREATE_GRANTED","CREATE_ACCEPTED","INACTIVE_COMMITTED","ACTIVATION_JOINED","ACTIVE_RECEIPT_SENT","ACTIVE_PENDING","ACTIVE","CLOSING"))
AUTH_REASONS = frozenset(("RECEIPT_SEND","REQUESTER_EOF","CREATE_MISMATCH","CREATE_ACCEPTED_SEND","COMMIT_SEND","PRIVATE_CONSTRUCTION","CREATED_SEND","COMMITTED_SEND","ACTIVATION_MISMATCH","ACTIVE_RECEIPT_SEND","ACTIVE_SEND","ACTIVE_ACK_SEND","PREACTIVE_OPERATION","ACTIVE_OPERATION_MISMATCH","SESSION_CLOSE_FAILURE","CONTROL_EOF"))
V7_TERMINAL_CAUSES = frozenset(("PREPARED_SEND","PREPARED_MISMATCH","TERMINAL_ENTROPY_FILL","TERMINAL_ENTROPY_COLLISION","TERMINAL_GRANT_SEND","TERMINAL_GRANT_MISMATCH","TERMINAL_FD4_SEND","TERMINAL_OBSERVATION_MISSING","TERMINAL_OBSERVATION_MISMATCH","SESSION_CLOSE_OR_CLEANUP","REQUESTER_EARLY_EOF","FINALIZE_SEND","FINALIZE_MISMATCH","FINALIZED_ACK_SEND","FINALIZED_ACK_MISMATCH","TERMINAL_RECEIPT_SEND","TERMINAL_EOF_MISSING","CONTROL_EOF","CONTROL_CRASH"))
V8_FAILURE_CAUSES = frozenset(("TERMINAL_RECEIPT_SEND","FD5_EARLY_EOF","FD5_EXTRA_DATAGRAM","FD4_EXTRA_DATAGRAM","POST_ACK_D_M1_RECORD","REQUESTER_IDENTITY","REQUESTER_EXIT_STATUS","REQUESTER_WAITID","REQUESTER_WRONG_CHILD","REQUESTER_DUPLICATE_REAP","REQUESTER_PROCESS_PRESENT","REQUESTER_FDSET_NONEMPTY","CHILD_REAPED_SEND","CHILD_REAPED_RECORD","CHILD_REAPED_ACK_SEND","CHILD_REAPED_ACK_RECORD","GLOBAL_FINAL_RECORD","GLOBAL_FINAL_PROOF","EXIT_RECORD","CONTROL_EOF_EARLY","P_CRASH","G_CRASH","CONTROL_DISPOSAL","PIDFD_ABSENCE","FD5_PEER_ABSENCE","G_REAP","CGROUP_FINAL","FINAL_LEDGER"))
COPIED_EXPECTED_STATUS = {
    "test_package_p20_post_run_cache":1,"test_package_p21_recursive_entry":1,"test_package_p22_concurrent_second_entry":1,
    "test_package_p23_verify_only_repair_attempt":1,"test_package_p24_forced_cleanup_failure":1,"test_rep_009":1,"test_rep_010":0,
}
GENERATED_NAMES = (
    "valuation_normalization_controls.csv","exponent_order_branch_controls.csv","finite_kernel_truncation_controls.csv","torsion_closure_type_controls.csv",
    "signature_nonpromotion_controls.csv","owner_firewall_controls.csv","proof_ceiling_controls.csv","target_summary.csv","manifest.json",
)
IMPLEMENTATION_PATHS = ("code/generate_controls.py","code/test_controls.py","code/README.md","experiments/reproduce.sh","experiments/README.md","results/README.md")
AUTHORITY_PATHS = (
    "papers/14-global-periodic-topology/notes/papers14_18_batch_design_lock.md","papers/14-global-periodic-topology/notes/papers14_18_batch_amendment_v1.md","papers/14-global-periodic-topology/notes/papers14_18_batch_amendment_v2.md",
    "papers/15-mixed-clock-rigidity/notes/phase1_transverse_ulm_precheck.md","papers/15-wieferich-ulm-packet-bases/notes/research_protocol.md","papers/15-wieferich-ulm-packet-bases/notes/candidate_lock.md",
    "papers/15-wieferich-ulm-packet-bases/notes/phase1_amendment_v1.md","papers/15-wieferich-ulm-packet-bases/notes/phase1_amendment_v2.md","papers/15-wieferich-ulm-packet-bases/notes/phase1_source_precedent_audit.md",
    "papers/15-wieferich-ulm-packet-bases/notes/phase1_methodology_devils_review.md","papers/15-wieferich-ulm-packet-bases/notes/phase1_final_gate.md","papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_proofs.md",
    "papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_peer_review.md","papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_gate.md",
)
LIFECYCLE_PATHS = (
    "notes/phase2_control_design_lock.md","notes/phase2_control_design_peer_review.md","notes/phase2_control_implementation_gate.md",
    "notes/phase2_control_design_amendment_v1.md","notes/phase2_control_design_amendment_v2.md","notes/phase2_control_design_amendment_v3.md","notes/phase2_control_design_amendment_v4.md",
    "notes/phase2_control_design_amendment_v5.md","notes/phase2_control_design_amendment_v6.md","notes/phase2_control_design_amendment_v7.md","notes/phase2_control_design_amendment_v8.md",
    "notes/phase2_control_design_amendment_v9.md","notes/phase2_control_design_amendment_v10.md","notes/phase2_control_design_amendment_v11.md",
    "notes/phase2_control_design_amendment_v13.md","notes/phase2_control_design_amendment_v14.md",
)
SOURCE_CAP_IDENTITIES: dict[int,tuple[int,int,int,int,int]] = {}

LIBC = ctypes.CDLL(None,use_errno=True)
LIBC.syscall.restype = ctypes.c_long


class PossessionFailure(RuntimeError):
    def __init__(self, token: str = E_POSSESSION, detail: str = "") -> None:
        super().__init__(token)
        self.token = token
        self.detail = detail


class BoundaryProtocolFailure(PossessionFailure):
    def __init__(self, label: str, detail: str) -> None:
        if label not in RAW17_LABELS: raise ValueError("boundary protocol label")
        super().__init__(E_POSSESSION,detail)
        self.label=label


class AuthenticatedSignal(RuntimeError):
    def __init__(self, signo: int) -> None:
        super().__init__("authenticated handled signal")
        self.signo=signo


def fail(detail: str = "", token: str = E_POSSESSION) -> None:
    raise PossessionFailure(token,detail)


def boundary_fail(label: str, detail: str) -> None:
    raise BoundaryProtocolFailure(label,detail)


def syscall(number: int, *arguments: object) -> int:
    ctypes.set_errno(0)
    result = int(LIBC.syscall(ctypes.c_long(number),*arguments))
    if result == -1:
        error = ctypes.get_errno()
        raise OSError(error,os.strerror(error))
    return result


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


ENDPOINT_INSTALL_READBACK0 = b"attach_rc=0 attach_fprog_len_insns=1 attach_fprog_optlen_bytes=16 attach_sock_filter_bytes=8 attach_code_u16=6 attach_jt_u8=0 attach_jf_u8=0 attach_k_u32=4294967295 get_filter_query0_rc=0 get_filter_query0_optval=NULL get_filter_query0_optlen_in_insns=0 get_filter_query0_optlen_out_insns=1 get_filter_read0_rc=0 get_filter_read0_optlen_in_insns=1 get_filter_read0_optlen_out_insns=1 get_filter_read0_buffer_bytes=8 get_filter_read0_buffer_pre_hex=a5a5a5a5a5a5a5a5 get_filter_read0_buffer_post_hex=06000000ffffffff get_filter_read0_code_u16=6 get_filter_read0_jt_u8=0 get_filter_read0_jf_u8=0 get_filter_read0_k_u32=4294967295 lock_set_rc=0 lock_set_value=1 lock_set_optlen_bytes=4 lock_get0_rc=0 lock_get0_optlen_in_bytes=4 lock_get0_optlen_out_bytes=4 lock_get0_value=1"
ENDPOINT_NEGATIVE_TESTS = b"unlock_value=0 unlock_optlen_bytes=4 unlock_rc=-1 unlock_errno=1 detach_dummy_value=0 detach_optlen_bytes=4 detach_rc=-1 detach_errno=1 replace_fprog_optlen_bytes=16 replace_sock_filter_bytes=8 replace_fprog_zero_initialized=1 replace_filter_pointer_valid=1 replace_fprog_len_insns=1 replace_code_u16=6 replace_jt_u8=0 replace_jf_u8=0 replace_k_u32=0 replace_rc=-1 replace_errno=1"
ENDPOINT_READBACK1 = b"get_filter_query1_rc=0 get_filter_query1_optval=NULL get_filter_query1_optlen_in_insns=0 get_filter_query1_optlen_out_insns=1 get_filter_read1_rc=0 get_filter_read1_optlen_in_insns=1 get_filter_read1_optlen_out_insns=1 get_filter_read1_buffer_bytes=8 get_filter_read1_buffer_pre_hex=a5a5a5a5a5a5a5a5 get_filter_read1_buffer_post_hex=06000000ffffffff get_filter_read1_code_u16=6 get_filter_read1_jt_u8=0 get_filter_read1_jf_u8=0 get_filter_read1_k_u32=4294967295 lock_get1_rc=0 lock_get1_optlen_in_bytes=4 lock_get1_optlen_out_bytes=4 lock_get1_value=1"
MECHANICAL_ENDPOINT_CHECK = b"ep_p_local_valid=1 ep_g_local_valid=1 holder_matrix_valid=1 identity_pre_filter_eq_post_owner_local_holder_freeze_both=1 holder_matrix_internal_reciprocal_peer_join=1 accept_all_locked_both=1 negative_tests_eperm_both=1 sole_proc_visible_holder_both=1 so_cookie_to_udiag_cookie_comparison=FORBIDDEN hidden_holder_custody_source=HOOK_CUSTODY_PROFILE"
HOLDER_MATRIX_CHECK = b"endpoint_inodes_distinct=1 ep_p_st_ino_eq_udiag_ino=1 ep_g_st_ino_eq_udiag_ino=1 ep_p_udiag_peer_eq_ep_g_udiag_ino=1 ep_g_udiag_peer_eq_ep_p_udiag_ino=1 sole_proc_visible_holder_both=1 fd_handoff_both=NONE so_cookie_to_udiag_cookie_comparison=FORBIDDEN hidden_or_queued_reference_absence=NOT_PROVED_BY_THIS_RECEIPT"


def _raw_sockopt_result(operation: str, result: int, expected_errno: int=0) -> None:
    observed_errno=ctypes.get_errno()
    if expected_errno:
        if result!=-1 or observed_errno!=expected_errno: fail(operation+" negative receipt")
    elif result!=0 or observed_errno!=0:
        fail(operation+" receipt")


def lock_actual_endpoint_filter(endpoint: socket.socket) -> None:
    """Install, lock, negatively probe, and reread the exact accept-all cBPF.

    The three constants serialized into HP/HG are admitted only after this
    raw ABI sequence completes on the actual ACCEPT/CONNECT endpoint.  The
    fixed strings are therefore receipt encodings, not substitute evidence.
    """
    fd=endpoint.fileno()
    if fd<0 or ctypes.sizeof(SockFilter)!=8 or ctypes.sizeof(SockFprog)!=16: fail("endpoint filter ABI")
    accept_storage=(SockFilter*1)(SockFilter(6,0,0,0xffffffff)); accept_program=SockFprog(1,accept_storage)
    ctypes.set_errno(0); result=int(LIBC.setsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(26),ctypes.byref(accept_program),ctypes.c_uint(16)))
    _raw_sockopt_result("attach",result)

    def read_filter(serial: int) -> None:
        query_length=ctypes.c_uint(0); ctypes.set_errno(0)
        result=int(LIBC.getsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(26),ctypes.c_void_p(),ctypes.byref(query_length)))
        _raw_sockopt_result("get filter query"+str(serial),result)
        if query_length.value!=1: fail("get filter query cardinality")
        raw=(ctypes.c_ubyte*8)(*([0xa5]*8)); read_length=ctypes.c_uint(1); ctypes.set_errno(0)
        result=int(LIBC.getsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(26),ctypes.byref(raw),ctypes.byref(read_length)))
        _raw_sockopt_result("get filter read"+str(serial),result)
        if read_length.value!=1 or bytes(raw)!=bytes.fromhex("06000000ffffffff"): fail("get filter bytes")
        parsed=SockFilter.from_buffer_copy(bytes(raw))
        if (parsed.code,parsed.jt,parsed.jf,parsed.k)!=(6,0,0,0xffffffff): fail("get filter parse")

    read_filter(0)
    one=ctypes.c_int(1); ctypes.set_errno(0)
    result=int(LIBC.setsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(44),ctypes.byref(one),ctypes.c_uint(4)))
    _raw_sockopt_result("lock set",result)

    def read_lock(serial: int) -> None:
        value=ctypes.c_int(-1); length=ctypes.c_uint(4); ctypes.set_errno(0)
        result=int(LIBC.getsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(44),ctypes.byref(value),ctypes.byref(length)))
        _raw_sockopt_result("lock get"+str(serial),result)
        if length.value!=4 or value.value!=1: fail("lock readback")

    read_lock(0)
    zero=ctypes.c_int(0)
    ctypes.set_errno(0); result=int(LIBC.setsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(44),ctypes.byref(zero),ctypes.c_uint(4)))
    _raw_sockopt_result("unlock",result,errno.EPERM)
    ctypes.set_errno(0); result=int(LIBC.setsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(27),ctypes.byref(zero),ctypes.c_uint(4)))
    _raw_sockopt_result("detach",result,errno.EPERM)
    replacement_storage=(SockFilter*1)(SockFilter(6,0,0,0)); replacement_program=SockFprog(1,replacement_storage)
    ctypes.set_errno(0); result=int(LIBC.setsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(26),ctypes.byref(replacement_program),ctypes.c_uint(16)))
    _raw_sockopt_result("replace",result,errno.EPERM)
    read_filter(1); read_lock(1)


def raw_actual_endpoint_identity(endpoint: socket.socket) -> tuple[int,int,int,int]:
    fd=endpoint.fileno(); values=[]
    for option,expected in ((getattr(socket,"SO_DOMAIN",39),socket.AF_UNIX),(socket.SO_TYPE,socket.SOCK_SEQPACKET),(getattr(socket,"SO_PROTOCOL",38),0)):
        value=ctypes.c_int(0x5a5a5a5a); length=ctypes.c_uint(4); ctypes.set_errno(0)
        result=int(LIBC.getsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(option),ctypes.byref(value),ctypes.byref(length)))
        _raw_sockopt_result("endpoint identity int",result)
        if length.value!=4 or value.value!=expected: fail("endpoint identity int readback")
        values.append(value.value)
    cookie=ctypes.c_uint64(0xa5a5a5a5a5a5a5a5); cookie_length=ctypes.c_uint(8); ctypes.set_errno(0)
    result=int(LIBC.getsockopt(ctypes.c_int(fd),ctypes.c_int(socket.SOL_SOCKET),ctypes.c_int(getattr(socket,"SO_COOKIE",57)),ctypes.byref(cookie),ctypes.byref(cookie_length)))
    _raw_sockopt_result("endpoint identity cookie",result)
    if cookie_length.value!=8 or cookie.value==0: fail("endpoint cookie readback")
    return values[0],values[1],values[2],cookie.value


@dataclass(frozen=True)
class EndpointIdentityEvidence:
    netns_dev: int
    netns_ino: int
    so_cookie_u64: int
    owner_outer_pid: int
    owner_starttime: int
    udiag_ino_u32: int=0
    udiag_peer_u32: int=0
    udiag_cookie0_u32: int=0
    udiag_cookie1_u32: int=0


def build_owner_local_endpoint_receipt(endpoint: socket.socket, session: int, role: str, evidence: EndpointIdentityEvidence) -> bytes:
    roles={"EP_P":("P","ACCEPT","G_TO_P"),"EP_G":("G","CONNECT","P_TO_G")}
    if role not in roles or session<=0: fail("endpoint receipt role")
    owner,creation,direction=roles[role]; st=os.fstat(endpoint.fileno())
    so_domain=endpoint.getsockopt(socket.SOL_SOCKET,getattr(socket,"SO_DOMAIN",39)); so_type=endpoint.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE); so_protocol=endpoint.getsockopt(socket.SOL_SOCKET,getattr(socket,"SO_PROTOCOL",38))
    cookie_raw=endpoint.getsockopt(socket.SOL_SOCKET,getattr(socket,"SO_COOKIE",57),8); cookie=int.from_bytes(cookie_raw,"little") if isinstance(cookie_raw,bytes) else int(cookie_raw)
    if (so_domain,so_type,so_protocol)!=(socket.AF_UNIX,socket.SOCK_SEQPACKET,0) or not stat.S_ISSOCK(st.st_mode) or cookie!=evidence.so_cookie_u64: fail("endpoint identity")
    binding=f"session={session} endpoint={role} owner={owner} creation={creation} fd_handoff=NONE receive_direction={direction} carrier_scope_id={CARRIER_SCOPE_ID} observation_deadline=POST_G_LOCAL_DROP_AND_L_PIDFD_REAP_AND_G_SOLE_GUARDIAN_MEMBER_AND_P_DENIAL_EVIDENCE_COMPLETE_PRE_LAUNCHER_REAPED_SEND".encode("ascii")
    common=f"so_domain=1 so_type=5 so_protocol=0 st_mode_type=S_IFSOCK netns_dev={evidence.netns_dev} netns_ino={evidence.netns_ino} st_dev={st.st_dev} st_ino={st.st_ino} so_cookie_u64={cookie}"
    suffix=(f" udiag_ino_u32={evidence.udiag_ino_u32} udiag_peer_u32={evidence.udiag_peer_u32} udiag_cookie0_u32={evidence.udiag_cookie0_u32} udiag_cookie1_u32={evidence.udiag_cookie1_u32} udiag_type_u8=5 udiag_state_u8=1 udiag_shutdown_u8=0" if role=="EP_P" else " udiag_observation=DELEGATED_TO_P_HOLDER_MATRIX")
    identity_pre=("phase=PRE_FILTER_FREEZE "+common+suffix).encode("ascii")
    identity_post=("phase=POST_OWNER_LOCAL_HOLDER_FREEZE "+common+suffix).encode("ascii")
    holder=f"freeze=1 observer={owner} owner_outer_pid={evidence.owner_outer_pid} owner_starttime={evidence.owner_starttime} owner_local_same_inode_fdrefs=1 actual_endpoint_fd_handoff=NONE hidden_or_queued_reference_absence=NOT_CLAIMED_BY_LOCAL_RECEIPT".encode("ascii")
    return tagged_preimage("P15R-ACTUAL-ENDPOINT-LOCAL-RECEIPT-v1",(binding,identity_pre,ENDPOINT_INSTALL_READBACK0,ENDPOINT_NEGATIVE_TESTS,ENDPOINT_READBACK1,identity_post,holder))


@dataclass(frozen=True)
class HolderMatrixEndpoint:
    endpoint: str
    owner: str
    owner_outer_pid: int
    owner_starttime: int
    st_dev: int
    st_ino: int
    udiag_ino_u32: int
    udiag_peer_u32: int
    udiag_cookie0_u32: int
    udiag_cookie1_u32: int
    p_refs: int
    g_refs: int

    def ascii(self) -> bytes:
        if (self.endpoint,self.owner,self.p_refs,self.g_refs) not in (("EP_P","P",1,0),("EP_G","G",0,1)): fail("holder row role")
        return f"endpoint={self.endpoint} owner={self.owner} owner_outer_pid={self.owner_outer_pid} owner_starttime={self.owner_starttime} st_dev={self.st_dev} st_ino={self.st_ino} udiag_ino_u32={self.udiag_ino_u32} udiag_peer_u32={self.udiag_peer_u32} udiag_cookie0_u32={self.udiag_cookie0_u32} udiag_cookie1_u32={self.udiag_cookie1_u32} proc_visible_p_fdrefs={self.p_refs} proc_visible_g_fdrefs={self.g_refs} proc_visible_launcher_fdrefs=0 proc_visible_other_design_fdrefs=0 proc_visible_total_fdrefs=1".encode("ascii")


def build_holder_matrix_receipt(session: int, scan_pidns: tuple[int,int], netns: tuple[int,int], ep_p: HolderMatrixEndpoint, ep_g: HolderMatrixEndpoint) -> bytes:
    if ep_p.st_ino==ep_g.st_ino or ep_p.st_ino!=ep_p.udiag_ino_u32 or ep_g.st_ino!=ep_g.udiag_ino_u32 or ep_p.udiag_peer_u32!=ep_g.udiag_ino_u32 or ep_g.udiag_peer_u32!=ep_p.udiag_ino_u32: fail("holder reciprocal join")
    binding=f"session={session} auditor=P scan_phase=POST_G_LOCAL_DROP_AND_L_PIDFD_REAP_AND_G_SOLE_GUARDIAN_MEMBER_AND_P_DENIAL_EVIDENCE_COMPLETE_PRE_LAUNCHER_REAPED_SEND scan_pidns_dev={scan_pidns[0]} scan_pidns_ino={scan_pidns[1]} netns_dev={netns[0]} netns_ino={netns[1]} carrier_scope_id={CARRIER_SCOPE_ID}".encode("ascii")
    return tagged_preimage("P15R-ACTUAL-ENDPOINT-HOLDER-MATRIX-v1",(binding,ep_p.ascii(),ep_g.ascii(),HOLDER_MATRIX_CHECK))


def build_mechanical_endpoint_receipt(session: int, hp: str, hg: str, hm: str) -> bytes:
    if any(re.fullmatch(r"[0-9a-f]{64}",digest) is None for digest in (hp,hg,hm)): fail("mechanical hash")
    binding=f"session={session} carrier_scope_id={CARRIER_SCOPE_ID} endpoint_order=EP_P_THEN_EP_G component_observation_deadline=POST_G_LOCAL_DROP_AND_L_PIDFD_REAP_AND_G_SOLE_GUARDIAN_MEMBER_AND_P_DENIAL_EVIDENCE_COMPLETE_PRE_LAUNCHER_REAPED_SEND assembly_phase=POST_RELEASE_VALIDATION_PRE_GUARDIAN_READY_ENQUEUE".encode("ascii")
    return tagged_preimage("P15R-MECHANICAL-ENDPOINT-RECEIPT-v1",(binding,f"ep_p_local_receipt_sha256={hp}".encode("ascii"),f"ep_g_local_receipt_sha256={hg}".encode("ascii"),f"holder_matrix_receipt_sha256={hm}".encode("ascii"),MECHANICAL_ENDPOINT_CHECK))


def actual_endpoint_contract(session: int, mechanical_sha256: str, profile_sha256: str) -> bytes:
    lines=(b"P15R_ACTUAL_ENDPOINT_CONTRACT_V1\n",f"session={session}\n".encode("ascii"),f"carrier_scope_id={CARRIER_SCOPE_ID}\n".encode("ascii"),f"mechanical_endpoint_receipt_sha256={mechanical_sha256}\n".encode("ascii"),f"hook_custody_profile_sha256={profile_sha256}\n".encode("ascii"))
    return b"".join(lines)


def build_release_frame(session: int, guardian: tuple[int,int,int,int,int], hp_raw: bytes, hm_raw: bytes, hc_raw: bytes, denial_items: tuple[bytes,bytes,bytes,bytes,bytes,bytes]) -> bytes:
    outer_pid,inner_pid,starttime,dev,ino=guardian
    if inner_pid!=1 or hc_raw!=hook_custody_profile_preimage(): fail("release profile")
    hp,hm,hc=map(sha256,(hp_raw,hm_raw,hc_raw))
    binding=f"session={session} g_outer_pid={outer_pid} g_inner_pid=1 g_starttime={starttime} guardian_dev={dev} guardian_ino={ino} ep_p_local_receipt_sha256={hp} holder_matrix_receipt_sha256={hm} hook_custody_profile_sha256={hc}".encode("ascii")
    bundle=tagged_preimage("P15R-RELEASE-ENDPOINT-BUNDLE-v14",(hp_raw,hm_raw,hc_raw))
    attestation=tagged_preimage("P15R-PRIVILEGE-DROP-ATTESTATION-v14",(binding,)+denial_items+(bundle,))
    payload=b"PRIVILEGE_DROP_RELEASE "+binding+b" attestation_sha256="+sha256(attestation).encode("ascii")
    return exact_frame(payload)


def build_ready_frame(session: int, outer_pid: int, hp: str, hm: str, hc: str, hg: str, mech: str, contract: str) -> bytes:
    payload=f"GUARDIAN_READY session={session} outer_pid={outer_pid} inner_pid=1 ep_p_local_receipt_sha256={hp} holder_matrix_receipt_sha256={hm} hook_custody_profile_sha256={hc} ep_g_local_receipt_sha256={hg} mechanical_endpoint_receipt_sha256={mech} actual_endpoint_contract_sha256={contract}".encode("ascii")
    return exact_frame(payload)


def build_ack_frame(session: int, guardian: tuple[int,int,int,int,int], contract: str, launcher_frame: bytes, release_frame: bytes, ready_frame: bytes) -> bytes:
    outer_pid,inner_pid,starttime,dev,ino=guardian
    core=f"GUARDIAN_READY_ACK session={session} g_outer_pid={outer_pid} g_inner_pid={inner_pid} g_starttime={starttime} guardian_dev={dev} guardian_ino={ino} actual_endpoint_contract_sha256={contract} release_frame_sha256={sha256(release_frame)} ready_frame_sha256={sha256(ready_frame)} e_pg=0".encode("ascii")
    protocol=b"owner=P form=GUARDIAN_READY_ACK direction=P_TO_G channel=GLOBAL_CONTROL one_use=1 entropy=NONE"
    chain=tagged_preimage("P15R-GUARDIAN-READY-ACK-CARRIER-CHAIN-v14",(core,launcher_frame,release_frame,ready_frame,protocol))
    return exact_frame(core+b" ack_chain_sha256="+sha256(chain).encode("ascii"))


def build_seal_frame(session: int, guardian: tuple[int,int,int,int,int], contract: str, launcher_frame: bytes, release_frame: bytes, ready_frame: bytes, ack_frame: bytes) -> bytes:
    outer_pid,inner_pid,starttime,dev,ino=guardian
    core=f"BOOTSTRAP_SEALED session={session} g_outer_pid={outer_pid} g_inner_pid={inner_pid} g_starttime={starttime} guardian_dev={dev} guardian_ino={ino} actual_endpoint_contract_sha256={contract} release_frame_sha256={sha256(release_frame)} ready_frame_sha256={sha256(ready_frame)} ack_frame_sha256={sha256(ack_frame)} e_pg=0 e_gp=0".encode("ascii")
    protocol=b"owner=G form=BOOTSTRAP_SEALED direction=G_TO_P channel=GLOBAL_CONTROL one_use=1 entropy=NONE"
    chain=tagged_preimage("P15R-BOOTSTRAP-SEALED-CARRIER-CHAIN-v14",(core,launcher_frame,release_frame,ready_frame,ack_frame,protocol))
    return exact_frame(core+b" bootstrap_seal_sha256="+sha256(chain).encode("ascii"))


@dataclass(frozen=True)
class LocalEndpointFreeze:
    role: str
    raw_receipt: bytes
    evidence: EndpointIdentityEvidence
    st_dev: int
    st_ino: int

    @property
    def digest(self) -> str:
        return sha256(self.raw_receipt)


def freeze_actual_endpoint(endpoint: socket.socket, session: int, role: str, owner_outer_pid: int, owner_starttime: int, diag: UnixDiagOracle|None) -> LocalEndpointFreeze:
    if role not in ("EP_P","EP_G") or owner_outer_pid<=0 or owner_starttime<=0: fail("endpoint freeze coordinate")
    st0=os.fstat(endpoint.fileno()); netns0=os.stat("/proc/self/ns/net",follow_symlinks=True); domain0,type0,protocol0,cookie0=raw_actual_endpoint_identity(endpoint)
    if (domain0,type0,protocol0)!=(socket.AF_UNIX,socket.SOCK_SEQPACKET,0): fail("endpoint identity pre")
    if role=="EP_P":
        if diag is None: fail("EP_P diag oracle")
        observed0=diag.query(st0.st_ino)
        evidence=EndpointIdentityEvidence(netns0.st_dev,netns0.st_ino,cookie0,owner_outer_pid,owner_starttime,observed0.queried_inode,observed0.peer_inode,observed0.cookie0,observed0.cookie1)
    else:
        if diag is not None: fail("EP_G delegated diag")
        evidence=EndpointIdentityEvidence(netns0.st_dev,netns0.st_ino,cookie0,owner_outer_pid,owner_starttime)
    lock_actual_endpoint_filter(endpoint)
    st1=os.fstat(endpoint.fileno()); netns1=os.stat("/proc/self/ns/net",follow_symlinks=True); domain1,type1,protocol1,cookie1=raw_actual_endpoint_identity(endpoint)
    if (st0.st_dev,st0.st_ino,netns0.st_dev,netns0.st_ino,domain0,type0,protocol0,cookie0)!=(st1.st_dev,st1.st_ino,netns1.st_dev,netns1.st_ino,domain1,type1,protocol1,cookie1): fail("endpoint freeze identity drift")
    if role=="EP_P":
        observed1=diag.query(st1.st_ino)
        if (observed1.queried_inode,observed1.peer_inode,observed1.cookie0,observed1.cookie1)!=(evidence.udiag_ino_u32,evidence.udiag_peer_u32,evidence.udiag_cookie0_u32,evidence.udiag_cookie1_u32): fail("endpoint freeze diag drift")
    raw=build_owner_local_endpoint_receipt(endpoint,session,role,evidence)
    return LocalEndpointFreeze(role,raw,evidence,st1.st_dev,st1.st_ino)


def _proc_inode_ref_count(proc_root: int, pid: int, inode: int) -> tuple[int,tuple[int,...],int]:
    process=openat2(proc_root,str(pid),OPEN_PATH_DIR); directory=openat2(process,"fd",OPEN_PATH_DIR)
    try:
        matches=[]; device=0
        for name in os.listdir(directory):
            if re.fullmatch(r"0|[1-9][0-9]*",name) is None: fail("holder fd name")
            try: observed=os.stat(name,dir_fd=directory,follow_symlinks=True)
            except FileNotFoundError: fail("holder fd ABA")
            if stat.S_ISSOCK(observed.st_mode) and observed.st_ino==inode: matches.append(int(name)); device=observed.st_dev
        return len(matches),tuple(sorted(matches)),device
    finally:
        close_proved(directory); close_proved(process)


def collect_holder_matrix(proc_root: int, session: int, p_pid: int, p_starttime: int, guardian_pid: int, guardian_starttime: int, closed_design_pids: tuple[int,...], ep_p: LocalEndpointFreeze, diag: UnixDiagOracle) -> bytes:
    if ep_p.role!="EP_P" or ep_p.evidence.owner_outer_pid!=p_pid: fail("holder EP_P role")
    if len(closed_design_pids)!=len(set(closed_design_pids)) or any(pid<=0 or pid in (p_pid,guardian_pid) for pid in closed_design_pids): fail("holder design-process closure")
    for pid in closed_design_pids:
        try: os.stat(str(pid),dir_fd=proc_root,follow_symlinks=False)
        except FileNotFoundError: pass
        else: fail("holder closed design actor remains")
    for pid,wanted in ((p_pid,p_starttime),(guardian_pid,guardian_starttime)):
        process=openat2(proc_root,str(pid),OPEN_PATH_DIR)
        try:
            if proc_start_time(process,pid)!=wanted: fail("holder owner starttime")
        finally: close_proved(process)
    p_to_g=diag.query(ep_p.st_ino); g_to_p=diag.query(p_to_g.peer_inode)
    if g_to_p.peer_inode!=ep_p.st_ino: fail("holder reciprocal diag")
    p_ep_p,p_slots,p_dev=_proc_inode_ref_count(proc_root,p_pid,ep_p.st_ino); g_ep_p,g_p_slots,_=_proc_inode_ref_count(proc_root,guardian_pid,ep_p.st_ino)
    p_ep_g,p_g_slots,_=_proc_inode_ref_count(proc_root,p_pid,p_to_g.peer_inode); g_ep_g,g_slots,g_dev=_proc_inode_ref_count(proc_root,guardian_pid,p_to_g.peer_inode)
    if (p_ep_p,g_ep_p,p_ep_g,g_ep_g)!=(1,0,0,1) or len(p_slots)!=1 or len(g_slots)!=1 or g_p_slots or p_g_slots: fail("holder matrix cardinality")
    for pid,wanted in ((p_pid,p_starttime),(guardian_pid,guardian_starttime)):
        process=openat2(proc_root,str(pid),OPEN_PATH_DIR)
        try:
            if proc_start_time(process,pid)!=wanted: fail("holder owner starttime drift")
        finally: close_proved(process)
    pidns=os.stat("/proc/self/ns/pid",follow_symlinks=True); netns=os.stat("/proc/self/ns/net",follow_symlinks=True)
    p_row=HolderMatrixEndpoint("EP_P","P",p_pid,p_starttime,p_dev,ep_p.st_ino,p_to_g.queried_inode,p_to_g.peer_inode,p_to_g.cookie0,p_to_g.cookie1,1,0)
    g_row=HolderMatrixEndpoint("EP_G","G",guardian_pid,guardian_starttime,g_dev,p_to_g.peer_inode,g_to_p.queried_inode,g_to_p.peer_inode,g_to_p.cookie0,g_to_p.cookie1,0,1)
    return build_holder_matrix_receipt(session,(pidns.st_dev,pidns.st_ino),(netns.st_dev,netns.st_ino),p_row,g_row)


@dataclass(frozen=True)
class V14SealFence:
    session: int
    contract_sha256: str
    seal_receipt: EndpointEnqueueReceipt
    profile_gate_sha256: str

    def validate(self) -> None:
        receipt=self.seal_receipt
        if self.session<=0 or re.fullmatch(r"[0-9a-f]{64}",self.contract_sha256) is None or re.fullmatch(r"[0-9a-f]{64}",self.profile_gate_sha256) is None or (receipt.form,receipt.owner,receipt.direction)!=("BOOTSTRAP_SEALED","G","G_TO_P") or receipt.endpoint_dev<0 or receipt.endpoint_ino<=0 or not receipt.complete(): fail("Seal full-return fence")
        try: payload=receipt.framed_bytes[4:].decode("ascii")
        except UnicodeDecodeError: fail("Seal fence ASCII")
        values=parse_exact(payload,"BOOTSTRAP_SEALED",(("session",r"[1-9][0-9]*"),("g_outer_pid",r"[1-9][0-9]*"),("g_inner_pid",r"1"),("g_starttime",r"[1-9][0-9]*"),("guardian_dev",r"[0-9]+"),("guardian_ino",r"[1-9][0-9]*"),("actual_endpoint_contract_sha256",r"[0-9a-f]{64}"),("release_frame_sha256",r"[0-9a-f]{64}"),("ready_frame_sha256",r"[0-9a-f]{64}"),("ack_frame_sha256",r"[0-9a-f]{64}"),("e_pg",r"0"),("e_gp",r"0"),("bootstrap_seal_sha256",r"[0-9a-f]{64}")))
        if values["session"]!=str(self.session) or values["actual_endpoint_contract_sha256"]!=self.contract_sha256: fail("Seal fence contract")


def received_boundary_receipt(endpoint: socket.socket, sender: str, form: str, frame: bytes) -> EndpointEnqueueReceipt:
    direction="P_TO_G" if sender=="P" else "G_TO_P"; st=os.fstat(endpoint.fileno())
    if frame!=exact_frame(frame[4:]): fail("received boundary frame")
    return EndpointEnqueueReceipt(sender,direction,form,frame,len(frame),st.st_dev,st.st_ino)


def canonical_boundary_predecessors(ledger: BoundaryLedger) -> dict[str,bytes]:
    result={"LAUNCHER_REAPED":ledger.launcher_frame} if ledger.launcher_frame else {}
    for form in ("PRIVILEGE_DROP_RELEASE","GUARDIAN_READY","GUARDIAN_READY_ACK","BOOTSTRAP_SEALED"):
        if form in ledger.frames: result[form]=ledger.frames[form]
    if any(frame!=exact_frame(frame[4:]) for frame in result.values()): fail("canonical boundary predecessors")
    return result


def route_old_boundary_observation(ledger: BoundaryLedger, item: BoundaryFrameObservation, expected_form: str, expected_direction: str, consumed_slots: set[tuple[str,str]]) -> str:
    _declared,_payload,form,complete,grammar=item.parsed()
    if not (complete and grammar and form in OLD_BOUNDARY_FORMS): return "NOT_OLD_FORM"
    baselines=canonical_boundary_predecessors(ledger)
    key=(item.direction,form); out_of_slot=item.packet in baselines.values() or key in consumed_slots or key!=(expected_direction,expected_form)
    if not out_of_slot: return "AUTHORIZED_SLOT_CANDIDATE"
    pre_cut=ledger.record_old_form_extra("P" if item.direction=="P_TO_G" else "G",item.direction,item.packet,item.carrier_bits)
    return "PRIMARY_PRE_CUT" if pre_cut else "SECONDARY_POST_CUT"


def retain_v14_failure(ledger: BoundaryLedger, endpoint: socket.socket, owner: str, caught: BaseException, control: FramedControl, guardian: tuple[int,int,int,int,int], guardian_cgroup_valid: bool, holder_ceiling: bool, peer_crash_observed: bool=False) -> tuple[BoundaryFailureTombstone|None,BoundaryTerminalContext]:
    observed=os.fstat(endpoint.fileno()); sequence=(("PRIVILEGE_DROP_RELEASE","P_TO_G"),("GUARDIAN_READY","G_TO_P"),("GUARDIAN_READY_ACK","P_TO_G"),("BOOTSTRAP_SEALED","G_TO_P")); index=sum(ledger.bits)
    if index>=4: fail("sealed boundary cannot retain failure")
    expected_form,expected_direction=sequence[index]; outbound="P_TO_G" if owner=="P" else "G_TO_P"; inbound="G_TO_P" if owner=="P" else "P_TO_G"
    observations: list[BoundaryFrameObservation]=[]; secondary_observations: list[BoundaryFrameObservation]=[]
    semantic_label=caught.label if isinstance(caught,BoundaryProtocolFailure) else "NONE"; duplicate_failure=semantic_label=="DUPLICATE"; event_bits=tuple(ledger.bits)
    canonical_predecessors=canonical_boundary_predecessors(ledger); predecessor_budget={(form,frame):1 for form,frame in canonical_predecessors.items()}
    for receipt in control.boundary_outbound:
        key=(receipt.form,receipt.framed_bytes)
        if predecessor_budget.get(key,0): predecessor_budget[key]-=1; continue
        observations.append(boundary_observation(receipt.direction,"SEND_FULL_RETURN",receipt.framed_bytes,receipt.full_return_count,0,len(receipt.framed_bytes),carrier_bits=event_bits,semantic_label=semantic_label if receipt.framed_bytes==control.last_send_packet else "NONE"))
    if control.last_send_packet and control.last_send_count>=0 and control.last_send_count<len(control.last_send_packet):
        observations.append(boundary_observation(outbound,"SEND_PREFIX",control.last_send_packet[:control.last_send_count],control.last_send_count,control.last_transport_errno,len(control.last_send_packet),carrier_bits=event_bits,semantic_label=semantic_label))
    if (control.last_received_packet or control.last_received_flags or control.last_received_ancillary_count) and (duplicate_failure or not control.last_received_packet or control.last_received_packet not in canonical_predecessors.values()):
        observations.append(boundary_observation(inbound,"RECEIVE",control.last_received_packet,-1,control.last_transport_errno,len(control.last_received_packet),control.last_received_flags,control.last_received_ancillary_count,carrier_bits=event_bits,semantic_label=semantic_label))
    elif control.first_failure=="CONTROL_RECEIVE" and control.last_transport_errno>0:
        observations.append(boundary_observation(inbound,"RECEIVE",b"",-1,control.last_transport_errno,0,carrier_bits=event_bits,semantic_label=semantic_label))
    if control.first_failure_record and control.first_failure!="CONTROL_SEND_RECORD" and (duplicate_failure or control.first_failure_record not in canonical_predecessors.values()) and control.first_failure_record not in tuple(item.packet for item in observations):
        direction=outbound if control.first_failure in ("CONTROL_SEND","CONTROL_SEND_RECORD") else inbound
        retained=control.first_failure_record if direction==inbound else control.first_failure_record[:max(control.last_send_count,0)]
        observations.append(boundary_observation(direction,"RECEIVE" if direction==inbound else "SEND_PREFIX",retained,control.last_send_count if direction==outbound else -1,control.last_transport_errno,len(control.last_send_packet) if direction==outbound else len(control.first_failure_record),control.last_received_flags if direction==inbound else 0,control.last_received_ancillary_count if direction==inbound else 0,carrier_bits=event_bits,semantic_label=semantic_label))
    consumed_slots={(WIRE_SPECS[form].direction,form) for form in canonical_predecessors}
    for item in tuple(observations):
        _declared,_payload,form,complete,grammar=item.parsed(); route=route_old_boundary_observation(ledger,item,expected_form,expected_direction,consumed_slots)
        if route=="SECONDARY_POST_CUT": observations.remove(item); secondary_observations.append(item)
        if complete and grammar: consumed_slots.add((item.direction,form))
    if semantic_label!="NONE" and not any(item.semantic_label==semantic_label for item in observations) and any(item.semantic_label==semantic_label for item in secondary_observations): semantic_label="NONE"
    timeout_expired=isinstance(caught,OSError) and caught.errno==errno.ETIMEDOUT
    p_alive=owner=="P" or not peer_crash_observed; g_alive=owner=="G" or not peer_crash_observed
    evidence=derive_boundary_raw_evidence(observations=observations,canonical_predecessors=canonical_predecessors,expected_frames=ledger.expected_frames,expected_form=expected_form,expected_direction=expected_direction,session=ledger.session,guardian=guardian,guardian_cgroup_valid=guardian_cgroup_valid,semantic_label=semantic_label,eof_observed=control.eof_observed,timeout_expired=timeout_expired,p_alive=p_alive,g_alive=g_alive,checkpoint_closed=False)
    reconciler=TerminalBoundaryReconciler(ledger); reconciler.stop_scope(); endpoint_identity=(observed.st_dev,observed.st_ino)
    holder_ceiling=holder_ceiling and not control.received_rights_violation
    tombstone=None if holder_ceiling else reconciler.retain_unreconciled(owner,endpoint_identity,evidence)
    context=BoundaryTerminalContext(owner,reconciler,evidence,endpoint_identity,expected_form,expected_direction,holder_ceiling,observations,secondary_observations,semantic_label,guardian,guardian_cgroup_valid,p_alive,g_alive,timeout_expired)
    return tombstone,context


def complete_v14_terminal_survivor(context: BoundaryTerminalContext, endpoint: socket.socket, control: FramedControl, receipts: Mapping[str,str], peer_death_reaped: bool) -> BoundaryFailureReceipt|BoundaryTerminalSuccessReceipt:
    if context.owner!="P" or not peer_death_reaped or endpoint.fileno()<0: fail("terminal survivor authority")
    observed=os.fstat(endpoint.fileno())
    if (observed.st_dev,observed.st_ino)!=context.endpoint_identity: fail("terminal endpoint identity drift")
    sequence=(("PRIVILEGE_DROP_RELEASE","P_TO_G"),("GUARDIAN_READY","G_TO_P"),("GUARDIAN_READY_ACK","P_TO_G"),("BOOTSTRAP_SEALED","G_TO_P")); terminal_receipts=dict(receipts)

    def expected_matches(form: str, packet: bytes) -> bool:
        expected=context.reconciler.ledger.expected_frames.get(form)
        if expected is not None: return expected==packet
        if form!="GUARDIAN_READY": return False
        try:
            record=packet[4:].decode("ascii")
            values=parse_exact(record,"GUARDIAN_READY",(("session",str(context.reconciler.ledger.session)),("outer_pid",str(context.guardian[0])),("inner_pid",r"1"),("ep_p_local_receipt_sha256",re.escape(terminal_receipts["hp"])),("holder_matrix_receipt_sha256",re.escape(terminal_receipts["hm"])),("hook_custody_profile_sha256",re.escape(HOOK_CUSTODY_PROFILE_SHA256)),("ep_g_local_receipt_sha256",r"[0-9a-f]{64}"),("mechanical_endpoint_receipt_sha256",r"[0-9a-f]{64}"),("actual_endpoint_contract_sha256",r"[0-9a-f]{64}")))
            mechanical=sha256(build_mechanical_endpoint_receipt(context.reconciler.ledger.session,terminal_receipts["hp"],values["ep_g_local_receipt_sha256"],terminal_receipts["hm"])); contract=sha256(actual_endpoint_contract(context.reconciler.ledger.session,mechanical,HOOK_CUSTODY_PROFILE_SHA256))
            expected=build_ready_frame(context.reconciler.ledger.session,context.guardian[0],terminal_receipts["hp"],terminal_receipts["hm"],HOOK_CUSTODY_PROFILE_SHA256,values["ep_g_local_receipt_sha256"],mechanical,contract)
        except (PossessionFailure,KeyError,UnicodeError): return False
        if packet!=expected or (values["mechanical_endpoint_receipt_sha256"],values["actual_endpoint_contract_sha256"])!=(mechanical,contract): return False
        context.reconciler.ledger.expect_carrier(form,expected); terminal_receipts.update({"hg":values["ep_g_local_receipt_sha256"],"mech":mechanical,"contract":contract}); return True

    consumed_slots={(WIRE_SPECS[form].direction,form) for form in canonical_boundary_predecessors(context.reconciler.ledger)}
    for item in tuple(context.observations):
        _declared,_payload,form,complete,grammar=item.parsed(); index=sum(context.reconciler.ledger.bits)
        key=(item.direction,form); eligible=complete and grammar and not item.message_flags and item.ancillary_count==0 and index<4 and form==sequence[index][0] and item.direction==sequence[index][1] and key not in consumed_slots
        if eligible and expected_matches(form,item.packet):
            receipt=EndpointEnqueueReceipt("P" if item.direction=="P_TO_G" else "G",item.direction,form,item.packet,len(item.packet),context.endpoint_identity[0],context.endpoint_identity[1])
            context.reconciler.ledger.commit_carrier(receipt)
            context.observations.remove(item)
        elif eligible:
            marked=replace(item,semantic_label="WRONG_ATTESTATION"); context.observations[context.observations.index(item)]=marked
        else:
            if complete and grammar and index<4 and key==(sequence[index][1],sequence[index][0]) and key in consumed_slots:
                marked=replace(item,semantic_label="WRONG_STATE"); context.observations[context.observations.index(item)]=marked; item=marked
            expected_now=sequence[index] if index<4 else ("BOOTSTRAP_SEALED","G_TO_P"); route=route_old_boundary_observation(context.reconciler.ledger,item,*expected_now,consumed_slots)
            if route=="SECONDARY_POST_CUT": context.observations.remove(item); context.secondary_observations.append(item)
        if complete and grammar: consumed_slots.add(key)
    if context.semantic_label!="NONE" and not any(item.semantic_label==context.semantic_label for item in context.observations) and any(item.semantic_label==context.semantic_label for item in context.secondary_observations): context.semantic_label="NONE"
    exact_eof=False
    terminal_ancillary_space=socket.CMSG_SPACE(array.array("i",[0]*16).itemsize)
    while True:
        packet,ancillary,flags,_address=endpoint.recvmsg(MAX_FRAME+5,terminal_ancillary_space)
        received_fds=received_rights(ancillary)
        if received_fds or flags&socket.MSG_CTRUNC: context.holder_ceiling=False
        discard_rights(received_fds)
        event_bits=tuple(context.reconciler.ledger.bits)
        if not packet:
            if ancillary or flags:
                observation=boundary_observation("G_TO_P","TERMINAL_DRAIN",b"",-1,0,0,flags,len(ancillary),carrier_bits=event_bits)
                (context.secondary_observations if event_bits[3] else context.observations).append(observation)
                continue
            exact_eof=True; break
        declared=int.from_bytes(packet[:4],"big") if len(packet)>=4 else -1
        intended_length=4+declared if 0<declared<=MAX_FRAME else len(packet)
        observation=boundary_observation("G_TO_P","TERMINAL_DRAIN",bytes(packet),-1,0,intended_length,flags,len(ancillary),carrier_bits=event_bits)
        _declared,_payload,form,complete,grammar=observation.parsed(); spec=WIRE_SPECS.get(form) if grammar else None
        index=sum(context.reconciler.ledger.bits)
        key=("G_TO_P",form); eligible=not flags and not ancillary and complete and grammar and spec is not None and spec.direction=="G_TO_P" and index<4 and (form,"G_TO_P")==sequence[index] and key not in consumed_slots
        if eligible and expected_matches(form,bytes(packet)):
            context.reconciler.ledger.commit_carrier(received_boundary_receipt(endpoint,"G",form,bytes(packet)))
        elif eligible:
            context.observations.append(replace(observation,semantic_label="WRONG_ATTESTATION"))
        else:
            if complete and grammar and index<4 and key==(sequence[index][1],sequence[index][0]) and key in consumed_slots: observation=replace(observation,semantic_label="WRONG_STATE")
            expected_now=sequence[index] if index<4 else ("BOOTSTRAP_SEALED","G_TO_P"); route=route_old_boundary_observation(context.reconciler.ledger,observation,*expected_now,consumed_slots)
            target=context.secondary_observations if route=="SECONDARY_POST_CUT" or event_bits[3] else context.observations
            target.append(observation)
        if complete and grammar: consumed_slots.add(key)
    endpoint_fd=endpoint.fileno(); endpoint.close(); immediate_ebadf(endpoint_fd)
    required=("hp","hg","hm","mech","contract","profile")
    if set(terminal_receipts)!=set(required) or any(value!="NONE" and re.fullmatch(r"[0-9a-f]{64}",value) is None for value in terminal_receipts.values()) or terminal_receipts["profile"]!=HOOK_CUSTODY_PROFILE_SHA256: fail("terminal receipt hashes")
    if sum(context.reconciler.ledger.bits)==4:
        if not exact_eof or not context.holder_ceiling: fail("terminal Seal audit ceiling")
        vector,row_class=context.reconciler.ledger.c14()
        if (vector,row_class)!=((1,1,1,1,0,0),"BOOTSTRAP_SEALED_COMMIT"): fail("terminal Seal row")
        frames=(("LAUNCHER_REAPED",context.reconciler.ledger.launcher_frame,sha256(context.reconciler.ledger.launcher_frame)),)+tuple((form,frame,sha256(frame)) for form,frame in context.reconciler.ledger.frames.items()); context.reconciler.ledger.reconciling=False
        return BoundaryTerminalSuccessReceipt(context.reconciler.ledger.session,vector,row_class,frames,context.endpoint_identity,terminal_receipts["hp"],terminal_receipts["hg"],terminal_receipts["hm"],terminal_receipts["mech"],terminal_receipts["contract"],terminal_receipts["profile"],exact_eof,True,tuple(context.secondary_observations)+tuple(context.observations))
    final_index=sum(context.reconciler.ledger.bits); expected_form,expected_direction=sequence[final_index]
    evidence=derive_boundary_raw_evidence(observations=context.observations,canonical_predecessors=canonical_boundary_predecessors(context.reconciler.ledger),expected_frames=context.reconciler.ledger.expected_frames,expected_form=expected_form,expected_direction=expected_direction,session=context.reconciler.ledger.session,guardian=context.guardian,guardian_cgroup_valid=context.guardian_cgroup_valid,semantic_label=context.semantic_label,eof_observed=context.evidence.eof_observed or exact_eof,timeout_expired=context.timeout_expired,p_alive=context.p_alive,g_alive=context.g_alive,checkpoint_closed=True)
    return context.reconciler.freeze(owners=("P",),owner_evidence={"P":evidence},expected_form=expected_form,expected_direction=expected_direction,endpoint_identity=context.endpoint_identity,exact_eof=exact_eof,no_alternate_reader=context.holder_ceiling,no_future_producer=peer_death_reaped,survivor_close_receipt=(0,errno.EBADF),peer_death_reaped=peer_death_reaped,receipts=terminal_receipts,secondary_observations=tuple(context.secondary_observations)+tuple(context.observations))


def combine_outcomes(values: Iterable[str]) -> str:
    material=tuple(values)
    if not material or any(value not in OUTCOMES for value in material): fail("outcome aggregation")
    return max(material,key=lambda value:OUTCOME_PRECEDENCE[value])


def v7_bind(domain: str, identity: bytes, payload: bytes) -> str:
    if not domain.isascii() or "\x00" in domain:
        fail("v7 binding domain")
    return sha256(domain.encode("ascii")+b"\x00"+struct.pack(">Q",len(identity))+identity+struct.pack(">Q",len(payload))+payload)


def complete_write(fd: int, data: bytes) -> None:
    view = memoryview(data)
    while view:
        try:
            count = os.write(fd,view)
        except InterruptedError:
            continue
        if count <= 0:
            fail("short write")
        view = view[count:]


def read_all(fd: int) -> bytes:
    parts: list[bytes] = []
    while True:
        try:
            part = os.read(fd,65536)
        except InterruptedError:
            continue
        if not part:
            return b"".join(parts)
        parts.append(part)


def getrandom32(kind: str, retained: list[tuple[str,bytearray]]) -> bytearray:
    if kind not in {"PREFLIGHT_ONLY","create_cap","reply_nonce","active_cap","terminal_cap"}:
        fail("entropy kind")
    buffer = (ctypes.c_ubyte*32)()
    offset = 0
    while offset < 32:
        try:
            count = syscall(SYS_GETRANDOM,ctypes.byref(buffer,offset),ctypes.c_size_t(32-offset),ctypes.c_uint(0))
        except OSError as error:
            if error.errno == errno.EINTR:
                continue
            partial = bytearray(bytes(buffer)[:offset])
            retained.append((kind+":PARTIAL",partial))
            raise
        if count <= 0 or count > 32-offset:
            retained.append((kind+":PARTIAL",bytearray(bytes(buffer)[:offset])))
            fail("getrandom return")
        offset += count
    value = bytearray(bytes(buffer))
    for _old_kind,old in retained:
        if len(old) == 32 and old == value:
            retained.append((kind+":COLLISION",value))
            fail("entropy collision")
    retained.append((kind,value))
    return value


def erase_secrets(values: list[tuple[str,bytearray]]) -> None:
    for _kind,value in values:
        for index in range(len(value)):
            value[index] = 0


def received_rights(ancillary: Sequence[tuple[int,int,bytes]]) -> list[int]:
    item_size=array.array("i").itemsize; result=[]
    for level,kind,data in ancillary:
        if (level,kind)!=(socket.SOL_SOCKET,socket.SCM_RIGHTS): continue
        usable=len(data)-(len(data)%item_size)
        if usable:
            values=array.array("i"); values.frombytes(data[:usable]); result.extend(values)
    return result


def discard_rights(values: Iterable[int]) -> None:
    for fd in values:
        if fd_is_open(fd): close_proved(fd)


class CloneArgs(ctypes.Structure):
    _fields_ = (
        ("flags",ctypes.c_uint64),("pidfd",ctypes.c_uint64),("child_tid",ctypes.c_uint64),("parent_tid",ctypes.c_uint64),("exit_signal",ctypes.c_uint64),
        ("stack",ctypes.c_uint64),("stack_size",ctypes.c_uint64),("tls",ctypes.c_uint64),("set_tid",ctypes.c_uint64),("set_tid_size",ctypes.c_uint64),("cgroup",ctypes.c_uint64),
    )


class OpenHow(ctypes.Structure):
    _fields_ = (("flags",ctypes.c_uint64),("mode",ctypes.c_uint64),("resolve",ctypes.c_uint64))


class SockFilter(ctypes.Structure):
    _fields_ = (("code",ctypes.c_ushort),("jt",ctypes.c_ubyte),("jf",ctypes.c_ubyte),("k",ctypes.c_uint32))


class SockFprog(ctypes.Structure):
    _fields_ = (("len",ctypes.c_ushort),("filter",ctypes.POINTER(SockFilter)))


class CapHeader(ctypes.Structure):
    _fields_ = (("version",ctypes.c_uint32),("pid",ctypes.c_int))


class CapData(ctypes.Structure):
    _fields_ = (("effective",ctypes.c_uint32),("permitted",ctypes.c_uint32),("inheritable",ctypes.c_uint32))


class StatFs(ctypes.Structure):
    _fields_ = (
        ("f_type",ctypes.c_long),("f_bsize",ctypes.c_long),("f_blocks",ctypes.c_ulong),("f_bfree",ctypes.c_ulong),
        ("f_bavail",ctypes.c_ulong),("f_files",ctypes.c_ulong),("f_ffree",ctypes.c_ulong),("f_fsid",ctypes.c_int*2),
        ("f_namelen",ctypes.c_long),("f_frsize",ctypes.c_long),("f_flags",ctypes.c_long),("f_spare",ctypes.c_long*4),
    )


@dataclass(frozen=True)
class WireSpec:
    direction: str
    pattern: re.Pattern[str]
    cardinality: str


WIRE_SPECS: dict[str,WireSpec] = {
    "PID1_READY":WireSpec("G_TO_P",re.compile(r"PID1_READY outer_pid=[1-9][0-9]* inner_pid=1"),"ONCE"),
    "WORKERS_CGROUP_FD":WireSpec("P_TO_G",re.compile(r"WORKERS_CGROUP_FD session=0"),"ONCE"),
    "WORKERS_CGROUP_FD_ACK":WireSpec("G_TO_P",re.compile(r"WORKERS_CGROUP_FD_ACK session=0"),"ONCE"),
    "CGROUP_PROBE_CHILD":WireSpec("G_TO_P",re.compile(r"CGROUP_PROBE_CHILD epoch=[12] inner_pid=[1-9][0-9]*"),"PER_EPOCH"),
    "CGROUP_PROBE_FROZEN":WireSpec("P_TO_G",re.compile(r"CGROUP_PROBE_FROZEN epoch=1"),"PER_EPOCH"),
    "CGROUP_PROBE_THAWED":WireSpec("P_TO_G",re.compile(r"CGROUP_PROBE_THAWED epoch=1"),"PER_EPOCH"),
    "CGROUP_PROBE_KILLED":WireSpec("P_TO_G",re.compile(r"CGROUP_PROBE_KILLED epoch=2"),"PER_EPOCH"),
    "CGROUP_PROBE_REAPED":WireSpec("G_TO_P",re.compile(r"CGROUP_PROBE_REAPED epoch=[12]"),"PER_EPOCH"),
    "LAUNCHER_REAPED":WireSpec("P_TO_G",re.compile(r"LAUNCHER_REAPED outer_pid=[1-9][0-9]*"),"ONCE"),
    "PRIVILEGE_DROP_RELEASE":WireSpec("P_TO_G",re.compile(r"PRIVILEGE_DROP_RELEASE session=[1-9][0-9]* g_outer_pid=[1-9][0-9]* g_inner_pid=1 g_starttime=[1-9][0-9]* guardian_dev=[0-9]+ guardian_ino=[1-9][0-9]* ep_p_local_receipt_sha256=[0-9a-f]{64} holder_matrix_receipt_sha256=[0-9a-f]{64} hook_custody_profile_sha256=[0-9a-f]{64} attestation_sha256=[0-9a-f]{64}"),"ONCE"),
    "GUARDIAN_READY":WireSpec("G_TO_P",re.compile(r"GUARDIAN_READY session=[1-9][0-9]* outer_pid=[1-9][0-9]* inner_pid=1 ep_p_local_receipt_sha256=[0-9a-f]{64} holder_matrix_receipt_sha256=[0-9a-f]{64} hook_custody_profile_sha256=[0-9a-f]{64} ep_g_local_receipt_sha256=[0-9a-f]{64} mechanical_endpoint_receipt_sha256=[0-9a-f]{64} actual_endpoint_contract_sha256=[0-9a-f]{64}"),"ONCE"),
    "GUARDIAN_READY_ACK":WireSpec("P_TO_G",re.compile(r"GUARDIAN_READY_ACK session=[1-9][0-9]* g_outer_pid=[1-9][0-9]* g_inner_pid=1 g_starttime=[1-9][0-9]* guardian_dev=[0-9]+ guardian_ino=[1-9][0-9]* actual_endpoint_contract_sha256=[0-9a-f]{64} release_frame_sha256=[0-9a-f]{64} ready_frame_sha256=[0-9a-f]{64} e_pg=0 ack_chain_sha256=[0-9a-f]{64}"),"ONCE"),
    "BOOTSTRAP_SEALED":WireSpec("G_TO_P",re.compile(r"BOOTSTRAP_SEALED session=[1-9][0-9]* g_outer_pid=[1-9][0-9]* g_inner_pid=1 g_starttime=[1-9][0-9]* guardian_dev=[0-9]+ guardian_ino=[1-9][0-9]* actual_endpoint_contract_sha256=[0-9a-f]{64} release_frame_sha256=[0-9a-f]{64} ready_frame_sha256=[0-9a-f]{64} ack_frame_sha256=[0-9a-f]{64} e_pg=0 e_gp=0 bootstrap_seal_sha256=[0-9a-f]{64}"),"ONCE"),
    "CHILD_REGISTERED":WireSpec("G_TO_P",re.compile(r"CHILD_REGISTERED session=[0-9]+ child=[1-9][0-9]* inner_pid=[1-9][0-9]* role=[A-Z0-9_]+ owner=[A-Za-z0-9_]+ purpose=[A-Z0-9_]+ admission=[A-Za-z0-9_:]+ fdset=[A-Z0-9_]+ cwd_dev=[0-9]+ cwd_ino=[1-9][0-9]*"),"PER_CHILD"),
    "CHILD_REGISTERED_AUDITED":WireSpec("G_TO_P",re.compile(r"CHILD_REGISTERED_AUDITED session=[0-9]+ child=[1-9][0-9]* inner_pid=[1-9][0-9]* role=[A-Z0-9_]+ owner=[A-Za-z0-9_]+ purpose=[A-Z0-9_]+ admission=[A-Za-z0-9_:]+ fdset=[A-Z0-9_]+ cwd_dev=[0-9]+ cwd_ino=[1-9][0-9]* target=[A-Z0-9_]+ trigger=[A-Z0-9_]+ request=[1-9][0-9]* requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) serial=(?:0|[1-9][0-9]*) nonce=[0-9a-f]{64} digest=[0-9a-f]{64}"),"PER_CHILD"),
    "CHILD_ADMITTED":WireSpec("P_TO_G",re.compile(r"CHILD_ADMITTED session=[0-9]+ child=[1-9][0-9]* admission=[A-Za-z0-9_:]+"),"PER_CHILD"),
    "SOURCE_READY":WireSpec("G_TO_P",re.compile(r"SOURCE_READY session=[0-9]+ child=[1-9][0-9]* admission=[A-Za-z0-9_:]+ fdset=[A-Z0-9_]+"),"PER_CHILD"),
    "START":WireSpec("P_TO_G",re.compile(r"START session=[0-9]+ child=[1-9][0-9]* admission=[A-Za-z0-9_:]+"),"PER_CHILD"),
    "CHILD_REAPED":WireSpec("G_TO_P",re.compile(r"CHILD_REAPED session=[0-9]+ child=[1-9][0-9]* status=[0-9]+"),"PER_CHILD"),
    "CHILD_REAPED_ACK":WireSpec("P_TO_G",re.compile(r"CHILD_REAPED_ACK session=[0-9]+ child=[1-9][0-9]* status=[0-9]+"),"PER_CHILD"),
    "OBJECT_REGISTERED":WireSpec("G_TO_P",re.compile(r"OBJECT_REGISTERED session=[0-9]+ handle=[1-9][0-9]* kind=(?:ROOT_PARENT|ROOT|ROOT_MEMBER|LOCK_PARENT|LOCK|LOCK_MEMBER) dev=[0-9]+ ino=[1-9][0-9]*"),"PER_OBJECT"),
    "OBJECT_REGISTERED_ACK":WireSpec("P_TO_G",re.compile(r"OBJECT_REGISTERED_ACK session=[0-9]+ handle=[1-9][0-9]* kind=(?:ROOT_PARENT|ROOT|ROOT_MEMBER|LOCK_PARENT|LOCK|LOCK_MEMBER) dev=[0-9]+ ino=[1-9][0-9]*"),"PER_OBJECT"),
    "OBJECT_RELEASED":WireSpec("G_TO_P",re.compile(r"OBJECT_RELEASED session=[0-9]+ handle=[1-9][0-9]* kind=(?:ROOT_PARENT|ROOT|ROOT_MEMBER|LOCK_PARENT|LOCK|LOCK_MEMBER) dev=[0-9]+ ino=[1-9][0-9]*"),"PER_OBJECT"),
    "MEMBER_CREATE_AUTHORIZED":WireSpec("G_TO_P",re.compile(r"MEMBER_CREATE_AUTHORIZED session=[0-9]+ child=[1-9][0-9]* root=[1-9][0-9]* target=(?:GENERATE_CANONICAL_A|GENERATE_CANONICAL_B|GENERATE_MUTATION) purpose=[A-Z0-9_]+ basename_set=GENERATED_NINE_V1 primitive=DIRFD_O_CREAT_O_EXCL_O_NOFOLLOW"),"PER_CREATOR"),
    "MEMBER_CREATE_ACK":WireSpec("P_TO_G",re.compile(r"MEMBER_CREATE_ACK session=[0-9]+ child=[1-9][0-9]* root=[1-9][0-9]* purpose=[A-Z0-9_]+ basename_set=GENERATED_NINE_V1"),"PER_CREATOR"),
    "AUDIT_FD_REQUEST":WireSpec("G_TO_P",re.compile(r"AUDIT_FD_REQUEST session=[0-9]+ child=[1-9][0-9]* target=(?:TOP_TEST_CONTROLS|COPIED_REPRODUCE) role=(?:TOP_TEST_RUNNER|REQUESTER) owner=[A-Za-z0-9_]+ purpose=NONE"),"PER_CHILD"),
    "AUDIT_FD_GRANTED":WireSpec("P_TO_G",re.compile(r"AUDIT_FD_GRANTED session=[0-9]+ child=[1-9][0-9]* audit=[0-9]+"),"PER_CHILD"),
    "AUDITED_RPC_ACCEPTED":WireSpec("G_TO_P",re.compile(r"AUDITED_RPC_ACCEPTED requester_session=[1-9][0-9]* requester_child=[1-9][0-9]* audit=[0-9]+ serial=[0-9]+ nonce=[0-9a-f]{64} digest=[0-9a-f]{64} rpc_inner_pid=[1-9][0-9]* rpc_inner_uid=0 rpc_inner_gid=0 payload=(?:[0-9a-f]{2})+"),"PER_AUDIT_REQUEST"),
    "AUDITED_RPC_CONFIRMED":WireSpec("P_TO_G",re.compile(r"AUDITED_RPC_CONFIRMED requester_session=[1-9][0-9]* requester_child=[1-9][0-9]* audit=[0-9]+ serial=[0-9]+ nonce=[0-9a-f]{64} digest=[0-9a-f]{64}"),"PER_AUDIT_REQUEST"),
    "MEMBER_LEDGER_CLOSED":WireSpec("G_TO_P",re.compile(r"MEMBER_LEDGER_CLOSED session=[0-9]+ child=[1-9][0-9]* root=[1-9][0-9]* count=[0-9]+"),"PER_CREATOR"),
    "MEMBER_LEDGER_ACK":WireSpec("P_TO_G",re.compile(r"MEMBER_LEDGER_ACK session=[0-9]+ child=[1-9][0-9]* root=[1-9][0-9]* count=[0-9]+"),"PER_CREATOR"),
    "LOCK_BOUND":WireSpec("G_TO_P",re.compile(r"LOCK_BOUND session=0 lock=[1-9][0-9]*"),"ONCE"),
    "FREEZE_REQUEST":WireSpec("G_TO_P",re.compile(r"FREEZE_REQUEST session=[0-9]+ handle=[0-9]+ phase=(?:METHOD|FINAL)"),"PER_FREEZE"),
    "FROZEN_NOREFS":WireSpec("P_TO_G",re.compile(r"FROZEN_NOREFS session=[1-9][0-9]* handle=[1-9][0-9]* phase=METHOD epoch=[1-9][0-9]*"),"PER_FREEZE"),
    "FROZEN_FINAL":WireSpec("P_TO_G",re.compile(r"FROZEN_FINAL session=0 handle=0 phase=FINAL epoch=[1-9][0-9]*"),"ONCE"),
    "CLEANUP_COMMITTED":WireSpec("G_TO_P",re.compile(r"CLEANUP_COMMITTED session=[1-9][0-9]* handle=[1-9][0-9]* epoch=[1-9][0-9]*"),"PER_FREEZE"),
    "THAWED":WireSpec("P_TO_G",re.compile(r"THAWED session=[1-9][0-9]* handle=[1-9][0-9]* epoch=[1-9][0-9]*"),"PER_FREEZE"),
    "KILL_REQUEST":WireSpec("G_TO_P",re.compile(r"KILL_REQUEST session=0 epoch=[1-9][0-9]*"),"ONCE"),
    "KILL_ISSUED":WireSpec("P_TO_G",re.compile(r"KILL_ISSUED session=0 epoch=[1-9][0-9]*"),"ONCE"),
    "REAPED":WireSpec("G_TO_P",re.compile(r"REAPED session=0 epoch=[1-9][0-9]*"),"ONCE"),
    "CGROUP_EMPTY":WireSpec("P_TO_G",re.compile(r"CGROUP_EMPTY session=0 epoch=[1-9][0-9]*"),"ONCE"),
    "CLEANUP_RESULT":WireSpec("G_TO_P",re.compile(r"CLEANUP_RESULT session=0 handle=[0-9]+ outcome=(?:UNSET|ABSENT|DISPLACED_OWNED|DISPLACED_CLEANED|FOREIGN_RETAINED|ERROR|CRASH_TEARDOWN)"),"PER_OBJECT"),
    "SIGNAL_PENDING":WireSpec("P_TO_G",re.compile(r"SIGNAL_PENDING signo=[1-9][0-9]*"),"PER_SIGNAL"),
    "SIGNAL_CLEANED":WireSpec("G_TO_P",re.compile(r"SIGNAL_CLEANED signo=[1-9][0-9]* outcome=(?:UNSET|ABSENT|DISPLACED_OWNED|DISPLACED_CLEANED|FOREIGN_RETAINED|ERROR|CRASH_TEARDOWN)"),"PER_SIGNAL"),
    "EXIT":WireSpec("G_TO_P",re.compile(rf"EXIT status=0 outcome={OUTCOME_RE}"),"ONCE"),
    "FD_AUDIT_QUIESCE_ENTER":WireSpec("P_TO_G",re.compile(r"FD_AUDIT_QUIESCE_ENTER audit_epoch=[1-9][0-9]* kind=(?:PREFLIGHT_PROBE|RUNTIME_CHILD) session=[0-9]+ child=[1-9][0-9]* slot=(?:FD4|FD5|FD8) child_pidfd_serial=[1-9][0-9]* guardian_pidfd_serial=[1-9][0-9]*"),"PER_AUDIT"),
    "FD_AUDIT_QUIESCE_ACK":WireSpec("G_TO_P",re.compile(r"FD_AUDIT_QUIESCE_ACK audit_epoch=[1-9][0-9]* kind=(?:PREFLIGHT_PROBE|RUNTIME_CHILD) session=[0-9]+ child=[1-9][0-9]* slot=(?:FD4|FD5|FD8) g_fd_generation=[1-9][0-9]*"),"PER_AUDIT"),
    "FD_AUDIT_QUIESCE_EXIT":WireSpec("P_TO_G",re.compile(r"FD_AUDIT_QUIESCE_EXIT audit_epoch=[1-9][0-9]* kind=(?:PREFLIGHT_PROBE|RUNTIME_CHILD) session=[0-9]+ child=[1-9][0-9]* slot=(?:FD4|FD5|FD8) g_fd_generation=[1-9][0-9]* outcome=(?:PASS|ABORT) transcript=[0-9a-f]{64}"),"PER_AUDIT"),
    "FD_AUDIT_QUIESCE_EXIT_ACK":WireSpec("G_TO_P",re.compile(r"FD_AUDIT_QUIESCE_EXIT_ACK audit_epoch=[1-9][0-9]* kind=(?:PREFLIGHT_PROBE|RUNTIME_CHILD) session=[0-9]+ child=[1-9][0-9]* slot=(?:FD4|FD5|FD8) g_fd_generation=[1-9][0-9]* outcome=(?:PASS|ABORT) transcript=[0-9a-f]{64}"),"PER_AUDIT"),
    "SESSION_AUTH_CREATE_GRANTED":WireSpec("P_TO_G",re.compile(r"SESSION_AUTH_CREATE_GRANTED requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* request=[1-9][0-9]* registration_digest=[0-9a-f]{64} create_commitment=[0-9a-f]{64} template=(?:[0-9a-f]{2})+ fd4_endpoint_inode=[1-9][0-9]* rpc_inner_pid=[1-9][0-9]* rpc_inner_uid=0 rpc_inner_gid=0"),"PER_AUTH"),
    "SESSION_AUTH_CREATE_ACCEPTED":WireSpec("G_TO_P",re.compile(r"SESSION_AUTH_CREATE_ACCEPTED requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* request=[1-9][0-9]* registration_digest=[0-9a-f]{64} create_commitment=[0-9a-f]{64} create_cap=[0-9a-f]{64} payload=(?:[0-9a-f]{2})+ fd4_endpoint_inode=[1-9][0-9]* rpc_inner_pid=[1-9][0-9]* rpc_inner_uid=0 rpc_inner_gid=0"),"PER_AUTH"),
    "SESSION_AUTH_COMMIT":WireSpec("P_TO_G",re.compile(r"SESSION_AUTH_COMMIT requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* request=[1-9][0-9]* reply_nonce=[0-9a-f]{64} created=(?:[0-9a-f]{2})+"),"PER_AUTH"),
    "SESSION_AUTH_COMMITTED":WireSpec("G_TO_P",re.compile(r"SESSION_AUTH_COMMITTED requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* request=[1-9][0-9]* reply_nonce=[0-9a-f]{64} created=(?:[0-9a-f]{2})+"),"PER_AUTH"),
    "SESSION_AUTH_ACTIVE":WireSpec("P_TO_G",re.compile(r"SESSION_AUTH_ACTIVE requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* request=[1-9][0-9]* active_cap_commitment=[0-9a-f]{64} created_digest=[0-9a-f]{64}"),"PER_AUTH"),
    "SESSION_AUTH_ACTIVE_ACK":WireSpec("G_TO_P",re.compile(r"SESSION_AUTH_ACTIVE_ACK requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* request=[1-9][0-9]* active_cap_commitment=[0-9a-f]{64} created_digest=[0-9a-f]{64}"),"PER_AUTH"),
    "SESSION_AUTH_ABORT":WireSpec("P_TO_G",re.compile(rf"SESSION_AUTH_ABORT requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* phase=(?:{'|'.join(sorted(AUTH_PHASES))}) reason=(?:{'|'.join(sorted(AUTH_REASONS))})"),"PER_AUTH"),
    "SESSION_AUTH_ABORTED":WireSpec("G_TO_P",re.compile(rf"SESSION_AUTH_ABORTED requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* phase=(?:{'|'.join(sorted(AUTH_PHASES))}) reason=(?:{'|'.join(sorted(AUTH_REASONS))}) outcome={OUTCOME_RE}"),"PER_AUTH"),
    "SESSION_AUTH_TERMINAL_PREPARED":WireSpec("G_TO_P",re.compile(rf"SESSION_AUTH_TERMINAL_PREPARED requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* close_request=[1-9][0-9]* outcome={OUTCOME_RE} terminal_template=(?:[0-9a-f]{{2}})+"),"PER_AUTH"),
    "SESSION_AUTH_TERMINAL_GRANTED":WireSpec("P_TO_G",re.compile(rf"SESSION_AUTH_TERMINAL_GRANTED requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* close_request=[1-9][0-9]* outcome={OUTCOME_RE} terminal_cap=[0-9a-f]{{64}} reply_digest=[0-9a-f]{{64}} reply=(?:[0-9a-f]{{2}})+"),"PER_AUTH"),
    "SESSION_AUTH_FINALIZE":WireSpec("P_TO_G",re.compile(rf"SESSION_AUTH_FINALIZE requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* close_request=[1-9][0-9]* outcome={OUTCOME_RE} terminal_cap_sha256=[0-9a-f]{{64}} reply_digest=[0-9a-f]{{64}}"),"PER_AUTH"),
    "SESSION_AUTH_FINALIZED_ACK":WireSpec("G_TO_P",re.compile(rf"SESSION_AUTH_FINALIZED_ACK requester_session=0 requester_child=[1-9][0-9]* audit=(?:0|[1-9][0-9]*) auth_serial=(?:0|[1-9][0-9]*) auth=[1-9][0-9]* session=[1-9][0-9]* close_request=[1-9][0-9]* outcome={OUTCOME_RE} terminal_cap_sha256=[0-9a-f]{{64}} reply_digest=[0-9a-f]{{64}}"),"PER_AUTH"),
}

if set(WIRE_SPECS)!=(set(BASE_CONTROL_FORMS)|set(D_M1_FORMS)|set(D_M2_FORMS)):
    fail("closed control enum coverage")


class ClosedDispatcher:
    def __init__(self, side: str) -> None:
        self.side = side
        self.counts: dict[tuple[str,str],int] = {}
        self.reserved: set[tuple[str,str]] = set()

    @staticmethod
    def token(record: str) -> str:
        if not record or "\x00" in record or "\n" in record or not record.isascii():
            fail("record grammar")
        token = record.partition(" ")[0]
        return token

    @staticmethod
    def coordinate(cardinality: str, record: str) -> str:
        names={"PER_EPOCH":("epoch",),"PER_CHILD":("child",),"PER_OBJECT":("handle",),"PER_CREATOR":("child",),"PER_AUDIT":("audit_epoch",),"PER_AUDIT_REQUEST":("audit","serial"),"PER_FREEZE":("session","handle"),"PER_SIGNAL":("signo",),"PER_AUTH":("requester_child","session")}.get(cardinality)
        if cardinality=="ONCE": return "0"
        if names is None: fail("wire cardinality enum")
        values=[]
        for name in names:
            match=re.search(rf"(?:^| ){re.escape(name)}=([A-Za-z0-9_:]+)(?: |$)",record)
            if match is None: fail("wire coordinate")
            values.append(match.group(1))
        return ":".join(values)

    def inspect(self, direction: str, record: str) -> tuple[str,tuple[str,str]]:
        token = self.token(record)
        spec = WIRE_SPECS.get(token)
        if spec is None: fail("unknown control form")
        boundary=token in OLD_BOUNDARY_FORMS or token in ("GUARDIAN_READY_ACK","BOOTSTRAP_SEALED")
        if spec.direction != direction:
            if boundary: boundary_fail("WRONG_DIRECTION","boundary direction")
            fail("closed dispatcher")
        if spec.pattern.fullmatch(record) is None:
            if boundary: boundary_fail("MALFORMED","boundary grammar")
            fail("closed dispatcher")
        return token,(token,self.coordinate(spec.cardinality,record))

    def reserve_send(self, direction: str, record: str) -> tuple[str,tuple[str,str]]:
        token,coordinate=self.inspect(direction,record)
        if coordinate in self.reserved or coordinate in self.counts:
            if token in OLD_BOUNDARY_FORMS or token in ("GUARDIAN_READY_ACK","BOOTSTRAP_SEALED"): boundary_fail("DUPLICATE","duplicate boundary send")
            fail("duplicate control record")
        self.reserved.add(coordinate)
        return token,coordinate

    def commit_send(self, coordinate: tuple[str,str]) -> None:
        if coordinate not in self.reserved or coordinate in self.counts: fail("control reservation")
        self.counts[coordinate]=1

    def validate(self, direction: str, record: str, key: str = "0") -> str:
        token,coordinate=self.inspect(direction,record)
        if coordinate in self.reserved or coordinate in self.counts:
            if token in OLD_BOUNDARY_FORMS or token in ("GUARDIAN_READY_ACK","BOOTSTRAP_SEALED"): boundary_fail("DUPLICATE","duplicate boundary receive")
            fail("duplicate control record")
        self.counts[coordinate]=1
        return token


class FramedControl:
    def __init__(self, sock: socket.socket, side: str) -> None:
        if sock.family != socket.AF_UNIX or sock.type & socket.SOCK_SEQPACKET != socket.SOCK_SEQPACKET:
            fail("control socket type")
        self.sock = sock
        self.side = side
        self.dispatcher = ClosedDispatcher(side)
        self.first_failure=""; self.first_failure_record=b""; self.first_failure_sha256=""
        self.last_received_packet=b""; self.last_received_flags=0; self.last_received_ancillary_count=0; self.received_rights_violation=False; self.last_transport_errno=0; self.eof_observed=False
        self.last_send_packet=b""; self.last_send_count=-1; self.boundary_outbound: list[EndpointEnqueueReceipt]=[]

    def retain_failure(self, cause: str, material: bytes) -> None:
        if not self.first_failure:
            self.first_failure=cause; self.first_failure_record=bytes(material); self.first_failure_sha256=sha256(self.first_failure_record)

    def send(self, record: str, key: str = "0") -> EndpointEnqueueReceipt:
        direction = "P_TO_G" if self.side == "P" else "G_TO_P"
        try: token,coordinate=self.dispatcher.reserve_send(direction,record)
        except PossessionFailure: self.retain_failure("CONTROL_SEND_RECORD",record.encode("ascii",errors="backslashreplace")); raise
        payload = record.encode("ascii")
        if not payload or len(payload) > MAX_FRAME:
            self.retain_failure("CONTROL_SEND_RECORD",payload)
            fail("control frame size")
        packet = struct.pack(">I",len(payload))+payload
        self.last_send_packet=bytes(packet); self.last_send_count=-1; self.last_transport_errno=0
        try: count=self.sock.send(packet)
        except OSError as error: self.last_transport_errno=error.errno or 0; self.retain_failure("CONTROL_SEND",packet); raise
        self.last_send_count=count
        if count != len(packet): self.retain_failure("CONTROL_SEND",packet[:max(count,0)]); fail("control partial send")
        self.dispatcher.commit_send(coordinate)
        identity=os.fstat(self.sock.fileno())
        receipt=EndpointEnqueueReceipt(self.side,direction,token,bytes(packet),count,identity.st_dev,identity.st_ino)
        if token in ("LAUNCHER_REAPED","PRIVILEGE_DROP_RELEASE","GUARDIAN_READY","GUARDIAN_READY_ACK","BOOTSTRAP_SEALED"): self.boundary_outbound.append(receipt)
        return receipt

    def receive(self, key: str = "0") -> str:
        ancillary_space=socket.CMSG_SPACE(array.array("i",[0]*16).itemsize)
        self.last_received_packet=b""; self.last_received_flags=0; self.last_received_ancillary_count=0; self.last_transport_errno=0
        try: packet,ancillary,flags,_address = self.sock.recvmsg(MAX_FRAME+5,ancillary_space)
        except OSError as error: self.last_transport_errno=error.errno or 0; self.retain_failure("CONTROL_RECEIVE",b""); raise
        self.last_received_packet=bytes(packet); self.last_received_flags=flags; self.last_received_ancillary_count=len(ancillary)
        received_fds=received_rights(ancillary); self.received_rights_violation=self.received_rights_violation or bool(received_fds) or bool(flags&socket.MSG_CTRUNC)
        discard_rights(received_fds)
        if not packet:
            if ancillary or flags:
                self.retain_failure("CONTROL_RECEIVE",b"")
                fail("control packet")
            self.eof_observed=True; self.retain_failure("CONTROL_EOF",b""); fail("control EOF")
        if ancillary or flags & (socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(packet) < 5:
            self.retain_failure("CONTROL_RECEIVE",packet)
            fail("control packet")
        size = struct.unpack(">I",packet[:4])[0]; payload = packet[4:]
        if size == 0 or size > MAX_FRAME or len(payload) != size or b"\x00" in payload or b"\n" in payload or not payload.isascii():
            self.retain_failure("CONTROL_RECEIVE",packet)
            fail("control frame")
        record = payload.decode("ascii")
        direction = "G_TO_P" if self.side == "P" else "P_TO_G"
        try: self.dispatcher.validate(direction,record,key)
        except PossessionFailure: self.retain_failure("CONTROL_RECEIVE_RECORD",packet); raise
        return record

    def send_fd(self, record: str, fd: int) -> None:
        direction = "P_TO_G" if self.side == "P" else "G_TO_P"
        try: _token,coordinate=self.dispatcher.reserve_send(direction,record)
        except PossessionFailure: self.retain_failure("CONTROL_SEND_RECORD",record.encode("ascii",errors="backslashreplace")); raise
        payload = record.encode("ascii"); packet = struct.pack(">I",len(payload))+payload
        rights = array.array("i",[fd])
        try: count=self.sock.sendmsg((packet,),((socket.SOL_SOCKET,socket.SCM_RIGHTS,rights),))
        except OSError: self.retain_failure("CONTROL_SEND_FD",packet); raise
        if count != len(packet): self.retain_failure("CONTROL_SEND_FD",packet[:max(count,0)]); fail("rights partial send")
        self.dispatcher.commit_send(coordinate)

    def receive_fd(self, expected_record: str) -> int:
        space = socket.CMSG_SPACE(array.array("i",[0]).itemsize)
        try: packet,ancillary,flags,_address = self.sock.recvmsg(MAX_FRAME+5,space,socket.MSG_CMSG_CLOEXEC)
        except OSError: self.retain_failure("CONTROL_RECEIVE_FD",b""); raise
        values=received_rights(ancillary)
        if flags & (socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(packet) < 5 or len(ancillary) != 1:
            discard_rights(values)
            self.retain_failure("CONTROL_RECEIVE_FD",packet)
            fail("rights packet")
        level,kind,data = ancillary[0]
        if (level,kind) != (socket.SOL_SOCKET,socket.SCM_RIGHTS) or len(data)!=array.array("i").itemsize:
            discard_rights(values)
            self.retain_failure("CONTROL_RECEIVE_FD",packet)
            fail("rights cmsg")
        if len(values) != 1:
            discard_rights(values)
            self.retain_failure("CONTROL_RECEIVE_FD",packet)
            fail("rights cardinality")
        size = struct.unpack(">I",packet[:4])[0]; payload = packet[4:]
        if size==0 or size>MAX_FRAME or size!=len(payload) or b"\x00" in payload or b"\n" in payload or not payload.isascii() or payload.decode("ascii")!=expected_record:
            discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); fail("rights record")
        direction = "P_TO_G" if self.side == "G" else "G_TO_P"
        try: self.dispatcher.validate(direction,expected_record)
        except PossessionFailure: discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); raise
        if fcntl.fcntl(values[0],fcntl.F_GETFD)!=FD_CLOEXEC:
            discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); fail("rights CLOEXEC")
        return values[0]

    def receive_fd_matching(self, expected_pattern: re.Pattern[str]) -> tuple[str,int]:
        space=socket.CMSG_SPACE(array.array("i",[0]).itemsize)
        packet,ancillary,flags,_address=self.sock.recvmsg(MAX_FRAME+5,space,socket.MSG_CMSG_CLOEXEC); values=received_rights(ancillary)
        if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(packet)<5 or len(ancillary)!=1 or len(values)!=1:
            discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); fail("rights packet")
        level,kind,data=ancillary[0]
        if (level,kind)!=(socket.SOL_SOCKET,socket.SCM_RIGHTS) or len(data)!=array.array("i").itemsize:
            discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); fail("rights cmsg")
        size=struct.unpack(">I",packet[:4])[0]; payload=packet[4:]
        if size==0 or size>MAX_FRAME or size!=len(payload) or b"\x00" in payload or b"\n" in payload or not payload.isascii():
            discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); fail("rights record")
        record=payload.decode("ascii")
        if expected_pattern.fullmatch(record) is None:
            discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); fail("rights record")
        direction="P_TO_G" if self.side=="G" else "G_TO_P"
        try: self.dispatcher.validate(direction,record)
        except PossessionFailure: discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); raise
        if fcntl.fcntl(values[0],fcntl.F_GETFD)!=FD_CLOEXEC:
            discard_rights(values); self.retain_failure("CONTROL_RECEIVE_FD",packet); fail("rights CLOEXEC")
        return record,values[0]


def fd_is_open(fd: int) -> bool:
    try:
        fcntl.fcntl(fd,fcntl.F_GETFD)
        return True
    except OSError as error:
        if error.errno == errno.EBADF:
            return False
        raise


def immediate_ebadf(fd: int) -> None:
    try:
        fcntl.fcntl(fd,fcntl.F_GETFD)
    except OSError as error:
        if error.errno == errno.EBADF:
            return
    fail("missing EBADF")


def close_proved(fd: int) -> None:
    os.close(fd)
    immediate_ebadf(fd)


def close_except(allowed: frozenset[int]) -> None:
    proc_fd = os.open("/proc/self/fd",OPEN_DIR)
    try:
        names = os.listdir(proc_fd)
    finally:
        close_proved(proc_fd)
    values = []
    for name in names:
        if re.fullmatch(r"0|[1-9][0-9]*",name) is None:
            fail("fd grammar")
        fd = int(name)
        if fd not in allowed:
            values.append(fd)
    for fd in sorted(values,reverse=True):
        if fd_is_open(fd): close_proved(fd)


def duplicate_to(source: int, target: int) -> None:
    if source == target:
        flags = fcntl.fcntl(target,fcntl.F_GETFD)
        fcntl.fcntl(target,fcntl.F_SETFD,flags|FD_CLOEXEC)
    else:
        os.dup2(source,target,inheritable=False)


def install_fd_map(mappings: Mapping[int,int]) -> None:
    """Install a complete descriptor map from high-numbered CLOEXEC staging.

    Staging every distinct source before the first target move makes the
    operation independent of target order: a low target can never destroy a
    source still needed by a later move.
    """
    targets=tuple(mappings); sources=tuple(mappings.values())
    if len(targets)!=len(set(targets)) or any(target<0 or source<0 for target,source in mappings.items()): fail("FD map grammar")
    staged: dict[int,int]={}; receipts: dict[int,tuple[int,int,int,int]]={}
    try:
        lower=max((64,*(target+1 for target in targets)))
        for source in sorted(set(mappings.values())):
            os.fstat(source)
            staged[source]=fcntl.fcntl(source,fcntl.F_DUPFD_CLOEXEC,lower)
            if staged[source] in targets: fail("staging target collision")
            observed=os.fstat(staged[source])
            receipts[source]=(stat.S_IFMT(observed.st_mode),observed.st_dev,observed.st_ino,fcntl.fcntl(staged[source],fcntl.F_GETFL))
            if fcntl.fcntl(staged[source],fcntl.F_GETFD)!=FD_CLOEXEC: fail("staging CLOEXEC")
        for target,source in sorted(mappings.items()): duplicate_to(staged[source],target)
        for target,source in mappings.items():
            observed=os.fstat(target)
            receipt=(stat.S_IFMT(observed.st_mode),observed.st_dev,observed.st_ino,fcntl.fcntl(target,fcntl.F_GETFL))
            if receipt!=receipts[source] or fcntl.fcntl(target,fcntl.F_GETFD)!=FD_CLOEXEC: fail("installed FD receipt")
    finally:
        for staged_fd in sorted(staged.values(),reverse=True):
            if fd_is_open(staged_fd): close_proved(staged_fd)


def clone3(child: Callable[[],int], *, cgroup_fd: int) -> tuple[int,int]:
    pidfd_value = ctypes.c_int(-1)
    flags = CLONE_PIDFD | CLONE_INTO_CGROUP
    args = CloneArgs(flags,ctypes.addressof(pidfd_value),0,0,signal.SIGCHLD,0,0,0,0,0,cgroup_fd)
    if ctypes.sizeof(args) != 88 or CloneArgs.cgroup.offset != 80:
        fail("clone_args layout")
    pid = syscall(SYS_CLONE3,ctypes.byref(args),ctypes.c_size_t(88))
    if pid == 0:
        status = 125
        try: status = int(child())
        except BaseException: status = 125
        os._exit(status & 0xff)
    if pid <= 0 or pidfd_value.value < 0 or fcntl.fcntl(pidfd_value.value,fcntl.F_GETFD)!=FD_CLOEXEC:
        fail("clone3 result")
    return pid,pidfd_value.value


def clone3_pidfd_only(child: Callable[[],int]) -> tuple[int,int]:
    pidfd_value=ctypes.c_int(-1)
    args=CloneArgs(CLONE_PIDFD,ctypes.addressof(pidfd_value),0,0,signal.SIGCHLD,0,0,0,0,0,0)
    if ctypes.sizeof(args)!=88 or any(bytes(args)[offset:offset+8]!=b"\x00"*8 for offset in (16,24,40,48,56,64,72,80)):
        fail("pidfd probe clone_args")
    pid=syscall(SYS_CLONE3,ctypes.byref(args),ctypes.c_size_t(88))
    if pid==0:
        status=125
        try: status=int(child())
        except BaseException: status=125
        os._exit(status&0xff)
    if pid<=0 or pidfd_value.value<0 or fcntl.fcntl(pidfd_value.value,fcntl.F_GETFD)!=FD_CLOEXEC: fail("pidfd probe clone3 result")
    return pid,pidfd_value.value


def install_worker_security() -> None:
    self_fd=os.open("/proc/self",OPEN_PATH_DIR)
    try: status=parse_proc_status(read_regular_at(self_fd,"status",1024*1024))
    finally: os.close(self_fd)
    if os.getgroups() or any(status.get(name)!="0000000000000000" for name in ("CapInh","CapPrm","CapEff","CapBnd","CapAmb")) or status.get("NoNewPrivs")!="1" or LIBC.prctl(3,0,0,0,0)!=0:
        fail("inherited worker security")
    denied=(56,57,58,59,206,207,208,209,210,272,307,308,322,333,425,426,427,435,46)
    filters=[SockFilter(0x20,0,0,4),SockFilter(0x15,1,0,AUDIT_ARCH_X86_64),SockFilter(0x06,0,0,0x80000000),SockFilter(0x20,0,0,0),SockFilter(0x45,0,1,X32_SYSCALL_BIT),SockFilter(0x06,0,0,0x80000000)]
    for number in denied:
        filters.extend((SockFilter(0x15,0,1,number),SockFilter(0x06,0,0,0x00050000|errno.EPERM)))
    filters.append(SockFilter(0x06,0,0,0x7fff0000))
    storage=(SockFilter*len(filters))(*filters); program=SockFprog(len(filters),storage)
    syscall(SYS_SECCOMP,ctypes.c_uint(1),ctypes.c_uint(0),ctypes.byref(program))


def native_scalar_preflight() -> None:
    if sys.platform != "linux" or os.uname().machine != "x86_64" or struct.calcsize("P") != 8 or struct.calcsize("l") != 8 or sys.byteorder != "little":
        fail("architecture")
    if (SYS_GETRANDOM,SYS_PIDFD_SEND_SIGNAL,SYS_PIDFD_OPEN,SYS_CLONE3,SYS_CLOSE_RANGE,SYS_OPENAT2,SYS_PIDFD_GETFD) != (318,424,434,435,436,437,438):
        fail("syscalls")
    expected_offsets=(0,8,16,24,32,40,48,56,64,72,80)
    actual=tuple(getattr(CloneArgs,name).offset for name,_ctype in CloneArgs._fields_)
    if ctypes.sizeof(CloneArgs) != 88 or actual != expected_offsets:
        fail("clone layout")
    if len(FD5_FORMS)!=12 or len(set(FD5_FORMS))!=12 or len(D_M1_FORMS)!=12 or len(set(D_M1_FORMS))!=12 or len(D_M2_FORMS)!=4 or len(set(D_M2_FORMS))!=4:
        fail("closed enums")


def seqpacket_probe() -> None:
    left,right=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
    try:
        right.setsockopt(socket.SOL_SOCKET,socket.SO_PASSCRED,1)
        payload=b"P15R-PREFLIGHT-SEQPACKET"
        if left.send(payload)!=len(payload): fail("seq send")
        data,ancillary,flags,_address=right.recvmsg(MAX_FRAME,socket.CMSG_SPACE(struct.calcsize("3i")))
        credentials=[item for item in ancillary if item[0]==socket.SOL_SOCKET and item[1]==socket.SCM_CREDENTIALS]
        if data!=payload or flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(credentials)!=1 or len(ancillary)!=1:
            fail("seq credentials")
        left.close()
        if right.recv(1)!=b"": fail("seq EOF")
    finally:
        try:left.close()
        except OSError:pass
        right.close()


def unix_diag_request(inode: int, sequence: int, portid: int) -> bytes:
    if not (0<inode<=0xffffffff and 0<sequence<=0xffffffff and 0<portid<=0xffffffff): fail("diag request identity")
    request=struct.pack("<IHHIIBBBBIII2I",40,SOCK_DIAG_BY_FAMILY,1,sequence,portid,socket.AF_UNIX,0,0,0,0xffffffff,inode,4,0xffffffff,0xffffffff)
    if len(request)!=40: fail("diag request ABI")
    return request


@dataclass(frozen=True)
class UnixDiagReceipt:
    queried_inode: int
    peer_inode: int
    sequence: int
    portid: int
    cookie0: int
    cookie1: int
    raw48: bytes


class UnixDiagOracle:
    """P-owned single-outstanding SOCK_DIAG oracle with monotone sequences."""
    def __init__(self) -> None:
        self.sock=socket.socket(socket.AF_NETLINK,socket.SOCK_RAW|socket.SOCK_CLOEXEC,NETLINK_SOCK_DIAG)
        self.sock.bind((0,0)); self.portid,self.groups=self.sock.getsockname(); self.next_sequence=1; self.outstanding=False; self.closed=False
        if self.portid<=0 or self.groups!=0 or fcntl.fcntl(self.sock,fcntl.F_GETFD)!=FD_CLOEXEC: fail("diag bind portid")

    def query(self, inode: int) -> UnixDiagReceipt:
        if self.closed or self.outstanding or self.next_sequence>0xffffffff: fail("diag query state")
        sequence=self.next_sequence; self.next_sequence+=1; request=unix_diag_request(inode,sequence,self.portid)
        deadline=time.monotonic_ns()+P15R_UNIX_DIAG_QUERY_TIMEOUT_NS; self.outstanding=True
        try:
            while True:
                try: sent=self.sock.sendto(request,(0,0))
                except InterruptedError:
                    if time.monotonic_ns()>=deadline: fail("diag send timeout")
                    continue
                break
            if sent!=40: fail("diag send")
            poller=select.poll(); identity=self.sock.fileno(); poller.register(self.sock,select.POLLIN|select.POLLERR|select.POLLHUP)
            while True:
                remaining=deadline-time.monotonic_ns()
                if remaining<=0: fail("diag timeout")
                try: events=poller.poll(max(1,(remaining+999999)//1000000))
                except InterruptedError: continue
                if not events: continue
                if events!=[(identity,select.POLLIN)]: fail("diag poll")
                break
            data,ancillary,flags,address=self.sock.recvmsg(256)
            if ancillary or flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or address!=(0,0) or len(data)!=48: fail("diag response")
            length,kind,nflags,seq,pid=struct.unpack_from("<IHHII",data,0)
            family,sock_type,state,_pad,response_inode,cookie0,cookie1=struct.unpack_from("<BBBBIII",data,16)
            nla1_len,nla1_type,peer=struct.unpack_from("<HHI",data,32); nla2_len,nla2_type,shutdown=struct.unpack_from("<HHB",data,40)
            if kind in (2,3,4) or nflags&2: fail("diag error/multipart")
            if (length,kind,nflags,seq,pid,family,sock_type,state,_pad,response_inode)!=(48,20,0,sequence,self.portid,socket.AF_UNIX,socket.SOCK_SEQPACKET,1,0,inode): fail("diag header")
            if (nla1_len,nla1_type,nla2_len,nla2_type,shutdown)!=(8,UNIX_DIAG_PEER,5,UNIX_DIAG_SHUTDOWN,0) or not (0<peer<=0xffffffff) or (cookie0,cookie1)==(0xffffffff,0xffffffff): fail("diag NLA")
            try: self.sock.recvmsg(256,0,socket.MSG_DONTWAIT)
            except BlockingIOError: pass
            else: fail("diag cardinality")
            return UnixDiagReceipt(inode,peer,sequence,self.portid,cookie0,cookie1,bytes(data))
        finally: self.outstanding=False

    def close(self) -> None:
        if self.closed or self.outstanding: fail("diag close state")
        descriptor=self.sock.fileno(); self.sock.close(); immediate_ebadf(descriptor); self.closed=True


def unix_diag_preflight() -> UnixDiagOracle:
    diag=UnixDiagOracle()
    a0,a1=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
    b0,b1=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
    try:
        identities=[]
        reciprocal=[]
        for left,right,seq in ((a0,a1,1),(b0,b1,3)):
            left_inode=os.fstat(left.fileno()).st_ino; right_inode=os.fstat(right.fileno()).st_ino
            observed=(diag.query(left_inode).peer_inode,diag.query(right_inode).peer_inode)
            if observed!=(right_inode,left_inode): fail("diag reciprocal")
            identities.append((left_inode,right_inode))
            reciprocal.append(observed)
        flat=identities[0]+identities[1]
        if len(set(flat))!=4 or any(not (0<inode<=0xffffffff) for inode in flat): fail("diag crossed")
        a0_inode,a1_inode=identities[0]; b0_inode,b1_inode=identities[1]
        peer_by_inode={a0_inode:reciprocal[0][0],a1_inode:reciprocal[0][1],b0_inode:reciprocal[1][0],b1_inode:reciprocal[1][1]}
        if not (peer_by_inode[a0_inode]!=b1_inode and peer_by_inode[b1_inode]!=a0_inode and peer_by_inode[b0_inode]!=a1_inode and peer_by_inode[a1_inode]!=b0_inode): fail("diag crossed acceptance")
        a0.close(); a1.close()
        if (diag.query(identities[1][0]).peer_inode,diag.query(identities[1][1]).peer_inode)!=(identities[1][1],identities[1][0]): fail("diag post close")
        return diag
    except BaseException:
        diag.close(); raise
    finally:
        for endpoint in (a0,a1,b0,b1):
            try:endpoint.close()
            except OSError:pass
def openat2(directory_fd: int, relative: str, flags: int, mode: int = 0) -> int:
    if not relative or relative.startswith("/") or any(part in ("",".","..") for part in relative.split("/")) or "\x00" in relative:
        fail("openat2 relative")
    how=OpenHow(flags,mode,RESOLVE_BENEATH|RESOLVE_NO_SYMLINKS|RESOLVE_NO_MAGICLINKS)
    return syscall(SYS_OPENAT2,ctypes.c_int(directory_fd),ctypes.c_char_p(os.fsencode(relative)),ctypes.byref(how),ctypes.c_size_t(ctypes.sizeof(how)))


def renameat2(old_fd: int, old_name: str, new_fd: int, new_name: str, flags: int) -> None:
    for name in (old_name,new_name):
        if not name or "/" in name or name in (".","..") or "\x00" in name:
            fail("rename basename")
    syscall(SYS_RENAMEAT2,ctypes.c_int(old_fd),ctypes.c_char_p(os.fsencode(old_name)),ctypes.c_int(new_fd),ctypes.c_char_p(os.fsencode(new_name)),ctypes.c_uint(flags))


def mount(source: str|None, target: str, kind: str|None, flags: int, data: str|None = None) -> None:
    source_value=None if source is None else ctypes.c_char_p(os.fsencode(source))
    kind_value=None if kind is None else ctypes.c_char_p(os.fsencode(kind))
    data_value=None if data is None else ctypes.c_char_p(os.fsencode(data))
    syscall(SYS_MOUNT,source_value,ctypes.c_char_p(os.fsencode(target)),kind_value,ctypes.c_ulong(flags),data_value)


def umount(target: str) -> None:
    syscall(SYS_UMOUNT2,ctypes.c_char_p(os.fsencode(target)),ctypes.c_int(MNT_DETACH))


def read_regular_at(directory_fd: int, relative: str, ceiling: int = 16*1024*1024) -> bytes:
    fd=openat2(directory_fd,relative,OPEN_REGULAR)
    try:
        st=os.fstat(fd)
        if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1 or st.st_size > ceiling:
            fail("source regular")
        data=read_all(fd)
        if st.st_size and len(data)!=st.st_size:
            fail("source changed")
        if len(data)>ceiling:
            fail("source ceiling")
        return data
    finally:
        os.close(fd)


def write_control_at(directory_fd: int, name: str, payload: bytes) -> None:
    fd=os.open(name,os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=directory_fd)
    try: complete_write(fd,payload)
    finally: os.close(fd)


def read_control_at(directory_fd: int, name: str) -> bytes:
    fd=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=directory_fd)
    try: return read_all(fd)
    finally: os.close(fd)


def read_retained_control(fd: int, ceiling: int = 1024*1024) -> bytes:
    if fd<0: fail("retained control tombstone")
    os.lseek(fd,0,os.SEEK_SET)
    data=read_all(fd)
    if len(data)>ceiling: fail("retained control ceiling")
    return data


def write_retained_control(fd: int, payload: bytes) -> None:
    if fd<0 or not payload: fail("retained control write")
    os.lseek(fd,0,os.SEEK_SET)
    complete_write(fd,payload)


def fd_statfs_type(fd: int) -> int:
    result=StatFs()
    ctypes.set_errno(0)
    if LIBC.fstatfs(ctypes.c_int(fd),ctypes.byref(result))!=0:
        error=ctypes.get_errno(); raise OSError(error,os.strerror(error))
    return int(result.f_type)&0xffffffffffffffff


def faccessat2(directory_fd: int, relative: str, mode: int) -> bool:
    if not relative or relative.startswith("/") or any(piece in ("",".","..") for piece in relative.split("/")):
        fail("faccess relative path")
    try:
        syscall(SYS_FACCESSAT2,ctypes.c_int(directory_fd),ctypes.c_char_p(os.fsencode(relative)),ctypes.c_int(mode),ctypes.c_int(AT_EACCESS|AT_SYMLINK_NOFOLLOW))
    except OSError as error:
        if error.errno in (errno.EACCES,errno.EPERM,errno.EROFS): return False
        raise
    return True


def faccess_fd(fd: int, mode: int) -> bool:
    try:
        syscall(SYS_FACCESSAT2,ctypes.c_int(fd),ctypes.c_char_p(b""),ctypes.c_int(mode),ctypes.c_int(AT_EMPTY_PATH|AT_EACCESS))
    except OSError as error:
        if error.errno in (errno.EACCES,errno.EPERM,errno.EROFS): return False
        raise
    return True


def exact_wait_pidfd(pidfd: int, pid: int) -> int:
    information=os.waitid(os.P_PIDFD,pidfd,os.WEXITED)
    if information is None or information.si_pid != pid or information.si_code not in (os.CLD_EXITED,os.CLD_KILLED,os.CLD_DUMPED):
        fail("waitid identity")
    if information.si_code == os.CLD_EXITED:
        return int(information.si_status)
    return 128+int(information.si_status)


def parse_proc_status(data: bytes) -> dict[str,str]:
    if b"\x00" in data or not data.endswith(b"\n"):
        fail("proc status bytes")
    result: dict[str,str]={}
    for raw in data.splitlines():
        if b":" not in raw: continue
        key,value=raw.split(b":",1)
        try: result[key.decode("ascii")]=value.decode("ascii").strip()
        except UnicodeDecodeError: fail("proc status ASCII")
    return result


def proc_start_time(process_fd: int, pid: int) -> int:
    data=read_regular_at(process_fd,"stat",1024*1024)
    if not data.endswith(b"\n") or b"\x00" in data: fail("proc stat bytes")
    close=data.rfind(b") ")
    if close<0 or data[:data.find(b" ")]!=str(pid).encode("ascii"): fail("proc stat identity")
    fields=data[close+2:].strip().split()
    if len(fields)<20 or re.fullmatch(rb"[1-9][0-9]*",fields[19]) is None: fail("proc starttime grammar")
    return int(fields[19])


def worker_proc_identity(process_fd: int, pid: int, expected_ppid: int, expected_inner_pid: int, expected_uid: int, expected_gid: int) -> tuple[int,tuple[int,...],str,int,int]:
    status=parse_proc_status(read_regular_at(process_fd,"status",1024*1024))
    nspid=tuple(int(value) for value in status.get("NSpid","").split())
    uid=tuple(int(value) for value in status.get("Uid","").split()); gid=tuple(int(value) for value in status.get("Gid","").split())
    cgroup=read_regular_at(process_fd,"cgroup",1024*1024).decode("ascii")
    if status.get("PPid")!=str(expected_ppid) or not nspid or nspid[-1]!=expected_inner_pid or uid!=(expected_uid,)*4 or gid!=(expected_gid,)*4 or status.get("Threads")!="1" or re.fullmatch(r"0::/[^\n]*\n",cgroup) is None: fail("worker proc identity")
    return proc_start_time(process_fd,pid),nspid,cgroup,uid[0],gid[0]


def current_cgroup_relative() -> str:
    self_fd=os.open("/proc/self",OPEN_PATH_DIR)
    try: data=read_regular_at(self_fd,"cgroup",1024*1024)
    finally: os.close(self_fd)
    rows=data.decode("ascii").splitlines()
    matches=[row[3:] for row in rows if row.startswith("0::/") or row=="0::/"]
    if len(matches)!=1 or not matches[0].startswith("/") or ".." in matches[0].split("/"):
        fail("cgroup membership")
    return matches[0].lstrip("/")


def cgroup2_mount() -> str:
    root=os.open("/proc/self",OPEN_PATH_DIR)
    try: data=read_regular_at(root,"mountinfo",4*1024*1024)
    finally: os.close(root)
    matches=[]
    for line in data.decode("utf-8").splitlines():
        pieces=line.split(" ")
        if "-" not in pieces: fail("mountinfo")
        separator=pieces.index("-")
        if separator+2<len(pieces) and pieces[separator+1]=="cgroup2": matches.append(pieces[4].replace("\\040"," "))
    if len(matches)!=1 or not matches[0].startswith("/"):
        fail("cgroup2 mount")
    return matches[0]


@dataclass
class CgroupTree:
    mount_path: str
    parent_fd: int
    session_fd: int
    guardian_fd: int
    workers_fd: int
    parent_identity: tuple[int,int]
    session_identity: tuple[int,int]
    guardian_identity: tuple[int,int]
    workers_identity: tuple[int,int]
    workers_freeze_fd: int
    workers_events_fd: int
    workers_kill_fd: int
    session_events_fd: int
    session_kill_fd: int
    session_procs_fd: int
    guardian_procs_fd: int
    workers_procs_fd: int
    names: tuple[str,str,str]
    probe_used: bool=False
    disposed: bool=False

    @classmethod
    def create(cls, pid_dec: int) -> "CgroupTree":
        if pid_dec!=os.getpid() or pid_dec<=0: fail("cgroup PID_DEC")
        mount_path=cgroup2_mount(); mount_fd=parent_fd=session_fd=guardian_fd=workers_fd=-1
        controls: dict[str,int]={}; created: list[tuple[int,str,int,tuple[int,int]]]=[]
        session=f"p15r-possession-v2-{pid_dec}"; guardian="guardian"; workers="workers"
        try:
            mount_fd=os.open(mount_path,OPEN_DIR)
            if fd_statfs_type(mount_fd)!=CGROUP2_SUPER_MAGIC: fail("cgroup2 statfs")
            relative=current_cgroup_relative()
            parent_fd=os.dup(mount_fd) if not relative else openat2(mount_fd,relative,OPEN_DIR)
            parent_st=os.fstat(parent_fd); parent_identity=(parent_st.st_dev,parent_st.st_ino)
            if not stat.S_ISDIR(parent_st.st_mode) or (parent_st.st_uid,parent_st.st_gid)!=(0,0) or stat.S_IMODE(parent_st.st_mode)&0o022:
                fail("cgroup parent authority")
            os.mkdir(session,0o700,dir_fd=parent_fd)
            session_fd=os.open(session,OPEN_PATH_DIR,dir_fd=parent_fd); session_st=os.fstat(session_fd); session_identity=(session_st.st_dev,session_st.st_ino)
            created.append((parent_fd,session,session_fd,session_identity))
            os.mkdir(guardian,0o700,dir_fd=session_fd)
            guardian_fd=os.open(guardian,OPEN_PATH_DIR,dir_fd=session_fd); guardian_st=os.fstat(guardian_fd); guardian_identity=(guardian_st.st_dev,guardian_st.st_ino)
            created.append((session_fd,guardian,guardian_fd,guardian_identity))
            os.mkdir(workers,0o700,dir_fd=session_fd)
            workers_fd=os.open(workers,OPEN_PATH_DIR,dir_fd=session_fd); workers_st=os.fstat(workers_fd); workers_identity=(workers_st.st_dev,workers_st.st_ino)
            created.append((session_fd,workers,workers_fd,workers_identity))
            for name,st in ((session,session_st),(guardian,guardian_st),(workers,workers_st)):
                if not stat.S_ISDIR(st.st_mode) or stat.S_IMODE(st.st_mode)!=0o700 or (st.st_uid,st.st_gid)!=(0,0): fail("cgroup directory "+name)
            for directory_fd in (session_fd,guardian_fd,workers_fd):
                if read_control_at(directory_fd,"cgroup.type")!=b"domain\n": fail("cgroup type")
                if read_control_at(directory_fd,"cgroup.subtree_control").strip()!=b"": fail("cgroup controller enabled")
            for directory_fd in (session_fd,workers_fd):
                os.chown("cgroup.procs",65534,65534,dir_fd=directory_fd,follow_symlinks=False)
                os.chmod("cgroup.procs",0o600,dir_fd=directory_fd,follow_symlinks=False)
            for directory_fd,name in ((session_fd,"session"),(workers_fd,"workers")):
                observed=os.stat("cgroup.procs",dir_fd=directory_fd,follow_symlinks=False)
                if (observed.st_uid,observed.st_gid,stat.S_IMODE(observed.st_mode))!=(65534,65534,0o600): fail("delegated cgroup.procs "+name)
            for directory_fd,name in ((guardian_fd,"cgroup.procs"),(workers_fd,"cgroup.freeze"),(workers_fd,"cgroup.kill"),(workers_fd,"cgroup.events"),(session_fd,"cgroup.events"),(session_fd,"cgroup.kill")):
                observed=os.stat(name,dir_fd=directory_fd,follow_symlinks=False)
                if (observed.st_uid,observed.st_gid)!=(0,0) or stat.S_IMODE(observed.st_mode)&0o022: fail("root-only cgroup control "+name)
            controls["workers_freeze"]=os.open("cgroup.freeze",os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=workers_fd)
            controls["workers_events"]=os.open("cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=workers_fd)
            controls["workers_kill"]=os.open("cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=workers_fd)
            controls["session_events"]=os.open("cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=session_fd)
            controls["session_kill"]=os.open("cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=session_fd)
            controls["session_procs"]=os.open("cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=session_fd)
            controls["guardian_procs"]=os.open("cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=guardian_fd)
            controls["workers_procs"]=os.open("cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=workers_fd)
            return cls(mount_path,parent_fd,session_fd,guardian_fd,workers_fd,parent_identity,session_identity,guardian_identity,workers_identity,
                       controls["workers_freeze"],controls["workers_events"],controls["workers_kill"],controls["session_events"],controls["session_kill"],
                       controls["session_procs"],controls["guardian_procs"],controls["workers_procs"],(session,guardian,workers))
        except BaseException:
            for fd in reversed(tuple(controls.values())):
                if fd>=0 and fd_is_open(fd): close_proved(fd)
            for parent,name,directory_fd,identity in reversed(created):
                if directory_fd>=0 and fd_is_open(directory_fd):
                    observed=os.fstat(directory_fd)
                    if (observed.st_dev,observed.st_ino)!=identity: fail("partial cgroup identity")
                    close_proved(directory_fd)
                try:
                    named=os.stat(name,dir_fd=parent,follow_symlinks=False)
                    if (named.st_dev,named.st_ino)!=identity: fail("partial cgroup name drift")
                    os.rmdir(name,dir_fd=parent)
                except FileNotFoundError: fail("partial cgroup missing")
            if parent_fd>=0 and fd_is_open(parent_fd): close_proved(parent_fd)
            raise
        finally:
            if mount_fd>=0 and fd_is_open(mount_fd): close_proved(mount_fd)

    @staticmethod
    def _named_identity(parent_fd: int, name: str, expected: tuple[int,int]) -> None:
        observed=os.stat(name,dir_fd=parent_fd,follow_symlinks=False)
        if (observed.st_dev,observed.st_ino)!=expected: fail("cgroup identity drift")

    def relative(self, leaf: str) -> str:
        if leaf not in ("guardian","workers"): fail("cgroup relative leaf")
        return "/"+"/".join(piece for piece in (current_cgroup_relative(),self.names[0],leaf) if piece)

    @staticmethod
    def parse_events(data: bytes) -> dict[str,int]:
        result={}
        for line in data.decode("ascii").splitlines():
            key,value=line.split(" ",1); result[key]=int(value)
        if set(result)!={"populated","frozen"}: fail("cgroup events")
        return result

    def events(self, fd: int) -> dict[str,int]:
        if fd==self.workers_fd: return self.parse_events(read_retained_control(self.workers_events_fd))
        if fd==self.session_fd: return self.parse_events(read_retained_control(self.session_events_fd))
        return self.parse_events(read_control_at(fd,"cgroup.events"))

    def freeze(self, fd: int) -> None:
        if fd!=self.workers_fd: fail("freeze authority")
        populated=self.events(fd)["populated"]
        write_retained_control(self.workers_freeze_fd,b"1\n")
        if self.events(fd)!={"populated":populated,"frozen":1}: fail("freeze evidence")

    def thaw(self, fd: int) -> None:
        if fd!=self.workers_fd: fail("thaw authority")
        write_retained_control(self.workers_freeze_fd,b"0\n")
        if self.events(fd).get("frozen")!=0: fail("thaw evidence")

    def kill(self, fd: int) -> None:
        if fd==self.workers_fd: write_retained_control(self.workers_kill_fd,b"1\n")
        elif fd==self.session_fd: write_retained_control(self.session_kill_fd,b"1\n")
        else: fail("kill authority")

    def members(self, fd: int) -> list[int]:
        if fd==self.session_fd: data=read_retained_control(self.session_procs_fd)
        elif fd==self.guardian_fd: data=read_retained_control(self.guardian_procs_fd)
        elif fd==self.workers_fd: data=read_retained_control(self.workers_procs_fd)
        else: data=read_control_at(fd,"cgroup.procs")
        values=data.decode("ascii").split()
        if any(re.fullmatch(r"[1-9][0-9]*",value) is None for value in values): fail("cgroup.procs grammar")
        result=[int(value) for value in values]
        if len(result)!=len(set(result)): fail("cgroup.procs duplicate")
        return result

    def require_member(self, fd: int, pid: int) -> None:
        if self.members(fd)!=[pid]: fail("atomic cgroup membership")

    def require_members(self, fd: int, members: Sequence[int]) -> None:
        if sorted(self.members(fd))!=sorted(members): fail("cgroup membership set")

    def require_empty(self, fd: int) -> None:
        if self.members(fd) or self.events(fd).get("populated")!=0:
            fail("cgroup not empty")

    def dispose(self) -> None:
        if self.disposed: fail("duplicate cgroup dispose")
        self.require_empty(self.workers_fd); self.require_empty(self.guardian_fd); self.require_empty(self.session_fd)
        for field_name in ("workers_freeze_fd","workers_events_fd","workers_kill_fd","session_events_fd","session_kill_fd","session_procs_fd","guardian_procs_fd","workers_procs_fd"):
            value=getattr(self,field_name)
            if value<0 or not fd_is_open(value): fail("cgroup control ownership")
            close_proved(value); setattr(self,field_name,-1)
        self._named_identity(self.session_fd,self.names[2],self.workers_identity); close_proved(self.workers_fd); self.workers_fd=-1; os.rmdir(self.names[2],dir_fd=self.session_fd)
        self._named_identity(self.session_fd,self.names[1],self.guardian_identity); close_proved(self.guardian_fd); self.guardian_fd=-1; os.rmdir(self.names[1],dir_fd=self.session_fd)
        self._named_identity(self.parent_fd,self.names[0],self.session_identity); close_proved(self.session_fd); self.session_fd=-1
        os.rmdir(self.names[0],dir_fd=self.parent_fd)
        observed=os.fstat(self.parent_fd)
        if (observed.st_dev,observed.st_ino)!=self.parent_identity: fail("cgroup parent drift")
        close_proved(self.parent_fd); self.parent_fd=-1
        self.disposed=True


def cgroup_atomic_probe(tree: CgroupTree) -> None:
    if tree.probe_used: fail("cgroup probe reuse")
    name="probe"; probe_fd=freeze_fd=events_fd=kill_fd=procs_fd=read_end=write_end=pidfd=-1; pid=0; created=False; reaped=False; identity=(0,0)
    os.mkdir(name,0o700,dir_fd=tree.session_fd); created=True
    def child() -> int:
        if read_end>=0: os.close(read_end)
        duplicate_to(write_end,3)
        syscall(SYS_CLOSE_RANGE,ctypes.c_uint(0),ctypes.c_uint(2),ctypes.c_uint(0))
        syscall(SYS_CLOSE_RANGE,ctypes.c_uint(4),ctypes.c_uint(0xffffffff),ctypes.c_uint(0))
        complete_write(3,b"F"); close_proved(3)
        signal.pause(); return 99
    try:
        probe_fd=os.open(name,OPEN_PATH_DIR,dir_fd=tree.session_fd); identity_st=os.fstat(probe_fd); identity=(identity_st.st_dev,identity_st.st_ino)
        if not stat.S_ISDIR(identity_st.st_mode) or stat.S_IMODE(identity_st.st_mode)!=0o700 or (identity_st.st_uid,identity_st.st_gid)!=(0,0): fail("probe cgroup identity")
        if read_control_at(probe_fd,"cgroup.type")!=b"domain\n" or read_control_at(probe_fd,"cgroup.subtree_control").strip(): fail("probe cgroup controls")
        freeze_fd=os.open("cgroup.freeze",os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=probe_fd)
        events_fd=os.open("cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=probe_fd)
        kill_fd=os.open("cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=probe_fd)
        procs_fd=os.open("cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=probe_fd)
        read_end,write_end=os.pipe2(os.O_CLOEXEC)
        pid,pidfd=clone3(child,cgroup_fd=probe_fd)
        close_proved(write_end); write_end=-1
        if read_all(read_end)!=b"F": fail("probe first instruction")
        close_proved(read_end); read_end=-1
        if read_retained_control(procs_fd).strip()!=str(pid).encode("ascii"): fail("probe atomic placement")
        before=tree.parse_events(read_retained_control(events_fd))
        if before!={"populated":1,"frozen":0}: fail("probe initial events")
        write_retained_control(freeze_fd,b"1\n")
        if tree.parse_events(read_retained_control(events_fd))!={"populated":1,"frozen":1}: fail("probe freeze events")
        write_retained_control(freeze_fd,b"0\n")
        if tree.parse_events(read_retained_control(events_fd))!={"populated":1,"frozen":0}: fail("probe thaw events")
        write_retained_control(kill_fd,b"1\n")
        if exact_wait_pidfd(pidfd,pid)!=128+signal.SIGKILL: fail("probe kill")
        reaped=True
        try: os.waitid(os.P_PIDFD,pidfd,os.WEXITED|os.WNOHANG)
        except ChildProcessError: pass
        else: fail("probe missing ECHILD")
        if read_retained_control(procs_fd).strip() or tree.parse_events(read_retained_control(events_fd))!={"populated":0,"frozen":0}: fail("probe populated zero")
    finally:
        if pid>0 and not reaped:
            try: syscall(SYS_PIDFD_SEND_SIGNAL,ctypes.c_int(pidfd),ctypes.c_int(signal.SIGKILL),ctypes.c_void_p(),ctypes.c_uint(0))
            except BaseException: pass
            try: exact_wait_pidfd(pidfd,pid)
            except BaseException: pass
        for fd_name,fd in (("write",write_end),("read",read_end),("pidfd",pidfd),("procs",procs_fd),("kill",kill_fd),("events",events_fd),("freeze",freeze_fd)):
            if fd>=0 and fd_is_open(fd): close_proved(fd)
        if probe_fd>=0 and fd_is_open(probe_fd):
            identity_st=os.fstat(probe_fd); identity=(identity_st.st_dev,identity_st.st_ino); close_proved(probe_fd); probe_fd=-1
        if created:
            if identity==(0,0): fail("probe retained identity unavailable")
            named=os.stat(name,dir_fd=tree.session_fd,follow_symlinks=False)
            if (named.st_dev,named.st_ino)!=identity: fail("probe removal identity")
            os.rmdir(name,dir_fd=tree.session_fd)
            try: os.stat(name,dir_fd=tree.session_fd,follow_symlinks=False)
            except FileNotFoundError: pass
            else: fail("probe removal proof")
            tree.probe_used=True


def openat2_rename_preflight(private_root_fd: int) -> None:
    os.mkdir("capability-probe",0o700,dir_fd=private_root_fd)
    parent=os.open("capability-probe",OPEN_DIR,dir_fd=private_root_fd)
    retained=-1
    try:
        os.mkdir("left",0o700,dir_fd=parent); os.mkdir("right",0o700,dir_fd=parent)
        left=os.open("left",OPEN_DIR,dir_fd=parent); right=os.open("right",OPEN_DIR,dir_fd=parent)
        try:
            for fd,name,data in ((left,"owned",b"A"),(right,"foreign",b"F")):
                member=os.open(name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW|os.O_CLOEXEC,0o600,dir_fd=fd)
                complete_write(member,data); os.close(member)
            retained=os.dup(left)
            renameat2(parent,"left",parent,"right",RENAME_EXCHANGE)
            if read_regular_at(retained,"owned")!=b"A" or read_regular_at(left,"owned")!=b"A" or read_regular_at(right,"foreign")!=b"F": fail("exchange retained capability")
            try: openat2(parent,"right/../left",OPEN_REGULAR)
            except OSError as error:
                if error.errno not in (errno.EXDEV,errno.ELOOP,errno.ENOENT): raise
            else: fail("openat2 escape")
            os.unlink("owned",dir_fd=retained); os.unlink("foreign",dir_fd=right)
        finally:
            for fd in (left,right): os.close(fd)
        os.rmdir("right",dir_fd=parent); os.rmdir("left",dir_fd=parent)
    finally:
        if retained>=0: os.close(retained)
        os.close(parent); os.rmdir("capability-probe",dir_fd=private_root_fd)


def proc_getdents64(fd_directory: int, storage: ctypes.Array[ctypes.c_char]) -> tuple[str,...]:
    if len(storage)!=65536 or os.lseek(fd_directory,0,os.SEEK_SET)!=0: fail("proc getdents reset")
    names=[]
    while True:
        count=syscall(SYS_GETDENTS64,ctypes.c_int(fd_directory),ctypes.byref(storage),ctypes.c_uint(len(storage)))
        if count==0: break
        if count<0 or count>len(storage): fail("proc getdents count")
        block=bytes(storage[:count]); offset=0
        while offset<count:
            if count-offset<20: fail("proc dirent short")
            _inode,_next,reclen,_dtype=struct.unpack_from("=QqHB",block,offset)
            if reclen<20 or reclen%8 or offset+reclen>count: fail("proc dirent record")
            field=block[offset+19:offset+reclen]; terminator=field.find(b"\x00")
            if terminator<0: fail("proc dirent name")
            try: name=field[:terminator].decode("ascii")
            except UnicodeDecodeError: fail("proc dirent ASCII")
            if name not in (".",".."): names.append(name)
            offset+=reclen
        if offset!=count: fail("proc dirent boundary")
    if len(names)!=len(set(names)): fail("proc duplicate dirent")
    return tuple(names)


def proc_readlink_exact(fd_directory: int, name: str, storage: ctypes.Array[ctypes.c_char]) -> str:
    if re.fullmatch(r"0|[1-9][0-9]*",name) is None or len(storage)!=4097: fail("proc readlink coordinate")
    encoded=name.encode("ascii")
    count=syscall(SYS_READLINKAT,ctypes.c_int(fd_directory),ctypes.c_char_p(encoded),ctypes.byref(storage),ctypes.c_size_t(len(storage)))
    if count<=0 or count>=len(storage): fail("proc readlink empty or truncated")
    raw=bytes(storage[:count])
    if b"\x00" in raw: fail("proc readlink NUL")
    try: return raw.decode("ascii")
    except UnicodeDecodeError: fail("proc readlink ASCII")


def fd_snapshot(fd_directory: int, directory_storage: ctypes.Array[ctypes.c_char], link_storage: ctypes.Array[ctypes.c_char]) -> tuple[tuple[int,str],...]:
    names=proc_getdents64(fd_directory,directory_storage)
    if any(re.fullmatch(r"0|[1-9][0-9]*",name) is None for name in names): fail("proc fd name")
    records=[]
    for name in sorted(names,key=int):
        target=proc_readlink_exact(fd_directory,name,link_storage)
        if target.startswith("socket:[") and re.fullmatch(r"socket:\[(?:[1-9][0-9]{0,9})\]",target) is None: fail("proc socket text")
        if re.fullmatch(r"socket:\[([1-9][0-9]*)\]",target):
            inode=int(target[8:-1])
            if inode>0xffffffff: fail("proc socket inode domain")
        records.append((int(name),target))
    return tuple(records)


def fd_snapshot_bytes(snapshot: tuple[tuple[int,str],...]) -> bytes:
    numbers=tuple(row[0] for row in snapshot)
    if numbers!=tuple(sorted(numbers)) or len(numbers)!=len(set(numbers)): fail("snapshot order")
    return b",".join(str(number).encode("ascii") for number in numbers)


@dataclass
class DMAuditOwnedFD:
    acquisition_serial: int=0
    local_fd: int=-1
    kind: str=""
    target_pidfd_serial: int=0
    targetfd: str=""
    state: str="RESERVED"


@dataclass(frozen=True)
class DMAuditIdentityExpectation:
    subject: str
    outer_pid: int
    start_time: int
    nspid: tuple[int,...]
    inner_pid: int
    cgroup_raw: str
    cgroup_dev: int
    cgroup_ino: int
    session: int=0
    child: int=0
    role: str=""
    owner: str=""
    identity_sha256: str=""


class DMAuditMismatch(PossessionFailure):
    def __init__(self, mismatch: str, detail: str="") -> None:
        if mismatch not in ("NONE","MEMORY","OPEN","RETURN","CLOEXEC","TYPE","INODE","PROC","DIAG","CARDINALITY","IDENTITY","SNAPSHOT","GENERATION","CLOSE","EBADF","HOLDER","CONTROL"):
            fail("D-M2 mismatch token")
        super().__init__(E_POSSESSION,detail)
        self.mismatch=mismatch


def dmaudit_identity_bytes(process_fd: int, expected: DMAuditIdentityExpectation) -> bytes:
    if expected.subject not in ("CHILD","GUARDIAN") or expected.outer_pid<=0 or expected.start_time<=0 or not expected.nspid or expected.nspid[-1]!=expected.inner_pid or expected.cgroup_dev<0 or expected.cgroup_ino<=0:
        raise DMAuditMismatch("IDENTITY","D-M2 expected identity")
    status=parse_proc_status(read_regular_at(process_fd,"status",1024*1024))
    nspid=tuple(int(value) for value in status.get("NSpid","").split())
    uid=tuple(int(value) for value in status.get("Uid","").split()); gid=tuple(int(value) for value in status.get("Gid","").split())
    groups=tuple(int(value) for value in status.get("Groups","").split())
    cgroup=read_regular_at(process_fd,"cgroup",1024*1024).decode("ascii")
    start_time=proc_start_time(process_fd,expected.outer_pid)
    if start_time!=expected.start_time or nspid!=expected.nspid or uid!=(65534,)*4 or gid!=(65534,)*4 or groups or status.get("Threads")!="1" or cgroup!=expected.cgroup_raw:
        raise DMAuditMismatch("IDENTITY","D-M2 live identity")
    vector=",".join(str(value) for value in nspid)
    common=(f"subject={expected.subject} outer_pid={expected.outer_pid} start_time={start_time} nspid={vector} "
            "outer_ruid=65534 outer_euid=65534 outer_suid=65534 outer_fsuid=65534 outer_rgid=65534 outer_egid=65534 outer_sgid=65534 outer_fsgid=65534 "
            "inner_ruid=0 inner_euid=0 inner_suid=0 inner_fsuid=0 inner_rgid=0 inner_egid=0 inner_sgid=0 inner_fsgid=0 outer_groups=NONE inner_groups=NONE threads=1")
    if expected.subject=="CHILD":
        if expected.session<0 or expected.child<=0 or expected.role not in set(ROLE_BY_TARGET.values()) or not expected.owner:
            raise DMAuditMismatch("IDENTITY","D-M2 child identity grammar")
        line=f"{common} session={expected.session} child={expected.child} role={expected.role} owner={expected.owner} cgroup_dev={expected.cgroup_dev} cgroup_ino={expected.cgroup_ino}"
    else:
        line=f"{common} guardian_pidfd_serial=1 cgroup_dev={expected.cgroup_dev} cgroup_ino={expected.cgroup_ino}"
    return line.encode("ascii")


def dmaudit_identity_digest(identity_bytes: bytes) -> str:
    return sha256(b"P15R-PROC-IDENTITY-v6 "+identity_bytes)


@dataclass
class PIDFDLifetimeEntry:
    pidfd_serial: int
    local_fd: int
    subject: str
    outer_pid: int
    start_time: int
    nspid_sha256: str
    credential_sha256: str
    cgroup_dev: int
    cgroup_ino: int
    state: str="RETURNED"


def pidfd_lifetime_entry(pidfd_serial: int, local_fd: int, expected: DMAuditIdentityExpectation, identity_bytes: bytes) -> PIDFDLifetimeEntry:
    vector=",".join(str(value) for value in expected.nspid); nspid_bytes=f"subject={expected.subject} nspid={vector}".encode("ascii")
    entry=PIDFDLifetimeEntry(pidfd_serial,local_fd,expected.subject,expected.outer_pid,expected.start_time,sha256(b"P15R-PIDFD-NSPID-v6 "+nspid_bytes),sha256(b"P15R-PIDFD-CREDENTIAL-v6 "+identity_bytes),expected.cgroup_dev,expected.cgroup_ino)
    if pidfd_serial<=0 or local_fd<0 or expected.subject not in ("CHILD","GUARDIAN") or any(re.fullmatch(r"[0-9a-f]{64}",value) is None for value in (entry.nspid_sha256,entry.credential_sha256)): fail("pidfd lifetime ledger")
    return entry


@dataclass
class LongLivedProcRootLedger:
    local_fd: int
    st_dev: int
    st_ino: int
    fd_flags: int
    state: str="OPEN"


def open_long_lived_proc_root() -> tuple[int,LongLivedProcRootLedger]:
    fd=os.open("/proc",OPEN_DIR); flags=fcntl.fcntl(fd,fcntl.F_GETFD); observed=os.fstat(fd)
    if flags!=FD_CLOEXEC or not stat.S_ISDIR(observed.st_mode):
        close_proved(fd); fail("LONG_LIVED_PROC_ROOT")
    return fd,LongLivedProcRootLedger(fd,observed.st_dev,observed.st_ino,flags)


class DMAuditTranscript:
    DOMAIN=b"P15R-FD-AUDIT-TRANSCRIPT-v6"

    def __init__(self) -> None:
        self.items: list[tuple[int,bytes]]=[]

    def add(self, tag: int, value: bytes) -> None:
        if type(tag) is not int or not 0<tag<2**16 or type(value) is not bytes: fail("D-M2 transcript item")
        self.items.append((tag,bytes(value)))

    def success_digest(self, candidate_count: int, fd5: bool) -> str:
        expected=list(range(1,11))+[11]*candidate_count+([12] if fd5 else [])+list(range(13,22))
        if [tag for tag,_value in self.items]!=expected: fail("D-M2 success schedule")
        return self.digest()

    def digest(self) -> str:
        material=self.DOMAIN+u32be(len(self.items))+b"".join(u16be(tag)+u64be(len(value))+value for tag,value in self.items)
        return sha256(material)


@dataclass
class AuditEvidence:
    epoch: int
    transcript: str
    child_slot_inode: int
    guardian_peer_inode: int


class FDAuditor:
    """P-only D-M2 auditor.  Every installed duplicate is closed and proved EBADF."""
    def __init__(self, control: FramedControl, proc_root: int, proc_root_ledger: LongLivedProcRootLedger, guardian_pid: int, guardian_pidfd: int, guardian_identity: DMAuditIdentityExpectation, guardian_pidfd_ledger: PIDFDLifetimeEntry, diag: UnixDiagOracle, tree: CgroupTree) -> None:
        if (proc_root_ledger.local_fd,proc_root_ledger.fd_flags,proc_root_ledger.state)!=(proc_root,FD_CLOEXEC,"OPEN") or not stat.S_ISDIR(os.fstat(proc_root).st_mode) or (os.fstat(proc_root).st_dev,os.fstat(proc_root).st_ino)!=(proc_root_ledger.st_dev,proc_root_ledger.st_ino): fail("LONG_LIVED_PROC_ROOT ledger")
        self.control=control; self.proc_root=proc_root; self.proc_root_ledger=proc_root_ledger; self.guardian_pid=guardian_pid; self.guardian_pidfd=guardian_pidfd; self.diag=diag; self.epoch=0; self.guardian_pidfd_serial=1; self.next_acquisition_serial=1
        cgroup_st=os.fstat(tree.guardian_fd); process=openat2(proc_root,str(guardian_pid),OPEN_PATH_DIR)
        try:
            status=parse_proc_status(read_regular_at(process,"status",1024*1024)); start_time=proc_start_time(process,guardian_pid); cgroup=read_regular_at(process,"cgroup",1024*1024).decode("ascii")
            nspid=tuple(int(value) for value in status.get("NSpid","").split()); uid=tuple(int(value) for value in status.get("Uid","").split()); gid=tuple(int(value) for value in status.get("Gid","").split())
            if not nspid or nspid[-1]!=1 or uid!=(65534,)*4 or gid!=(65534,)*4 or status.get("Groups","").split() or status.get("Threads")!="1" or cgroup!="0::"+tree.relative("guardian")+"\n": fail("guardian D-M2 identity")
            expectation=DMAuditIdentityExpectation("GUARDIAN",guardian_pid,start_time,nspid,1,cgroup,cgroup_st.st_dev,cgroup_st.st_ino)
            identity=dmaudit_identity_bytes(process,expectation); identity_sha=dmaudit_identity_digest(identity)
            if replace(expectation,identity_sha256=identity_sha)!=guardian_identity or (guardian_pidfd_ledger.pidfd_serial,guardian_pidfd_ledger.local_fd,guardian_pidfd_ledger.subject,guardian_pidfd_ledger.outer_pid,guardian_pidfd_ledger.start_time,guardian_pidfd_ledger.nspid_sha256,guardian_pidfd_ledger.credential_sha256,guardian_pidfd_ledger.cgroup_dev,guardian_pidfd_ledger.cgroup_ino,guardian_pidfd_ledger.state)!=(1,guardian_pidfd,"GUARDIAN",guardian_pid,start_time,sha256(b"P15R-PIDFD-NSPID-v6 "+f"subject=GUARDIAN nspid={','.join(str(value) for value in nspid)}".encode("ascii")),sha256(b"P15R-PIDFD-CREDENTIAL-v6 "+identity),cgroup_st.st_dev,cgroup_st.st_ino,"VALIDATED"): fail("guardian pidfd lifetime join")
            self.guardian_identity=guardian_identity; self.guardian_pidfd_ledger=guardian_pidfd_ledger
        finally: close_proved(process)

    @staticmethod
    def _abort_value(stage: int, mismatch_hint: str, caught: BaseException, targetfd: str, row: DMAuditOwnedFD|None) -> bytes:
        if isinstance(caught,DMAuditMismatch): mismatch=caught.mismatch
        elif isinstance(caught,MemoryError): mismatch="MEMORY"
        elif isinstance(caught,OSError): mismatch=mismatch_hint
        else: mismatch=mismatch_hint if mismatch_hint in ("NONE","MEMORY","OPEN","RETURN","CLOEXEC","TYPE","INODE","PROC","DIAG","CARDINALITY","IDENTITY","SNAPSHOT","GENERATION","CLOSE","EBADF","HOLDER","CONTROL") else "NONE"
        observed_errno=(caught.errno or 0) if isinstance(caught,OSError) else 0
        base=f"stage={stage} errno={observed_errno} mismatch={mismatch}"
        if stage in (3,4,5,6,10,11):
            if row is not None and row.state=="OPEN":
                base+=f" acquisition_serial={row.acquisition_serial} local_fd={row.local_fd} targetfd={row.targetfd}"
            else:
                base+=f" targetfd={targetfd}"
        return base.encode("ascii")

    def audit(self, kind: str, session: int, child: int, outer_pid: int, slot: int, child_pidfd: int, child_pidfd_serial: int, child_identity: DMAuditIdentityExpectation, child_pidfd_ledger: PIDFDLifetimeEntry, p_peer_fd: int=-1) -> AuditEvidence:
        validate_p_signal_barrier()
        if kind not in AUDIT_KINDS or ("FD"+str(slot)) not in AUDIT_SLOTS: fail("audit coordinate")
        if child_pidfd<0 or child_pidfd_serial<=self.guardian_pidfd_serial or fcntl.fcntl(child_pidfd,fcntl.F_GETFD)!=FD_CLOEXEC or (child_identity.subject,child_identity.outer_pid,child_identity.session,child_identity.child)!=("CHILD",outer_pid,session,child) or (child_pidfd_ledger.pidfd_serial,child_pidfd_ledger.local_fd,child_pidfd_ledger.subject,child_pidfd_ledger.outer_pid,child_pidfd_ledger.start_time,child_pidfd_ledger.cgroup_dev,child_pidfd_ledger.cgroup_ino,child_pidfd_ledger.state)!=(child_pidfd_serial,child_pidfd,"CHILD",outer_pid,child_identity.start_time,child_identity.cgroup_dev,child_identity.cgroup_ino,"VALIDATED") or self.guardian_pidfd_ledger.state!="VALIDATED": fail("retained child pidfd")
        self.epoch+=1; transcript=DMAuditTranscript(); base_slots: list[DMAuditOwnedFD]=[]; candidate_slots: list[DMAuditOwnedFD]=[]; generation=0; stage=1; acknowledged=False; candidate_count=-1; completed_candidates=0; close_ambiguous=False
        current_targetfd=""; current_row: DMAuditOwnedFD|None=None; mismatch_hint="CONTROL"; candidate_numbers: tuple[int,...]=(); before_g: tuple[tuple[int,str],...]=()
        enter=f"FD_AUDIT_QUIESCE_ENTER audit_epoch={self.epoch} kind={kind} session={session} child={child} slot=FD{slot} child_pidfd_serial={child_pidfd_serial} guardian_pidfd_serial={self.guardian_pidfd_serial}"

        def own(row: DMAuditOwnedFD, fd: int, row_kind: str, pidfd_serial: int, targetfd: str) -> DMAuditOwnedFD:
            if row.state!="RESERVED" or fd<0 or any(other.state=="OPEN" and other.local_fd==fd for other in base_slots+candidate_slots): raise DMAuditMismatch("IDENTITY","D-M2 ledger slot")
            row.acquisition_serial=self.next_acquisition_serial; self.next_acquisition_serial+=1; row.local_fd=fd; row.kind=row_kind; row.target_pidfd_serial=pidfd_serial; row.targetfd=targetfd; row.state="OPEN"
            return row

        def proc_value(row: DMAuditOwnedFD, st: os.stat_result, identity_digest: str) -> bytes:
            return f"acquisition_serial={row.acquisition_serial} local_fd={row.local_fd} kind={row.kind} target_pidfd_serial={row.target_pidfd_serial} targetfd={row.targetfd} fd_flags={FD_CLOEXEC} st_mode={stat.S_IFMT(st.st_mode)} st_dev={st.st_dev} st_ino={st.st_ino} identity_sha256={identity_digest}".encode("ascii")

        def unwind(prior_failure: bool) -> tuple[bytes,BaseException|None]:
            nonlocal close_ambiguous
            rows=[]
            close_failure: BaseException|None=None
            opened=sorted((row for row in base_slots+candidate_slots if row.state=="OPEN"),key=lambda row:row.acquisition_serial,reverse=True)
            for row in opened:
                close_return=0; close_errno=0
                try: os.close(row.local_fd)
                except OSError as error: close_return=-1; close_errno=error.errno or 0
                f_getfd_return=-1; f_getfd_errno=0
                try: f_getfd_return=fcntl.fcntl(row.local_fd,fcntl.F_GETFD)
                except OSError as error: f_getfd_errno=error.errno or 0
                proved=close_return==0 and close_errno==0 and f_getfd_return==-1 and f_getfd_errno==errno.EBADF
                if not proved:
                    close_ambiguous=True; row.state="AMBIGUOUS_CRASH_ONLY"
                    if not prior_failure and close_failure is None:
                        mismatch="CLOSE" if close_return!=0 else "EBADF"
                        transcript.add(65533,f"stage=18 errno={close_errno or f_getfd_errno} mismatch={mismatch} acquisition_serial={row.acquisition_serial} local_fd={row.local_fd} targetfd={row.targetfd}".encode("ascii"))
                        close_failure=DMAuditMismatch(mismatch,"D-M2 unwind")
                else: row.state="CLOSED_PROVED"
                receipt=f"acquisition_serial={row.acquisition_serial} local_fd={row.local_fd} close_return={close_return} close_errno={close_errno} f_getfd_return={f_getfd_return} f_getfd_errno={f_getfd_errno} final_state={row.state}".encode("ascii")
                rows.append(receipt)
            return u32be(len(rows))+b"".join(u64be(len(value))+value for value in rows),close_failure

        failure: BaseException|None=None
        try:
            self.control.send(enter,str(self.epoch)); ack=self.control.receive(str(self.epoch))
            match=re.fullmatch(rf"FD_AUDIT_QUIESCE_ACK audit_epoch={self.epoch} kind={kind} session={session} child={child} slot=FD{slot} g_fd_generation=([1-9][0-9]*)",ack)
            if match is None: raise DMAuditMismatch("CONTROL","D-M2 ACK")
            generation=int(match.group(1)); acknowledged=True
            transcript.add(1,f"audit_epoch={self.epoch} kind={kind} session={session} child={child} slot=FD{slot} child_pidfd_serial={child_pidfd_serial} guardian_pidfd_serial={self.guardian_pidfd_serial} g_fd_generation={generation}".encode("ascii"))
            stage=2; mismatch_hint="MEMORY"; base_slots=[DMAuditOwnedFD() for _index in range(5)]; child_directory_storage=ctypes.create_string_buffer(65536); guardian_directory_storage=ctypes.create_string_buffer(65536); link_storage=ctypes.create_string_buffer(4097); transcript.add(2,b"reserved_proc_slots=4 reserved_child_duplicate_slots=1")
            stage=3; current_targetfd="PROC_PID_DIR"; current_row=None; mismatch_hint="OPEN"; child_proc_fd=os.open(str(outer_pid),OPEN_DIR,dir_fd=self.proc_root); child_row=own(base_slots[0],child_proc_fd,"CHILD_PROC_PID_DIR",child_pidfd_serial,current_targetfd); current_row=child_row
            mismatch_hint="CLOEXEC"; child_proc_flags=fcntl.fcntl(child_proc_fd,fcntl.F_GETFD)
            if child_proc_flags!=FD_CLOEXEC: raise DMAuditMismatch("CLOEXEC","child proc dir")
            child_proc_st=os.fstat(child_proc_fd)
            if not stat.S_ISDIR(child_proc_st.st_mode): raise DMAuditMismatch("TYPE","child proc dir")
            mismatch_hint="PROC"; child_identity_before=dmaudit_identity_bytes(child_proc_fd,child_identity); child_identity_sha=dmaudit_identity_digest(child_identity_before)
            if child_identity.identity_sha256!=child_identity_sha: raise DMAuditMismatch("IDENTITY","child pidfd identity join")
            transcript.add(3,proc_value(child_row,child_proc_st,child_identity_sha))
            stage=4; current_targetfd="PROC_FD_DIR"; current_row=None; mismatch_hint="OPEN"; child_fds_fd=os.open("fd",OPEN_DIR,dir_fd=child_proc_fd); child_fds_row=own(base_slots[1],child_fds_fd,"CHILD_PROC_FD_DIR",child_pidfd_serial,current_targetfd); current_row=child_fds_row
            mismatch_hint="CLOEXEC"; child_fds_flags=fcntl.fcntl(child_fds_fd,fcntl.F_GETFD)
            if child_fds_flags!=FD_CLOEXEC: raise DMAuditMismatch("CLOEXEC","child fd dir")
            child_fds_st=os.fstat(child_fds_fd)
            if not stat.S_ISDIR(child_fds_st.st_mode): raise DMAuditMismatch("TYPE","child fd dir")
            transcript.add(4,proc_value(child_fds_row,child_fds_st,child_identity_sha))
            stage=5; current_targetfd="PROC_PID_DIR"; current_row=None; mismatch_hint="OPEN"; guardian_proc_fd=os.open(str(self.guardian_pid),OPEN_DIR,dir_fd=self.proc_root); guardian_row=own(base_slots[2],guardian_proc_fd,"GUARDIAN_PROC_PID_DIR",self.guardian_pidfd_serial,current_targetfd); current_row=guardian_row
            mismatch_hint="CLOEXEC"; guardian_proc_flags=fcntl.fcntl(guardian_proc_fd,fcntl.F_GETFD)
            if guardian_proc_flags!=FD_CLOEXEC: raise DMAuditMismatch("CLOEXEC","guardian proc dir")
            guardian_proc_st=os.fstat(guardian_proc_fd)
            if not stat.S_ISDIR(guardian_proc_st.st_mode): raise DMAuditMismatch("TYPE","guardian proc dir")
            mismatch_hint="PROC"; guardian_identity_before=dmaudit_identity_bytes(guardian_proc_fd,self.guardian_identity); guardian_identity_sha=dmaudit_identity_digest(guardian_identity_before)
            if self.guardian_identity.identity_sha256!=guardian_identity_sha: raise DMAuditMismatch("IDENTITY","guardian pidfd identity join")
            transcript.add(5,proc_value(guardian_row,guardian_proc_st,guardian_identity_sha))
            stage=6; current_targetfd="PROC_FD_DIR"; current_row=None; mismatch_hint="OPEN"; guardian_fds_fd=os.open("fd",OPEN_DIR,dir_fd=guardian_proc_fd); guardian_fds_row=own(base_slots[3],guardian_fds_fd,"GUARDIAN_PROC_FD_DIR",self.guardian_pidfd_serial,current_targetfd); current_row=guardian_fds_row
            mismatch_hint="CLOEXEC"; guardian_fds_flags=fcntl.fcntl(guardian_fds_fd,fcntl.F_GETFD)
            if guardian_fds_flags!=FD_CLOEXEC: raise DMAuditMismatch("CLOEXEC","guardian fd dir")
            guardian_fds_st=os.fstat(guardian_fds_fd)
            if not stat.S_ISDIR(guardian_fds_st.st_mode): raise DMAuditMismatch("TYPE","guardian fd dir")
            transcript.add(6,proc_value(guardian_fds_row,guardian_fds_st,guardian_identity_sha))
            stage=7; current_row=None; mismatch_hint="SNAPSHOT"; before_child=fd_snapshot(child_fds_fd,child_directory_storage,link_storage); transcript.add(7,fd_snapshot_bytes(before_child))
            stage=8; before_g=fd_snapshot(guardian_fds_fd,guardian_directory_storage,link_storage); transcript.add(8,fd_snapshot_bytes(before_g))
            candidate_numbers=tuple(row[0] for row in before_g if re.fullmatch(r"socket:\[[1-9][0-9]*\]",row[1]) is not None)
            candidate_count=len(candidate_numbers)
            stage=9; mismatch_hint="MEMORY"; candidate_slots=[DMAuditOwnedFD() for _candidate in candidate_numbers]; candidates: list[tuple[int,os.stat_result]|None]=[None]*candidate_count; transcript.add(9,f"reserved_g_candidate_slots={candidate_count}".encode("ascii"))
            stage=10; current_targetfd=str(slot); current_row=None; mismatch_hint="RETURN"; child_dup=syscall(SYS_PIDFD_GETFD,ctypes.c_int(child_pidfd),ctypes.c_int(slot),ctypes.c_uint(0)); child_socket_row=own(base_slots[4],child_dup,"CHILD_SOCKET_DUP",child_pidfd_serial,current_targetfd); current_row=child_socket_row
            mismatch_hint="CLOEXEC"; child_flags=fcntl.fcntl(child_dup,fcntl.F_GETFD)
            if child_flags!=FD_CLOEXEC: raise DMAuditMismatch("CLOEXEC","D-M2 child duplicate")
            mismatch_hint="TYPE"; child_stat=os.fstat(child_dup)
            child_proc_rows=[row for row in before_child if row[0]==slot]
            if not stat.S_ISSOCK(child_stat.st_mode): raise DMAuditMismatch("TYPE","D-M2 child duplicate")
            if not 0<child_stat.st_ino<=0xffffffff: raise DMAuditMismatch("INODE","D-M2 child duplicate")
            if len(child_proc_rows)!=1 or child_proc_rows[0][1]!="socket:["+str(child_stat.st_ino)+"]": raise DMAuditMismatch("PROC","D-M2 child duplicate")
            transcript.add(10,f"acquisition_serial={child_socket_row.acquisition_serial} local_fd={child_dup} target_pidfd_serial={child_pidfd_serial} targetfd={slot} fd_flags={child_flags} st_mode={stat.S_IFMT(child_stat.st_mode)} st_dev={child_stat.st_dev} st_ino={child_stat.st_ino} proc_inode={child_stat.st_ino}".encode("ascii"))
            for candidate_index,targetfd in enumerate(candidate_numbers):
                stage=11; current_targetfd=str(targetfd); current_row=None; mismatch_hint="RETURN"; local=syscall(SYS_PIDFD_GETFD,ctypes.c_int(self.guardian_pidfd),ctypes.c_int(targetfd),ctypes.c_uint(0)); row=own(candidate_slots[candidate_index],local,"GUARDIAN_SOCKET_DUP",self.guardian_pidfd_serial,current_targetfd); current_row=row
                mismatch_hint="CLOEXEC"; flags=fcntl.fcntl(local,fcntl.F_GETFD)
                if flags!=FD_CLOEXEC: raise DMAuditMismatch("CLOEXEC","D-M2 G candidate")
                mismatch_hint="TYPE"; observed=os.fstat(local)
                proc_row=[entry for entry in before_g if entry[0]==targetfd]
                if not stat.S_ISSOCK(observed.st_mode): raise DMAuditMismatch("TYPE","D-M2 G candidate")
                if not 0<observed.st_ino<=0xffffffff: raise DMAuditMismatch("INODE","D-M2 G candidate")
                if len(proc_row)!=1 or proc_row[0][1]!="socket:["+str(observed.st_ino)+"]": raise DMAuditMismatch("PROC","D-M2 G candidate")
                transcript.add(11,f"acquisition_serial={row.acquisition_serial} local_fd={local} target_pidfd_serial={self.guardian_pidfd_serial} targetfd={targetfd} fd_flags={flags} st_mode={stat.S_IFMT(observed.st_mode)} st_dev={observed.st_dev} st_ino={observed.st_ino} proc_inode={observed.st_ino}".encode("ascii")); candidates[candidate_index]=(targetfd,observed); completed_candidates+=1
            if slot==5:
                stage=12; current_row=None; mismatch_hint="HOLDER"
                if p_peer_fd<0: raise DMAuditMismatch("HOLDER","D-M2 P peer absent")
                p_peer=os.fstat(p_peer_fd); p_flags=fcntl.fcntl(p_peer_fd,fcntl.F_GETFD)
                if p_flags!=FD_CLOEXEC or not stat.S_ISSOCK(p_peer.st_mode) or not 0<p_peer.st_ino<=0xffffffff: raise DMAuditMismatch("HOLDER","D-M2 P peer")
                transcript.add(12,f"local_fd={p_peer_fd} fd_flags={p_flags} st_mode={stat.S_IFMT(p_peer.st_mode)} st_dev={p_peer.st_dev} st_ino={p_peer.st_ino}".encode("ascii")); peer_inode=p_peer.st_ino
                if any(candidate is not None and candidate[1].st_ino in (child_stat.st_ino,peer_inode) for candidate in candidates): raise DMAuditMismatch("CARDINALITY","FD5 zero G holder")
            stage=13; current_row=None; mismatch_hint="DIAG"; child_to_peer=self.diag.query(child_stat.st_ino)
            if slot!=5:
                peer_inode=child_to_peer.peer_inode
                if len([1 for candidate in candidates if candidate is not None and candidate[1].st_ino==peer_inode])!=1: raise DMAuditMismatch("CARDINALITY","D-M2 G holder cardinality")
            if child_to_peer.peer_inode!=peer_inode: raise DMAuditMismatch("DIAG","D-M2 child peer")
            transcript.add(13,child_to_peer.raw48)
            stage=14; mismatch_hint="DIAG"; peer_to_child=self.diag.query(peer_inode)
            if peer_to_child.peer_inode!=child_stat.st_ino: raise DMAuditMismatch("DIAG","D-M2 reciprocal peer")
            transcript.add(14,peer_to_child.raw48)
            stage=15; mismatch_hint="SNAPSHOT"; after_child=fd_snapshot(child_fds_fd,child_directory_storage,link_storage); transcript.add(15,fd_snapshot_bytes(after_child))
            stage=16; after_g=fd_snapshot(guardian_fds_fd,guardian_directory_storage,link_storage); transcript.add(16,fd_snapshot_bytes(after_g))
            stage=17; mismatch_hint="IDENTITY"; child_identity_after=dmaudit_identity_bytes(child_proc_fd,child_identity); guardian_identity_after=dmaudit_identity_bytes(guardian_proc_fd,self.guardian_identity)
            if before_child!=after_child or before_g!=after_g: raise DMAuditMismatch("SNAPSHOT","D-M2 snapshot drift")
            if child_identity_after!=child_identity_before or guardian_identity_after!=guardian_identity_before: raise DMAuditMismatch("IDENTITY","D-M2 identity drift")
            transcript.add(17,f"child_identity_sha256={dmaudit_identity_digest(child_identity_after)} guardian_identity_sha256={dmaudit_identity_digest(guardian_identity_after)} child_snapshot_equal=1 g_snapshot_equal=1 g_fd_generation={generation}".encode("ascii"))
        except BaseException as caught:
            failure=caught

        if failure is not None:
            transcript.add(65533,self._abort_value(stage,mismatch_hint,failure,current_targetfd,current_row))
        close_ledger,close_failure=unwind(failure is not None); transcript.add(18,close_ledger)
        if failure is None and close_failure is not None: failure=close_failure
        if close_ambiguous or not acknowledged:
            fail("D-M2 close/control ambiguity")
        if failure is None:
            try:
                stage=19; mismatch_hint="DIAG"; post_child=self.diag.query(child_stat.st_ino)
                if post_child.peer_inode!=peer_inode: raise DMAuditMismatch("DIAG","D-M2 post child peer")
                transcript.add(19,post_child.raw48)
                stage=20; post_peer=self.diag.query(peer_inode)
                if post_peer.peer_inode!=child_stat.st_ino: raise DMAuditMismatch("DIAG","D-M2 post reciprocal peer")
                transcript.add(20,post_peer.raw48)
                stage=21; mismatch_hint="HOLDER"
                child_original_holders=sum(link=="socket:["+str(child_stat.st_ino)+"]" for _number,link in after_child)
                g_matching_holders=sum(link=="socket:["+str(peer_inode)+"]" for _number,link in after_g)
                if slot==5:
                    post_p_peer=os.fstat(p_peer_fd); post_p_flags=fcntl.fcntl(p_peer_fd,fcntl.F_GETFD)
                    peer_original_holders=int(post_p_flags==FD_CLOEXEC and stat.S_ISSOCK(post_p_peer.st_mode) and (post_p_peer.st_dev,post_p_peer.st_ino)==(p_peer.st_dev,peer_inode))
                else:
                    peer_original_holders=g_matching_holders
                p_audit_duplicates=sum(row.local_fd>=0 and fd_is_open(row.local_fd) for row in base_slots+candidate_slots)
                all_closed=all(row.state in ("RESERVED","CLOSED_PROVED") for row in base_slots+candidate_slots)
                restored=int(child_original_holders==1 and peer_original_holders==1 and p_audit_duplicates==0 and g_matching_holders==(0 if slot==5 else 1) and all_closed)
                if restored!=1: raise DMAuditMismatch("HOLDER","D-M2 permanent holder restoration")
                transcript.add(21,f"slot=FD{slot} child_original_holders={child_original_holders} peer_original_holders={peer_original_holders} p_audit_duplicates={p_audit_duplicates} g_matching_holders={g_matching_holders} restored={restored}".encode("ascii"))
            except BaseException as caught:
                failure=caught; transcript.add(65533,self._abort_value(stage,mismatch_hint,caught,"",None))
        if failure is None:
            digest=transcript.success_digest(candidate_count,slot==5); outcome="PASS"
        else:
            existing=[tag for tag,_value in transcript.items]
            for tag in range(1,22):
                if tag==12 and slot!=5: continue
                if tag==11:
                    if candidate_count<0: transcript.add(65534,b"missing_tag=11 candidate_set=UNFIXED")
                    else:
                        for candidate in tuple(row[0] for row in before_g if re.fullmatch(r"socket:\[[1-9][0-9]*\]",row[1]) is not None)[completed_candidates:]: transcript.add(65534,f"missing_tag=11 candidate={candidate}".encode("ascii"))
                elif tag not in existing: transcript.add(65534,f"missing_tag={tag}".encode("ascii"))
            digest=transcript.digest(); outcome="ABORT"
        exit_record=f"FD_AUDIT_QUIESCE_EXIT audit_epoch={self.epoch} kind={kind} session={session} child={child} slot=FD{slot} g_fd_generation={generation} outcome={outcome} transcript={digest}"
        self.control.send(exit_record,str(self.epoch)); exit_ack=self.control.receive(str(self.epoch)); expected=exit_record.replace("FD_AUDIT_QUIESCE_EXIT ","FD_AUDIT_QUIESCE_EXIT_ACK ",1)
        if exit_ack!=expected: fail("D-M2 EXIT_ACK")
        validate_p_signal_barrier()
        if failure is not None: raise failure
        return AuditEvidence(self.epoch,digest,child_stat.st_ino,peer_inode)


@dataclass(frozen=True)
class ObjectIdentity:
    handle: int
    session: int
    kind: str
    dev: int
    ino: int


class GuardianChannel:
    """G-side control adapter; D-M2 is the only operation admitted while quiesced."""
    def __init__(self, control: FramedControl) -> None:
        self.control=control; self.fd_generation=1; self.last_audit_epoch=0; self.quiesced=False; self.failure_hook: Callable[[bytes],None]|None=None
        self.audit_validator: Callable[[str,int,int,int,int],None]|None=None
        self.freeze_audit_begin: Callable[[],None]|None=None; self.freeze_audit_end: Callable[[],None]|None=None
        self.pending_signal=0; self.finalizing=False; self.admission_closed=False; self.boundary_ledger: BoundaryLedger|None=None; self.boundary_failure: BoundaryFailureTombstone|None=None; self.boundary_terminal_context: BoundaryTerminalContext|None=None; self.boundary_receipt: BoundaryFailureReceipt|BoundaryTerminalSuccessReceipt|None=None
        self.boundary_hashes={"hp":"NONE","hg":"NONE","hm":"NONE","mech":"NONE","contract":"NONE","profile":HOOK_CUSTODY_PROFILE_SHA256}

    def send(self, record: str, key: str="0") -> EndpointEnqueueReceipt:
        if self.quiesced and record.partition(" ")[0] not in D_M2_FORMS:
            fail("allocation during D-M2")
        if record.startswith("FREEZE_REQUEST ") and record.endswith(" phase=METHOD"):
            if self.freeze_audit_begin is None: fail("frozen-reference audit authority")
            self.freeze_audit_begin()
        return self.control.send(record,key)

    def _accept_signal(self, record: str) -> None:
        values=parse_exact(record,"SIGNAL_PENDING",(("signo",r"[1-9][0-9]*"),)); signo=int(values["signo"])
        if self.pending_signal or signo not in HANDLED_SIGNALS or self.quiesced: fail("signal pending state")
        self.pending_signal=signo; self.admission_closed=True

    def poll_signal(self) -> None:
        poller=select.poll(); poller.register(self.control.sock,select.POLLIN|select.POLLHUP|select.POLLERR)
        events=poller.poll(0)
        if not events: return
        if events[0][1]&(select.POLLHUP|select.POLLERR): fail("control failure while polling signal")
        record=self.control.receive()
        if record.partition(" ")[0]!="SIGNAL_PENDING": fail("non-signal record at final signal poll")
        self._accept_signal(record)

    def receive_fd(self, expected_record: str) -> int:
        space=socket.CMSG_SPACE(array.array("i",[0]).itemsize)
        try: packet,ancillary,flags,_address=self.control.sock.recvmsg(MAX_FRAME+5,space,socket.MSG_CMSG_CLOEXEC)
        except OSError: self.control.retain_failure("CONTROL_RECEIVE_FD",b""); raise
        values=received_rights(ancillary)
        if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(packet)<5:
            discard_rights(values)
            self.control.retain_failure("CONTROL_RECEIVE_FD",packet); fail("guardian rights packet")
        size=struct.unpack(">I",packet[:4])[0]; payload=packet[4:]
        if size==0 or size>MAX_FRAME or size!=len(payload) or b"\x00" in payload or b"\n" in payload or not payload.isascii():
            discard_rights(values)
            self.control.retain_failure("CONTROL_RECEIVE_FD",packet); fail("guardian rights frame")
        record=payload.decode("ascii")
        if record.partition(" ")[0]=="SIGNAL_PENDING" and not ancillary:
            self.control.dispatcher.validate("P_TO_G",record); self._accept_signal(record)
            raise AuthenticatedSignal(self.pending_signal)
        if record!=expected_record or len(ancillary)!=1:
            discard_rights(values)
            self.control.retain_failure("CONTROL_RECEIVE_FD",packet); fail("guardian rights record")
        level,kind,data=ancillary[0]
        if (level,kind)!=(socket.SOL_SOCKET,socket.SCM_RIGHTS) or len(data)!=array.array("i").itemsize or len(values)!=1:
            discard_rights(values)
            self.control.retain_failure("CONTROL_RECEIVE_FD",packet); fail("guardian rights cardinality")
        if fcntl.fcntl(values[0],fcntl.F_GETFD)!=FD_CLOEXEC:
            discard_rights(values); self.control.retain_failure("CONTROL_RECEIVE_FD",packet); fail("guardian rights CLOEXEC")
        try: self.control.dispatcher.validate("P_TO_G",record)
        except BaseException: discard_rights(values); raise
        return values[0]

    def receive(self, predicate: Callable[[str],bool]|None=None, key: str="0") -> str:
        while True:
            try: record=self.control.receive(key)
            except (PossessionFailure,OSError):
                if self.failure_hook is not None: self.failure_hook(self.control.first_failure_record)
                raise
            if record.partition(" ")[0]=="FD_AUDIT_QUIESCE_ENTER":
                self._d_m2(record); continue
            if record.partition(" ")[0]=="SIGNAL_PENDING":
                self._accept_signal(record); signo=self.pending_signal
                if self.finalizing: continue
                raise AuthenticatedSignal(signo)
            if record.partition(" ")[0]=="FROZEN_NOREFS":
                if self.freeze_audit_end is None: fail("frozen-reference audit completion")
                self.freeze_audit_end()
            if predicate is not None and not predicate(record): fail("unexpected P record")
            return record

    def _d_m2(self, enter: str) -> None:
        match=re.fullmatch(r"FD_AUDIT_QUIESCE_ENTER audit_epoch=([1-9][0-9]*) kind=(PREFLIGHT_PROBE|RUNTIME_CHILD) session=([0-9]+) child=([1-9][0-9]*) slot=(FD4|FD5|FD8) child_pidfd_serial=([1-9][0-9]*) guardian_pidfd_serial=([1-9][0-9]*)",enter)
        if match is None or self.quiesced or match.group(7)!="1" or self.audit_validator is None or int(match.group(1))!=self.last_audit_epoch+1: fail("D-M2 ENTER")
        self.audit_validator(match.group(2),int(match.group(3)),int(match.group(4)),int(match.group(5)[2:]),int(match.group(6)))
        self.last_audit_epoch=int(match.group(1))
        self.quiesced=True; self.fd_generation+=1
        prefix=f"audit_epoch={match.group(1)} kind={match.group(2)} session={match.group(3)} child={match.group(4)} slot={match.group(5)}"
        generation=self.fd_generation
        self.send(f"FD_AUDIT_QUIESCE_ACK {prefix} g_fd_generation={generation}",match.group(1))
        exit_record=self.control.receive(match.group(1))
        wanted=re.fullmatch(rf"FD_AUDIT_QUIESCE_EXIT {re.escape(prefix)} g_fd_generation={generation} outcome=(PASS|ABORT) transcript=([0-9a-f]{{64}})",exit_record)
        if wanted is None: fail("D-M2 EXIT")
        self.send(exit_record.replace("FD_AUDIT_QUIESCE_EXIT ","FD_AUDIT_QUIESCE_EXIT_ACK ",1),match.group(1))
        if wanted.group(1)!="PASS":
            self.admission_closed=True
            fail("D-M2 abort containment")
        self.quiesced=False

    def allocated(self) -> None:
        if self.quiesced or self.admission_closed: fail("allocation after closed admission")
        self.fd_generation+=1


class GuardianObjectLedger:
    def __init__(self, channel: GuardianChannel) -> None:
        self.channel=channel; self.next_handle=1; self.live: dict[int,ObjectIdentity]={}; self.capabilities: dict[int,int]={}; self.released: set[int]=set(); self.pending_released: dict[int,ObjectIdentity]={}

    def register(self, session: int, kind: str, fd: int) -> int:
        if kind not in OBJECT_KINDS: fail("object kind")
        st=os.fstat(fd); handle=self.next_handle; self.next_handle+=1
        identity=ObjectIdentity(handle,session,kind,st.st_dev,st.st_ino); self.live[handle]=identity; self.capabilities[handle]=fd
        record=f"OBJECT_REGISTERED session={session} handle={handle} kind={kind} dev={st.st_dev} ino={st.st_ino}"
        self.channel.send(record,str(handle))
        expected=record.replace("OBJECT_REGISTERED ","OBJECT_REGISTERED_ACK ",1)
        if self.channel.receive(lambda value:value==expected,str(handle))!=expected: fail("object ACK")
        return handle

    def release(self, handle: int, fd: int) -> None:
        identity=self.validate(handle,fd)
        self.release_closed(handle,(identity.dev,identity.ino))

    def validate(self, handle: int, fd: int) -> ObjectIdentity:
        identity=self.live.get(handle)
        if identity is None or handle in self.released: fail("object release state")
        st=os.fstat(fd)
        if (st.st_dev,st.st_ino)!=(identity.dev,identity.ino): fail("object replacement")
        return identity

    def release_closed(self, handle: int, observed: tuple[int,int]) -> None:
        identity=self.live.pop(handle,None)
        if identity is None or handle in self.released or observed!=(identity.dev,identity.ino): fail("closed object release state")
        self.capabilities.pop(handle,None)
        self.channel.send(f"OBJECT_RELEASED session={identity.session} handle={handle} kind={identity.kind} dev={identity.dev} ino={identity.ino}",str(handle))
        self.released.add(handle); self.pending_released[handle]=identity

    def retire_session(self, session: int) -> None:
        for handle,identity in tuple(self.pending_released.items()):
            if identity.session==session: self.pending_released.pop(handle)


class OwnedTree:
    """G-only retained-dirfd tree.  Cleanup consumes an identity ledger, never a prefix."""
    def __init__(self, parent_fd: int, basename: str, mode: int=0o700) -> None:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+",basename): fail("owned root basename")
        os.mkdir(basename,mode,dir_fd=parent_fd)
        self.parent_fd=parent_fd; self.basename=basename
        self.root_fd=os.open(basename,OPEN_DIR,dir_fd=parent_fd)
        self.owned_basename=basename; self.foreign_basename=""; self.foreign_identity: tuple[int,int]|None=None
        self.foreign_member_identity: tuple[int,int,int,int,int,bytes]|None=None
        self.foreign_fd=-1; self.foreign_parent_fd=-1; self.foreign_parent_relative=""; self.foreign_fixed=""; self.foreign_internal=""
        self.foreign_actor_parent=""; self.foreign_exchanged=False; self.foreign_audited=False
        self.directories: dict[str,int]={".":self.root_fd}; self.files: dict[str,tuple[int,int]]={}; self.members_cleaned=False; self.cleaned=False

    def prepare_foreign_child(self, relative: str, coordinate: str, actor_parent: str) -> tuple[str,str,str,tuple[int,int],tuple[int,int]]:
        """G creates/retains the controlled fixture; it never performs the exchange."""
        if relative in ("",".","..") or relative.startswith("/") or self.foreign_identity is not None or self.cleaned: fail("foreign preparation state")
        parent_relative,fixed=relative.rsplit("/",1) if "/" in relative else (".",relative)
        parent_fd=self.directory(parent_relative); owned_fd=self.directory(relative)
        internal=".owner."+sha256((self.basename+":"+relative+":"+coordinate).encode("utf-8"))[:20]
        if "/" in fixed or "/" in internal: fail("foreign basename")
        os.mkdir(internal,0o700,dir_fd=parent_fd)
        foreign_fd=os.open(internal,OPEN_DIR,dir_fd=parent_fd)
        try:
            foreign=os.fstat(foreign_fd); owned=os.fstat(owned_fd)
            if not stat.S_ISDIR(foreign.st_mode) or stat.S_IMODE(foreign.st_mode)!=0o700 or foreign.st_uid!=0: fail("foreign directory metadata")
            self.foreign_identity=(foreign.st_dev,foreign.st_ino)
            self.foreign_fd=foreign_fd; foreign_fd=-1; self.foreign_parent_fd=parent_fd; self.foreign_parent_relative=parent_relative
            self.foreign_fixed=fixed; self.foreign_internal=internal; self.foreign_basename=(parent_relative+"/" if parent_relative!="." else "")+fixed
            self.foreign_actor_parent=actor_parent
            return actor_parent,fixed,internal,(owned.st_dev,owned.st_ino),(foreign.st_dev,foreign.st_ino)
        finally:
            if foreign_fd>=0: os.close(foreign_fd)

    def populate_foreign_member(self, payload: bytes=b"P15R-FOREIGN-ROOT-v1\n") -> int:
        if self.foreign_fd<0 or self.foreign_member_identity is not None or payload not in (b"P15R-FOREIGN-ROOT-v1\n",b"P15R-FOREIGN-LOCK-v1\n"): fail("foreign member creation state")
        fd=os.open("foreign",os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW|os.O_CLOEXEC,0o600,dir_fd=self.foreign_fd)
        complete_write(fd,payload); os.fsync(fd); os.lseek(fd,0,os.SEEK_SET); member=os.fstat(fd)
        if not stat.S_ISREG(member.st_mode) or stat.S_IMODE(member.st_mode)!=0o600 or member.st_nlink!=1 or member.st_uid!=0: fail("foreign member metadata")
        self.foreign_member_identity=(member.st_dev,member.st_ino,stat.S_IMODE(member.st_mode),member.st_uid,member.st_nlink,payload)
        return fd

    def confirm_foreign_exchange(self, actor_stdout: bytes) -> None:
        if self.foreign_identity is None or self.foreign_exchanged or self.foreign_parent_fd<0: fail("foreign exchange state")
        owned_fd=self.directory((self.foreign_parent_relative+"/" if self.foreign_parent_relative!="." else "")+self.foreign_fixed)
        owned=os.fstat(owned_fd); foreign=os.fstat(self.foreign_fd)
        expected=(f"EXCHANGED fixed_dev={foreign.st_dev} fixed_ino={foreign.st_ino} internal_dev={owned.st_dev} internal_ino={owned.st_ino}\n").encode("ascii")
        if actor_stdout!=expected: fail("replacement actor receipt")
        fixed=os.stat(self.foreign_fixed,dir_fd=self.foreign_parent_fd,follow_symlinks=False)
        internal=os.stat(self.foreign_internal,dir_fd=self.foreign_parent_fd,follow_symlinks=False)
        if (fixed.st_dev,fixed.st_ino)!=(foreign.st_dev,foreign.st_ino) or (internal.st_dev,internal.st_ino)!=(owned.st_dev,owned.st_ino): fail("replacement exchange evidence")
        old=(self.foreign_parent_relative+"/" if self.foreign_parent_relative!="." else "")+self.foreign_fixed
        new=(self.foreign_parent_relative+"/" if self.foreign_parent_relative!="." else "")+self.foreign_internal
        self.directories={new+key[len(old):] if key==old or key.startswith(old+"/") else key:fd for key,fd in self.directories.items()}
        self.files={new+key[len(old):] if key==old or key.startswith(old+"/") else key:value for key,value in self.files.items()}
        self.foreign_exchanged=True

    def audit_foreign(self) -> str:
        if self.foreign_identity is None: return "OWNED_REMOVED"
        if not self.foreign_exchanged or self.foreign_audited or self.foreign_fd<0: fail("foreign audit state")
        directory=os.fstat(self.foreign_fd); fixed=os.stat(self.foreign_fixed,dir_fd=self.foreign_parent_fd,follow_symlinks=False)
        if (directory.st_dev,directory.st_ino)!=self.foreign_identity or (fixed.st_dev,fixed.st_ino)!=self.foreign_identity: fail("foreign directory drift")
        member_fd=os.open("foreign",OPEN_REGULAR,dir_fd=self.foreign_fd)
        try:
            member=os.fstat(member_fd); expected=self.foreign_member_identity
            actual=(member.st_dev,member.st_ino,stat.S_IMODE(member.st_mode),member.st_uid,member.st_nlink,read_all(member_fd))
            if expected is None or actual!=expected: fail("foreign member drift")
        finally: os.close(member_fd)
        self.foreign_audited=True
        return "FOREIGN_RETAINED"

    def teardown_foreign_fixture(self) -> None:
        if self.foreign_identity is None: return
        if not self.foreign_audited or self.foreign_fd<0: fail("foreign teardown before audit")
        os.unlink("foreign",dir_fd=self.foreign_fd)
        if os.listdir(self.foreign_fd): fail("foreign fixture member residue")
        fixed=os.stat(self.foreign_fixed,dir_fd=self.foreign_parent_fd,follow_symlinks=False)
        if (fixed.st_dev,fixed.st_ino)!=self.foreign_identity: fail("foreign fixture replacement")
        os.rmdir(self.foreign_fixed,dir_fd=self.foreign_parent_fd)
        try: os.stat(self.foreign_fixed,dir_fd=self.foreign_parent_fd,follow_symlinks=False)
        except FileNotFoundError: pass
        else: fail("foreign fixture teardown")
        close_proved(self.foreign_fd); self.foreign_fd=-1

    def cancel_unexchanged_foreign_fixture(self) -> None:
        if self.foreign_identity is None: return
        if self.foreign_exchanged or self.foreign_audited or self.foreign_fd<0: fail("foreign cancellation state")
        if self.foreign_member_identity is not None:
            member=os.stat("foreign",dir_fd=self.foreign_fd,follow_symlinks=False)
            if (member.st_dev,member.st_ino)!=self.foreign_member_identity[:2]: fail("foreign cancellation member")
            os.unlink("foreign",dir_fd=self.foreign_fd)
        if os.listdir(self.foreign_fd): fail("foreign cancellation residue")
        internal=os.stat(self.foreign_internal,dir_fd=self.foreign_parent_fd,follow_symlinks=False)
        if (internal.st_dev,internal.st_ino)!=self.foreign_identity: fail("foreign cancellation identity")
        close_proved(self.foreign_fd); self.foreign_fd=-1
        os.rmdir(self.foreign_internal,dir_fd=self.foreign_parent_fd)
        self.foreign_identity=None; self.foreign_member_identity=None; self.foreign_internal=""; self.foreign_fixed=""; self.foreign_basename=""

    def directory(self, relative: str) -> int:
        if relative in ("","."): return self.root_fd
        if relative in self.directories: return self.directories[relative]
        parent,name=relative.rsplit("/",1) if "/" in relative else (".",relative)
        parent_fd=self.directory(parent)
        try: os.mkdir(name,0o700,dir_fd=parent_fd)
        except FileExistsError: pass
        fd=os.open(name,OPEN_DIR,dir_fd=parent_fd)
        self.directories[relative]=fd
        return fd

    def write(self, relative: str, data: bytes, mode: int=0o600) -> int:
        parent,name=relative.rsplit("/",1) if "/" in relative else (".",relative)
        parent_fd=self.directory(parent)
        fd=os.open(name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW|os.O_CLOEXEC,mode,dir_fd=parent_fd)
        try:
            complete_write(fd,data); os.fsync(fd); st=os.fstat(fd)
            self.files[relative]=(st.st_dev,st.st_ino)
            return st.st_ino
        finally: os.close(fd)

    def replace(self, relative: str, data: bytes) -> None:
        parent,name=relative.rsplit("/",1) if "/" in relative else (".",relative); parent_fd=self.directory(parent)
        temporary=".owner."+sha256(relative.encode("utf-8"))[:16]
        fd=os.open(temporary,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW|os.O_CLOEXEC,0o600,dir_fd=parent_fd)
        try: complete_write(fd,data); os.fsync(fd)
        finally: os.close(fd)
        if relative in self.files:
            renameat2(parent_fd,temporary,parent_fd,name,RENAME_EXCHANGE)
            old_fd=os.open(temporary,OPEN_REGULAR,dir_fd=parent_fd)
            try:
                old=os.fstat(old_fd)
                if (old.st_dev,old.st_ino)!=self.files[relative]: fail("owned displaced identity")
            finally: os.close(old_fd)
            os.unlink(temporary,dir_fd=parent_fd)
        else:
            renameat2(parent_fd,temporary,parent_fd,name,RENAME_NOREPLACE)
        new_fd=os.open(name,OPEN_REGULAR,dir_fd=parent_fd)
        try:
            st=os.fstat(new_fd); self.files[relative]=(st.st_dev,st.st_ino)
        finally: os.close(new_fd)

    def unlink_owned(self, relative: str) -> None:
        identity=self.files.pop(relative,None)
        if identity is None: fail("unregistered unlink")
        parent,name=relative.rsplit("/",1) if "/" in relative else (".",relative); parent_fd=self.directory(parent)
        st=os.stat(name,dir_fd=parent_fd,follow_symlinks=False)
        if (st.st_dev,st.st_ino)!=identity or stat.S_ISDIR(st.st_mode): fail("foreign replacement preserved")
        os.unlink(name,dir_fd=parent_fd)

    def adopt(self, relative: str) -> None:
        if relative in self.files: fail("duplicate adoption")
        parent,name=relative.rsplit("/",1) if "/" in relative else (".",relative); parent_fd=self.directory(parent)
        st=os.stat(name,dir_fd=parent_fd,follow_symlinks=False)
        if stat.S_ISDIR(st.st_mode): fail("member adoption type")
        self.files[relative]=(st.st_dev,st.st_ino)

    def cleanup_members(self) -> None:
        if self.cleaned or self.members_cleaned: fail("duplicate member cleanup")
        for relative in sorted(tuple(self.files),key=lambda value:(value.count("/"),value.encode("utf-8")),reverse=True): self.unlink_owned(relative)
        self.members_cleaned=True

    def cleanup_directories(self) -> None:
        if self.cleaned or not self.members_cleaned or self.files: fail("directory cleanup state")
        for relative in sorted((value for value in self.directories if value!="."),key=lambda value:(value.count("/"),value.encode("utf-8")),reverse=True):
            fd=self.directories.pop(relative)
            if os.listdir(fd): fail("foreign entry retained")
            os.close(fd); parent,name=relative.rsplit("/",1) if "/" in relative else (".",relative)
            os.rmdir(name,dir_fd=self.directories[parent])
        if self.foreign_identity is not None:
            self.audit_foreign()
            self.teardown_foreign_fixture()
        if os.listdir(self.root_fd): fail("owned root not empty")
        os.close(self.root_fd); os.rmdir(self.owned_basename,dir_fd=self.parent_fd)
        self.cleaned=True

    def cleanup(self) -> None:
        self.cleanup_members(); self.cleanup_directories()


def copy_bound_source(tree: OwnedTree, destination: str, source_fd: int, relative: str) -> None:
    tree.write(destination,read_regular_at(source_fd,relative))


def populate_synthetic_repository(tree: OwnedTree, repository_fd: int, package_fd: int) -> str:
    package_prefix="repository/papers/15-wieferich-ulm-packet-bases/"
    for relative in AUTHORITY_PATHS:
        copy_bound_source(tree,"repository/"+relative,repository_fd,relative)
    package_sources=tuple(dict.fromkeys(IMPLEMENTATION_PATHS+LIFECYCLE_PATHS+("notes/phase2_control_design_lock.md","notes/phase2_control_design_peer_review.md","notes/phase2_control_implementation_gate.md")))
    for relative in package_sources:
        copy_bound_source(tree,package_prefix+relative,package_fd,relative)
    tree.directory(package_prefix+"results")
    return "/tmp/"+tree.basename+"/"+package_prefix.rstrip("/")


def private_mount_setup() -> int:
    mount(None,"/",None,MS_PRIVATE|MS_REC)
    mount("tmpfs","/tmp","tmpfs",MS_NODEV|MS_NOSUID,"mode=0700,size=268435456,nr_inodes=32768")
    try: umount("/proc")
    except OSError: pass
    mount("proc","/proc","proc",MS_NODEV|MS_NOSUID|MS_NOEXEC,"hidepid=0")
    return os.open("/tmp",OPEN_DIR)


def hide_cgroup_mounts() -> None:
    root=os.open("/proc/self",OPEN_PATH_DIR)
    try: rows=read_regular_at(root,"mountinfo",4*1024*1024).decode("utf-8").splitlines()
    finally: os.close(root)
    targets=[]
    for row in rows:
        fields=row.split(" "); separator=fields.index("-")
        if fields[separator+1] in ("cgroup","cgroup2"): targets.append(fields[4].replace("\\040"," "))
    for target in sorted(set(targets),key=lambda value:value.count("/"),reverse=True): umount(target)


@dataclass(frozen=True)
class WorkerSpec:
    session: int
    child: int
    role: str
    owner: str
    method: str
    purpose: str
    admission: str
    fdset: str
    source_relative: str|None
    cwd: str
    argv: tuple[str,...]
    environment: tuple[tuple[str,str],...]
    root_fd: int|None=None
    request: int=0
    audit: int=0
    serial: int=0
    nonce: str=""
    digest: str=""
    trigger: str="NONE"
    expected_status: int=0
    requester_child: int=0
    target: str=""
    phase: str="METHOD"
    request_audit: int=0


@dataclass
class WorkerRecord:
    spec: WorkerSpec
    pid: int
    pidfd: int
    stdout_fd: int
    stderr_fd: int
    rpc_peer: socket.socket|None
    audit_transit: int|None
    admission_peer: socket.socket
    proc_fd: int
    start_time: int
    nspid: tuple[int,...]
    cgroup: str
    uid: int
    gid: int
    state: str="REGISTERED"
    stdout: bytearray=field(default_factory=bytearray)
    stderr: bytearray=field(default_factory=bytearray)
    status: int=-1
    process_gone: bool=False
    proc_closed: bool=False
    descriptor_empty: bool=False
    streams_nonblocking: bool=False
    stdout_eof: bool=False
    stderr_eof: bool=False
    audit_barrier: str="NONE"
    audit_expected: tuple[int,...]=()
    p_pidfd_serial: int=0


def extract_embedded_python(source: bytes) -> bytes:
    begin=b"<<'P15R_POSSESSION_PY_V2_END'\n"
    index=source.find(begin)
    if index<0: fail("wrapper byte bound")
    start=index+len(begin); end=source.find(b"\nP15R_POSSESSION_PY_V2_END\n",start)
    if end<0 or source.find(begin,start)>=0: fail("wrapper byte bound")
    return source[start:end]+b"\n"


def fd8_receive_exact(endpoint: socket.socket, expected: bytes) -> None:
    packet,ancillary,flags,address=endpoint.recvmsg(len(expected)+1,1)
    if packet!=expected or ancillary or flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or address not in (None,"",b""): fail("FD8 closed codec")


def fd8_require_empty(endpoint: socket.socket) -> None:
    try: endpoint.recvmsg(1,1,socket.MSG_DONTWAIT)
    except BlockingIOError: return
    fail("FD8 extra datagram")


def worker_entry(spec: WorkerSpec, workers_capability: int, cwd_capability: int, mappings: Mapping[int,int], stage_ready_fd: int, transit_release_fd: int) -> int:
    try:
        target=spec.target or spec.role
        close_proved(workers_capability)
        os.fchdir(cwd_capability); close_proved(cwd_capability)
        install_fd_map(mappings)
        for source in sorted(set(mappings.values()),reverse=True):
            if source not in mappings and fd_is_open(source): close_proved(source)
        complete_write(stage_ready_fd,b"STAGED"); close_proved(stage_ready_fd)
        if read_all(transit_release_fd)!=b"RELEASE": return 125
        close_proved(transit_release_fd)
        allowed=FDSETS[spec.fdset][0]
        close_except(allowed)
        if target=="CGROUP_PROBE_CHILD": drop_capabilities(no_new_privileges=True)
        install_worker_security()
        barrier=socket.socket(fileno=8)
        if barrier.send(b"SANITIZED")!=9: return 125
        fd8_receive_exact(barrier,b"ADMIT")
        source=b""
        if 3 in allowed:
            st=os.fstat(3)
            if not stat.S_ISREG(st.st_mode) or st.st_nlink!=1: return 125
            source=read_all(3); close_proved(3)
        if barrier.send(b"SOURCE_READY")!=12: return 125
        fd8_receive_exact(barrier,b"START"); fd8_require_empty(barrier)
        barrier.close(); immediate_ebadf(8)
        if frozenset(fd for fd in range(0,10) if fd_is_open(fd)) != FDSETS[spec.fdset][2]: return 125
        os.environ.clear()
        for name,value in spec.environment: os.environ[name]=value
        os.environ.update({"LC_ALL":"C","TZ":"UTC","PYTHONHASHSEED":"0","PYTHONDONTWRITEBYTECODE":"1","P15R_WORKER_ROLE":target})
        sys.argv=list(spec.argv)
        if target=="CGROUP_PROBE_CHILD":
            if spec.purpose=="BOOTSTRAP_FREEZE_THAW_E1":
                if signal.sigwait((signal.SIGUSR1,))!=signal.SIGUSR1: return 125
                return 0
            signal.pause(); return 125
        if target=="REPLACEMENT_ACTOR": return replacement_actor_worker()
        if target=="LOCK_HOLDER": return lock_holder_worker()
        if target=="LOCK_CONTENDER": return lock_contender_worker()
        executable=extract_embedded_python(source) if target=="COPIED_REPRODUCE" else source
        module_mode=target in ("GENERATE_CANONICAL_A","GENERATE_CANONICAL_B")
        namespace={"__name__":"p15r_fd3_subject" if module_mode else "__main__","__file__":"<p15r-fd3>","__package__":None,"__cached__":None,"P15R_AUDIT_HANDLE":spec.request_audit,"P15R_AUTH_SERIAL":0}
        code=compile(executable,"<p15r-fd3>","exec",dont_inherit=True,optimize=0)
        exec(code,namespace,namespace)
        if module_mode:
            if namespace["main"](list(spec.argv[1:]))!=0: return 1
            verify_arguments=["--verify-only","--input-dir",spec.argv[-1]]
            if namespace["main"](verify_arguments)!=0: return 1
        return 0
    except SystemExit as exit_value:
        return int(exit_value.code or 0) if isinstance(exit_value.code,(int,type(None))) else 1
    except BaseException:
        return 125


class GuardianWorkers:
    def __init__(self, channel: GuardianChannel, workers_fd: int, repository_fd: int, package_fd: int, actual_endpoint_fd: int) -> None:
        self.channel=channel; self.workers_fd=workers_fd; self.repository_fd=repository_fd; self.package_fd=package_fd
        self.proc_root=os.open("/proc",OPEN_DIR)
        if actual_endpoint_fd<0 or fcntl.fcntl(actual_endpoint_fd,fcntl.F_GETFD)!=FD_CLOEXEC or not stat.S_ISSOCK(os.fstat(actual_endpoint_fd).st_mode): fail("actual EP_G clone stub authority")
        self.next_child=1; self.live: dict[int,WorkerRecord]={}; self.completed: dict[int,WorkerRecord]={}; self.actual_endpoint_fd=actual_endpoint_fd; self.seal_fence: V14SealFence|None=None; self.frozen_reference_children: tuple[int,...]=(); self.last_p_pidfd_serial=1
        self.channel.audit_validator=self.validate_d_m2_barrier; self.channel.freeze_audit_begin=self.begin_frozen_references; self.channel.freeze_audit_end=self.finish_frozen_references

    def authorize_post_seal_clones(self, fence: V14SealFence, actual_endpoint_fd: int) -> None:
        fence.validate()
        if self.seal_fence is not None or actual_endpoint_fd<0 or actual_endpoint_fd!=self.actual_endpoint_fd: fail("post-Seal clone authority")
        endpoint=os.fstat(actual_endpoint_fd)
        if (endpoint.st_dev,endpoint.st_ino)!=(fence.seal_receipt.endpoint_dev,fence.seal_receipt.endpoint_ino): fail("post-Seal endpoint identity")
        self.seal_fence=fence

    @staticmethod
    def _ordered_live_slots(record: WorkerRecord, phase: int) -> tuple[int,...]:
        if phase not in (0,1,2): fail("D-M2 phase")
        slots=tuple(slot for slot in (8,4,5) if slot in FDSETS[record.spec.fdset][phase])
        if phase==2:
            if (record.spec.target or record.spec.role) not in ("TOP_TEST_CONTROLS","COPIED_REPRODUCE"): return ()
            slots=tuple(slot for slot in slots if slot in (4,5))
        return slots

    def _arm_audit(self, record: WorkerRecord, phase: int, barrier: str) -> None:
        if record.audit_barrier!="NONE" or record.audit_expected: fail("D-M2 barrier overlap")
        slots=self._ordered_live_slots(record,phase)
        if not slots: fail("D-M2 empty barrier")
        record.audit_barrier=barrier; record.audit_expected=slots

    @staticmethod
    def _finish_audit(record: WorkerRecord, barrier: str) -> None:
        if record.audit_barrier!=barrier or record.audit_expected: fail("D-M2 incomplete barrier")
        record.audit_barrier="NONE"

    def validate_d_m2_barrier(self, kind: str, session: int, child: int, slot: int, child_pidfd_serial: int) -> None:
        record=self.live.get(child); expected_kind="PREFLIGHT_PROBE" if child==1 else "RUNTIME_CHILD"
        if record is None or record.state not in ("REGISTERED","SOURCE_READY","RUNNING") or record.spec.session!=session or kind!=expected_kind or not record.audit_expected or record.audit_expected[0]!=slot: fail("D-M2 G barrier tuple")
        if record.p_pidfd_serial==0:
            if child_pidfd_serial<=self.last_p_pidfd_serial: fail("D-M2 child pidfd serial order")
            record.p_pidfd_serial=child_pidfd_serial; self.last_p_pidfd_serial=child_pidfd_serial
        elif child_pidfd_serial!=record.p_pidfd_serial: fail("D-M2 child pidfd serial drift")
        if kind=="PREFLIGHT_PROBE" and (child,session,slot)!=(1,0,8): fail("D-M2 preflight row")
        if kind=="RUNTIME_CHILD" and child==1: fail("D-M2 runtime kind")
        if record.state=="REGISTERED" and record.audit_barrier!="REGISTERED_PRE_START": fail("D-M2 registered barrier")
        if record.state=="SOURCE_READY" and record.audit_barrier!="SOURCE_READY_PRE_START": fail("D-M2 source barrier")
        if record.state=="RUNNING" and record.audit_barrier not in ("RPC_RUNNING_REFERENCE","FROZEN_RUNNING_REFERENCE"): fail("D-M2 running barrier")
        record.audit_expected=record.audit_expected[1:]

    def begin_running_reference(self, record: WorkerRecord) -> None:
        if record.state!="RUNNING": fail("D-M2 running reference state")
        self._arm_audit(record,2,"RPC_RUNNING_REFERENCE")

    def finish_running_reference(self, record: WorkerRecord) -> None:
        self._finish_audit(record,"RPC_RUNNING_REFERENCE")

    def begin_frozen_references(self) -> None:
        if self.frozen_reference_children: fail("D-M2 frozen barrier overlap")
        selected=[]
        for child,record in sorted(self.live.items()):
            if record.state=="RUNNING" and self._ordered_live_slots(record,2):
                self._arm_audit(record,2,"FROZEN_RUNNING_REFERENCE"); selected.append(child)
        self.frozen_reference_children=tuple(selected)

    def finish_frozen_references(self) -> None:
        for child in self.frozen_reference_children:
            record=self.live.get(child)
            if record is None: fail("D-M2 frozen child lifetime")
            self._finish_audit(record,"FROZEN_RUNNING_REFERENCE")
        self.frozen_reference_children=()

    def _source(self, relative: str) -> int:
        return openat2(self.package_fd,relative,OPEN_REGULAR)

    @staticmethod
    def configure_streams(record: WorkerRecord) -> None:
        if record.streams_nonblocking: return
        if record.stdout_eof or record.stderr_eof or record.stdout_fd<0 or record.stderr_fd<0 or record.stdout_fd==record.stderr_fd: fail("worker stream setup state")
        for fd in (record.stdout_fd,record.stderr_fd):
            flags=fcntl.fcntl(fd,fcntl.F_GETFL)
            fcntl.fcntl(fd,fcntl.F_SETFL,flags|os.O_NONBLOCK)
        record.streams_nonblocking=True

    @staticmethod
    def stream_fds(record: WorkerRecord) -> tuple[int,...]:
        return tuple(fd for fd in (record.stdout_fd,record.stderr_fd) if fd>=0)

    @staticmethod
    def drain_stream_event(record: WorkerRecord, poller: select.poll, fd: int, event: int) -> None:
        if fd==record.stdout_fd:
            field_name="stdout_fd"; eof_name="stdout_eof"; sink=record.stdout
        elif fd==record.stderr_fd:
            field_name="stderr_fd"; eof_name="stderr_eof"; sink=record.stderr
        else: fail("worker stream unknown fd")
        if getattr(record,eof_name) or event&select.POLLNVAL or not event&(select.POLLIN|select.POLLHUP|select.POLLERR): fail("worker stream poll event")
        try: chunk=os.read(fd,65536)
        except BlockingIOError:
            if event&(select.POLLHUP|select.POLLERR): fail("worker stream HUP without tail")
            return
        if chunk:
            if len(sink)+len(chunk)>WORKER_STREAM_BYTE_CEILING: fail("worker stream byte ceiling")
            sink.extend(chunk)
            return
        if getattr(record,eof_name): fail("duplicate worker stream EOF")
        close_proved(fd); setattr(record,field_name,-1); setattr(record,eof_name,True)
        poller.unregister(fd); fd=-1

    def _drain_until_exit_ready(self, record: WorkerRecord) -> None:
        self.configure_streams(record)
        poller=select.poll(); poller.register(record.pidfd,select.POLLIN|select.POLLHUP|select.POLLERR)
        for fd in self.stream_fds(record): poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
        pidfd_ready=False
        while not pidfd_ready or self.stream_fds(record):
            try: events=poller.poll()
            except InterruptedError: fail("worker drain poll EINTR")
            if not events: fail("worker drain empty poll")
            for fd,event in sorted(events,key=lambda item:item[0]==record.pidfd):
                if fd==record.pidfd:
                    if pidfd_ready or event&select.POLLNVAL or event&select.POLLERR or not event&(select.POLLIN|select.POLLHUP): fail("worker pidfd readiness")
                    pidfd_ready=True; poller.unregister(fd)
                elif fd in self.stream_fds(record):
                    self.drain_stream_event(record,poller,fd,event)
                else: fail("worker drain unknown fd")

    def _collect(self, record: WorkerRecord, auth_state: object|None=None) -> int:
        def auth_failure(cause: str, material: str="") -> None:
            if auth_state is not None: getattr(auth_state,"post_finalize_failure")(cause,material)
        identity_failed=False
        try:
            identity=worker_proc_identity(record.proc_fd,record.pid,1,record.pid,0,0)
            if identity!=(record.start_time,record.nspid,record.cgroup,record.uid,record.gid): fail("requester proc identity drift")
        except (PossessionFailure,OSError,ValueError,UnicodeError):
            auth_failure("REQUESTER_IDENTITY"); identity_failed=True
        try:
            self._drain_until_exit_ready(record)
            status=exact_wait_pidfd(record.pidfd,record.pid)
        except (PossessionFailure,OSError,ChildProcessError): auth_failure("REQUESTER_WAITID"); raise
        record.status=status
        try: os.stat(str(record.pid),dir_fd=self.proc_root,follow_symlinks=False)
        except FileNotFoundError: record.process_gone=True
        except OSError: auth_failure("REQUESTER_PROCESS_PRESENT"); raise
        else: auth_failure("REQUESTER_PROCESS_PRESENT"); fail("requester process remains")
        try:
            proc_fd=record.proc_fd; close_proved(proc_fd); record.proc_fd=-1; record.proc_closed=True; proc_fd=-1
        except (PossessionFailure,OSError): auth_failure("REQUESTER_FDSET_NONEMPTY"); raise
        try:
            pidfd=record.pidfd; close_proved(pidfd); record.pidfd=-1; pidfd=-1
        except (PossessionFailure,OSError): auth_failure("PIDFD_ABSENCE"); raise
        if identity_failed: fail("requester identity tombstone")
        return status

    def spawn(self, spec: WorkerSpec, audit_fd: int|None=None, pre_admit: Callable[[],None]|None=None) -> WorkerRecord:
        target=spec.target or spec.role
        if spec.child!=self.next_child or target not in TARGETS|{"CGROUP_PROBE_CHILD"} or spec.fdset not in FDSETS: fail("worker registry")
        if self.seal_fence is None:
            if spec.child not in (1,2): fail("pre-Seal clone budget")
            row=PRE_SUITE_CHILDREN[spec.child-1]
            if (spec.session,target,spec.role,spec.owner,spec.purpose,spec.admission,spec.fdset,spec.phase)!=(row.session,"CGROUP_PROBE_CHILD",row.role,row.owner,row.purpose,row.admission,row.fdset,row.phase): fail("pre-Seal probe registry")
        else:
            self.seal_fence.validate()
            if spec.child<=2 or target=="CGROUP_PROBE_CHILD" or self.actual_endpoint_fd<0: fail("post-Seal clone registry")
        self.channel.allocated()
        self.next_child+=1
        stdin_read,stdin_write=os.pipe2(os.O_CLOEXEC); stdout_read,stdout_write=os.pipe2(os.O_CLOEXEC); stderr_read,stderr_write=os.pipe2(os.O_CLOEXEC)
        admission_child,admission_peer=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
        rpc_child=rpc_peer=None
        if spec.fdset=="STDIO_SOURCE_RPC_AUDIT_BARRIER":
            rpc_child,rpc_peer=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
            rpc_peer.setsockopt(socket.SOL_SOCKET,socket.SO_PASSCRED,1)
        source_fd=self._source(spec.source_relative) if spec.source_relative is not None else None
        stage_read,stage_write=os.pipe2(os.O_CLOEXEC); release_read,release_write=os.pipe2(os.O_CLOEXEC)
        mappings={0:stdin_read,1:stdout_write,2:stderr_write,8:admission_child.fileno()}
        if source_fd is not None: mappings[3]=source_fd
        if rpc_child is not None: mappings[4]=rpc_child.fileno()
        if audit_fd is not None: mappings[5]=audit_fd
        if spec.root_fd is not None: mappings[9]=os.dup(spec.root_fd)
        if spec.cwd=="@PACKAGE_FD11": cwd_fd=os.dup(self.package_fd)
        elif spec.cwd=="/tmp" or spec.cwd.startswith("/tmp/"): cwd_fd=os.open(spec.cwd,OPEN_DIR)
        else: fail("worker cwd registry")
        cwd=os.fstat(cwd_fd)
        def child() -> int:
            if self.actual_endpoint_fd>=0:
                os.close(self.actual_endpoint_fd)
                immediate_ebadf(self.actual_endpoint_fd)
            close_proved(stage_read); close_proved(release_write)
            return worker_entry(spec,self.workers_fd,cwd_fd,mappings,stage_write,release_read)
        pid,pidfd=clone3(child,cgroup_fd=self.workers_fd)
        close_proved(stage_write); close_proved(release_read)
        for fd in (stdin_read,stdout_write,stderr_write,stdin_write): close_proved(fd)
        admission_child_fd=admission_child.fileno(); admission_child.close(); immediate_ebadf(admission_child_fd)
        if rpc_child is not None:
            rpc_child_fd=rpc_child.fileno(); rpc_child.close(); immediate_ebadf(rpc_child_fd)
        if source_fd is not None: close_proved(source_fd)
        if spec.root_fd is not None: close_proved(mappings[9])
        if audit_fd is not None: close_proved(audit_fd)
        if read_all(stage_read)!=b"STAGED": fail("child staging barrier")
        close_proved(stage_read)
        complete_write(release_write,b"RELEASE"); close_proved(release_write)
        close_proved(cwd_fd); cwd_fd=-1
        process_fd=openat2(self.proc_root,str(pid),OPEN_PATH_DIR); start_time,nspid,cgroup,uid,gid=worker_proc_identity(process_fd,pid,1,pid,0,0)
        record=WorkerRecord(spec,pid,pidfd,stdout_read,stderr_read,rpc_peer,None,admission_peer,process_fd,start_time,nspid,cgroup,uid,gid)
        self.live[spec.child]=record
        fd8_receive_exact(admission_peer,b"SANITIZED")
        self._arm_audit(record,0,"REGISTERED_PRE_START")
        base=f"CHILD_REGISTERED session={spec.session} child={spec.child} inner_pid={pid} role={spec.role} owner={spec.owner} purpose={spec.purpose} admission={spec.admission} fdset={spec.fdset} cwd_dev={cwd.st_dev} cwd_ino={cwd.st_ino}"
        if spec.request:
            if spec.requester_child<=0: fail("audited requester child")
            base+=f" target={target} trigger={spec.trigger} request={spec.request} requester_child={spec.requester_child} audit={spec.audit} serial={spec.serial} nonce={spec.nonce} digest={spec.digest}"
            base=base.replace("CHILD_REGISTERED ","CHILD_REGISTERED_AUDITED ",1)
        self.channel.send(base,str(spec.child))
        if pre_admit is not None: pre_admit()
        wanted=f"CHILD_ADMITTED session={spec.session} child={spec.child} admission={spec.admission}"
        if self.channel.receive(lambda value:value==wanted,str(spec.child))!=wanted: fail("CHILD_ADMITTED")
        self._finish_audit(record,"REGISTERED_PRE_START")
        if admission_peer.send(b"ADMIT")!=5: fail("ADMIT send")
        fd8_receive_exact(admission_peer,b"SOURCE_READY"); fd8_require_empty(admission_peer)
        record.state="SOURCE_READY"; self._arm_audit(record,1,"SOURCE_READY_PRE_START")
        self.channel.send(f"SOURCE_READY session={spec.session} child={spec.child} admission={spec.admission} fdset={spec.fdset}",str(spec.child))
        start=f"START session={spec.session} child={spec.child} admission={spec.admission}"
        if self.channel.receive(lambda value:value==start,str(spec.child))!=start: fail("START")
        self._finish_audit(record,"SOURCE_READY_PRE_START")
        if admission_peer.send(b"START")!=5: fail("START barrier")
        admission_fd=admission_peer.fileno(); admission_peer.close(); immediate_ebadf(admission_fd); record.state="RUNNING"
        return record

    def reap(self, record: WorkerRecord, auth_state: object|None=None) -> int:
        def auth_failure(cause: str, material: str="") -> None:
            if auth_state is not None:
                getattr(auth_state,"post_finalize_failure")(cause,material)
        if record.rpc_peer is not None:
            try: packet,ancillary,flags,_address=record.rpc_peer.recvmsg(MAX_FRAME+5,socket.CMSG_SPACE(struct.calcsize("3i")))
            except OSError: auth_failure("FD4_EXTRA_DATAGRAM"); raise
            if packet or ancillary or flags:
                auth_failure("FD4_EXTRA_DATAGRAM",packet.hex()); fail("FD4 drain anomaly")
            rpc_fd=record.rpc_peer.fileno()
            try: record.rpc_peer.close(); immediate_ebadf(rpc_fd); record.rpc_peer=None; rpc_fd=-1
            except (PossessionFailure,OSError): auth_failure("REQUESTER_FDSET_NONEMPTY"); raise
            if auth_state is not None: setattr(auth_state,"fd4_eof_observed",True)
        status=self._collect(record,auth_state)
        record.descriptor_empty=record.admission_peer.fileno()<0 and record.rpc_peer is None and record.audit_transit is None and record.proc_closed and record.process_gone and record.proc_fd==-1 and record.pidfd==-1 and record.stdout_fd==-1 and record.stderr_fd==-1 and record.stdout_eof and record.stderr_eof
        if not record.descriptor_empty: auth_failure("REQUESTER_FDSET_NONEMPTY"); fail("requester descriptor ledger")
        if auth_state is not None and status!=record.spec.expected_status:
            setattr(auth_state,"requester_status",status); auth_failure("REQUESTER_EXIT_STATUS",str(status)); fail("requester exit status")
        if auth_state is not None:
            if getattr(auth_state,"state","")!="FINALIZED_AWAITING_REAP" or not getattr(auth_state,"finalized_ack_complete",False) or not getattr(auth_state,"fd4_eof_observed",False):
                auth_failure("REQUESTER_IDENTITY"); fail("requester reap auth state")
            auth_state.requester_status=status; auth_state.state="REQUESTER_REAPED"
        record.state="REAPED"; self.completed[record.spec.child]=record; self.live.pop(record.spec.child)
        message=f"CHILD_REAPED session={record.spec.session} child={record.spec.child} status={status}"
        try: self.channel.send(message,str(record.spec.child))
        except (PossessionFailure,OSError): auth_failure("CHILD_REAPED_SEND",message); raise
        if auth_state is not None: auth_state.child_reaped_record=message; auth_state.state="CHILD_REAPED_SENT"
        expected=message.replace("CHILD_REAPED ","CHILD_REAPED_ACK ",1)
        try: acknowledged=self.channel.receive(lambda value:value==expected,str(record.spec.child))
        except (PossessionFailure,OSError): auth_failure("CHILD_REAPED_ACK_RECORD",expected); raise
        if acknowledged!=expected: auth_failure("CHILD_REAPED_ACK_RECORD",acknowledged); fail("CHILD_REAPED_ACK")
        if auth_state is not None:
            auth_state.child_reaped_ack=acknowledged; auth_state.state="CHILD_REAPED_ACKED"; auth_state.state="AUTH_REAP_RECONCILED"
        return status

    def contain_all(self) -> None:
        for child,record in sorted(tuple(self.live.items())):
            try:
                if record.rpc_peer is not None:
                    rpc_fd=record.rpc_peer.fileno(); record.rpc_peer.close(); immediate_ebadf(rpc_fd); record.rpc_peer=None; rpc_fd=-1
                admission_fd=record.admission_peer.fileno()
                if admission_fd>=0: record.admission_peer.close(); immediate_ebadf(admission_fd)
                admission_fd=-1
                record.status=self._collect(record)
                record.descriptor_empty=record.proc_closed and record.process_gone and record.proc_fd==-1 and record.pidfd==-1 and record.stdout_fd==-1 and record.stderr_fd==-1 and record.stdout_eof and record.stderr_eof and record.rpc_peer is None and record.admission_peer.fileno()<0 and record.audit_transit is None
                if not record.descriptor_empty: fail("contained worker descriptor ledger")
                record.state="CONTAINED_REAPED"; self.completed[child]=record; self.live.pop(child)
            except BaseException:
                record.state="CONTAINMENT_ERROR"
                raise


def parse_exact(record: str, token: str, fields: Sequence[tuple[str,str]]) -> dict[str,str]:
    pattern=[re.escape(token)]
    for name,grammar in fields: pattern.append(re.escape(name)+"=(?P<"+name+">"+grammar+")")
    match=re.fullmatch(" ".join(pattern),record)
    if match is None: fail("exact record "+token)
    return match.groupdict()


def send_bare(endpoint: socket.socket, record: str) -> None:
    payload=record.encode("ascii")
    if not payload or len(payload)>MAX_FRAME or b"\x00" in payload or b"\n" in payload or endpoint.send(payload)!=len(payload): fail("bare send")


def receive_bare_credential(endpoint: socket.socket, expected_pid: int) -> str|None:
    data,ancillary,flags,_address=endpoint.recvmsg(MAX_FRAME+1,socket.CMSG_SPACE(struct.calcsize("3i")))
    if not data:
        if ancillary or flags: fail("FD5 EOF ancillary")
        return None
    credentials=[value for value in ancillary if value[0]==socket.SOL_SOCKET and value[1]==socket.SCM_CREDENTIALS]
    if len(ancillary)!=1 or len(credentials)!=1 or len(credentials[0][2])!=struct.calcsize("3i") or flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC): fail("FD5 credential")
    pid,uid,gid=struct.unpack("3i",credentials[0][2])
    if pid!=expected_pid or uid!=65534 or gid!=65534: fail("FD5 peer identity")
    if len(data)>MAX_FRAME or b"\x00" in data or b"\n" in data or not data.isascii(): fail("FD5 bytes")
    return data.decode("ascii")


@dataclass
class PAuthPeer:
    child: int
    endpoint: socket.socket
    outer_pid: int=0
    expected_inner_pid: int=0
    audited_fd4_inode: int=0
    state: str="NEW"
    audit_id: int=0
    auth_serial: int=0
    spawn_serial: int=0
    auth: int=0
    session: int=0
    request: int=0
    registration_digest: str=""
    method: str=""
    trigger: str=""
    owner: str=""
    fd4_inode: int=0
    rpc_inner_pid: int=0
    create_identity: bytes=b""
    create_template: bytes=b""
    create_frame: bytes=b""
    create_commitment: str=""
    create_cap: str=""
    reply_nonce: str=""
    active_cap: str=""
    active_identity: bytes=b""
    active_cap_commitment: str=""
    created: bytes=b""
    created_digest: str=""
    activation_hold: str=""
    create_receipt_sent: bool=False
    terminal_cap: str=""
    terminal_cap_digest: str=""
    terminal_request: int=0
    terminal_outcome: str=""
    terminal_reply_digest: str=""
    terminal_template: bytes=b""
    terminal_frame: bytes=b""
    terminal_observation_consumed: bool=False
    audits: dict[tuple[int,int],tuple[str,str,str,bytes]]=field(default_factory=dict)
    confirmed_audits: set[tuple[int,int]]=field(default_factory=set)
    consumed_audits: set[tuple[int,int]]=field(default_factory=set)
    eof_seen: bool=False
    first_failure: str=""
    failure_state: str=""
    failure_record_sha256: str=""
    terminal_cause: str=""
    terminal_receipt: bytes=b""
    terminal_receipt_attempted: bool=False
    terminal_receipt_complete: bool=False
    finalized_ack_complete: bool=False


class PAuthentication:
    """P is the sole entropy and causal-capability owner."""
    def __init__(self, control: FramedControl, secrets: list[tuple[str,bytearray]]) -> None:
        self.control=control; self.secrets=secrets; self.next_audit=0; self.next_auth=1; self.next_session=1; self.peers: dict[int,PAuthPeer]={}

    def create_endpoint(self, child: int) -> tuple[int,int]:
        if child in self.peers: fail("duplicate FD5")
        p_side,g_transit=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
        p_side.setsockopt(socket.SOL_SOCKET,socket.SO_PASSCRED,1)
        audit=self.next_audit; self.next_audit+=1
        self.peers[child]=PAuthPeer(child,p_side,audit_id=audit,auth_serial=0,spawn_serial=0)
        return g_transit.detach(),audit

    def attach_pid(self, child: int, outer_pid: int, inner_pid: int, fd4_inode: int) -> None:
        peer=self.peers.get(child)
        if peer is None or peer.outer_pid or inner_pid<=0 or fd4_inode<=0: fail("FD5 attach")
        peer.outer_pid=outer_pid; peer.expected_inner_pid=inner_pid; peer.audited_fd4_inode=fd4_inode

    def _secret(self, kind: str) -> str:
        return bytes(getrandom32(kind,self.secrets)).hex()

    @staticmethod
    def _phase(peer: PAuthPeer) -> str:
        phase={
            "REGISTERED":"REGISTERED","CREATE_GRANTED":"CREATE_GRANTED","CREATE_ACCEPTED":"CREATE_ACCEPTED",
            "INACTIVE_COMMITTED":"INACTIVE_COMMITTED","ACTIVATION_JOINED":"ACTIVATION_JOINED",
            "ACTIVE_RECEIPT_SENT":"ACTIVE_RECEIPT_SENT","ACTIVE_PENDING":"ACTIVE_PENDING",
            "ACTIVE_AUTHORIZED":"ACTIVE","CLOSING":"CLOSING","TERMINAL_PREPARED":"CLOSING",
            "TERMINAL_GRANTED":"CLOSING","TERMINAL_OBSERVED":"CLOSING","FINALIZE_SENT":"CLOSING",
        }.get(peer.state)
        if phase is None or phase not in AUTH_PHASES: fail("auth phase state")
        return phase

    @staticmethod
    def _retain_failure(peer: PAuthPeer, cause: str, state: str, record: str="") -> None:
        if cause not in AUTH_REASONS|V7_TERMINAL_CAUSES|V8_FAILURE_CAUSES: fail("auth failure cause")
        if not peer.first_failure:
            peer.first_failure=cause; peer.failure_state=state
            peer.failure_record_sha256=sha256(record.encode("ascii")) if record else sha256(b"")

    @staticmethod
    def _post_finalize_failure(peer: PAuthPeer, cause: str, record: str="") -> None:
        PAuthentication._retain_failure(peer,cause,peer.state,record)
        peer.state="POST_FINALIZE_FAILED"

    @staticmethod
    def complete_failure_containment(peer: PAuthPeer) -> None:
        if peer.state=="POST_FINALIZE_FAILED": peer.state="AUTH_REAP_FAILED_TOMBSTONE"

    @staticmethod
    def _tuple(peer: PAuthPeer) -> str:
        return f"requester_session=0 requester_child={peer.child} audit={peer.audit_id} auth_serial={peer.auth_serial} auth={peer.auth} session={peer.session}"

    def abort(self, peer: PAuthPeer, reason: str) -> None:
        if peer.state in ("FAILED_TOMBSTONE","POST_FINALIZE_FAILED","AUTH_REAP_FAILED_TOMBSTONE","FINALIZED_ACKED","TERMINAL_RECEIPT_SENT","FD5_EOF_OBSERVED","CHILD_REAPED_VALIDATED","CHILD_REAPED_ACK_SENT","AUTH_REAP_ACK_SENT"): return
        if reason not in AUTH_REASONS: fail("abort reason")
        phase=self._phase(peer); peer.state="ABORTING"
        try:
            self.control.send(f"SESSION_AUTH_ABORT {self._tuple(peer)} phase={phase} reason={reason}")
            reply=self.control.receive()
            values=parse_exact(reply,"SESSION_AUTH_ABORTED",(("requester_session",r"0"),("requester_child",str(peer.child)),("audit",str(peer.audit_id)),("auth_serial",str(peer.auth_serial)),("auth",str(peer.auth)),("session",str(peer.session)),("phase",re.escape(phase)),("reason",re.escape(reason)),("outcome",r"(?:UNSET|ABSENT|DISPLACED_OWNED|DISPLACED_CLEANED|FOREIGN_RETAINED|ERROR|CRASH_TEARDOWN)")))
            if values["outcome"]!="UNSET": fail("abort outcome")
        finally:
            peer.activation_hold=""; peer.state="FAILED_TOMBSTONE"

    def handle(self, peer: PAuthPeer) -> None:
        if peer.outer_pid<=0: fail("FD5 before registration")
        try: record=receive_bare_credential(peer.endpoint,peer.outer_pid)
        except (PossessionFailure,OSError,ValueError,UnicodeError):
            if peer.state in ("FINALIZED_ACKED","TERMINAL_RECEIPT_SENT","FD5_EOF_OBSERVED","CHILD_REAPED_VALIDATED","CHILD_REAPED_ACK_SENT","AUTH_REAP_ACK_SENT"):
                self._post_finalize_failure(peer,"FD5_EXTRA_DATAGRAM")
            elif peer.state in ("NEW","CHALLENGE_ISSUED"):
                self._retain_failure(peer,"REQUESTER_EARLY_EOF",peer.state); peer.state="FAILED_TOMBSTONE"
            else:
                self._retain_failure(peer,"REQUESTER_EARLY_EOF",peer.state)
                self.abort(peer,"REQUESTER_EOF")
            raise
        if record is None:
            if peer.state!="TERMINAL_RECEIPT_SENT" or peer.eof_seen:
                if peer.state in ("FINALIZED_ACKED","POST_FINALIZE_FAILED"):
                    self._post_finalize_failure(peer,"FD5_EARLY_EOF")
                elif peer.state in ("NEW","CHALLENGE_ISSUED"):
                    self._retain_failure(peer,"REQUESTER_EARLY_EOF",peer.state); peer.state="FAILED_TOMBSTONE"
                else:
                    self._retain_failure(peer,"REQUESTER_EARLY_EOF",peer.state)
                    self.abort(peer,"REQUESTER_EOF")
                fail("FD5 premature EOF")
            peer.eof_seen=True; peer.state="FD5_EOF_OBSERVED"; return
        try:
            token=record.partition(" ")[0]
            if token=="SESSION_AUTH_OPEN": self._open(peer,record)
            elif token=="SESSION_AUTH_REGISTERED": self._registered(peer,record)
            elif token=="SESSION_AUTH_ACTIVATED": self._activated(peer,record)
            elif token=="AUDIT_OPEN": self._audit_open(peer,record)
            elif token=="AUDITED_SPAWN": self._audited_spawn(peer,record)
            elif token=="SESSION_AUTH_TERMINAL_OBSERVED": self._terminal(peer,record)
            else: fail("FD5 closed enum")
        except (PossessionFailure,OSError,ValueError,UnicodeError):
            if peer.state in ("FINALIZED_ACKED","TERMINAL_RECEIPT_SENT","FD5_EOF_OBSERVED","CHILD_REAPED_VALIDATED","CHILD_REAPED_ACK_SENT","AUTH_REAP_ACK_SENT"):
                self._post_finalize_failure(peer,"FD5_EXTRA_DATAGRAM",record)
            elif peer.state in ("POST_FINALIZE_FAILED","AUTH_REAP_FAILED_TOMBSTONE"):
                pass
            elif peer.state in ("NEW","CHALLENGE_ISSUED"):
                self._retain_failure(peer,"REQUESTER_EARLY_EOF",peer.state,record); peer.state="FAILED_TOMBSTONE"
            elif peer.state not in ("ABORTING","FAILED_TOMBSTONE"):
                terminal=peer.state in ("CLOSING","TERMINAL_PREPARED","TERMINAL_GRANTED","TERMINAL_OBSERVED","FINALIZE_SENT")
                self._retain_failure(peer,"TERMINAL_OBSERVATION_MISMATCH" if terminal else "REQUESTER_EARLY_EOF",peer.state,record)
                self.abort(peer,"SESSION_CLOSE_FAILURE" if terminal else ("ACTIVATION_MISMATCH" if peer.state in ("CREATE_ACCEPTED","INACTIVE_COMMITTED") else "PREACTIVE_OPERATION"))
            raise

    def _open(self, peer: PAuthPeer, record: str) -> None:
        values=parse_exact(record,"SESSION_AUTH_OPEN",(("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("request",r"[1-9][0-9]*"),("method",r"test_[a-z0-9_]+"),("trigger",r"[A-Z0-9_]+"),("owner",r"[A-Z0-9_]+")))
        expected_owner="SUITE_173" if peer.child==6 else values["method"]
        if peer.state!="NEW" or values["trigger"] not in TRIGGERS or values["owner"]!=expected_owner or (int(values["audit"]),int(values["auth_serial"]),int(values["request"]))!=(peer.audit_id,peer.auth_serial,1): fail("auth OPEN state")
        peer.request=int(values["request"])
        peer.method=values["method"]; peer.trigger=values["trigger"]; peer.owner=values["owner"]
        peer.auth=self.next_auth; self.next_auth+=1; peer.session=self.next_session; self.next_session+=1; peer.state="CHALLENGE_ISSUED"
        send_bare(peer.endpoint,f"SESSION_AUTH_CHALLENGE audit={peer.audit_id} auth_serial={peer.auth_serial} auth={peer.auth} session={peer.session}")

    def _registered(self, peer: PAuthPeer, record: str) -> None:
        values=parse_exact(record,"SESSION_AUTH_REGISTERED",(("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("method",r"test_[a-z0-9_]+"),("trigger",r"[A-Z0-9_]+"),("owner",r"[A-Z0-9_]+"),("registration",r"(?:[0-9a-f]{2})+"),("digest",r"[0-9a-f]{64}")))
        if peer.state!="CHALLENGE_ISSUED" or (values["audit"],values["auth_serial"],values["auth"],values["session"],values["request"],values["method"],values["trigger"],values["owner"])!=(str(peer.audit_id),str(peer.auth_serial),str(peer.auth),str(peer.session),str(peer.request),peer.method,peer.trigger,peer.owner): fail("auth registration join")
        registration=bytes.fromhex(values["registration"])
        if sha256(registration)!=values["digest"]: fail("auth registration digest")
        match=re.fullmatch(rb"request=([1-9][0-9]*) method=(test_[a-z0-9_]+) trigger=([A-Z0-9_]+) owner=([A-Z0-9_]+) fd4_inode=([1-9][0-9]*) rpc_inner_pid=([1-9][0-9]*) rpc_inner_uid=0 rpc_inner_gid=0",registration)
        if match is None or (match.group(1).decode(),match.group(2).decode(),match.group(3).decode(),match.group(4).decode(),int(match.group(5)),int(match.group(6)))!=(str(peer.request),values["method"],values["trigger"],values["owner"],peer.audited_fd4_inode,peer.expected_inner_pid): fail("auth registration")
        peer.registration_digest=values["digest"]; peer.fd4_inode=int(match.group(5)); peer.rpc_inner_pid=int(match.group(6)); peer.state="REGISTERED"
        peer.create_cap=self._secret("create_cap")
        create_payload=f"SESSION_CREATE request={peer.request} session={peer.session} method={peer.method} trigger={peer.trigger} owner={peer.owner} auth={peer.auth} create_cap={peer.create_cap}".encode("ascii")
        peer.create_frame=struct.pack(">I",len(create_payload))+create_payload
        peer.create_template=f"SESSION_CREATE request={peer.request} session={peer.session} method={peer.method} trigger={peer.trigger} owner={peer.owner} auth={peer.auth} create_cap={{CREATE_CAP64}}".encode("ascii")
        peer.create_identity=f"requester_child={peer.child} audit={peer.audit_id} auth_serial={peer.auth_serial} auth={peer.auth} session={peer.session} request={peer.request} method={peer.method} trigger={peer.trigger} owner={peer.owner} fd4_endpoint_inode={peer.fd4_inode} rpc_inner_pid={peer.rpc_inner_pid} rpc_inner_uid=0 rpc_inner_gid=0".encode("ascii")
        peer.create_commitment=v7_bind("P15R-CREATE-COMMITMENT-v7",peer.create_identity,peer.create_frame)
        self.control.send(f"SESSION_AUTH_CREATE_GRANTED requester_session=0 requester_child={peer.child} audit={peer.audit_id} auth_serial={peer.auth_serial} auth={peer.auth} session={peer.session} request={peer.request} registration_digest={peer.registration_digest} create_commitment={peer.create_commitment} template={peer.create_template.hex()} fd4_endpoint_inode={peer.fd4_inode} rpc_inner_pid={peer.rpc_inner_pid} rpc_inner_uid=0 rpc_inner_gid=0")
        peer.state="CREATE_GRANTED"
        send_bare(peer.endpoint,f"SESSION_AUTH_RECEIPT audit={peer.audit_id} auth_serial={peer.auth_serial} auth={peer.auth} session={peer.session} request={peer.request} digest={peer.registration_digest} create_cap={peer.create_cap} create={peer.create_frame.hex()}")
        peer.create_receipt_sent=True

    def handle_control(self, record: str) -> None:
        token=record.partition(" ")[0]
        if token=="SESSION_AUTH_CREATE_ACCEPTED":
            fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("registration_digest",r"[0-9a-f]{64}"),("create_commitment",r"[0-9a-f]{64}"),("create_cap",r"[0-9a-f]{64}"),("payload",r"(?:[0-9a-f]{2})+"),("fd4_endpoint_inode",r"[1-9][0-9]*"),("rpc_inner_pid",r"[1-9][0-9]*"),("rpc_inner_uid",r"0"),("rpc_inner_gid",r"0"))
            values=parse_exact(record,token,fields); peer=self.peers.get(int(values["requester_child"]))
            if peer is None or peer.state!="CREATE_GRANTED" or not peer.create_receipt_sent or (values["audit"],values["auth_serial"],values["auth"],values["session"],values["request"],values["registration_digest"],values["create_commitment"],values["create_cap"],values["payload"],values["fd4_endpoint_inode"],values["rpc_inner_pid"])!=(str(peer.audit_id),str(peer.auth_serial),str(peer.auth),str(peer.session),str(peer.request),peer.registration_digest,peer.create_commitment,peer.create_cap,peer.create_frame.hex(),str(peer.fd4_inode),str(peer.rpc_inner_pid)) or v7_bind("P15R-CREATE-COMMITMENT-v7",peer.create_identity,bytes.fromhex(values["payload"]))!=peer.create_commitment: fail("create accepted causal source")
            peer.state="CREATE_ACCEPTED"; peer.reply_nonce=self._secret("reply_nonce"); peer.created=f"SESSION_CREATED request={peer.request} session={peer.session} reply_nonce={peer.reply_nonce}".encode("ascii"); peer.created_digest=sha256(peer.created)
            self.control.send(f"SESSION_AUTH_COMMIT {self._tuple(peer)} request={peer.request} reply_nonce={peer.reply_nonce} created={peer.created.hex()}")
        elif token=="SESSION_AUTH_COMMITTED":
            fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("reply_nonce",r"[0-9a-f]{64}"),("created",r"(?:[0-9a-f]{2})+"))
            values=parse_exact(record,token,fields); peer=self.peers.get(int(values["requester_child"]))
            if peer is None or peer.state!="CREATE_ACCEPTED" or (values["audit"],values["auth_serial"],values["auth"],values["session"],values["request"],values["reply_nonce"],values["created"])!=(str(peer.audit_id),str(peer.auth_serial),str(peer.auth),str(peer.session),str(peer.request),peer.reply_nonce,peer.created.hex()): fail("committed join")
            peer.state="INACTIVE_COMMITTED"
            if peer.activation_hold: self._join_activation(peer)
        elif token=="SESSION_AUTH_ACTIVE_ACK":
            fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("active_cap_commitment",r"[0-9a-f]{64}"),("created_digest",r"[0-9a-f]{64}"))
            values=parse_exact(record,token,fields); peer=self.peers.get(int(values["requester_child"]))
            if peer is None or peer.state!="ACTIVE_PENDING" or (values["audit"],values["auth_serial"],values["auth"],values["session"],values["request"],values["active_cap_commitment"],values["created_digest"])!=(str(peer.audit_id),str(peer.auth_serial),str(peer.auth),str(peer.session),str(peer.request),peer.active_cap_commitment,peer.created_digest): fail("active ACK join")
            peer.state="ACTIVE_AUTHORIZED"
        elif token=="SESSION_AUTH_ABORTED":
            fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("phase",r"(?:REGISTERED|CREATE_GRANTED|CREATE_ACCEPTED|INACTIVE_COMMITTED|ACTIVATION_JOINED|ACTIVE_RECEIPT_SENT|ACTIVE_PENDING|ACTIVE|CLOSING)"),("reason",r"(?:RECEIPT_SEND|REQUESTER_EOF|CREATE_MISMATCH|CREATE_ACCEPTED_SEND|COMMIT_SEND|PRIVATE_CONSTRUCTION|CREATED_SEND|COMMITTED_SEND|ACTIVATION_MISMATCH|ACTIVE_RECEIPT_SEND|ACTIVE_SEND|ACTIVE_ACK_SEND|PREACTIVE_OPERATION|ACTIVE_OPERATION_MISMATCH|SESSION_CLOSE_FAILURE|CONTROL_EOF)"),("outcome",r"(?:UNSET|ABSENT|DISPLACED_OWNED|DISPLACED_CLEANED|FOREIGN_RETAINED|ERROR|CRASH_TEARDOWN)"))
            values=parse_exact(record,token,fields); peer=self.peers.get(int(values["requester_child"]))
            if peer is None or peer.state in ("FINALIZED_ACKED","TERMINAL_RECEIPT_SENT","FD5_EOF_OBSERVED","CHILD_REAPED_VALIDATED","CHILD_REAPED_ACK_SENT","AUTH_REAP_ACK_SENT","POST_FINALIZE_FAILED","AUTH_REAP_FAILED_TOMBSTONE","FAILED_TOMBSTONE") or (values["audit"],values["auth_serial"],values["auth"],values["session"])!=(str(peer.audit_id),str(peer.auth_serial),str(peer.auth),str(peer.session)) or values["phase"]!=self._phase(peer) or values["outcome"]!="UNSET": fail("G abort join")
            self._retain_failure(peer,values["reason"],peer.state,record)
            peer.activation_hold=""; peer.state="FAILED_TOMBSTONE"
        else: fail("P D-M1 control")

    def _activated(self, peer: PAuthPeer, record: str) -> None:
        values=parse_exact(record,"SESSION_AUTH_ACTIVATED",(("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("reply_nonce",r"[0-9a-f]{64}"),("created",r"(?:[0-9a-f]{2})+")))
        created=bytes.fromhex(values["created"])
        if peer.state not in ("CREATE_ACCEPTED","INACTIVE_COMMITTED") or peer.activation_hold or (values["audit"],values["auth_serial"],values["auth"],values["session"],values["request"],values["reply_nonce"])!=(str(peer.audit_id),str(peer.auth_serial),str(peer.auth),str(peer.session),str(peer.request),peer.reply_nonce) or created!=peer.created: fail("active direct claim")
        peer.activation_hold=record
        if peer.state=="INACTIVE_COMMITTED": self._join_activation(peer)

    def _join_activation(self, peer: PAuthPeer) -> None:
        if peer.state!="INACTIVE_COMMITTED" or not peer.activation_hold: fail("activation hold join")
        peer.state="ACTIVATION_JOINED"
        peer.active_cap=self._secret("active_cap")
        peer.active_identity=f"requester_child={peer.child} audit={peer.audit_id} auth_serial={peer.auth_serial} auth={peer.auth} session={peer.session} method={peer.method} trigger={peer.trigger} owner={peer.owner} fd4_endpoint_inode={peer.fd4_inode}".encode("ascii")
        peer.active_cap_commitment=v7_bind("P15R-ACTIVE-COMMITMENT-v7",peer.active_identity,bytes.fromhex(peer.active_cap))
        send_bare(peer.endpoint,f"SESSION_AUTH_ACTIVE_RECEIPT audit={peer.audit_id} auth_serial={peer.auth_serial} auth={peer.auth} session={peer.session} request={peer.request} active_cap={peer.active_cap} created_digest={peer.created_digest}")
        peer.state="ACTIVE_RECEIPT_SENT"
        self.control.send(f"SESSION_AUTH_ACTIVE {self._tuple(peer)} request={peer.request} active_cap_commitment={peer.active_cap_commitment} created_digest={peer.created_digest}")
        peer.state="ACTIVE_PENDING"
        peer.activation_hold=""

    def _audit_open(self, peer: PAuthPeer, record: str) -> None:
        values=parse_exact(record,"AUDIT_OPEN",(("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)")))
        key=(int(values["audit"]),int(values["serial"]))
        if peer.state!="ACTIVE_AUTHORIZED" or key!=(peer.audit_id,peer.spawn_serial) or key in peer.audits: fail("audit OPEN")
        nonce=sha256(f"P15R-AUDIT-NONCE-v1 audit={peer.audit_id} requester_session={peer.session} requester_child={peer.child} serial={peer.spawn_serial}".encode("ascii"))
        peer.audits[key]=(nonce,"","",b"")
        send_bare(peer.endpoint,f"AUDIT_CHALLENGE audit={key[0]} serial={key[1]} nonce={nonce}")

    def _audited_spawn(self, peer: PAuthPeer, record: str) -> None:
        values=parse_exact(record,"AUDITED_SPAWN",(("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}"),("trigger",r"[A-Z0-9_]+"),("core",r"(?:[0-9a-f]{2})+")))
        key=(int(values["audit"]),int(values["serial"])); prior=peer.audits.get(key)
        core=bytes.fromhex(values["core"])
        if peer.state!="ACTIVE_AUTHORIZED" or prior is None or prior[1] or values["nonce"]!=prior[0] or values["trigger"] not in TRIGGERS or sha256(core)!=values["digest"]: fail("audited spawn")
        text=core.decode("ascii")
        if re.fullmatch(r"SPAWN request=[1-9][0-9]* session=[1-9][0-9]* target=[A-Z0-9_]+ method=test_[a-z0-9_]+ purpose=[A-Z0-9_]+ handle=[0-9]+",text) is None: fail("audited spawn core")
        peer.audits[key]=(prior[0],values["digest"],text,record.encode("ascii"))
        send_bare(peer.endpoint,f"AUDIT_RECEIPT audit={key[0]} serial={key[1]} nonce={prior[0]} digest={values['digest']}")
        peer.spawn_serial+=1

    def grant_terminal(self, record: str, cleanup_ready: bool) -> None:
        fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("close_request",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("terminal_template",r"(?:[0-9a-f]{2})+"))
        values=parse_exact(record,"SESSION_AUTH_TERMINAL_PREPARED",fields); peer=self.peers.get(int(values["requester_child"]))
        if peer is None or peer.state!="ACTIVE_AUTHORIZED" or not cleanup_ready or (values["audit"],values["auth_serial"],values["auth"],values["session"])!=(str(peer.audit_id),str(peer.auth_serial),str(peer.auth),str(peer.session)): fail("terminal prepared")
        peer.terminal_request=int(values["close_request"]); peer.terminal_outcome=values["outcome"]
        peer.terminal_template=f"SESSION_CLOSED request={peer.terminal_request} session={peer.session} outcome={peer.terminal_outcome} terminal_cap={{TERMINAL_CAP64}}".encode("ascii")
        if values["terminal_template"]!=peer.terminal_template.hex(): fail("terminal template")
        peer.state="CLOSING"; peer.state="TERMINAL_PREPARED"; peer.terminal_cap=self._secret("terminal_cap")
        payload=f"SESSION_CLOSED request={peer.terminal_request} session={peer.session} outcome={peer.terminal_outcome} terminal_cap={peer.terminal_cap}".encode("ascii")
        peer.terminal_frame=struct.pack(">I",len(payload))+payload
        peer.terminal_reply_digest=sha256(b"P15R-TERMINAL-REPLY-v7 "+peer.terminal_frame)
        peer.terminal_cap_digest=sha256(b"P15R-TERMINAL-CAP-v7 "+bytes.fromhex(peer.terminal_cap))
        self.control.send(f"SESSION_AUTH_TERMINAL_GRANTED {self._tuple(peer)} close_request={peer.terminal_request} outcome={peer.terminal_outcome} terminal_cap={peer.terminal_cap} reply_digest={peer.terminal_reply_digest} reply={peer.terminal_frame.hex()}")
        peer.state="TERMINAL_GRANTED"

    def _terminal(self, peer: PAuthPeer, record: str) -> None:
        values=parse_exact(record,"SESSION_AUTH_TERMINAL_OBSERVED",(("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("close_request",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("terminal_cap",r"[0-9a-f]{64}"),("reply_digest",r"[0-9a-f]{64}"),("reply",r"(?:[0-9a-f]{2})+")))
        if peer.state!="TERMINAL_GRANTED" or peer.terminal_observation_consumed or (values["audit"],values["auth_serial"],values["auth"],values["session"],values["close_request"],values["outcome"],values["terminal_cap"],values["reply_digest"])!=(str(peer.audit_id),str(peer.auth_serial),str(peer.auth),str(peer.session),str(peer.terminal_request),peer.terminal_outcome,peer.terminal_cap,peer.terminal_reply_digest): fail("terminal observation")
        peer.terminal_observation_consumed=True
        reply=bytes.fromhex(values["reply"])
        if reply!=peer.terminal_frame or sha256(b"P15R-TERMINAL-REPLY-v7 "+reply)!=values["reply_digest"]: fail("terminal reply digest")
        peer.state="TERMINAL_OBSERVED"
        self.control.send(f"SESSION_AUTH_FINALIZE {self._tuple(peer)} close_request={peer.terminal_request} outcome={peer.terminal_outcome} terminal_cap_sha256={peer.terminal_cap_digest} reply_digest={peer.terminal_reply_digest}")
        peer.state="FINALIZE_SENT"
        finalized=self.control.receive()
        fields=(("requester_session",r"0"),("requester_child",str(peer.child)),("audit",str(peer.audit_id)),("auth_serial",str(peer.auth_serial)),("auth",str(peer.auth)),("session",str(peer.session)),("close_request",str(peer.terminal_request)),("outcome",re.escape(peer.terminal_outcome)),("terminal_cap_sha256",re.escape(peer.terminal_cap_digest)),("reply_digest",re.escape(peer.terminal_reply_digest)))
        parse_exact(finalized,"SESSION_AUTH_FINALIZED_ACK",fields); peer.finalized_ack_complete=True; peer.state="FINALIZED_ACKED"
        receipt=f"SESSION_AUTH_TERMINAL_RECEIPT audit={peer.audit_id} auth_serial={peer.auth_serial} auth={peer.auth} session={peer.session} close_request={peer.terminal_request} outcome={peer.terminal_outcome} terminal_cap_sha256={peer.terminal_cap_digest} reply_digest={peer.terminal_reply_digest}"
        peer.terminal_receipt=receipt.encode("ascii"); peer.terminal_receipt_attempted=True
        try: send_bare(peer.endpoint,receipt)
        except (PossessionFailure,OSError):
            peer.terminal_cause="TERMINAL_RECEIPT_SEND"; self._post_finalize_failure(peer,"TERMINAL_RECEIPT_SEND",receipt); raise
        peer.terminal_receipt_complete=True; peer.state="TERMINAL_RECEIPT_SENT"


def resolve_direct_child(proc_root: int, guardian_outer_pid: int, inner_pid: int) -> int:
    matches=[]
    for name in os.listdir(proc_root):
        if re.fullmatch(r"[1-9][0-9]*",name) is None: continue
        pid=int(name)
        try:
            directory=openat2(proc_root,name,OPEN_PATH_DIR)
            try:
                status=parse_proc_status(read_regular_at(directory,"status",1024*1024))
            finally: os.close(directory)
        except OSError: continue
        nspid=tuple(int(value) for value in status.get("NSpid","").split())
        if int(status.get("PPid","0"))==guardian_outer_pid and nspid and nspid[-1]==inner_pid: matches.append(pid)
    if len(matches)!=1: fail("child outer pid cardinality")
    return matches[0]


@dataclass
class PChildMirror:
    child: int
    session: int
    inner_pid: int
    outer_pid: int
    role: str
    target: str
    owner: str
    purpose: str
    admission: str
    fdset: str
    pidfd: int
    pidfd_serial: int
    pidfd_identity_sha256: str
    pidfd_ledger: PIDFDLifetimeEntry
    pidfd_state: str="VALIDATED"
    fd4_inode: int=0
    fd4_peer_inode: int=0
    start_time: int=0
    nspid: tuple[int,...]=()
    cgroup: str=""
    uid: int=0
    gid: int=0
    expected_status: int=0
    source_ready: bool=False
    reaped: bool=False
    status: int=-1
    reap_record: str=""
    reap_ack: str=""


class PController:
    def __init__(self, control: FramedControl, tree: CgroupTree, guardian_pid: int, guardian_pidfd: int, guardian_identity: DMAuditIdentityExpectation, guardian_pidfd_ledger: PIDFDLifetimeEntry, proc_root: int, proc_root_ledger: LongLivedProcRootLedger, diag: UnixDiagOracle, secrets: list[tuple[str,bytearray]], source_fds: tuple[int,int], signal_fd: int) -> None:
        self.control=control; self.tree=tree; self.guardian_pid=guardian_pid; self.guardian_pidfd=guardian_pidfd; self.proc_root=proc_root; self.diag=diag
        self.auth=PAuthentication(control,secrets); self.auditor=FDAuditor(control,proc_root,proc_root_ledger,guardian_pid,guardian_pidfd,guardian_identity,guardian_pidfd_ledger,diag,tree)
        self.children: dict[int,PChildMirror]={}; self.objects: dict[int,ObjectIdentity]={}; self.released_objects: dict[int,ObjectIdentity]={}; self.member_authorizations: dict[int,tuple[int,str,str]]={}; self.creator_reaped: dict[int,tuple[int,int,int]]={}; self.method_role_counts: dict[tuple[int,str],int]={}; self.final_states: list[str]=[]; self.global_phase=0; self.cleanup_results=0; self.cleanup_outcomes: list[str]=[]; self.freeze_epoch=0; self.method_epochs: dict[tuple[int,int],int]={}; self.final_epoch=0; self.final_cleanup_expected=0; self.final_cleanup_reported: set[int]=set(); self.probe_reaped: set[int]=set(); self.done=False; self.source_fds=source_fds; self.signal_fd=signal_fd
        self.next_pidfd_serial=2; self.guardian_pidfd_serial=1; self.boundary_ledger: BoundaryLedger|None=None; self.boundary_failure: BoundaryFailureTombstone|None=None; self.boundary_terminal_context: BoundaryTerminalContext|None=None; self.boundary_receipt: BoundaryFailureReceipt|BoundaryTerminalSuccessReceipt|None=None; self.seal_validated=False
        self.boundary_hashes={"hp":"NONE","hg":"NONE","hm":"NONE","mech":"NONE","contract":"NONE","profile":HOOK_CUSTODY_PROFILE_SHA256}
        self.pending_signal=0; self.signal_cleaned=False; self.final_outcome="ABSENT"
        self.first_failure=""; self.failure_state=""; self.failure_record_sha256=""

    def _bootstrap_record(self) -> str:
        poller=select.poll(); poller.register(self.control.sock,select.POLLIN|select.POLLHUP|select.POLLERR); poller.register(self.signal_fd,select.POLLIN|select.POLLERR)
        while True:
            try: events=poller.poll()
            except InterruptedError: fail("bootstrap poll EINTR")
            if not events: fail("bootstrap empty poll")
            for fd,event in events:
                if event&(select.POLLERR|select.POLLNVAL): fail("bootstrap poll event")
                if fd==self.signal_fd: fail("handled signal during bootstrap")
                if fd==self.control.sock.fileno():
                    if event&select.POLLHUP: fail("bootstrap control EOF")
                    return self.control.receive()
                fail("bootstrap unknown fd")

    def run_bootstrap_probes(self) -> None:
        allowed={"CHILD_REGISTERED","SOURCE_READY","CHILD_REAPED","CGROUP_PROBE_CHILD","CGROUP_PROBE_REAPED"}
        while self.probe_reaped!={1,2}:
            record=self._bootstrap_record()
            if record.partition(" ")[0] not in allowed: fail("bootstrap probe record")
            self.handle_control(record)
        if any(not self.children[index].reaped for index in (1,2)) or self.tree.members(self.tree.workers_fd): fail("bootstrap probe terminal ledger")

    def retain_failure(self, cause: str, record: str="") -> None:
        if cause not in V8_FAILURE_CAUSES: fail("P global failure cause")
        if not self.first_failure:
            self.first_failure=cause; self.failure_state=f"global={self.global_phase}"
            self.failure_record_sha256=sha256(record.encode("ascii")) if record else sha256(b"")

    def complete_failure_containment(self, peer_reaped: bool) -> None:
        if peer_reaped: self.close_child_pidfd_ledgers()
        else: self.mark_child_pidfd_ledgers_ambiguous()
        for peer in self.auth.peers.values(): self.auth.complete_failure_containment(peer)

    def close_child_pidfd_ledgers(self) -> bool:
        unambiguous=True
        for child in sorted(self.children):
            mirror=self.children[child]; ledger=mirror.pidfd_ledger
            if mirror.pidfd_state=="CLOSED_PROVED":
                if mirror.pidfd!=-1 or ledger.state!="CLOSED_PROVED":
                    mirror.pidfd_state=ledger.state="AMBIGUOUS_CRASH_ONLY"; unambiguous=False
                continue
            if mirror.pidfd_state!="VALIDATED" or ledger.state!="VALIDATED" or mirror.pidfd<0:
                mirror.pidfd_state=ledger.state="AMBIGUOUS_CRASH_ONLY"; unambiguous=False; continue
            try: close_proved(mirror.pidfd)
            except (OSError,PossessionFailure):
                mirror.pidfd_state=ledger.state="AMBIGUOUS_CRASH_ONLY"; unambiguous=False
            else:
                mirror.pidfd=-1; mirror.pidfd_state=ledger.state="CLOSED_PROVED"
        return unambiguous

    def mark_child_pidfd_ledgers_ambiguous(self) -> None:
        for child in sorted(self.children):
            mirror=self.children[child]; ledger=mirror.pidfd_ledger
            if mirror.pidfd_state=="VALIDATED" and ledger.state=="VALIDATED" and mirror.pidfd>=0:
                mirror.pidfd_state=ledger.state="AMBIGUOUS_CRASH_ONLY"
            elif mirror.pidfd_state!="CLOSED_PROVED" or ledger.state!="CLOSED_PROVED" or mirror.pidfd!=-1:
                mirror.pidfd_state=ledger.state="AMBIGUOUS_CRASH_ONLY"

    def complete_terminal_or_unreconciled(self, connection: socket.socket, peer_reaped: bool, child_pidfds_closed: bool) -> None:
        context=self.boundary_terminal_context
        def close_unreconciled_endpoint() -> None:
            endpoint_fd=connection.fileno()
            if endpoint_fd<0: return
            try: connection.close(); immediate_ebadf(endpoint_fd)
            except (OSError,PossessionFailure): os._exit(125)
        if context is None or not context.holder_ceiling:
            close_unreconciled_endpoint(); return
        if connection.fileno()<0: return
        if not child_pidfds_closed:
            self.boundary_receipt=None; self.boundary_failure=context.reconciler.retain_unreconciled("P",context.endpoint_identity,context.evidence); close_unreconciled_endpoint(); return
        try: receipt=complete_v14_terminal_survivor(context,connection,self.control,self.boundary_hashes,peer_reaped)
        except (PossessionFailure,OSError,ValueError,UnicodeError,MemoryError):
            self.boundary_receipt=None; self.boundary_failure=context.reconciler.retain_unreconciled("P",context.endpoint_identity,context.evidence)
            close_unreconciled_endpoint()
        else:
            self.boundary_receipt=receipt; self.boundary_failure=None

    def consume_signalfd(self) -> None:
        try: record=os.read(self.signal_fd,128)
        except BlockingIOError: fail("signalfd readiness without record")
        if len(record)!=128: fail("signalfd record")
        signo=struct.unpack_from("=I",record,0)[0]
        if signo not in HANDLED_SIGNALS or self.pending_signal: fail("signalfd signal/cardinality")
        wire=f"SIGNAL_PENDING signo={signo}"
        self.control.send(wire)
        self.pending_signal=signo
        for peer in self.auth.peers.values():
            if peer.state in ("FINALIZED_ACKED","TERMINAL_RECEIPT_SENT","FD5_EOF_OBSERVED","CHILD_REAPED_VALIDATED","CHILD_REAPED_ACK_SENT","AUTH_REAP_ACK_SENT"):
                self.auth._post_finalize_failure(peer,"GLOBAL_FINAL_PROOF",wire)
            elif peer.state not in ("FAILED_TOMBSTONE","AUTH_REAP_FAILED_TOMBSTONE"):
                self.auth._retain_failure(peer,"SESSION_CLOSE_FAILURE",peer.state,wire); peer.state="FAILED_TOMBSTONE"

    def control_failure(self, cause: str, record: str="") -> None:
        global_failure=self.global_phase>0 or all(peer.state in ("AUTH_REAP_ACK_SENT","AUTH_REAP_FAILED_TOMBSTONE") for peer in self.auth.peers.values())
        self.retain_failure("GLOBAL_FINAL_RECORD" if global_failure else cause,record)
        for peer in self.auth.peers.values():
            if peer.state in ("FINALIZED_ACKED","TERMINAL_RECEIPT_SENT","FD5_EOF_OBSERVED","CHILD_REAPED_VALIDATED","CHILD_REAPED_ACK_SENT","AUTH_REAP_ACK_SENT"):
                self.auth._post_finalize_failure(peer,cause,record)
            elif peer.state not in ("NEW","CHALLENGE_ISSUED","FAILED_TOMBSTONE","AUTH_REAP_FAILED_TOMBSTONE"):
                self.auth._retain_failure(peer,"CONTROL_EOF",peer.state,record); peer.state="FAILED_TOMBSTONE"

    def expected_child_status(self, session: int, child: int, values: Mapping[str,str]) -> int:
        if session==0: return (0 if child==1 else 128+signal.SIGKILL) if child in (1,2) else 0
        target=values.get("target",values["role"]); method=values["admission"].split(":",2)[1]
        coordinate=(session,target); count=self.method_role_counts.get(coordinate,0)+1; self.method_role_counts[coordinate]=count
        if target=="COPIED_REPRODUCE":
            if method not in COPIED_EXPECTED_STATUS: fail("copied expected status method")
            return COPIED_EXPECTED_STATUS[method]
        if target=="LOCK_CONTENDER": return 74
        if target in ("VERIFY_ONLY_GENERATOR","GENERATE_MUTATION") and count>1: return 1
        return 0

    def _registered(self, record: str) -> None:
        token=record.partition(" ")[0]; audited=token=="CHILD_REGISTERED_AUDITED"
        if token not in ("CHILD_REGISTERED","CHILD_REGISTERED_AUDITED"): fail("registered token")
        base=(("session",r"[0-9]+"),("child",r"[1-9][0-9]*"),("inner_pid",r"[1-9][0-9]*"),("role",r"[A-Z0-9_]+"),("owner",r"[A-Za-z0-9_]+"),("purpose",r"[A-Z0-9_]+"),("admission",r"[A-Za-z0-9_:]+"),("fdset",r"[A-Z0-9_]+"),("cwd_dev",r"[0-9]+"),("cwd_ino",r"[1-9][0-9]*"))
        extra=(("target",r"[A-Z0-9_]+"),("trigger",r"[A-Z0-9_]+"),("request",r"[1-9][0-9]*"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}")) if audited else ()
        values=parse_exact(record,token,base+extra); child=int(values["child"]); session=int(values["session"]); inner=int(values["inner_pid"])
        if child in self.children or values["fdset"] not in FDSETS or values["role"] not in set(ROLE_BY_TARGET.values()): fail("child mirror registry")
        if (session>0)!=audited: fail("method child audit class")
        if session==0 and child<=len(PRE_SUITE_CHILDREN):
            row=PRE_SUITE_CHILDREN[child-1]
            target=row.target.split(" ",1)[0]
            if (child,session,values["role"],values["owner"],values["purpose"],values["admission"],values["fdset"])!=(row.child,row.session,row.role,row.owner,row.purpose,row.admission,row.fdset): fail("frozen pre-suite registry")
        else:
            target=values.get("target","")
        if audited:
            requester=int(values["requester_child"]); peer=self.auth.peers.get(requester); key=(int(values["audit"]),int(values["serial"])); authorization=None if peer is None else peer.audits.get(key)
            requester_mirror=self.children.get(requester)
            if authorization is None or requester_mirror is None or requester_mirror.reaped or key not in peer.confirmed_audits or key in peer.consumed_audits or (values["nonce"],values["digest"])!=(authorization[0],authorization[1]): fail("audited child authorization")
            core=parse_exact(authorization[2],"SPAWN",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("target",r"[A-Z0-9_]+"),("method",r"test_[a-z0-9_]+"),("purpose",r"[A-Z0-9_]+"),("handle",r"[0-9]+")))
            outer=parse_exact(authorization[3].decode("ascii"),"AUDITED_SPAWN",(("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}"),("trigger",r"[A-Z0-9_]+"),("core",r"(?:[0-9a-f]{2})+")))
            if (core["request"],core["session"],core["target"],core["method"],core["purpose"],outer["trigger"],bytes.fromhex(outer["core"]))!=(values["request"],values["session"],values["target"],values["admission"].split(":",2)[1],values["purpose"],values["trigger"],authorization[2].encode("ascii")): fail("audited child causal join")
            peer.consumed_audits.add(key)
        outer=resolve_direct_child(self.proc_root,self.guardian_pid,inner)
        process_fd=openat2(self.proc_root,str(outer),OPEN_PATH_DIR)
        try:
            start_time,nspid,cgroup,uid,gid=worker_proc_identity(process_fd,outer,self.guardian_pid,inner,65534,65534)
            workers_st=os.fstat(self.tree.workers_fd)
            identity_expectation=DMAuditIdentityExpectation("CHILD",outer,start_time,nspid,inner,cgroup,workers_st.st_dev,workers_st.st_ino,session,child,values["role"],values["owner"])
            identity_before=dmaudit_identity_bytes(process_fd,identity_expectation)
        finally: close_proved(process_fd)
        pidfd=-1; pidfd_ledger: PIDFDLifetimeEntry|None=None
        try:
            pidfd=syscall(SYS_PIDFD_OPEN,ctypes.c_int(outer),ctypes.c_uint(0))
            pidfd_serial=self.next_pidfd_serial; self.next_pidfd_serial+=1
            pidfd_ledger=pidfd_lifetime_entry(pidfd_serial,pidfd,identity_expectation,identity_before)
            if fcntl.fcntl(pidfd,fcntl.F_GETFD)!=FD_CLOEXEC: fail("child pidfd CLOEXEC")
            process_fd=openat2(self.proc_root,str(outer),OPEN_PATH_DIR)
            try:
                after=worker_proc_identity(process_fd,outer,self.guardian_pid,inner,65534,65534); identity_after=dmaudit_identity_bytes(process_fd,identity_expectation)
            finally: close_proved(process_fd)
            if after!=(start_time,nspid,cgroup,uid,gid) or identity_after!=identity_before: fail("child pidfd identity ABA")
            pidfd_ledger.state="VALIDATED"
        except BaseException:
            if pidfd>=0 and fd_is_open(pidfd): close_proved(pidfd)
            if pidfd_ledger is not None: pidfd_ledger.state="CLOSED_PROVED"
            raise
        if pidfd_ledger is None or pidfd_ledger.state!="VALIDATED": fail("child pidfd ledger validation")
        expected_status=self.expected_child_status(session,child,values)
        identity_sha=dmaudit_identity_digest(identity_before)
        mirror=PChildMirror(child,session,inner,outer,values["role"],target,values["owner"],values["purpose"],values["admission"],values["fdset"],pidfd,pidfd_serial,identity_sha,pidfd_ledger,start_time=start_time,nspid=nspid,cgroup=cgroup,uid=uid,gid=gid,expected_status=expected_status); self.children[child]=mirror
        if self.pending_signal:
            return
        if mirror.fdset=="STDIO_SOURCE_ROOT_BARRIER": return
        self._audit_and_admit(mirror)

    def _dmaudit_child_identity(self, mirror: PChildMirror) -> DMAuditIdentityExpectation:
        cgroup_st=os.fstat(self.tree.workers_fd)
        if mirror.start_time<=0 or not mirror.nspid or mirror.nspid[-1]!=mirror.inner_pid or mirror.cgroup!="0::"+self.tree.relative("workers")+"\n" or (mirror.uid,mirror.gid)!=(65534,65534): fail("child D-M2 identity")
        ledger=mirror.pidfd_ledger
        if re.fullmatch(r"[0-9a-f]{64}",mirror.pidfd_identity_sha256) is None or mirror.pidfd_state!="VALIDATED" or (ledger.pidfd_serial,ledger.local_fd,ledger.subject,ledger.outer_pid,ledger.start_time,ledger.cgroup_dev,ledger.cgroup_ino,ledger.state)!=(mirror.pidfd_serial,mirror.pidfd,"CHILD",mirror.outer_pid,mirror.start_time,cgroup_st.st_dev,cgroup_st.st_ino,"VALIDATED"): fail("child pidfd ledger")
        return DMAuditIdentityExpectation("CHILD",mirror.outer_pid,mirror.start_time,mirror.nspid,mirror.inner_pid,mirror.cgroup,cgroup_st.st_dev,cgroup_st.st_ino,mirror.session,mirror.child,mirror.role,mirror.owner,mirror.pidfd_identity_sha256)

    def _audit_live_slots(self, mirror: PChildMirror, phase: int) -> None:
        if phase not in (0,1,2) or mirror.reaped or mirror.pidfd_state!="VALIDATED": fail("D-M2 P phase")
        kind="PREFLIGHT_PROBE" if mirror.child==1 else "RUNTIME_CHILD"
        if kind=="PREFLIGHT_PROBE" and (mirror.session,mirror.target)!=(0,"CGROUP_PROBE_CHILD"): fail("D-M2 P preflight tuple")
        slots=tuple(slot for slot in (8,4,5) if slot in FDSETS[mirror.fdset][phase])
        if phase==2:
            if mirror.target not in ("TOP_TEST_CONTROLS","COPIED_REPRODUCE") or not mirror.source_ready: fail("D-M2 P running tuple")
            slots=tuple(slot for slot in slots if slot in (4,5))
        child_identity=self._dmaudit_child_identity(mirror)
        for slot in slots:
            peer=self.auth.peers.get(mirror.child); p_peer_fd=peer.endpoint.fileno() if slot==5 and peer is not None else -1
            evidence=self.auditor.audit(kind,mirror.session,mirror.child,mirror.outer_pid,slot,mirror.pidfd,mirror.pidfd_serial,child_identity,mirror.pidfd_ledger,p_peer_fd)
            if slot==4:
                observed=(evidence.child_slot_inode,evidence.guardian_peer_inode)
                if phase==0: mirror.fd4_inode,mirror.fd4_peer_inode=observed
                elif observed!=(mirror.fd4_inode,mirror.fd4_peer_inode): fail("FD4 audit phase ABA")

    def _audit_and_admit(self, mirror: PChildMirror) -> None:
        child=mirror.child; session=mirror.session; outer=mirror.outer_pid
        if mirror.fdset=="STDIO_SOURCE_ROOT_BARRIER":
            authorization=self.member_authorizations.get(child)
            if authorization is None or authorization[1]!=mirror.target or authorization[2]!=mirror.purpose: fail("FD9 creation authorization")
        self._audit_live_slots(mirror,0)
        if child in self.auth.peers:
            if mirror.fd4_inode<=0 or mirror.fd4_peer_inode<=0: fail("FD4 audit evidence absent")
            self.auth.attach_pid(child,outer,mirror.inner_pid,mirror.fd4_inode)
        self.control.send(f"CHILD_ADMITTED session={session} child={child} admission={mirror.admission}",str(child))

    def _source_ready(self, record: str) -> None:
        values=parse_exact(record,"SOURCE_READY",(("session",r"[0-9]+"),("child",r"[1-9][0-9]*"),("admission",r"[A-Za-z0-9_:]+"),("fdset",r"[A-Z0-9_]+")))
        child=int(values["child"]); mirror=self.children.get(child)
        if mirror is None or mirror.source_ready or values["admission"]!=mirror.admission or values["fdset"]!=mirror.fdset: fail("source ready join")
        if self.pending_signal: return
        self._audit_live_slots(mirror,1)
        mirror.source_ready=True; self.control.send(f"START session={mirror.session} child={child} admission={mirror.admission}",str(child))

    def _object_registered(self, record: str, acknowledge: bool=True) -> None:
        values=parse_exact(record,"OBJECT_REGISTERED",(("session",r"[0-9]+"),("handle",r"[1-9][0-9]*"),("kind",r"(?:ROOT_PARENT|ROOT|ROOT_MEMBER|LOCK_PARENT|LOCK|LOCK_MEMBER)"),("dev",r"[0-9]+"),("ino",r"[1-9][0-9]*")))
        handle=int(values["handle"])
        if handle in self.objects or handle in self.released_objects: fail("duplicate object")
        identity=ObjectIdentity(handle,int(values["session"]),values["kind"],int(values["dev"]),int(values["ino"])); self.objects[handle]=identity
        process=openat2(self.proc_root,str(self.guardian_pid),OPEN_PATH_DIR)
        try:
            fd_directory=openat2(process,"fd",OPEN_PATH_DIR)
            try:
                matches=[]
                for name in os.listdir(fd_directory):
                    if re.fullmatch(r"[0-9]+",name) is None: fail("guardian fd basename")
                    try: observed=os.stat(name,dir_fd=fd_directory,follow_symlinks=True)
                    except FileNotFoundError: fail("guardian fd ABA")
                    if (observed.st_dev,observed.st_ino)==(identity.dev,identity.ino): matches.append(int(name))
                if len(matches)!=1: fail("object validation FD cardinality")
            finally: os.close(fd_directory)
        finally: os.close(process)
        if identity.kind=="ROOT_MEMBER":
            pending=[child for child in self.creator_reaped if self.children[child].session==identity.session]
            if len(pending)==1:
                child=pending[0]; root,status,count=self.creator_reaped[child]; self.creator_reaped[child]=(root,status,count+1)
        if acknowledge: self.control.send(record.replace("OBJECT_REGISTERED ","OBJECT_REGISTERED_ACK ",1),str(handle))

    def _member_ledger_closed(self, record: str) -> None:
        values=parse_exact(record,"MEMBER_LEDGER_CLOSED",(("session",r"[0-9]+"),("child",r"[1-9][0-9]*"),("root",r"[1-9][0-9]*"),("count",r"[0-9]+")))
        child=int(values["child"]); authorization=self.member_authorizations.get(child); reaped=self.creator_reaped.get(child)
        if authorization is None or reaped is None or authorization[0]!=int(values["root"]) or reaped!=(int(values["root"]),self.children[child].status,int(values["count"])): fail("creator ledger join")
        count=int(values["count"])
        if (self.children[child].status==0 and count!=9) or count>9: fail("creator ledger cardinality")
        self.member_authorizations.pop(child); self.creator_reaped.pop(child)
        self.control.send(record.replace("MEMBER_LEDGER_CLOSED ","MEMBER_LEDGER_ACK ",1),str(child))

    def _object_released(self, record: str) -> None:
        values=parse_exact(record,"OBJECT_RELEASED",(("session",r"[0-9]+"),("handle",r"[1-9][0-9]*"),("kind",r"(?:ROOT_PARENT|ROOT|ROOT_MEMBER|LOCK_PARENT|LOCK|LOCK_MEMBER)"),("dev",r"[0-9]+"),("ino",r"[1-9][0-9]*")))
        handle=int(values["handle"]); identity=self.objects.pop(handle,None)
        if identity is None or (identity.session,identity.kind,identity.dev,identity.ino)!=(int(values["session"]),values["kind"],int(values["dev"]),int(values["ino"])): fail("object release join")
        self.released_objects[handle]=identity

    def _reaped(self, record: str) -> None:
        try: values=parse_exact(record,"CHILD_REAPED",(("session",r"[0-9]+"),("child",r"[1-9][0-9]*"),("status",r"[0-9]+")))
        except (PossessionFailure,ValueError): self.retain_failure("CHILD_REAPED_RECORD",record); raise
        child=int(values["child"]); mirror=self.children.get(child)
        if mirror is None or mirror.reaped or values["session"]!=str(mirror.session):
            self.retain_failure("CHILD_REAPED_RECORD",record); fail("child reap state")
        if int(values["status"])!=mirror.expected_status:
            peer=self.auth.peers.get(child)
            if peer is not None: self.auth._post_finalize_failure(peer,"REQUESTER_EXIT_STATUS",record)
            self.retain_failure("REQUESTER_EXIT_STATUS",record); fail("child reap status")
        probe=select.poll(); probe.register(mirror.pidfd,select.POLLIN|select.POLLHUP)
        if not probe.poll(0): self.retain_failure("REQUESTER_PROCESS_PRESENT",record); fail("P child pidfd evidence")
        peer=self.auth.peers.get(child)
        if peer is not None and (peer.state!="FD5_EOF_OBSERVED" or not peer.eof_seen):
            self.auth._post_finalize_failure(peer,"CHILD_REAPED_RECORD",record); self.retain_failure("CHILD_REAPED_RECORD",record)
            fail("auth reap tombstone")
        mirror.status=int(values["status"]); mirror.reap_record=record
        try: close_proved(mirror.pidfd); mirror.pidfd=-1; mirror.pidfd_state="CLOSED_PROVED"; mirror.pidfd_ledger.state="CLOSED_PROVED"
        except (PossessionFailure,OSError):
            if peer is not None: self.auth._post_finalize_failure(peer,"PIDFD_ABSENCE",record)
            self.retain_failure("PIDFD_ABSENCE",record); raise
        if child in self.member_authorizations:
            root,_target,_purpose=self.member_authorizations[child]; self.creator_reaped[child]=(root,mirror.status,0)
        if peer is not None:
            endpoint_fd=peer.endpoint.fileno()
            try: peer.endpoint.close(); immediate_ebadf(endpoint_fd)
            except (PossessionFailure,OSError):
                self.auth._post_finalize_failure(peer,"FD5_PEER_ABSENCE",record); self.retain_failure("FD5_PEER_ABSENCE",record); raise
            peer.state="CHILD_REAPED_VALIDATED"
        mirror.reaped=True
        acknowledgment=record.replace("CHILD_REAPED ","CHILD_REAPED_ACK ",1); mirror.reap_ack=acknowledgment
        try: self.control.send(acknowledgment,str(child))
        except (PossessionFailure,OSError):
            if peer is not None: self.auth._post_finalize_failure(peer,"CHILD_REAPED_ACK_SEND",acknowledgment)
            self.retain_failure("CHILD_REAPED_ACK_SEND",acknowledgment); raise
        if peer is not None:
            peer.state="CHILD_REAPED_ACK_SENT"; peer.state="AUTH_REAP_ACK_SENT"

    def handle_control(self, record: str) -> None:
        token=record.partition(" ")[0]
        if token in ("CHILD_REGISTERED","CHILD_REGISTERED_AUDITED"): self._registered(record)
        elif token=="SOURCE_READY": self._source_ready(record)
        elif token=="AUDIT_FD_REQUEST":
            values=parse_exact(record,"AUDIT_FD_REQUEST",(("session",r"[0-9]+"),("child",r"[1-9][0-9]*"),("target",r"(?:TOP_TEST_CONTROLS|COPIED_REPRODUCE)"),("role",r"(?:TOP_TEST_RUNNER|REQUESTER)"),("owner",r"[A-Za-z0-9_]+"),("purpose",r"NONE")))
            if self.pending_signal: return
            child=int(values["child"]); session=int(values["session"])
            if session==0:
                if (child,values["target"],values["role"],values["owner"])!=(6,"TOP_TEST_CONTROLS","TOP_TEST_RUNNER","SUITE_173"): fail("top audit allocation tuple")
            else:
                parents=[peer for peer in self.auth.peers.values() if peer.session==session and peer.state=="ACTIVE_AUTHORIZED" and peer.method==values["owner"]]
                if len(parents)!=1 or (values["target"],values["role"])!=("COPIED_REPRODUCE","REQUESTER"): fail("method audit allocation tuple")
            transit,audit=self.auth.create_endpoint(child)
            try: self.control.send_fd(f"AUDIT_FD_GRANTED session={session} child={child} audit={audit}",transit)
            finally: close_proved(transit)
        elif token=="AUDITED_RPC_ACCEPTED": self._audited_rpc_accepted(record)
        elif token=="OBJECT_REGISTERED": self._object_registered(record,not self.pending_signal)
        elif token=="OBJECT_RELEASED": self._object_released(record)
        elif token=="MEMBER_CREATE_AUTHORIZED": self._member_authorized(record,not self.pending_signal)
        elif token=="MEMBER_LEDGER_CLOSED":
            if not self.pending_signal: self._member_ledger_closed(record)
        elif token=="LOCK_BOUND":
            values=parse_exact(record,"LOCK_BOUND",(("session",r"0"),("lock",r"[1-9][0-9]*")))
            identity=self.objects.get(int(values["lock"]))
            if identity is None or identity.session!=0 or identity.kind!="LOCK" or "LOCK_BOUND" in self.final_states: fail("lock bound")
            self.final_states.append("LOCK_BOUND")
        elif token=="CHILD_REAPED":
            if not self.pending_signal: self._reaped(record)
        elif token=="CGROUP_PROBE_CHILD": self._cgroup_probe(record)
        elif token=="CGROUP_PROBE_REAPED":
            values=parse_exact(record,"CGROUP_PROBE_REAPED",(("epoch",r"[12]"),)); epoch=int(values["epoch"])
            mirror=self.children.get(epoch)
            if mirror is None or not mirror.reaped or epoch in self.probe_reaped: fail("cgroup probe reap join")
            self.probe_reaped.add(epoch)
            if epoch==2: self.tree.require_empty(self.tree.workers_fd)
        elif token in ("SESSION_AUTH_CREATE_ACCEPTED","SESSION_AUTH_COMMITTED","SESSION_AUTH_ACTIVE_ACK","SESSION_AUTH_ABORTED"):
            if not self.pending_signal: self.auth.handle_control(record)
        elif token=="SESSION_AUTH_TERMINAL_PREPARED":
            if self.pending_signal: return
            terminal_values=parse_exact(record,"SESSION_AUTH_TERMINAL_PREPARED",(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("close_request",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("terminal_template",r"(?:[0-9a-f]{2})+")))
            requester_child=int(terminal_values["requester_child"]); requester=self.children.get(requester_child)
            if requester is None: fail("terminal requester mirror")
            cleanup_ready=(all(identity.session==0 for identity in self.objects.values()) and all(child==requester_child or mirror.reaped for child,mirror in self.children.items())) if requester_child==6 else (not requester.reaped and all(child==requester_child or mirror.session!=requester.session or mirror.reaped for child,mirror in self.children.items()))
            self.auth.grant_terminal(record,cleanup_ready)
        elif token=="FREEZE_REQUEST" and "phase=METHOD" in record: self._method_freeze(record)
        elif token=="CLEANUP_COMMITTED": self._method_cleanup(record)
        elif token in ("FREEZE_REQUEST","KILL_REQUEST","REAPED","CLEANUP_RESULT","SIGNAL_CLEANED","EXIT"): self._global(record)
        else: fail("P control enum "+token)

    def _member_authorized(self, record: str, acknowledge: bool=True) -> None:
        values=parse_exact(record,"MEMBER_CREATE_AUTHORIZED",(("session",r"[0-9]+"),("child",r"[1-9][0-9]*"),("root",r"[1-9][0-9]*"),("target",r"(?:GENERATE_CANONICAL_A|GENERATE_CANONICAL_B|GENERATE_MUTATION)"),("purpose",r"[A-Z0-9_]+"),("basename_set",r"GENERATED_NINE_V1"),("primitive",r"DIRFD_O_CREAT_O_EXCL_O_NOFOLLOW")))
        child=int(values["child"]); root=int(values["root"]); identity=self.objects.get(root)
        mirror=self.children.get(child)
        if child in self.member_authorizations or identity is None or identity.session!=int(values["session"]) or mirror is None or mirror.session!=int(values["session"]) or mirror.target!=values["target"] or mirror.fdset!="STDIO_SOURCE_ROOT_BARRIER": fail("member authorization state")
        self.member_authorizations[child]=(root,values["target"],values["purpose"])
        if acknowledge: self.control.send(f"MEMBER_CREATE_ACK session={values['session']} child={child} root={root} purpose={values['purpose']} basename_set=GENERATED_NINE_V1",str(child))
        self._audit_and_admit(mirror)

    def _audited_rpc_accepted(self, record: str) -> None:
        values=parse_exact(record,"AUDITED_RPC_ACCEPTED",(("requester_session",r"[1-9][0-9]*"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}"),("rpc_inner_pid",r"[1-9][0-9]*"),("rpc_inner_uid",r"0"),("rpc_inner_gid",r"0"),("payload",r"(?:[0-9a-f]{2})+")))
        child=int(values["requester_child"]); peer=self.auth.peers.get(child); requester_mirror=self.children.get(child); key=(int(values["audit"]),int(values["serial"]))
        direct=None if peer is None else peer.audits.get(key); payload=bytes.fromhex(values["payload"])
        outer=parse_exact(payload.decode("ascii"),"AUDITED_SPAWN",(("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}"),("trigger",r"[A-Z0-9_]+"),("core",r"(?:[0-9a-f]{2})+")))
        core=bytes.fromhex(outer["core"])
        parse_exact(core.decode("ascii"),"SPAWN",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("target",r"[A-Z0-9_]+"),("method",r"test_[a-z0-9_]+"),("purpose",r"[A-Z0-9_]+"),("handle",r"[0-9]+")))
        if peer is None or requester_mirror is None or requester_mirror.reaped or not requester_mirror.source_ready or requester_mirror.target not in ("TOP_TEST_CONTROLS","COPIED_REPRODUCE") or peer.state!="ACTIVE_AUTHORIZED" or key in peer.confirmed_audits or peer.session!=int(values["requester_session"]) or peer.expected_inner_pid!=int(values["rpc_inner_pid"]) or direct is None or direct[3]!=payload or direct[2].encode("ascii")!=core or (values["nonce"],values["digest"])!=(direct[0],direct[1]) or (outer["audit"],outer["serial"],outer["nonce"],outer["digest"])!=(values["audit"],values["serial"],values["nonce"],values["digest"]) or sha256(core)!=direct[1]: fail("audited RPC byte join")
        self._audit_live_slots(requester_mirror,2)
        confirmed=f"AUDITED_RPC_CONFIRMED requester_session={peer.session} requester_child={child} audit={key[0]} serial={key[1]} nonce={direct[0]} digest={direct[1]}"
        peer.confirmed_audits.add(key)
        self.control.send(confirmed,f"{key[0]}:{key[1]}")

    def _cgroup_probe(self, record: str) -> None:
        values=parse_exact(record,"CGROUP_PROBE_CHILD",(("epoch",r"[12]"),("inner_pid",r"[1-9][0-9]*")))
        epoch=int(values["epoch"]); mirror=self.children.get(epoch)
        if mirror is None or mirror.target!="CGROUP_PROBE_CHILD" or mirror.role!="PROBE" or mirror.inner_pid!=int(values["inner_pid"]): fail("cgroup probe join")
        if epoch==1:
            self.tree.freeze(self.tree.workers_fd); self.control.send("CGROUP_PROBE_FROZEN epoch=1")
            self.tree.thaw(self.tree.workers_fd); self.control.send("CGROUP_PROBE_THAWED epoch=1")
        elif epoch==2:
            self.tree.kill(self.tree.workers_fd); self.control.send("CGROUP_PROBE_KILLED epoch=2")
        else: fail("cgroup probe action")

    def _prove_frozen_no_references(self, session: int) -> None:
        identities={(identity.dev,identity.ino) for identity in self.objects.values() if identity.session==session}
        live={mirror.outer_pid:mirror for mirror in self.children.values() if not mirror.reaped}
        members=self.tree.members(self.tree.workers_fd)
        if len(members)!=len(set(members)) or set(members)!=set(live): fail("frozen worker membership ledger")
        for pid in members:
            process=openat2(self.proc_root,str(pid),OPEN_PATH_DIR)
            try:
                fd_directory=openat2(process,"fd",OPEN_PATH_DIR)
                try:
                    for name in os.listdir(fd_directory):
                        if re.fullmatch(r"0|[1-9][0-9]*",name) is None: fail("reference fd basename")
                        observed=os.stat(name,dir_fd=fd_directory,follow_symlinks=True)
                        if (observed.st_dev,observed.st_ino) in identities: fail("worker object FD reference")
                finally: os.close(fd_directory)
                for name in ("cwd","root","exe"):
                    observed=os.stat(name,dir_fd=process,follow_symlinks=True)
                    if (observed.st_dev,observed.st_ino) in identities: fail("worker task reference")
                maps=read_regular_at(process,"maps",16*1024*1024).decode("ascii")
                for line in maps.splitlines():
                    fields=line.split(None,5)
                    if len(fields)<5 or re.fullmatch(r"[0-9a-f]+-[0-9a-f]+",fields[0]) is None or re.fullmatch(r"[0-9a-f]+:[0-9a-f]+",fields[3]) is None or re.fullmatch(r"[0-9]+",fields[4]) is None: fail("proc maps grammar")
                    major,minor=(int(value,16) for value in fields[3].split(":")); mapped=(os.makedev(major,minor),int(fields[4]))
                    if mapped in identities and mapped[1]!=0: fail("worker object mapping reference")
            finally: os.close(process)
        if self.tree.events(self.tree.workers_fd).get("frozen")!=1: fail("frozen reference epoch drift")
        repeated=self.tree.members(self.tree.workers_fd)
        if repeated!=members: fail("frozen membership ABA")

    def _method_freeze(self, record: str) -> None:
        values=parse_exact(record,"FREEZE_REQUEST",(("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("phase",r"METHOD")))
        handle=int(values["handle"]); session=int(values["session"]); identity=self.objects.get(handle)
        key=(session,handle)
        if identity is None or identity.session!=session or key in self.method_epochs: fail("method freeze object")
        active=[child for child in self.children.values() if child.session==session and not child.reaped]
        if any(child.target not in ("TOP_TEST_CONTROLS","COPIED_REPRODUCE") for child in active): fail("method child references")
        self.freeze_epoch+=1; epoch=self.freeze_epoch; self.method_epochs[key]=epoch; self.tree.freeze(self.tree.workers_fd)
        for mirror in sorted(self.children.values(),key=lambda value:value.child):
            if not mirror.reaped and mirror.target in ("TOP_TEST_CONTROLS","COPIED_REPRODUCE"): self._audit_live_slots(mirror,2)
        self._prove_frozen_no_references(session)
        self.control.send(f"FROZEN_NOREFS session={session} handle={handle} phase=METHOD epoch={epoch}")

    def _method_cleanup(self, record: str) -> None:
        values=parse_exact(record,"CLEANUP_COMMITTED",(("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("epoch",r"[1-9][0-9]*")))
        key=(int(values["session"]),int(values["handle"])); epoch=self.method_epochs.get(key)
        if epoch!=int(values["epoch"]) or int(values["handle"]) in self.objects or any(identity.session==int(values["session"]) for identity in self.objects.values()): fail("cleanup before object release")
        self.tree.thaw(self.tree.workers_fd)
        self.control.send(f"THAWED session={values['session']} handle={values['handle']} epoch={epoch}")
        self.method_epochs.pop(key)
        for object_handle,identity in tuple(self.released_objects.items()):
            if identity.session==int(values["session"]): self.released_objects.pop(object_handle)

    def _signal_reconcile_children(self) -> None:
        if not self.pending_signal: fail("signal reap without pending signal")
        for child,mirror in sorted(self.children.items()):
            if mirror.reaped: continue
            probe=select.poll(); probe.register(mirror.pidfd,select.POLLIN|select.POLLHUP)
            if not probe.poll(0): fail("signal child still present")
            try: os.stat(str(mirror.outer_pid),dir_fd=self.proc_root,follow_symlinks=False)
            except FileNotFoundError: pass
            else: fail("signal child proc remains")
            close_proved(mirror.pidfd); mirror.pidfd=-1; mirror.pidfd_state="CLOSED_PROVED"; mirror.pidfd_ledger.state="CLOSED_PROVED"; mirror.status=128+signal.SIGKILL; mirror.reaped=True
            peer=self.auth.peers.get(child)
            if peer is not None:
                endpoint_fd=peer.endpoint.fileno()
                if endpoint_fd>=0:
                    peer.endpoint.close(); immediate_ebadf(endpoint_fd)
                self.auth._retain_failure(peer,"GLOBAL_FINAL_PROOF",peer.state,"SIGNAL_REAP")
                peer.state="AUTH_REAP_FAILED_TOMBSTONE"
        self.member_authorizations.clear(); self.creator_reaped.clear()

    def _global(self, record: str) -> None:
        token=record.partition(" ")[0]
        if token=="FREEZE_REQUEST":
            values=parse_exact(record,"FREEZE_REQUEST",(("session",r"0"),("handle",r"0"),("phase",r"FINAL")))
            successful_auth=all(peer.state=="AUTH_REAP_ACK_SENT" for peer in self.auth.peers.values())
            signal_auth=bool(self.pending_signal)
            if self.global_phase!=0 or (not successful_auth and not signal_auth) or (self.method_epochs and not signal_auth): fail("global freeze duplicate")
            self.freeze_epoch+=1; self.final_epoch=self.freeze_epoch; self.final_cleanup_expected=len(self.objects)+len(self.released_objects)+1
            if self.method_epochs:
                if self.tree.events(self.tree.workers_fd).get("frozen")!=1: fail("signal inherited freeze")
                self.method_epochs.clear()
            else: self.tree.freeze(self.tree.workers_fd)
            self.final_states.append("FROZEN_FINAL"); self.control.send(f"FROZEN_FINAL session=0 handle=0 phase=FINAL epoch={self.final_epoch}")
            self.global_phase=1
        elif token=="KILL_REQUEST":
            values=parse_exact(record,"KILL_REQUEST",(("session",r"0"),("epoch",str(self.final_epoch))))
            if self.global_phase!=1 or self.final_states[-1:]!=["FROZEN_FINAL"]: fail("global FINAL order")
            self.tree.kill(self.tree.workers_fd); self.final_states.append("KILL_ISSUED"); self.control.send(f"KILL_ISSUED session=0 epoch={self.final_epoch}")
            self.global_phase=2
        elif token=="REAPED":
            parse_exact(record,"REAPED",(("session",r"0"),("epoch",str(self.final_epoch))))
            if self.global_phase!=2 or self.final_states[-1:]!=["KILL_ISSUED"]: fail("global reap ledger")
            if self.pending_signal: self._signal_reconcile_children()
            if any(not value.reaped for value in self.children.values()): fail("global child reap ledger")
            self.final_states.append("REAPED"); self.tree.require_empty(self.tree.workers_fd); self.control.send(f"CGROUP_EMPTY session=0 epoch={self.final_epoch}"); self.final_states.append("CGROUP_EMPTY")
            self.global_phase=4
        elif token=="CLEANUP_RESULT":
            values=parse_exact(record,"CLEANUP_RESULT",(("session",r"0"),("handle",r"[0-9]+"),("outcome",OUTCOME_RE)))
            if self.global_phase!=4: fail("cleanup result order")
            handle=int(values["handle"])
            if handle in self.final_cleanup_reported or values["outcome"] in ("UNSET","ERROR","CRASH_TEARDOWN") or (handle!=0 and handle not in self.released_objects): fail("cleanup result join")
            if handle!=0: self.released_objects.pop(handle)
            if handle==0:
                aggregate=combine_outcomes(self.cleanup_outcomes or ("ABSENT",))
                if values["outcome"]!=aggregate: fail("terminal cleanup aggregate")
                self.final_outcome=aggregate
            else: self.cleanup_outcomes.append(values["outcome"])
            self.final_cleanup_reported.add(handle)
            self.cleanup_results+=1; self.final_states.append("CLEANUP_RESULT")
        elif token=="SIGNAL_CLEANED":
            values=parse_exact(record,"SIGNAL_CLEANED",(("signo",str(self.pending_signal)),("outcome",OUTCOME_RE)))
            if self.global_phase!=4 or not self.pending_signal or self.signal_cleaned or self.cleanup_results!=self.final_cleanup_expected or values["outcome"]!=self.final_outcome: fail("signal clean order")
            self.signal_cleaned=True; self.final_states.append("SIGNAL_CLEANED")
        elif token=="EXIT":
            values=parse_exact(record,"EXIT",(("status",r"0"),("outcome",OUTCOME_RE)))
            terminal_order=(self.signal_cleaned and self.final_states[-1:]==["SIGNAL_CLEANED"]) if self.pending_signal else (not self.signal_cleaned and self.final_states[-1:]==["CLEANUP_RESULT"])
            if self.global_phase!=4 or self.cleanup_results!=self.final_cleanup_expected or len(self.final_cleanup_reported)!=self.final_cleanup_expected or self.objects or self.released_objects or self.member_authorizations or not terminal_order or values["outcome"]!=self.final_outcome: fail("global exit evidence")
            self.done=True

    def run(self) -> None:
        poller=select.poll(); poller.register(self.control.sock,select.POLLIN|select.POLLHUP|select.POLLERR)
        poller.register(self.signal_fd,select.POLLIN|select.POLLERR)
        registered_peers: set[int]=set()
        while not self.done:
            for child,peer in self.auth.peers.items():
                endpoint_fd=peer.endpoint.fileno()
                if endpoint_fd>=0 and endpoint_fd not in registered_peers:
                    poller.register(peer.endpoint,select.POLLIN|select.POLLHUP|select.POLLERR); registered_peers.add(endpoint_fd)
            events=poller.poll()
            # Kernel-authenticated requester EOF/receipts have precedence over a later CHILD_REAPED control packet.
            for fd,event in sorted(events,key=lambda item:(item[0]==self.control.sock.fileno(),item[0])):
                if fd==self.signal_fd:
                    self.consume_signalfd()
                elif fd==self.control.sock.fileno():
                    if event&(select.POLLHUP|select.POLLERR): self.control_failure("CONTROL_EOF_EARLY"); fail("P/G control failure")
                    try: incoming=self.control.receive()
                    except (PossessionFailure,OSError): self.control_failure("CONTROL_EOF_EARLY"); raise
                    try: self.handle_control(incoming)
                    except (PossessionFailure,OSError,ValueError,UnicodeError):
                        token=incoming.partition(" ")[0]
                        cause="POST_ACK_D_M1_RECORD" if token in D_M1_FORMS else ("EXIT_RECORD" if token=="EXIT" else "GLOBAL_FINAL_RECORD")
                        self.control_failure(cause,incoming); raise
                else:
                    peers=[peer for peer in self.auth.peers.values() if peer.endpoint.fileno()==fd]
                    if len(peers)!=1: fail("FD5 poll join")
                    peer=peers[0]
                    if self.pending_signal:
                        poller.unregister(fd); registered_peers.remove(fd); continue
                    if peer.state=="ACTIVE_PENDING": continue
                    self.auth.handle(peer)
                    if peer.state=="FD5_EOF_OBSERVED":
                        poller.unregister(fd); registered_peers.remove(fd)

    def dispose_control_after_exit(self) -> None:
        if not self.done: fail("control disposal before EXIT")
        packet,ancillary,flags,_address=self.control.sock.recvmsg(1,1)
        if packet or ancillary or flags: fail("post-EXIT control disposal")
        control_fd=self.control.sock.fileno(); self.control.sock.close(); immediate_ebadf(control_fd)


@dataclass(frozen=True)
class RPCFrame:
    packet: bytes
    record: str
    pid: int
    uid: int
    gid: int


def rpc_receive(endpoint: socket.socket, expected_pid: int) -> RPCFrame|None:
    packet,ancillary,flags,_address=endpoint.recvmsg(MAX_FRAME+5,socket.CMSG_SPACE(struct.calcsize("3i")))
    if not packet:
        if ancillary or flags: fail("FD4 EOF ancillary")
        return None
    credentials=[value for value in ancillary if value[0]==socket.SOL_SOCKET and value[1]==socket.SCM_CREDENTIALS]
    if len(ancillary)!=1 or len(credentials)!=1 or len(credentials[0][2])!=struct.calcsize("3i") or flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(packet)<5: fail("FD4 packet")
    pid,uid,gid=struct.unpack("3i",credentials[0][2])
    if (pid,uid,gid)!=(expected_pid,0,0): fail("FD4 kernel credential")
    size=struct.unpack(">I",packet[:4])[0]; payload=packet[4:]
    if size==0 or size>MAX_FRAME or len(payload)!=size or b"\x00" in payload or b"\n" in payload or not payload.isascii(): fail("FD4 frame")
    return RPCFrame(packet,payload.decode("ascii"),pid,uid,gid)


def rpc_send(endpoint: socket.socket, record: str) -> bytes:
    payload=record.encode("ascii")
    if not payload or len(payload)>MAX_FRAME or b"\x00" in payload or b"\n" in payload: fail("FD4 reply")
    packet=struct.pack(">I",len(payload))+payload
    if endpoint.send(packet)!=len(packet): fail("FD4 reply short")
    return packet


def rpc_send_packet(endpoint: socket.socket, packet: bytes) -> None:
    if len(packet)<5 or len(packet)-4!=struct.unpack(">I",packet[:4])[0] or len(packet)-4>MAX_FRAME or b"\x00" in packet[4:] or b"\n" in packet[4:] or not packet[4:].isascii(): fail("FD4 raw reply")
    if endpoint.send(packet)!=len(packet): fail("FD4 raw reply short")


@dataclass
class GAuthState:
    child: int
    state: str="NO_SESSION"
    audit: int=0
    auth_serial: int=0
    auth: int=0
    session: int=0
    request: int=0
    registration_digest: str=""
    method: str=""
    trigger: str=""
    owner: str=""
    fd4_inode: int=0
    guardian_peer_inode: int=0
    rpc_inner_pid: int=0
    create_identity: bytes=b""
    create_template: bytes=b""
    create_commitment: str=""
    create_frame: bytes=b""
    first_create_consumed: bool=False
    create_cap: str=""
    reply_nonce: str=""
    created: bytes=b""
    created_digest: str=""
    active_identity: bytes=b""
    active_cap_commitment: str=""
    active_cap: str=""
    terminal_cap: str=""
    terminal_cap_digest: str=""
    terminal_request: int=0
    terminal_outcome: str=""
    terminal_template: bytes=b""
    terminal_frame: bytes=b""
    terminal_reply_digest: str=""
    terminal_full_send: bool=False
    first_failure: str=""
    failure_state: str=""
    failure_record_sha256: str=""
    finalized_ack_complete: bool=False
    fd4_eof_observed: bool=False
    requester_status: int=-1
    child_reaped_record: str=""
    child_reaped_ack: str=""

    def retain_failure(self, cause: str, record: str="") -> None:
        if cause not in AUTH_REASONS|V7_TERMINAL_CAUSES|V8_FAILURE_CAUSES: fail("G failure cause")
        if not self.first_failure:
            self.first_failure=cause; self.failure_state=self.state
            self.failure_record_sha256=sha256(record.encode("ascii")) if record else sha256(b"")

    def post_finalize_failure(self, cause: str, record: str="") -> None:
        self.retain_failure(cause,record); self.state="POST_FINALIZE_FAILED"

    def complete_failure_containment(self) -> None:
        if self.state=="POST_FINALIZE_FAILED": self.state="AUTH_REAP_FAILED_TOMBSTONE"


class GuardianAuthentication:
    def __init__(self, channel: GuardianChannel) -> None:
        self.channel=channel; self.states: dict[int,GAuthState]={}; self.channel.failure_hook=self.control_failure

    def control_failure(self, material: bytes) -> None:
        payload=material
        if len(material)>=4 and struct.unpack(">I",material[:4])[0]==len(material)-4: payload=material[4:]
        try: record=payload.decode("ascii")
        except UnicodeError: record=""
        match=re.search(r"(?:^| )requester_child=([1-9][0-9]*)(?: |$)",record)
        selected=[self.states[int(match.group(1))]] if match is not None and int(match.group(1)) in self.states else list(self.states.values())
        for state in selected:
            if state.state in ("FINALIZED_AWAITING_REAP","REQUESTER_REAPED","CHILD_REAPED_SENT","CHILD_REAPED_ACKED"):
                state.post_finalize_failure("POST_ACK_D_M1_RECORD" if record.partition(" ")[0] in D_M1_FORMS else "CONTROL_EOF_EARLY",record)
            elif state.state=="AUTH_REAP_RECONCILED":
                state.retain_failure("GLOBAL_FINAL_RECORD",record); state.state="GLOBAL_FAILED_TERMINAL"
            elif state.state not in ("NO_SESSION","FAILED_TOMBSTONE","AUTH_REAP_FAILED_TOMBSTONE"):
                state.retain_failure("CONTROL_EOF",record); state.state="FAILED_TOMBSTONE"

    def state(self, child: int) -> GAuthState:
        if child not in self.states: self.states[child]=GAuthState(child)
        return self.states[child]

    def signal_containment(self, signo: int) -> None:
        material=f"SIGNAL_PENDING signo={signo}"
        for state in self.states.values():
            if state.state in ("FINALIZED_AWAITING_REAP","REQUESTER_REAPED","CHILD_REAPED_SENT","CHILD_REAPED_ACKED","AUTH_REAP_RECONCILED","POST_FINALIZE_FAILED"):
                state.post_finalize_failure("GLOBAL_FINAL_PROOF",material); state.complete_failure_containment()
            elif state.state not in ("FAILED_TOMBSTONE","AUTH_REAP_FAILED_TOMBSTONE"):
                state.retain_failure("SESSION_CLOSE_OR_CLEANUP",material); state.state="FAILED_TOMBSTONE"

    def handles(self, record: str) -> bool:
        return record.partition(" ")[0] in D_M1_FORMS

    @staticmethod
    def _tuple(state: GAuthState) -> str:
        return f"requester_session=0 requester_child={state.child} audit={state.audit} auth_serial={state.auth_serial} auth={state.auth} session={state.session}"

    @staticmethod
    def _join(state: GAuthState, values: dict[str,str]) -> bool:
        return (values["requester_child"],values["audit"],values["auth_serial"],values["auth"],values["session"])==(str(state.child),str(state.audit),str(state.auth_serial),str(state.auth),str(state.session))

    @staticmethod
    def _phase(state: GAuthState) -> str:
        phase={
            "CREATE_ARMED":"CREATE_GRANTED","CREATE_HELD":"CREATE_ACCEPTED","INACTIVE_REPLY_PENDING":"CREATE_ACCEPTED",
            "INACTIVE":"INACTIVE_COMMITTED","ACTIVE_ARMED":"ACTIVE_PENDING","ACTIVE_AUTHORIZED":"ACTIVE",
            "CLOSING":"CLOSING","TERMINAL_PREPARED":"CLOSING","TERMINAL_GRANTED":"CLOSING",
            "TERMINAL_REPLY_SENT":"CLOSING","FINALIZE_RECEIVED":"CLOSING",
        }.get(state.state)
        if phase is None or phase not in AUTH_PHASES: fail("G auth phase state")
        return phase

    def _abort_from_g(self, state: GAuthState, phase: str, reason: str) -> None:
        if phase not in AUTH_PHASES or reason not in AUTH_REASONS or phase!=self._phase(state): fail("G abort mapping")
        state.retain_failure(reason); state.state="ABORTING"
        try: self.channel.send(f"SESSION_AUTH_ABORTED {self._tuple(state)} phase={phase} reason={reason} outcome=UNSET")
        finally: state.state="FAILED_TOMBSTONE"

    def handle(self, record: str) -> None:
        token=record.partition(" ")[0]
        if token=="SESSION_AUTH_CREATE_GRANTED":
            fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("registration_digest",r"[0-9a-f]{64}"),("create_commitment",r"[0-9a-f]{64}"),("template",r"(?:[0-9a-f]{2})+"),("fd4_endpoint_inode",r"[1-9][0-9]*"),("rpc_inner_pid",r"[1-9][0-9]*"),("rpc_inner_uid",r"0"),("rpc_inner_gid",r"0"))
            values=parse_exact(record,token,fields); state=self.state(int(values["requester_child"]))
            if state.state!="NO_SESSION": fail("G auth create state")
            template=bytes.fromhex(values["template"])
            match=re.fullmatch(rb"SESSION_CREATE request=([1-9][0-9]*) session=([1-9][0-9]*) method=(test_[a-z0-9_]+) trigger=([A-Z0-9_]+) owner=([A-Z0-9_]+) auth=([1-9][0-9]*) create_cap=\{CREATE_CAP64\}",template)
            if match is None or (match.group(1).decode(),match.group(2).decode(),match.group(6).decode())!=(values["request"],values["session"],values["auth"]): fail("G create template")
            state.audit=int(values["audit"]); state.auth_serial=int(values["auth_serial"]); state.auth=int(values["auth"]); state.session=int(values["session"]); state.request=int(values["request"])
            state.registration_digest=values["registration_digest"]; state.create_commitment=values["create_commitment"]; state.create_template=template
            state.method=match.group(3).decode(); state.trigger=match.group(4).decode(); state.owner=match.group(5).decode(); state.fd4_inode=int(values["fd4_endpoint_inode"]); state.rpc_inner_pid=int(values["rpc_inner_pid"])
            state.create_identity=f"requester_child={state.child} audit={state.audit} auth_serial={state.auth_serial} auth={state.auth} session={state.session} request={state.request} method={state.method} trigger={state.trigger} owner={state.owner} fd4_endpoint_inode={state.fd4_inode} rpc_inner_pid={state.rpc_inner_pid} rpc_inner_uid=0 rpc_inner_gid=0".encode("ascii")
            state.state="CREATE_ARMED"
        elif token=="SESSION_AUTH_COMMIT":
            self._commit(record)
        elif token=="SESSION_AUTH_ACTIVE":
            fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("active_cap_commitment",r"[0-9a-f]{64}"),("created_digest",r"[0-9a-f]{64}"))
            values=parse_exact(record,token,fields); state=self.state(int(values["requester_child"]))
            if state.state!="INACTIVE" or not self._join(state,values) or values["request"]!=str(state.request) or values["created_digest"]!=state.created_digest: fail("G auth active")
            state.active_cap_commitment=values["active_cap_commitment"]
            state.active_identity=f"requester_child={state.child} audit={state.audit} auth_serial={state.auth_serial} auth={state.auth} session={state.session} method={state.method} trigger={state.trigger} owner={state.owner} fd4_endpoint_inode={state.fd4_inode}".encode("ascii")
            state.state="ACTIVE_ARMED"
            self.channel.send(f"SESSION_AUTH_ACTIVE_ACK {self._tuple(state)} request={state.request} active_cap_commitment={state.active_cap_commitment} created_digest={state.created_digest}")
            state.state="ACTIVE_AUTHORIZED"
        elif token=="SESSION_AUTH_ABORT":
            fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("phase",r"(?:REGISTERED|CREATE_GRANTED|CREATE_ACCEPTED|INACTIVE_COMMITTED|ACTIVATION_JOINED|ACTIVE_RECEIPT_SENT|ACTIVE_PENDING|ACTIVE|CLOSING)"),("reason",r"(?:RECEIPT_SEND|REQUESTER_EOF|CREATE_MISMATCH|CREATE_ACCEPTED_SEND|COMMIT_SEND|PRIVATE_CONSTRUCTION|CREATED_SEND|COMMITTED_SEND|ACTIVATION_MISMATCH|ACTIVE_RECEIPT_SEND|ACTIVE_SEND|ACTIVE_ACK_SEND|PREACTIVE_OPERATION|ACTIVE_OPERATION_MISMATCH|SESSION_CLOSE_FAILURE|CONTROL_EOF)"))
            values=parse_exact(record,token,fields); state=self.state(int(values["requester_child"]))
            if not self._join(state,values) or state.state in ("FINALIZED_AWAITING_REAP","REQUESTER_REAPED","CHILD_REAPED_SENT","CHILD_REAPED_ACKED","AUTH_REAP_RECONCILED","POST_FINALIZE_FAILED","AUTH_REAP_FAILED_TOMBSTONE","FAILED_TOMBSTONE") or values["phase"]!=self._phase(state): fail("G abort join")
            state.retain_failure(values["reason"],record); state.state="ABORTING"
            try: self.channel.send(record.replace("SESSION_AUTH_ABORT ","SESSION_AUTH_ABORTED ",1)+" outcome=UNSET")
            finally: state.state="FAILED_TOMBSTONE"
        elif token=="SESSION_AUTH_TERMINAL_GRANTED":
            fail("terminal grant outside prepared wait")
        elif token=="SESSION_AUTH_FINALIZE":
            fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("close_request",r"[1-9][0-9]*"),("outcome",OUTCOME_RE),("terminal_cap_sha256",r"[0-9a-f]{64}"),("reply_digest",r"[0-9a-f]{64}"))
            values=parse_exact(record,token,fields); state=self.state(int(values["requester_child"]))
            if state.state!="TERMINAL_REPLY_SENT" or not state.terminal_full_send or not self._join(state,values) or (int(values["close_request"]),values["outcome"],values["terminal_cap_sha256"],values["reply_digest"])!=(state.terminal_request,state.terminal_outcome,state.terminal_cap_digest,state.terminal_reply_digest): fail("G finalize")
            state.state="FINALIZE_RECEIVED"
            self.channel.send(f"SESSION_AUTH_FINALIZED_ACK {self._tuple(state)} close_request={state.terminal_request} outcome={state.terminal_outcome} terminal_cap_sha256={state.terminal_cap_digest} reply_digest={state.terminal_reply_digest}")
            state.finalized_ack_complete=True; state.state="FINALIZED_AWAITING_REAP"
        else: fail("G D-M1 direction")

    def _commit(self, record: str) -> None:
        fields=(("requester_session",r"0"),("requester_child",r"[1-9][0-9]*"),("audit",r"(?:0|[1-9][0-9]*)"),("auth_serial",r"(?:0|[1-9][0-9]*)"),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("request",r"[1-9][0-9]*"),("reply_nonce",r"[0-9a-f]{64}"),("created",r"(?:[0-9a-f]{2})+"))
        values=parse_exact(record,"SESSION_AUTH_COMMIT",fields); state=self.state(int(values["requester_child"]))
        created=bytes.fromhex(values["created"]); expected=f"SESSION_CREATED request={state.request} session={state.session} reply_nonce={values['reply_nonce']}".encode("ascii")
        if state.state!="CREATE_HELD" or not self._join(state,values) or values["request"]!=str(state.request) or created!=expected: fail("G auth commit")
        state.reply_nonce=values["reply_nonce"]; state.created=created; state.created_digest=sha256(created); state.state="INACTIVE_REPLY_PENDING"

    def accept_create(self, child: int, frame: RPCFrame, endpoint_inode: int) -> bytes:
        state=self.state(child)
        if state.state!="CREATE_ARMED" or state.first_create_consumed: fail("first FD4 create state")
        state.first_create_consumed=True
        values=parse_exact(frame.record,"SESSION_CREATE",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("method",r"test_[a-z0-9_]+"),("trigger",r"[A-Z0-9_]+"),("owner",r"[A-Z0-9_]+"),("auth",r"[1-9][0-9]*"),("create_cap",r"[0-9a-f]{64}")))
        if endpoint_inode<=0 or endpoint_inode==state.fd4_inode or (frame.pid,frame.uid,frame.gid)!=(state.rpc_inner_pid,0,0) or (values["request"],values["session"],values["method"],values["trigger"],values["owner"],values["auth"])!=(str(state.request),str(state.session),state.method,state.trigger,state.owner,str(state.auth)) or v7_bind("P15R-CREATE-COMMITMENT-v7",state.create_identity,frame.packet)!=state.create_commitment: self._abort_from_g(state,"CREATE_GRANTED","CREATE_MISMATCH"); fail("first FD4 create")
        state.guardian_peer_inode=endpoint_inode; state.create_cap=values["create_cap"]; state.create_frame=frame.packet; state.state="CREATE_HELD"
        self.channel.send(f"SESSION_AUTH_CREATE_ACCEPTED {self._tuple(state)} request={state.request} registration_digest={state.registration_digest} create_commitment={state.create_commitment} create_cap={state.create_cap} payload={frame.packet.hex()} fd4_endpoint_inode={state.fd4_inode} rpc_inner_pid={state.rpc_inner_pid} rpc_inner_uid=0 rpc_inner_gid=0")
        commit=self.channel.receive(lambda value:value.partition(" ")[0]=="SESSION_AUTH_COMMIT")
        self._commit(commit)
        return state.created

    def created_sent(self, child: int, packet: bytes) -> None:
        state=self.state(child); expected=struct.pack(">I",len(state.created))+state.created
        if state.state!="INACTIVE_REPLY_PENDING" or packet!=expected: fail("created complete send")
        self.channel.send(f"SESSION_AUTH_COMMITTED {self._tuple(state)} request={state.request} reply_nonce={state.reply_nonce} created={state.created.hex()}")
        state.state="INACTIVE"

    def authorize_active(self, child: int, cap: str) -> None:
        state=self.state(child)
        if state.state!="ACTIVE_AUTHORIZED" or re.fullmatch(r"[0-9a-f]{64}",cap) is None: fail("RPC active state")
        if not state.active_cap:
            if v7_bind("P15R-ACTIVE-COMMITMENT-v7",state.active_identity,bytes.fromhex(cap))!=state.active_cap_commitment:
                self._abort_from_g(state,"ACTIVE","ACTIVE_OPERATION_MISMATCH"); fail("first active capability")
            state.active_cap=cap
        elif state.active_cap!=cap:
            self._abort_from_g(state,"ACTIVE","ACTIVE_OPERATION_MISMATCH"); fail("active capability replay")

    def terminal(self, child: int, request: int, outcome: str) -> bytes:
        state=self.state(child)
        if state.state!="ACTIVE_AUTHORIZED" or not state.active_cap or outcome not in OUTCOMES: fail("terminal not active")
        state.terminal_request=request; state.terminal_outcome=outcome
        state.terminal_template=f"SESSION_CLOSED request={request} session={state.session} outcome={outcome} terminal_cap={{TERMINAL_CAP64}}".encode("ascii")
        state.state="CLOSING"
        self.channel.send(f"SESSION_AUTH_TERMINAL_PREPARED {self._tuple(state)} close_request={request} outcome={outcome} terminal_template={state.terminal_template.hex()}")
        state.state="TERMINAL_PREPARED"
        grant=self.channel.receive(lambda value:value.partition(" ")[0]=="SESSION_AUTH_TERMINAL_GRANTED")
        fields=(("requester_session",r"0"),("requester_child",str(child)),("audit",str(state.audit)),("auth_serial",str(state.auth_serial)),("auth",str(state.auth)),("session",str(state.session)),("close_request",str(request)),("outcome",re.escape(outcome)),("terminal_cap",r"[0-9a-f]{64}"),("reply_digest",r"[0-9a-f]{64}"),("reply",r"(?:[0-9a-f]{2})+"))
        values=parse_exact(grant,"SESSION_AUTH_TERMINAL_GRANTED",fields); packet=bytes.fromhex(values["reply"]); payload=packet[4:]
        expected=f"SESSION_CLOSED request={request} session={state.session} outcome={outcome} terminal_cap={values['terminal_cap']}".encode("ascii")
        digest=sha256(b"P15R-TERMINAL-REPLY-v7 "+packet)
        if len(packet)<5 or struct.unpack(">I",packet[:4])[0]!=len(payload) or payload!=expected or values["reply_digest"]!=digest: fail("terminal grant")
        state.terminal_cap=values["terminal_cap"]; state.terminal_cap_digest=sha256(b"P15R-TERMINAL-CAP-v7 "+bytes.fromhex(state.terminal_cap)); state.terminal_frame=packet; state.terminal_reply_digest=digest; state.state="TERMINAL_GRANTED"
        return packet

    def terminal_sent(self, child: int, packet: bytes) -> None:
        state=self.state(child)
        if state.state!="TERMINAL_GRANTED" or packet is not state.terminal_frame: fail("terminal same-buffer send")
        state.terminal_full_send=True; state.state="TERMINAL_REPLY_SENT"


@dataclass
class MutationReceipt:
    mutation: str
    coordinate: str
    before: str
    after: str
    variant: int

    def bytes(self) -> bytes:
        return (json.dumps({"after":self.after,"before":self.before,"coordinate":self.coordinate,"mutation":self.mutation,"variant":self.variant},sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode("ascii")


@dataclass
class MethodSession:
    session: int
    method: str
    trigger: str
    descriptor: dict[str,object]|None
    lock: int=0
    lock_state: str="UNOWNED"
    lock_tree: OwnedTree|None=None
    lock_socket: socket.socket|None=None
    lock_parent_handle: int=0
    lock_parent_cap: int=-1
    lock_root_handle: int=0
    lock_root_cap: int=-1
    lock_member_handle: int=0
    lock_member_cap: int=-1
    lock_foreign_outcome: str=""
    signal_tree: OwnedTree|None=None
    signal_state: str="UNOWNED"
    signal_pending: int=0
    signal_ledger_session: int=0
    signal_parent_handle: int=0
    signal_parent_cap: int=-1
    signal_root_handle: int=0
    signal_root_cap: int=-1
    signal_member_handle: int=0
    signal_member_cap: int=-1
    signal_acquiring_token: str=""
    signal_foreign_receipt: tuple[int,int,int,int,bytes]|None=None
    handle: int=0
    parent_handle: int=0
    parent_cap: int=-1
    root_cap: int=-1
    member_caps: list[tuple[int,int]]=field(default_factory=list)
    tree: OwnedTree|None=None
    package_path: str=""
    package_relative: str="repository/papers/15-wieferich-ulm-packet-bases"
    result_path: str=""
    result_relative: str="candidate"
    root_purpose: str=""
    receipt: MutationReceipt|None=None
    detector: str=""
    cleaned: bool=False
    closed: bool=False
    foreign_basename: str=""
    foreign_identity: tuple[int,int]|None=None
    foreign_outcome: str=""
    foreign_root_handle: int=0
    foreign_root_cap: int=-1
    foreign_member_handle: int=0
    foreign_member_cap: int=-1
    empty_p25: bool=False
    outcome: str="UNSET"


def canonical_json_bytes(value: object) -> bytes:
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n").encode("utf-8")


def csv_table(data: bytes) -> tuple[list[str],list[list[str]]]:
    import csv,io
    text=data.decode("utf-8"); rows=list(csv.reader(io.StringIO(text,newline=""),strict=True))
    if not rows: fail("mutation CSV")
    return rows[0],rows[1:]


def csv_bytes(header: Sequence[str], rows: Sequence[Sequence[str]], terminal_lf: bool=True) -> bytes:
    import csv,io
    stream=io.StringIO(newline=""); writer=csv.writer(stream,lineterminator="\n",quoting=csv.QUOTE_MINIMAL); writer.writerow(header); writer.writerows(rows)
    data=stream.getvalue().encode("utf-8")
    return data if terminal_lf else data[:-1]


def adopt_generated(tree: OwnedTree, relative_root: str) -> None:
    for name in GENERATED_NAMES: tree.adopt(relative_root+"/"+name if relative_root else name)


def parse_descriptor(encoded: str) -> dict[str,object]:
    try:
        raw=bytes.fromhex(encoded); value=json.loads(raw.decode("utf-8"))
    except (ValueError,UnicodeError,json.JSONDecodeError): fail("mutation descriptor")
    keys={"after","before","coordinate","kind","method","mutation","target","trigger","variant","variants"}
    if not isinstance(value,dict) or set(value)!=keys or canonical_json_bytes(value)!=raw or not all(isinstance(value[name],str) for name in ("after","before","coordinate","kind","method","mutation","target","trigger")) or not all(isinstance(value[name],int) for name in ("variant","variants")): fail("mutation descriptor canonical")
    if value["target"] not in TARGETS or value["trigger"] not in TRIGGERS or not (1<=value["variant"]<=value["variants"]): fail("mutation descriptor values")
    return value


def apply_mutation(session: MethodSession) -> MutationReceipt:
    descriptor=session.descriptor; tree=session.tree
    if descriptor is None or tree is None: fail("mutation session")
    mutation=str(descriptor["mutation"]); coordinate=str(descriptor["coordinate"]); before=str(descriptor["before"]); after=str(descriptor["after"]); kind=str(descriptor["kind"])
    package=session.package_relative; result_prefix=session.result_relative; relative=coordinate.split(":",1)[0]
    if relative.startswith("results/"): target=result_prefix+"/"+relative[len("results/"):]
    elif relative.startswith(("code/","experiments/")): target=package+"/"+relative
    else: target=relative
    def regular(path: str) -> bytes:
        parent,name=path.rsplit("/",1); return read_regular_at(tree.directory(parent),name)
    def replace(path: str, data: bytes) -> None: tree.replace(path,data)
    if kind in ("ARTIFACT","HEADER","ROW_COUNT","ROW_ORDER"):
        header,rows=csv_table(regular(target))
        if kind=="ARTIFACT":
            row_id,field=coordinate.rsplit(":",1)[1].split(".",1); index=header.index(field); matches=[row for row in rows if row[header.index("row_id")]==row_id]
            if len(matches)!=1 or matches[0][index]!=before: fail("artifact before")
            matches[0][index]=after
        elif kind=="HEADER":
            old=coordinate.rsplit("[",1)[1][:-1]; index=header.index(old)
            if header[index]!=before: fail("header before")
            header[index]=after
        elif kind=="ROW_COUNT":
            row_id=coordinate.rsplit("[",1)[1][:-1]; matches=[index for index,row in enumerate(rows) if row[header.index("row_id")]==row_id]
            if len(matches)!=1 or before!="PRESENT" or after!="ABSENT": fail("row-count before")
            rows.pop(matches[0])
        else:
            if len(rows)<2 or ",".join((rows[0][header.index("row_id")],rows[1][header.index("row_id")]))!=before: fail("row-order before")
            rows[0],rows[1]=rows[1],rows[0]
        replace(target,csv_bytes(header,rows))
    elif kind in ("MISSING_ARTIFACT","MISSING_MANIFEST"):
        if before!="REGULAR" or after!="ABSENT": fail("missing transition")
        tree.unlink_owned(target)
    elif kind in ("EXTRA_CSV","EXTRA_FILE"):
        if before!="ABSENT": fail("extra before")
        tree.write(target,b"")
    elif kind=="EXTRA_DIRECTORY":
        if before!="ABSENT": fail("extra directory before")
        tree.directory(target)
    elif kind in ("MANIFEST","SELF_CYCLE","AUTHORITY","DESIGN","REVIEW","GATE","FUTURE_CYCLE","AMBIENT"):
        manifest_path=result_prefix+"/manifest.json"; value=json.loads(regular(manifest_path).decode("utf-8"))
        suffix=coordinate.partition(":")[2]
        if kind=="MANIFEST": value["status"]=after
        elif kind=="SELF_CYCLE": value["self_sha256"]=after
        elif kind=="AUTHORITY": value["authority_bindings"][0]["sha256"]=after
        elif kind=="DESIGN": value["design_lock"]["sha256"]=after
        elif kind=="REVIEW": value["design_review"]["sha256"]=after
        elif kind=="GATE": value["implementation_gate"]["sha256"]=after
        elif kind=="FUTURE_CYCLE": value["result_review"]=json.loads(after)
        elif kind=="AMBIENT": value[suffix]=after
        replace(manifest_path,canonical_json_bytes(value))
    elif kind=="IMPLEMENTATION":
        data=regular(target)
        if before!="EOF": fail("implementation before")
        replace(target,data+bytes.fromhex(after))
    elif kind=="LINK_SYMLINK":
        tree.unlink_owned(target); parent,name=target.rsplit("/",1); os.symlink("target_summary.csv",name,dir_fd=tree.directory(parent)); tree.adopt(target)
    elif kind=="LINK_HARDLINK":
        parent,name=target.rsplit("/",1); alias=name+".method-copy"; parent_fd=tree.directory(parent)
        os.link(name,alias,src_dir_fd=parent_fd,dst_dir_fd=parent_fd,follow_symlinks=False); tree.adopt(parent+"/"+alias)
    elif kind in ("CACHE_PRE","CACHE_POST"):
        cache_path=target; parent,name=cache_path.rsplit("/",1); tree.write(parent+"/"+name,b"")
    elif kind=="CANONICAL":
        if coordinate.endswith(":encoding"):
            value=json.loads(regular(target).decode("utf-8")); replace(target,(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode("utf-8"))
        else:
            header,rows=csv_table(regular(target)); replace(target,csv_bytes(header,rows,terminal_lf=False))
    elif kind in ("RECURSIVE_ENTRY","CONCURRENT_LOCK","CLI_REPAIR","CLEANUP","NONEMPTY"):
        if kind=="NONEMPTY": tree.write(result_prefix+"/occupied",b"")
    else: fail("typed mutation kind")
    receipt=MutationReceipt(mutation,coordinate,before,after,int(descriptor["variant"])); session.receipt=receipt; return receipt


class GuardianRPC:
    def __init__(self, channel: GuardianChannel, authentication: GuardianAuthentication, workers: GuardianWorkers, objects: GuardianObjectLedger, tmp_fd: int, repository_fd: int, package_fd: int, global_lock_name: bytes) -> None:
        self.channel=channel; self.authentication=authentication; self.workers=workers; self.objects=objects; self.tmp_fd=tmp_fd; self.repository_fd=repository_fd; self.package_fd=package_fd; self.global_lock_name=global_lock_name
        self.sessions: dict[int,MethodSession]={}; self.next_session=100; self.next_lock=1

    def _active(self, child: int, cap: str) -> None:
        self.authentication.authorize_active(child,cap)

    def _confirm_audited_spawn(self, requester: WorkerRecord, frame: RPCFrame) -> dict[str,str]:
        auth=self.authentication.state(requester.spec.child)
        payload=frame.packet[4:]
        if auth.state!="ACTIVE_AUTHORIZED" or payload!=frame.record.encode("ascii"): fail("audited RPC local bytes")
        outer=parse_exact(frame.record,"AUDITED_SPAWN",(("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}"),("trigger",r"[A-Z0-9_]+"),("core",r"(?:[0-9a-f]{2})+")))
        if int(outer["audit"])!=auth.audit or outer["trigger"] not in TRIGGERS: fail("audited RPC local authority")
        core=bytes.fromhex(outer["core"])
        if sha256(core)!=outer["digest"]: fail("audited RPC local digest")
        values=parse_exact(core.decode("ascii"),"SPAWN",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("target",r"[A-Z0-9_]+"),("method",r"test_[a-z0-9_]+"),("purpose",r"[A-Z0-9_]+"),("handle",r"[0-9]+")))
        accepted=f"AUDITED_RPC_ACCEPTED requester_session={auth.session} requester_child={requester.spec.child} audit={outer['audit']} serial={outer['serial']} nonce={outer['nonce']} digest={outer['digest']} rpc_inner_pid={frame.pid} rpc_inner_uid={frame.uid} rpc_inner_gid={frame.gid} payload={payload.hex()}"
        correlation=f"{outer['audit']}:{outer['serial']}"
        self.workers.begin_running_reference(requester)
        self.channel.send(accepted,correlation)
        confirmed=f"AUDITED_RPC_CONFIRMED requester_session={auth.session} requester_child={requester.spec.child} audit={outer['audit']} serial={outer['serial']} nonce={outer['nonce']} digest={outer['digest']}"
        if self.channel.receive(lambda record:record==confirmed,correlation)!=confirmed: fail("audited RPC confirmation")
        self.workers.finish_running_reference(requester)
        values.update({name:outer[name] for name in ("audit","serial","nonce","digest","trigger")})
        values["outer_sha256"]=sha256(payload)
        return values

    def _register_foreign_fixture(self, session: MethodSession, tree: OwnedTree, *, lock: bool) -> None:
        if session.foreign_root_handle or tree.foreign_fd<0: fail("foreign fixture registration state")
        session.foreign_root_cap=tree.foreign_fd; session.foreign_root_handle=self.objects.register(session.session,"LOCK" if lock else "ROOT",session.foreign_root_cap)
        session.foreign_member_cap=tree.populate_foreign_member(b"P15R-FOREIGN-LOCK-v1\n" if lock else b"P15R-FOREIGN-ROOT-v1\n")
        session.foreign_member_handle=self.objects.register(session.session,"LOCK_MEMBER" if lock else "ROOT_MEMBER",session.foreign_member_cap)

    def _prepare_lock_fixture(self, session: MethodSession) -> None:
        if session.lock_tree is not None: fail("duplicate lock fixture")
        tree=OwnedTree(self.tmp_fd,f"p15r.lock.{session.session}"); lock_fd=tree.directory("p15r-wieferich-ulm-controls-0.lock")
        lock_st=os.fstat(lock_fd); token=sha256(f"P15R-LOCK-OWNER-v1:0:{lock_st.st_dev}:{lock_st.st_ino}:p15r-wieferich-ulm-controls-0.lock".encode("ascii"))
        session.lock_tree=tree; session.lock_parent_cap=tree.root_fd; session.lock_parent_handle=self.objects.register(session.session,"LOCK_PARENT",session.lock_parent_cap)
        session.lock_root_cap=lock_fd; session.lock_root_handle=self.objects.register(session.session,"LOCK",session.lock_root_cap)
        tree.write("p15r-wieferich-ulm-controls-0.lock/.owner",f"P15R-LOCK-OWNER-v1 {token}\n".encode("ascii"))
        session.lock_member_cap=os.open(".owner",OPEN_REGULAR,dir_fd=lock_fd); session.lock_member_handle=self.objects.register(session.session,"LOCK_MEMBER",session.lock_member_cap)
        session.lock_state="ACQUIRING" if session.trigger=="P15R_TEST_REPLACE_LOCK_ACQUIRING" else "UNOWNED"

    def _prepare_signal_fixture(self, session: MethodSession) -> None:
        if session.method!="test_rep_009" or session.trigger!="P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN" or session.signal_tree is not None or session.signal_state!="UNOWNED": fail("signal fixture authority")
        tree=OwnedTree(self.tmp_fd,f"p15r.signal.{session.session}"); root_fd=tree.directory("p15r-isolated.lock")
        root=os.fstat(root_fd); token=sha256(f"P15R-LOCK-OWNER-v1:{session.session}:{root.st_dev}:{root.st_ino}:p15r-isolated.lock".encode("ascii"))
        session.signal_tree=tree; session.signal_ledger_session=2000000+session.session; session.signal_parent_cap=tree.root_fd; session.signal_parent_handle=self.objects.register(session.signal_ledger_session,"LOCK_PARENT",session.signal_parent_cap)
        session.signal_root_cap=root_fd; session.signal_root_handle=self.objects.register(session.signal_ledger_session,"LOCK",session.signal_root_cap)
        tree.write("p15r-isolated.lock/.owner",f"P15R-LOCK-OWNER-v1 {token}\n".encode("ascii"))
        session.signal_member_cap=os.open(".owner",OPEN_REGULAR,dir_fd=root_fd); session.signal_member_handle=self.objects.register(session.signal_ledger_session,"LOCK_MEMBER",session.signal_member_cap)
        session.signal_acquiring_token=token; session.signal_state="ACQUIRING"; session.signal_pending=0

    def _queue_signal_after_created(self, session: MethodSession, requester: WorkerRecord) -> None:
        if (session.method,session.trigger)!=("test_rep_009","P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN") or session.signal_tree is None or session.signal_state!="ACQUIRING" or session.signal_pending:
            fail("signal injection state")
        syscall(SYS_PIDFD_SEND_SIGNAL,ctypes.c_int(requester.pidfd),ctypes.c_int(signal.SIGTERM),ctypes.c_void_p(),ctypes.c_uint(0))
        session.signal_pending=signal.SIGTERM
        self._cleanup_signal_fixture(session)

    def _cleanup_signal_fixture(self, session: MethodSession) -> None:
        tree=session.signal_tree
        if tree is None or session.signal_state!="ACQUIRING" or session.signal_pending!=signal.SIGTERM: fail("signal fixture cleanup state")
        self.channel.send(f"FREEZE_REQUEST session={session.signal_ledger_session} handle={session.signal_root_handle} phase=METHOD")
        frozen=self.channel.receive(lambda value:value.partition(" ")[0]=="FROZEN_NOREFS")
        values=parse_exact(frozen,"FROZEN_NOREFS",(("session",str(session.signal_ledger_session)),("handle",str(session.signal_root_handle)),("phase",r"METHOD"),("epoch",r"[1-9][0-9]*")))
        member=self.objects.validate(session.signal_member_handle,session.signal_member_cap); root=self.objects.validate(session.signal_root_handle,session.signal_root_cap); parent=self.objects.validate(session.signal_parent_handle,session.signal_parent_cap)
        tree.cleanup_members(); close_proved(session.signal_member_cap); session.signal_member_cap=-1; self.objects.release_closed(session.signal_member_handle,(member.dev,member.ino))
        tree.cleanup_directories(); session.signal_root_cap=-1; self.objects.release_closed(session.signal_root_handle,(root.dev,root.ino)); session.signal_parent_cap=-1; self.objects.release_closed(session.signal_parent_handle,(parent.dev,parent.ino))
        self.channel.send(f"CLEANUP_COMMITTED session={session.signal_ledger_session} handle={session.signal_root_handle} epoch={values['epoch']}")
        thawed=f"THAWED session={session.signal_ledger_session} handle={session.signal_root_handle} epoch={values['epoch']}"
        if self.channel.receive(lambda value:value==thawed)!=thawed: fail("signal fixture thaw")
        self.objects.retire_session(session.signal_ledger_session); session.signal_tree=None; session.signal_state="ABSENT"

    def _prepare_signal_foreign_fixture(self, session: MethodSession) -> bytes:
        if session.signal_tree is not None or session.signal_state!="ABSENT" or session.signal_pending!=signal.SIGTERM or session.signal_foreign_receipt is not None: fail("signal foreign fixture authority")
        tree=OwnedTree(self.tmp_fd,f"p15r.foreign.{session.session}"); root_fd=tree.directory("p15r-isolated.lock")
        root=os.fstat(root_fd); token=sha256(f"P15R-FOREIGN-LOCK:{session.session}:{root.st_dev}:{root.st_ino}".encode("ascii"))
        if not session.signal_acquiring_token or token==session.signal_acquiring_token: fail("signal foreign token distinction")
        owner=f"P15R-LOCK-OWNER-v1 {token}\n".encode("ascii")
        session.signal_tree=tree; session.signal_parent_cap=tree.root_fd; session.signal_parent_handle=self.objects.register(session.signal_ledger_session,"LOCK_PARENT",session.signal_parent_cap)
        session.signal_root_cap=root_fd; session.signal_root_handle=self.objects.register(session.signal_ledger_session,"LOCK",session.signal_root_cap)
        tree.write("p15r-isolated.lock/.owner",owner); member_fd=os.open(".owner",OPEN_REGULAR,dir_fd=root_fd); member=os.fstat(member_fd)
        session.signal_member_cap=member_fd; session.signal_member_handle=self.objects.register(session.signal_ledger_session,"LOCK_MEMBER",session.signal_member_cap)
        session.signal_foreign_receipt=(root.st_dev,root.st_ino,member.st_dev,member.st_ino,owner); session.signal_state="FOREIGN_HELD"
        return b"\0/tmp/p15r-isolated."+str(session.session).encode("ascii")+b".lock"

    def _cleanup_signal_foreign_fixture(self, session: MethodSession) -> None:
        tree=session.signal_tree; receipt=session.signal_foreign_receipt
        if tree is None or receipt is None or session.signal_state!="FOREIGN_HELD" or set(os.listdir(tree.directory("p15r-isolated.lock")))!={".owner"}: fail("signal foreign fixture state")
        root=self.objects.validate(session.signal_root_handle,session.signal_root_cap); member=self.objects.validate(session.signal_member_handle,session.signal_member_cap); parent=self.objects.validate(session.signal_parent_handle,session.signal_parent_cap)
        if (root.dev,root.ino,member.dev,member.ino,read_regular_at(session.signal_root_cap,".owner"))!=receipt: fail("signal foreign fixture drift")
        self.channel.send(f"FREEZE_REQUEST session={session.signal_ledger_session} handle={session.signal_root_handle} phase=METHOD")
        frozen=self.channel.receive(lambda value:value.partition(" ")[0]=="FROZEN_NOREFS")
        values=parse_exact(frozen,"FROZEN_NOREFS",(("session",str(session.signal_ledger_session)),("handle",str(session.signal_root_handle)),("phase",r"METHOD"),("epoch",r"[1-9][0-9]*")))
        tree.cleanup_members(); close_proved(session.signal_member_cap); session.signal_member_cap=-1; self.objects.release_closed(session.signal_member_handle,(member.dev,member.ino))
        tree.cleanup_directories(); session.signal_root_cap=-1; self.objects.release_closed(session.signal_root_handle,(root.dev,root.ino)); session.signal_parent_cap=-1; self.objects.release_closed(session.signal_parent_handle,(parent.dev,parent.ino))
        self.channel.send(f"CLEANUP_COMMITTED session={session.signal_ledger_session} handle={session.signal_root_handle} epoch={values['epoch']}")
        thawed=f"THAWED session={session.signal_ledger_session} handle={session.signal_root_handle} epoch={values['epoch']}"
        if self.channel.receive(lambda value:value==thawed)!=thawed: fail("signal foreign fixture thaw")
        self.objects.retire_session(session.signal_ledger_session); session.signal_tree=None; session.signal_foreign_receipt=None; session.signal_state="ABSENT"

    def _cleanup_lock_fixture(self, session: MethodSession) -> None:
        tree=session.lock_tree
        if tree is None or session.lock_root_handle<=0: fail("lock fixture cleanup state")
        self.channel.send(f"FREEZE_REQUEST session={session.session} handle={session.lock_root_handle} phase=METHOD")
        frozen=self.channel.receive(lambda value:value.partition(" ")[0]=="FROZEN_NOREFS")
        frozen_values=parse_exact(frozen,"FROZEN_NOREFS",(("session",str(session.session)),("handle",str(session.lock_root_handle)),("phase",r"METHOD"),("epoch",r"[1-9][0-9]*")))
        epoch=frozen_values["epoch"]
        member_identity=self.objects.validate(session.lock_member_handle,session.lock_member_cap); root_identity=self.objects.validate(session.lock_root_handle,session.lock_root_cap); parent_identity=self.objects.validate(session.lock_parent_handle,session.lock_parent_cap)
        foreign_root_identity=self.objects.validate(session.foreign_root_handle,session.foreign_root_cap) if session.foreign_root_handle else None
        foreign_member_identity=self.objects.validate(session.foreign_member_handle,session.foreign_member_cap) if session.foreign_member_handle else None
        tree.cleanup_members(); close_proved(session.lock_member_cap); session.lock_member_cap=-1; self.objects.release_closed(session.lock_member_handle,(member_identity.dev,member_identity.ino))
        tree.cleanup_directories(); session.lock_foreign_outcome="FOREIGN_RETAINED" if tree.foreign_audited else "ABSENT"
        if foreign_member_identity is not None:
            close_proved(session.foreign_member_cap); session.foreign_member_cap=-1; self.objects.release_closed(session.foreign_member_handle,(foreign_member_identity.dev,foreign_member_identity.ino))
        if foreign_root_identity is not None:
            session.foreign_root_cap=-1; self.objects.release_closed(session.foreign_root_handle,(foreign_root_identity.dev,foreign_root_identity.ino))
        session.lock_root_cap=-1; self.objects.release_closed(session.lock_root_handle,(root_identity.dev,root_identity.ino))
        session.lock_parent_cap=-1; self.objects.release_closed(session.lock_parent_handle,(parent_identity.dev,parent_identity.ino))
        self.channel.send(f"CLEANUP_COMMITTED session={session.session} handle={session.lock_root_handle} epoch={epoch}")
        thawed=f"THAWED session={session.session} handle={session.lock_root_handle} epoch={epoch}"
        if self.channel.receive(lambda value:value==thawed)!=thawed: fail("lock fixture thaw")
        self.objects.retire_session(session.session)
        session.lock_tree=None; session.lock_state="DISPLACED_CLEANED" if session.lock_foreign_outcome=="FOREIGN_RETAINED" else "ABSENT"
        if session.lock_foreign_outcome=="FOREIGN_RETAINED": session.outcome="FOREIGN_RETAINED"
        elif session.outcome=="UNSET": session.outcome="ABSENT"

    def handle(self, requester: WorkerRecord, frame: RPCFrame) -> None:
        endpoint=requester.rpc_peer
        if endpoint is None: fail("RPC peer")
        record=frame.record
        auth=self.authentication.state(requester.spec.child); token=record.partition(" ")[0]
        current_peer_inode=os.fstat(endpoint.fileno()).st_ino
        if auth.guardian_peer_inode and current_peer_inode!=auth.guardian_peer_inode: fail("FD4 endpoint ABA")
        if token=="SESSION_CREATE" and auth.state=="CREATE_ARMED":
            created=self.authentication.accept_create(requester.spec.child,frame,current_peer_inode)
            packet=rpc_send(endpoint,created.decode("ascii")); self.authentication.created_sent(requester.spec.child,packet); return
        if token=="SESSION_CREATE":
            values=parse_exact(record,token,(("request",r"[1-9][0-9]*"),("method",r"test_[a-z0-9_]+"),("trigger",r"[A-Z0-9_]+"),("mutation",r"(?:[0-9a-f]{2})+"),("active_cap",r"[0-9a-f]{64}"))) if " mutation=" in record else parse_exact(record,token,(("request",r"[1-9][0-9]*"),("method",r"test_[a-z0-9_]+"),("trigger",r"[A-Z0-9_]+"),("active_cap",r"[0-9a-f]{64}")))
            self._active(requester.spec.child,values["active_cap"])
            if auth.state!="ACTIVE_AUTHORIZED" or values["trigger"] not in TRIGGERS: fail("method session create")
            session_id=self.next_session; self.next_session+=1; descriptor=parse_descriptor(values["mutation"]) if "mutation" in values else None
            session=MethodSession(session_id,values["method"],values["trigger"],descriptor); self.sessions[session_id]=session
            if values["trigger"] in ("P15R_TEST_REPLACE_LOCK_ACQUIRING","P15R_TEST_REPLACE_LOCK_CLEANING"): self._prepare_lock_fixture(session)
            rpc_send(endpoint,f"SESSION_CREATED request={values['request']} session={session_id}"); return
        if token=="LOCK_ACQUIRE":
            values=parse_exact(record,token,(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("active_cap",r"[0-9a-f]{64}"))); self._active(requester.spec.child,values["active_cap"])
            session=self.sessions[int(values["session"])]
            if session.lock: fail("duplicate logical lock")
            if session.lock_tree is not None:
                if session.trigger=="P15R_TEST_REPLACE_LOCK_ACQUIRING" and not session.lock_tree.foreign_exchanged: fail("acquiring replacement not reaped")
                session.lock_socket=socket.socket(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
                address=b"\0/tmp/p15r-wieferich-ulm-controls-0.lock.session."+str(session.session).encode("ascii")
                session.lock_socket.bind(address); session.lock_state="OWNED"
            session.lock=self.next_lock; self.next_lock+=1
            rpc_send(endpoint,f"LOCK_ACQUIRED request={values['request']} session={session.session} lock={session.lock} state=OWNED"); return
        if token=="ROOT_CREATE":
            values=parse_exact(record,token,(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("purpose",r"[A-Z0-9_]+"),("active_cap",r"[0-9a-f]{64}"))); self._active(requester.spec.child,values["active_cap"])
            session=self.sessions[int(values["session"])]
            if not session.lock or session.tree is not None: fail("root create state")
            tree=OwnedTree(self.tmp_fd,f"p15r.method.{session.session}"); session.tree=tree; session.package_path=populate_synthetic_repository(tree,self.repository_fd,self.package_fd)
            session.root_purpose=values["purpose"]
            result_fd=tree.directory(session.result_relative); session.result_path="/tmp/"+tree.basename+"/"+session.result_relative
            session.parent_cap=tree.root_fd; session.parent_handle=self.objects.register(session.session,"ROOT_PARENT",session.parent_cap)
            session.root_cap=result_fd; session.handle=self.objects.register(session.session,"ROOT",session.root_cap)
            rpc_send(endpoint,f"ROOT_CREATED request={values['request']} session={session.session} handle={session.handle}"); return
        if token=="ROOT_VALIDATE":
            values=parse_exact(record,token,(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("active_cap",r"[0-9a-f]{64}"))); self._active(requester.spec.child,values["active_cap"])
            session=self.sessions[int(values["session"])]
            if session.handle!=int(values["handle"]) or session.tree is None: fail("root validate")
            present=tuple(name for name in GENERATED_NAMES if session.result_relative+"/"+name in session.tree.files)
            session.empty_p25=bool(session.descriptor is not None and session.descriptor.get("mutation")=="P25" and session.trigger in ("P15R_TEST_REPLACE_MUTATION_ROOT","P15R_TEST_REPLACE_P25_ROOT") and not present)
            if not session.empty_p25 and present!=GENERATED_NAMES: fail("generated member set")
            for name in (() if session.empty_p25 else GENERATED_NAMES):
                relative=session.result_relative+"/"+name
                if relative not in session.tree.files: session.tree.adopt(relative)
                if not any((os.fstat(fd).st_dev,os.fstat(fd).st_ino)==session.tree.files[relative] for _handle,fd in session.member_caps):
                    parent,basename=relative.rsplit("/",1); fd=os.open(basename,OPEN_REGULAR,dir_fd=session.tree.directory(parent)); handle=self.objects.register(session.session,"ROOT_MEMBER",fd); session.member_caps.append((handle,fd))
            rpc_send(endpoint,f"ROOT_VALIDATED request={values['request']} session={session.session} handle={session.handle}"); return
        if token=="INJECT_EXCHANGE":
            values=parse_exact(record,token,(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("trigger",r"[A-Z0-9_]+"),("active_cap",r"[0-9a-f]{64}"))); self._active(requester.spec.child,values["active_cap"])
            session=self.sessions[int(values["session"])]
            if values["trigger"]!=session.trigger: fail("inject join")
            if values["trigger"] in ("P15R_TEST_REPLACE_LOCK_ACQUIRING","P15R_TEST_REPLACE_LOCK_CLEANING"):
                if int(values["handle"])!=0 or session.lock_tree is None: fail("lock inject handle")
                if values["trigger"]=="P15R_TEST_REPLACE_LOCK_CLEANING":
                    if session.lock_state!="OWNED": fail("lock cleaning state")
                    session.lock_state="CLEANING"
                session.lock_tree.prepare_foreign_child("p15r-wieferich-ulm-controls-0.lock",values["trigger"],"/tmp/"+session.lock_tree.basename)
                self._register_foreign_fixture(session,session.lock_tree,lock=True)
            elif values["trigger"] in ("P15R_TEST_REPLACE_CANONICAL_ROOT","P15R_TEST_REPLACE_MUTATION_ROOT","P15R_TEST_REPLACE_P25_ROOT"):
                if session.handle!=int(values["handle"]): fail("root inject handle")
                if session.descriptor is not None and values["trigger"]=="P15R_TEST_REPLACE_P25_ROOT" and not session.empty_p25:
                    apply_mutation(session)
                    occupied=session.result_relative+"/occupied"; parent,basename=occupied.rsplit("/",1); fd=os.open(basename,OPEN_REGULAR,dir_fd=session.tree.directory(parent)); handle=self.objects.register(session.session,"ROOT_MEMBER",fd); session.member_caps.append((handle,fd))
                if session.tree is None: fail("replacement root absent")
                session.tree.prepare_foreign_child(session.result_relative,values["trigger"],"/tmp/"+session.tree.basename)
                self._register_foreign_fixture(session,session.tree,lock=False)
            else:
                if session.handle!=int(values["handle"]): fail("mutation inject handle")
                apply_mutation(session)
            rpc_send(endpoint,f"INJECTED request={values['request']} session={session.session} handle={session.handle} outcome=UNSET"); return
        if token=="AUDITED_SPAWN":
            values=self._confirm_audited_spawn(requester,frame)
            self._spawn(requester,values); return
        if token=="CLEAN": self._clean(requester,record); return
        if token=="FOREIGN_AUDIT":
            values=parse_exact(record,token,(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("active_cap",r"[0-9a-f]{64}"))); self._active(requester.spec.child,values["active_cap"])
            session=self.sessions[int(values["session"])]
            if int(values["handle"])==0:
                if session.lock_state not in ("ABSENT","DISPLACED_CLEANED"): fail("lock foreign audit before cleanup")
                outcome=session.lock_foreign_outcome or "ABSENT"
            else:
                if not session.cleaned: fail("foreign audit before cleanup")
                outcome=session.foreign_outcome or "ABSENT"
            if outcome not in ("ABSENT","FOREIGN_RETAINED"): fail("foreign audit receipt")
            rpc_send(endpoint,f"FOREIGN_AUDITED request={values['request']} session={session.session} handle={values['handle']} outcome={outcome}"); return
        if token=="LOCK_RELEASE":
            values=parse_exact(record,token,(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("lock",r"[1-9][0-9]*"),("active_cap",r"[0-9a-f]{64}"))); self._active(requester.spec.child,values["active_cap"])
            session=self.sessions[int(values["session"])]
            if session.lock!=int(values["lock"]): fail("lock release")
            if session.lock_tree is not None:
                if session.trigger=="P15R_TEST_REPLACE_LOCK_CLEANING" and not session.lock_tree.foreign_exchanged: fail("cleaning replacement not reaped")
                self._cleanup_lock_fixture(session)
            if session.lock_socket is not None: session.lock_socket.close(); session.lock_socket=None
            session.lock=0; outcome="DISPLACED_CLEANED" if session.lock_foreign_outcome=="FOREIGN_RETAINED" else "ABSENT"
            rpc_send(endpoint,f"LOCK_RELEASED request={values['request']} session={session.session} lock={values['lock']} outcome={outcome}"); return
        if token=="SESSION_CLOSE":
            values=parse_exact(record,token,(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("active_cap",r"[0-9a-f]{64}")))
            if int(values["session"])==auth.session:
                self._active(requester.spec.child,values["active_cap"])
                for method_session in self.sessions.values():
                    signal_complete=((method_session.signal_state,method_session.signal_pending)==("ABSENT",signal.SIGTERM) and bool(method_session.signal_acquiring_token)) if method_session.trigger=="P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN" else ((method_session.signal_state,method_session.signal_pending,method_session.signal_acquiring_token)==("UNOWNED",0,""))
                    if not method_session.closed or method_session.tree is not None or method_session.lock_tree is not None or method_session.signal_tree is not None or method_session.signal_foreign_receipt is not None or method_session.lock or method_session.member_caps or not signal_complete: fail("terminal inherited cleanup")
                packet=self.authentication.terminal(requester.spec.child,int(values["request"]),"UNSET"); rpc_send_packet(endpoint,packet); self.authentication.terminal_sent(requester.spec.child,packet); return
            self._active(requester.spec.child,values["active_cap"]); session=self.sessions[int(values["session"])]
            if not session.cleaned and session.tree is not None: fail("session close before clean")
            if session.lock or session.lock_tree is not None: fail("session close with lock")
            signal_complete=((session.signal_state,session.signal_pending)==("ABSENT",signal.SIGTERM) and bool(session.signal_acquiring_token)) if session.trigger=="P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN" else ((session.signal_state,session.signal_pending,session.signal_acquiring_token)==("UNOWNED",0,""))
            if session.signal_tree is not None or session.signal_foreign_receipt is not None or not signal_complete: fail("session close with signal residue")
            if session.outcome=="UNSET": session.outcome="ABSENT"
            if session.outcome not in OUTCOMES: fail("method terminal outcome")
            session.closed=True; terminal=sha256(f"P15R-METHOD-TERMINAL:{session.session}:{values['request']}".encode("ascii"))
            rpc_send(endpoint,f"SESSION_CLOSED request={values['request']} session={session.session} outcome={session.outcome} terminal_cap={terminal}"); return
        fail("FD4 request enum")

    @staticmethod
    def _send_spawn_result(endpoint: socket.socket, values: Mapping[str,str], record: WorkerRecord, status: int) -> None:
        request=int(values["request"]); stdout=bytes(record.stdout); stderr=bytes(record.stderr)
        for stream_name,data in (("SPAWN_STDOUT",bytes(record.stdout)),("SPAWN_STDERR",bytes(record.stderr))):
            for sequence,offset in enumerate(range(0,len(data),1024)): rpc_send(endpoint,f"{stream_name} request={request} seq={sequence} hex={data[offset:offset+1024].hex()}")
        stdout_chunks=(len(stdout)+1023)//1024; stderr_chunks=(len(stderr)+1023)//1024
        core=f"SPAWN_RESULT request={request} audit={values['audit']} serial={values['serial']} nonce={values['nonce']} digest={values['digest']} outer_sha256={values['outer_sha256']} target={values['target']} method={values['method']} purpose={values['purpose']} handle={values['handle']} child={record.spec.child} status={status} outcome=EXITED stdout_bytes={len(stdout)} stderr_bytes={len(stderr)} stdout_chunks={stdout_chunks} stderr_chunks={stderr_chunks} stdout_sha256={sha256(stdout)} stderr_sha256={sha256(stderr)}"
        core_bytes=core.encode("ascii"); capability=sha256(b"P15R-SPAWN-RESULT-CAP-v1"+u64be(len(core_bytes))+core_bytes)
        rpc_send(endpoint,core+f" capability_sha256={capability}")

    def _spawn_signal_lock_pair(self, requester: WorkerRecord, session: MethodSession, holder_values: Mapping[str,str]) -> None:
        endpoint=requester.rpc_peer
        if endpoint is None or (session.method,session.trigger)!=("test_rep_009","P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN") or holder_values["target"]!="LOCK_HOLDER" or holder_values["purpose"]!="NONE" or int(holder_values["handle"])!=0: fail("signal holder authority")
        self._queue_signal_after_created(session,requester)
        address=self._prepare_signal_foreign_fixture(session); environment=(("P15R_LOCK_ADDRESS_HEX",address.hex()),("P15R_LOCK_METHOD",session.method),("P15R_LOCK_TRIGGER",session.trigger))
        holder_child=self.workers.next_child; holder_admission=f"METHOD_V1:{session.method}:S{session.session}:R{holder_values['request']}:C{holder_child}"
        holder_spec=WorkerSpec(session.session,holder_child,ROLE_BY_TARGET["LOCK_HOLDER"],session.method,session.method,"NONE",holder_admission,"STDIO_BARRIER",None,session.package_path or "@PACKAGE_FD11",("<lock-holder>",),environment,None,int(holder_values["request"]),int(holder_values["audit"]),int(holder_values["serial"]),holder_values["nonce"],holder_values["digest"],session.trigger,0,requester.spec.child,target="LOCK_HOLDER")
        holder=self.workers.spawn(holder_spec)
        self.workers.configure_streams(holder); holder_poller=select.poll()
        for fd in self.workers.stream_fds(holder): holder_poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
        holder_poller.register(holder.pidfd,select.POLLIN|select.POLLHUP|select.POLLERR)
        while len(holder.stdout)<len(b"HOLDER_READY\n"):
            try: holder_events=holder_poller.poll()
            except InterruptedError: fail("holder readiness poll EINTR")
            if not holder_events: fail("holder readiness empty poll")
            for fd,event in sorted(holder_events,key=lambda item:item[0]==holder.pidfd):
                if fd in self.workers.stream_fds(holder): self.workers.drain_stream_event(holder,holder_poller,fd,event)
                elif fd==holder.pidfd: fail("holder terminated before contender")
                else: fail("holder readiness unknown fd")
            if holder.stderr or holder.stdout_eof or len(holder.stdout)>len(b"HOLDER_READY\n"): fail("holder readiness bytes")
        if bytes(holder.stdout)!=b"HOLDER_READY\n": fail("holder readiness")
        contender_frame=rpc_receive(endpoint,requester.pid)
        if contender_frame is None: fail("contender request EOF")
        contender_values=self._confirm_audited_spawn(requester,contender_frame)
        if (contender_values["request"],contender_values["session"],contender_values["target"],contender_values["method"],contender_values["purpose"],contender_values["handle"],contender_values["trigger"])!=(str(int(holder_values["request"])+1),str(session.session),"LOCK_CONTENDER",session.method,"NONE","0",session.trigger): fail("contender audited request")
        current_peer_inode=os.fstat(endpoint.fileno()).st_ino; state=self.authentication.state(requester.spec.child)
        if state.state!="ACTIVE_AUTHORIZED" or (state.guardian_peer_inode and current_peer_inode!=state.guardian_peer_inode): fail("contender endpoint authority")
        contender_child=self.workers.next_child; contender_admission=f"METHOD_V1:{session.method}:S{session.session}:R{contender_values['request']}:C{contender_child}"
        contender_spec=WorkerSpec(session.session,contender_child,ROLE_BY_TARGET["LOCK_CONTENDER"],session.method,session.method,"NONE",contender_admission,"STDIO_BARRIER",None,session.package_path or "@PACKAGE_FD11",("<lock-contender>",),environment,None,int(contender_values["request"]),int(contender_values["audit"]),int(contender_values["serial"]),contender_values["nonce"],contender_values["digest"],session.trigger,74,requester.spec.child,target="LOCK_CONTENDER")
        contender=self.workers.spawn(contender_spec); contender_status=self.workers.reap(contender)
        if contender_status!=74 or contender.stdout or bytes(contender.stderr)!=b"E_CONCURRENT_ENTRY\n": fail("contender causal result")
        syscall(SYS_PIDFD_SEND_SIGNAL,ctypes.c_int(holder.pidfd),ctypes.c_int(signal.SIGUSR1),ctypes.c_void_p(),ctypes.c_uint(0))
        holder_status=self.workers.reap(holder)
        if holder_status!=0 or bytes(holder.stdout)!=b"HOLDER_READY\n" or holder.stderr: fail("holder causal result")
        self._cleanup_signal_foreign_fixture(session)
        self._send_spawn_result(endpoint,holder_values,holder,holder_status)
        self._send_spawn_result(endpoint,contender_values,contender,contender_status)

    def _spawn(self, requester: WorkerRecord, values: Mapping[str,str]) -> None:
        target=values["target"]
        if target not in TARGETS or target=="TOP_TEST_CONTROLS": fail("spawn target")
        session=self.sessions.get(int(values["session"]))
        if session is None or values["method"]!=session.method: fail("spawn method session join")
        evidence_trigger=session.trigger if target in ("COPIED_REPRODUCE","REPLACEMENT_ACTOR","LOCK_HOLDER","LOCK_CONTENDER") or (target in ("VERIFY_ONLY_GENERATOR","GENERATE_MUTATION") and session.receipt is not None) else "NONE"
        if values["trigger"]!=evidence_trigger: fail("spawn exact trigger join")
        signal_fixture=target=="COPIED_REPRODUCE" and session.method=="test_rep_009" and session.trigger=="P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN"
        if signal_fixture: self._prepare_signal_fixture(session)
        if target=="LOCK_HOLDER": self._spawn_signal_lock_pair(requester,session,values); return
        descriptor=session.descriptor or {}; child=self.workers.next_child
        admission=f"METHOD_V1:{values['method']}:S{session.session}:R{values['request']}:C{child}"
        source=None if target in ("REPLACEMENT_ACTOR","LOCK_HOLDER","LOCK_CONTENDER") else {"GENERATE_MUTATION":"code/generate_controls.py","VERIFY_ONLY_GENERATOR":"code/generate_controls.py","COPIED_REPRODUCE":"experiments/reproduce.sh"}.get(target,"code/generate_controls.py")
        creation_target=target in ("GENERATE_CANONICAL_A","GENERATE_CANONICAL_B","GENERATE_MUTATION")
        fdset="STDIO_SOURCE_ROOT_BARRIER" if creation_target else ("STDIO_SOURCE_RPC_AUDIT_BARRIER" if target=="COPIED_REPRODUCE" else ("STDIO_BARRIER" if target in ("REPLACEMENT_ACTOR","LOCK_HOLDER","LOCK_CONTENDER") else "STDIO_SOURCE_BARRIER"))
        root_fd=None; argv=(source,) if source is not None else ("<in-block-stub>",); environment: list[tuple[str,str]]=[]; audit_fd=None; creator_preexisting: set[str]=set(); creator_authorize: Callable[[],None]|None=None
        if creation_target:
            if session.tree is None or session.handle<=0 or int(values["handle"])!=session.handle: fail("generation root")
            root_fd=session.tree.directory(session.result_relative)
            creator_preexisting={name for name in os.listdir(root_fd)}
            argv=(source,"--generate","--output-dir",session.result_path)
            if target=="GENERATE_MUTATION":
                purpose=str(descriptor.get("mutation","P00")); variant=int(descriptor.get("variant",1)); generation_purpose=f"MUTATION_{purpose}_V{variant}"
            else: generation_purpose="CANONICAL_A" if target=="GENERATE_CANONICAL_A" else "CANONICAL_B"
            st=os.fstat(root_fd); environment.extend((("P15R_TEST_CONTEXT","1"),("P15R_GENERATION_ROOT_FD","9"),("P15R_GENERATION_PURPOSE",generation_purpose),("P15R_GENERATION_UID",str(st.st_uid)),("P15R_GENERATION_DEV",str(st.st_dev)),("P15R_GENERATION_INO",str(st.st_ino))))
            if values["purpose"]!=generation_purpose: fail("generation purpose join")
            authorization=f"MEMBER_CREATE_AUTHORIZED session={session.session} child={child} root={session.handle} target={target} purpose={values['purpose']} basename_set=GENERATED_NINE_V1 primitive=DIRFD_O_CREAT_O_EXCL_O_NOFOLLOW"
            def creator_authorize() -> None:
                self.channel.send(authorization,str(child)); expected=f"MEMBER_CREATE_ACK session={session.session} child={child} root={session.handle} purpose={values['purpose']} basename_set=GENERATED_NINE_V1"
                if self.channel.receive(lambda value:value==expected,str(child))!=expected: fail("mutation member authorization")
        elif target=="VERIFY_ONLY_GENERATOR":
            if values["purpose"]!="NONE" or session.tree is None or int(values["handle"])!=session.handle: fail("verify target authority")
            argv=(source,"--verify-only","--input-dir",session.result_path)
        elif target=="REPLACEMENT_ACTOR":
            tree=session.lock_tree if session.trigger in ("P15R_TEST_REPLACE_LOCK_ACQUIRING","P15R_TEST_REPLACE_LOCK_CLEANING") else session.tree
            if tree is None or tree.foreign_identity is None or tree.foreign_exchanged: fail("replacement actor preparation")
            expected_handle=0 if session.trigger in ("P15R_TEST_REPLACE_LOCK_ACQUIRING","P15R_TEST_REPLACE_LOCK_CLEANING") else session.handle
            if values["purpose"]!="NONE" or int(values["handle"])!=expected_handle: fail("replacement actor authority")
            owned=os.fstat(tree.directory((tree.foreign_parent_relative+"/" if tree.foreign_parent_relative!="." else "")+tree.foreign_fixed)); foreign=os.fstat(tree.foreign_fd)
            environment.extend((("P15R_REPLACE_PARENT",tree.foreign_actor_parent),("P15R_REPLACE_FIXED",tree.foreign_fixed),("P15R_REPLACE_INTERNAL",tree.foreign_internal),("P15R_REPLACE_OWNED_DEV",str(owned.st_dev)),("P15R_REPLACE_OWNED_INO",str(owned.st_ino)),("P15R_REPLACE_FOREIGN_DEV",str(foreign.st_dev)),("P15R_REPLACE_FOREIGN_INO",str(foreign.st_ino))))
            environment.extend((("P15R_TEST_CONTEXT","1"),(session.trigger,"1"),("P15R_REPLACE_METHOD",session.method),("P15R_REPLACE_PURPOSE",session.root_purpose or "NONE")))
        elif target=="COPIED_REPRODUCE":
            expected_handle=session.handle if session.tree is not None else 0
            if values["purpose"]!="NONE" or int(values["handle"])!=expected_handle: fail("copied target authority")
            self.channel.send(f"AUDIT_FD_REQUEST session={session.session} child={child} target=COPIED_REPRODUCE role=REQUESTER owner={session.method} purpose=NONE",str(child))
            granted,audit_fd=self.channel.control.receive_fd_matching(re.compile(rf"AUDIT_FD_GRANTED session={session.session} child={child} audit=(?:0|[1-9][0-9]*)")); request_audit=int(parse_exact(granted,"AUDIT_FD_GRANTED",(("session",str(session.session)),("child",str(child)),("audit",r"(?:0|[1-9][0-9]*)")))["audit"])
            copied_package=session.package_path or "."
            copied_root=("/tmp/"+session.tree.basename) if session.tree is not None else "."
            environment.extend((("P15R_COPIED_METHOD",session.method),("P15R_COPIED_TRIGGER",session.trigger),("P15R_COPIED_SESSION",str(session.session)),("P15R_COPIED_PACKAGE",copied_package),("P15R_COPIED_ROOT",copied_root)))
            if descriptor.get("kind")=="RECURSIVE_ENTRY": environment.append(("P15R_REPRO_ACTIVE","1"))
            if descriptor.get("kind")=="CLEANUP": environment.append(("P15R_TEST_ABORT_AFTER_FRESH_A","1"))
            if descriptor.get("kind")=="CONCURRENT_LOCK": environment.append(("P15R_LOCK_PROBE","1"))
            argv=(source,"--verify-only","--input-dir",copied_package+"/results","--repair") if descriptor.get("kind")=="CLI_REPAIR" else (source,copied_package)
        elif target=="LOCK_CONTENDER":
            if values["purpose"]!="NONE" or int(values["handle"])!=0 or descriptor.get("kind")!="CONCURRENT_LOCK": fail("lock contender authority")
            environment.extend((("P15R_LOCK_ADDRESS_HEX",self.global_lock_name.hex()),("P15R_LOCK_METHOD",session.method),("P15R_LOCK_TRIGGER",session.trigger)))
            argv=("<lock-contender>",)
        worker_cwd=session.package_path or "@PACKAGE_FD11"
        expected_status=0
        if target=="COPIED_REPRODUCE": expected_status=1 if signal_fixture or descriptor.get("kind") in ("RECURSIVE_ENTRY","CLEANUP","CACHE_POST","CLI_REPAIR","CONCURRENT_LOCK") else 0
        elif target=="LOCK_CONTENDER": expected_status=74
        elif target in ("VERIFY_ONLY_GENERATOR","GENERATE_MUTATION") and session.receipt is not None: expected_status=1
        spec=WorkerSpec(session.session,child,ROLE_BY_TARGET[target],session.method,values["method"],values["purpose"],admission,fdset,source,worker_cwd,argv,tuple(environment),root_fd,int(values["request"]),int(values["audit"]),int(values["serial"]),values["nonce"],values["digest"],values["trigger"],expected_status,requester.spec.child,target=target,request_audit=request_audit if target=="COPIED_REPRODUCE" else 0)
        child_record=self.workers.spawn(spec,audit_fd,creator_authorize)
        if target=="COPIED_REPRODUCE": self.drive_requester(child_record)
        status=self.workers.reap(child_record,self.authentication.state(child) if target=="COPIED_REPRODUCE" else None)
        if status!=expected_status: fail("spawn status contract")
        if target=="COPIED_REPRODUCE":
            auth_state=self.authentication.state(child)
            if auth_state.state!="AUTH_REAP_RECONCILED": fail("copied auth reap state")
            if signal_fixture and (session.signal_tree is not None or session.signal_foreign_receipt is not None or session.signal_state!="ABSENT" or session.signal_pending!=signal.SIGTERM or not session.signal_acquiring_token): fail("signal fixture terminal residue")
        if creation_target and session.tree is not None:
            actual=set(os.listdir(session.tree.directory(session.result_relative))); produced=actual-creator_preexisting
            if status==0 and produced!=set(GENERATED_NAMES): fail("creator produced set")
            if status!=0 and not produced.issubset(set(GENERATED_NAMES)): fail("failed creator unexpected member")
            for name in GENERATED_NAMES:
                if name not in produced: continue
                relative=session.result_relative+"/"+name
                if relative not in session.tree.files: session.tree.adopt(relative)
                parent,basename=relative.rsplit("/",1); fd=os.open(basename,OPEN_REGULAR,dir_fd=session.tree.directory(parent)); handle=self.objects.register(session.session,"ROOT_MEMBER",fd); session.member_caps.append((handle,fd))
            closed=f"MEMBER_LEDGER_CLOSED session={session.session} child={child} root={session.handle} count={len(produced)}"
            self.channel.send(closed,str(child)); acknowledged=closed.replace("MEMBER_LEDGER_CLOSED ","MEMBER_LEDGER_ACK ",1)
            if self.channel.receive(lambda value:value==acknowledged,str(child))!=acknowledged: fail("creator ledger ACK")
        if target=="REPLACEMENT_ACTOR":
            tree=session.lock_tree if session.trigger in ("P15R_TEST_REPLACE_LOCK_ACQUIRING","P15R_TEST_REPLACE_LOCK_CLEANING") else session.tree
            if status!=0 or child_record.stderr or tree is None: fail("replacement actor")
            tree.confirm_foreign_exchange(bytes(child_record.stdout)); session.detector="E_CLEANUP"
        if target in ("VERIFY_ONLY_GENERATOR","GENERATE_MUTATION","COPIED_REPRODUCE") and status!=0:
            observed=re.findall(rb"(?<![A-Z0-9_])E_[A-Z0-9_]+(?![A-Z0-9_])",bytes(child_record.stderr))
            if len(observed)!=1: fail("child detector cardinality")
            session.detector=observed[0].decode("ascii")
        endpoint=requester.rpc_peer
        if endpoint is None: fail("requester endpoint")
        self._send_spawn_result(endpoint,values,child_record,status)

    def drive_requester(self, record: WorkerRecord) -> None:
        endpoint=record.rpc_peer
        if endpoint is None: fail("copied requester endpoint")
        self.workers.configure_streams(record)
        poller=select.poll(); poller.register(self.channel.control.sock,select.POLLIN); poller.register(endpoint,select.POLLIN|select.POLLHUP); poller.register(record.pidfd,select.POLLIN)
        for fd in self.workers.stream_fds(record): poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
        while self.authentication.state(record.spec.child).state!="FINALIZED_AWAITING_REAP":
            try: events=poller.poll()
            except InterruptedError: fail("copied requester poll EINTR")
            if not events: fail("copied requester empty poll")
            for fd,event in sorted(events,key=lambda item:(0 if item[0]==self.channel.control.sock.fileno() else (1 if item[0] in self.workers.stream_fds(record) else (2 if item[0]==endpoint.fileno() else 3)))):
                if fd==self.channel.control.sock.fileno():
                    if event&(select.POLLHUP|select.POLLERR|select.POLLNVAL): fail("copied control event")
                    control_record=self.channel.receive()
                    if not self.authentication.handles(control_record): fail("copied control")
                    self.authentication.handle(control_record)
                elif fd in self.workers.stream_fds(record):
                    self.workers.drain_stream_event(record,poller,fd,event)
                elif fd==endpoint.fileno():
                    if event&(select.POLLERR|select.POLLNVAL): fail("copied FD4 poll event")
                    state=self.authentication.state(record.spec.child)
                    if state.state not in ("CREATE_ARMED","ACTIVE_AUTHORIZED"): continue
                    frame=rpc_receive(endpoint,record.pid)
                    if frame is None: fail("copied FD4 early EOF")
                    current_peer_inode=os.fstat(endpoint.fileno()).st_ino
                    if state.guardian_peer_inode and current_peer_inode!=state.guardian_peer_inode: fail("copied FD4 endpoint ABA")
                    if frame.record.partition(" ")[0]=="SESSION_CREATE" and state.state=="CREATE_ARMED":
                        created=self.authentication.accept_create(record.spec.child,frame,current_peer_inode)
                        packet=rpc_send(endpoint,created.decode("ascii")); self.authentication.created_sent(record.spec.child,packet)
                    elif frame.record.partition(" ")[0]=="SESSION_CLOSE":
                        values=parse_exact(frame.record,"SESSION_CLOSE",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("active_cap",r"[0-9a-f]{64}")))
                        self.authentication.authorize_active(record.spec.child,values["active_cap"])
                        method_session=self.sessions.get(record.spec.session)
                        if method_session is None: fail("copied method session")
                        signal_fixture=(method_session.method,method_session.trigger)==("test_rep_009","P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN")
                        if signal_fixture:
                            if method_session.signal_tree is not None or method_session.signal_state!="ABSENT" or method_session.signal_pending!=signal.SIGTERM or method_session.signal_foreign_receipt is not None or not method_session.signal_acquiring_token: fail("incomplete copied signal lifecycle")
                        elif method_session.signal_tree is not None or method_session.signal_state!="UNOWNED" or method_session.signal_pending: fail("unexpected copied signal state")
                        packet=self.authentication.terminal(record.spec.child,int(values["request"]),"UNSET"); rpc_send_packet(endpoint,packet); self.authentication.terminal_sent(record.spec.child,packet)
                    elif state.state=="ACTIVE_AUTHORIZED" and frame.record.partition(" ")[0]=="AUDITED_SPAWN": self.handle(record,frame)
                    else: fail("copied RPC enum")
                elif fd==record.pidfd:
                    if self.authentication.state(record.spec.child).state!="FINALIZED_AWAITING_REAP": fail("copied requester crash")
                else: fail("copied requester unknown poll fd")

    def _clean(self, requester: WorkerRecord, record: str) -> None:
        values=parse_exact(record,"CLEAN",(("request",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*"),("handle",r"[1-9][0-9]*"),("active_cap",r"[0-9a-f]{64}"))); self._active(requester.spec.child,values["active_cap"])
        session=self.sessions[int(values["session"])]
        if session.tree is None or session.handle!=int(values["handle"]) or session.cleaned: fail("cleanup state")
        self.channel.send(f"FREEZE_REQUEST session={session.session} handle={session.handle} phase=METHOD")
        frozen=self.channel.receive(lambda value:value.partition(" ")[0]=="FROZEN_NOREFS")
        frozen_values=parse_exact(frozen,"FROZEN_NOREFS",(("session",str(session.session)),("handle",str(session.handle)),("phase",r"METHOD"),("epoch",r"[1-9][0-9]*")))
        epoch=frozen_values["epoch"]
        tree=session.tree
        if tree.foreign_identity is not None:
            session.foreign_basename=tree.foreign_basename; session.foreign_identity=tree.foreign_identity
        member_identities=[(member_handle,member_fd,self.objects.validate(member_handle,member_fd)) for member_handle,member_fd in reversed(session.member_caps)]
        root_identity=self.objects.validate(session.handle,session.root_cap); parent_identity=self.objects.validate(session.parent_handle,session.parent_cap)
        foreign_root_identity=self.objects.validate(session.foreign_root_handle,session.foreign_root_cap) if session.foreign_root_handle else None
        foreign_member_identity=self.objects.validate(session.foreign_member_handle,session.foreign_member_cap) if session.foreign_member_handle else None
        tree.cleanup_members()
        for member_handle,member_fd,identity in member_identities:
            close_proved(member_fd); self.objects.release_closed(member_handle,(identity.dev,identity.ino))
        session.member_caps.clear()
        tree.cleanup_directories()
        session.foreign_outcome="FOREIGN_RETAINED" if tree.foreign_audited else "ABSENT"
        if foreign_member_identity is not None:
            close_proved(session.foreign_member_cap); session.foreign_member_cap=-1; self.objects.release_closed(session.foreign_member_handle,(foreign_member_identity.dev,foreign_member_identity.ino))
        if foreign_root_identity is not None:
            session.foreign_root_cap=-1; self.objects.release_closed(session.foreign_root_handle,(foreign_root_identity.dev,foreign_root_identity.ino))
        self.objects.release_closed(session.handle,(root_identity.dev,root_identity.ino)); session.root_cap=-1
        self.objects.release_closed(session.parent_handle,(parent_identity.dev,parent_identity.ino)); session.parent_cap=-1
        session.cleaned=True; session.tree=None
        if session.foreign_outcome=="FOREIGN_RETAINED": session.outcome="FOREIGN_RETAINED"
        elif session.outcome=="UNSET": session.outcome="ABSENT"
        self.channel.send(f"CLEANUP_COMMITTED session={session.session} handle={session.handle} epoch={epoch}")
        thawed=f"THAWED session={session.session} handle={session.handle} epoch={epoch}"
        if self.channel.receive(lambda value:value==thawed)!=thawed: fail("method thaw")
        self.objects.retire_session(session.session)
        if not session.detector: fail("cleanup without child detector")
        detector="E_CLEANUP" if session.foreign_outcome=="FOREIGN_RETAINED" else session.detector
        cleanup_outcome="DISPLACED_CLEANED" if session.foreign_outcome=="FOREIGN_RETAINED" else "ABSENT"
        endpoint=requester.rpc_peer
        if endpoint is None: fail("cleanup requester")
        rpc_send(endpoint,f"CLEANED request={values['request']} session={session.session} handle={session.handle} outcome={cleanup_outcome} detector={detector}")


@dataclass
class CanonicalRoot:
    label: str
    tree: OwnedTree
    parent_handle: int
    parent_cap: int
    root_handle: int
    root_cap: int
    root_relative: str="candidate"
    member_handles: list[tuple[int,int]]=field(default_factory=list)


class GuardianTransaction:
    def __init__(self, channel: GuardianChannel, workers: GuardianWorkers, objects: GuardianObjectLedger, rpc: GuardianRPC, authentication: GuardianAuthentication, tmp_fd: int, package_fd: int) -> None:
        self.channel=channel; self.workers=workers; self.objects=objects; self.rpc=rpc; self.authentication=authentication; self.tmp_fd=tmp_fd; self.package_fd=package_fd; self.global_lock: socket.socket|None=None
        self.canonical: list[CanonicalRoot]=[]; self.lock_tree: OwnedTree|None=None; self.lock_parent_handle=0; self.lock_parent_cap=-1; self.lock_handle=0; self.lock_member_handle=0; self.lock_member_cap=-1

    def _spec(self, row: RegistryRow, *, cwd: str, argv: tuple[str,...], environment: tuple[tuple[str,str],...]=(), root_fd: int|None=None, source: str|None=None) -> WorkerSpec:
        target=row.target.split(" ",1)[0]
        return WorkerSpec(row.session,row.child,row.role,row.owner,row.phase,row.purpose,row.admission,row.fdset,source,cwd,argv,environment,root_fd,target=target,phase=row.phase)

    def preflight_children(self, before_epoch2_reaped: Callable[[],None]|None=None) -> None:
        for epoch,row in enumerate(PRE_SUITE_CHILDREN[:2],1):
            record=self.workers.spawn(self._spec(row,cwd="/tmp",argv=("<probe>",)))
            self.channel.send(f"CGROUP_PROBE_CHILD epoch={epoch} inner_pid={record.pid}",str(epoch))
            if epoch==1:
                if self.channel.receive(lambda value:value=="CGROUP_PROBE_FROZEN epoch=1",str(epoch))!="CGROUP_PROBE_FROZEN epoch=1": fail("probe frozen")
                if self.channel.receive(lambda value:value=="CGROUP_PROBE_THAWED epoch=1",str(epoch))!="CGROUP_PROBE_THAWED epoch=1": fail("probe thawed")
                syscall(SYS_PIDFD_SEND_SIGNAL,ctypes.c_int(record.pidfd),ctypes.c_int(signal.SIGUSR1),ctypes.c_void_p(),ctypes.c_uint(0))
            else:
                if self.channel.receive(lambda value:value=="CGROUP_PROBE_KILLED epoch=2",str(epoch))!="CGROUP_PROBE_KILLED epoch=2": fail("probe killed")
            expected=0 if epoch==1 else 128+signal.SIGKILL
            if self.workers.reap(record)!=expected: fail("probe reap status")
            if epoch==2:
                if before_epoch2_reaped is None: fail("missing F12 epoch-2 boundary")
                before_epoch2_reaped()
            self.channel.send(f"CGROUP_PROBE_REAPED epoch={epoch}",str(epoch))

    def verify_checked(self) -> None:
        row=PRE_SUITE_CHILDREN[2]; source="code/generate_controls.py"
        spec=self._spec(row,cwd="@PACKAGE_FD11",argv=(source,"--verify-only","--input-dir","results"),source=source)
        record=self.workers.spawn(spec); status=self.workers.reap(record)
        if status!=0 or record.stdout or record.stderr: fail("checked-in verify-only")

    def generate_root(self, row: RegistryRow, label: str) -> CanonicalRoot:
        tree=OwnedTree(self.tmp_fd,"p15r.canonical."+label.lower()); root_fd=tree.directory("candidate"); parent_cap=tree.root_fd; parent_handle=self.objects.register(0,"ROOT_PARENT",parent_cap); root_cap=root_fd; root_handle=self.objects.register(0,"ROOT",root_cap)
        path="/tmp/"+tree.basename+"/candidate"; st=os.fstat(root_fd); source="code/generate_controls.py"
        environment=(("P15R_REPRO_ACTIVE","1"),("P15R_GENERATION_ROOT_FD","9"),("P15R_GENERATION_PURPOSE",label),("P15R_GENERATION_UID",str(st.st_uid)),("P15R_GENERATION_DEV",str(st.st_dev)),("P15R_GENERATION_INO",str(st.st_ino)))
        authorization=f"MEMBER_CREATE_AUTHORIZED session=0 child={row.child} root={root_handle} target={row.target} purpose={label} basename_set=GENERATED_NINE_V1 primitive=DIRFD_O_CREAT_O_EXCL_O_NOFOLLOW"
        def authorize_creation() -> None:
            self.channel.send(authorization,str(row.child)); expected=f"MEMBER_CREATE_ACK session=0 child={row.child} root={root_handle} purpose={label} basename_set=GENERATED_NINE_V1"
            if self.channel.receive(lambda value:value==expected,str(row.child))!=expected: fail("canonical member authorization")
        spec=self._spec(row,cwd="@PACKAGE_FD11",argv=(source,"--generate","--output-dir",path),environment=environment,root_fd=root_fd,source=source)
        record=self.workers.spawn(spec,pre_admit=authorize_creation); status=self.workers.reap(record)
        if status!=0 or record.stdout or record.stderr: fail("canonical generate+verify")
        if set(os.listdir(root_fd))!=set(GENERATED_NAMES): fail("canonical creator produced set")
        adopt_generated(tree,"candidate")
        canonical=CanonicalRoot(label,tree,parent_handle,parent_cap,root_handle,root_cap)
        for name in GENERATED_NAMES:
            fd=os.open(name,OPEN_REGULAR,dir_fd=root_fd); handle=self.objects.register(0,"ROOT_MEMBER",fd); canonical.member_handles.append((handle,fd))
        closed=f"MEMBER_LEDGER_CLOSED session=0 child={row.child} root={root_handle} count=9"; self.channel.send(closed,str(row.child)); acknowledged=closed.replace("MEMBER_LEDGER_CLOSED ","MEMBER_LEDGER_ACK ",1)
        if self.channel.receive(lambda value:value==acknowledged,str(row.child))!=acknowledged: fail("canonical creator ledger")
        self.canonical.append(canonical); return canonical

    @staticmethod
    def compare_roots(checked_fd: int, a: CanonicalRoot, b: CanonicalRoot) -> None:
        for name in GENERATED_NAMES:
            checked=read_regular_at(checked_fd,name); left=read_regular_at(a.tree.directory(a.root_relative),name); right=read_regular_at(b.tree.directory(b.root_relative),name)
            if checked!=left or left!=right or checked!=right: fail("three-way canonical bytes")

    def run_top(self, checked_path: str, a: CanonicalRoot, b: CanonicalRoot) -> None:
        row=PRE_SUITE_CHILDREN[5]; child=row.child
        self.channel.send(f"AUDIT_FD_REQUEST session=0 child={child} target=TOP_TEST_CONTROLS role=TOP_TEST_RUNNER owner=SUITE_173 purpose=NONE",str(child))
        granted,audit_fd=self.channel.control.receive_fd_matching(re.compile(rf"AUDIT_FD_GRANTED session=0 child={child} audit=(?:0|[1-9][0-9]*)")); request_audit=int(parse_exact(granted,"AUDIT_FD_GRANTED",(("session",r"0"),("child",str(child)),("audit",r"(?:0|[1-9][0-9]*)")))["audit"])
        source="code/test_controls.py"; argv=(source,"--checked-in",checked_path,"--fresh-a","/tmp/"+a.tree.basename+"/"+a.root_relative,"--fresh-b","/tmp/"+b.tree.basename+"/"+b.root_relative)
        record=self.workers.spawn(replace(self._spec(row,cwd="@PACKAGE_FD11",argv=argv,source=source),request_audit=request_audit),audit_fd)
        endpoint=record.rpc_peer
        if endpoint is None: fail("top RPC endpoint")
        self.workers.configure_streams(record)
        poller=select.poll(); poller.register(self.channel.control.sock,select.POLLIN|select.POLLHUP); poller.register(endpoint,select.POLLIN|select.POLLHUP); poller.register(record.pidfd,select.POLLIN)
        for fd in self.workers.stream_fds(record): poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
        finalized=False
        while not finalized:
            try: events=poller.poll()
            except InterruptedError: fail("top requester poll EINTR")
            if not events: fail("top requester empty poll")
            for fd,event in sorted(events,key=lambda item:(0 if item[0]==self.channel.control.sock.fileno() else (1 if item[0] in self.workers.stream_fds(record) else (2 if item[0]==endpoint.fileno() else 3)))):
                if fd==self.channel.control.sock.fileno():
                    if event&(select.POLLHUP|select.POLLERR|select.POLLNVAL): fail("top control event")
                    incoming=self.channel.receive()
                    if not self.authentication.handles(incoming): fail("top P record")
                    self.authentication.handle(incoming)
                    finalized=self.authentication.state(child).state=="FINALIZED_AWAITING_REAP"
                elif fd in self.workers.stream_fds(record):
                    self.workers.drain_stream_event(record,poller,fd,event)
                elif fd==endpoint.fileno():
                    if event&(select.POLLERR|select.POLLNVAL): fail("top FD4 poll event")
                    if self.authentication.state(child).state not in ("CREATE_ARMED","ACTIVE_AUTHORIZED"): continue
                    frame=rpc_receive(endpoint,record.pid)
                    if frame is None: fail("top FD4 early EOF")
                    self.rpc.handle(record,frame)
                elif fd==record.pidfd:
                    if not finalized: fail("top crash before finalize")
                else: fail("top requester unknown poll fd")
        status=self.workers.reap(record,self.authentication.state(child))
        if status!=0 or record.stdout or record.stderr: fail("suite 173")
        if self.authentication.state(child).state!="AUTH_REAP_RECONCILED": fail("top auth final state")

    @staticmethod
    def _adopt_interrupted_generation(tree: OwnedTree, relative: str) -> None:
        directory=tree.directory(relative)
        for name in GENERATED_NAMES:
            path=relative+"/"+name if relative else name
            if path in tree.files: continue
            try: member=os.stat(name,dir_fd=directory,follow_symlinks=False)
            except FileNotFoundError: continue
            if not stat.S_ISREG(member.st_mode) or member.st_nlink!=1: fail("interrupted generation member")
            tree.adopt(path)

    def _close_setup_sources(self) -> None:
        aliases=(self.workers.repository_fd,self.rpc.repository_fd,self.workers.package_fd,self.rpc.package_fd,self.package_fd)
        if aliases==(-1,-1,-1,-1,-1): return
        if aliases!=(10,10,11,11,11): fail("G setup source alias ownership")
        package_fd=self.workers.package_fd; close_proved(package_fd)
        self.workers.package_fd=-1; self.rpc.package_fd=-1; self.package_fd=-1; package_fd=-1
        repository_fd=self.workers.repository_fd; close_proved(repository_fd)
        self.workers.repository_fd=-1; self.rpc.repository_fd=-1; repository_fd=-1

    def _cleanup_all_capabilities(self) -> str:
        trees: dict[int,tuple[OwnedTree,int,str]]={}
        for canonical in self.canonical:
            trees[id(canonical.tree)]=(canonical.tree,0,canonical.root_relative)
        for session in self.rpc.sessions.values():
            if session.tree is not None: trees[id(session.tree)]=(session.tree,session.session,session.result_relative)
            if session.lock_tree is not None: trees[id(session.lock_tree)]=(session.lock_tree,session.session,"")
            if session.signal_tree is not None: trees[id(session.signal_tree)]=(session.signal_tree,session.session,"")
        if self.lock_tree is not None: trees[id(self.lock_tree)]=(self.lock_tree,0,"")
        session_outcomes: dict[int,list[str]]={}
        for session in self.rpc.sessions.values():
            retained=[value for value in (session.outcome,session.foreign_outcome,session.lock_foreign_outcome) if value in OUTCOMES and value!="UNSET"]
            if retained: session_outcomes[session.session]=retained
        for tree,session,generated_relative in reversed(tuple(trees.values())):
            if tree.cleaned: continue
            if generated_relative: self._adopt_interrupted_generation(tree,generated_relative)
            if tree.foreign_identity is not None and not tree.foreign_exchanged: tree.cancel_unexchanged_foreign_fixture()
            if not tree.members_cleaned: tree.cleanup_members()
            tree.cleanup_directories()
            session_outcomes.setdefault(session,[]).append("FOREIGN_RETAINED" if tree.foreign_audited else "ABSENT")
        for session in self.rpc.sessions.values():
            if session.lock_socket is not None: session.lock_socket.close(); session.lock_socket=None
            session.signal_acquiring_token=""; session.signal_foreign_receipt=None
        if self.global_lock is not None: self.global_lock.close(); self.global_lock=None
        live=tuple(sorted(self.objects.live.items(),reverse=True))
        for handle,identity in live:
            fd=self.objects.capabilities.get(handle,-1)
            if fd>=0:
                try: observed=os.fstat(fd)
                except OSError as error:
                    if error.errno!=errno.EBADF: raise
                else:
                    if (observed.st_dev,observed.st_ino)!=(identity.dev,identity.ino): fail("final capability ABA")
                    close_proved(fd)
            self.objects.release_closed(handle,(identity.dev,identity.ino))
        per_handle=[]
        for handle,identity in sorted(tuple(self.objects.pending_released.items()),reverse=True):
            outcome=combine_outcomes(session_outcomes.get(identity.session,("ABSENT",)))
            self.channel.send(f"CLEANUP_RESULT session=0 handle={handle} outcome={outcome}")
            per_handle.append(outcome); self.objects.pending_released.pop(handle)
        self._close_setup_sources()
        for fd_name in ("package_fd","repository_fd","proc_root","workers_fd"):
            fd=getattr(self.workers,fd_name)
            if fd==-1: continue
            if fd<0 or not fd_is_open(fd): fail("final descriptor ownership")
            close_proved(fd)
            setattr(self.workers,fd_name,-1)
        if self.tmp_fd>=0 and fd_is_open(self.tmp_fd): close_proved(self.tmp_fd)
        self.tmp_fd=-1; self.lock_parent_cap=-1; self.lock_member_cap=-1
        if self.objects.live or self.objects.capabilities or self.objects.pending_released: fail("final object ledger")
        if self.workers.live or any(record.state not in ("REAPED","CONTAINED_REAPED") or not record.process_gone or not record.proc_closed or not record.descriptor_empty for record in self.workers.completed.values()): fail("final worker tombstone ledger")
        aggregate=combine_outcomes(per_handle or ("ABSENT",))
        self.channel.send(f"CLEANUP_RESULT session=0 handle=0 outcome={aggregate}")
        return aggregate

    def global_final(self) -> None:
        self.channel.finalizing=True
        signalled=bool(self.channel.pending_signal)
        if not signalled and (not self.authentication.states or any(state.state!="AUTH_REAP_RECONCILED" for state in self.authentication.states.values())): fail("auth reap reconciliation incomplete")
        if signalled: self.authentication.signal_containment(self.channel.pending_signal)
        self.channel.send("FREEZE_REQUEST session=0 handle=0 phase=FINAL")
        frozen=self.channel.receive(lambda value:value.partition(" ")[0]=="FROZEN_FINAL")
        frozen_values=parse_exact(frozen,"FROZEN_FINAL",(("session",r"0"),("handle",r"0"),("phase",r"FINAL"),("epoch",r"[1-9][0-9]*"))); epoch=frozen_values["epoch"]
        if self.channel.pending_signal and not signalled:
            signalled=True; self.authentication.signal_containment(self.channel.pending_signal)
        self.channel.send(f"KILL_REQUEST session=0 epoch={epoch}")
        killed=f"KILL_ISSUED session=0 epoch={epoch}"
        if self.channel.receive(lambda value:value==killed)!=killed: fail("KILL_ISSUED")
        if self.channel.pending_signal and not signalled:
            signalled=True; self.authentication.signal_containment(self.channel.pending_signal)
        if self.workers.live:
            if not signalled: fail("global live worker ledger")
            self.workers.contain_all()
        self.channel.send(f"REAPED session=0 epoch={epoch}")
        empty=f"CGROUP_EMPTY session=0 epoch={epoch}"
        if self.channel.receive(lambda value:value==empty)!=empty: fail("CGROUP_EMPTY")
        self.channel.poll_signal()
        if self.channel.pending_signal and not signalled:
            signalled=True; self.authentication.signal_containment(self.channel.pending_signal)
        outcome=self._cleanup_all_capabilities()
        self.channel.poll_signal()
        if self.channel.pending_signal and not signalled:
            signalled=True; self.authentication.signal_containment(self.channel.pending_signal)
        if signalled: self.channel.send(f"SIGNAL_CLEANED signo={self.channel.pending_signal} outcome={outcome}")
        self.channel.send(f"EXIT status=0 outcome={outcome}")

    def run_after_preflight(self, seal_fence: V14SealFence) -> None:
        seal_fence.validate()
        if self.workers.seal_fence is not seal_fence or self.workers.actual_endpoint_fd<0: fail("Seal fence ownership")
        self.global_lock=socket.socket(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
        try: self.global_lock.bind(self.rpc.global_lock_name)
        except OSError as error:
            if error.errno==errno.EADDRINUSE: fail("abstract package lock",token="E_CONCURRENT_ENTRY")
            raise
        candidate=".p15r-lock-candidate."+sha256(self.rpc.global_lock_name)[:20]; fixed="p15r-wieferich-ulm-controls-0.lock"
        self.lock_tree=OwnedTree(self.tmp_fd,candidate); owner_st=os.fstat(self.lock_tree.root_fd); token=sha256(f"P15R-LOCK-OWNER-v1:0:{owner_st.st_dev}:{owner_st.st_ino}:{candidate}".encode("ascii"))
        self.lock_parent_cap=self.tmp_fd; self.lock_parent_handle=self.objects.register(0,"LOCK_PARENT",self.lock_parent_cap); self.lock_handle=self.objects.register(0,"LOCK",self.lock_tree.root_fd)
        self.lock_tree.write(".owner",f"P15R-LOCK-OWNER-v1 {token}\n".encode("ascii")); self.lock_member_cap=os.open(".owner",OPEN_REGULAR,dir_fd=self.lock_tree.root_fd); self.lock_member_handle=self.objects.register(0,"LOCK_MEMBER",self.lock_member_cap)
        renameat2(self.tmp_fd,candidate,self.tmp_fd,fixed,RENAME_NOREPLACE); installed=os.stat(fixed,dir_fd=self.tmp_fd,follow_symlinks=False)
        if (installed.st_dev,installed.st_ino)!=(owner_st.st_dev,owner_st.st_ino): fail("lock candidate install")
        self.lock_tree.basename=fixed; self.lock_tree.owned_basename=fixed
        self.channel.send(f"LOCK_BOUND session=0 lock={self.lock_handle}")
        self.verify_checked()
        first=self.generate_root(PRE_SUITE_CHILDREN[3],"CANONICAL_A")
        second=self.generate_root(PRE_SUITE_CHILDREN[4],"CANONICAL_B")
        checked_fd=openat2(self.package_fd,"results",OPEN_DIR)
        try: self.compare_roots(checked_fd,first,second)
        finally: os.close(checked_fd)
        self.run_top("results",first,second)
        if self.workers.live: fail("post-suite worker residue")
        self._close_setup_sources()
        self.global_final()


class CopiedRequester:
    def __init__(self, method: str, trigger: str) -> None:
        self.rpc=socket.socket(fileno=4); self.audit=socket.socket(fileno=5); self.method=method; self.trigger=trigger
        try: self.logical_session=int(os.environ["P15R_COPIED_SESSION"])
        except (KeyError,ValueError): fail("copied logical session")
        if self.logical_session<=0: fail("copied logical session")
        self.audit_id=int(P15R_AUDIT_HANDLE); self.auth_serial=int(P15R_AUTH_SERIAL)
        if self.audit_id<0 or self.auth_serial!=0: fail("P-owned endpoint coordinates")
        self.spawn_serial=0; self.request=1; self.auth=0; self.session=0; self.active_cap=""; self.pending_spawns: dict[int,bytes]={}; self.consumed_spawn_children: set[int]=set(); self.authenticate()

    def bare_send_bytes(self, payload: bytes) -> None:
        if not payload or len(payload)>MAX_FRAME or b"\x00" in payload or b"\n" in payload or not payload.isascii() or self.audit.send(payload)!=len(payload): fail("copied FD5 send")

    def framed_send_payload(self, payload: bytes) -> None:
        if not payload or len(payload)>MAX_FRAME or b"\x00" in payload or b"\n" in payload or not payload.isascii(): fail("copied FD4 payload")
        packet=struct.pack(">I",len(payload))+payload
        if self.rpc.send(packet)!=len(packet): fail("copied FD4 payload send")

    def bare_receive(self) -> str:
        data,ancillary,flags,_address=self.audit.recvmsg(MAX_FRAME+1,1)
        if ancillary or flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or not data or b"\x00" in data or b"\n" in data or not data.isascii(): fail("copied FD5")
        return data.decode("ascii")

    def framed_receive(self) -> tuple[str,bytes]:
        packet,ancillary,flags,_address=self.rpc.recvmsg(MAX_FRAME+5,1)
        if ancillary or flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or len(packet)<5: fail("copied FD4")
        size=struct.unpack(">I",packet[:4])[0]; payload=packet[4:]
        if size!=len(payload) or not payload.isascii(): fail("copied FD4 frame")
        return payload.decode("ascii"),packet

    def authenticate(self) -> None:
        send_bare(self.audit,f"SESSION_AUTH_OPEN audit={self.audit_id} auth_serial={self.auth_serial} request=1 method={self.method} trigger={self.trigger} owner=COPIED_REPRODUCE")
        challenge=parse_exact(self.bare_receive(),"SESSION_AUTH_CHALLENGE",(("audit",str(self.audit_id)),("auth_serial",str(self.auth_serial)),("auth",r"[1-9][0-9]*"),("session",r"[1-9][0-9]*")))
        self.auth=int(challenge["auth"]); self.session=int(challenge["session"])
        registration=f"request=1 method={self.method} trigger={self.trigger} owner=COPIED_REPRODUCE fd4_inode={os.fstat(4).st_ino} rpc_inner_pid={os.getpid()} rpc_inner_uid=0 rpc_inner_gid=0".encode("ascii"); digest=sha256(registration)
        send_bare(self.audit,f"SESSION_AUTH_REGISTERED audit={self.audit_id} auth_serial={self.auth_serial} auth={self.auth} session={self.session} request=1 method={self.method} trigger={self.trigger} owner=COPIED_REPRODUCE registration={registration.hex()} digest={digest}")
        receipt=parse_exact(self.bare_receive(),"SESSION_AUTH_RECEIPT",(("audit",str(self.audit_id)),("auth_serial",str(self.auth_serial)),("auth",str(self.auth)),("session",str(self.session)),("request",r"1"),("digest",re.escape(digest)),("create_cap",r"[0-9a-f]{64}"),("create",r"(?:[0-9a-f]{2})+")))
        frame=bytes.fromhex(receipt["create"])
        if receipt["create_cap"].encode("ascii") not in frame or self.rpc.send(frame)!=len(frame): fail("copied create")
        created,_packet=self.framed_receive(); values=parse_exact(created,"SESSION_CREATED",(("request",r"1"),("session",str(self.session)),("reply_nonce",r"[0-9a-f]{64}")))
        created_bytes=created.encode("ascii")
        send_bare(self.audit,f"SESSION_AUTH_ACTIVATED audit={self.audit_id} auth_serial={self.auth_serial} auth={self.auth} session={self.session} request=1 reply_nonce={values['reply_nonce']} created={created_bytes.hex()}")
        active=parse_exact(self.bare_receive(),"SESSION_AUTH_ACTIVE_RECEIPT",(("audit",str(self.audit_id)),("auth_serial",str(self.auth_serial)),("auth",str(self.auth)),("session",str(self.session)),("request",r"1"),("active_cap",r"[0-9a-f]{64}"),("created_digest",re.escape(sha256(created_bytes)))))
        self.active_cap=active["active_cap"]

    def audited_spawn(self, core: str, trigger: str) -> bytes:
        serial=self.spawn_serial
        send_bare(self.audit,f"AUDIT_OPEN audit={self.audit_id} serial={serial}")
        challenge=parse_exact(self.bare_receive(),"AUDIT_CHALLENGE",(("audit",str(self.audit_id)),("serial",str(serial)),("nonce",r"[0-9a-f]{64}")))
        core_bytes=core.encode("ascii"); digest=sha256(core_bytes)
        outer=f"AUDITED_SPAWN audit={self.audit_id} serial={serial} nonce={challenge['nonce']} digest={digest} trigger={trigger} core={core_bytes.hex()}".encode("ascii")
        self.bare_send_bytes(outer)
        receipt=parse_exact(self.bare_receive(),"AUDIT_RECEIPT",(("audit",str(self.audit_id)),("serial",str(serial)),("nonce",re.escape(challenge["nonce"])),("digest",re.escape(digest))))
        if (receipt["nonce"],receipt["digest"])!=(challenge["nonce"],digest): fail("copied audit receipt join")
        self.spawn_serial+=1
        return outer

    def prepare_spawn(self, target: str, purpose: str, handle: int, trigger: str) -> tuple[int,bytes]:
        self.request+=1; request=self.request
        core=f"SPAWN request={request} session={self.logical_session} target={target} method={self.method} purpose={purpose} handle={handle}"
        outer=self.audited_spawn(core,trigger)
        if request in self.pending_spawns: fail("duplicate pending spawn")
        self.pending_spawns[request]=outer
        return request,outer

    def receive_spawn(self, request: int) -> tuple[int,bytes,bytes]:
        pending=self.pending_spawns.get(request)
        if pending is None: fail("spawn result without pending authorization")
        outer=parse_exact(pending.decode("ascii"),"AUDITED_SPAWN",(("audit",r"(?:0|[1-9][0-9]*)"),("serial",r"(?:0|[1-9][0-9]*)"),("nonce",r"[0-9a-f]{64}"),("digest",r"[0-9a-f]{64}"),("trigger",r"[A-Z0-9_]+"),("core",r"(?:[0-9a-f]{2})+")))
        core=parse_exact(bytes.fromhex(outer["core"]).decode("ascii"),"SPAWN",(("request",str(request)),("session",str(self.logical_session)),("target",r"[A-Z0-9_]+"),("method",re.escape(self.method)),("purpose",r"[A-Z0-9_]+"),("handle",r"[0-9]+")))
        stdout=bytearray(); stderr=bytearray(); stdout_sequence=stderr_sequence=0
        while True:
            record,_packet=self.framed_receive()
            stdout_match=re.fullmatch(rf"SPAWN_STDOUT request={request} seq=([0-9]+) hex=([0-9a-f]*)",record)
            stderr_match=re.fullmatch(rf"SPAWN_STDERR request={request} seq=([0-9]+) hex=([0-9a-f]*)",record)
            result_match=re.fullmatch(rf"SPAWN_RESULT request={request} audit=({re.escape(outer['audit'])}) serial=({re.escape(outer['serial'])}) nonce=({re.escape(outer['nonce'])}) digest=({re.escape(outer['digest'])}) outer_sha256=({sha256(pending)}) target=({re.escape(core['target'])}) method=({re.escape(core['method'])}) purpose=({re.escape(core['purpose'])}) handle=({re.escape(core['handle'])}) child=([1-9][0-9]*) status=([0-9]+) outcome=EXITED stdout_bytes=([0-9]+) stderr_bytes=([0-9]+) stdout_chunks=([0-9]+) stderr_chunks=([0-9]+) stdout_sha256=([0-9a-f]{{64}}) stderr_sha256=([0-9a-f]{{64}}) capability_sha256=([0-9a-f]{{64}})",record)
            if stdout_match is not None:
                if int(stdout_match.group(1))!=stdout_sequence: fail("copied stdout sequence")
                encoded=stdout_match.group(2)
                if len(encoded)>2048 or len(encoded)%2: fail("copied stdout chunk")
                chunk=bytes.fromhex(encoded)
                if len(stdout)+len(chunk)>WORKER_STREAM_BYTE_CEILING: fail("copied stdout ceiling")
                stdout.extend(chunk); stdout_sequence+=1
            elif stderr_match is not None:
                if int(stderr_match.group(1))!=stderr_sequence: fail("copied stderr sequence")
                encoded=stderr_match.group(2)
                if len(encoded)>2048 or len(encoded)%2: fail("copied stderr chunk")
                chunk=bytes.fromhex(encoded)
                if len(stderr)+len(chunk)>WORKER_STREAM_BYTE_CEILING: fail("copied stderr ceiling")
                stderr.extend(chunk); stderr_sequence+=1
            elif result_match is not None:
                child=int(result_match.group(10)); status=int(result_match.group(11))
                if child in self.consumed_spawn_children or int(result_match.group(12))!=len(stdout) or int(result_match.group(13))!=len(stderr) or int(result_match.group(14))!=stdout_sequence or int(result_match.group(15))!=stderr_sequence: fail("copied spawn cardinality")
                if sha256(bytes(stdout))!=result_match.group(16) or sha256(bytes(stderr))!=result_match.group(17): fail("copied spawn digest")
                core_text=record.rsplit(" capability_sha256=",1)[0]; core_bytes=core_text.encode("ascii")
                if sha256(b"P15R-SPAWN-RESULT-CAP-v1"+u64be(len(core_bytes))+core_bytes)!=result_match.group(18): fail("copied spawn capability")
                self.pending_spawns.pop(request); self.consumed_spawn_children.add(child)
                return status,bytes(stdout),bytes(stderr)
            else: fail("copied spawn reply enum")

    def spawn(self, target: str, purpose: str, handle: int, trigger: str) -> tuple[int,bytes,bytes]:
        request,payload=self.prepare_spawn(target,purpose,handle,trigger); self.framed_send_payload(payload)
        return self.receive_spawn(request)

    def signal_lock_pair(self) -> tuple[tuple[int,bytes,bytes],tuple[int,bytes,bytes]]:
        holder_request,holder=self.prepare_spawn("LOCK_HOLDER","NONE",0,self.trigger)
        contender_request,contender=self.prepare_spawn("LOCK_CONTENDER","NONE",0,self.trigger)
        self.framed_send_payload(holder); self.framed_send_payload(contender)
        return self.receive_spawn(holder_request),self.receive_spawn(contender_request)

    def close(self) -> None:
        self.request+=1; request=self.request
        text=f"SESSION_CLOSE request={request} session={self.session} active_cap={self.active_cap}"; payload=text.encode("ascii"); packet=struct.pack(">I",len(payload))+payload
        if self.rpc.send(packet)!=len(packet): fail("copied close")
        terminal,terminal_packet=self.framed_receive()
        values=parse_exact(terminal,"SESSION_CLOSED",(("request",str(request)),("session",str(self.session)),("outcome",OUTCOME_RE),("terminal_cap",r"[0-9a-f]{64}")))
        digest=sha256(b"P15R-TERMINAL-REPLY-v7 "+terminal_packet)
        send_bare(self.audit,f"SESSION_AUTH_TERMINAL_OBSERVED audit={self.audit_id} auth_serial={self.auth_serial} auth={self.auth} session={self.session} close_request={request} outcome={values['outcome']} terminal_cap={values['terminal_cap']} reply_digest={digest} reply={terminal_packet.hex()}")
        parse_exact(self.bare_receive(),"SESSION_AUTH_TERMINAL_RECEIPT",(("audit",str(self.audit_id)),("auth_serial",str(self.auth_serial)),("auth",str(self.auth)),("session",str(self.session)),("close_request",str(request)),("outcome",re.escape(values["outcome"])),("terminal_cap_sha256",r"[0-9a-f]{64}"),("reply_digest",re.escape(digest))))
        self.rpc.close(); self.audit.close()


def consume_worker_signal(signal_fd: int, expected_signal: int) -> None:
    poller=select.poll(); poller.register(signal_fd,select.POLLIN|select.POLLHUP|select.POLLERR)
    events=poller.poll()
    if len(events)!=1 or events[0][0]!=signal_fd or events[0][1]&(select.POLLHUP|select.POLLERR) or not events[0][1]&select.POLLIN: fail("copied signal readiness")
    receipt=os.read(signal_fd,128)
    if len(receipt)!=128: fail("copied signal receipt size")
    signo,signal_errno,signal_code,source_pid,source_uid=struct.unpack_from("=IiiII",receipt,0)
    if signo!=expected_signal or signal_errno!=0 or signal_code!=0 or source_pid!=os.getppid() or source_pid!=1 or source_uid!=0 or poller.poll(0): fail("copied signal receipt identity")


def metadata_receipt(package: str) -> list[tuple[object,...]]:
    root=os.open(package,OPEN_DIR); stack=[(".",root)]; records=[]
    try:
        while stack:
            relative,directory_fd=stack.pop()
            for name in sorted(os.listdir(directory_fd),key=lambda value:value.encode("utf-8"),reverse=True):
                child=name if relative=="." else relative+"/"+name
                if not child.startswith(("code/","experiments/","results/")): continue
                st=os.stat(name,dir_fd=directory_fd,follow_symlinks=False)
                repository_relative="papers/15-wieferich-ulm-packet-bases/"+child
                if stat.S_ISDIR(st.st_mode):
                    fd=os.open(name,OPEN_DIR,dir_fd=directory_fd); stack.append((child,fd)); records.append((repository_relative,"DIRECTORY",stat.S_IMODE(st.st_mode),0,"",st.st_mtime_ns,st.st_ctime_ns,st.st_nlink,st.st_dev,st.st_ino))
                elif stat.S_ISREG(st.st_mode):
                    fd=os.open(name,OPEN_REGULAR,dir_fd=directory_fd)
                    try: data=read_all(fd)
                    finally: os.close(fd)
                    records.append((repository_relative,"REGULAR",stat.S_IMODE(st.st_mode),len(data),sha256(data),st.st_mtime_ns,st.st_ctime_ns,st.st_nlink,st.st_dev,st.st_ino))
                else: records.append((repository_relative,"OTHER",stat.S_IMODE(st.st_mode),0,"",st.st_mtime_ns,st.st_ctime_ns,st.st_nlink,st.st_dev,st.st_ino))
            if directory_fd!=root: os.close(directory_fd)
        return sorted(records,key=lambda row:str(row[0]).encode("utf-8"))
    finally: os.close(root)


def copied_reproduce_action(client: CopiedRequester) -> tuple[int,bytes,bytes]:
    package=os.environ["P15R_COPIED_PACKAGE"]; root=os.environ["P15R_COPIED_ROOT"]
    if os.environ.get("P15R_REPRO_ACTIVE")=="1": return 1,b"",b"E_RECURSIVE_ENTRY\n"
    if "--repair" in sys.argv: return 1,b"",b"E_VERIFY_ONLY_WRITE\n"
    if os.environ.get("P15R_TEST_ABORT_AFTER_FRESH_A")=="1":
        root_fd=os.open(root,OPEN_DIR); probe_name="cleanup-denial"
        try:
            os.mkdir(probe_name,0o700,dir_fd=root_fd); probe_fd=os.open(probe_name,OPEN_DIR,dir_fd=root_fd)
            try:
                member=os.open("owned",os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW|os.O_CLOEXEC,0o600,dir_fd=probe_fd); os.close(member)
                os.fchmod(probe_fd,0)
                try: os.unlink("owned",dir_fd=probe_fd)
                except OSError as error:
                    if error.errno not in (errno.EACCES,errno.EPERM): raise
                    detector=b"E_CLEANUP\n"
                else: fail("cleanup denial not enforced")
                os.fchmod(probe_fd,0o700); os.unlink("owned",dir_fd=probe_fd)
            finally: os.close(probe_fd)
            os.rmdir(probe_name,dir_fd=root_fd)
        finally: os.close(root_fd)
        return 1,b"",detector
    cache_hits=[]
    pending=[os.open(root,OPEN_DIR)]
    try:
        while pending:
            directory=pending.pop()
            try:
                for name in os.listdir(directory):
                    st=os.stat(name,dir_fd=directory,follow_symlinks=False)
                    if name=="__pycache__": cache_hits.append((st.st_dev,st.st_ino))
                    if stat.S_ISDIR(st.st_mode): pending.append(os.open(name,OPEN_DIR,dir_fd=directory))
            finally: os.close(directory)
    finally:
        for directory in pending: os.close(directory)
    if cache_hits: return 1,b"",b"E_CACHE_POST\n"
    if os.environ.get("P15R_LOCK_PROBE")=="1":
        status,stdout,stderr=client.spawn("LOCK_CONTENDER","NONE",0,client.trigger)
        if (status,stdout,stderr)!=(74,b"",b"E_CONCURRENT_ENTRY\n"): fail("delegated contender result")
        return 1,b"",b"E_CONCURRENT_ENTRY\n"
    before=metadata_receipt(package); after=metadata_receipt(package)
    if before!=after: return 1,b"",b"E_VERIFY_ONLY_METADATA\n"
    return 0,canonical_json_bytes({"after":after,"before":before}),b""


def copied_reproduce_worker() -> int:
    method=os.environ.get("P15R_COPIED_METHOD",""); trigger=os.environ.get("P15R_COPIED_TRIGGER","NONE")
    client=CopiedRequester(method,trigger)
    if trigger=="P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN":
        if method!="test_rep_009": fail("copied signal authority")
        signal_fd=make_signalfd()
        try:
            holder,contender=client.signal_lock_pair()
            if holder!=(0,b"HOLDER_READY\n",b"") or contender!=(74,b"",b"E_CONCURRENT_ENTRY\n"): fail("signal lock pair receipt")
            consume_worker_signal(signal_fd,signal.SIGTERM)
        finally:
            if fd_is_open(signal_fd): close_proved(signal_fd)
        client.close()
        complete_write(2,b"E_SIGNAL_ACQUIRE\n")
        return 1
    status,stdout,stderr=copied_reproduce_action(client)
    client.close()
    complete_write(1,stdout); complete_write(2,stderr)
    return status


def lock_contender_worker() -> int:
    if os.environ.get("P15R_WORKER_ROLE")!="LOCK_CONTENDER": return 125
    try: address=bytes.fromhex(os.environ["P15R_LOCK_ADDRESS_HEX"])
    except (KeyError,ValueError): return 125
    method=os.environ.get("P15R_LOCK_METHOD"); trigger=os.environ.get("P15R_LOCK_TRIGGER")
    authorized=(method,trigger)==("test_package_p22_concurrent_second_entry","NONE") and re.fullmatch(rb"\x00/tmp/p15r\.[0-9a-f]{40}\.lock",address) is not None
    authorized=authorized or ((method,trigger)==("test_rep_009","P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN") and re.fullmatch(rb"\x00/tmp/p15r-isolated\.[1-9][0-9]*\.lock",address) is not None)
    if not authorized or len(address)>107: return 125
    contender=socket.socket(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
    try:
        try: contender.bind(address)
        except OSError as error:
            if error.errno!=errno.EADDRINUSE: raise
            complete_write(2,b"E_CONCURRENT_ENTRY\n")
            return 74
        return 125
    finally: contender.close()


def lock_holder_worker() -> int:
    if os.environ.get("P15R_WORKER_ROLE")!="LOCK_HOLDER" or (os.environ.get("P15R_LOCK_METHOD"),os.environ.get("P15R_LOCK_TRIGGER"))!=("test_rep_009","P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN"): return 125
    try: address=bytes.fromhex(os.environ["P15R_LOCK_ADDRESS_HEX"])
    except (KeyError,ValueError): return 125
    if re.fullmatch(rb"\x00/tmp/p15r-isolated\.[1-9][0-9]*\.lock",address) is None or len(address)>107: return 125
    holder=socket.socket(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
    try:
        holder.bind(address); complete_write(1,b"HOLDER_READY\n")
        return 0 if signal.sigwait((signal.SIGUSR1,))==signal.SIGUSR1 else 125
    finally: holder.close()


def replacement_actor_worker() -> int:
    parent=os.environ.get("P15R_REPLACE_PARENT",""); fixed=os.environ.get("P15R_REPLACE_FIXED",""); internal=os.environ.get("P15R_REPLACE_INTERNAL","")
    triggers=[name for name in ("P15R_TEST_REPLACE_CANONICAL_ROOT","P15R_TEST_REPLACE_MUTATION_ROOT","P15R_TEST_REPLACE_P25_ROOT","P15R_TEST_REPLACE_LOCK_ACQUIRING","P15R_TEST_REPLACE_LOCK_CLEANING") if os.environ.get(name)=="1"]
    method=os.environ.get("P15R_REPLACE_METHOD",""); purpose=os.environ.get("P15R_REPLACE_PURPOSE","")
    allowed={("P15R_TEST_REPLACE_CANONICAL_ROOT","test_rep_009","CANONICAL_A"),("P15R_TEST_REPLACE_MUTATION_ROOT","test_package_p25_nonempty_generation_root","MUTATION_P25_V1"),("P15R_TEST_REPLACE_P25_ROOT","test_package_p25_nonempty_generation_root","MUTATION_P25_V1"),("P15R_TEST_REPLACE_LOCK_ACQUIRING","test_rep_009","NONE"),("P15R_TEST_REPLACE_LOCK_CLEANING","test_rep_009","NONE")}
    if os.environ.get("P15R_TEST_CONTEXT")!="1" or len(triggers)!=1 or (triggers[0],method,purpose) not in allowed or not parent.startswith("/tmp/p15r.") or re.fullmatch(r"[A-Za-z0-9_.-]+",fixed) is None or re.fullmatch(r"\.owner\.[0-9a-f]{20}",internal) is None: return 125
    try:
        owned_expected=(int(os.environ["P15R_REPLACE_OWNED_DEV"]),int(os.environ["P15R_REPLACE_OWNED_INO"]))
        foreign_expected=(int(os.environ["P15R_REPLACE_FOREIGN_DEV"]),int(os.environ["P15R_REPLACE_FOREIGN_INO"]))
    except (KeyError,ValueError): return 125
    parent_fd=os.open(parent,OPEN_DIR)
    try:
        owned=os.stat(fixed,dir_fd=parent_fd,follow_symlinks=False); foreign=os.stat(internal,dir_fd=parent_fd,follow_symlinks=False)
        if (owned.st_dev,owned.st_ino)!=owned_expected or (foreign.st_dev,foreign.st_ino)!=foreign_expected: return 125
        renameat2(parent_fd,fixed,parent_fd,internal,RENAME_EXCHANGE)
        fixed_after=os.stat(fixed,dir_fd=parent_fd,follow_symlinks=False); internal_after=os.stat(internal,dir_fd=parent_fd,follow_symlinks=False)
        if (fixed_after.st_dev,fixed_after.st_ino)!=foreign_expected or (internal_after.st_dev,internal_after.st_ino)!=owned_expected: return 125
        complete_write(1,f"EXCHANGED fixed_dev={fixed_after.st_dev} fixed_ino={fixed_after.st_ino} internal_dev={internal_after.st_dev} internal_ino={internal_after.st_ino}\n".encode("ascii"))
        return 0
    finally: close_proved(parent_fd)


def write_proc_map(proc_root: int, pid: int, name: str, data: bytes) -> None:
    if (name,data) not in (("uid_map",b"65534 65534 1\n"),("gid_map",b"65534 65534 1\n"),("setgroups",b"deny\n")):
        fail("U1 map contract")
    process=openat2(proc_root,str(pid),OPEN_PATH_DIR)
    try:
        fd=os.open(name,os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=process)
        try: complete_write(fd,data)
        finally: close_proved(fd)
        if read_control_at(process,name)!=data: fail("id map byte verification")
    finally: close_proved(process)


def bootstrap_send(endpoint: socket.socket, record: str) -> None:
    if not record.isascii() or "\x00" in record or "\n" in record or len(record)>MAX_FRAME: fail("bootstrap send grammar")
    packet=record.encode("ascii")
    if endpoint.send(packet)!=len(packet): fail("bootstrap send")


def bootstrap_receive(endpoint: socket.socket, expected: str) -> None:
    packet,ancillary,flags,address=endpoint.recvmsg(MAX_FRAME+1,1)
    if packet!=expected.encode("ascii") or ancillary or flags or address not in (None,"",b""): fail("bootstrap receive")


def bootstrap_require_eof(endpoint: socket.socket) -> None:
    packet,ancillary,flags,address=endpoint.recvmsg(1,1)
    if packet or ancillary or flags or address not in (None,"",b""): fail("bootstrap terminal EOF")


def current_fsids() -> tuple[int,int]:
    fsuid=syscall(SYS_SETFSUID,ctypes.c_int(-1)); fsgid=syscall(SYS_SETFSGID,ctypes.c_int(-1))
    return fsuid,fsgid


def require_ids(expected: int, detail: str) -> None:
    if os.getresuid()!=(expected,expected,expected) or os.getresgid()!=(expected,expected,expected) or current_fsids()!=(expected,expected): fail(detail)


def attest_outer_launcher(proc_root: int, launcher_pid: int) -> None:
    process=openat2(proc_root,str(launcher_pid),OPEN_PATH_DIR)
    try: status=parse_proc_status(read_regular_at(process,"status",1024*1024))
    finally: close_proved(process)
    uid=tuple(int(value) for value in status.get("Uid","").split()); gid=tuple(int(value) for value in status.get("Gid","").split())
    if uid!=(65534,)*4 or gid!=(65534,)*4 or status.get("Groups","") or status.get("Threads")!="1": fail("outer launcher IDs")
    if any(status.get(name)!="0000000000000000" for name in ("CapInh","CapPrm","CapEff","CapAmb")): fail("outer launcher capabilities")


def attest_launcher_placement(proc_root: int, launcher_pid: int, launcher_pidfd: int, parent_pid: int, tree: CgroupTree) -> None:
    if fcntl.fcntl(launcher_pidfd,fcntl.F_GETFD)!=FD_CLOEXEC: fail("launcher pidfd CLOEXEC")
    process=openat2(proc_root,str(launcher_pid),OPEN_PATH_DIR)
    try:
        status=parse_proc_status(read_regular_at(process,"status",1024*1024)); cgroup=read_regular_at(process,"cgroup",1024*1024); proc_start_time(process,launcher_pid)
    finally: close_proved(process)
    nspid=tuple(int(value) for value in status.get("NSpid","").split()); uid=tuple(int(value) for value in status.get("Uid","").split()); gid=tuple(int(value) for value in status.get("Gid","").split())
    if status.get("PPid")!=str(parent_pid) or not nspid or nspid[-1]!=launcher_pid or uid!=(0,)*4 or gid!=(0,)*4 or cgroup!=("0::"+tree.relative("guardian")+"\n").encode("ascii"): fail("launcher placement proc")
    tree.require_member(tree.guardian_fd,launcher_pid)


def validate_p_signal_barrier() -> None:
    blocked=frozenset(int(number) for number in signal.pthread_sigmask(signal.SIG_BLOCK,()))
    if blocked!=frozenset(int(number) for number in HANDLED_SIGNALS): fail("P signal mask barrier")
    for number in sorted(int(value) for value in signal.valid_signals()):
        if number in (int(signal.SIGKILL),int(signal.SIGSTOP)): continue
        disposition=signal.getsignal(number)
        if disposition is not None and disposition!=signal.SIG_DFL: fail("P signal disposition barrier")


def make_signalfd() -> int:
    for number in sorted(int(value) for value in signal.valid_signals()):
        if number not in (int(signal.SIGKILL),int(signal.SIGSTOP)) and signal.getsignal(number) is not None: signal.signal(number,signal.SIG_DFL)
    signal.pthread_sigmask(signal.SIG_SETMASK,HANDLED_SIGNALS)
    validate_p_signal_barrier()
    mask=ctypes.c_uint64(0)
    for number in HANDLED_SIGNALS: mask.value|=1<<(number-1)
    return syscall(SYS_SIGNALFD4,ctypes.c_int(-1),ctypes.byref(mask),ctypes.c_size_t(8),ctypes.c_int(os.O_CLOEXEC|os.O_NONBLOCK))


def drop_capabilities(*, no_new_privileges: bool) -> None:
    PR_SET_DUMPABLE=4; PR_SET_NO_NEW_PRIVS=38; PR_CAPBSET_DROP=24; PR_SET_SECUREBITS=28; PR_CAP_AMBIENT=47; PR_CAP_AMBIENT_CLEAR_ALL=4
    for capability in range(64):
        result=LIBC.prctl(PR_CAPBSET_DROP,capability,0,0,0)
        if result!=0 and ctypes.get_errno()!=errno.EINVAL: fail("drop bounding")
    if LIBC.prctl(PR_CAP_AMBIENT,PR_CAP_AMBIENT_CLEAR_ALL,0,0,0)!=0: fail("drop ambient")
    if LIBC.prctl(PR_SET_SECUREBITS,1|2|4|8|32,0,0,0)!=0: fail("drop securebits")
    header=CapHeader(0x20080522,0); data=(CapData*2)()
    if LIBC.capset(ctypes.byref(header),ctypes.byref(data))!=0: fail("drop capset")
    if no_new_privileges and LIBC.prctl(PR_SET_NO_NEW_PRIVS,1,0,0,0)!=0: fail("drop nnp")
    if LIBC.prctl(PR_SET_DUMPABLE,0,0,0,0)!=0: fail("drop dumpable")


def drop_outer_u1() -> None:
    PR_SET_DUMPABLE=4; PR_CAP_AMBIENT=47; PR_CAP_AMBIENT_CLEAR_ALL=4
    os.setresgid(65534,65534,65534); os.setresuid(65534,65534,65534)
    header=CapHeader(0x20080522,0); data=(CapData*2)()
    if LIBC.capset(ctypes.byref(header),ctypes.byref(data))!=0: fail("U1 capset")
    if LIBC.prctl(PR_CAP_AMBIENT,PR_CAP_AMBIENT_CLEAR_ALL,0,0,0)!=0: fail("U1 ambient")
    if LIBC.prctl(PR_SET_DUMPABLE,0,0,0,0)!=0: fail("U1 dumpable")
    require_ids(65534,"U1 IDs")
    if os.getgroups(): fail("U1 groups")


def u2_setup() -> None:
    syscall(SYS_UNSHARE,ctypes.c_int(CLONE_NEWUSER))
    self_fd=os.open("/proc/self",OPEN_PATH_DIR)
    try:
        if read_control_at(self_fd,"setgroups")!=b"deny\n": fail("U2 setgroups inherited denial")
        write_control_at(self_fd,"uid_map",b"0 65534 1\n")
        write_control_at(self_fd,"gid_map",b"0 65534 1\n")
        if read_control_at(self_fd,"uid_map")!=b"0 65534 1\n" or read_control_at(self_fd,"gid_map")!=b"0 65534 1\n": fail("U2 maps")
    finally: close_proved(self_fd)
    require_ids(0,"U2 identity")
    if os.getgroups() or LIBC.prctl(3,0,0,0,0)!=0: fail("U2 security")


def source_capability_receipt(fd: int) -> tuple[int,int,int,int,int]:
    observed=os.fstat(fd)
    if not stat.S_ISDIR(observed.st_mode): fail("source capability type")
    return (stat.S_IFMT(observed.st_mode),stat.S_IMODE(observed.st_mode),observed.st_uid,observed.st_dev,observed.st_ino)


def source_boundary_preflight(repository_fd: int, package_fd: int) -> None:
    if SOURCE_CAP_IDENTITIES!={10:source_capability_receipt(repository_fd),11:source_capability_receipt(package_fd)}: fail("source capability receipt drift")
    required=((repository_fd,AUTHORITY_PATHS),(package_fd,IMPLEMENTATION_PATHS+LIFECYCLE_PATHS))
    for root_fd,paths in required:
        if not faccess_fd(root_fd,os.R_OK|os.X_OK) or faccess_fd(root_fd,os.W_OK): fail("source root access boundary")
        directories: set[str]=set()
        for relative in paths:
            pieces=relative.split("/")
            if not pieces or any(re.fullmatch(r"[A-Za-z0-9_.-]+",piece) is None or piece in (".","..") for piece in pieces): fail("source path registry")
            directories.update("/".join(pieces[:index]) for index in range(1,len(pieces)))
        for relative in sorted(directories,key=lambda value:(value.count("/"),value)):
            directory=openat2(root_fd,relative,OPEN_PATH_DIR)
            try:
                observed=os.fstat(directory)
                if not stat.S_ISDIR(observed.st_mode) or not faccessat2(root_fd,relative,os.X_OK) or faccessat2(root_fd,relative,os.W_OK): fail("source directory access boundary")
            finally: close_proved(directory)
        for relative in paths:
            if not faccessat2(root_fd,relative,os.R_OK) or faccessat2(root_fd,relative,os.W_OK): fail("source file access boundary")
            try: writable=os.open(relative,os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=root_fd)
            except OSError as error:
                if error.errno not in (errno.EACCES,errno.EPERM,errno.EROFS): raise
            else:
                close_proved(writable); fail("source file unexpectedly writable")
            file_fd=openat2(root_fd,relative,OPEN_REGULAR)
            try:
                observed=os.fstat(file_fd)
                if observed.st_mode&(stat.S_ISUID|stat.S_ISGID): fail("source set-id")
                try: capability=os.getxattr(file_fd,"security.capability")
                except OSError as error:
                    if error.errno not in (errno.ENODATA,errno.ENOTSUP,getattr(errno,"EOPNOTSUPP",errno.ENOTSUP)): raise
                else:
                    if capability: fail("source file capability")
                data=read_all(file_fd)
                if len(data)!=observed.st_size or len(data)>16*1024*1024: fail("source read boundary")
            finally: close_proved(file_fd)


def guardian_identity_preflight() -> None:
    if os.getpid()!=1: fail("guardian PID1")
    require_ids(0,"guardian nested identity")
    if os.getgroups(): fail("guardian groups")
    self_fd=os.open("/proc/self",OPEN_PATH_DIR)
    try:
        status=parse_proc_status(read_regular_at(self_fd,"status",1024*1024))
    finally: os.close(self_fd)
    nspid=tuple(int(value) for value in status.get("NSpid","").split())
    if len(nspid)<2 or nspid[-1]!=1 or any(status.get(name)!="0000000000000000" for name in ("CapInh","CapPrm","CapEff","CapBnd","CapAmb")) or status.get("NoNewPrivs")!="1" or LIBC.prctl(3,0,0,0,0)!=0: fail("guardian final credentials")


def initial_namespace_denial_probe(proc_root: int, guardian_pid: int, endpoint_fd: int) -> tuple[bytes,bytes,bytes]:
    guardian_process=openat2(proc_root,str(guardian_pid),OPEN_PATH_DIR); guardian_ns=openat2(guardian_process,"ns",OPEN_PATH_DIR)
    try:
        namespace_names=tuple(sorted((os.fsencode(name) for name in os.listdir(guardian_ns))))
        if not namespace_names or any(re.fullmatch(rb"[A-Za-z0-9_.-]+",name) is None for name in namespace_names): fail("denial namespace snapshot")
    finally: close_proved(guardian_ns); close_proved(guardian_process)
    read_end,write_end=os.pipe2(os.O_CLOEXEC); pidfd=-1; pid=0; reaped=False
    def child() -> int:
        try: os.close(endpoint_fd)
        except OSError: return 125
        immediate_ebadf(endpoint_fd)
        close_proved(read_end)
        close_except(frozenset((proc_root,write_end)))
        PR_CAPBSET_DROP=24; PR_CAP_AMBIENT=47; PR_CAP_AMBIENT_CLEAR_ALL=4
        for capability in range(64):
            result=LIBC.prctl(PR_CAPBSET_DROP,capability,0,0,0)
            if result!=0 and ctypes.get_errno()!=errno.EINVAL: return 125
        if LIBC.prctl(PR_CAP_AMBIENT,PR_CAP_AMBIENT_CLEAR_ALL,0,0,0)!=0: return 125
        os.setgroups([]); os.setresgid(65534,65534,65534); os.setresuid(65534,65534,65534)
        header=CapHeader(0x20080522,0); data=(CapData*2)()
        if LIBC.capset(ctypes.byref(header),ctypes.byref(data))!=0 or LIBC.prctl(38,1,0,0,0)!=0 or LIBC.prctl(4,0,0,0,0)!=0: return 125
        require_ids(65534,"initial denial probe IDs")
        probe_process=openat2(proc_root,str(os.getpid()),OPEN_PATH_DIR)
        try: probe_starttime=proc_start_time(probe_process,os.getpid())
        finally: close_proved(probe_process)
        probe_identity=f"probe_outer_pid={os.getpid()} probe_starttime={probe_starttime} uid_r=65534 uid_e=65534 uid_s=65534 uid_fs=65534 gid_r=65534 gid_e=65534 gid_s=65534 gid_fs=65534 groups=EMPTY cap_inh=0 cap_prm=0 cap_eff=0 cap_bnd=0 cap_amb=0".encode("ascii")
        attempts=[]; surfaces=((1,b"fd"),(2,b"root"))+tuple((3,b"ns/"+name) for name in namespace_names)
        for surface_kind,relative_name in surfaces:
            relative=f"{guardian_pid}/"+relative_name.decode("ascii"); flags=OPEN_DIR if relative_name in (b"fd",b"root") else os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW
            try: forbidden=os.open(relative,flags,dir_fd=proc_root)
            except OSError as error:
                if error.errno not in (errno.EACCES,errno.EPERM): return 125
                attempts.append(u16be(surface_kind)+u64be(len(relative_name))+relative_name+u32be(error.errno))
            else:
                close_proved(forbidden); return 125
        denial_ledger=u32be(len(attempts))+b"".join(attempts)
        complete_write(write_end,u64be(len(probe_identity))+probe_identity+denial_ledger); close_proved(write_end)
        signal.pause(); return 125
    try:
        pid,pidfd=clone3_pidfd_only(child); close_proved(write_end); write_end=-1
        evidence=read_all(read_end)
        if len(evidence)<8: fail("initial namespace denial evidence")
        identity_size=int.from_bytes(evidence[:8],"big"); probe_identity=evidence[8:8+identity_size]; denial_ledger=evidence[8+identity_size:]
        if not probe_identity or len(denial_ledger)<4 or int.from_bytes(denial_ledger[:4],"big")!=2+len(namespace_names): fail("initial namespace denial ledger")
        close_proved(read_end); read_end=-1
        syscall(SYS_PIDFD_SEND_SIGNAL,ctypes.c_int(pidfd),ctypes.c_int(signal.SIGKILL),ctypes.c_void_p(),ctypes.c_uint(0))
        if exact_wait_pidfd(pidfd,pid)!=128+signal.SIGKILL: fail("initial denial probe reap")
        reaped=True
        try: os.waitid(os.P_PIDFD,pidfd,os.WEXITED|os.WNOHANG)
        except ChildProcessError: pass
        else: fail("initial denial probe ECHILD")
        try: os.stat(str(pid),dir_fd=proc_root,follow_symlinks=False)
        except FileNotFoundError: pass
        else: fail("initial denial probe proc residue")
        identity_text=probe_identity.decode("ascii"); starttime_text=identity_text.split(" probe_starttime=",1)[1].split(" ",1)[0]
        if re.fullmatch(r"[1-9][0-9]*",starttime_text) is None: fail("probe starttime receipt")
        probe_reap=f"probe_outer_pid={pid} probe_starttime={starttime_text} pidfd_kill_signal=9 pidfd_kill_result=0 waitid_si_pid={pid} waitid_si_code=2 waitid_si_status=9 reaped=1 process_gone=1".encode("ascii")
        return probe_identity,denial_ledger,probe_reap
    finally:
        if pid>0 and not reaped:
            try: syscall(SYS_PIDFD_SEND_SIGNAL,ctypes.c_int(pidfd),ctypes.c_int(signal.SIGKILL),ctypes.c_void_p(),ctypes.c_uint(0))
            except BaseException: pass
            try: exact_wait_pidfd(pidfd,pid)
            except BaseException: pass
        for fd in (write_end,read_end,pidfd):
            if fd>=0 and fd_is_open(fd): close_proved(fd)


def attest_guardian_privilege_drop(proc_root: int, guardian_pid: int, tree: CgroupTree, endpoint_fd: int) -> tuple[bytes,bytes,bytes,bytes,bytes,bytes]:
    process=openat2(proc_root,str(guardian_pid),OPEN_PATH_DIR)
    try:
        status_raw=read_regular_at(process,"status",1024*1024); cgroup_raw=read_regular_at(process,"cgroup",1024*1024); status=parse_proc_status(status_raw)
    finally: close_proved(process)
    uid=tuple(int(value) for value in status.get("Uid","").split()); gid=tuple(int(value) for value in status.get("Gid","").split()); nspid=tuple(int(value) for value in status.get("NSpid","").split())
    expected_cgroup=("0::"+tree.relative("guardian")+"\n").encode("ascii")
    if uid!=(65534,)*4 or gid!=(65534,)*4 or status.get("Groups","") or status.get("PPid")!=str(os.getpid()) or len(nspid)<2 or nspid[-1]!=1 or status.get("Threads")!="1" or status.get("NoNewPrivs")!="1" or cgroup_raw!=expected_cgroup: fail("guardian privilege status")
    if any(status.get(name)!="0000000000000000" for name in ("CapInh","CapPrm","CapEff","CapBnd","CapAmb")): fail("guardian privilege capabilities")
    tree.require_member(tree.guardian_fd,guardian_pid)
    probe_identity,denial_ledger,probe_reap=initial_namespace_denial_probe(proc_root,guardian_pid,endpoint_fd)
    pass_vector=b"denial_vector_pass=1 probe_kill_reap_pass=1 g_status_pass=1 g_cgroup_pass=1"
    return probe_identity,denial_ledger,probe_reap,status_raw,cgroup_raw,pass_vector


def guardian_v14_exchange(channel: GuardianChannel, endpoint: socket.socket, acceptance: ExternalProfileAcceptance, session: int, guardian: tuple[int,int,int,int,int], launcher_outer_pid: int, hg: LocalEndpointFreeze) -> V14SealFence:
    validate_external_profile_acceptance(acceptance)
    ledger=BoundaryLedger(session); channel.boundary_ledger=ledger; channel.boundary_hashes["hg"]=hg.digest; launcher_record=channel.receive(lambda value:value==f"LAUNCHER_REAPED outer_pid={launcher_outer_pid}")
    launcher_frame=exact_frame(launcher_record.encode("ascii")); ledger.retain_launcher(launcher_frame)
    release_record=channel.receive(lambda value:value.partition(" ")[0]=="PRIVILEGE_DROP_RELEASE")
    release_frame=exact_frame(release_record.encode("ascii")); release_values=parse_exact(release_record,"PRIVILEGE_DROP_RELEASE",(("session",str(session)),("g_outer_pid",str(guardian[0])),("g_inner_pid",r"1"),("g_starttime",str(guardian[2])),("guardian_dev",str(guardian[3])),("guardian_ino",str(guardian[4])),("ep_p_local_receipt_sha256",r"[0-9a-f]{64}"),("holder_matrix_receipt_sha256",r"[0-9a-f]{64}"),("hook_custody_profile_sha256",re.escape(HOOK_CUSTODY_PROFILE_SHA256)),("attestation_sha256",r"[0-9a-f]{64}")))
    ledger.expect_carrier("PRIVILEGE_DROP_RELEASE",release_frame)
    ledger.commit_carrier(received_boundary_receipt(endpoint,"P","PRIVILEGE_DROP_RELEASE",release_frame))
    hp=release_values["ep_p_local_receipt_sha256"]; hm=release_values["holder_matrix_receipt_sha256"]; hc=release_values["hook_custody_profile_sha256"]; hg_digest=hg.digest
    mechanical=build_mechanical_endpoint_receipt(session,hp,hg_digest,hm); mechanical_digest=sha256(mechanical); contract=sha256(actual_endpoint_contract(session,mechanical_digest,hc))
    channel.boundary_hashes.update({"hp":hp,"hm":hm,"mech":mechanical_digest,"contract":contract})
    ready_frame=build_ready_frame(session,guardian[0],hp,hm,hc,hg_digest,mechanical_digest,contract)
    ledger.expect_carrier("GUARDIAN_READY",ready_frame)
    ready_receipt=channel.send(ready_frame[4:].decode("ascii"));
    if ready_receipt.framed_bytes!=ready_frame: fail("READY framed bytes")
    ledger.commit_carrier(ready_receipt)
    ack_record=channel.receive(lambda value:value.partition(" ")[0]=="GUARDIAN_READY_ACK"); ack_frame=exact_frame(ack_record.encode("ascii")); expected_ack=build_ack_frame(session,guardian,contract,launcher_frame,release_frame,ready_frame)
    ledger.expect_carrier("GUARDIAN_READY_ACK",expected_ack)
    if ack_frame!=expected_ack: boundary_fail("WRONG_ATTESTATION","ACK chain")
    ledger.commit_carrier(received_boundary_receipt(endpoint,"P","GUARDIAN_READY_ACK",ack_frame))
    seal_frame=build_seal_frame(session,guardian,contract,launcher_frame,release_frame,ready_frame,ack_frame); ledger.expect_carrier("BOOTSTRAP_SEALED",seal_frame); seal_receipt=channel.send(seal_frame[4:].decode("ascii"))
    if seal_receipt.framed_bytes!=seal_frame: boundary_fail("MALFORMED","Seal framed bytes")
    ledger.commit_carrier(seal_receipt)
    if ledger.c14()!=((1,1,1,1,0,0),"BOOTSTRAP_SEALED_COMMIT"): boundary_fail("WRONG_STATE","C14 live row")
    ledger.stopped=True
    fence=V14SealFence(session,contract,seal_receipt,acceptance.execution_gate_sha256); fence.validate(); return fence


def p_v14_exchange(controller: PController, endpoint: socket.socket, acceptance: ExternalProfileAcceptance, session: int, launcher_pid: int, guardian: tuple[int,int,int,int,int], p_starttime: int) -> None:
    validate_external_profile_acceptance(acceptance)
    ledger=BoundaryLedger(session); controller.boundary_ledger=ledger
    denial_items=attest_guardian_privilege_drop(controller.proc_root,controller.guardian_pid,controller.tree,endpoint.fileno())
    hp=freeze_actual_endpoint(endpoint,session,"EP_P",os.getpid(),p_starttime,controller.diag)
    controller.boundary_hashes["hp"]=hp.digest
    probe_reap=denial_items[2].decode("ascii"); probe_match=re.fullmatch(r"probe_outer_pid=([1-9][0-9]*) probe_starttime=[1-9][0-9]* pidfd_kill_signal=9 pidfd_kill_result=0 waitid_si_pid=[1-9][0-9]* waitid_si_code=2 waitid_si_status=9 reaped=1 process_gone=1",probe_reap)
    if probe_match is None or any(index not in controller.children or not controller.children[index].reaped for index in (1,2)): fail("holder predecessor closure")
    closed_design_pids=(launcher_pid,int(probe_match.group(1)),controller.children[1].outer_pid,controller.children[2].outer_pid)
    hm_raw=collect_holder_matrix(controller.proc_root,session,os.getpid(),p_starttime,controller.guardian_pid,guardian[2],closed_design_pids,hp,controller.diag); hc_raw=hook_custody_profile_preimage(); controller.boundary_hashes["hm"]=sha256(hm_raw)
    launcher_frame=exact_frame(f"LAUNCHER_REAPED outer_pid={launcher_pid}".encode("ascii")); ledger.retain_launcher(launcher_frame); launcher_receipt=controller.control.send(launcher_frame[4:].decode("ascii"))
    if launcher_receipt.framed_bytes!=launcher_frame: fail("Launcher framed bytes")
    release_frame=build_release_frame(session,guardian,hp.raw_receipt,hm_raw,hc_raw,denial_items); ledger.expect_carrier("PRIVILEGE_DROP_RELEASE",release_frame); release_receipt=controller.control.send(release_frame[4:].decode("ascii"))
    if release_receipt.framed_bytes!=release_frame: fail("Release framed bytes")
    ledger.commit_carrier(release_receipt)
    ready_record=controller._bootstrap_record()
    if ready_record.partition(" ")[0]!="GUARDIAN_READY": boundary_fail("REORDERED","READY order")
    ready_frame=exact_frame(ready_record.encode("ascii")); ready_values=parse_exact(ready_record,"GUARDIAN_READY",(("session",str(session)),("outer_pid",str(guardian[0])),("inner_pid",r"1"),("ep_p_local_receipt_sha256",re.escape(hp.digest)),("holder_matrix_receipt_sha256",re.escape(sha256(hm_raw))),("hook_custody_profile_sha256",re.escape(HOOK_CUSTODY_PROFILE_SHA256)),("ep_g_local_receipt_sha256",r"[0-9a-f]{64}"),("mechanical_endpoint_receipt_sha256",r"[0-9a-f]{64}"),("actual_endpoint_contract_sha256",r"[0-9a-f]{64}")))
    expected_mechanical=sha256(build_mechanical_endpoint_receipt(session,hp.digest,ready_values["ep_g_local_receipt_sha256"],sha256(hm_raw)))
    expected_contract=sha256(actual_endpoint_contract(session,expected_mechanical,HOOK_CUSTODY_PROFILE_SHA256))
    controller.boundary_hashes.update({"hg":ready_values["ep_g_local_receipt_sha256"],"mech":expected_mechanical,"contract":expected_contract})
    if (ready_values["mechanical_endpoint_receipt_sha256"],ready_values["actual_endpoint_contract_sha256"])!=(expected_mechanical,expected_contract): boundary_fail("WRONG_ATTESTATION","READY endpoint contract")
    expected_ready=build_ready_frame(session,guardian[0],hp.digest,sha256(hm_raw),HOOK_CUSTODY_PROFILE_SHA256,ready_values["ep_g_local_receipt_sha256"],expected_mechanical,expected_contract)
    ledger.expect_carrier("GUARDIAN_READY",expected_ready)
    if ready_frame!=expected_ready: boundary_fail("WRONG_ATTESTATION","READY commitment frame")
    ledger.commit_carrier(received_boundary_receipt(endpoint,"G","GUARDIAN_READY",ready_frame))
    ack_frame=build_ack_frame(session,guardian,expected_contract,launcher_frame,release_frame,ready_frame); ledger.expect_carrier("GUARDIAN_READY_ACK",ack_frame); ack_receipt=controller.control.send(ack_frame[4:].decode("ascii"))
    if ack_receipt.framed_bytes!=ack_frame: boundary_fail("MALFORMED","ACK framed bytes")
    ledger.commit_carrier(ack_receipt)
    seal_record=controller._bootstrap_record()
    if seal_record.partition(" ")[0]!="BOOTSTRAP_SEALED": boundary_fail("REORDERED","Seal order")
    seal_frame=exact_frame(seal_record.encode("ascii")); expected_seal=build_seal_frame(session,guardian,expected_contract,launcher_frame,release_frame,ready_frame,ack_frame); ledger.expect_carrier("BOOTSTRAP_SEALED",expected_seal)
    if seal_frame!=expected_seal: boundary_fail("WRONG_ATTESTATION","Seal chain")
    ledger.commit_carrier(received_boundary_receipt(endpoint,"G","BOOTSTRAP_SEALED",seal_frame))
    if ledger.c14()!=((1,1,1,1,0,0),"BOOTSTRAP_SEALED_COMMIT"): boundary_fail("WRONG_STATE","P C14 live row")
    ledger.stopped=True; controller.seal_validated=True


def guardian_start_identity() -> tuple[int,int,int]:
    process=os.open("/proc/self",OPEN_PATH_DIR)
    try:
        status=parse_proc_status(read_regular_at(process,"status",1024*1024)); outer_pid=int(status.get("NSpid",str(os.getpid())).split()[0]); starttime=proc_start_time(process,outer_pid); observed=os.fstat(process)
        return starttime,observed.st_dev,observed.st_ino
    finally: close_proved(process)


def guardian_bootstrap(address: bytes, launcher_done_fd: int, workers_identity: tuple[int,int], acceptance: ExternalProfileAcceptance, session: int) -> int:
    validate_external_profile_acceptance(acceptance)
    inherited_self=os.open("/proc/self",OPEN_PATH_DIR)
    try:
        inherited_status=parse_proc_status(read_regular_at(inherited_self,"status",1024*1024)); outer_from_status=int(inherited_status.get("NSpid",str(os.getpid())).split()[0]); guardian_starttime=proc_start_time(inherited_self,outer_from_status); guardian_proc_st=os.fstat(inherited_self)
    finally: os.close(inherited_self)
    nspid=tuple(int(value) for value in inherited_status.get("NSpid","").split())
    if len(nspid)<2 or nspid[-1]!=1: fail("guardian PID1")
    outer_pid=nspid[0]; launcher_outer_pid=int(inherited_status.get("PPid","0"))
    if launcher_outer_pid<=0: fail("launcher outer PID")
    os.setsid()
    if os.getsid(0)!=os.getpid() or os.getpgrp()!=os.getpid() or LIBC.prctl(36,1,0,0,0)!=0: fail("guardian session/subreaper")
    tmp_fd=private_mount_setup()
    connection=socket.socket(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC); connection.connect(address)
    close_except(frozenset((connection.fileno(),tmp_fd,launcher_done_fd,10,11)))
    control=FramedControl(connection,"G"); channel=GuardianChannel(control)
    channel.send(f"PID1_READY outer_pid={outer_pid} inner_pid=1")
    workers_fd=control.receive_fd("WORKERS_CGROUP_FD session=0")
    workers_st=os.fstat(workers_fd); workers_flags=fcntl.fcntl(workers_fd,fcntl.F_GETFL)
    if not stat.S_ISDIR(workers_st.st_mode) or (workers_st.st_dev,workers_st.st_ino)!=workers_identity or workers_flags&getattr(os,"O_PATH",0)!=getattr(os,"O_PATH",0) or fcntl.fcntl(workers_fd,fcntl.F_GETFD)!=FD_CLOEXEC: fail("workers capability receipt")
    channel.allocated(); channel.send("WORKERS_CGROUP_FD_ACK session=0")
    authentication=GuardianAuthentication(channel); objects=GuardianObjectLedger(channel); workers=GuardianWorkers(channel,workers_fd,10,11,connection.fileno())
    lock_name=b"\x00/tmp/p15r."+sha256(repr(os.fstat(11)[:3]).encode("ascii"))[:40].encode("ascii")+b".lock"
    rpc=GuardianRPC(channel,authentication,workers,objects,tmp_fd,10,11,lock_name)
    transaction=GuardianTransaction(channel,workers,objects,rpc,authentication,tmp_fd,11)
    try:
        hg: LocalEndpointFreeze|None=None
        def finish_epoch2_boundary() -> None:
            nonlocal hg
            openat2_rename_preflight(tmp_fd)
            hide_cgroup_mounts(); drop_capabilities(no_new_privileges=True)
            source_boundary_preflight(10,11); guardian_identity_preflight()
            hg=freeze_actual_endpoint(connection,session,"EP_G",outer_pid,guardian_starttime,None)
        transaction.preflight_children(finish_epoch2_boundary)
        complete_write(launcher_done_fd,b"CGROUP_PREFLIGHTED"); close_proved(launcher_done_fd); launcher_done_fd=-1
        if hg is None: fail("HG7 missing")
        guardian=(outer_pid,1,guardian_starttime,guardian_proc_st.st_dev,guardian_proc_st.st_ino)
        try: fence=guardian_v14_exchange(channel,connection,acceptance,session,guardian,launcher_outer_pid,hg)
        except BaseException as caught:
            if channel.boundary_ledger is not None and sum(channel.boundary_ledger.bits)<4:
                channel.boundary_failure,channel.boundary_terminal_context=retain_v14_failure(channel.boundary_ledger,connection,"G",caught,control,guardian,hg is not None,channel.boundary_hashes["hg"]!="NONE")
            raise
        workers.authorize_post_seal_clones(fence,connection.fileno())
        try: transaction.run_after_preflight(fence)
        except AuthenticatedSignal as caught:
            if caught.signo!=channel.pending_signal: fail("signal exception join")
            transaction.global_final()
    except BaseException:
        for state in authentication.states.values(): state.complete_failure_containment()
        raise
    finally:
        if launcher_done_fd>=0 and fd_is_open(launcher_done_fd): close_proved(launcher_done_fd)
    if fd_is_open(tmp_fd): close_proved(tmp_fd)
    connection_fd=connection.fileno(); connection.close(); immediate_ebadf(connection_fd)
    return 0


def launcher_bootstrap(bootstrap_fd: int, address: bytes, expected_guardian_relative: str, workers_identity: tuple[int,int], acceptance: ExternalProfileAcceptance, session: int) -> int:
    validate_external_profile_acceptance(acceptance)
    outer_pid=os.getpid()
    if current_cgroup_relative()!=expected_guardian_relative: fail("launcher first-instruction cgroup")
    close_except(frozenset((bootstrap_fd,10,11)))
    require_ids(0,"launcher initial IDs")
    os.setsid()
    if os.getsid(0)!=outer_pid or os.getpgrp()!=outer_pid: fail("launcher setsid")
    os.setgroups([])
    syscall(SYS_UNSHARE,ctypes.c_int(CLONE_NEWUSER))
    bootstrap=socket.socket(fileno=bootstrap_fd)
    bootstrap_send(bootstrap,f"U1_CREATED outer_pid={outer_pid}")
    bootstrap_receive(bootstrap,f"U1_MAPS_COMMITTED outer_pid={outer_pid}")
    drop_outer_u1()
    bootstrap_send(bootstrap,f"OUTER_IDS_READY outer_pid={outer_pid}")
    bootstrap_receive(bootstrap,f"OUTER_IDS_ATTESTED outer_pid={outer_pid}")
    u2_setup()
    bootstrap_send(bootstrap,f"U2_MAPS_COMMITTED outer_pid={outer_pid}")
    bootstrap_number=bootstrap.fileno(); bootstrap.close(); immediate_ebadf(bootstrap_number); bootstrap_fd=-1
    launcher_read,guardian_write=os.pipe2(os.O_CLOEXEC)
    syscall(SYS_UNSHARE,ctypes.c_int(CLONE_NEWNS|CLONE_NEWPID))
    guardian_pid=os.fork()
    if guardian_pid==0:
        close_proved(launcher_read)
        status=125
        try:
            if os.getpid()!=1: fail("guardian fork PID1")
            status=guardian_bootstrap(address,guardian_write,workers_identity,acceptance,session)
        except BaseException: status=125
        os._exit(status&0xff)
    if guardian_pid<=0: fail("guardian fork result")
    close_proved(guardian_write); guardian_write=-1
    try:
        if read_all(launcher_read)!=b"CGROUP_PREFLIGHTED": fail("launcher probe handoff")
    finally: close_proved(launcher_read)
    close_proved(10); close_proved(11)
    close_except(frozenset())
    return 0


def preopen_sources() -> tuple[int,int]:
    if fd_is_open(10) or fd_is_open(11): fail("setup source ABI occupied")
    repository=package=repository_high=package_high=-1
    installed: list[int]=[]
    try:
        repository=os.open(REPOSITORY_PATH,OPEN_DIR); package=os.open(PACKAGE_PATH,OPEN_DIR)
        repository_high=fcntl.fcntl(repository,fcntl.F_DUPFD_CLOEXEC,20); package_high=fcntl.fcntl(package,fcntl.F_DUPFD_CLOEXEC,20)
        duplicate_to(repository_high,10); installed.append(10)
        duplicate_to(package_high,11); installed.append(11)
        for fd,wanted in ((10,REPOSITORY_PATH),(11,PACKAGE_PATH)):
            observed=os.fstat(fd); expected=os.stat(wanted,follow_symlinks=False)
            if not stat.S_ISDIR(observed.st_mode) or (observed.st_dev,observed.st_ino)!=(expected.st_dev,expected.st_ino): fail("source capability identity")
            SOURCE_CAP_IDENTITIES[fd]=source_capability_receipt(fd)
        if set(SOURCE_CAP_IDENTITIES)!={10,11}: fail("source capability receipt")
        return 10,11
    except BaseException:
        SOURCE_CAP_IDENTITIES.clear()
        for fd in reversed(installed):
            if fd_is_open(fd): close_proved(fd)
        raise
    finally:
        for fd in (package_high,repository_high,package,repository):
            if fd>=0 and fd_is_open(fd): close_proved(fd)


def accept_guardian(listener: socket.socket, proc_root: int, launcher_pid: int, tree: CgroupTree) -> tuple[socket.socket,int]:
    connection,_address=listener.accept(); credentials=connection.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,struct.calcsize("3i")); pid,uid,gid=struct.unpack("3i",credentials)
    if pid<=0 or (uid,gid)!=(65534,65534): connection.close(); fail("guardian peer credentials")
    process=openat2(proc_root,str(pid),OPEN_PATH_DIR)
    try:
        status=parse_proc_status(read_regular_at(process,"status",1024*1024)); cgroup=read_regular_at(process,"cgroup",1024*1024); proc_start_time(process,pid)
    finally: close_proved(process)
    nspid=tuple(int(value) for value in status.get("NSpid","").split()); uid_columns=tuple(int(value) for value in status.get("Uid","").split()); gid_columns=tuple(int(value) for value in status.get("Gid","").split())
    if status.get("PPid")!=str(launcher_pid) or len(nspid)<2 or nspid[-1]!=1 or uid_columns!=(65534,)*4 or gid_columns!=(65534,)*4 or status.get("Threads")!="1" or cgroup!=("0::"+tree.relative("guardian")+"\n").encode("ascii"):
        connection.close(); fail("guardian proc identity")
    tree.require_members(tree.guardian_fd,(launcher_pid,pid))
    return connection,pid


def p_crash_containment(tree: CgroupTree|None, pidfds: Sequence[int]) -> CgroupTree|None:
    if tree is None: return None
    try:
        tree.kill(tree.session_fd)
        while True:
            try: os.waitpid(-1,0)
            except ChildProcessError: break
        for fd in pidfds:
            if fd>=0 and fd_is_open(fd): close_proved(fd)
        tree.require_empty(tree.workers_fd); tree.require_empty(tree.guardian_fd); tree.require_empty(tree.session_fd)
        tree.dispose()
        return None
    except BaseException:
        return tree


def p_main(external_acceptance: ExternalProfileAcceptance|None) -> int:
    secrets: list[tuple[str,bytearray]]=[]; tree: CgroupTree|None=None; listener: socket.socket|None=None; connection: socket.socket|None=None; diag: UnixDiagOracle|None=None; bootstrap_parent: socket.socket|None=None; bootstrap_child: socket.socket|None=None
    launcher_pidfd=guardian_pidfd=proc_root=signal_fd=-1; proc_root_ledger: LongLivedProcRootLedger|None=None; guardian_dmaudit_identity: DMAuditIdentityExpectation|None=None; guardian_pidfd_ledger: PIDFDLifetimeEntry|None=None; source_fds=(-1,-1); controller: PController|None=None
    try:
        validate_external_profile_acceptance(external_acceptance)
        if external_acceptance is None: fail("external acceptance absent")
        pid_dec=os.getpid(); uid_dec=os.getuid(); bootstrap_session=pid_dec
        if pid_dec<=1 or uid_dec!=0: fail("initial PID/UID")
        require_ids(0,"initial IDs")
        if len(os.listdir("/proc/self/task"))!=1: fail("initial single thread")
        os.setgroups([])
        signal_fd=make_signalfd()
        if LIBC.prctl(36,1,0,0,0)!=0: fail("subreaper")
        source_fds=preopen_sources(); native_scalar_preflight(); seqpacket_probe(); proc_root=os.open("/proc",OPEN_PATH_DIR)
        for namespace in ("user","mnt","pid","cgroup"):
            self_ns=os.stat("self/ns/"+namespace,dir_fd=proc_root,follow_symlinks=True); init_ns=os.stat("1/ns/"+namespace,dir_fd=proc_root,follow_symlinks=True)
            if (self_ns.st_dev,self_ns.st_ino)!=(init_ns.st_dev,init_ns.st_ino): fail("non-initial namespace "+namespace)
        tree=CgroupTree.create(pid_dec); cgroup_atomic_probe(tree)
        address=b"\x00p15r-possession-control-v2:"+str(pid_dec).encode("ascii")
        if len(address)>107: fail("control address size")
        listener=socket.socket(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC); listener.bind(address); listener.listen(1)
        bootstrap_parent,bootstrap_child=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC)
        bootstrap_child_fd=bootstrap_child.fileno(); guardian_relative=tree.relative("guardian").lstrip("/")
        launcher_pid,launcher_pidfd=clone3(lambda:launcher_bootstrap(bootstrap_child_fd,address,guardian_relative,tree.workers_identity,external_acceptance,bootstrap_session),cgroup_fd=tree.guardian_fd)
        bootstrap_child.close(); immediate_ebadf(bootstrap_child_fd); bootstrap_child=None
        attest_launcher_placement(proc_root,launcher_pid,launcher_pidfd,pid_dec,tree)
        bootstrap_receive(bootstrap_parent,f"U1_CREATED outer_pid={launcher_pid}")
        diag=unix_diag_preflight()
        write_proc_map(proc_root,launcher_pid,"uid_map",b"65534 65534 1\n")
        write_proc_map(proc_root,launcher_pid,"setgroups",b"deny\n")
        write_proc_map(proc_root,launcher_pid,"gid_map",b"65534 65534 1\n")
        bootstrap_send(bootstrap_parent,f"U1_MAPS_COMMITTED outer_pid={launcher_pid}")
        bootstrap_receive(bootstrap_parent,f"OUTER_IDS_READY outer_pid={launcher_pid}"); attest_outer_launcher(proc_root,launcher_pid)
        bootstrap_send(bootstrap_parent,f"OUTER_IDS_ATTESTED outer_pid={launcher_pid}")
        bootstrap_receive(bootstrap_parent,f"U2_MAPS_COMMITTED outer_pid={launcher_pid}")
        bootstrap_require_eof(bootstrap_parent)
        bootstrap_parent_fd=bootstrap_parent.fileno(); bootstrap_parent.close(); immediate_ebadf(bootstrap_parent_fd); bootstrap_parent=None
        connection,guardian_pid=accept_guardian(listener,proc_root,launcher_pid,tree); listener.close(); listener=None
        guardian_process=openat2(proc_root,str(guardian_pid),OPEN_PATH_DIR)
        try:
            guardian_starttime=proc_start_time(guardian_process,guardian_pid); guardian_proc_st=os.fstat(guardian_process)
        finally: close_proved(guardian_process)
        p_process=openat2(proc_root,str(pid_dec),OPEN_PATH_DIR)
        try: p_starttime=proc_start_time(p_process,pid_dec)
        finally: close_proved(p_process)
        guardian_identity=(guardian_pid,1,guardian_starttime,guardian_proc_st.st_dev,guardian_proc_st.st_ino)
        control=FramedControl(connection,"P")
        ready=control.receive()
        parse_exact(ready,"PID1_READY",(("outer_pid",str(guardian_pid)),("inner_pid",r"1")))
        guardian_cgroup_st=os.fstat(tree.guardian_fd); guardian_process=openat2(proc_root,str(guardian_pid),OPEN_PATH_DIR)
        try:
            guardian_status=parse_proc_status(read_regular_at(guardian_process,"status",1024*1024)); guardian_cgroup=read_regular_at(guardian_process,"cgroup",1024*1024).decode("ascii"); guardian_nspid=tuple(int(value) for value in guardian_status.get("NSpid","").split())
            guardian_expectation=DMAuditIdentityExpectation("GUARDIAN",guardian_pid,guardian_starttime,guardian_nspid,1,guardian_cgroup,guardian_cgroup_st.st_dev,guardian_cgroup_st.st_ino)
            guardian_identity_bytes=dmaudit_identity_bytes(guardian_process,guardian_expectation); guardian_dmaudit_identity=replace(guardian_expectation,identity_sha256=dmaudit_identity_digest(guardian_identity_bytes))
        finally: close_proved(guardian_process)
        guardian_pidfd=syscall(SYS_PIDFD_OPEN,ctypes.c_int(guardian_pid),ctypes.c_uint(0)); guardian_pidfd_ledger=pidfd_lifetime_entry(1,guardian_pidfd,guardian_dmaudit_identity,guardian_identity_bytes)
        try:
            if fcntl.fcntl(guardian_pidfd,fcntl.F_GETFD)!=FD_CLOEXEC: fail("guardian pidfd CLOEXEC")
            guardian_process=openat2(proc_root,str(guardian_pid),OPEN_PATH_DIR)
            try: guardian_identity_after=dmaudit_identity_bytes(guardian_process,guardian_dmaudit_identity)
            finally: close_proved(guardian_process)
            if guardian_identity_after!=guardian_identity_bytes: fail("guardian pidfd identity ABA")
            guardian_pidfd_ledger.state="VALIDATED"
        except BaseException:
            if fd_is_open(guardian_pidfd): close_proved(guardian_pidfd)
            guardian_pidfd_ledger.state="CLOSED_PROVED"; guardian_pidfd=-1; raise
        close_proved(proc_root); proc_root=-1
        proc_root,proc_root_ledger=open_long_lived_proc_root()
        if proc_root_ledger is None: fail("LONG_LIVED_PROC_ROOT absent")
        control.send_fd("WORKERS_CGROUP_FD session=0",tree.workers_fd)
        if control.receive()!="WORKERS_CGROUP_FD_ACK session=0": fail("workers capability ACK")
        if guardian_dmaudit_identity is None or guardian_pidfd_ledger is None or guardian_pidfd_ledger.state!="VALIDATED": fail("guardian pidfd ledger absent")
        controller=PController(control,tree,guardian_pid,guardian_pidfd,guardian_dmaudit_identity,guardian_pidfd_ledger,proc_root,proc_root_ledger,diag,secrets,source_fds,signal_fd)
        source_fds=(-1,-1)
        controller.run_bootstrap_probes()
        launcher_status=exact_wait_pidfd(launcher_pidfd,launcher_pid); close_proved(launcher_pidfd); launcher_pidfd=-1
        if launcher_status!=0: fail("launcher status")
        tree.require_member(tree.guardian_fd,guardian_pid)
        try: p_v14_exchange(controller,connection,external_acceptance,bootstrap_session,launcher_pid,guardian_identity,p_starttime)
        except BaseException as caught:
            if controller.boundary_ledger is not None and sum(controller.boundary_ledger.bits)<4:
                holder_ceiling=controller.boundary_hashes["hp"]!="NONE" and controller.boundary_hashes["hm"]!="NONE"
                guardian_cgroup_valid=controller.tree.members(controller.tree.guardian_fd)==(controller.guardian_pid,)
                death_probe=select.poll(); death_probe.register(guardian_pidfd,select.POLLIN|select.POLLHUP); peer_crash_observed=bool(death_probe.poll(0))
                controller.boundary_failure,controller.boundary_terminal_context=retain_v14_failure(controller.boundary_ledger,connection,"P",caught,control,guardian_identity,guardian_cgroup_valid,holder_ceiling,peer_crash_observed)
            raise
        if not controller.seal_validated or controller.boundary_ledger is None: fail("P Seal validation")
        repository_fd,package_fd=controller.source_fds; close_proved(repository_fd); controller.source_fds=(-1,package_fd); close_proved(package_fd); controller.source_fds=(-1,-1)
        controller.run()
        guardian_status=exact_wait_pidfd(guardian_pidfd,guardian_pid); close_proved(guardian_pidfd); controller.auditor.guardian_pidfd_ledger.state="CLOSED_PROVED"; guardian_pidfd=-1
        if guardian_status!=0 or not controller.seal_validated: fail("guardian terminal status")
        tree.require_empty(tree.guardian_fd); tree.dispose(); tree=None
        controller.dispose_control_after_exit()
        close_proved(proc_root); immediate_ebadf(proc_root); proc_root_ledger.state="CLOSED_PROVED"; proc_root=-1; diag.close(); diag=None; close_proved(signal_fd); signal_fd=-1
        erase_secrets(secrets)
        if controller.pending_signal:
            if not controller.signal_cleaned: fail("signal exit without cleanup receipt")
            signo=controller.pending_signal
            signal.signal(signo,signal.SIG_DFL)
            signal.pthread_sigmask(signal.SIG_UNBLOCK,(signo,))
            os.kill(os.getpid(),signo)
            fail("handled signal re-raise returned")
        return 0
    except PossessionFailure as failure:
        guardian_pidfd_was_open=guardian_pidfd>=0
        for pidfd in (guardian_pidfd,launcher_pidfd):
            if pidfd>=0:
                try: syscall(SYS_PIDFD_SEND_SIGNAL,ctypes.c_int(pidfd),ctypes.c_int(signal.SIGKILL),ctypes.c_void_p(),ctypes.c_uint(0))
                except BaseException: pass
        tree=p_crash_containment(tree,(guardian_pidfd,launcher_pidfd)); peer_reaped=tree is None
        if peer_reaped: guardian_pidfd=launcher_pidfd=-1
        if guardian_pidfd_ledger is not None and guardian_pidfd_was_open and peer_reaped: guardian_pidfd_ledger.state="CLOSED_PROVED"
        if controller is not None and guardian_pidfd_was_open and peer_reaped: controller.auditor.guardian_pidfd_ledger.state="CLOSED_PROVED"
        if controller is not None and peer_reaped: child_pidfds_closed=controller.close_child_pidfd_ledgers()
        elif controller is not None: controller.mark_child_pidfd_ledgers_ambiguous(); child_pidfds_closed=False
        else: child_pidfds_closed=True
        if controller is not None and connection is not None: controller.complete_terminal_or_unreconciled(connection,peer_reaped,child_pidfds_closed)
        if controller is not None: controller.complete_failure_containment(peer_reaped)
        erase_secrets(secrets)
        print(failure.token,file=sys.stderr)
        return 1
    except (OSError,ValueError,UnicodeError,MemoryError):
        guardian_pidfd_was_open=guardian_pidfd>=0
        for pidfd in (guardian_pidfd,launcher_pidfd):
            if pidfd>=0:
                try: syscall(SYS_PIDFD_SEND_SIGNAL,ctypes.c_int(pidfd),ctypes.c_int(signal.SIGKILL),ctypes.c_void_p(),ctypes.c_uint(0))
                except BaseException: pass
        tree=p_crash_containment(tree,(guardian_pidfd,launcher_pidfd)); peer_reaped=tree is None
        if peer_reaped: guardian_pidfd=launcher_pidfd=-1
        if guardian_pidfd_ledger is not None and guardian_pidfd_was_open and peer_reaped: guardian_pidfd_ledger.state="CLOSED_PROVED"
        if controller is not None and guardian_pidfd_was_open and peer_reaped: controller.auditor.guardian_pidfd_ledger.state="CLOSED_PROVED"
        if controller is not None and peer_reaped: child_pidfds_closed=controller.close_child_pidfd_ledgers()
        elif controller is not None: controller.mark_child_pidfd_ledgers_ambiguous(); child_pidfds_closed=False
        else: child_pidfds_closed=True
        if controller is not None and connection is not None: controller.complete_terminal_or_unreconciled(connection,peer_reaped,child_pidfds_closed)
        if controller is not None: controller.complete_failure_containment(peer_reaped)
        erase_secrets(secrets); print(E_POSSESSION,file=sys.stderr); return 1
    finally:
        if listener is not None: listener.close()
        if connection is not None and connection.fileno()>=0:
            connection_fd=connection.fileno()
            try: connection.close(); immediate_ebadf(connection_fd)
            except (OSError,PossessionFailure): os._exit(125)
        if bootstrap_parent is not None: bootstrap_parent.close()
        if bootstrap_child is not None: bootstrap_child.close()
        if diag is not None: diag.close()
        remaining_sources=controller.source_fds if controller is not None else source_fds
        for fd in remaining_sources:
            if fd>=0:
                try: close_proved(fd)
                except (OSError,PossessionFailure): pass
        if controller is not None: controller.source_fds=(-1,-1)
        remaining_sources=(-1,-1); source_fds=(-1,-1)
        for fd_kind,fd in (("LAUNCHER_PIDFD",launcher_pidfd),("GUARDIAN_PIDFD",guardian_pidfd),("LONG_LIVED_PROC_ROOT",proc_root),("SIGNALFD",signal_fd)):
            if fd>=0:
                try: close_proved(fd)
                except (OSError,PossessionFailure):
                    if fd_kind=="LONG_LIVED_PROC_ROOT" and proc_root_ledger is not None: proc_root_ledger.state="AMBIGUOUS_CRASH_ONLY"
                    if fd_kind=="GUARDIAN_PIDFD" and guardian_pidfd_ledger is not None: guardian_pidfd_ledger.state="AMBIGUOUS_CRASH_ONLY"
                    os._exit(125)
                else:
                    if fd_kind=="LONG_LIVED_PROC_ROOT" and proc_root_ledger is not None: proc_root_ledger.state="CLOSED_PROVED"
                    if fd_kind=="GUARDIAN_PIDFD" and guardian_pidfd_ledger is not None: guardian_pidfd_ledger.state="CLOSED_PROVED"


def successor_execution_gate_entry(acceptance: ExternalProfileAcceptance) -> int:
    """Static callgraph root reserved to a separately authorized future gate."""
    validate_external_profile_acceptance(acceptance)
    return p_main(acceptance)


role=os.environ.get("P15R_WORKER_ROLE","")
if role=="COPIED_REPRODUCE":
    raise SystemExit(copied_reproduce_worker())
raise SystemExit(p_main(None))
P15R_POSSESSION_PY_V2_END
