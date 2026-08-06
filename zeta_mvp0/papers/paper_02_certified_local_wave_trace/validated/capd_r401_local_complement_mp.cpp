// R401-VAL-L2-S0: validated evaluator for a local root-complement box.
//
// Arguments:
//   bits eps_lo eps_hi qm_lo qm_hi qp_lo qp_hi pm_lo pm_hi T_lo T_hi
//
// The positive fast turning section is P_+=0 and the energy equation is
// contracted first in a caller-supplied Q_+ subinterval of the frozen
// [0.12,0.17] domain.  The remaining return equations
// are enclosed by a CAPD C1 Taylor/Lohner flow.  A box is excluded only when
// a rigorously enclosed residual (direct, mean-value, or fixed-point
// preconditioned mean-value) has a component that omits zero.  This program
// evaluates one box; coverage is the responsibility of the tree driver and
// its independent checker.

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

using ComplementMpSolver = capd::dynsys::OdeSolver<
    capd::MpIMap,
    capd::dynsys::MpLastTermsStepControl>;
using ComplementMpTimeMap = capd::poincare::TimeMap<ComplementMpSolver>;

static bool omits_zero(const MpInterval& value, const MpFloat& margin) {
  return value.rightBound() < -margin || value.leftBound() > margin;
}

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
  // Use a factor-two construction guard so the represented MpFloat remains
  // strictly above the frozen mathematical margin after binary conversion.
  const MpFloat logical_margin(bits == 128 ? "2e-30" : "2e-60");
  // This padding is part of the frozen proof-object construction.  It makes
  // the printed Newton image a conservative enclosure when an independent
  // checker re-evaluates m-F/D from separately printed decimal intervals.
  const MpInterval newton_guard = bits == 128
      ? MpInterval("-1e-40", "1e-40")
      : MpInterval("-1e-75", "1e-75");

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

  const MpInterval epsilon(argv[2], argv[3]);
  const MpInterval qminus(argv[4], argv[5]);
  const MpInterval qplus_input(argv[6], argv[7]);
  const MpInterval pminus(argv[8], argv[9]);
  const MpInterval period(argv[10], argv[11]);

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

  // Contract all possible energy-section points in the Q_+ direction.
  MpInterval qplus = qplus_input;
  MpInterval energy_qplus_before = qplus;
  MpInterval energy_midpoint = mid(qplus);
  MpInterval energy_midpoint_residual(0);
  MpInterval energy_derivative(0);
  MpInterval energy_newton = qplus;
  bool energy_derivative_positive = true;
  bool energy_has_candidate = true;
  bool energy_exclusion_guard = true;
  int energy_iterations = 0;
  for (; energy_iterations < 10; ++energy_iterations) {
    MpIVector full_root(4), midpoint_root(4), gradient_full, gradient_mid;
    full_root[0] = qminus;
    full_root[1] = qplus;
    full_root[2] = pminus;
    full_root[3] = period;
    midpoint_root = full_root;
    midpoint_root[1] = mid(qplus);
    const MpInterval midpoint_residual =
        energy_and_gradient(midpoint_root, gradient_mid) - 1;
    energy_and_gradient(full_root, gradient_full);
    energy_qplus_before = qplus;
    energy_midpoint = midpoint_root[1];
    energy_midpoint_residual = midpoint_residual;
    energy_derivative = gradient_full[1];
    cout << "energy_step_" << energy_iterations << "_before=" << qplus << "\n";
    cout << "energy_step_" << energy_iterations << "_midpoint="
         << midpoint_root[1] << "\n";
    cout << "energy_step_" << energy_iterations << "_residual="
         << midpoint_residual << "\n";
    cout << "energy_step_" << energy_iterations << "_derivative="
         << gradient_full[1] << "\n";
    if (gradient_full[1].leftBound() <= MpFloat(0)) {
      cout << "energy_step_" << energy_iterations
           << "_derivative_positive=0\n";
      energy_derivative_positive = false;
      break;
    }
    const MpInterval newton_raw = midpoint_root[1]
        - midpoint_residual / gradient_full[1];
    const MpInterval newton = newton_raw + newton_guard;
    energy_newton = newton;
    cout << "energy_step_" << energy_iterations << "_newton_raw="
         << newton_raw << "\n";
    cout << "energy_step_" << energy_iterations << "_newton="
         << newton << "\n";
    MpInterval contracted;
    if (!intersection(qplus, newton, contracted)) {
      cout << "energy_step_" << energy_iterations << "_intersects=0\n";
      MpFloat gap(0);
      if (newton.leftBound() > qplus.rightBound()) {
        gap = newton.leftBound() - qplus.rightBound();
      } else if (qplus.leftBound() > newton.rightBound()) {
        gap = qplus.leftBound() - newton.rightBound();
      }
      cout << "energy_step_" << energy_iterations << "_gap="
           << MpInterval(gap) << "\n";
      energy_exclusion_guard = gap > logical_margin;
      energy_has_candidate = !energy_exclusion_guard;
      break;
    }
    cout << "energy_step_" << energy_iterations << "_intersects=1\n";
    cout << "energy_step_" << energy_iterations << "_after="
         << contracted << "\n";
    if (contracted.leftBound() == qplus.leftBound()
        && contracted.rightBound() == qplus.rightBound()) {
      qplus = contracted;
      ++energy_iterations;
      break;
    }
    qplus = contracted;
  }

  cout << "precision_bits=" << bits << "\n";
  cout << "epsilon=" << epsilon << "\n";
  cout << "reduced_box={" << qminus << "," << pminus << "," << period << "}\n";
  cout << "qplus_input=" << qplus_input << "\n";
  cout << "energy_qplus=" << qplus << "\n";
  cout << "energy_qplus_before=" << energy_qplus_before << "\n";
  cout << "energy_midpoint=" << energy_midpoint << "\n";
  cout << "energy_midpoint_residual=" << energy_midpoint_residual << "\n";
  cout << "energy_derivative=" << energy_derivative << "\n";
  cout << "energy_newton=" << energy_newton << "\n";
  cout << "energy_iterations=" << energy_iterations << "\n";
  cout << "energy_derivative_positive=" << energy_derivative_positive << "\n";
  cout << "energy_has_candidate=" << energy_has_candidate << "\n";
  cout << "energy_exclusion_guard=" << energy_exclusion_guard << "\n";
  cout << "logical_margin=" << MpInterval(logical_margin) << "\n";
  cout << "newton_guard=" << newton_guard << "\n";

  if (!energy_derivative_positive) {
    cout << "status=ENERGY_DERIVATIVE_FAIL\n";
    return 3;
  }
  if (!energy_exclusion_guard) {
    cout << "status=ENERGY_GUARD_FAIL\n";
    return 3;
  }
  if (!energy_has_candidate) {
    cout << "status=ENERGY_EXCLUDED\n";
    return 0;
  }

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

  MpIVector X(4);
  X[0] = qminus;
  X[1] = qplus;
  X[2] = pminus;
  X[3] = period;
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

  try {
    const int taylor_order = 24;
    const MpFloat tolerance(bits == 128 ? "1e-30" : "1e-60");
    ComplementMpSolver solver(vector_field, taylor_order);
    solver.setAbsoluteTolerance(tolerance);
    solver.setRelativeTolerance(tolerance);
    ComplementMpTimeMap time_map(solver);
    MpC1Rect2Set flow_set(embed(X));
    const MpIVector terminal_box = time_map(MpInterval(1), flow_set);
    const MpIMatrix monodromy_box = flow_set;

    ComplementMpSolver center_solver(vector_field, taylor_order);
    center_solver.setAbsoluteTolerance(tolerance);
    center_solver.setRelativeTolerance(tolerance);
    ComplementMpTimeMap center_time_map(center_solver);
    MpC1Rect2Set center_set(embed(x_bar));
    const MpIVector center_terminal = center_time_map(MpInterval(1), center_set);

    MpIVector center_gradient, box_gradient;
    MpIVector F_center(4), F_direct(4);
    F_center[0] = energy_and_gradient(x_bar, center_gradient) - 1;
    energy_and_gradient(X, box_gradient);
    F_center[1] = center_terminal[0] - x_bar[0];
    F_center[2] = center_terminal[2] - x_bar[2];
    F_center[3] = center_terminal[3];
    F_direct[0] = energy_and_gradient(X, box_gradient) - 1;
    F_direct[1] = terminal_box[0] - X[0];
    F_direct[2] = terminal_box[2] - X[2];
    F_direct[3] = terminal_box[3];

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
    const MpIVector F_mean = F_center + J * (X - x_bar);
    const MpIMatrix C = midMatrix(
        capd::matrixAlgorithms::inverseMatrix(midMatrix(J)));
    const MpIVector F_preconditioned = C * F_mean;
    const MpIVector K = x_bar - C * F_center
        + (MpIMatrix::Identity(4) - C * J) * (X - x_bar);

    int direct_component = -1;
    int mean_component = -1;
    int preconditioned_component = -1;
    for (int index = 0; index < 4; ++index) {
      if (direct_component < 0 && omits_zero(F_direct[index], logical_margin)) {
        direct_component = index;
      }
      if (mean_component < 0 && omits_zero(F_mean[index], logical_margin)) {
        mean_component = index;
      }
      if (preconditioned_component < 0
          && omits_zero(F_preconditioned[index], logical_margin)) {
        preconditioned_component = index;
      }
    }
    const bool excluded = direct_component >= 0 || mean_component >= 0
        || preconditioned_component >= 0;
    const bool krawczyk_subset = subsetInterior(K, X);
    cout << "X=" << X << "\n";
    cout << "x_bar=" << x_bar << "\n";
    cout << "F_center=" << F_center << "\n";
    cout << "F_direct=" << F_direct << "\n";
    cout << "J=" << J << "\n";
    cout << "F_mean=" << F_mean << "\n";
    cout << "C=" << C << "\n";
    cout << "F_preconditioned=" << F_preconditioned << "\n";
    cout << "K=" << K << "\n";
    cout << "direct_component=" << direct_component << "\n";
    cout << "mean_component=" << mean_component << "\n";
    cout << "preconditioned_component=" << preconditioned_component << "\n";
    cout << "excluded=" << excluded << "\n";
    cout << "krawczyk_subset=" << krawczyk_subset << "\n";
    if (excluded && krawczyk_subset) {
      cout << "status=INVALID_EXCLUSION_UNIQUENESS_CONFLICT\n";
      return 5;
    }
    if (excluded) {
      cout << "status=RETURN_EXCLUDED\n";
      return 0;
    }
    if (krawczyk_subset) {
      // A root inclusion in a complement node is a candidate requiring a
      // separate full-return and identity audit, never an exclusion pass.
      cout << "status=ROOT_CANDIDATE\n";
      return 4;
    }
    cout << "status=UNKNOWN\n";
    return 2;
  } catch (const exception& error) {
    cout << "flow_error=" << error.what() << "\n";
    cout << "status=FLOW_FAIL\n";
    return 3;
  }
}
