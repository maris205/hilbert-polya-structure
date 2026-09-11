// UGR nonauthor candidate verifier. Standard C++17 plus checked GNU int128.
// No repository/runtime inputs, no author code, no canonical reads.
// Full 13-letter local certificate; 81-state height-overlap core automaton;
// TCSD sign-stratum union for the complete shared rank-family inverse.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Z = __int128_t;
uint64_t assertions = 0;
map<string,uint64_t> kinds;
uint64_t record_digest = 14695981039346656037ull;
void need(bool ok, const string& kind) {
    ++assertions; ++kinds[kind];
    if (!ok) throw runtime_error(kind);
}
Z plusz(Z a, Z b) {
    Z c;
    if (__builtin_add_overflow(a,b,&c)) throw runtime_error("int128 addition overflow");
    return c;
}
Z timesz(Z a, Z b) {
    Z c;
    if (__builtin_mul_overflow(a,b,&c)) throw runtime_error("int128 multiplication overflow");
    return c;
}
string decimal(Z x) {
    if (x == 0) return "0";
    bool neg = x < 0; if (neg) x = -x;
    string ans;
    while (x) { ans.push_back(char('0' + x%10)); x /= 10; }
    if (neg) ans.push_back('-');
    reverse(ans.begin(),ans.end()); return ans;
}
void record(uint64_t x) {
    for (int k=0;k<8;++k) { record_digest ^= (x >> (8*k)) & 255; record_digest *= 1099511628211ull; }
}
int power3(int n) { int p=1; while(n--) p*=3; return p; }
vector<int> digits(int id,int n) {
    vector<int> v(n); for(int i=n-1;i>=0;--i) {v[i]=id%3;id/=3;} return v;
}
int encode(const vector<int>& v) { int id=0;for(int x:v)id=3*id+x;return id; }
string word(const vector<int>& v) { string s;for(int x:v)s+=char('0'+x);return s; }
int rank_rule(int a,int b,int c) { return (a>b)+(c>b); }
vector<int> step(const vector<int>& x) {
    const int n=x.size(); vector<int> y(n);
    for(int i=0;i<n;++i)y[i]=rank_rule(x[(i+n-1)%n],x[i],x[(i+1)%n]);return y;
}
bool extreme(int a,int b,int c) {return (b<a && b<c)||(b>a && b>c);}
unsigned extrema(const vector<int>& x) {
    unsigned s=0;int n=x.size();
    for(int i=0;i<n;++i)if(extreme(x[(i+n-1)%n],x[i],x[(i+1)%n]))s|=1u<<i;
    return s;
}

void full_local_certificate() {
    uint64_t changed=0,unchanged=0;
    map<pair<int,int>,uint64_t> events;
    for(int id=0;id<power3(13);++id) {
        int row[5][13] = {};
        int q=id;for(int j=12;j>=0;--j){row[0][j]=q%3;q/=3;}
        unsigned initial=0;
        for(int j=1;j<=11;++j)if(extreme(row[0][j-1],row[0][j],row[0][j+1]))initial|=1u<<j;
        int ws=0,wj=0;
        for(int t=1;t<=4;++t) {
            for(int j=t;j<=12-t;++j)row[t][j]=rank_rule(row[t-1][j-1],row[t-1][j],row[t-1][j+1]);
            for(int j=t+1;j<=11-t;++j)
                if(!ws && !(initial&(1u<<j)) && extreme(row[t][j-1],row[t][j],row[t][j+1])) {ws=t;wj=j;}
        }
        bool differs=row[4][6]!=row[2][6];
        need(!differs || ws>0,"direct_full_13_letter_local_implication");
        if(differs) {
            ++changed;++events[{ws,wj-6}];
            need(!extreme(row[0][wj-1],row[0][wj],row[0][wj+1]),"local_witness_original_nonextreme");
            need(extreme(row[ws][wj-1],row[ws][wj],row[ws][wj+1]),"local_witness_new_extreme");
        } else ++unchanged;
        record(id);record(differs);record(differs ? 100*ws+wj : 0);
    }
    cout<<"{\"section\":\"direct_full_local_certificate\",\"words\":"<<power3(13)
        <<",\"center_changed\":"<<changed<<",\"center_equal\":"<<unchanged<<",\"witness_census\":[";
    bool comma=false;for(auto [key,val]:events){if(comma)cout<<',';comma=true;cout<<'['<<key.first<<','<<key.second<<','<<val<<']';}
    cout<<"]}\n";
}

