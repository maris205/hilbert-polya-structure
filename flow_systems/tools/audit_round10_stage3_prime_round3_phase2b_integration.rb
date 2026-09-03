#!/usr/bin/env ruby
# frozen_string_literal: true

ARGV.unshift("2026-09-03T15:40:00Z")
ARGV.unshift("--generated-at")
ARGV.unshift("P29,P32")
ARGV.unshift("--papers")
ARGV.unshift("round3")
ARGV.unshift("--round")
load File.expand_path("audit_round10_stage3_prime_round2_phase2b_integration.rb", __dir__)
