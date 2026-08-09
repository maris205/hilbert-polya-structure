// R401-VAL-L3-A1: prospective formal branch-tube cell evaluator.
//
// This source implements only the closed evaluator ABI.  It is intentionally
// not a scheduler, does not compile itself, does not publish an archive, and
// cannot assign a component, milestone, theorem, or final status.  A future
// accepted freeze must bind the persistent binary and the complete CAPD
// machine chain before any production dispatch is permitted.
//
// Exact invocation (twelve strings including argv[0]):
//   binary bits eps_lo eps_hi qm_lo qm_hi qp_lo qp_hi pm_lo pm_hi T_lo T_hi

// Exit/status namespace:
//   0  BRANCH_CELL_CERTIFIED
//   2  BRANCH_TUBE_UNRESOLVED
//   3  BRANCH_FLOW_FAIL
//   4  BRANCH_TUBE_VIOLATION
//   5  INVALID_BRANCH_PROOF_CONTRACT

// A violation is emitted only when a CAPD phase enclosure has a rigorous
// lower bound at or above 0.04^2.  Failure to prove a strict upper bound is
// unresolved, never a violation.

#include <cctype>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

#include "capd/capdlib.h"
#include "capd/mpcapdlib.h"
#include "capd/dynsys/MpStepControl.h"
#include "capd/dynsys/OdeSolver.hpp"
#include "capd/poincare/TimeMap.hpp"

using namespace capd;
using namespace std;

using BranchTubeMpSolverA1 = capd::dynsys::OdeSolver<
    capd::MpIMap,
    capd::dynsys::MpLastTermsStepControl>;
using BranchTubeMpTimeMapA1 = capd::poincare::TimeMap<BranchTubeMpSolverA1>;

