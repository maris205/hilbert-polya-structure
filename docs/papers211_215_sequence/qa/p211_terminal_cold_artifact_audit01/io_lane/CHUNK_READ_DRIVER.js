async function readChunks(){
 const all=load("io_chunks"),start=load("io_chunk_progress"),chosen=all.slice(start,start+6);
 const rows=await Promise.all(chosen.map(async chunk=>{const request={cmd:"sed -n '"+chunk.start+","+chunk.end+"p' "+chunk.path,workdir:"/root/autodl-tmp/symbolic_dynamics",max_output_tokens:35000};return {...chunk,request,result:await tools.exec_command(request)};}));
 let index=load("io_next"),bodies=load("io_chunk_bodies"),patch="*** Begin Patch\n";
 for(const row of rows){patch+="*** Add File: "+load("io_dir")+"/native/read"+String(index++).padStart(3,"0")+".json\n"+JSON.stringify(row,null,2).split("\n").map(x=>"+"+x).join("\n")+"\n";if(row.result.exit_code===0&&!row.result.output.includes("tokens truncated"))(bodies[row.path]??={})[row.start]=row.result.output;}
 await tools.apply_patch(patch+"*** End Patch");store("io_chunk_bodies",bodies);store("io_next",index);store("io_chunk_progress",start+chosen.length);
 return {chunk_done:load("io_chunk_progress"),total:all.length,failed:rows.filter(r=>r.result.exit_code!==0||r.result.output.includes("tokens truncated")).map(r=>({path:r.path,start:r.start,exit:r.result.exit_code,tokens:r.result.original_token_count}))};
}
