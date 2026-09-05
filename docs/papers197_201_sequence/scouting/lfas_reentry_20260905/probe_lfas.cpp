#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>
using Matrix=std::vector<uint32_t>;
struct Rect {int i,k,a,b; bool operator==(const Rect& x)const{return i==x.i&&k==x.k&&a==x.a&&b==x.b;}};
Rect select(const Matrix& x) {
 for(int i=0;i<(int)x.size();++i)for(int k=i+1;k<(int)x.size();++k){
  auto a=x[i]&~x[k], b=x[k]&~x[i];
  if(a&&b){int u=__builtin_ctz(a),v=__builtin_ctz(b); return {i,k,std::min(u,v),std::max(u,v)};}
 } return {-1,-1,-1,-1};
}
void step(Matrix&x,const Rect&q){auto m=(1u<<q.a)|(1u<<q.b);x[q.i]^=m;x[q.k]^=m;}
int depth(Matrix x){
 auto q=select(x);int t=0;
 while(q.i>=0){step(x,q);auto p=select(x);if(p==q)return t;++t;q=p;}
 return t;
}
void show(Matrix x,int s){std::cout<<" rows=";for(auto v:x){for(int j=0;j<s;++j)std::cout<<((v>>j)&1);std::cout<<",";}}
int main(int argc,char**argv){
 int r=std::stoi(argv[1]),s=std::stoi(argv[2]);uint64_t count=std::stoull(argv[3]);
 std::mt19937_64 rng(20260905);uint32_t mask=(1u<<s)-1;int best=-1;Matrix witness(r),x(r),walk(r);int walkdepth=-1;
 for(uint64_t z=0;z<count;++z){
  if(argc>4){for(int i=0;i<r;++i)x[i]=(z>>(i*s))&mask;}
  else if(z%10000==0||best<0){for(auto&v:x)v=rng()&mask;walkdepth=-1;}
  else {x=walk;for(unsigned m=0;m<1+rng()%4;++m)x[rng()%r]^=1u<<(rng()%s);}
  int d=depth(x);if(d>=walkdepth){walk=x;walkdepth=d;}
  if(d>best){best=d;witness=x;std::cout<<"r="<<r<<" s="<<s<<" sample="<<z<<" max_tail="<<best;show(witness,s);std::cout<<"\n";}
 }
 std::cout<<"trace"; x=witness;for(int t=0;t<=best;++t){auto q=select(x);std::cout<<" ("<<q.i<<","<<q.k<<","<<q.a<<","<<q.b<<")";if(q.i>=0)step(x,q);}std::cout<<"\n";
}