namespace {

constexpr int kPhaseGrid = 64;
constexpr int kTaylorOrder = 24;

enum class EvaluatorStatus {
  kCertified,
  kUnresolved,
  kFlowFail,
  kViolation,
  kInvalidContract,
};

const char* status_name(EvaluatorStatus status) {
  switch (status) {
    case EvaluatorStatus::kCertified:
      return "BRANCH_CELL_CERTIFIED";
    case EvaluatorStatus::kUnresolved:
      return "BRANCH_TUBE_UNRESOLVED";
    case EvaluatorStatus::kFlowFail:
      return "BRANCH_FLOW_FAIL";
    case EvaluatorStatus::kViolation:
      return "BRANCH_TUBE_VIOLATION";
    case EvaluatorStatus::kInvalidContract:
      return "INVALID_BRANCH_PROOF_CONTRACT";
  }
  return "INVALID_BRANCH_PROOF_CONTRACT";
}

int status_code(EvaluatorStatus status) {
  switch (status) {
    case EvaluatorStatus::kCertified:
      return 0;
    case EvaluatorStatus::kUnresolved:
      return 2;
    case EvaluatorStatus::kFlowFail:
      return 3;
    case EvaluatorStatus::kViolation:
      return 4;
    case EvaluatorStatus::kInvalidContract:
      return 5;
  }
  return 5;
}

void emit_common_header() {
  cout << "protocol_id=R401-VAL-L3-A1\n";
  cout << "artifact_role=BRANCH_CELL_EVALUATOR_TRANSCRIPT\n";
  cout << "authority=PRODUCER_ONLY\n";
  cout << "scientific_licensing_enabled=false\n";
  cout << "dispatch_authorized_by_evaluator=false\n";
  cout << "component_status=null\n";
  cout << "milestone_status=null\n";
  cout << "theorem_status=null\n";
  cout << "final_status=null\n";
  cout << "claim_boundary=accepted-branch complete-period tube cell only\n";
}

int emit_terminal_status(EvaluatorStatus status) {
  // Exactly one status line is emitted by every ordinary exit path.
  cout << "status=" << status_name(status) << "\n";
  return status_code(status);
}

bool is_decimal_token(const string& token) {
  // Closed, locale-independent decimal grammar.  CAPD receives the original
  // bytes only after this lexical check; NaN, Infinity, whitespace, commas,
  // and trailing junk are all rejected.
  if (token.empty() || token.size() > 512) {
    return false;
  }
  size_t index = 0;
  if (token[index] == '+' || token[index] == '-') {
    ++index;
    if (index == token.size()) {
      return false;
    }
  }
  bool integral_digit = false;
  while (index < token.size() && isdigit(static_cast<unsigned char>(token[index]))) {
    integral_digit = true;
    ++index;
  }
  bool fractional_digit = false;
  if (index < token.size() && token[index] == '.') {
    ++index;
    while (index < token.size() &&
           isdigit(static_cast<unsigned char>(token[index]))) {
      fractional_digit = true;
      ++index;
    }
  }
  if (!integral_digit && !fractional_digit) {
    return false;
  }
  if (index < token.size() && (token[index] == 'e' || token[index] == 'E')) {
    ++index;
    if (index < token.size() && (token[index] == '+' || token[index] == '-')) {
      ++index;
    }
    bool exponent_digit = false;
    while (index < token.size() &&
           isdigit(static_cast<unsigned char>(token[index]))) {
      exponent_digit = true;
      ++index;
    }
    if (!exponent_digit) {
      return false;
    }
  }
  return index == token.size();
}

bool is_canonical_argv0(const string& token) {
  if (token.empty() || token.size() > 4096 || token.front() != '/') {
    return false;
  }
  for (unsigned char byte : token) {
    if (byte < 0x20 || byte == 0x7f || byte == '\\') {
      return false;
    }
  }
  return token.find("/../") == string::npos &&
         token.find("/./") == string::npos &&
         token.find("//") == string::npos;
}

int parse_precision(const string& token) {
  if (token != "128" && token != "256") {
    throw invalid_argument("precision token is outside the closed ABI");
  }
  return token == "128" ? 128 : 256;
}

MpInterval input_interval(const char* lower, const char* upper) {
  if (!is_decimal_token(lower) || !is_decimal_token(upper)) {
    throw invalid_argument("noncanonical decimal endpoint");
  }
  const MpInterval result(lower, upper);
  if (result.leftBound() > result.rightBound()) {
    throw invalid_argument("reversed interval endpoint pair");
  }
  return result;
}

void emit_exact_input_echo(int argc, char** argv) {
  cout << "input_argv_count=" << argc << "\n";
  for (int index = 0; index < argc; ++index) {
    cout << "input_arg_" << setw(2) << setfill('0') << index << "="
         << argv[index] << "\n";
  }
  cout << setfill(' ');
}

}  // namespace

