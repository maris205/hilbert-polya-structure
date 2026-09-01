#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"

ROOT = File.expand_path("..", __dir__)

PAPERS = {
  "P29" => "papers/29-bianchi-ideal-owner-refinement",
  "P30" => "papers/30-three-disk-nonconstant-roof-determinant",
  "P31" => "papers/31-level11-conjugacy-owner-ledger",
  "P32" => "papers/32-homology-cover-renormalization-uniformity",
  "P33" => "papers/33-bolza-control-matched-census"
}.freeze

NOTE_FILES = %w[
  stage1_phase1_rq_brief.md
  stage1_phase1_methodology_blueprint.md
  stage1_phase1_devils_advocate.md
  stage1_phase1_resolution.md
  stage1_phase1_devils_advocate_recheck.md
  stage1_phase1_checkpoint.md
].freeze

SPECIAL_MARKERS = {
  "P29" => ["S_H(M)", "QUOTIENT_NOT_EVALUABLE", "SPECIFICITY_NOT_ESTABLISHED"],
  "P30" => ["roof-agnostic", "pointwise", "A2_NOT_ELIGIBLE", "TYPED_PHYSICAL_DETERMINANT_INFRASTRUCTURE"],
  "P31" => ["G(owner_id", "I(owner_id", "M(h,d)", "9,453", "NOT_EVALUABLE_CONJUGACY_INCOMPLETE"],
  "P32" => ["K(delta,T,R)", "SG2OwnerCanonical-v1", "R_+", "k>=1", "k<=8", "Hahn"],
  "P33" => ["A0_INCONCLUSIVE_SYSTOLE_CONFOUNDED", "A0_CONTROL_PANEL_INCOMPLETE", "BOTH_CENSUSES_CLOSED_UNDER_COMMON_CONTRACT"]
}.freeze

UPSTREAM_HASHES = {
  "papers/26-level11-newform-time-change/results/round4_hecke_cycle_ledger.csv" => "f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662",
  "papers/26-level11-newform-time-change/results/round6_quadratic_degree_moment_ledger.csv" => "f95e1435c9293f8e008cebf80084ea2b522b76186dbd684b5e3997c5e588edea",
  "papers/26-level11-newform-time-change/results/round8_exact_instance_taxonomy_ledger.csv" => "beb363e4080b794e33ec6bc729b1f3e4dd7ef322be63fc59755e18fdf6bc889f",
  "papers/26-level11-newform-time-change/results/round8_exact_group_moment_taxonomy_ledger.csv" => "532e799686dd8afefa3a7529717208305fedede3f3e74e14ccf761ab35d74f69",
  "papers/26-level11-newform-time-change/results/round8_summary.json" => "4ba5de801dfd06c8b03bfe5fc07297b8c4e074bcf26c70ec6566de401ae2384d",
  "papers/27-congruence-inverse-limit-no-go/results/round5_cocompact_homology_escape_ledger.csv" => "0c74333b63f6027b16d134f19a320b8148e7fab6f86fa204d213c801106fe825",
  "papers/27-congruence-inverse-limit-no-go/results/round5_cocompact_homology_escape_validation.json" => "afdc51ca7ecfbd8777955c7438f08d4580e6b924419a807191e097b0292d9c10",
  "papers/27-congruence-inverse-limit-no-go/results/round8_renormalization_quadrants.csv" => "879ce8aec4e041e7cbba947706319511d99bb72592421584e76bbe47fad5ae57",
  "papers/27-congruence-inverse-limit-no-go/results/round8_renormalization_prefix_coefficients.csv" => "63f9632a0a715be26545e645a0f1d238e3ff24baec70fd8f478f1eda6c12c132",
  "papers/27-congruence-inverse-limit-no-go/results/round8_homology_renormalization_summary.json" => "c482c0e48fb1036faed37f123fbdec0b1c54f757a75f35e8a24cee27cb242b1a",
  "papers/28-bolza-magnetic-flow/notes/round3_trace_regime_contract.md" => "6fec628b7ec910296a81038d1f66a140b97c16113c29dce261b8e7b22d2ee5e0",
  "papers/28-bolza-magnetic-flow/results/round4_bolza_group_certificate.json" => "e3e6c486c66116dc6fe9fdd054c2fce9d4b1a58318f56d1656f6db168c807eca",
  "papers/28-bolza-magnetic-flow/results/round6_bolza_conjugacy_validation.json" => "ce8c751035b0f367c0f74594f93b0e5ed0bbec140897c8458cf5c9e11b9c8269",
  "papers/28-bolza-magnetic-flow/notes/round7_nonarithmetic_source_package_freeze.md" => "efdbeca3611b92863e1e8b8b1769a7d18c2ac4d839001275afb5b8db09c9255a",
  "papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json" => "a900749b6905a5f324c2e2670363ec1bc9480481f3f5aa1240ed0ebbee55e6ca",
  "papers/28-bolza-magnetic-flow/notes/round8_control_systole_completeness_freeze.md" => "b2655431dcc27c471e8da3c092435dbe30c6a483e2244f78543adcd2a3141528",
  "papers/28-bolza-magnetic-flow/results/round8_control_finite_ball_certificate.json" => "c1bf68a8a1485665680dba01d0012fb691c7ca1a795e36334639e34bbbdbcb1f",
  "papers/28-bolza-magnetic-flow/results/round8_control_systole_validation.json" => "4bf132b0d53e2cec329b26d0963f0e0f721c4c98fd4c58873b781bb5053e00c4"
}.freeze

