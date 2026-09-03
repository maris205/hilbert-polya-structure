#!/usr/bin/env ruby
# frozen_string_literal: true

# Round-3 convenience entry point. The underlying builder retains Round 2 as
# its default so earlier invocations remain byte-for-byte behavior compatible.
ARGV.unshift("P29,P32,P33")
ARGV.unshift("--papers")
ARGV.unshift("round3")
ARGV.unshift("--round")
load File.expand_path("build_round10_stage3_prime_round2_traceability.rb", __dir__)
