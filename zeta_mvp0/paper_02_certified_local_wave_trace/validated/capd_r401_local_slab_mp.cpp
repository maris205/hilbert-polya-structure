// R401-VAL-L0: multiprecision CAPD local-slab implementation smoke.
//
// This program proves only a parameterized Krawczyk inclusion for the local
// four-equation return system on epsilon in [0.099, 0.101].  It does not
// exclude the complement of the root box, build the phase/global cover, or
// certify delta_tr.  CAPD is an external GPLv3 dependency and is not vendored
// in this project.

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

using MpSolver = capd::dynsys::OdeSolver<
    capd::MpIMap,
    capd::dynsys::MpLastTermsStepControl>;
using LocalMpTimeMap = capd::poincare::TimeMap<MpSolver>;

static MpInterval point(const char* value) {
  return MpInterval(value, value);
}

static MpInterval radius(const long numerator, const long denominator) {
  return MpInterval(-numerator, numerator) / MpInterval(denominator);
}

int main(int argc, char** argv) {
  const int bits = argc > 1 ? std::stoi(argv[1]) : 128;
  if (bits != 128 && bits != 256) {
    throw std::invalid_argument("precision must be 128 or 256 bits");
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

  // Keep the state in exact protocol normal coordinates.  Constructing a
  // physical axis-aligned box would discard the Q_-/Q_+ correlations and
  // materially weaken the Lohner enclosure.
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

  // Exact rational/decimal center and root box in protocol normal
  // coordinates (Q_-, Q_+, P_-, T).
  MpIVector X(4);
  X[0] = point("-0.002217614251311155746359014235924058")
      + radius(4, 100000);
  X[1] = point("0.148503551176855185013286874895890763")
      + radius(2, 100000);
  X[2] = radius(8, 100000);
  X[3] = point("0.663569791793793062672019028284358387")
      + radius(2, 100000);
  const MpIVector x_bar = midVector(X);
  const MpInterval epsilon = intervalHull(
      MpInterval(99) / MpInterval(1000),
      MpInterval(101) / MpInterval(1000));

  auto embed = [&](const MpIVector& root, const MpInterval& eps) {
    MpIVector state(6);
    state[0] = root[0];
    state[1] = root[1];
    state[2] = root[2];
    state[3] = 0;
    state[4] = eps;
    state[5] = root[3];
    return state;
  };

  auto energy_and_gradient = [&](const MpIVector& root,
                                 const MpInterval& eps,
                                 MpIVector& gradient) {
    const MpInterval q1 = os1 * root[0] + of1 * root[1];
    const MpInterval q2 = os2 * root[0] + of2 * root[1];
    const MpInterval w1 = -c * q1 - q2 - a * eps * q1 * q1;
    const MpInterval w2 = q1;
    const MpInterval squared_radius = w1 * w1 + w2 * w2;
    const MpInterval s = pi * eps * eps * squared_radius;
    if (s.leftBound() < MpFloat(0)) {
      throw std::runtime_error("nonnegative exprel argument gate failed");
    }
    MpInterval term(1);
    MpInterval exprel(1);
    for (int degree = 1; degree <= 12; ++degree) {
      term = term * s / MpInterval(degree + 1);
      exprel += term;
    }
    MpInterval factorial(1);
    for (int factor = 2; factor <= 14; ++factor) {
      factorial *= MpInterval(factor);
    }
    exprel += MpInterval(0, 1) * exp(s) * power(s, 13) / factorial;
    const MpInterval energy = root[2] * root[2] / 2
        + 2 * pi * pi * squared_radius * exprel;

    const MpInterval j11 = -c - 2 * a * eps * q1;
    const MpInterval exponential = exp(s);
    const MpInterval g1 = 4 * pi * pi * exponential * (j11 * w1 + w2);
    const MpInterval g2 = -4 * pi * pi * exponential * w1;
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

  // Full interval root box: provides D_x F(X,E).
  MpSolver solver(vector_field, taylor_order);
  solver.setAbsoluteTolerance(tolerance);
  solver.setRelativeTolerance(tolerance);
  LocalMpTimeMap time_map(solver);
  MpIVector state_box = embed(X, epsilon);
  MpC1Rect2Set flow_set(state_box);
  const MpIVector terminal_box = time_map(MpInterval(1), flow_set);
  const MpIMatrix monodromy_box = flow_set;

  // Center evaluation retains the complete epsilon slab, as required by the
  // parameterized Krawczyk operator.
  MpSolver center_solver(vector_field, taylor_order);
  center_solver.setAbsoluteTolerance(tolerance);
  center_solver.setRelativeTolerance(tolerance);
  LocalMpTimeMap center_time_map(center_solver);
  const MpIVector center_state = embed(x_bar, epsilon);
  MpC1Rect2Set center_set(center_state);
  const MpIVector center_terminal = center_time_map(MpInterval(1), center_set);

  auto normal_component = [&](const MpIVector& state, const int output) {
    return state[output];
  };

  MpIVector center_gradient;
  MpIVector box_gradient;
  MpIVector F_center(4);
  F_center[0] = energy_and_gradient(x_bar, epsilon, center_gradient) - 1;
  // The Krawczyk derivative enclosure must use the complete root box X.
  // In particular, dH/dp_minus = p_minus is not identically zero merely
  // because the midpoint has p_minus=0.
  energy_and_gradient(X, epsilon, box_gradient);
  F_center[1] = normal_component(center_terminal, 0) - x_bar[0];
  F_center[2] = normal_component(center_terminal, 2) - x_bar[2];
  F_center[3] = normal_component(center_terminal, 3);

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

  // Freeze one point preconditioner.  The outer midMatrix is essential:
  // inverseMatrix on interval point data may acquire rounding width.
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

  // A direct interval infinity-norm bound makes the uniqueness hypothesis
  // explicit instead of relying only on a shorthand Krawczyk theorem.
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

  // Recover the omitted Q_plus return equation from exact energy
  // conservation.  At a zero of the reduced system, all other terminal
  // coordinates agree with their initial values.  If both Q_plus values lie
  // in this interval and dH/dQ_plus is strictly positive there, equality of
  // the energies forces Q_plus(T)=Q_plus(0).
  const MpInterval phase_interval("0.10", "0.18");
  MpIVector phase_root = X;
  phase_root[1] = phase_interval;
  MpIVector phase_gradient;
  energy_and_gradient(phase_root, epsilon, phase_gradient);
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

  cout << "status=" << (certified ? "PASS_LOCAL_SLAB_SMOKE" : "FAIL") << "\n";
  cout << "precision_bits=" << bits << "\n";
  cout << "taylor_order=" << taylor_order << "\n";
  cout << "tolerance=" << tolerance_text << "\n";
  cout << "epsilon=" << epsilon << "\n";
  cout << "a=" << a << "\n";
  cout << "pi=" << pi << "\n";
  cout << "c=" << c << "\n";
  cout << "lambda_slow=" << lambda_slow << "\n";
  cout << "lambda_fast=" << lambda_fast << "\n";
  cout << "e_slow={" << os1 << "," << os2 << "}\n";
  cout << "e_fast={" << of1 << "," << of2 << "}\n";
  cout << "X=" << X << "\n";
  cout << "x_bar=" << x_bar << "\n";
  cout << "state_box=" << state_box << "\n";
  cout << "terminal_box=" << terminal_box << "\n";
  cout << "F_center=" << F_center << "\n";
  cout << "J=" << J << "\n";
  cout << "C=" << C << "\n";
  cout << "preconditioner_point=" << preconditioner_point << "\n";
  cout << "defect=" << defect << "\n";
  cout << "defect_row_sums=" << defect_row_sums << "\n";
  cout << "contraction=" << contraction << "\n";
  cout << "K=" << K << "\n";
  cout << "left_margin=" << left_margin << "\n";
  cout << "right_margin=" << right_margin << "\n";
  cout << "subset_interior=" << included << "\n";
  cout << "phase_interval=" << phase_interval << "\n";
  cout << "initial_qplus=" << X[1] << "\n";
  cout << "terminal_qplus=" << terminal_box[1] << "\n";
  cout << "phase_gradient_qplus=" << phase_gradient[1] << "\n";
  cout << "phase_gate=" << phase_gate << "\n";
  cout << "monodromy_box=" << monodromy_box << "\n";
  return certified ? EXIT_SUCCESS : EXIT_FAILURE;
}
