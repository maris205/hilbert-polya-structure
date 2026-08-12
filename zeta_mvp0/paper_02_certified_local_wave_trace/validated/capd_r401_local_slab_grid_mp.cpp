// R401-VAL-L1: general multiprecision CAPD parameter-slab verifier.
//
// Arguments:
//   bits eps_lo eps_hi qminus qplus pminus period
//        r_qminus r_qplus r_pminus r_period
//
// All decimal strings are parsed as outward intervals.  The program returns
// success exactly when the parameterized Krawczyk image is strictly inside
// the supplied four-dimensional root box.

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

using GridMpSolver = capd::dynsys::OdeSolver<
    capd::MpIMap,
    capd::dynsys::MpLastTermsStepControl>;
using GridMpTimeMap = capd::poincare::TimeMap<GridMpSolver>;

static MpInterval point(const string& value) {
  return MpInterval(value, value);
}

static MpInterval symmetric_radius(const string& value) {
  return MpInterval("-" + value, value);
}

int main(int argc, char** argv) {
  if (argc != 12) {
    throw invalid_argument(
        "expected: bits eps_lo eps_hi qm qp pm T rqm rqp rpm rT");
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

  const MpInterval epsilon(argv[2], argv[3]);
  MpIVector X(4);
  X[0] = point(argv[4]) + symmetric_radius(argv[8]);
  X[1] = point(argv[5]) + symmetric_radius(argv[9]);
  X[2] = point(argv[6]) + symmetric_radius(argv[10]);
  X[3] = point(argv[7]) + symmetric_radius(argv[11]);
  const MpIVector x_bar = midVector(X);

  auto embed = [&](const MpIVector& root) {
    MpIVector state(6);
    state[0] = root[0];
    state[1] = root[1];
    state[2] = root[2];
    state[3] = 0;
    state[4] = epsilon;
    state[5] = root[3];
    return state;
  };

  auto energy_and_gradient = [&](const MpIVector& root, MpIVector& gradient) {
    const MpInterval physical_q1 = os1 * root[0] + of1 * root[1];
    const MpInterval physical_q2 = os2 * root[0] + of2 * root[1];
    const MpInterval warped_1 = -c * physical_q1 - physical_q2
        - a * epsilon * physical_q1 * physical_q1;
    const MpInterval warped_2 = physical_q1;
    const MpInterval squared_radius = warped_1 * warped_1 + warped_2 * warped_2;
    const MpInterval s = pi * epsilon * epsilon * squared_radius;
    if (s.leftBound() < MpFloat(0)) {
      throw runtime_error("nonnegative exprel argument gate failed");
    }
    MpInterval term(1), exprel(1), factorial(1);
    for (int degree = 1; degree <= 12; ++degree) {
      term = term * s / MpInterval(degree + 1);
      exprel += term;
    }
    for (int factor = 2; factor <= 14; ++factor) {
      factorial *= MpInterval(factor);
    }
    exprel += MpInterval(0, 1) * exp(s) * power(s, 13) / factorial;
    const MpInterval energy = root[2] * root[2] / 2
        + 2 * pi * pi * squared_radius * exprel;
    const MpInterval j11 = -c - 2 * a * epsilon * physical_q1;
    const MpInterval exponential_value = exp(s);
    const MpInterval g1 = 4 * pi * pi * exponential_value
        * (j11 * warped_1 + warped_2);
    const MpInterval g2 = -4 * pi * pi * exponential_value * warped_1;
    gradient.resize(4);
    gradient[0] = os1 * g1 + os2 * g2;
    gradient[1] = of1 * g1 + of2 * g2;
    gradient[2] = root[2];
    gradient[3] = 0;
    return energy;
  };

  const int taylor_order = 24;
  const char* tolerance_text = bits == 128 ? "1e-30" : "1e-60";
  const MpFloat tolerance(tolerance_text);

  GridMpSolver solver(vector_field, taylor_order);
  solver.setAbsoluteTolerance(tolerance);
  solver.setRelativeTolerance(tolerance);
  GridMpTimeMap time_map(solver);
  const MpIVector state_box = embed(X);
  MpC1Rect2Set flow_set(state_box);
  const MpIVector terminal_box = time_map(MpInterval(1), flow_set);
  const MpIMatrix monodromy_box = flow_set;

  GridMpSolver center_solver(vector_field, taylor_order);
  center_solver.setAbsoluteTolerance(tolerance);
  center_solver.setRelativeTolerance(tolerance);
  GridMpTimeMap center_time_map(center_solver);
  const MpIVector center_state = embed(x_bar);
  MpC1Rect2Set center_set(center_state);
  const MpIVector center_terminal = center_time_map(MpInterval(1), center_set);

  MpIVector center_gradient;
  MpIVector box_gradient;
  MpIVector F_center(4);
  F_center[0] = energy_and_gradient(x_bar, center_gradient) - 1;
  // Krawczyk needs D_x F(X,E), not the derivative at the midpoint.
  // Retaining the full p_minus interval here is essential even though the
  // midpoint value of p_minus is exactly zero.
  energy_and_gradient(X, box_gradient);
  F_center[1] = center_terminal[0] - x_bar[0];
  F_center[2] = center_terminal[2] - x_bar[2];
  F_center[3] = center_terminal[3];

  MpIMatrix J(4, 4);
  const int input_column[4] = {0, 1, 2, 5};
  const int output_row[3] = {0, 2, 3};
  for (int column = 0; column < 4; ++column) {
    J[0][column] = box_gradient[column];
    J[1][column] = monodromy_box[output_row[0]][input_column[column]]
        - (column == 0 ? 1 : 0);
    J[2][column] = monodromy_box[output_row[1]][input_column[column]]
        - (column == 2 ? 1 : 0);
    J[3][column] = monodromy_box[output_row[2]][input_column[column]];
  }

  // Use one fixed point preconditioner in the Krawczyk map.
  const MpIMatrix C = midMatrix(
      capd::matrixAlgorithms::inverseMatrix(midMatrix(J)));
  bool preconditioner_point = true;
  for (int row = 0; row < 4; ++row) {
    for (int column = 0; column < 4; ++column) {
      preconditioner_point = preconditioner_point
          && C[row][column].leftBound() == C[row][column].rightBound();
    }
  }
  const MpIMatrix defect = MpIMatrix::Identity(4) - C * J;
  const MpIVector K = x_bar - C * F_center + defect * (X - x_bar);
  const bool included = subsetInterior(K, X);
  MpIVector defect_row_sums(4);
  bool contraction = true;
  for (int row = 0; row < 4; ++row) {
    defect_row_sums[row] = 0;
    for (int column = 0; column < 4; ++column) {
      defect_row_sums[row] += abs(defect[row][column]);
    }
    contraction = contraction
        && defect_row_sums[row].rightBound() < MpFloat(1);
  }

  const MpInterval phase_interval("0.10", "0.18");
  MpIVector phase_root = X;
  phase_root[1] = phase_interval;
  MpIVector phase_gradient;
  energy_and_gradient(phase_root, phase_gradient);
  const bool phase_gate = subset(X[1], phase_interval)
      && subset(terminal_box[1], phase_interval)
      && phase_gradient[1].leftBound() > MpFloat(0);
  const bool certified = included && contraction && phase_gate
      && preconditioner_point;
  MpIVector left_margin(4), right_margin(4);
  for (int index = 0; index < 4; ++index) {
    left_margin[index] = MpInterval(K[index].leftBound() - X[index].leftBound());
    right_margin[index] = MpInterval(X[index].rightBound() - K[index].rightBound());
  }

  cout << "status=" << (certified ? "PASS_LOCAL_SLAB" : "FAIL") << "\n";
  cout << "precision_bits=" << bits << "\n";
  cout << "epsilon=" << epsilon << "\n";
  cout << "X=" << X << "\n";
  cout << "x_bar=" << x_bar << "\n";
  cout << "K=" << K << "\n";
  cout << "left_margin=" << left_margin << "\n";
  cout << "right_margin=" << right_margin << "\n";
  cout << "subset_interior=" << included << "\n";
  cout << "F_center=" << F_center << "\n";
  cout << "J=" << J << "\n";
  cout << "C=" << C << "\n";
  cout << "preconditioner_point=" << preconditioner_point << "\n";
  cout << "defect=" << defect << "\n";
  cout << "defect_row_sums=" << defect_row_sums << "\n";
  cout << "contraction=" << contraction << "\n";
  cout << "monodromy_box=" << monodromy_box << "\n";
  cout << "phase_interval=" << phase_interval << "\n";
  cout << "initial_qplus=" << X[1] << "\n";
  cout << "terminal_qplus=" << terminal_box[1] << "\n";
  cout << "phase_gradient_qplus=" << phase_gradient[1] << "\n";
  cout << "phase_gate=" << phase_gate << "\n";
  return certified ? EXIT_SUCCESS : EXIT_FAILURE;
}
