function sha256Text(text) {
  const bytes=[];
  for (const char of text) {
    const c=char.codePointAt(0);
    if(c<128) bytes.push(c);
    else if(c<2048) bytes.push(192|(c>>>6),128|(c&63));
    else if(c<65536) bytes.push(224|(c>>>12),128|((c>>>6)&63),128|(c&63));
    else bytes.push(240|(c>>>18),128|((c>>>12)&63),128|((c>>>6)&63),128|(c&63));
  }
  const length=bytes.length, bits=length*8;
  bytes.push(128);while(bytes.length%64!==56)bytes.push(0);
  const high=Math.floor(bits/4294967296),low=bits>>>0;
  for(let j=3;j>=0;j--)bytes.push((high>>>(8*j))&255);
  for(let j=3;j>=0;j--)bytes.push((low>>>(8*j))&255);
  const primes=[];for(let n=2;primes.length<64;n++)if(primes.every(p=>n%p!==0))primes.push(n);
  const H=primes.slice(0,8).map(n=>(Math.sqrt(n)%1*4294967296)>>>0);
  const K=primes.map(n=>(Math.cbrt(n)%1*4294967296)>>>0);
  const rot=(v,n)=>(v>>>n)|(v<<(32-n));
  for(let offset=0;offset<bytes.length;offset+=64){
    const w=new Uint32Array(64);
    for(let j=0;j<16;j++)w[j]=(bytes[offset+4*j]<<24)|(bytes[offset+4*j+1]<<16)|(bytes[offset+4*j+2]<<8)|bytes[offset+4*j+3];
    for(let j=16;j<64;j++){const x=w[j-15],y=w[j-2];w[j]=(w[j-16]+(rot(x,7)^rot(x,18)^(x>>>3))+w[j-7]+(rot(y,17)^rot(y,19)^(y>>>10)))>>>0;}
    let [a,b,c,d,e,f,g,h]=H;
    for(let j=0;j<64;j++){const t1=(h+(rot(e,6)^rot(e,11)^rot(e,25))+((e&f)^(~e&g))+K[j]+w[j])>>>0;
      const t2=((rot(a,2)^rot(a,13)^rot(a,22))+((a&b)^(a&c)^(b&c)))>>>0;
      h=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;
    }
    const block=[a,b,c,d,e,f,g,h];for(let j=0;j<8;j++)H[j]=(H[j]+block[j])>>>0;
  }
  return {bytes:length,sha256:H.map(v=>v.toString(16).padStart(8,"0")).join("")};
}
