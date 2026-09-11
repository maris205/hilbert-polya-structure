function reconstructIO(data) {
  const {bodies,pins,inventory,headers}=data;
  const root="/root/autodl-tmp/symbolic_dynamics/";
  const base="papers/211-kernel-image-projection-feedback/qa_final/cold_build_2/inner/";
  const cold=root+base+"source_only";
  const body=n=>bodies[base+n], obj=n=>JSON.parse(body(n));
  const generated=["aux","bbl","blg","fls","log","out","pdf","toc"].map(e=>"main."+e);
  const passes=["pass1","bibtex","pass2","pass3"];
  const sourceNames=["main.tex","math_commands.tex","references.bib","sections/0_abstract.tex","sections/1_introduction.tex","sections/2_image.tex","sections/3_clock.tex","sections/4_inverse.tex","sections/5_scope.tex"];
  const roleNames=["SOURCE","EXTERNAL_PRELOCKED","GENERATED_BEFORE","GENERATED_EARLIER_OUTPUT_SAME_PASS","GENERATED_OUTPUT"];
  const initial=obj("SOURCE_ONLY_INITIAL.json"),config=obj("CONFIGURATION_BEFORE.json"),result=obj("RESULT.json");
  const groups={},failures=[],checks=[];
  const stable=x=>JSON.stringify(x,(_,v)=>v&&typeof v==="object"&&!Array.isArray(v)?Object.fromEntries(Object.entries(v).sort(([a],[b])=>a.localeCompare(b))):v);
  const check=(test,group,detail)=>{groups[group]=(groups[group]||0)+1;if(!test)failures.push({group,detail});checks.push({group,detail,passed:!!test});};
  const equal=(a,b,g,d)=>check(stable(a)===stable(b),g,d);
  const pin=n=>pins[base+n];
  const pinOnly=v=>({bytes:v.bytes,sha256:v.sha256});
  const lines=t=>{const a=t.split("\n");if(a.at(-1)==="")a.pop();return a;};
  const exactMemberList=prefix=>inventory.filter(p=>p.startsWith(base+prefix)).map(p=>p.slice((base+prefix).length)).sort();
  equal(Object.keys(initial).sort(),sourceNames.slice().sort(),"source","exact initial nine names");
  for(const name of sourceNames)equal(initial[name],pin("source_only/"+name),"source","actual copied source "+name);
  for(const file of ["SOURCES_BEFORE.json","SOURCES_AFTER.json","COPIED_SOURCES_AFTER.json"])equal(obj(file),initial,"source",file);
  equal(exactMemberList("source_only/"),[...sourceNames,...generated.filter(n=>Object.hasOwn(pins,base+"source_only/"+n))].sort(),"source","final source_only exact permitted members");
  const main=body("source_only/main.tex");
  check(main.includes("\\documentclass[11pt,a4paper]{amsart}")&&main.includes("\\bibliographystyle{amsplain}")&&main.includes("\\bibliography{references}"),"source_graph","literal amsart/amsplain/references");
  equal([...main.matchAll(/\\input\{([^}]+)\}/g)].map(m=>m[1]+(m[1].endsWith(".tex")?"":".tex")),sourceNames.filter(n=>!["main.tex","references.bib"].includes(n)),"source_graph","ordered local inputs");
  equal([...main.matchAll(/\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(",")),["fontenc","lmodern","geometry","amsmath","amssymb","mathtools","booktabs","microtype","hyperref"],"source_graph","packages");
  for(const name of sourceNames)check(!/\\(?:include|includegraphics|write18|openin|openout|read|catcode)\b/.test(body("source_only/"+name)),"source_graph","bounded explicit I/O "+name);
  const normalize=path=>{const parts=[];for(const part of path.split("/")){if(!part||part===".")continue;if(part==="..")parts.pop();else parts.push(part);}return "/"+parts.join("/");};
  const recon={},summaries={},diagnostics={},snapshots={},fullFLS=[];
  let previous=null;
  for(let pi=0;pi<passes.length;pi++){
    const pass=passes[pi],prefix="pass_artifacts_"+pass+"/";
    const before=obj(prefix+"before/GENERATED.json"),after=obj(prefix+"after/GENERATED.json");
    snapshots[pass]={before,after};
    for(const [phase,snap] of Object.entries({before,after})){
      equal(Object.keys(snap).sort(),generated.slice().sort(),"snapshot",pass+"/"+phase+" eight roles");
      const expected=["GENERATED.json"];
      for(const name of generated){
        const row=snap[name];
        check(typeof row.present==="boolean","snapshot",pass+"/"+phase+"/"+name+" boolean present");
        equal(Object.keys(row).sort(),(row.present?["present","bytes","sha256"]:["present"]).sort(),"snapshot",pass+"/"+phase+"/"+name+" exact keys");
        if(row.present&&name!=="main.pdf"){expected.push(name);equal(pin(prefix+phase+"/"+name),pinOnly(row),"snapshot",pass+"/"+phase+"/"+name+" archived bytes");}
      }
      equal(exactMemberList(prefix+phase+"/"),expected.sort(),"snapshot",pass+"/"+phase+" complete archive members; intermediate PDFs intentionally absent");
    }
    if(previous===null)check(generated.every(n=>before[n].present===false),"chain","source-only: every generated role absent before pass1");
    else equal(before,previous,"chain",pass+" before equals previous after");
    previous=after;
    const recorded=obj(prefix+"INPUT_OUTPUT_ROLES.json");
    if(pass!=="bibtex"){
      const written=new Set(),raw=body(prefix+"after/main.fls");
      const events=lines(raw).map((line,i)=>{
        const number=i+1;
        if(line.startsWith("PWD ")){check(line==="PWD "+cold,"fls",pass+":"+number+" exact PWD");return {line:number,kind:"PWD",raw:line};}
        const split=line.indexOf(" "),kind=line.slice(0,split),spelling=line.slice(split+1);
        check(split>0&&["INPUT","OUTPUT"].includes(kind),"fls",pass+":"+number+" record syntax");
        const absolute=normalize(spelling.startsWith("/")?spelling:cold+"/"+spelling);
        const local=absolute.startsWith(cold+"/");
        let event={line:number,kind,spelling,absolute,resolved:local?absolute:config[absolute]?.resolved};
        if(local){
          const name=absolute.slice(cold.length+1);event.relative=name;
          if(kind==="OUTPUT"){check(generated.includes(name)&&!sourceNames.includes(name),"fls",pass+":"+number+" bounded generated output");written.add(name);event={...event,role:"GENERATED_OUTPUT",after:after[name]};}
          else if(Object.hasOwn(initial,name))event={...event,role:"SOURCE",pin:initial[name]};
          else {
            check(generated.includes(name),"fls",pass+":"+number+" generated local input name");
            if(written.has(name))event={...event,role:"GENERATED_EARLIER_OUTPUT_SAME_PASS",read_time_bytes:"NOT_OBSERVED_BY_FLS",pass_start:before[name],pass_end:after[name]};
            else {check(before[name]?.present===true,"fls",pass+":"+number+" prior-pass generated input exists");event={...event,role:"GENERATED_BEFORE",input_pin:before[name],pass_end:after[name]};}
          }
        }else{
          check(kind==="INPUT"&&config[absolute]?.kind==="file"&&config[absolute]?.path===absolute,"fls",pass+":"+number+" exact external spelling in archived prelock");
          event={...event,role:"EXTERNAL_PRELOCKED",pin:config[absolute]?pinOnly(config[absolute]):null};
        }
        return event;
      });
      const roles=Object.fromEntries(roleNames.map(role=>[role,events.filter(e=>e.role===role).length]));
      const expected={events,count:events.length,roles,limitation:"FLS records ordered declared I/O, not exact mid-pass content or non-FLS OS reads."};
      equal(recorded,expected,"fls_full_object",pass+" complete event order/duplicate/spelling/role/field equality");
      recon[pass]=expected;
      equal([...new Set(events.filter(e=>e.kind==="OUTPUT").map(e=>e.relative))].sort(),["main.aux","main.log","main.out","main.pdf"],"fls_outputs",pass+" four declared outputs; recorder does not declare its own FLS");
      const log=body(prefix+"after/main.log"),logLines=lines(log);
      const patterns={undefined:/undefined/,overfull:/Overfull/,underfull:/Underfull/,warnings:/Warning/,missing_characters:/Missing character/,rerun:/(?:Rerun to|Please .*rerun|Label\(s\) may have changed)/};
      const captured=Object.fromEntries(Object.entries(patterns).map(([key,rx])=>[key,logLines.filter(l=>rx.test(l))]));
      const warningEmissions=logLines.flatMap((text,i)=>/^(?:pdfTeX\s+warning\b|(?:LaTeX|Package\s+\S+)\s+Warning\b)/i.test(text)?[{line:i+1,text}]:[]);
      const infoMissing=logLines.flatMap((text,i)=>/^Package microtype Info: Character .* is missing$/.test(text)?[{line:i+1,context:logLines.slice(i,i+3)}]:[]);
      const outputs=[...log.matchAll(/Output written on main\.pdf \((\d+) pages?, (\d+) bytes\)/g)];
      const stdoutOutputs=[...body("commands/"+pass+"/stdout.raw").matchAll(/Output written on main\.pdf \((\d+) pages?, (\d+) bytes\)/g)];
      check(outputs.length===1&&+outputs[0][2]===after["main.pdf"].bytes,"pdf_measurement",pass+" complete log PDF bytes");
      equal(outputs.map(m=>m.slice(1)),stdoutOutputs.map(m=>m.slice(1)),"pdf_measurement",pass+" log/stdout PDF tuple");
      diagnostics[pass]={raw_log:pin(prefix+"after/main.log"),lines:logLines.length,recorded_regex_census:captured,actual_warning_emissions:warningEmissions,uncaptured_warning_emissions:warningEmissions.filter(e=>!captured.warnings.includes(e.text)),microtype_informational_missing_character_contexts:infoMissing};
      summaries[pass]={events:events.length,roles,external_unique_spellings:new Set(events.filter(e=>e.role==="EXTERNAL_PRELOCKED").map(e=>e.absolute)).size,external_unique_resolved:new Set(events.filter(e=>e.role==="EXTERNAL_PRELOCKED").map(e=>e.resolved)).size,local_generated_events:events.filter(e=>e.relative&&!sourceNames.includes(e.relative)).map(e=>({line:e.line,kind:e.kind,spelling:e.spelling,role:e.role})),source_unique_names:[...new Set(events.filter(e=>e.role==="SOURCE").map(e=>e.relative))].sort(),pdf_pages:+outputs[0][1],pdf_bytes:+outputs[0][2]};
      fullFLS.push(...events);
    }else{
      const aux=body(prefix+"before/main.aux"),blg=body(prefix+"after/main.blg"),style="/usr/share/texlive/texmf-dist/bibtex/bst/amscls/amsplain.bst";
      equal([...aux.matchAll(/\\bibstyle\{([^}]+)\}/g)].map(m=>m[1]),["amsplain"],"bibtex","one explicit style");
      equal([...aux.matchAll(/\\bibdata\{([^}]+)\}/g)].map(m=>m[1]),["references"],"bibtex","one explicit database");
      check(!/\\@input\{/.test(aux),"bibtex","no nested aux input");
      equal([...blg.matchAll(/^The top-level auxiliary file:\s*(.+)$/gm)].map(m=>m[1]),["main.aux"],"bibtex","BLG aux");
      equal([...blg.matchAll(/^The style file:\s*(.+)$/gm)].map(m=>m[1]),["amsplain.bst"],"bibtex","BLG style");
      equal([...blg.matchAll(/^Database file #[0-9]+:\s*(.+)$/gm)].map(m=>m[1]),["references.bib"],"bibtex","BLG database");
      check(config[style]?.kind==="file","bibtex","unique named style has archived prelock file entry");
      const expected={mode:"BibTeX has no FLS; explicit aux/style/database plus native/config lock",inputs:[{path:"main.aux",role:"GENERATED_BEFORE",pin:before["main.aux"]},{path:"references.bib",role:"SOURCE",pin:initial["references.bib"]},{path:style,role:"EXTERNAL_PRELOCKED",pin:pinOnly(config[style])}],outputs:{"main.bbl":after["main.bbl"],"main.blg":after["main.blg"]},blg_pin:pin(prefix+"after/main.blg"),non_FLS_trace:false};
      equal(recorded,expected,"bibtex","complete input/output role object");
      for(const name of generated.filter(n=>!["main.bbl","main.blg"].includes(n)))equal(before[name],after[name],"bibtex","only BBL/BLG are new: "+name);
      const citationOccurrences=[...aux.matchAll(/\\citation\{([^}]+)\}/g)].flatMap(m=>m[1].split(","));
      const databaseKeys=[...body("source_only/references.bib").matchAll(/@\w+\{([^,]+),/g)].map(m=>m[1]);
      const bblKeys=[...body(prefix+"after/main.bbl").matchAll(/\\bibitem\{([^}]+)\}/g)].map(m=>m[1]);
      equal([...new Set(citationOccurrences)].sort(),databaseKeys.slice().sort(),"bibtex","three unique cited entries equal database");
      equal(bblKeys.slice().sort(),databaseKeys.slice().sort(),"bibtex","three generated entries equal database");
      equal(lines(blg).filter(l=>/Warning--|I couldn.t open|error message/i.test(l)),[],"bibtex","complete BLG no findings");
      recon[pass]=expected;
      summaries[pass]={input_count:expected.inputs.length,input_roles:expected.inputs.map(r=>r.role),style:expected.inputs[2],citation_occurrences:citationOccurrences,unique_citations:[...new Set(citationOccurrences)],database_keys:databaseKeys,bbl_keys:bblKeys,outputs:expected.outputs,fls_after_is_unchanged_prior_pass_recorder:body(prefix+"after/main.fls")===body(prefix+"before/main.fls")};
    }
    equal(result.passes[pi],{label:pass,native:obj("commands/"+pass+"/RECEIPT.json"),generated_after:after,roles:pin(prefix+"INPUT_OUTPUT_ROLES.json")},"pass_association",pass+" complete RESULT pass object");
  }
  equal(result.passes.map(p=>p.label),passes,"pass_association","four physical pass order");
  for(const [name,value] of Object.entries(previous)){
    equal(value,Object.hasOwn(pins,base+"source_only/"+name)?{present:true,...pin("source_only/"+name)}:{present:false},"final_chain",name+" final presence/bytes");
    if(value.present&&name!=="main.pdf")check(body("pass_artifacts_pass3/after/"+name)===body("source_only/"+name),"final_chain",name+" actual raw final/archive equality");
  }
  const measured=obj("MEASURED_NOT_VIEWED.json");
  equal(measured,result.measurements,"measurement","complete measured/result object");
  equal(measured.pdf,pin("source_only/main.pdf"),"measurement","final PDF actual digest/size");
  equal(measured.diagnostics,diagnostics.pass3.recorded_regex_census,"measurement","stored final regex census matches its source mechanism, not complete warnings");
  const metadata=Object.fromEntries(lines(body("commands/pdfinfo/stdout.raw")).filter(l=>l.includes(":")).map(l=>{const p=l.indexOf(":");return [l.slice(0,p).trim(),l.slice(p+1).trim()];}));
  equal(metadata.Pages,"5","measurement","five PDF pages");equal(metadata["File size"],measured.pdf.bytes+" bytes","measurement","PDF file size");equal(metadata.Author,"","measurement","anonymous Author");
  equal(metadata["Page size"],"595.276 x 841.89 pts (A4)","measurement","A4 media dimensions");equal(metadata["PDF version"],"1.5","measurement","PDF version");
  equal(metadata.Encrypted,"no","measurement","not encrypted");
  const fontLines=lines(body("commands/pdffonts/stdout.raw"));
  equal(fontLines[0].trim().split(/\s+/).slice(-5),["emb","sub","uni","object","ID"],"fonts","column meanings");
  const fonts=fontLines.slice(2).filter(l=>l.trim()).map(l=>l.trim().split(/\s+/));
  check(fonts.length===21&&fonts.every(f=>f.slice(-5,-2).join(" ")==="yes yes yes"),"fonts","21 actual font objects embedded/subset/Unicode flag yes");
  equal(measured.embedded_fonts,fonts.length,"fonts","measured count");
  const text=body("main.txt"),textPages=text.split("\f");if(!textPages.at(-1).trim())textPages.pop();
  equal(textPages.length,measured.pages,"measurement","full text/PDF page census");
  const markers=["[VERIFY]","??","[?]"].filter(s=>text.includes(s));
  equal(markers,[],"measurement","no specified text markers");equal(measured.text_markers,markers,"measurement","marker array");
  const refs=textPages.flatMap((p,i)=>/^\s*(?:References|Bibliography)\s*$/m.test(p)?[i+1]:[]);
  equal(refs,[5],"measurement","references on page 5");equal(measured.reference_heading_pages,refs,"measurement","reference-page array");
  equal(measured.bibtex_findings,[],"measurement","BLG finding array");
  equal(measured.visual_review,"NOT_VIEWED","measurement_scope","not a view");
  equal(measured.venue_page_limit,null,"measurement_scope","no invented venue limit");
  equal(measured.size_threshold_100KB,"NOT_AN_ACCEPTANCE_RULE","measurement_scope","100KB not acceptance");
  const imageFiles=Array.from({length:5},(_,i)=>"page-"+String(i+1).padStart(4,"0")+".png");
  equal(exactMemberList("pages/"),imageFiles,"renders","five image members");
  const renderRows=[];
  for(let i=0;i<5;i++){
    const image="pages/"+imageFiles[i],expected={page:i+1,image:root+base+image,pin:pin(image),visual_review:"NOT_VIEWED"};
    equal(measured.renders[i],expected,"renders","complete row "+(i+1));
    const hex=headers.find(r=>r.path===base+image).result.output.trim().split(/\s+/).map(h=>parseInt(h,16));
    equal(hex.slice(0,16),[137,80,78,71,13,10,26,10,0,0,0,13,73,72,68,82],"renders","PNG/IHDR header "+(i+1));
    const u32=pos=>hex.slice(pos,pos+4).reduce((a,v)=>a*256+v,0);
    const dimensions=[u32(16),u32(20)];equal(dimensions,[869,1228],"renders","bounded IHDR dimensions "+(i+1));
    renderRows.push({...expected,dimensions,visual_review:false,png_full_decode:false});
  }
  const labels=[...passes,"pdfinfo","pdffonts","pdftotext",...Array.from({length:5},(_,i)=>"render_"+String(i+1).padStart(4,"0"))];
  const native=[];
  for(const label of labels){
    const p="commands/"+label+"/",attempt=obj(p+"ATTEMPT.json"),receipt=obj(p+"RECEIPT.json"),spawn=obj(p+"SPAWNED.json"),before=obj(p+"INPUTS_BEFORE.json"),after=obj(p+"INPUTS_AFTER.json");
    equal(Object.fromEntries(Object.keys(attempt).map(k=>[k,receipt[k]])),attempt,"native","complete attempt projected from receipt "+label);
    equal(before,after,"native","direct input before/after "+label);
    equal(receipt,result.native_commands.find(r=>r.label===label),"native","complete RESULT native receipt "+label);
    check(receipt.native_exit_code===0&&receipt.successful===true&&receipt.streams_settled===true&&receipt.error===null&&receipt.native_handle_received===true&&receipt.wrapper_reason==="NATIVE_EXIT"&&receipt.direct_inputs_equal===true,"native","successful settled native outcome "+label);
    equal(receipt.owned_session_interventions,[],"native","no interventions "+label);equal(receipt.remaining_session_members,[],"native","no remaining session "+label);equal(receipt.session_members_at_settlement,[],"native","no settlement members "+label);
    check(spawn.pid===spawn.session&&Number.isInteger(spawn.pid)&&spawn.pid>0&&attempt.attempted_epoch<=spawn.spawned_epoch&&spawn.spawned_epoch<=receipt.ended_epoch,"native","recorded identity/time "+label);
    for(const name of ["stdout.raw","stderr.raw"])equal(receipt.streams[name],pin(p+name),"native","complete native stream pin "+label+"/"+name);
    check(body(p+"stderr.raw")==="","native","empty actual stderr "+label);
    for(const name of sourceNames)if(Object.hasOwn(before,cold+"/"+name))equal(before[cold+"/"+name],{path:cold+"/"+name,present:true,symlink:false,resolved:cold+"/"+name,kind:"file",...initial[name]},"native","copied source direct role "+label+"/"+name);
    if(label==="bibtex"){
      equal(before[cold+"/main.aux"],{path:cold+"/main.aux",present:true,symlink:false,resolved:cold+"/main.aux",kind:"file",...pin("pass_artifacts_bibtex/before/main.aux")},"native","BibTeX actual same-stage aux bytes, not final aux");
      const style=summaries.bibtex.style.path;equal(before[style],config[style],"native","BibTeX direct style agrees archived prelock");
    }
    if(!passes.includes(label))equal(before[cold+"/main.pdf"],{path:cold+"/main.pdf",present:true,symlink:false,resolved:cold+"/main.pdf",kind:"file",...measured.pdf},"native","measured same final PDF "+label);
    native.push({label,pid:spawn.pid,attempted:attempt.attempted_epoch,ended:receipt.ended_epoch,direct_inputs:Object.keys(before).length,stdout:pin(p+"stdout.raw"),stderr:pin(p+"stderr.raw")});
  }
  for(let i=1;i<native.length;i++)check(native[i-1].ended<=native[i].attempted,"native","ordered recorded selected commands "+native[i].label);
  const firstHead=headers.find(r=>r.path===base+"source_only/main.pdf").result.output.trim().split(/\s+/).map(h=>parseInt(h,16));
  equal(firstHead.slice(0,8),[37,80,68,70,45,49,46,53],"measurement","actual PDF-1.5 signature");
  return {status:failures.length?"RECONSTRUCTION_DISCREPANCIES":"ORDERED_IO_RECONSTRUCTION_MATCH_WITH_DIAGNOSTIC_CENSUS_FINDING",failures,checks:checks.length,check_groups:groups,checks_detail:checks,reconstructed_roles:recon,pass_summaries:summaries,diagnostics,metadata,font_rows:fonts,render_rows:renderRows,native_rows:native,source_only_initial:initial,total_fls_events:fullFLS.length,limitations:["External resolved paths and bytes are compared only as saved configuration data; no current host lookup or reopen.", "FLS is declared ordered I/O, not OS-level exhaustive read tracing.", "Same-pass output-then-input bytes are not observed; beginning/end pins do not fill that gap.", "Intermediate PDF bytes were not archived; only their recorded pins and native/log byte counts are available.", "BibTeX has no new FLS; aux/style/database plus saved direct/configuration evidence is bounded, not an OS trace.", "PNG header, hash, dimensions, native receipt and font metadata are measurements, not viewing or glyph correctness.", "This lane is not manuscript review, two-build comparison, runtime/settings authority, or terminal acceptance."],diagnostic_finding:{id:"P211-COLD2-DIAGNOSTIC-CENSUS",severity:"Minor",status:"OPEN_PENDING_ROOT_DIAGNOSTIC_DISPOSITION",scope:"Saved diagnostic summary coverage, not proven PDF corruption",actual:diagnostics.pass3.uncaptured_warning_emissions,recorded_warning_array:measured.diagnostics.warnings,mechanism:"Case-sensitive /Warning/ misses lowercase pdfTeX warning. The old initial auditor repeats the same case-sensitive mechanism.",required:"Keep original artifacts unchanged; incorporate the actual warning into a new exact diagnostic supplement/root disposition and do not describe this final log as warning-free. Actual all-page view remains a separate gate."}};
}
