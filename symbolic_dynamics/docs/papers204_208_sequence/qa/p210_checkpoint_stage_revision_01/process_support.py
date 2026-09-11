#!/usr/bin/env python3
"""Proposed bounded native-process ownership support; not run by preparation."""
from pathlib import Path
import json
import os
import selectors
import signal
import subprocess
import time


def existing_overlay_writers(dest):
    """Fresh read-only ownership check; never enumerate inherited environment."""
    found=[]
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            comm=(proc/'comm').read_text().strip()
            if comm not in ('git','git-remote-https','git-remote-http','ssh','index-pack','pack-objects'):
                continue
            args=(proc/'cmdline').read_bytes().split(b'\0')
            match=os.readlink(proc/'cwd')==str(dest) or str(dest).encode() in args
            for fd in (proc/'fd').iterdir():
                try:
                    match=match or os.readlink(fd).startswith(str(dest)+'/.git/')
                except (OSError,ProcessLookupError,PermissionError):
                    pass
            if match:
                found.append({'pid':int(proc.name),'comm':comm})
        except (OSError,ProcessLookupError,PermissionError):
            continue
    return found


def group_members(pgid):
    members=[]
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            raw=(proc/'stat').read_text()
            fields=raw[raw.rfind(')')+2:].split()
            if int(fields[2])==pgid:
                members.append({'pid':int(proc.name),'state':fields[0],'ppid':int(fields[1]),
                                'pgid':int(fields[2]),'sid':int(fields[3]),'start_ticks':int(fields[19])})
        except (OSError,ProcessLookupError,PermissionError):
            continue
    return members


def settle_group(p, terminate=False):
    """Signals are limited to the new session/group created by this launcher.

    No output digest may be finalized unless quiescent is true. Zombies have
    no file-writing capability; their identities are retained separately.
    """
    events=[]
    def live():
        members=group_members(p.pid)
        assert all(m['sid']==p.pid for m in members),'unexpected process-group/session identity'
        return [m for m in members if m['state']!='Z']
    def send(sig):
        if live():
            try:
                os.killpg(p.pid,sig)
                events.append({'signal':signal.Signals(sig).name,'epoch':time.time()})
            except ProcessLookupError:
                pass
    if terminate:
        send(signal.SIGTERM)
    end=time.monotonic()+5
    while live() and time.monotonic()<end:
        p.poll()
        time.sleep(0.1)
    if live():
        send(signal.SIGTERM)
        end=time.monotonic()+3
        while live() and time.monotonic()<end:
            p.poll()
            time.sleep(0.1)
    if live():
        send(signal.SIGKILL)
        end=time.monotonic()+5
        while live() and time.monotonic()<end:
            p.poll()
            time.sleep(0.1)
    p.poll()
    remaining=group_members(p.pid)
    return {'owned_pgid':p.pid,'owned_sid':p.pid,'signals':events,
            'remaining_members':remaining,'quiescent':not any(m['state']!='Z' for m in remaining),
            'native_returncode':p.returncode}


def run_files(argv, stdin_path, stdout_path, stderr_path, env, timeout=300):
    """No inherited input pipe; heartbeat at most 30s while caller can yield."""
    start=time.time()
    code=None
    with stdin_path.open('rb') as inp, stdout_path.open('xb') as out, stderr_path.open('xb') as err:
        p=subprocess.Popen(argv,stdin=inp,stdout=out,stderr=err,env=env,start_new_session=True)
        end=time.monotonic()+timeout
        try:
            while p.poll() is None:
                remaining=end-time.monotonic()
                if remaining<=0:
                    code='TIMEOUT'
                    break
                try:
                    p.wait(timeout=min(30,remaining))
                except subprocess.TimeoutExpired:
                    print(json.dumps({'native_pid':p.pid,'running_seconds':round(time.time()-start,1),
                                      'deadline_seconds':timeout,'status':'RUNNING_OWNED_NATIVE_PROCESS'}),flush=True)
            if code is None:
                code=p.returncode
        except BaseException:
            code='INTERRUPTED'
            raise
        finally:
            settlement=settle_group(p,terminate=code in ('TIMEOUT','INTERRUPTED') or code is None)
        assert settlement['quiescent'],'owned process group not quiescent; raw streams are unfinished and must not be hashed'
    if settlement['signals'] and code==0:
        code='UNEXPECTED_DESCENDANT_TERMINATION'
    return {'exit':code,'pid':p.pid,'started_epoch':start,'ended_epoch':time.time(),
            'timeout_seconds':timeout,'process_group_settlement':settlement}


class TimedReader:
    """Bounded, nonblocking native stdout reader for the exact blob protocol."""
    def __init__(self, stream, pid, timeout=300):
        self.fd=stream.fileno()
        os.set_blocking(self.fd,False)
        self.selector=selectors.DefaultSelector()
        self.selector.register(self.fd,selectors.EVENT_READ)
        self.buffer=bytearray()
        self.eof=False
        self.end=time.monotonic()+timeout
        self.last=time.monotonic()
        self.pid=pid
    def fill(self):
        while not self.eof:
            now=time.monotonic()
            if now>=self.end:
                raise TimeoutError('bounded native blob capture exceeded 300 seconds')
            if now-self.last>=20:
                print(json.dumps({'native_pid':self.pid,'status':'RUNNING_BOUNDED_BLOB_CAPTURE'}),flush=True)
                self.last=now
            if self.selector.select(min(1,self.end-now)):
                data=os.read(self.fd,1024*1024)
                if data:
                    self.buffer.extend(data)
                    return
                self.eof=True
    def readline(self):
        while b'\n' not in self.buffer and not self.eof:
            self.fill()
            assert len(self.buffer)<1024*1024 or b'\n' in self.buffer, 'oversized native blob header'
        end=self.buffer.find(b'\n')
        n=end+1 if end>=0 else len(self.buffer)
        data=bytes(self.buffer[:n])
        del self.buffer[:n]
        return data
    def read(self,n=-1):
        if n<0:
            while not self.eof:
                self.fill()
                assert len(self.buffer)<=1024*1024, 'unexpected trailing native blob stream'
            n=len(self.buffer)
        else:
            while len(self.buffer)<n and not self.eof:
                self.fill()
        data=bytes(self.buffer[:n])
        del self.buffer[:n]
        return data
    def close(self):
        self.selector.close()
