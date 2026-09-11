'use strict';
// AUTHOR SOURCE_ONLY finite command-plan emitter; never a host-query executor.
// Only writes prospective JSON to stdout. No imports, reads, children or eval.
// The separately inspected future capture source is intentionally not supplied.
const environment = {"PATH":"/usr/bin:/bin","LANG":"C.UTF-8","LC_ALL":"C.UTF-8","TZ":"UTC","SOURCE_DATE_EPOCH":"1788825600","FORCE_SOURCE_DATE":"1","openin_any":"p","openout_any":"p"};
const cwd = "/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_build_dependency_query01/query_cwd";
const profile = {
  "source_graph_path": "docs/papers211_215_sequence/qa/p212_initial_build_preparation01/SOURCE_GRAPH.json",
  "paper_root": "papers/212-closed-pointer-orbits",
  "source_pins": {
    "main.tex": {
      "bytes": 1463,
      "sha256": "da04d4ca19ed94ce2fae1d181f238b0e1ae944ca09a714a30c6bb0e11f375d8a"
    },
    "math_commands.tex": {
      "bytes": 243,
      "sha256": "3ebb1fd506f17810d19531cee9333b52617ee5a5f9231df6307936e0a392f938"
    },
    "references.bib": {
      "bytes": 1927,
      "sha256": "9ad7c6bebc1aeef3a9d0e3f0703e876f2e1a634c5bf2d7f46297cfa7d5d1cf38"
    },
    "sections/01_setup.tex": {
      "bytes": 4249,
      "sha256": "44ca562e26d6e8c6c5d92f33245e0a26f1a2cbbd2d5caf204352437d343cc04b"
    },
    "sections/02_returns.tex": {
      "bytes": 4937,
      "sha256": "7185cd89b09569bc2977e71a5a74ea6c65b5a734a18905e8b11a592985be9002"
    },
    "sections/03_period_set.tex": {
      "bytes": 1537,
      "sha256": "45f2e69dbe9d9f4418a439c407fd77309513fb515b12b38ab64bb421f12df490"
    },
    "sections/04_census.tex": {
      "bytes": 4499,
      "sha256": "4f4e2db96c6f2fd9734f0ed29d1dedc759daef2d87e02d68890deb5f0cf4b353"
    },
    "sections/05_scope.tex": {
      "bytes": 804,
      "sha256": "6f0d84102903eb21dffb52095b9b78f257550a4c6d2ec22c8add6a3a4cdd3a1c"
    }
  },
  "source_files": 8,
  "source_bytes": 19659,
  "document_class": {
    "name": "article",
    "options": [
      "10pt"
    ]
  },
  "packages": [
    {
      "name": "geometry",
      "options": [
        "margin=0.85in"
      ]
    },
    {
      "name": "amsmath",
      "options": []
    },
    {
      "name": "amssymb",
      "options": []
    },
    {
      "name": "amsthm",
      "options": []
    },
    {
      "name": "booktabs",
      "options": []
    },
    {
      "name": "array",
      "options": []
    },
    {
      "name": "fontenc",
      "options": [
        "T1"
      ]
    },
    {
      "name": "hyperref",
      "options": [
        "hidelinks"
      ]
    }
  ],
  "main_inputs": [
    "math_commands",
    "sections/01_setup",
    "sections/02_returns",
    "sections/03_period_set",
    "sections/04_census",
    "sections/05_scope"
  ],
  "bibliography_style": "plain",
  "bibliography": [
    "references"
  ],
  "external_figures": []
};
const seeds = [
  {"label":"class_article","name":"article.cls","program":"pdflatex","engine":"pdftex","role":"class source","basis":"main.tex exact documentclass[10pt]{article}","required":true},
  {"label":"package_01_geometry","name":"geometry.sty","program":"pdflatex","engine":"pdftex","role":"ordered direct package source","basis":"main.tex package 1 options=[\"margin=0.85in\"]","required":true},
  {"label":"package_02_amsmath","name":"amsmath.sty","program":"pdflatex","engine":"pdftex","role":"ordered direct package source","basis":"main.tex package 2 options=[]","required":true},
  {"label":"package_03_amssymb","name":"amssymb.sty","program":"pdflatex","engine":"pdftex","role":"ordered direct package source","basis":"main.tex package 3 options=[]","required":true},
  {"label":"package_04_amsthm","name":"amsthm.sty","program":"pdflatex","engine":"pdftex","role":"ordered direct package source","basis":"main.tex package 4 options=[]","required":true},
  {"label":"package_05_booktabs","name":"booktabs.sty","program":"pdflatex","engine":"pdftex","role":"ordered direct package source","basis":"main.tex package 5 options=[]","required":true},
  {"label":"package_06_array","name":"array.sty","program":"pdflatex","engine":"pdftex","role":"ordered direct package source","basis":"main.tex package 6 options=[]","required":true},
  {"label":"package_07_fontenc","name":"fontenc.sty","program":"pdflatex","engine":"pdftex","role":"ordered direct package source","basis":"main.tex package 7 options=[\"T1\"]","required":true},
  {"label":"package_08_hyperref","name":"hyperref.sty","program":"pdflatex","engine":"pdftex","role":"ordered direct package source","basis":"main.tex package 8 options=[\"hidelinks\"]","required":true},
  {"label":"style_plain","name":"plain.bst","program":"bibtex","engine":"pdftex","role":"BibTeX style source","basis":"main.tex exact bibliographystyle{plain}; use BibTeX program search context","required":true},
  {"label":"config_pdflatex_texmf","name":"texmf.cnf","program":"pdflatex","engine":"pdftex","role":"TeX search configuration candidate","basis":"inherited query mechanism only; current whole body/search precedence remains to be received","required":false},
  {"label":"config_bibtex_texmf","name":"texmf.cnf","program":"bibtex","engine":"pdftex","role":"BibTeX search configuration candidate","basis":"separate effective BibTeX program context","required":false},
  {"label":"format_pdflatex","name":"pdflatex.fmt","program":"pdflatex","engine":"pdftex","role":"opaque compiled-format dependency","basis":"proposed pdflatex build; program/engine-specific lookup required by preserved old discovery failure","required":true},
  {"label":"source_pdftexconfig","name":"pdftexconfig.tex","program":"pdflatex","engine":"pdftex","role":"format/configuration source candidate","basis":"old explicit configuration seed, not assumed active or sufficient for new format","required":false},
  {"label":"source_latex_kernel","name":"latex.ltx","program":"pdflatex","engine":"pdftex","role":"candidate kernel/NFSS source for manual semantics","basis":"candidate explanatory body; equality to the dumped-format kernel is NOT established by current file presence","required":false},
  {"label":"map_pdftex","name":"pdftex.map","program":"pdflatex","engine":"pdftex","role":"candidate map source","basis":"old explicit map seed; actual map names/order must follow received configuration/source","required":false},
  {"label":"config_fmtutil","name":"fmtutil.cnf","program":"pdflatex","engine":"pdftex","role":"format-construction configuration candidate","basis":"historical explicit seed only; not permission to regenerate a format","required":false},
  {"label":"config_updmap","name":"updmap.cfg","program":"pdflatex","engine":"pdftex","role":"font-map construction configuration candidate","basis":"historical explicit seed only; not permission to regenerate maps","required":false},
  {"label":"config_texfonts","name":"texfonts.map","program":"pdflatex","engine":"pdftex","role":"font-alias configuration candidate","basis":"historical explicit seed only; actual use awaits source semantics","required":false}
];
const variables = ["TEXMF","TEXMFCNF","TEXMFHOME","TEXMFCONFIG","TEXMFVAR","TEXMFDBS","TEXINPUTS","BIBINPUTS","BSTINPUTS","shell_escape","openin_any","openout_any"];
const generation = {
  "status": "NOT_ESTABLISHED_UNTIL_INSTALLED_HELP_AND_RUNTIME_SOURCE_RECEIVED",
  "requested_no_generation_flags": [
    "--no-mktex=tex",
    "--no-mktex=fmt",
    "--no-mktex=tfm",
    "--no-mktex=pk"
  ],
  "policy": "These literal proposed flags are a source-review requirement, not a claim of installed support or sufficient disabling. If help/configuration exposes another generator or a different option contract, preserve outputs, stop and receive a separate exact source amendment before any lookup. No filename lookup runs merely because this emitter prints it."
};
const commands = [
  {label:'contract_help',phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--help'],expected_exit_codes:[0],result:null},
  {label:'contract_version',phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--version'],expected_exit_codes:[0],result:null}
];
const later = 'LOOKUP_ONLY_AFTER_SEPARATE_OPTION_AND_RUNTIME_SOURCE_ACCEPTANCE';
for (const seed of seeds) for (const mode of ['default','all']) commands.push({
  label:seed.label+'_'+mode, phase:later,
  argv:['/usr/bin/kpsewhich','--progname='+seed.program,'--engine='+seed.engine,
        ...generation.requested_no_generation_flags,...(mode==='all'?['--all']:[]),seed.name],
  expected_exit_codes:[0,1],result:null
});
for (const name of variables) commands.push({
  label:'var_'+name,phase:later,
  argv:['/usr/bin/kpsewhich','--progname='+(['BIBINPUTS','BSTINPUTS'].includes(name)?'bibtex':'pdflatex'),
        '--engine=pdftex',...generation.requested_no_generation_flags,'-var-value='+name],
  expected_exit_codes:[0,1],result:null
});
commands.push({label:'expanded_TEXMF',phase:later,
  argv:['/usr/bin/kpsewhich','--progname=pdflatex','--engine=pdftex',
        ...generation.requested_no_generation_flags,'-expand-path=$TEXMF'],
  expected_exit_codes:[0,1],result:null
});
const frontier = {
  schema:'p212-build-finite-query-frontier-source-v1',
  status:'SOURCE_ONLY_PLAN_NOT_A_QUERY_EXECUTOR_OR_DEPENDENCY_LOCK',approved:false,
  environment,command_cwd_proposal:cwd,command_cwd_observation:null,profile,
  initial_name_seeds:seeds,generation_policy:generation,ordered_command_proposals:commands,
  native_commands_executed:0,host_dependency_bodies_received:0,actual_resolutions:null,
  actual_source_edges:null,actual_class_configuration_semantics:null,actual_font_selector:null,
  actual_format_provenance:null,actual_runtime_tool_linkage_key:null,
  actual_effective_build_cwd_configuration:null,dependency_lock:null,root_authority:null,
  continuation:"Stop after receiving this finite frontier and all returned dependency bodies; a separately inspected source-derived edge table and any next finite query source are required. No automatic recursive discovery, build-driven lock enlargement, guessed article.cfg, lmodern regex, metric list or inherited840 rows."
};
process.stdout.write(JSON.stringify(frontier,null,2)+'\n');