@checks = 0
@failures = []

def check(label, condition)
  @checks += 1
  @failures << label unless condition
end

def path(relative)
  File.join(ROOT, relative)
end

def read(relative)
  File.binread(path(relative)).force_encoding(Encoding::UTF_8)
end

def section(text, heading)
  match = text.match(/^## #{Regexp.escape(heading)}\s*$\n(.*?)(?=^## |\z)/m)
  match && match[1]
end

authorization = "BATCH_ROUND10_STAGE1_BUDGET_AUTHORIZATION_20260901.txt"
check("authorization file exists", File.file?(path(authorization)))
if File.file?(path(authorization))
  check("authorization bytes are exact", read(authorization).bytes == "确认\n".bytes)
  check(
    "authorization SHA-256 is exact",
    Digest::SHA256.file(path(authorization)).hexdigest == "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe"
  )
end

check("batch start receipt exists", File.file?(path("BATCH_ROUND10_STAGE1_PHASE1_START.md")))
check("batch checkpoint exists", File.file?(path("BATCH_ROUND10_STAGE1_PHASE1_CHECKPOINT.md")))

PAPERS.each do |paper, directory|
  notes = File.join(directory, "notes")
  NOTE_FILES.each do |filename|
    check("#{paper} #{filename} exists", File.file?(path(File.join(notes, filename))))
  end

  next unless NOTE_FILES.all? { |filename| File.file?(path(File.join(notes, filename))) }

  rq = read(File.join(notes, "stage1_phase1_rq_brief.md"))
  method = read(File.join(notes, "stage1_phase1_methodology_blueprint.md"))
  da = read(File.join(notes, "stage1_phase1_devils_advocate.md"))
  resolution = read(File.join(notes, "stage1_phase1_resolution.md"))
  recheck = read(File.join(notes, "stage1_phase1_devils_advocate_recheck.md"))
  checkpoint = read(File.join(notes, "stage1_phase1_checkpoint.md"))

  primary = section(rq, "Primary research question")
  check("#{paper} has primary RQ section", !primary.nil?)
  if primary
    question_lines = primary.lines.select { |line| line.include?("?") }
    check("#{paper} has exactly one primary question", primary.count("?") == 1 && question_lines.length == 1)
  end

  %w[Feasible Interesting Novel Ethical Relevant].each do |criterion|
    check("#{paper} FINER #{criterion}", rq.include?("| #{criterion} |"))
  end
  check("#{paper} novelty is provisional", rq.include?("PROVISIONAL"))

  subquestions = section(rq, "Sub-questions")
  check("#{paper} has exactly three subquestions", subquestions && subquestions.scan(/^\d+\. /).length == 3)
  candidates = section(rq, "Candidate questions considered")
  check("#{paper} has at least three candidate questions", candidates && candidates.scan(/^\|\s*\d+\s*\|/).length >= 3)

  check("#{paper} method section research paradigm", method.match?(/^## .*Paradigm/i))
  check("#{paper} method section method", method.match?(/^## .*Method/i))
  check("#{paper} method section data strategy", method.match?(/^## (?:Data strategy|Data and target firewall)/i))
  check("#{paper} method section limitations", method.match?(/^## .*Limitations/i))
  check("#{paper} method has kill gates", method.match?(/^## .*Kill gates|^## .*fail-closed stopping rules/i))
  check("#{paper} method has human-subjects boundary", method.match?(/human[- ]subjects|human participants/i))
  check("#{paper} method has discipline reporting", method.match?(/Reporting standard|Discipline reporting|discipline standard/i))
  check("#{paper} preregistration declaration", method.include?("not_provided") && method.match?(/companion handle:\s*\*?\*?`?none/i))
  check("#{paper} dispatcher-only declaration", method.match?(/dispatcher[- ]only|dispatcher only/i))
  route_text = (rq + method).gsub(/\s+/, " ")
  check(
    "#{paper} Route B remains closed",
    route_text.include?("Route B") && route_text.match?(/closed|excluded|unauthorized|NOT_RUN|NO_ROUTE_PROMOTION/i)
  )

  SPECIAL_MARKERS.fetch(paper).each do |marker|
    check("#{paper} special marker #{marker}", (rq + method + resolution).include?(marker))
  end

  check("#{paper} initial DA is REVISE", da.match?(/(?:Verdict|verdict).*REVISE/i))
  check("#{paper} resolution records closure", resolution.match?(/Resolved|resolved|关闭|closed/))
  check("#{paper} independent recheck is PASS", recheck.match?(/(?:Verdict|verdict).*PASS/i))
  check("#{paper} checkpoint is complete", checkpoint.include?("PHASE_1_COMPLETE"))
  check("#{paper} checkpoint awaits confirmation", checkpoint.match?(/awaiting.*confirmation|AWAITING_CONFIRMATION/i))

  ["stage1_phase1_rq_brief.md", "stage1_phase1_methodology_blueprint.md",
   "stage1_phase1_devils_advocate.md", "stage1_phase1_resolution.md",
   "stage1_phase1_devils_advocate_recheck.md"].each do |filename|
    digest = Digest::SHA256.file(path(File.join(notes, filename))).hexdigest
    check("#{paper} checkpoint binds #{filename}", checkpoint.include?(digest))
  end

  state = read(File.join(notes, "pipeline_state.md"))
  project_readme = read(File.join(directory, "README.md"))
  check("#{paper} state awaits Phase-2 confirmation", state.include?("AWAITING_PHASE_2_CONFIRMATION"))
  check("#{paper} literature remains not run", state.match?(/Literature.*NOT_RUN/i))
  check("#{paper} computation remains not run", state.match?(/computation.*NOT_RUN/i))
  check("#{paper} project README records Phase-1 completion", project_readme.match?(/Phase 1.*complete|Phase-1.*complete/i))

  forbidden = Dir.glob(path(File.join(notes, "*"))).select do |candidate|
    File.file?(candidate) && File.basename(candidate).match?(/phase2|bibliograph|synthesis/i)
  end
  check("#{paper} has no Phase-2/bibliography/synthesis artifact", forbidden.empty?)
end

UPSTREAM_HASHES.each do |relative, expected|
  check("upstream file exists: #{relative}", File.file?(path(relative)))
  next unless File.file?(path(relative))

  check("upstream hash: #{relative}", Digest::SHA256.file(path(relative)).hexdigest == expected)
end

root_readme = read("README.md")
registry = read("docs/candidate_registry.md")
batch_checkpoint = File.file?(path("BATCH_ROUND10_STAGE1_PHASE1_CHECKPOINT.md")) ? read("BATCH_ROUND10_STAGE1_PHASE1_CHECKPOINT.md") : ""

check("root README references Phase-1 checkpoint", root_readme.include?("BATCH_ROUND10_STAGE1_PHASE1_CHECKPOINT.md"))
check("root README records five Phase-1 outputs", root_readme.include?("RQ_BRIEFS=5/5") && root_readme.include?("DA_RECHECK_PASS=5/5"))
check("candidate registry references Phase-1 checkpoint", registry.include?("BATCH_ROUND10_STAGE1_PHASE1_CHECKPOINT.md"))
check("batch checkpoint records 0/20 round trips", batch_checkpoint.include?("ACCUMULATED_DOCUMENT_ROUND_TRIPS=0/20"))
check("batch checkpoint keeps literature stopped", batch_checkpoint.include?("LITERATURE_INVESTIGATION=NOT_STARTED"))
check("batch checkpoint keeps computation stopped", batch_checkpoint.include?("SCIENTIFIC_COMPUTATION=NOT_STARTED"))
check("batch checkpoint keeps Route B at zero", batch_checkpoint.include?("ROUTE_B_INVOCATIONS=0/5"))

if @failures.empty?
  puts "ROUND10_STAGE1_PHASE1_AUDIT=PASS checks=#{@checks} failures=0"
  exit 0
end

warn "ROUND10_STAGE1_PHASE1_AUDIT=FAIL checks=#{@checks} failures=#{@failures.length}"
@failures.each { |failure| warn "- #{failure}" }
exit 1