vector<Z> core_traces() {
    const int N=81;
    vector<vector<int>> edges(N);
    int count=0;
    for(int id=0;id<N;++id) {
        auto w=digits(id,4);
        for(int e=0;e<3;++e) {
            int u=rank_rule(w[0],w[1],w[2]),v=rank_rule(w[1],w[2],w[3]),z=rank_rule(w[2],w[3],e);
            if(rank_rule(u,v,z)==w[2]){edges[id].push_back((id%27)*3+e);++count;}
        }
    }
    vector<vector<Z>> p(N,vector<Z>(N));for(int i=0;i<N;++i)p[i][i]=1;
    vector<Z> traces(82), coeff(82);coeff[0]=1;
    vector<int> expected={1,-1,-1,-3,2,2,0,0,1,-1};
    for(int n=1;n<=81;++n) {
        vector<vector<Z>> nxt(N,vector<Z>(N));
        for(int i=0;i<N;++i)for(int k=0;k<N;++k)if(p[i][k])
            for(int j:edges[k])nxt[i][j]=plusz(nxt[i][j],p[i][k]);
        p.swap(nxt);
        for(int i=0;i<N;++i)traces[n]=plusz(traces[n],p[i][i]);
        Z sum=0;for(int k=1;k<=n;++k)sum=plusz(sum,timesz(coeff[n-k],traces[k]));
        need(sum%n==0,"exact_Newton_divisibility_81_state_graph");
        coeff[n]=-sum/n;
        need(coeff[n]==(n<(int)expected.size()?expected[n]:0),"full_81_degree_characteristic_polynomial");
        need((traces[n]-1)%2==0,"core_nonzero_two_cycle_pairing");
    }
    cout<<"{\"section\":\"independent_height_overlap_core_graph\",\"vertices\":81,\"edges\":"<<count
        <<",\"det_I_minus_zA_nonzero_coefficients\":[1,-1,-1,-3,2,2,0,0,1,-1],\"all_72_remaining_coefficients_zero\":true,\"traces_n1_to_81\":[";
    for(int n=1;n<=81;++n){if(n>1)cout<<',';cout<<decimal(traces[n]);}cout<<"]}\n";
    return traces;
}