int main(int argc, char** argv) {
  emit_common_header();

  if (argc != 12) {
    cout << "contract_error=ARGUMENT_COUNT\n";
    return emit_terminal_status(EvaluatorStatus::kInvalidContract);
  }

  int bits = 0;
  MpInterval epsilon;
  MpInterval q_slow;
  MpInterval q_fast;
  MpInterval p_slow;
  MpInterval period;
  try {
    if (!is_canonical_argv0(argv[0])) {
      throw invalid_argument("argv0 is outside the closed path grammar");
    }
    bits = parse_precision(argv[1]);
    MpFloat::setDefaultPrecision(bits);
    epsilon = input_interval(argv[2], argv[3]);
    q_slow = input_interval(argv[4], argv[5]);
    q_fast = input_interval(argv[6], argv[7]);
    p_slow = input_interval(argv[8], argv[9]);
    period = input_interval(argv[10], argv[11]);
    if (period.leftBound() <= MpFloat(0)) {
      throw invalid_argument("period interval is not strictly positive");
    }
  } catch (const exception&) {
    cout << "contract_error=INVALID_INPUT_TOKEN_OR_INTERVAL\n";
    return emit_terminal_status(EvaluatorStatus::kInvalidContract);
  } catch (...) {
    cout << "contract_error=UNKNOWN_INPUT_FAILURE\n";
    return emit_terminal_status(EvaluatorStatus::kInvalidContract);
  }

  cout << setprecision(bits == 128 ? 45 : 84);
  emit_exact_input_echo(argc, argv);
  cout << "precision_bits=" << bits << "\n";
  cout << "taylor_order=" << kTaylorOrder << "\n";
  cout << "tolerance=" << (bits == 128 ? "1e-30" : "1e-60") << "\n";
  cout << "phase_grid=" << kPhaseGrid << "\n";

  try {
    const MpInterval a = MpInterval(51) / MpInterval(50);
    const MpInterval c = 2 * (sqrt(1 + a) - 1);
    const MpInterval discriminant = c * sqrt(c * c + 4);
    const MpInterval lambda_slow = (c * c + 2 - discriminant) / 2;
    const MpInterval lambda_fast = (c * c + 2 + discriminant) / 2;
    const MpInterval slow_raw_1 = 1 - lambda_slow;
    const MpInterval slow_raw_2 = -c;
    const MpInterval fast_raw_1 = lambda_fast - 1;
    const MpInterval fast_raw_2 = c;
    const MpInterval slow_norm = sqrt(
        slow_raw_1 * slow_raw_1 + slow_raw_2 * slow_raw_2);
    const MpInterval fast_norm = sqrt(
        fast_raw_1 * fast_raw_1 + fast_raw_2 * fast_raw_2);
    const MpInterval os1 = slow_raw_1 / slow_norm;
    const MpInterval os2 = slow_raw_2 / slow_norm;
    const MpInterval of1 = fast_raw_1 / fast_norm;
    const MpInterval of2 = fast_raw_2 / fast_norm;
    const MpInterval pi = 4 * atan(MpInterval(1));
    const MpInterval omega_slow = 2 * pi * sqrt(lambda_slow);

    const string q1 = "(os1*qm+of1*qp)";
    const string q2 = "(os2*qm+of2*qp)";
    const string w1 = "(-c*" + q1 + "-" + q2 + "-a*eps*" + q1 + "^2)";
    const string exponent = "exp(pi*eps*eps*(" + w1 + "^2+" + q1 + "^2))";
    const string force1 = "(-4*pi*pi*" + exponent + "*((-c-2*a*eps*" + q1
        + ")*" + w1 + "+" + q1 + "))";
    const string force2 = "(4*pi*pi*" + exponent + "*" + w1 + ")";
    const string field_description =
        "par:a,c,os1,os2,of1,of2,pi;"
        "var:qm,qp,pm,pp,eps,per;"
        "fun:per*pm,per*pp,per*(os1*" + force1 + "+os2*" + force2
        + "),per*(of1*" + force1 + "+of2*" + force2 + "),0,0;";
    MpIMap vector_field(field_description);
    vector_field.setParameter("a", a);
    vector_field.setParameter("c", c);
    vector_field.setParameter("os1", os1);
    vector_field.setParameter("os2", os2);
    vector_field.setParameter("of1", of1);
    vector_field.setParameter("of2", of2);
    vector_field.setParameter("pi", pi);

    MpIVector initial_box(6);
    initial_box[0] = q_slow;
    initial_box[1] = q_fast;
    initial_box[2] = p_slow;
    initial_box[3] = MpInterval(0);
    initial_box[4] = epsilon;
    initial_box[5] = period;

    const char* tolerance_text = bits == 128 ? "1e-30" : "1e-60";
    const MpFloat tolerance(tolerance_text);
    const MpInterval tube_radius_sq = MpInterval(1) / MpInterval(625);

    cout << "epsilon=" << initial_box[4] << "\n";
    cout << "root_box={" << initial_box[0] << "," << initial_box[1]
         << "," << initial_box[2] << "," << initial_box[5] << "}\n";
    cout << "initial_state_box=" << initial_box << "\n";
    cout << "omega_slow=" << omega_slow << "\n";
    cout << "tube_radius_sq=" << tube_radius_sq << "\n";

    BranchTubeMpSolverA1 solver(vector_field, kTaylorOrder);
    solver.setAbsoluteTolerance(tolerance);
    solver.setRelativeTolerance(tolerance);
    BranchTubeMpTimeMapA1 time_map(solver);
    MpC0Rect2Set flow_set(initial_box);
    BranchTubeMpTimeMapA1::SolutionCurve solution(MpInterval(0));
    const MpIVector terminal_box = time_map(MpInterval(1), flow_set, solution);

    bool every_segment_inside = true;
    bool any_segment_violation = false;
    MpFloat maximum_rslow_sq_upper(0);
    for (int index = 0; index < kPhaseGrid; ++index) {
      const MpInterval phase = intervalHull(
          MpInterval(index) / MpInterval(kPhaseGrid),
          MpInterval(index + 1) / MpInterval(kPhaseGrid));
      const MpIVector state = solution(phase);
      const MpInterval rslow_sq =
          sqr(omega_slow * state[0]) + sqr(state[2]);
      const MpInterval margin_sq = tube_radius_sq - rslow_sq;
      const bool segment_inside =
          rslow_sq.rightBound() < tube_radius_sq.leftBound();
      const bool segment_violation =
          rslow_sq.leftBound() >= tube_radius_sq.rightBound();
      every_segment_inside = every_segment_inside && segment_inside;
      any_segment_violation = any_segment_violation || segment_violation;
      if (rslow_sq.rightBound() > maximum_rslow_sq_upper) {
        maximum_rslow_sq_upper = rslow_sq.rightBound();
      }
      cout << "segment_" << setw(3) << setfill('0') << index
           << "_phase=" << phase << "\n";
      cout << "segment_" << setw(3) << setfill('0') << index
           << "_state=" << state << "\n";
      cout << "segment_" << setw(3) << setfill('0') << index
           << "_rslow_sq=" << rslow_sq << "\n";
      cout << "segment_" << setw(3) << setfill('0') << index
           << "_margin_sq=" << margin_sq << "\n";
      cout << "segment_" << setw(3) << setfill('0') << index
           << "_relation="
           << (segment_inside
                   ? "INSIDE"
                   : (segment_violation ? "VIOLATION" : "UNRESOLVED"))
           << "\n";
      cout << setfill(' ');
    }

    cout << "solution_left_domain=" << solution.getLeftDomain() << "\n";
    cout << "solution_right_domain=" << solution.getRightDomain() << "\n";
    cout << "solution_piece_count=" << solution.getNumberOfPieces() << "\n";
    cout << "terminal_state_box=" << terminal_box << "\n";
    cout << "maximum_rslow_sq_upper="
         << MpInterval(maximum_rslow_sq_upper) << "\n";
    cout << "all_segments_inside=" << every_segment_inside << "\n";
    cout << "lower_bound_violation_witness=" << any_segment_violation << "\n";

    if (every_segment_inside) {
      return emit_terminal_status(EvaluatorStatus::kCertified);
    }
    if (any_segment_violation) {
      return emit_terminal_status(EvaluatorStatus::kViolation);
    }
    return emit_terminal_status(EvaluatorStatus::kUnresolved);
  } catch (const exception&) {
    cout << "flow_error=CAPD_COMPLETE_PERIOD_ENCLOSURE_FAILED\n";
    return emit_terminal_status(EvaluatorStatus::kFlowFail);
  } catch (...) {
    cout << "flow_error=UNKNOWN_CAPD_FAILURE\n";
    return emit_terminal_status(EvaluatorStatus::kFlowFail);
  }
}
