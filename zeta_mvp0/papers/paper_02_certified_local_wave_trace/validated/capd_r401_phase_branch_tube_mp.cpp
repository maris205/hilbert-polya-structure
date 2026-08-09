// R401-VAL-L3-BT-S0: NON-LICENSING dense-output branch-tube prototype.
//
// Arguments:
//   bits eps_lo eps_hi qm_lo qm_hi qp_lo qp_hi pm_lo pm_hi T_lo T_hi
//
// The input box is taken from an already accepted A4.12 primary Krawczyk
// certificate.  It is embedded in the positive turning section P_+=0 and
// propagated for one normalized period s in [0,1].  CAPD's rigorous
// multiprecision SolutionCurve is evaluated on a fixed 64-cell dyadic phase
// grid.  This prototype checks only that the distinguished branch enclosure
// remains inside r_- < 0.04.  It does not certify phase completeness for an
// arbitrary candidate orbit, a global shell cover, or delta_tr.

#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>

#include "capd/capdlib.h"
#include "capd/mpcapdlib.h"
#include "capd/dynsys/MpStepControl.h"
#include "capd/dynsys/OdeSolver.hpp"
#include "capd/poincare/TimeMap.hpp"

using namespace capd;
using namespace std;

using BranchTubeMpSolver = capd::dynsys::OdeSolver<
    capd::MpIMap,
    capd::dynsys::MpLastTermsStepControl>;
using BranchTubeMpTimeMap = capd::poincare::TimeMap<BranchTubeMpSolver>;

int main(int argc, char** argv) {
  if (argc != 12) {
    throw invalid_argument(
        "expected: bits eps_lo eps_hi qm_lo qm_hi qp_lo qp_hi "
        "pm_lo pm_hi T_lo T_hi");
  }

  const int bits = stoi(argv[1]);
  if (bits != 128 && bits != 256) {
    throw invalid_argument("precision must be 128 or 256 bits");
  }
  MpFloat::setDefaultPrecision(bits);
  cout << setprecision(bits == 128 ? 45 : 84);

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
  initial_box[0] = MpInterval(argv[4], argv[5]);
  initial_box[1] = MpInterval(argv[6], argv[7]);
  initial_box[2] = MpInterval(argv[8], argv[9]);
  initial_box[3] = MpInterval(0);
  initial_box[4] = MpInterval(argv[2], argv[3]);
  initial_box[5] = MpInterval(argv[10], argv[11]);

  const int taylor_order = 24;
  const char* tolerance_text = bits == 128 ? "1e-30" : "1e-60";
  const MpFloat tolerance(tolerance_text);
  const int phase_grid = 64;
  const MpInterval tube_radius_sq = MpInterval(1) / MpInterval(625);

  cout << "licensing=NON_LICENSING\n";
  cout << "protocol_id=R401-VAL-L3-BT-S0\n";
  cout << "milestone_status=null\n";
  cout << "theorem_status=null\n";
  cout << "final_status=null\n";
  cout << "precision_bits=" << bits << "\n";
  cout << "taylor_order=" << taylor_order << "\n";
  cout << "tolerance=" << tolerance_text << "\n";
  cout << "phase_grid=" << phase_grid << "\n";
  cout << "epsilon=" << initial_box[4] << "\n";
  cout << "root_box={" << initial_box[0] << "," << initial_box[1]
       << "," << initial_box[2] << "," << initial_box[5] << "}\n";
  cout << "initial_state_box=" << initial_box << "\n";
  cout << "omega_slow=" << omega_slow << "\n";
  cout << "tube_radius_sq=" << tube_radius_sq << "\n";

  try {
    BranchTubeMpSolver solver(vector_field, taylor_order);
    solver.setAbsoluteTolerance(tolerance);
    solver.setRelativeTolerance(tolerance);
    BranchTubeMpTimeMap time_map(solver);
    MpC0Rect2Set flow_set(initial_box);
    BranchTubeMpTimeMap::SolutionCurve solution(MpInterval(0));
    const MpIVector terminal_box = time_map(MpInterval(1), flow_set, solution);

    bool all_segments_inside = true;
    MpFloat maximum_rslow_sq_upper(0);
    for (int index = 0; index < phase_grid; ++index) {
      const MpInterval phase = intervalHull(
          MpInterval(index) / MpInterval(phase_grid),
          MpInterval(index + 1) / MpInterval(phase_grid));
      const MpIVector state = solution(phase);
      const MpInterval rslow_sq =
          sqr(omega_slow * state[0]) + sqr(state[2]);
      const MpInterval margin_sq = tube_radius_sq - rslow_sq;
      const bool segment_inside = margin_sq.leftBound() > MpFloat(0);
      all_segments_inside = all_segments_inside && segment_inside;
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
           << "_inside=" << segment_inside << "\n";
      cout << setfill(' ');
    }

    cout << "solution_left_domain=" << solution.getLeftDomain() << "\n";
    cout << "solution_right_domain=" << solution.getRightDomain() << "\n";
    cout << "solution_piece_count=" << solution.getNumberOfPieces() << "\n";
    cout << "terminal_state_box=" << terminal_box << "\n";
    cout << "maximum_rslow_sq_upper="
         << MpInterval(maximum_rslow_sq_upper) << "\n";
    cout << "all_segments_inside=" << all_segments_inside << "\n";
    cout << "status="
         << (all_segments_inside
                 ? "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE"
                 : "INCONCLUSIVE_BRANCH_TUBE_SMOKE")
         << "\n";
    return all_segments_inside ? EXIT_SUCCESS : 2;
  } catch (const exception& error) {
    cout << "flow_error=" << error.what() << "\n";
    cout << "status=FLOW_FAIL\n";
    return 3;
  }
}