bool core_language(const vector<int>& x) {
    int n=x.size(),nz=count_if(x.begin(),x.end(),[](int v){return v>0;});
    if(nz==0)return true;if(nz==n)return false;
    int start=0;while(!(x[start]==0 && x[(start+n-1)%n]>0))++start;
    vector<int> zero_lengths;vector<string> positive;
    int used=0;
    while(used<n) {
        int len=0;while(used<n && x[(start+used)%n]==0){++len;++used;}
        zero_lengths.push_back(len);string s;
        while(used<n && x[(start+used)%n]>0){s+=char('0'+x[(start+used)%n]);++used;}
        positive.push_back(s);
    }
    set<string> allowed={"2","11","12","21","121"};
    for(int j=0;j<(int)positive.size();++j) {
        if(zero_lengths[j]>2 || !allowed.count(positive[j]))return false;
        if((positive[j]=="12"||positive[j]=="121")&&zero_lengths[j]!=1)return false;
        if((positive[j]=="21"||positive[j]=="121")&&zero_lengths[(j+1)%positive.size()]!=1)return false;
    }
    return true;
}
long long fib(int n){long long a=0,b=1;while(n--){long long c=a+b;a=b;b=c;}return a;}
long long lucas(int n){if(n==0)return 2;return fib(n-1)+fib(n+1);}
long long tcsd_weight(const vector<int>& encoded_signs) {
    vector<int>s;for(int v:encoded_signs)if(v!=1)s.push_back(v);
    if(s.empty())return 3;
    if(all_of(s.begin(),s.end(),[&](int v){return v==s[0];}))return 0;
    int n=s.size(),start=0;while(s[start]==s[(start+n-1)%n])++start;
    vector<int>runs;
    for(int done=0;done<n;){int z=s[(start+done)%n],len=0;while(done<n&&s[(start+done)%n]==z){++done;++len;}if(len>2)return 0;runs.push_back(len);}
    vector<int>doubled;for(int j=0;j<(int)runs.size();++j)if(runs[j]==2)doubled.push_back(j);
    if(doubled.empty())return lucas(n);
    long long total=1;for(int j=0;j<(int)doubled.size();++j){int gap=(doubled[(j+1)%doubled.size()]-doubled[j]-1+(int)runs.size())%runs.size();total*=fib(gap+1);}return total;
}
void add_rotations(set<int>& out,const string& s){for(int k=0;k<(int)s.size();++k){vector<int>x;for(int j=0;j<(int)s.size();++j)x.push_back(s[(j+k)%s.size()]-'0');out.insert(encode(x));}}
set<int> expected_maximizers(int n) {
    set<int>out;
    if(n==3){out.insert(0);add_rotations(out,"002");add_rotations(out,"011");return out;}
    if(n%2==0){string s;for(int j=0;j<n/2;++j)s+="02";add_rotations(out,s);return out;}
    string a="00",b="011";for(int j=0;j<n/2-1;++j){a+="20";b+="02";}a+="2";add_rotations(out,a);add_rotations(out,b);return out;
}

void cyclic_boxes(const vector<Z>& core_counts) {
    for(int n=3;n<=10;++n) {
        int total=power3(n);vector<int>next(total),fibre(total),lower_fibre(total),sign_fibre(total);
        map<int,int>height_hist,period_hist;int fixed=0,core=0;
        for(int id=0;id<total;++id) {
            auto x=digits(id,n),y=step(x);int yi=encode(y);next[id]=yi;++fibre[yi];
            vector<int>complement(n),lower(n),signs(n);
            for(int i=0;i<n;++i){complement[i]=2-x[i];lower[i]=(x[(i+n-1)%n]<x[i])+(x[(i+1)%n]<x[i]);int d=x[(i+1)%n]-x[i];signs[i]=(d>0)-(d<0)+1;}
            ++lower_fibre[encode(lower)];++sign_fibre[encode(signs)];
            auto inverse_flip=step(complement);
            need(inverse_flip==lower,"full_source_input_complement_inverse_bijection");
            need((extrema(x)&~extrema(y))==0,"strict_extrema_monotone_all_cyclic_sources");
            bool is_core=step(y)==x;
            need(is_core==core_language(x),"complete_core_language_vs_literal_square");
            core+=is_core;fixed+=(id==yi);
            if(id==yi)need(id==0,"only_fixed_point_zero");
        }
        need(fixed==1,"fixed_count_exact");need(core_counts[n]==core,"81_state_trace_vs_complete_literal_core");
        vector<long long>union_counts(total);vector<int>strata(total),largest_stratum(total);
        for(int id=0;id<total;++id) {
            auto signs=digits(id,n);long long count=tcsd_weight(signs);
            need(count==sign_fibre[id],"prior_TCSD_exact_gap_weight_vs_literal_sources");
            vector<int>b(n);for(int i=0;i<n;++i)b[i]=(signs[(i+n-1)%n]==0)+(signs[i]==2);
            int bi=encode(b);union_counts[bi]+=count;
            if(count){++strata[bi];largest_stratum[bi]=max(largest_stratum[bi],(int)count);}
        }
        set<int>maxima;int mx=*max_element(fibre.begin(),fibre.end()),image=0,multi=0;
        int strict_union_example=-1;
        for(int id=0;id<total;++id) {
            need(union_counts[id]==fibre[id],"every_target_full_TCSD_union_inverse");
            need(lower_fibre[id]==fibre[id],"every_target_shared_rank_fibre_cardinality");
            if(fibre[id]==mx)maxima.insert(id);image+=(fibre[id]>0);multi+=(strata[id]>1);
            if(strata[id]>1 && strict_union_example<0)strict_union_example=id;
            vector<int>seen(total,-1); // bounded traversal has at most 3^n vertices.
            int cur=id,t=0;while(seen[cur]<0){seen[cur]=t++;cur=next[cur];}
            int h=seen[cur],period=t-h;
            need(period==1||period==2,"all_cyclic_periods_one_or_two");
            need(h<=4*n+2,"nonsharp_global_clock_pressure");
            ++height_hist[h];++period_hist[period];record(id);record(fibre[id]);record(h);record(period);
        }
        need(mx==lucas(2*(n/2)),"sharp_shared_fibre_maximum_value");
        need(maxima==expected_maximizers(n),"complete_shared_fibre_maximum_equality_targets");
        cout<<"{\"section\":\"full_original_cyclic_box\",\"n\":"<<n<<",\"states\":"<<total<<",\"image\":"<<image<<",\"core\":"<<core<<",\"height_histogram\":{";
        bool comma=false;for(auto [h,c]:height_hist){if(comma)cout<<',';comma=true;cout<<'\"'<<h<<"\":"<<c;}cout<<"},\"eventual_period_histogram\":{";
        comma=false;for(auto [h,c]:period_hist){if(comma)cout<<',';comma=true;cout<<'\"'<<h<<"\":"<<c;}cout<<"},\"maximum\":"<<mx<<",\"all_maximizers\":[";
        comma=false;for(int id:maxima){if(comma)cout<<',';comma=true;cout<<'\"'<<word(digits(id,n))<<'\"';}
        cout<<"],\"targets_with_multiple_feasible_sign_strata\":"<<multi;
        if(strict_union_example>=0)cout<<",\"first_union_example\":{\"target\":\""<<word(digits(strict_union_example,n))<<"\",\"strata\":"<<strata[strict_union_example]<<",\"largest_stratum\":"<<largest_stratum[strict_union_example]<<",\"whole_fibre\":"<<fibre[strict_union_example]<<'}';
        cout<<"}\n";
    }
}

