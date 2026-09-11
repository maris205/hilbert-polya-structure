async function readBatch(){
 const selected=load("io_selected"),start=load("io_progress"),chosen=selected.slice(start,start+12).filter(p=>!p.endsWith("CONFIGURATION_BEFORE.json")&&!(p.endsWith("INPUT_OUTPUT_ROLES.json")&&!p.includes("_bibtex/")));
 const rows=await Promise.all(chosen.map(async path=>{const request={cmd:"cat "+path,workdir:"/root/autodl-tmp/symbolic_dynamics",max_output_tokens:40000};return {path,request,result:await tools.exec_command(request)};}));
 let index=load("io_next"),bodies=load("io_bodies"),patch="*** Begin Patch\n";
 for(const row of rows){const body=JSON.stringify(row,null,2);patch+="*** Add File: "+load("io_dir")+"/native/read"+String(index++).padStart(3,"0")+".json\n"+body.split("\n").map(x=>"+"+x).join("\n")+"\n";if(row.result.exit_code===0&&!row.result.output.includes("tokens truncated"))bodies[row.path]=row.result.output;}
 await tools.apply_patch(patch+"*** End Patch");store("io_bodies",bodies);store("io_next",index);store("io_progress",Math.min(start+12,selected.length));
 return {done:load("io_progress"),total:selected.length,failed:rows.filter(r=>r.result.exit_code!==0||r.result.output.includes("tokens truncated")).map(r=>({path:r.path,exit:r.result.exit_code,tokens:r.result.original_token_count}))};
}
