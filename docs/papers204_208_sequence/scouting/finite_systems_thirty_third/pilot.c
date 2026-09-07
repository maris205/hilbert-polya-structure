/* Original OTC census. Fixed complete box n=1..4. No imports or data files. */
typedef unsigned long U;
static char buffer[65536];
static U used;
static unsigned next[729], fibre[729], seen[729], stamp;

static long call3(long n, long a, long b, long c) {
    long r;
    __asm__ volatile ("syscall" : "=a"(r) : "a"(n), "D"(a), "S"(b), "d"(c) : "rcx", "r11", "memory");
    return r;
}
static void stop(unsigned code) {
    call3(60, code, 0, 0);
    for (;;) {}
}
static void flush(void) {
    U sent = 0;
    while (sent < used) {
        long r = call3(1, 1, (long)(buffer + sent), used - sent);
        if (r <= 0) stop(90);
        sent += (U)r;
    }
    used = 0;
}
static void put(char c) {
    if (used == sizeof buffer) flush();
    buffer[used++] = c;
}
static void text(const char *s) { while (*s) put(*s++); }
static void number(unsigned x) {
    char b[20]; unsigned z = 0;
    do { b[z++] = (char)('0' + x % 10); x /= 10; } while(x);
    while(z) put(b[--z]);
}
static void field(unsigned x) { put(' '); number(x); }
static unsigned checked;
static void check(int b) { ++checked; if (!b) stop(91); }

static unsigned step(unsigned n, unsigned id) {
    unsigned a[4][4], b[4][4];
    for (unsigned i=0;i<4;++i) for(unsigned j=0;j<4;++j) a[i][j]=b[i][j]=0;
    for (unsigned i=0;i<n;++i) for(unsigned j=i+1;j<n;++j) {
        unsigned d=id%3; id/=3;
        a[i][j]=(d==1); a[j][i]=(d==2);
    }
    for (unsigned i=0;i<n;++i) for(unsigned j=0;j<n;++j)
        for(unsigned k=0;k<n;++k) b[i][j] |= a[i][k] & a[k][j];
    unsigned out=0, w=1;
    for (unsigned i=0;i<n;++i) for(unsigned j=i+1;j<n;++j) {
        unsigned d=(b[i][j] && !b[j][i]) ? 1 : ((!b[i][j] && b[j][i]) ? 2 : 0);
        out += w*d; w*=3;
    }
    return out;
}

static void census(void) {
    text("OTC original complete pilot v1; columns STATE n id target tail period cycle_min incoming\n");
    unsigned total=0;
    for(unsigned n=1;n<=4;++n) {
        unsigned count=1;
        for(unsigned k=0;k<n*(n-1)/2;++k) count*=3;
        unsigned tails[730], periods[730], max_tail=0, max_period=0, image=0, rec=0, fixed=0, max_fibre=0;
        for(unsigned k=0;k<730;++k) tails[k]=periods[k]=0;
        for(unsigned k=0;k<count;++k) fibre[k]=0;
        for(unsigned k=0;k<count;++k) {
            next[k]=step(n,k); check(next[k]<count); ++fibre[next[k]];
        }
        for(unsigned k=0;k<count;++k) {
            unsigned x=k, clock=0, arrival[729]; ++stamp;
            while(seen[x]!=stamp) { seen[x]=stamp; arrival[x]=clock++; x=next[x]; check(clock<=count); }
            unsigned tail=arrival[x], period=clock-tail, rep=x, y=next[x];
            while(y!=x) { if(y<rep) rep=y; y=next[y]; }
            ++tails[tail]; ++periods[period];
            if(tail>max_tail) max_tail=tail;
            if(period>max_period) max_period=period;
            if(!tail) ++rec;
            if(next[k]==k) ++fixed;
            if(fibre[k]) ++image;
            if(fibre[k]>max_fibre) max_fibre=fibre[k];
            text("STATE"); field(n); field(k); field(next[k]); field(tail); field(period); field(rep); field(fibre[k]); put('\n');
            if(!tail && k==rep) {
                text("CYCLE"); field(n); field(period); y=k;
                do { field(y); y=next[y]; } while(y!=k);
                put('\n');
            }
        }
        unsigned fs=0, ts=0, ps=0;
        for(unsigned k=0;k<count;++k) fs+=fibre[k];
        for(unsigned k=0;k<730;++k) { ts+=tails[k]; ps+=periods[k]; }
        check(fs==count); check(ts==count); check(ps==count);
        text("SUMMARY n states image recurrent fixed max_tail max_period max_fibre");
        field(n); field(count); field(image); field(rec); field(fixed); field(max_tail); field(max_period); field(max_fibre); put('\n');
        text("TAIL_HIST"); field(n);
        for(unsigned k=0;k<=max_tail;++k) { field(k); put(':'); number(tails[k]); }
        put('\n'); text("PERIOD_HIST"); field(n);
        for(unsigned k=1;k<=max_period;++k) if(periods[k]) { field(k); put(':'); number(periods[k]); }
        put('\n'); total+=count;
    }
    text("DONE states checks"); field(total); field(checked); put('\n'); flush();
}

void _start(void) { census(); stop(0); }