void witness_profiles() {
    for(int n=4;n<=64;++n) {
        vector<int>source(n,1);source[0]=0;auto row=step(source);int m=n/2;
        for(int s=0;s<=m;++s) {
            vector<int>expected(n);
            for(int i=0;i<n;++i) {
                int d=min(i,n-i);
                if(s==m)expected[i]=(n%2&&d==m)?1:2*((s-d)%2==0);
                else if(d==s&&s>0)expected[i]=1;
                else if(d<s||d==0)expected[i]=2*((s-d)%2==0);
            }
            need(row==expected,"single_seed_complete_wave_profile");
            need((step(step(row))==row)==(s==m),"single_seed_exact_entrance");
            row=step(row);
        }
    }
    cout<<"{\"section\":\"witness_only_not_full_boxes\",\"n_min\":4,\"n_max\":64,\"exact_source_entrance\":\"floor(n/2)+1\",\"global_sharp_clock_not_claimed\":true}\n";
}
int main() {
    try {
        full_local_certificate();auto traces=core_traces();cyclic_boxes(traces);witness_profiles();
        cout<<"{\"section\":\"summary\",\"status\":\"PASS_MATHEMATICS_NOT_SOURCE_ADMISSION\",\"assertions\":"<<assertions<<",\"fnv1a_64_ordered_record_digest_decimal\":\""<<record_digest<<"\",\"assertions_by_kind\":{";
        bool comma=false;for(auto [k,v]:kinds){if(comma)cout<<',';comma=true;cout<<'\"'<<k<<"\":"<<v;}cout<<"}}\n";return 0;
    } catch(const exception& e) {cerr<<"FAIL "<<e.what()<<" after "<<assertions<<" assertions\n";return 1;}
}
