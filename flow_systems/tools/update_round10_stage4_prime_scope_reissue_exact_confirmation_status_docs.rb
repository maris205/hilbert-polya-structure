#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "optparse"
require "pathname"
require "securerandom"
require "tempfile"
require "tmpdir"

module Round10ExactConfirmationStatusDocs
  class ContractError < StandardError; end

  DEFAULT_ROOT = Pathname.new(__dir__).parent.expand_path.freeze
  EXACT_PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
  FINAL_MANIFEST = "#{EXACT_PREFIX}_FINAL_EMISSION_MANIFEST.json"
  PLANNED_COMPLETION_REPORT = "#{EXACT_PREFIX}_COMPLETION_REPORT.md"
  FINAL_MANIFEST_SCHEMA =
    "round10-stage4-prime-scope-reissue-exact-confirmation-final-emission-manifest/1.0"
  FINAL_MANIFEST_STATUS =
    "PASS_EXACT_CONFIRMATION_FINAL_EMISSION_READY_FOR_DETERMINISTIC_APPLY"
  FINAL_MANIFEST_SHA256 =
    "db98aa8ace700196044b7bb1903251a90782e709d65f6c0712da041c36421091"
  PREPARATION_ROLE =
    "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY"

  OLD_ROOT_MARKER = "<!-- ROUND10_STAGE4_PRIME_SCOPE_REISSUE_STATUS_20260904 -->"
  NEW_MARKER = "<!-- ROUND10_STAGE4_PRIME_EXACT_CONFIRMATION_EXECUTION_STATUS_20260904 -->"
  ROOT_HISTORY_BOUNDARY =
    "### 历史：Stage 4′ execution / Stage 4.5 / Round-5 checkpoint（已被上文取代）"
  PIPELINE_HISTORY_BOUNDARY = "## Historical previous-checkpoint state"
  CONTROL_STATE =
    "stage4_prime_exact_confirmation_correction_complete_awaiting_separately_authorized_fresh_stage4_5"

  AUTHORITY = {
    "author_event" => {
      path: "#{EXACT_PREFIX}_AUTHOR_EVENT_20260904.txt",
      sha256: "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe"
    },
    "authorization_record" => {
      path: "#{EXACT_PREFIX}_AUTHORIZATION_RECORD.md",
      sha256: "98755a5998aeee16034db32c89d997b3349a1b77b0c41a93ab32ac994a8d8f79"
    },
    "input_freeze" => {
      path: "#{EXACT_PREFIX}_INPUT_FREEZE.json",
      sha256: "7a140287ce95ad6304cc52e7568d66780d77f54d7aaba461515cb087886075e1"
    },
    "authorization_receipt" => {
      path: "#{EXACT_PREFIX}_AUTHORIZATION_RECEIPT.json",
      sha256: "a21655745ea33c565626c5cc980b8f91a82f4b87ce2d74cfcb012f0c5d7bae21"
    },
    "authority_audit" => {
      path: "#{EXACT_PREFIX}_AUTHORITY_AUDIT.json",
      sha256: "813a600253cdeac98003a69beb7f28dbf35080cfdfe7bb974d1d8c9a323857b2"
    }
  }.freeze

  RECEIPT_STATUS =
    "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION"
  FREEZE_STATUS = "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION"
  AUTHORITY_AUDIT_STATUS =
    "PASS_EXACT_CONFIRMATION_AUTHORITY_FROZEN_READY_FOR_DETERMINISTIC_APPLY"

  PAPER_CONFIGS = {
    "P29" => {
      number: 29,
      title: "Bianchi ideal-owner refinement",
      slug: "29-bianchi-ideal-owner-refinement",
      revision_round: 3,
      expected_ops: 31,
      base: "stage4_prime_revision_round2.tex",
      successor: "stage4_prime_revision_round3.tex",
      patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
      build_receipt: "stage4_prime_revision_round3_build_receipt.json",
      bundle: "stage4_prime_revision_evidence_bundle_round3.json",
      pdf: "stage4_prime_revision_round3.pdf",
      build_log: "stage4_prime_revision_round3.build.log",
      build_transcript: "stage4_prime_preview_build_transcript_round3.log",
      bibliography: "notes/stage4_prime_references_round2.bib",
      first_history: "### Historical Stage-4.5 audit checkpoint (superseded)",
      conclusion: "31 个精确来源／现态修复已落入新的版本化稿件；引文用途、bounded-unavailability、owner/primitive 术语及 provenance 表述被收窄到证据实际支持的范围，但没有建立完整 owner law、quotient、certificate 或 Route 结论。",
      system: "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal",
      route: "A0/A1 preparation only; formal Route-A tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B not invoked"
    },
    "P30" => {
      number: 30,
      title: "three-disk physical-roof determinant",
      slug: "30-three-disk-nonconstant-roof-determinant",
      revision_round: 3,
      expected_ops: 34,
      base: "stage4_prime_revision_round2.tex",
      successor: "stage4_prime_revision_round3.tex",
      patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
      build_receipt: "stage4_prime_revision_round3_build_receipt.json",
      bundle: "stage4_prime_revision_evidence_bundle_round3.json",
      pdf: "stage4_prime_revision_round3.pdf",
      build_log: "stage4_prime_revision_round3.build.log",
      build_transcript: "stage4_prime_preview_build_transcript_round3.log",
      bibliography: "notes/stage4_prime_references_round2.bib",
      matrix: "notes/stage4_prime_claim_passage_matrix_round2.json",
      matrix_receipt: "notes/stage4_prime_correction_round3_matrix_regeneration_receipt.json",
      matrix_kind: "claim-passage",
      matrix_counts: {
        "bounded_substantive_locator_rows" => 18,
        "explicit_bounded_unavailability_rows" => 8,
        "preexisting_narrow_record_or_method_locator_rows" => 2,
        "inconclusive_unadjudicated_rows" => 0,
        "row_count" => 28
      },
      first_history: "### Historical Stage-4.5 audit checkpoint (superseded)",
      conclusion: "34 个 source-scoped 修复已落入新的版本化稿件，并把物理 roof 文献支持与明确不可用状态逐项对齐；这闭合的是来源、披露与现态一致性，不是 roof、算子、determinant、误差界或数值结果。",
      system: "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control",
      route: "A0_FAIL / A2_NOT_ELIGIBLE; formal Route-A tuple UNASSIGNED; A3=0; A4=0; Route B not invoked"
    },
    "P31" => {
      number: 31,
      title: "level-11 conjugacy owner ledger",
      slug: "31-level11-conjugacy-owner-ledger",
      revision_round: 3,
      expected_ops: 13,
      base: "stage4_prime_revision_round2.tex",
      successor: "stage4_prime_revision_round3.tex",
      patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
      build_receipt: "stage4_prime_revision_round3_build_receipt.json",
      bundle: "stage4_prime_revision_evidence_bundle_round3.json",
      pdf: "stage4_prime_revision_round3.pdf",
      build_log: "stage4_prime_revision_round3.build.log",
      build_transcript: "stage4_prime_preview_build_transcript_round3.log",
      bibliography: "notes/stage4_prime_references_round2.bib",
      matrix: "notes/stage4_prime_method_passage_matrix_round2.json",
      matrix_receipt: "notes/stage4_prime_correction_round3_matrix_regeneration_receipt.json",
      matrix_kind: "method-passage",
      matrix_counts: {
        "bounded_substantive_locator_rows" => 7,
        "explicit_bounded_unavailability_rows" => 15,
        "preexisting_narrow_record_or_method_locator_rows" => 2,
        "inconclusive_unadjudicated_rows" => 0,
        "row_count" => 24
      },
      first_history: "### Historical Stage-4.5 audit checkpoint (superseded)",
      conclusion: "13 个精确修复已使 owner-ledger 稿件的来源可用性、方法边界、披露与现态表述一致；完整 owner ledger、inverse theorem、executable verifier 与全对执行仍未被声称。",
      system: "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers repetitions; Hecke degree distinct",
      route: "A1-only preparation; formal Route-A tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B not invoked"
    },
    "P32" => {
      number: 32,
      title: "homology-cover renormalization uniformity",
      slug: "32-homology-cover-renormalization-uniformity",
      revision_round: 3,
      expected_ops: 15,
      base: "stage4_prime_revision_round2.tex",
      successor: "stage4_prime_revision_round3.tex",
      patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
      build_receipt: "stage4_prime_revision_round3_build_receipt.json",
      bundle: "stage4_prime_revision_evidence_bundle_round3.json",
      pdf: "stage4_prime_revision_round3.pdf",
      build_log: "stage4_prime_revision_round3.build.log",
      build_transcript: "stage4_prime_preview_build_transcript_round3.log",
      bibliography: "notes/stage4_prime_references_round2.bib",
      first_history: "### Historical Stage-4.5 audit checkpoint (superseded)",
      conclusion: "15 个来源与现态修复已写入新的版本化稿件，按单一来源逐句限定 passage support，并纠正 matrix／artifact 语义；factor、global product、limit interchange、obstruction 与 Route credit 仍未被证明或执行。",
      system: "unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3",
      route: "generic A1--A2 preparation with arithmetic A0 unavailable; formal Route-A tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B not invoked"
    },
    "P33" => {
      number: 33,
      title: "Bolza/control certificate census",
      slug: "33-bolza-control-matched-census",
      revision_round: 2,
      expected_ops: 37,
      base: "stage4_revision_round1.tex",
      successor: "stage4_prime_revision_round2.tex",
      patch: "stage4_prime_revision_patch_round6_exact_confirmation.json",
      build_receipt: "stage4_prime_revision_round2_build_receipt.json",
      bundle: "stage4_prime_revision_evidence_bundle_round2.json",
      pdf: "stage4_prime_revision_round2.pdf",
      build_log: "stage4_prime_revision_round2.build.log",
      build_transcript: "stage4_prime_preview_build_transcript_round2.log",
      bibliography: "paper/references.bib",
      bibliography_receipt: "notes/stage4_prime_round6_bibliography_append_receipt.json",
      bibliography_plan: "notes/stage4_prime_round6_bibliography_append_plan.json",
      bibliography_prospective: "notes/stage4_prime_round5_correction_bibliography_prospective.json",
      first_history: "### Historical Round-5 review checkpoint (superseded)",
      conclusion: "37 个精确修复已把 43-row replay、48-use bounded unavailability、synthetic-only conformance 与生产非执行边界写入版本化稿件；恰好两条 correction Bib 记录完成五处 dual binding，但没有 producer、owner census 或科学验证结果。",
      system: "unit-speed Bolza geodesic flow with a separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning rule",
      route: "A1 preparation with formal A0 prohibited/confounded; formal Route-A tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B not invoked"
    }
  }.freeze

  class Updater
    attr_reader :root

    def initialize(root)
      @root = Pathname.new(root).expand_path
      @evidence = {}
    end

    def run(check_only: false)
      authority_context = validate_authority_and_manifest!
      metrics = validate_official_outputs!(authority_context)
      validate_aggregate_boundaries!(authority_context, metrics)
      rewrites = build_document_rewrites(metrics, authority_context)
      summary = build_summary(metrics, authority_context, rewrites, check_only)

      if check_only
        puts JSON.pretty_generate(summary)
        return summary
      end

      atomic_replace_all!(rewrites) { verify_evidence_unchanged! }
      summary["mode"] = "APPLIED"
      puts JSON.pretty_generate(summary)
      summary
    end

    def rewrite_root_document(raw, replacement)
      require_utf8!(raw, "README.md")
      require_count!(raw, OLD_ROOT_MARKER, 1, "README.md old root marker")
      require_count!(raw, NEW_MARKER, 0, "README.md new marker collision")
      require_count!(raw, ROOT_HISTORY_BOUNDARY, 1, "README.md exact history boundary")
      start_at = byte_index(raw, OLD_ROOT_MARKER)
      generic = heading_positions(raw, /^### 历史.*$/).select { |position, _| position > start_at }
      require!(!generic.empty?, "README.md has no history heading after the old marker")
      boundary_at, boundary_line = generic.first
      require!(boundary_line == ROOT_HISTORY_BOUNDARY,
               "README.md first history boundary is #{boundary_line.inspect}, expected #{ROOT_HISTORY_BOUNDARY.inspect}")
      require!(boundary_at == byte_index(raw, ROOT_HISTORY_BOUNDARY), "README.md history boundary is ambiguous")
      replace_range(raw, start_at, boundary_at, replacement)
    end

    def rewrite_paper_readme(raw, config, replacement)
      label = "papers/#{config.fetch(:slug)}/README.md"
      require_utf8!(raw, label)
      require_count!(raw, "## Current status", 1, "#{label} Current status heading")
      require_count!(raw, NEW_MARKER, 0, "#{label} new marker collision")
      require_count!(raw, config.fetch(:first_history), 1, "#{label} exact first history boundary")
      start_line = "## Current status"
      heading_at = byte_index(raw, start_line)
      line_end = raw.b.index("\n".b, heading_at)
      require!(!line_end.nil?, "#{label} Current status heading lacks a newline")
      content_start = line_end + 1
      generic = heading_positions(raw, /^### Historical.*$/).select { |position, _| position > content_start }
      require!(!generic.empty?, "#{label} has no Historical heading after Current status")
      boundary_at, boundary_line = generic.first
      require!(boundary_line == config.fetch(:first_history),
               "#{label} first Historical boundary is #{boundary_line.inspect}")
      require!(boundary_at == byte_index(raw, config.fetch(:first_history)),
               "#{label} Historical boundary is ambiguous")
      replace_range(raw, content_start, boundary_at, replacement)
    end

    def rewrite_pipeline_state(raw, config, replacement)
      label = "papers/#{config.fetch(:slug)}/notes/pipeline_state.md"
      require_utf8!(raw, label)
      require_count!(raw, NEW_MARKER, 0, "#{label} new marker collision")
      require_count!(raw, PIPELINE_HISTORY_BOUNDARY, 1, "#{label} exact Historical boundary")
      generic = heading_positions(raw, /^## Historical.*$/)
      require!(!generic.empty?, "#{label} has no Historical heading")
      boundary_at, boundary_line = generic.first
      require!(boundary_line == PIPELINE_HISTORY_BOUNDARY,
               "#{label} first Historical boundary is #{boundary_line.inspect}")
      require!(boundary_at == byte_index(raw, PIPELINE_HISTORY_BOUNDARY),
               "#{label} Historical boundary is ambiguous")
      replace_range(raw, 0, boundary_at, replacement)
    end

    # Eleven separate paths cannot be committed by one kernel primitive.  This
    # transaction therefore stages every successor in the destination directory,
    # hard-links all eleven originals into one same-filesystem backup directory,
    # promotes by atomic rename, verifies, and restores every promoted original
    # by atomic rename if any later step fails.
    def atomic_replace_all!(rewrites, fail_after: nil)
      require!(rewrites.length == 11 && rewrites.keys.uniq.length == 11,
               "status transaction must cover exactly 11 unique documents")
      staged = {}
      rewrites.each do |relative, row|
        target = safe_path(relative)
        assert_snapshot!(target, row, "pre-stage")
        temporary = Tempfile.new([".#{target.basename}.", ".round10-status-stage"], target.dirname.to_s)
        temporary.binmode
        temporary.write(row.fetch(:replacement))
        temporary.flush
        temporary.fsync
        File.chmod(row.fetch(:mode), temporary.path)
        temporary.close
        staged_path = Pathname.new(temporary.path)
        require!(Digest::SHA256.file(staged_path).hexdigest == row.fetch(:replacement_sha256),
                 "staged replacement digest mismatch #{relative}")
        staged[relative] = {temporary: temporary, path: staged_path, target: target}
      end

      Dir.mktmpdir(".round10-stage4-prime-status-doc-backup.", root.to_s) do |backup_string|
        backup_root = Pathname.new(backup_string)
        backups = {}
        installed = []
        committed = false
        begin
          rewrites.each do |relative, row|
            target = staged.fetch(relative).fetch(:target)
            assert_snapshot!(target, row, "pre-backup")
            backup = backup_root / relative
            backup.dirname.mkpath
            require!(!backup.exist? && !backup.symlink?, "backup collision #{backup}")
            File.link(target, backup)
            require!(Digest::SHA256.file(backup).hexdigest == row.fetch(:original_sha256),
                     "backup digest mismatch #{relative}")
            backups[relative] = backup
          end
          fsync_directories(backups.values.map(&:dirname))

          rewrites.each do |relative, row|
            target = staged.fetch(relative).fetch(:target)
            assert_snapshot!(target, row, "pre-promotion")
            File.rename(staged.fetch(relative).fetch(:path), target)
            installed << relative
            raise ContractError, "injected fixture failure after #{installed.length} promotions" if
              fail_after && installed.length == fail_after
          end
          fsync_directories(staged.values.map { |entry| entry.fetch(:target).dirname })
          rewrites.each do |relative, row|
            target = staged.fetch(relative).fetch(:target)
            require!(Digest::SHA256.file(target).hexdigest == row.fetch(:replacement_sha256),
                     "post-promotion digest mismatch #{relative}")
          end
          yield if block_given?
          committed = true
        rescue Exception => error # rubocop:disable Lint/RescueException
          rollback_errors = []
          installed.reverse_each do |relative|
            begin
              backup = backups.fetch(relative)
              target = staged.fetch(relative).fetch(:target)
              require!(backup.file? && Digest::SHA256.file(backup).hexdigest ==
                       rewrites.fetch(relative).fetch(:original_sha256),
                       "rollback backup drift #{relative}")
              File.rename(backup, target)
            rescue StandardError => rollback_error
              rollback_errors << "#{relative}: #{rollback_error.message}"
            end
          end
          fsync_directories(staged.values.map { |entry| entry.fetch(:target).dirname }) rescue nil
          rewrites.each do |relative, row|
            target = staged.fetch(relative).fetch(:target)
            next if target.file? && Digest::SHA256.file(target).hexdigest == row.fetch(:original_sha256)

            rollback_errors << "#{relative}: original bytes were not restored"
          end
          suffix = rollback_errors.empty? ? "" : "; ROLLBACK ERRORS: #{rollback_errors.join('; ')}"
          raise ContractError, "status transaction failed: #{error.message}#{suffix}"
        ensure
          if committed
            backups.each_value { |backup| File.unlink(backup) if backup.exist? }
            fsync_directories([backup_root]) rescue nil
          end
        end
      end
    ensure
      staged&.each_value do |entry|
        begin
          File.unlink(entry.fetch(:path)) if entry.fetch(:path).exist?
        rescue Errno::ENOENT
          nil
        end
        entry.fetch(:temporary).close! rescue nil
      end
    end

    private

    def validate_authority_and_manifest!
      authority_bindings = {}
      AUTHORITY.each do |role, expected|
        bytes = read_evidence(expected.fetch(:path), "exact authority #{role}")
        actual_sha = Digest::SHA256.hexdigest(bytes)
        require!(actual_sha == expected.fetch(:sha256), "exact authority SHA-256 drift #{role}")
        authority_bindings[role] = {
          "path" => expected.fetch(:path), "sha256" => actual_sha, "bytes" => bytes.bytesize
        }
      end
      require!(read_evidence(AUTHORITY.dig("author_event", :path), "exact author event") == "确认\n".b,
               "exact author event bytes are not 确认\\n")
      authority_bindings.fetch("author_event")["exact_text"] = "确认\n"

      receipt = read_json_evidence(AUTHORITY.dig("authorization_receipt", :path), "authorization receipt")
      freeze = read_json_evidence(AUTHORITY.dig("input_freeze", :path), "input freeze")
      audit = read_json_evidence(AUTHORITY.dig("authority_audit", :path), "authority audit")
      require!(receipt.fetch("status") == RECEIPT_STATUS, "authorization receipt status")
      require!(receipt.fetch("prepared_evidence_authority_role") == PREPARATION_ROLE,
               "authorization receipt preparation-evidence role")
      require!(receipt.dig("aggregate", "papers") == 5, "authorization receipt paper count")
      require!(receipt.dig("aggregate", "unique_replace_block_pairs") == 130,
               "authorization receipt operation count")
      require!(receipt.dig("aggregate", "matrix_regenerations") == 2,
               "authorization receipt matrix count")
      require!(receipt.dig("aggregate", "p33_bibliography_appends") == 2,
               "authorization receipt bibliography count")
      require!(freeze.fetch("status") == FREEZE_STATUS, "input freeze status")
      require!(freeze.fetch("prepared_evidence_authority_role") == PREPARATION_ROLE,
               "input freeze preparation-evidence role")
      require!(audit.fetch("status") == AUTHORITY_AUDIT_STATUS, "authority audit status")
      require!(audit.fetch("checks_failed", 0).zero?, "authority audit failed-check count")
      require!(audit.fetch("checks").all? { |row| row.fetch("status") == "PASS" },
               "authority audit contains a non-PASS check")
      validate_execution_boundaries!(receipt.fetch("boundaries"), "authorization receipt")
      validate_execution_boundaries!(freeze.fetch("boundaries"), "input freeze")

      manifest = read_json_evidence(FINAL_MANIFEST, "final exact-confirmation emission manifest")
      require!(evidence_binding(FINAL_MANIFEST).fetch("sha256") == FINAL_MANIFEST_SHA256,
               "final exact-confirmation emission manifest SHA-256 drift")
      require!(manifest.fetch("schema_version") == FINAL_MANIFEST_SCHEMA, "final manifest schema")
      require!(manifest.fetch("status") == FINAL_MANIFEST_STATUS, "final manifest status")
      require!(manifest.fetch("preparation_evidence_authority_role") == PREPARATION_ROLE,
               "final manifest preparation-evidence role")
      require!(manifest.dig("aggregate", "papers") == 5, "final manifest paper count")
      require!(manifest.dig("aggregate", "unique_replace_block_pairs") == 130,
               "final manifest operation count")
      require!(manifest.fetch("papers").map { |row| row.fetch("paper_id") } == PAPER_CONFIGS.keys,
               "final manifest paper order")
      AUTHORITY.each_key do |role|
        require_same_binding!(manifest.dig("authority", role), authority_bindings.fetch(role),
                              "final manifest authority #{role}")
      end
      require!(manifest.dig("authority", "author_event", "exact_text") == "确认\n",
               "final manifest exact author text")

      {
        authority: authority_bindings,
        receipt: receipt,
        freeze: freeze,
        manifest: manifest,
        manifest_binding: evidence_binding(FINAL_MANIFEST),
        receipt_binding: evidence_binding(AUTHORITY.dig("authorization_receipt", :path))
      }
    end

    def validate_official_outputs!(context)
      manifest_by_paper = context.fetch(:manifest).fetch("papers").to_h do |row|
        [row.fetch("paper_id"), row]
      end
      freeze_by_paper = context.fetch(:freeze).fetch("papers").to_h do |row|
        [row.fetch("paper_id"), row]
      end
      require!(freeze_by_paper.keys == PAPER_CONFIGS.keys, "input-freeze paper order")

      metrics = PAPER_CONFIGS.to_h do |paper_id, config|
        manifest_row = manifest_by_paper.fetch(paper_id)
        freeze_row = freeze_by_paper.fetch(paper_id)
        metric = validate_one_paper!(paper_id, config, manifest_row, freeze_row)
        [paper_id, metric]
      end

      PAPER_CONFIGS.each do |paper_id, config|
        support = if config.key?(:matrix_receipt)
                    validate_matrix_receipt!(paper_id, config, metrics.fetch(paper_id),
                                             freeze_by_paper.fetch(paper_id), context)
                  elsif paper_id == "P33"
                    validate_bibliography_receipt!(config, metrics.fetch(paper_id),
                                                   freeze_by_paper.fetch(paper_id), context)
                  else
                    {kind: "none", summary: "No authorized in-place support artifact changed."}
                  end
        metrics.fetch(paper_id)[:support] = support
      end

      validate_frozen_files!(freeze_by_paper, metrics)
      metrics
    end

    def validate_one_paper!(paper_id, config, manifest_row, freeze_row)
      slug = config.fetch(:slug)
      notes_prefix = "papers/#{slug}/notes"
      base_rel = "#{notes_prefix}/#{config.fetch(:base)}"
      successor_rel = "#{notes_prefix}/#{config.fetch(:successor)}"
      patch_rel = "#{notes_prefix}/#{config.fetch(:patch)}"
      report_rel = "#{successor_rel}.apply-report.json"
      build_rel = "#{notes_prefix}/#{config.fetch(:build_receipt)}"

      require!(manifest_row.fetch("paper_slug") == slug, "#{paper_id} final-manifest slug")
      require!(manifest_row.fetch("authorized_replace_block_pairs") == config.fetch(:expected_ops),
               "#{paper_id} final-manifest operation count")
      patch_binding = manifest_row.dig("artifacts", "patch")
      verify_bound_artifact!(patch_binding, patch_rel, "#{paper_id} final-manifest patch", require_bytes: true)

      base_bytes = read_evidence(base_rel, "#{paper_id} frozen base")
      verify_row_against_bytes!(freeze_row.fetch("current_working_draft"), base_rel, base_bytes,
                                "#{paper_id} frozen base")
      successor_bytes = read_evidence(successor_rel, "#{paper_id} official successor")
      patch = read_json_evidence(patch_rel, "#{paper_id} exact patch")
      report = read_json_evidence(report_rel, "#{paper_id} official apply report")

      expected_ops = config.fetch(:expected_ops)
      ops = patch.fetch("ops")
      require!(patch.fetch("patch_format_version") == "1.1", "#{paper_id} patch format")
      require!(patch.fetch("revision_round") == config.fetch(:revision_round), "#{paper_id} patch round")
      require!(ops.length == expected_ops, "#{paper_id} patch op count")
      require!(ops.map { |op| op.fetch("block_id") }.uniq.length == expected_ops,
               "#{paper_id} patch target uniqueness")
      require!(ops.all? do |op|
        op.fetch("op") == "replace_block" && op.fetch("claim_strength_changes") == [] &&
          op.fetch("collateral_authorization_ids") == []
      end, "#{paper_id} patch operation/claim/collateral boundary")

      require!(report.fetch("report_format_version") == "1.3", "#{paper_id} apply-report format")
      require!(report.fetch("mode") == "patch", "#{paper_id} apply mode")
      require!(report.fetch("base_path") == base_rel, "#{paper_id} apply base path")
      require!(report.fetch("output_path") == successor_rel, "#{paper_id} apply output path")
      require!(report.fetch("base_draft_hash") == Digest::SHA256.hexdigest(base_bytes)[0, 12],
               "#{paper_id} apply base hash")
      successor_sha = Digest::SHA256.hexdigest(successor_bytes)
      # JSON is read from the exact file, so use the tracked byte hash rather than
      # assuming a serialization convention when checking the official report.
      patch_sha = evidence_binding(patch_rel).fetch("sha256")
      require!(report.fetch("output_draft_hash") == successor_sha[0, 12],
               "#{paper_id} apply output hash")
      require!(report.fetch("patch_digest") == patch_sha, "#{paper_id} apply patch digest")
      require!(report.fetch("revision_round") == config.fetch(:revision_round),
               "#{paper_id} apply revision round")
      require!(report.fetch("authorization_context") == "review_roadmap",
               "#{paper_id} apply authorization context")
      require!(report.dig("authorization_witness", "status") == "pass",
               "#{paper_id} apply authorization witness")
      %w[revision_roadmap author_adjudication claim_surface_manifest].each do |role|
        witness_key = role == "revision_roadmap" ? "roadmap_sha256" : "#{role}_sha256"
        require!(report.dig("authorization_witness", witness_key) ==
                 manifest_row.dig("artifacts", role, "sha256"),
                 "#{paper_id} apply witness #{role}")
      end
      require!(report.dig("authorization_witness", "registered_claim_surfaces_checked") == 0,
               "#{paper_id} registered-claim population")
      require!(report.dig("authorization_witness", "unregistered_claim_drift_review_required") == true,
               "#{paper_id} unregistered-claim boundary")
      require!(report.dig("structural_flags", "any") == false,
               "#{paper_id} apply structural flags")

      applied = report.fetch("ops_applied")
      require!(applied.length == expected_ops, "#{paper_id} applied op count")
      applied.each_with_index do |row, index|
        op = ops.fetch(index)
        require!(row.fetch("op_index") == index && row.fetch("op") == "replace_block" &&
                 row.fetch("block_id") == op.fetch("block_id") &&
                 row.fetch("roadmap_item_ids") == op.fetch("roadmap_item_ids") &&
                 row.fetch("claim_strength_changes") == [] &&
                 row.fetch("collateral_authorization_ids") == [] &&
                 row.fetch("new_block_ids").is_a?(Array),
                 "#{paper_id} apply op #{index} does not replay the patch")
      end
      fresh_ids = applied.flat_map { |row| row.fetch("new_block_ids") }
      require!(fresh_ids == report.fetch("fresh_block_ids") && fresh_ids.uniq == fresh_ids,
               "#{paper_id} fresh block allocation does not replay the apply report")

      counters = report.fetch("counters")
      total = counters.fetch("blocks_total")
      preserved = counters.fetch("blocks_preserved_byte_identical")
      require!(counters.fetch("blocks_touched") == expected_ops, "#{paper_id} touched-block count")
      require!(preserved + expected_ops == total, "#{paper_id} preserved-block arithmetic")
      validate_successor_blocks!(paper_id, base_bytes, successor_bytes, ops, applied, total, preserved)
      require!(successor_bytes.include?("\\usepackage[numbers,sort&compress]{natbib}"),
               "#{paper_id} natbib numeric configuration drift")
      require!(successor_bytes.include?("\\bibliographystyle{plainnat}"),
               "#{paper_id} plainnat style drift")
      require!(!successor_bytes.match?(/[\x00-\x08\x0b\x0c\x0e-\x1f]/),
               "#{paper_id} successor contains a forbidden control byte")

      build = read_json_evidence(build_rel, "#{paper_id} clean build receipt")
      require!(build.fetch("status") == "PASS_CLEAN", "#{paper_id} build status")
      require!(build.fetch("paper_id") == paper_id, "#{paper_id} build identity")
      require!(build.fetch("citation_style") == "natbib[numbers,sort&compress] + plainnat",
               "#{paper_id} build citation style")
      pages = build.fetch("pages")
      require!(pages.is_a?(Integer) && pages.positive?, "#{paper_id} build page count")
      %w[undefined_citations undefined_references missing_glyphs fatal_errors overfull_hboxes].each do |key|
        require!(build.fetch(key).zero?, "#{paper_id} build #{key} is nonzero")
      end
      require!(build.dig("bindings", "revised_draft_sha256") == successor_sha,
               "#{paper_id} build/successor binding")
      require!(build.dig("bindings", "patch_sha256") == patch_sha,
               "#{paper_id} build/patch binding")

      bibliography_rel = "papers/#{slug}/#{config.fetch(:bibliography)}"
      bibliography_bytes = read_evidence(bibliography_rel, "#{paper_id} build bibliography")
      require!(build.dig("bindings", "references_bib_sha256") == Digest::SHA256.hexdigest(bibliography_bytes),
               "#{paper_id} build/bibliography binding")
      bundle_rel = "#{notes_prefix}/#{config.fetch(:bundle)}"
      pdf_rel = "#{notes_prefix}/#{config.fetch(:pdf)}"
      log_rel = "#{notes_prefix}/#{config.fetch(:build_log)}"
      transcript_rel = "#{notes_prefix}/#{config.fetch(:build_transcript)}"
      bundle_bytes = read_evidence(bundle_rel, "#{paper_id} revision bundle")
      pdf_bytes = read_evidence(pdf_rel, "#{paper_id} preview PDF")
      log_bytes = read_evidence(log_rel, "#{paper_id} build log")
      transcript_bytes = read_evidence(transcript_rel, "#{paper_id} build transcript")
      require!(pdf_bytes.start_with?("%PDF".b), "#{paper_id} preview is not a PDF")
      {
        "evidence_bundle_sha256" => Digest::SHA256.hexdigest(bundle_bytes),
        "preview_pdf_sha256" => Digest::SHA256.hexdigest(pdf_bytes),
        "final_build_log_sha256" => Digest::SHA256.hexdigest(log_bytes),
        "build_transcript_sha256" => Digest::SHA256.hexdigest(transcript_bytes)
      }.each do |key, digest|
        require!(build.dig("bindings", key) == digest, "#{paper_id} build binding #{key}")
      end
      boundaries = build.fetch("boundaries")
      require!(boundaries.fetch("canonical_manuscript_or_pdf_modified") == false,
               "#{paper_id} canonical manuscript/PDF boundary")
      require!(boundaries.fetch("canonical_bibliography_modified") == (paper_id == "P33"),
               "#{paper_id} canonical bibliography boundary")
      require!(boundaries.fetch("p33_exact_bibliography_exception") == (paper_id == "P33"),
               "#{paper_id} P33 bibliography exception boundary")
      require!(boundaries.fetch("canonical_results_refreshed") == false,
               "#{paper_id} result-refresh boundary")
      require!(boundaries.fetch("fresh_stage4_5_invoked") == false,
               "#{paper_id} fresh Stage 4.5 boundary")
      require!(boundaries.fetch("stage5_or_stage6_invoked") == false,
               "#{paper_id} Stage 5/6 boundary")

      before_words = marker_free_word_count(base_bytes)
      after_words = marker_free_word_count(successor_bytes)
      {
        paper_id: paper_id,
        config: config,
        ops: applied.length,
        total_blocks: total,
        preserved_blocks: preserved,
        pages: pages,
        word_count_before: before_words,
        word_count_after: after_words,
        word_delta: after_words - before_words,
        base_path: base_rel,
        base_sha256: Digest::SHA256.hexdigest(base_bytes),
        successor_path: successor_rel,
        successor_sha256: successor_sha,
        patch_path: patch_rel,
        patch_sha256: patch_sha,
        apply_report_path: report_rel,
        apply_report_sha256: evidence_binding(report_rel).fetch("sha256"),
        build_receipt_path: build_rel,
        build_receipt_sha256: evidence_binding(build_rel).fetch("sha256"),
        preview_pdf_path: pdf_rel,
        preview_pdf_sha256: Digest::SHA256.hexdigest(pdf_bytes),
        bibliography_path: bibliography_rel,
        bibliography_sha256: Digest::SHA256.hexdigest(bibliography_bytes),
        support: nil
      }
    end

    def validate_successor_blocks!(paper_id, base_bytes, successor_bytes, ops, applied, total, preserved)
      base_pairs = parse_blocks(base_bytes, "#{paper_id} base")
      successor_pairs = parse_blocks(successor_bytes, "#{paper_id} successor")
      require!(base_pairs.length == total, "#{paper_id} block total differs from apply report")
      fresh_ids = applied.flat_map { |row| row.fetch("new_block_ids") }
      require!((successor_pairs.keys - fresh_ids) == base_pairs.keys,
               "#{paper_id} base-block order/set changed in successor")
      require!((successor_pairs.keys - base_pairs.keys) == fresh_ids,
               "#{paper_id} successor fresh-block order/set differs from apply report")
      require!(successor_pairs.length == total + fresh_ids.length,
               "#{paper_id} successor block count does not include exactly the reported fresh blocks")
      op_by_block = ops.to_h { |op| [op.fetch("block_id"), op] }
      applied_by_block = applied.to_h { |row| [row.fetch("block_id"), row] }
      unchanged = 0
      base_pairs.each do |block_id, old_text|
        new_text = successor_pairs.fetch(block_id)
        if op_by_block.key?(block_id)
          allocated = applied_by_block.fetch(block_id).fetch("new_block_ids")
          reconstructed = ([new_text] + allocated.map { |fresh_id| successor_pairs.fetch(fresh_id) }).join("\n")
          require!(normalized_block_text(reconstructed) ==
                   normalized_block_text(op_by_block.fetch(block_id).fetch("new_text")),
                   "#{paper_id}/#{block_id} successor text differs from patch")
        else
          require!(new_text == old_text, "#{paper_id}/#{block_id} untouched block changed")
          unchanged += 1
        end
      end
      require!(unchanged == preserved, "#{paper_id} byte-identical preserved-block count")
    end

    def validate_matrix_receipt!(paper_id, config, metric, freeze_row, context)
      slug = config.fetch(:slug)
      receipt_rel = "papers/#{slug}/#{config.fetch(:matrix_receipt)}"
      matrix_rel = "papers/#{slug}/#{config.fetch(:matrix)}"
      receipt = read_json_evidence(receipt_rel, "#{paper_id} matrix regeneration receipt")
      require!(receipt.fetch("status") == "PASS_AUTHORIZED_IN_PLACE_REGENERATION",
               "#{paper_id} matrix receipt status")
      require!(receipt.fetch("paper_id") == paper_id, "#{paper_id} matrix receipt identity")
      validate_embedded_authority!(receipt.fetch("exact_confirmation_authority"), context.fetch(:authority),
                                   "#{paper_id} matrix receipt")
      require_same_binding!(receipt.fetch("final_emission_manifest"), context.fetch(:manifest_binding),
                            "#{paper_id} matrix final manifest")
      frozen_matrix = freeze_row.fetch("authorized_in_place_matrix_regeneration")
      require!(receipt.fetch("matrix_path") == matrix_rel, "#{paper_id} matrix path")
      require!(receipt.fetch("before_sha256") == frozen_matrix.fetch("sha256"),
               "#{paper_id} matrix before hash")
      require!(receipt.fetch("before_bytes") == frozen_matrix.fetch("bytes"),
               "#{paper_id} matrix before bytes")
      matrix_bytes = read_evidence(matrix_rel, "#{paper_id} regenerated matrix")
      require!(receipt.fetch("after_sha256") == Digest::SHA256.hexdigest(matrix_bytes),
               "#{paper_id} matrix after hash")
      require!(receipt.fetch("after_bytes") == matrix_bytes.bytesize, "#{paper_id} matrix after bytes")
      require!(receipt.fetch("after_sha256") != receipt.fetch("before_sha256"),
               "#{paper_id} matrix regeneration was a no-op")
      require!(receipt.fetch("patch_path") == metric.fetch(:patch_path) &&
               receipt.fetch("patch_sha256") == metric.fetch(:patch_sha256),
               "#{paper_id} matrix/patch binding")
      require!(receipt.fetch("successor_draft_path") == metric.fetch(:successor_path) &&
               receipt.fetch("successor_draft_sha256") == metric.fetch(:successor_sha256),
               "#{paper_id} matrix/successor binding")
      require!(receipt.fetch("apply_report_path") == metric.fetch(:apply_report_path) &&
               receipt.fetch("apply_report_sha256") == metric.fetch(:apply_report_sha256),
               "#{paper_id} matrix/apply binding")
      require!(receipt.fetch("applied_operation_count") == metric.fetch(:ops),
               "#{paper_id} matrix applied-op count")
      expected_counts = config.fetch(:matrix_counts)
      require!(receipt.fetch("result_counts") == expected_counts, "#{paper_id} matrix result counts")
      matrix = parse_json(matrix_bytes, "#{paper_id} regenerated matrix")
      require!(matrix.fetch("result_counts") == expected_counts, "#{paper_id} matrix embedded counts")
      require!(matrix.fetch("row_count") == expected_counts.fetch("row_count"),
               "#{paper_id} matrix embedded row count")
      boundaries = receipt.fetch("boundaries")
      %w[locator_guessing claim_strengthening scientific_result_change route_change other_matrix_or_tsv_changed].each do |key|
        require!(boundaries.fetch(key) == false, "#{paper_id} matrix boundary #{key}")
      end
      {
        kind: "matrix",
        path: matrix_rel,
        before_sha256: receipt.fetch("before_sha256"),
        after_sha256: receipt.fetch("after_sha256"),
        receipt_path: receipt_rel,
        receipt_sha256: evidence_binding(receipt_rel).fetch("sha256"),
        counts: expected_counts,
        summary: "#{config.fetch(:matrix_kind)} matrix updated in place: " \
                 "#{expected_counts.fetch('bounded_substantive_locator_rows')} bounded locators + " \
                 "#{expected_counts.fetch('explicit_bounded_unavailability_rows')} explicit unavailable + " \
                 "#{expected_counts.fetch('preexisting_narrow_record_or_method_locator_rows')} retained = " \
                 "#{expected_counts.fetch('row_count')} rows."
      }
    end

    def validate_bibliography_receipt!(config, metric, freeze_row, context)
      paper_id = "P33"
      slug = config.fetch(:slug)
      receipt_rel = "papers/#{slug}/#{config.fetch(:bibliography_receipt)}"
      receipt = read_json_evidence(receipt_rel, "P33 bibliography append receipt")
      require!(receipt.fetch("status") == "PASS_EXACT_TWO_ENTRY_APPEND_AND_FIVE_USE_BINDING",
               "P33 bibliography receipt status")
      require!(receipt.fetch("paper_id") == paper_id, "P33 bibliography receipt identity")
      validate_embedded_authority!(receipt.fetch("exact_confirmation_authority"), context.fetch(:authority),
                                   "P33 bibliography receipt")
      require_same_binding!(receipt.fetch("final_emission_manifest"), context.fetch(:manifest_binding),
                            "P33 bibliography final manifest")
      bib_bytes = read_evidence(metric.fetch(:bibliography_path), "P33 canonical bibliography result")
      frozen_bib = freeze_row.fetch("current_working_bibliography")
      bibliography = receipt.fetch("bibliography")
      require!(bibliography.fetch("path") == config.fetch(:bibliography), "P33 bibliography path")
      require!(bibliography.fetch("before_sha256") == frozen_bib.fetch("sha256") &&
               bibliography.fetch("before_bytes") == frozen_bib.fetch("bytes"),
               "P33 bibliography frozen base binding")
      require!(bibliography.fetch("after_sha256") == Digest::SHA256.hexdigest(bib_bytes) &&
               bibliography.fetch("after_bytes") == bib_bytes.bytesize,
               "P33 bibliography result binding")
      keys = %w[P33-S03-CORR P33-S16-CORR]
      require!(bibliography.fetch("entries_appended") == keys, "P33 appended bibliography keys")
      parsed_keys = bib_bytes.scan(/@[A-Za-z]+\{([^,]+),/).flatten
      keys.each { |key| require!(parsed_keys.count(key) == 1, "P33 bibliography key count #{key}") }
      counts = receipt.fetch("counts")
      require!(counts == {"entries_appended" => 2, "affected_uses_dual_bound" => 5,
                          "existing_entries_overwritten" => 0}, "P33 bibliography receipt counts")
      manuscript = receipt.fetch("manuscript")
      require!(manuscript.fetch("path") == "notes/#{config.fetch(:successor)}" &&
               manuscript.fetch("sha256") == metric.fetch(:successor_sha256),
               "P33 bibliography/successor binding")
      require!(manuscript.fetch("patch_sha256") == metric.fetch(:patch_sha256) &&
               manuscript.fetch("apply_report_path") == metric.fetch(:apply_report_path) &&
               manuscript.fetch("apply_report_sha256") == metric.fetch(:apply_report_sha256) &&
               manuscript.fetch("applied_operation_count") == metric.fetch(:ops),
               "P33 bibliography patch/apply binding")
      require!(manuscript.fetch("dual_bound_uses").length == 5,
               "P33 bibliography dual-bound use count")
      require!(manuscript.fetch("dual_bound_uses").map { |row| row.fetch("use_id") } ==
               %w[P33-U08 P33-U22 P33-U27 P33-U28 P33-U37],
               "P33 bibliography dual-bound use order")
      expected_support = {
        "plan" => "papers/#{slug}/#{config.fetch(:bibliography_plan)}",
        "prospective_contract" => "papers/#{slug}/#{config.fetch(:bibliography_prospective)}"
      }
      expected_support.each do |role, root_relative|
        paper_relative = root_relative.delete_prefix("papers/#{slug}/")
        row = receipt.fetch(role)
        require!(row.fetch("path") == paper_relative, "P33 bibliography #{role} path")
        bytes = read_evidence(root_relative, "P33 bibliography #{role}")
        require!(row.fetch("sha256") == Digest::SHA256.hexdigest(bytes) &&
                 row.fetch("bytes") == bytes.bytesize, "P33 bibliography #{role} binding")
      end
      boundaries = receipt.fetch("boundaries")
      %w[third_entry_added scientific_claim_strengthened systematic_retraction_or_conflict_audit_claimed
         canonical_manuscript_or_pdf_changed fresh_stage4_5_or_re_review_run].each do |key|
        require!(boundaries.fetch(key) == false, "P33 bibliography boundary #{key}")
      end
      {
        kind: "bibliography",
        path: metric.fetch(:bibliography_path),
        before_sha256: bibliography.fetch("before_sha256"),
        after_sha256: bibliography.fetch("after_sha256"),
        receipt_path: receipt_rel,
        receipt_sha256: evidence_binding(receipt_rel).fetch("sha256"),
        appended_keys: keys,
        entries_appended: 2,
        affected_uses: 5,
        summary: "canonical references.bib received exactly 2 append-only correction entries " \
                 "(P33-S03-CORR, P33-S16-CORR), dual-binding exactly 5 uses."
      }
    end

    def validate_frozen_files!(freeze_by_paper, metrics)
      PAPER_CONFIGS.each do |paper_id, config|
        freeze_row = freeze_by_paper.fetch(paper_id)
        metric = metrics.fetch(paper_id)
        require!(freeze_row.fetch("paper_slug") == config.fetch(:slug), "#{paper_id} frozen slug")
        require!(freeze_row.fetch("authorized_unique_replace_block_pairs") == config.fetch(:expected_ops),
                 "#{paper_id} frozen operation count")
        verify_unchanged_binding!(freeze_row.fetch("initial_system_source"), "#{paper_id} initial system")
        verify_unchanged_binding!(freeze_row.fetch("route_crosswalk"), "#{paper_id} Route crosswalk")
        freeze_row.fetch("science_files").each do |row|
          verify_unchanged_binding!(row, "#{paper_id} frozen science file")
        end

        freeze_row.fetch("canonical_files").each do |row|
          if paper_id == "P33" && row.fetch("path") == metric.fetch(:bibliography_path)
            support = metric.fetch(:support)
            require!(support.fetch(:kind) == "bibliography" &&
                     row.fetch("sha256") == support.fetch(:before_sha256) &&
                     metric.fetch(:bibliography_sha256) == support.fetch(:after_sha256),
                     "P33 sole canonical bibliography exception binding")
          else
            verify_unchanged_binding!(row, "#{paper_id} canonical freeze")
          end
        end

        current_bib = freeze_row.fetch("current_working_bibliography")
        if paper_id == "P33"
          require!(current_bib.fetch("path") == metric.fetch(:bibliography_path) &&
                   current_bib.fetch("sha256") == metric.dig(:support, :before_sha256),
                   "P33 frozen working bibliography exception")
        else
          verify_unchanged_binding!(current_bib, "#{paper_id} working bibliography")
        end

        if config.key?(:matrix_receipt)
          frozen_matrix = freeze_row.fetch("authorized_in_place_matrix_regeneration")
          require!(frozen_matrix.fetch("path") == metric.dig(:support, :path) &&
                   frozen_matrix.fetch("sha256") == metric.dig(:support, :before_sha256),
                   "#{paper_id} authorized matrix exception")
        else
          require!(!freeze_row.key?("authorized_in_place_matrix_regeneration"),
                   "#{paper_id} unexpected matrix exception")
        end
      end
    end

    def validate_aggregate_boundaries!(context, metrics)
      require!(metrics.values.sum { |metric| metric.fetch(:ops) } == 130,
               "official applied-operation total is not 130")
      require!(metrics.values.all? { |metric| metric.fetch(:pages).positive? },
               "one or more clean previews has no pages")
      require!(metrics.values.count { |metric| metric.dig(:support, :kind) == "matrix" } == 2,
               "matrix receipt coverage is not exactly two")
      p33 = metrics.fetch("P33")
      require!(p33.dig(:support, :kind) == "bibliography" &&
               p33.dig(:support, :entries_appended) == 2,
               "P33 exact bibliography append coverage")
      PAPER_CONFIGS.keys.reject { |paper_id| paper_id == "P33" }.each do |paper_id|
        require!(metrics.fetch(paper_id).dig(:support, :kind) != "bibliography",
                 "non-P33 canonical bibliography mutation")
      end
      verify_evidence_unchanged!
      require!(context.fetch(:manifest_binding).fetch("sha256") == evidence_binding(FINAL_MANIFEST).fetch("sha256"),
               "final manifest changed during preflight")
    end

    def build_document_rewrites(metrics, context)
      replacements = {}
      root_relative = "README.md"
      root_raw, root_snapshot = read_target(root_relative)
      root_new = rewrite_root_document(root_raw, render_root_status(metrics, context))
      replacements[root_relative] = replacement_row(root_snapshot, root_new)

      PAPER_CONFIGS.each do |paper_id, config|
        metric = metrics.fetch(paper_id)
        paper_relative = "papers/#{config.fetch(:slug)}/README.md"
        paper_raw, paper_snapshot = read_target(paper_relative)
        paper_new = rewrite_paper_readme(paper_raw, config,
                                         render_paper_status(metric, context, paper_relative))
        replacements[paper_relative] = replacement_row(paper_snapshot, paper_new)

        pipeline_relative = "papers/#{config.fetch(:slug)}/notes/pipeline_state.md"
        pipeline_raw, pipeline_snapshot = read_target(pipeline_relative)
        pipeline_new = rewrite_pipeline_state(pipeline_raw, config,
                                              render_pipeline_status(metric, context, pipeline_relative))
        replacements[pipeline_relative] = replacement_row(pipeline_snapshot, pipeline_new)
      end
      require!(replacements.length == 11, "rendered status-document count is not 11")
      replacements.each do |relative, row|
        require!(row.fetch(:replacement).include?(NEW_MARKER), "#{relative} lacks new status marker")
        require_count!(row.fetch(:replacement), NEW_MARKER, 1, "#{relative} rendered marker")
        require!(row.fetch(:replacement) != row.fetch(:original), "#{relative} replacement is a no-op")
      end
      replacements
    end

    def render_root_status(metrics, context)
      rows = PAPER_CONFIGS.map do |paper_id, config|
        metric = metrics.fetch(paper_id)
        support = case metric.dig(:support, :kind)
                  when "matrix"
                    counts = metric.dig(:support, :counts)
                    "notes-side #{config.fetch(:matrix_kind)} matrix：" \
                      "#{counts.fetch('bounded_substantive_locator_rows')}/" \
                      "#{counts.fetch('explicit_bounded_unavailability_rows')}/" \
                      "#{counts.fetch('preexisting_narrow_record_or_method_locator_rows')}，" \
                      "共 #{counts.fetch('row_count')} 行"
                  when "bibliography"
                    "canonical Bib 恰好 +2；5 uses dual-bound"
                  else
                    "无 in-place support mutation"
                  end
        "| [#{paper_id}](papers/#{config.fetch(:slug)}/README.md) | #{config.fetch(:conclusion)} | " \
          "#{metric.fetch(:ops)}/#{config.fetch(:expected_ops)} | " \
          "#{metric.fetch(:preserved_blocks)}/#{metric.fetch(:total_blocks)} | " \
          "#{format_delta(metric.fetch(:word_delta))} | #{metric.fetch(:pages)} 页 clean | #{support} |"
      end.join("\n")

      artifact_rows = metrics.map do |paper_id, metric|
        "| #{paper_id} | [successor](#{metric.fetch(:successor_path)}) `#{metric.fetch(:successor_sha256)}` | " \
          "[apply report](#{metric.fetch(:apply_report_path)}) `#{metric.fetch(:apply_report_sha256)}` | " \
          "[build receipt](#{metric.fetch(:build_receipt_path)}) `#{metric.fetch(:build_receipt_sha256)}` |"
      end.join("\n")

      systems = PAPER_CONFIGS.map do |paper_id, config|
        "- **#{paper_id}** — #{config.fetch(:system)}."
      end.join("\n")
      routes = PAPER_CONFIGS.map do |paper_id, config|
        "- **#{paper_id}** — #{config.fetch(:route)}."
      end.join("\n")
      matrix_lines = %w[P30 P31].map do |paper_id|
        support = metrics.fetch(paper_id).fetch(:support)
        "- #{paper_id} matrix：`#{support.fetch(:before_sha256)}` → `#{support.fetch(:after_sha256)}`；" \
          "receipt `#{support.fetch(:receipt_sha256)}`。"
      end.join("\n")
      p33_support = metrics.fetch("P33").fetch(:support)

      <<~MD.rstrip
        #{NEW_MARKER}

        本轮 exact-confirmation 执行已经完成：**Papers 29--33 的 Stage 4′ correction
        complete，当前等待另行授权的 fresh Stage 4.5**。五篇正式 successor 与 apply
        report、五份 `PASS_CLEAN` build receipt、P30/P31 两份 matrix receipt，以及
        P33 的精确 Bib receipt 均已通过交叉绑定；整批为 **130/130 个
        `replace_block` operations**。这不是 Stage 4.5 PASS，也不会自动进入 Stage 5。

        | Paper | 本轮明确结论 | Ops | Byte-identical preserved | Marker-free word Δ | Preview | 授权 support 变化 |
        |---|---|---:|---:|---:|---:|---|
        #{rows}

        P30/P31 的既有 notes-side matrices 已按授权原位更新，且没有猜测 locator、增强
        claim 或改变 Route／科学结果：

        #{matrix_lines}

        P33 在 canonical `paper/references.bib` **恰好 append 2 条**
        `P33-S03-CORR` / `P33-S16-CORR`，并 dual-bind 恰好 5 个 uses；Bib SHA-256
        `#{p33_support.fetch(:before_sha256)}` → `#{p33_support.fetch(:after_sha256)}`，
        receipt `#{p33_support.fetch(:receipt_sha256)}`。这是本轮**唯一授权的 canonical
        byte change**。五篇 canonical manuscript/PDF、P29--P32 canonical Bib、全部
        frozen initial-system/Route crosswalk 保持不变；scientific execution = `0`，
        canonical result refresh = `0`，引用继续为 `plainnat` 数字制。

        Route A 坐标保持既定值：

        #{routes}

        汇总仍为 formal Route-A tuple `0/5`、positive arithmetic A2 `0/5`、A3
        `0/5`、A4 `0/5`、Route-B invocation `0/5`。五个初始动力学限定保持：

        #{systems}

        当前可回放工件：

        | Paper | Official successor SHA-256 | Apply-report SHA-256 | Clean-build receipt SHA-256 |
        |---|---|---|---|
        #{artifact_rows}

        - [Exact-confirmation final-emission manifest](#{FINAL_MANIFEST}) — `#{context.dig(:manifest_binding, "sha256")}`
        - [Exact-confirmation authorization receipt](#{AUTHORITY.dig("authorization_receipt", :path)}) — `#{context.dig(:receipt_binding, "sha256")}`
        - [预定 completion report](#{PLANNED_COMPLETION_REPORT})（本状态更新器不要求该报告预先存在）

        下一合法转换只有：在新的、独立的明确授权之后，对这五个 exact successor
        启动 fresh Stage 4.5 from-scratch integrity gate。当前状态本身不授权该 gate。
      MD
    end

    def render_paper_status(metric, context, document_relative)
      config = metric.fetch(:config)
      support = render_support_paragraph(metric)
      artifact_rows = paper_artifact_rows(metric, context, document_relative)
      <<~MD.rstrip

        #{NEW_MARKER}

        **ARS STAGE 4′ CORRECTION COMPLETE — AWAITING SEPARATELY AUTHORIZED FRESH STAGE 4.5.**

        Control state: `#{CONTROL_STATE}`. The exact-confirmation chain applied
        **#{metric.fetch(:ops)}/#{config.fetch(:expected_ops)}** authorized
        `replace_block` operations to a new versioned successor, preserving
        **#{metric.fetch(:preserved_blocks)}/#{metric.fetch(:total_blocks)}** source
        blocks byte-identically. Marker-free word count changed from
        #{metric.fetch(:word_count_before)} to #{metric.fetch(:word_count_after)}
        (#{format_delta(metric.fetch(:word_delta))}). The notes-side preview is
        **#{metric.fetch(:pages)} pages** and `PASS_CLEAN`: fatal, undefined
        citation/reference, missing-glyph, and overfull counts are all zero.

        本轮结论概要：#{config.fetch(:conclusion)}

        #{support}

        Frozen initial system: #{config.fetch(:system)}.

        Route mapping: #{config.fetch(:route)}. No Route coordinate changed and
        this correction round awards no Route credit.

        Batch boundary: 130/130 exact manuscript operations completed across
        Papers 29--33. Scientific execution and canonical-result refresh both
        remain `0`. Citation formatting remains `plainnat` numeric. Canonical
        manuscript/PDF bytes are unchanged for all five papers; P33's exact
        two-entry append to canonical `references.bib` is the sole authorized
        canonical byte change, while P29--P32 canonical bibliographies are
        unchanged. Fresh Stage 4.5, Stage 5/6, canonical manuscript/PDF
        promotion, submission, and new scientific execution were not invoked.

        | Current exact artifact | SHA-256 |
        |---|---|
        #{artifact_rows}

        Next legal transition: a separately authorized fresh Stage 4.5
        from-scratch integrity audit of this exact successor. This status does
        not itself authorize that mandatory gate.
      MD
    end

    def render_pipeline_status(metric, context, document_relative)
      config = metric.fetch(:config)
      support = render_support_paragraph(metric)
      artifact_rows = paper_artifact_rows(metric, context, document_relative)
      <<~MD.rstrip
        # #{metric.fetch(:paper_id)} pipeline state

        Synchronized: **2026-09-04 UTC**

        Current controlling state: **`#{CONTROL_STATE}`**.

        #{NEW_MARKER}

        | Current gate field | Value |
        |---|---|
        | Pipeline global state | `#{CONTROL_STATE}` |
        | Current completed gate | Stage 4′ exact-confirmation correction `COMPLETE`; fresh Stage 4.5 `NOT_INVOKED` |
        | Explicit paper conclusion | #{config.fetch(:conclusion)} |
        | Deterministic apply | #{metric.fetch(:ops)}/#{config.fetch(:expected_ops)} exact `replace_block`; #{metric.fetch(:preserved_blocks)}/#{metric.fetch(:total_blocks)} blocks preserved byte-identically |
        | Marker-free word count | #{metric.fetch(:word_count_before)} → #{metric.fetch(:word_count_after)} (#{format_delta(metric.fetch(:word_delta))}) |
        | Clean preview | `PASS_CLEAN`; #{metric.fetch(:pages)} pages; fatal/undefined citation/undefined reference/missing glyph/overfull all `0` |
        | Authorized support result | #{support} |
        | Frozen initial system | #{config.fetch(:system)} |
        | Route | #{config.fetch(:route)}; no coordinate change or credit |
        | Canonical/science boundary | canonical manuscript/PDF unchanged; scientific execution/result refresh `0`; P33 exact two-entry canonical Bib append is the sole authorized canonical change |
        | Citation style | `natbib[numbers,sort&compress] + plainnat` numeric; unchanged |
        | Next legal transition | separately authorized fresh Stage 4.5 from-scratch integrity gate only |

        Batch aggregate: **130/130 operations**, five clean versioned previews,
        two authorized notes-side matrix regenerations, and exactly two P33
        canonical bibliography appends. This is Stage 4′ correction completion,
        not a Stage 4.5 integrity verdict or Route advancement.

        | Current exact artifact | SHA-256 |
        |---|---|
        #{artifact_rows}

      MD
    end

    def render_support_paragraph(metric)
      support = metric.fetch(:support)
      case support.fetch(:kind)
      when "matrix"
        counts = support.fetch(:counts)
        "Authorized notes-side support update: the #{metric.dig(:config, :matrix_kind)} matrix was regenerated in place with " \
          "#{counts.fetch('bounded_substantive_locator_rows')} bounded locator rows, " \
          "#{counts.fetch('explicit_bounded_unavailability_rows')} explicit bounded-unavailability rows, " \
          "#{counts.fetch('preexisting_narrow_record_or_method_locator_rows')} retained narrow rows, and " \
          "#{counts.fetch('row_count')} rows total. Matrix SHA-256: `#{support.fetch(:before_sha256)}` → " \
          "`#{support.fetch(:after_sha256)}`."
      when "bibliography"
        "Authorized canonical exception: `paper/references.bib` received exactly two append-only entries " \
          "(`P33-S03-CORR`, `P33-S16-CORR`) and exactly five uses were dual-bound. " \
          "No third entry or existing-entry overwrite occurred. Bibliography SHA-256: " \
          "`#{support.fetch(:before_sha256)}` → `#{support.fetch(:after_sha256)}`."
      else
        "No in-place support artifact or canonical package byte was authorized to change for this paper."
      end
    end

    def paper_artifact_rows(metric, context, document_relative)
      rows = [
        ["Exact patch", metric.fetch(:patch_path), metric.fetch(:patch_sha256)],
        ["Official successor", metric.fetch(:successor_path), metric.fetch(:successor_sha256)],
        ["Official apply report", metric.fetch(:apply_report_path), metric.fetch(:apply_report_sha256)],
        ["Clean build receipt", metric.fetch(:build_receipt_path), metric.fetch(:build_receipt_sha256)],
        ["Preview PDF", metric.fetch(:preview_pdf_path), metric.fetch(:preview_pdf_sha256)]
      ]
      support = metric.fetch(:support)
      if %w[matrix bibliography].include?(support.fetch(:kind))
        rows << [support.fetch(:kind) == "matrix" ? "Matrix regeneration receipt" : "P33 Bib append receipt",
                 support.fetch(:receipt_path), support.fetch(:receipt_sha256)]
      end
      rows << ["Exact final-emission manifest", FINAL_MANIFEST,
               context.dig(:manifest_binding, "sha256")]
      rows << ["Exact authorization receipt", AUTHORITY.dig("authorization_receipt", :path),
               context.dig(:receipt_binding, "sha256")]
      rows << ["Planned completion report (not a precondition)", PLANNED_COMPLETION_REPORT, nil]
      rows.map do |label, path, digest|
        suffix = digest ? "`#{digest}`" : "not required to pre-exist"
        "| [#{label}](#{relative_link(document_relative, path)}) | #{suffix} |"
      end.join("\n")
    end

    def build_summary(metrics, context, rewrites, check_only)
      {
        "status" => "PASS",
        "mode" => check_only ? "CHECK_ONLY_NO_WRITES" : "READY_TO_APPLY",
        "marker" => NEW_MARKER,
        "pipeline_state" => CONTROL_STATE,
        "documents_validated" => rewrites.length,
        "documents" => rewrites.keys,
        "aggregate" => {
          "papers" => metrics.length,
          "operations" => metrics.values.sum { |metric| metric.fetch(:ops) },
          "matrix_regenerations" => metrics.values.count { |metric| metric.dig(:support, :kind) == "matrix" },
          "p33_bibliography_entries_appended" => metrics.dig("P33", :support, :entries_appended),
          "scientific_executions" => 0,
          "canonical_result_refreshes" => 0,
          "fresh_stage4_5_invoked" => false
        },
        "final_emission_manifest" => context.fetch(:manifest_binding),
        "papers" => metrics.transform_values do |metric|
          {
            "ops" => metric.fetch(:ops),
            "preserved_blocks" => metric.fetch(:preserved_blocks),
            "total_blocks" => metric.fetch(:total_blocks),
            "word_delta" => metric.fetch(:word_delta),
            "pages" => metric.fetch(:pages),
            "successor_sha256" => metric.fetch(:successor_sha256),
            "apply_report_sha256" => metric.fetch(:apply_report_sha256),
            "build_receipt_sha256" => metric.fetch(:build_receipt_sha256),
            "support_receipt_sha256" => metric.dig(:support, :receipt_sha256)
          }.compact
        end,
        "evidence_files_replay_checked" => @evidence.length,
        "planned_completion_report_required_to_exist" => false
      }
    end

    def read_evidence(relative, label)
      path = safe_path(relative)
      bytes, stat = stable_regular_read(path, label)
      binding = {"path" => relative, "sha256" => Digest::SHA256.hexdigest(bytes),
                 "bytes" => bytes.bytesize, "device" => stat.dev, "inode" => stat.ino}
      prior = @evidence[relative]
      if prior
        require!(prior.slice("sha256", "bytes") == binding.slice("sha256", "bytes"),
                 "evidence changed between reads #{relative}")
      else
        @evidence[relative] = binding
      end
      bytes
    end

    def read_json_evidence(relative, label)
      parse_json(read_evidence(relative, label), label)
    end

    def read_target(relative)
      path = safe_path(relative)
      bytes, stat = stable_regular_read(path, "status target #{relative}")
      snapshot = {
        original: bytes,
        original_sha256: Digest::SHA256.hexdigest(bytes),
        bytes: bytes.bytesize,
        mode: stat.mode & 0o777,
        device: stat.dev,
        inode: stat.ino
      }
      [bytes.dup.force_encoding(Encoding::UTF_8), snapshot]
    end

    def stable_regular_read(path, label)
      stat_before = path.lstat
      require!(stat_before.file? && !stat_before.symlink?, "#{label} is not a regular non-symlink file")
      bytes = path.binread
      stat_after = path.lstat
      require!(stat_before.dev == stat_after.dev && stat_before.ino == stat_after.ino &&
               stat_after.size == bytes.bytesize,
               "#{label} changed while being read")
      [bytes, stat_after]
    rescue Errno::ENOENT
      raise ContractError, "missing required prerequisite #{label}: #{path.relative_path_from(root)}"
    end

    def parse_json(bytes, label)
      JSON.parse(bytes)
    rescue JSON::ParserError => error
      raise ContractError, "invalid JSON #{label}: #{error.message}"
    end

    def evidence_binding(relative)
      row = @evidence.fetch(relative)
      row.slice("path", "sha256", "bytes")
    end

    def verify_evidence_unchanged!
      @evidence.each do |relative, row|
        path = safe_path(relative)
        stat = path.lstat
        require!(stat.file? && !stat.symlink?, "evidence ceased to be a regular file #{relative}")
        require!(path.size == row.fetch("bytes") && Digest::SHA256.file(path).hexdigest == row.fetch("sha256"),
                 "evidence drift before status commit #{relative}")
      end
      true
    end

    def verify_bound_artifact!(row, expected_relative, label, require_bytes: false)
      require!(row.is_a?(Hash), "#{label} binding is not an object")
      require!(row.fetch("path") == expected_relative, "#{label} path")
      bytes = read_evidence(expected_relative, label)
      require!(row.fetch("sha256") == Digest::SHA256.hexdigest(bytes), "#{label} SHA-256")
      require!(row.key?("bytes"), "#{label} byte count missing") if require_bytes
      require!(row.fetch("bytes") == bytes.bytesize, "#{label} byte count") if row.key?("bytes")
      bytes
    end

    def verify_unchanged_binding!(row, label)
      verify_bound_artifact!(row, row.fetch("path"), label, require_bytes: true)
    end

    def verify_row_against_bytes!(row, expected_relative, bytes, label)
      require!(row.fetch("path") == expected_relative, "#{label} path")
      require!(row.fetch("sha256") == Digest::SHA256.hexdigest(bytes), "#{label} SHA-256")
      require!(row.fetch("bytes") == bytes.bytesize, "#{label} bytes")
    end

    def validate_embedded_authority!(actual, expected, label)
      require!(actual.keys.sort == AUTHORITY.keys.sort, "#{label} authority key set")
      AUTHORITY.each_key do |role|
        require_same_binding!(actual.fetch(role), expected.fetch(role), "#{label} authority #{role}")
      end
      require!(actual.dig("author_event", "exact_text") == "确认\n", "#{label} exact author text")
    end

    def require_same_binding!(actual, expected, label)
      require!(actual.is_a?(Hash), "#{label} is not a binding")
      %w[path sha256 bytes].each do |key|
        require!(actual.fetch(key) == expected.fetch(key), "#{label} #{key}")
      end
    end

    def validate_execution_boundaries!(boundaries, label)
      require!(boundaries.fetch("fresh_stage4_5_authorized") == false,
               "#{label} fresh Stage 4.5 boundary")
      require!(boundaries.fetch("stage5_or_stage6_authorized") == false,
               "#{label} Stage 5/6 boundary")
      require!(boundaries.fetch("canonical_promotion_authorized") == false,
               "#{label} canonical promotion boundary")
      require!(boundaries.fetch("scientific_producer_enumeration_census_or_result_refresh_authorized") == false,
               "#{label} scientific execution/result boundary")
      require!(boundaries.fetch("route_a_or_route_b_credit_authorized") == false,
               "#{label} Route credit boundary")
      require!(boundaries.fetch("route_or_initial_system_mutation_authorized") == false,
               "#{label} Route/initial-system boundary")
      require!(boundaries.fetch("citation_style") == "natbib numbers sort&compress with plainnat",
               "#{label} citation style boundary")
    end

    def parse_blocks(bytes, label)
      text = bytes.dup.force_encoding(Encoding::UTF_8)
      require_utf8!(text, label)
      pairs = text.scan(/<!--block:(B\d{4})-->\n(.*?)(?=\n<!--block:B\d{4}-->|\z)/m)
      require!(pairs.length == pairs.map(&:first).uniq.length, "#{label} duplicate block marker")
      pairs.to_h
    end

    def normalized_block_text(text)
      lines = text.gsub("\r\n", "\n").split("\n", -1)
      lines.shift while !lines.empty? && lines.first.strip.empty?
      lines.pop while !lines.empty? && lines.last.strip.empty?
      lines.join("\n")
    end

    def marker_free_word_count(bytes)
      text = bytes.dup.force_encoding(Encoding::UTF_8)
      require_utf8!(text, "marker-free word count input")
      text.gsub(/<!--.*?-->/m, " ").split.length
    end

    def safe_path(relative)
      relative_path = Pathname.new(relative)
      require!(!relative_path.absolute? && relative_path.cleanpath.to_s == relative &&
               relative_path.each_filename.none? { |part| part == ".." },
               "unsafe repository-relative path #{relative.inspect}")
      root / relative_path
    end

    def read_target_snapshot(path, label)
      bytes, stat = stable_regular_read(path, label)
      {original: bytes, original_sha256: Digest::SHA256.hexdigest(bytes), bytes: bytes.bytesize,
       mode: stat.mode & 0o777, device: stat.dev, inode: stat.ino}
    end

    def replacement_row(snapshot, replacement)
      bytes = replacement.encode(Encoding::UTF_8)
      snapshot.merge(replacement: bytes, replacement_sha256: Digest::SHA256.hexdigest(bytes))
    end

    def assert_snapshot!(path, row, phase)
      stat = path.lstat
      require!(stat.file? && !stat.symlink?, "#{phase}: target is not regular #{path}")
      require!(stat.dev == row.fetch(:device) && stat.ino == row.fetch(:inode) &&
               stat.size == row.fetch(:bytes) && Digest::SHA256.file(path).hexdigest == row.fetch(:original_sha256),
               "#{phase}: status target drift #{path.relative_path_from(root)}")
    rescue Errno::ENOENT
      raise ContractError, "#{phase}: status target disappeared #{path.relative_path_from(root)}"
    end

    def replace_range(raw, start_at, boundary_at, replacement)
      require!(boundary_at > start_at, "replacement boundary does not follow start")
      prefix = raw.byteslice(0, start_at)
      suffix = raw.byteslice(boundary_at, raw.bytesize - boundary_at)
      "#{prefix}#{replacement.rstrip}\n\n#{suffix}"
    end

    def heading_positions(text, pattern)
      positions = []
      offset = 0
      text.each_line do |line|
        stripped = line.delete_suffix("\n").delete_suffix("\r")
        positions << [offset, stripped] if stripped.match?(pattern)
        offset += line.bytesize
      end
      positions
    end

    def byte_index(text, token)
      text.b.index(token.b)
    end

    def require_utf8!(text, label)
      require!(text.valid_encoding?, "#{label} is not valid UTF-8")
    end

    def require_count!(text, token, expected, label)
      actual = text.scan(Regexp.new(Regexp.escape(token))).length
      require!(actual == expected, "#{label}: expected #{expected}, found #{actual}")
    end

    def relative_link(document_relative, target_relative)
      Pathname.new(target_relative).relative_path_from(Pathname.new(document_relative).dirname).to_s
    end

    def format_delta(value)
      value.positive? ? "+#{value}" : value.to_s
    end

    def fsync_directories(directories)
      directories.uniq.each do |directory|
        File.open(directory.to_s, File::RDONLY) { |handle| handle.fsync }
      end
    end

    def require!(condition, message)
      raise ContractError, message unless condition
    end
  end

  module_function

  def run_fixture_self_test
    Dir.mktmpdir("round10-status-doc-fixture.") do |directory|
      root = Pathname.new(directory)
      updater = Updater.new(root)
      originals = {}
      replacements = {}

      root_raw = <<~MD
        # Fixture root

        #{OLD_ROOT_MARKER}

        stale root status

        #{ROOT_HISTORY_BOUNDARY}

        historical root bytes
      MD
      root.join("README.md").write(root_raw)
      originals["README.md"] = root_raw.b

      PAPER_CONFIGS.each do |paper_id, config|
        paper_dir = root / "papers" / config.fetch(:slug)
        notes = paper_dir / "notes"
        notes.mkpath
        paper_raw = <<~MD
          # #{paper_id}

          ## Current status

          stale paper status

          #{config.fetch(:first_history)}

          historical paper bytes
        MD
        pipeline_raw = <<~MD
          # #{paper_id} old pipeline state

          stale pipeline status

          #{PIPELINE_HISTORY_BOUNDARY}

          historical pipeline bytes
        MD
        paper_relative = "papers/#{config.fetch(:slug)}/README.md"
        pipeline_relative = "papers/#{config.fetch(:slug)}/notes/pipeline_state.md"
        (root / paper_relative).write(paper_raw)
        (root / pipeline_relative).write(pipeline_raw)
        originals[paper_relative] = paper_raw.b
        originals[pipeline_relative] = pipeline_raw.b
      end

      root_new = updater.rewrite_root_document(root_raw, "#{NEW_MARKER}\n\nfixture root replacement")
      snapshot = updater.send(:read_target_snapshot, root / "README.md", "fixture root")
      replacements["README.md"] = updater.send(:replacement_row, snapshot, root_new)
      PAPER_CONFIGS.each do |paper_id, config|
        paper_relative = "papers/#{config.fetch(:slug)}/README.md"
        pipeline_relative = "papers/#{config.fetch(:slug)}/notes/pipeline_state.md"
        paper_raw = (root / paper_relative).read
        pipeline_raw = (root / pipeline_relative).read
        paper_new = updater.rewrite_paper_readme(
          paper_raw, config, "\n#{NEW_MARKER}\n\nfixture #{paper_id} replacement"
        )
        pipeline_new = updater.rewrite_pipeline_state(
          pipeline_raw, config, "# #{paper_id} pipeline state\n\n#{NEW_MARKER}\n\nfixture replacement"
        )
        replacements[paper_relative] = updater.send(
          :replacement_row,
          updater.send(:read_target_snapshot, root / paper_relative, "fixture paper"),
          paper_new
        )
        replacements[pipeline_relative] = updater.send(
          :replacement_row,
          updater.send(:read_target_snapshot, root / pipeline_relative, "fixture pipeline"),
          pipeline_new
        )
      end

      raise "fixture replacement count" unless replacements.length == 11
      updater.atomic_replace_all!(replacements)
      replacements.each do |relative, row|
        actual = (root / relative).binread
        next if actual == row.fetch(:replacement).b

        raise "fixture commit mismatch #{relative}: " \
              "actual=#{Digest::SHA256.hexdigest(actual)}/#{actual.bytesize} " \
              "expected=#{row.fetch(:replacement_sha256)}/#{row.fetch(:replacement).bytesize}"
      end

      originals.each { |relative, bytes| (root / relative).binwrite(bytes) }
      rollback_replacements = replacements.to_h do |relative, row|
        snapshot = updater.send(:read_target_snapshot, root / relative, "fixture rollback input")
        [relative, updater.send(:replacement_row, snapshot, row.fetch(:replacement))]
      end
      begin
        updater.atomic_replace_all!(rollback_replacements, fail_after: 5)
        raise "fixture failure injection did not fail"
      rescue ContractError => error
        raise unless error.message.include?("injected fixture failure")
      end
      originals.each do |relative, bytes|
        raise "fixture rollback mismatch #{relative}" unless (root / relative).binread == bytes.b
      end

      ambiguous = root_raw.sub(ROOT_HISTORY_BOUNDARY,
                               "#{ROOT_HISTORY_BOUNDARY}\n\n#{ROOT_HISTORY_BOUNDARY}")
      begin
        updater.rewrite_root_document(ambiguous, "#{NEW_MARKER}\nfixture")
        raise "fixture duplicate boundary was accepted"
      rescue ContractError => error
        raise unless error.message.include?("expected 1, found 2")
      end

      leftovers = Dir.glob(root.join("**/{.*round10-status*,*.round10-status-stage*}"),
                           File::FNM_DOTMATCH).reject { |path| [".", ".."].include?(File.basename(path)) }
      raise "fixture left transaction debris: #{leftovers.join(', ')}" unless leftovers.empty?
    end
    puts "ROUND10_EXACT_STATUS_DOCS_FIXTURE_PASS: boundaries, 11-file commit, and injected rollback"
    true
  end
end

if $PROGRAM_NAME == __FILE__
  options = {root: Round10ExactConfirmationStatusDocs::DEFAULT_ROOT, mode: :apply}
  selected_modes = []
  parser = OptionParser.new do |opts|
    opts.banner = "Usage: ruby #{File.basename(__FILE__)} [--check-only|--apply|--self-test] [--root PATH]"
    opts.on("--check-only", "Validate all prerequisites and render all 11 replacements without writing") do
      options[:mode] = :check
      selected_modes << :check
    end
    opts.on("--apply", "Apply the validated 11-document transaction (default mode)") do
      options[:mode] = :apply
      selected_modes << :apply
    end
    opts.on("--self-test", "Run isolated boundary/transaction fixture tests only") do
      options[:mode] = :self_test
      selected_modes << :self_test
    end
    opts.on("--root PATH", "Repository root (defaults to the parent of tools/)") do |path|
      options[:root] = Pathname.new(path)
    end
  end

  begin
    parser.parse!(ARGV)
    raise Round10ExactConfirmationStatusDocs::ContractError,
          "choose at most one of --check-only, --apply, and --self-test" if selected_modes.uniq.length > 1
    raise Round10ExactConfirmationStatusDocs::ContractError,
          "unknown positional arguments: #{ARGV.join(' ')}" unless ARGV.empty?

    if options.fetch(:mode) == :self_test
      Round10ExactConfirmationStatusDocs.run_fixture_self_test
    else
      Round10ExactConfirmationStatusDocs::Updater.new(options.fetch(:root)).run(
        check_only: options.fetch(:mode) == :check
      )
    end
  rescue Round10ExactConfirmationStatusDocs::ContractError, KeyError, TypeError => error
    warn "ROUND10_EXACT_STATUS_DOCS_FAIL: #{error.message}"
    exit 1
  end
end
