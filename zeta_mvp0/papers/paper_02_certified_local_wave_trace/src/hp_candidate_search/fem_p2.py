"""Complex straight-triangle P2 finite elements for R108-C0.

The R108-C0 order-isolation experiment deliberately reuses the frozen R108-S
polygon and P1 triangulations.  This module adds only quadratic Lagrange trial
functions and does not import the finite-difference implementations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import ArpackNoConvergence, eigsh, splu

from .fem_independent import (
    FEMAssembly,
    FEMMesh,
    duffy_gauss_rule,
    henon_potential,
    wall_radius,
)


@dataclass
class P2Topology:
    """Global six-node topology built on one frozen straight P1 mesh."""

    base_mesh: FEMMesh
    edge_keys: np.ndarray
    q_nodes: np.ndarray
    elements: np.ndarray
    boundary_mask: np.ndarray
    interior_indices: np.ndarray
    global_to_dof: np.ndarray
    metadata: dict[str, Any]


def _sparse_frobenius(matrix: sparse.spmatrix) -> float:
    return float(np.sqrt(np.sum(np.abs(matrix.data) ** 2)))


def _relative_sparse_frobenius(
    first: sparse.spmatrix, second: sparse.spmatrix
) -> float:
    return _sparse_frobenius(first - second) / max(
        _sparse_frobenius(second), 1.0e-300
    )


def build_p2_topology(mesh: FEMMesh) -> P2Topology:
    """Append one midpoint node per lexicographically sorted undirected edge."""

    triangles = np.asarray(mesh.triangles, dtype=np.int64)
    edge_rows = np.vstack(
        (
            triangles[:, [0, 1]],
            triangles[:, [1, 2]],
            triangles[:, [2, 0]],
        )
    )
    edge_rows = np.sort(edge_rows, axis=1)
    edge_keys, incidence = np.unique(edge_rows, axis=0, return_counts=True)
    edge_lookup = {
        (int(edge[0]), int(edge[1])): index
        for index, edge in enumerate(edge_keys)
    }
    vertex_count = len(mesh.q_vertices)
    elements = np.empty((len(triangles), 6), dtype=np.int64)
    elements[:, :3] = triangles
    for triangle_index, triangle in enumerate(triangles):
        for local_edge, (left, right) in enumerate(
            ((triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0]))
        ):
            key = (int(min(left, right)), int(max(left, right)))
            elements[triangle_index, 3 + local_edge] = vertex_count + edge_lookup[key]

    midpoint_coordinates = 0.5 * (
        mesh.q_vertices[edge_keys[:, 0]] + mesh.q_vertices[edge_keys[:, 1]]
    )
    q_nodes = np.vstack((mesh.q_vertices, midpoint_coordinates))
    boundary_mask = np.zeros(len(q_nodes), dtype=bool)
    boundary_mask[:vertex_count] = mesh.boundary_mask
    boundary_edges = incidence == 1
    if np.any(
        ~(
            mesh.boundary_mask[edge_keys[boundary_edges, 0]]
            & mesh.boundary_mask[edge_keys[boundary_edges, 1]]
        )
    ):
        raise RuntimeError("P2 boundary edge has a nonboundary endpoint")
    boundary_mask[vertex_count + np.flatnonzero(boundary_edges)] = True
    interior_indices = np.flatnonzero(~boundary_mask)
    global_to_dof = np.full(len(q_nodes), -1, dtype=np.int64)
    global_to_dof[interior_indices] = np.arange(len(interior_indices))

    expected_boundary_edges = int(mesh.spec.boundary_vertices)
    if int(np.sum(boundary_edges)) != expected_boundary_edges:
        raise RuntimeError("P2 topology changed the frozen boundary-edge count")
    if np.any(incidence > 2) or np.any(incidence < 1):
        raise RuntimeError("P2 topology received a nonmanifold base mesh")
    metadata = {
        "base_vertex_count": int(vertex_count),
        "edge_count": int(len(edge_keys)),
        "boundary_edge_count": int(np.sum(boundary_edges)),
        "p2_node_count": int(len(q_nodes)),
        "p2_interior_dof_count": int(len(interior_indices)),
        "element_count": int(len(elements)),
        "local_order": "v0,v1,v2,e01,e12,e20",
        "edge_order": "lexicographic undirected vertex pair",
    }
    return P2Topology(
        base_mesh=mesh,
        edge_keys=edge_keys,
        q_nodes=q_nodes,
        elements=elements,
        boundary_mask=boundary_mask,
        interior_indices=interior_indices,
        global_to_dof=global_to_dof,
        metadata=metadata,
    )


def p2_basis_and_gradients(
    barycentric: np.ndarray, linear_gradients: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Evaluate the frozen six-node P2 basis and physical gradients."""

    barycentric = np.asarray(barycentric, dtype=float)
    linear_gradients = np.asarray(linear_gradients, dtype=float)
    values = np.empty((len(barycentric), 6), dtype=float)
    gradients = np.empty((len(barycentric), 6, 2), dtype=float)
    values[:, :3] = barycentric * (2.0 * barycentric - 1.0)
    for index in range(3):
        gradients[:, index, :] = (
            (4.0 * barycentric[:, index] - 1.0)[:, None]
            * linear_gradients[index]
        )
    edge_pairs = ((0, 1), (1, 2), (2, 0))
    for offset, (left, right) in enumerate(edge_pairs, start=3):
        values[:, offset] = 4.0 * barycentric[:, left] * barycentric[:, right]
        gradients[:, offset, :] = 4.0 * (
            barycentric[:, left, None] * linear_gradients[right]
            + barycentric[:, right, None] * linear_gradients[left]
        )
    return values, gradients


def p1_to_p2_local_prolongation() -> np.ndarray:
    return np.asarray(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.5, 0.5, 0.0],
            [0.0, 0.5, 0.5],
            [0.5, 0.0, 0.5],
        ]
    )


def p2_analytic_mass(area: float) -> np.ndarray:
    matrix = np.asarray(
        [
            [6, -1, -1, 0, -4, 0],
            [-1, 6, -1, 0, 0, -4],
            [-1, -1, 6, -4, 0, 0],
            [0, 0, -4, 32, 16, 16],
            [-4, 0, 0, 16, 32, 16],
            [0, -4, 0, 16, 16, 32],
        ],
        dtype=float,
    )
    return float(area) * matrix / 180.0


def _linear_gradients(coordinates: np.ndarray) -> tuple[np.ndarray, float]:
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    x2, y2 = coordinates[2]
    determinant = (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)
    if determinant <= 0.0:
        raise RuntimeError("P2 assembly received a nonpositive triangle")
    gradients = np.asarray(
        (
            (y1 - y2, x2 - x1),
            (y2 - y0, x0 - x2),
            (y0 - y1, x1 - x0),
        ),
        dtype=float,
    ) / determinant
    return gradients, float(determinant)


def local_p1_p2_matrices(
    coordinates: np.ndarray,
    *,
    magnetic_field: float,
    quadrature_order: int,
    potential_function: Callable[[np.ndarray], np.ndarray],
    constant_potential_shift: float = 0.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Assemble matching local P1/P2 matrices at identical quadrature points."""

    barycentric, reference_weights = duffy_gauss_rule(quadrature_order)
    linear_gradients, determinant = _linear_gradients(np.asarray(coordinates))
    points = barycentric @ coordinates
    weights = reference_weights * determinant
    potential = np.asarray(potential_function(points), dtype=float)
    if potential.shape == ():
        potential = np.full(len(points), float(potential))
    potential = potential + float(constant_potential_shift)
    p2_values, p2_gradients = p2_basis_and_gradients(
        barycentric, linear_gradients
    )
    p1_gradients = np.broadcast_to(
        linear_gradients[None, :, :], (len(points), 3, 2)
    )

    def assemble_basis(
        basis: np.ndarray, gradients: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        mass = np.einsum("q,qi,qj->ij", weights, basis, basis)
        kinetic = 0.5 * np.einsum(
            "q,qia,qja->ij", weights, gradients, gradients
        )
        vector_potential = 0.5 * magnetic_field * np.column_stack(
            (-points[:, 1], points[:, 0])
        )
        scalar = potential + 0.5 * np.sum(vector_potential**2, axis=1)
        scalar_matrix = np.einsum(
            "q,q,qi,qj->ij", weights, scalar, basis, basis
        )
        a_dot_grad = np.einsum("qa,qja->qj", vector_potential, gradients)
        first = np.einsum("q,qi,qj->ij", weights, basis, a_dot_grad)
        stiffness = kinetic + scalar_matrix + 0.5j * (first - first.T)
        return stiffness, mass

    p1_stiffness, p1_mass = assemble_basis(barycentric, p1_gradients)
    p2_stiffness, p2_mass = assemble_basis(p2_values, p2_gradients)
    return p1_stiffness, p1_mass, p2_stiffness, p2_mass


def global_p1_to_p2_prolongation(topology: P2Topology) -> sparse.csr_matrix:
    """Map interior P1 coefficients to the nested interior P2 coefficients."""

    mesh = topology.base_mesh
    rows: list[int] = []
    columns: list[int] = []
    data: list[float] = []
    for vertex in mesh.interior_indices:
        rows.append(int(topology.global_to_dof[int(vertex)]))
        columns.append(int(mesh.global_to_dof[int(vertex)]))
        data.append(1.0)
    vertex_count = len(mesh.q_vertices)
    for edge_index, edge in enumerate(topology.edge_keys):
        row = int(topology.global_to_dof[vertex_count + edge_index])
        if row < 0:
            continue
        for endpoint in edge:
            column = int(mesh.global_to_dof[int(endpoint)])
            if column >= 0:
                rows.append(row)
                columns.append(column)
                data.append(0.5)
    matrix = sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(len(topology.interior_indices), len(mesh.interior_indices)),
    ).tocsr()
    matrix.sum_duplicates()
    return matrix


def assemble_p2_problem(
    topology: P2Topology,
    *,
    magnetic_field: float,
    quadrature_order: int = 7,
    potential_function: Callable[[np.ndarray], np.ndarray] | None = None,
    constant_potential_shift: float = 0.0,
) -> FEMAssembly:
    """Assemble the R108-C0 consistent-mass complex P2 problem."""

    mesh = topology.base_mesh
    barycentric, reference_weights = duffy_gauss_rule(quadrature_order)
    rows: list[int] = []
    columns: list[int] = []
    stiffness_data: list[complex] = []
    mass_data: list[float] = []
    layer_data: list[float] = []
    maximum_exponent = -np.inf
    maximum_potential = 0.0
    integrated_area = 0.0
    boundary_area = 0.0
    boundary_triangle_count = 0

    for triangle_index, triangle in enumerate(mesh.triangles):
        coordinates = mesh.q_vertices[triangle]
        linear_gradients, determinant = _linear_gradients(coordinates)
        area = 0.5 * determinant
        points = barycentric @ coordinates
        weights = reference_weights * determinant
        if potential_function is None:
            potential, exponent = henon_potential(points, mesh.spec.a)
            maximum_exponent = max(maximum_exponent, float(np.max(exponent)))
        else:
            potential = np.asarray(potential_function(points), dtype=float)
            if potential.shape == ():
                potential = np.full(len(points), float(potential))
            if potential.shape != (len(points),):
                raise ValueError("potential_function must return one value per point")
        potential = potential + float(constant_potential_shift)
        maximum_potential = max(maximum_potential, float(np.max(potential)))
        basis, gradients = p2_basis_and_gradients(barycentric, linear_gradients)
        mass_local = np.einsum("q,qi,qj->ij", weights, basis, basis)
        kinetic = 0.5 * np.einsum(
            "q,qia,qja->ij", weights, gradients, gradients
        )
        vector_potential = 0.5 * magnetic_field * np.column_stack(
            (-points[:, 1], points[:, 0])
        )
        scalar = potential + 0.5 * np.sum(vector_potential**2, axis=1)
        scalar_local = np.einsum(
            "q,q,qi,qj->ij", weights, scalar, basis, basis
        )
        a_dot_grad = np.einsum("qa,qja->qj", vector_potential, gradients)
        first = np.einsum("q,qi,qj->ij", weights, basis, a_dot_grad)
        stiffness_local = kinetic + scalar_local + 0.5j * (first - first.T)
        boundary_triangle = bool(np.any(mesh.boundary_mask[triangle]))
        if boundary_triangle:
            boundary_triangle_count += 1
            boundary_area += area
        integrated_area += area
        dofs = topology.global_to_dof[topology.elements[triangle_index]]
        for local_i in range(6):
            dof_i = int(dofs[local_i])
            if dof_i < 0:
                continue
            for local_j in range(6):
                dof_j = int(dofs[local_j])
                if dof_j < 0:
                    continue
                rows.append(dof_i)
                columns.append(dof_j)
                stiffness_data.append(stiffness_local[local_i, local_j])
                mass_data.append(float(mass_local[local_i, local_j]))
                layer_data.append(
                    float(mass_local[local_i, local_j])
                    if boundary_triangle
                    else 0.0
                )

    size = len(topology.interior_indices)
    stiffness = sparse.coo_matrix(
        (np.asarray(stiffness_data, dtype=complex), (rows, columns)),
        shape=(size, size),
    ).tocsr()
    mass = sparse.coo_matrix(
        (np.asarray(mass_data), (rows, columns)), shape=(size, size)
    ).tocsr()
    boundary_mass = sparse.coo_matrix(
        (np.asarray(layer_data), (rows, columns)), shape=(size, size)
    ).tocsr()
    for matrix in (stiffness, mass, boundary_mass):
        matrix.sum_duplicates()
        matrix.eliminate_zeros()

    stiffness_scale = max(float(np.max(np.abs(stiffness.data))), 1.0e-300)
    mass_scale = max(float(np.max(np.abs(mass.data))), 1.0e-300)
    hermitian_defect = stiffness - stiffness.conjugate().T
    mass_defect = mass - mass.T
    diagonal = mass.diagonal()
    if np.any(diagonal <= 0.0):
        raise RuntimeError("P2 mass has a nonpositive diagonal")
    inverse_sqrt = sparse.diags(diagonal ** -0.5)
    normalized_mass = inverse_sqrt @ mass @ inverse_sqrt
    minimum_value, minimum_vector = eigsh(
        normalized_mass, k=1, which="SA", tol=1.0e-12
    )
    minimum_residual = np.linalg.norm(
        normalized_mass @ minimum_vector - minimum_vector * minimum_value[0]
    )
    metadata = {
        "basis_order": 2,
        "magnetic_field": float(magnetic_field),
        "quadrature_order": int(quadrature_order),
        "dof_count": int(size),
        "stiffness_nnz": int(stiffness.nnz),
        "mass_nnz": int(mass.nnz),
        "integrated_area": float(integrated_area),
        "mesh_mapped_polygon_area": float(mesh.metadata["mapped_polygon_area"]),
        "area_relative_discrepancy": float(
            abs(integrated_area - mesh.metadata["mapped_polygon_area"])
            / mesh.metadata["mapped_polygon_area"]
        ),
        "maximum_potential": float(maximum_potential),
        "maximum_potential_exponent": (
            None if not np.isfinite(maximum_exponent) else float(maximum_exponent)
        ),
        "potential_clipped": False,
        "raw_stiffness_hermiticity_relative_max": float(
            np.max(np.abs(hermitian_defect.data), initial=0.0) / stiffness_scale
        ),
        "raw_mass_symmetry_relative_max": float(
            np.max(np.abs(mass_defect.data), initial=0.0) / mass_scale
        ),
        "normalized_mass_smallest_eigenvalue": float(minimum_value[0]),
        "normalized_mass_smallest_eigen_residual": float(minimum_residual),
        "mass_positive_definite": bool(
            minimum_value[0] > 0.0 and minimum_residual < 1.0e-10
        ),
        "boundary_layer_triangle_count": int(boundary_triangle_count),
        "boundary_layer_area": float(boundary_area),
        "boundary_layer_area_fraction": float(boundary_area / integrated_area),
        "potential_function": (
            "independent centered Henon exponential"
            if potential_function is None
            else "caller-supplied test potential"
        ),
        "constant_potential_shift": float(constant_potential_shift),
    }
    return FEMAssembly(stiffness, mass, boundary_mass, metadata)


def global_embedding_defects(
    topology: P2Topology,
    p1_assembly: FEMAssembly,
    p2_assembly: FEMAssembly,
) -> dict[str, float]:
    prolongation = global_p1_to_p2_prolongation(topology)
    mass_projected = prolongation.conjugate().T @ p2_assembly.mass @ prolongation
    stiffness_projected = (
        prolongation.conjugate().T @ p2_assembly.stiffness @ prolongation
    )
    return {
        "mass_relative_frobenius": _relative_sparse_frobenius(
            mass_projected, p1_assembly.mass
        ),
        "stiffness_relative_frobenius": _relative_sparse_frobenius(
            stiffness_projected, p1_assembly.stiffness
        ),
    }


def deterministic_start(size: int, mass: sparse.spmatrix) -> np.ndarray:
    index = np.arange(size, dtype=float)
    vector = np.sin((index + 1.0) * np.sqrt(2.0)) + 0.5 * np.cos(
        (index + 1.0) * np.sqrt(3.0)
    )
    vector = vector.astype(complex)
    return vector / np.sqrt(float(np.real(vector.conjugate() @ (mass @ vector))))


def solve_p2_generalized_eigensystem(
    assembly: FEMAssembly,
    count: int,
    *,
    tolerance: float = 2.0e-10,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, Any]]:
    """Solve a P2 generalized problem with the frozen R108-C0 diagnostics."""

    stiffness = assembly.stiffness
    mass = assembly.mass
    if count >= stiffness.shape[0] - 1:
        raise ValueError("count must be smaller than the P2 DOF count minus one")
    ncv = min(stiffness.shape[0] - 1, 257)
    if ncv <= count:
        raise ValueError("P2 eigensolver requires ncv greater than count")
    try:
        returned_values, vectors = eigsh(
            stiffness,
            k=count,
            M=mass,
            sigma=0.0,
            which="LM",
            tol=tolerance,
            maxiter=5000,
            v0=deterministic_start(stiffness.shape[0], mass),
            ncv=ncv,
        )
    except ArpackNoConvergence as error:
        raise RuntimeError("R108-C0 ARPACK did not converge") from error
    order = np.argsort(returned_values.real, kind="mergesort")
    vectors = np.asarray(vectors[:, order], dtype=complex)
    # Complex ARPACK can return a non-orthogonal basis inside a degenerate
    # Ritz cluster.  Perform a mass-orthogonal subspace normalization followed
    # by a dense Rayleigh--Ritz rotation.  This changes only the returned Ritz
    # basis, never the assembled K or M matrices.
    initial_gram = vectors.conjugate().T @ (mass @ vectors)
    gram_values, gram_vectors = np.linalg.eigh(
        0.5 * (initial_gram + initial_gram.conjugate().T)
    )
    if np.any(gram_values <= 0.0):
        raise RuntimeError("ARPACK returned a rank-deficient mass subspace")
    mass_orthogonalizer = gram_vectors @ np.diag(gram_values ** -0.5)
    vectors = vectors @ mass_orthogonalizer
    projected_stiffness = vectors.conjugate().T @ (stiffness @ vectors)
    projected_hermiticity = float(
        np.max(
            np.abs(projected_stiffness - projected_stiffness.conjugate().T),
            initial=0.0,
        )
        / max(np.max(np.abs(projected_stiffness)), 1.0e-300)
    )
    projected_values, projected_vectors = np.linalg.eigh(
        0.5 * (projected_stiffness + projected_stiffness.conjugate().T)
    )
    vectors = vectors @ projected_vectors
    stiffness_vectors = stiffness @ vectors
    mass_vectors = mass @ vectors
    rayleigh = np.einsum(
        "ik,ik->k", vectors.conjugate(), stiffness_vectors
    ) / np.einsum("ik,ik->k", vectors.conjugate(), mass_vectors)
    second_order = np.argsort(projected_values.real, kind="mergesort")
    vectors = vectors[:, second_order]
    rayleigh = rayleigh[second_order]
    stiffness_vectors = stiffness @ vectors
    mass_vectors = mass @ vectors
    values = np.asarray(rayleigh.real, dtype=float)
    residual_matrix = stiffness_vectors - mass_vectors * values[None, :]
    residual_norm = np.linalg.norm(residual_matrix, axis=0)
    equation_scale = np.maximum(
        1.0, np.abs(values) * np.linalg.norm(mass_vectors, axis=0)
    )
    equation_residual = residual_norm / equation_scale
    backward_scale = np.maximum(
        np.linalg.norm(stiffness_vectors, axis=0)
        + np.abs(values) * np.linalg.norm(mass_vectors, axis=0),
        np.finfo(float).tiny,
    )
    backward = residual_norm / backward_scale
    factor = splu(mass.astype(complex).tocsc())
    dual_solution = factor.solve(np.asarray(residual_matrix, dtype=complex))
    dual_squared_raw = np.real(
        np.einsum("ik,ik->k", residual_matrix.conjugate(), dual_solution)
    )
    dual_negative_tolerance = 1024.0 * np.finfo(float).eps * max(
        1.0, float(np.max(np.abs(dual_squared_raw), initial=0.0))
    )
    if float(np.min(dual_squared_raw)) < -dual_negative_tolerance:
        raise RuntimeError("mass-dual residual quadratic form is significantly negative")
    dual_squared = np.maximum(dual_squared_raw, 0.0)
    mass_norm = np.sqrt(
        np.real(np.einsum("ik,ik->k", vectors.conjugate(), mass_vectors))
    )
    dual = np.sqrt(dual_squared) / (np.maximum(np.abs(values), 1.0) * mass_norm)
    gram = vectors.conjugate().T @ mass_vectors
    orthogonality_matrix = gram - np.eye(count)
    layer_fraction = np.real(
        np.einsum(
            "ik,ik->k",
            vectors.conjugate(),
            assembly.boundary_layer_mass @ vectors,
        )
    ) / np.real(np.einsum("ik,ik->k", vectors.conjugate(), mass_vectors))
    imaginary_relative = np.abs(rayleigh.imag) / np.maximum(
        1.0, np.abs(rayleigh.real)
    )
    metadata = {
        "count": int(count),
        "lowest_eigenvalue": float(values[0]),
        "highest_eigenvalue": float(values[-1]),
        "monotone": bool(np.all(np.diff(values) >= 0.0)),
        "maximum_equation_scaled_residual": float(np.max(equation_residual)),
        "maximum_backward_residual": float(np.max(backward)),
        "maximum_mass_dual_relative_residual": float(np.max(dual)),
        "maximum_mass_orthogonality_defect": float(
            np.max(np.abs(orthogonality_matrix))
        ),
        "maximum_rayleigh_relative_imaginary_part": float(
            np.max(imaginary_relative)
        ),
        "maximum_boundary_layer_mass_fraction": float(np.max(layer_fraction)),
        "boundary_layer_area_fraction": float(
            assembly.metadata["boundary_layer_area_fraction"]
        ),
        "solver": "scipy.sparse.linalg.eigsh complex generalized shift-invert",
        "solver_tolerance": float(tolerance),
        "maxiter": 5000,
        "ncv": int(ncv),
        "arpack_nonconvergence_is_failure": True,
        "mass_orthogonal_rayleigh_ritz_postprocessing": True,
        "projected_stiffness_hermiticity_relative_max": projected_hermiticity,
        "minimum_unclipped_mass_dual_quadratic_form": float(
            np.min(dual_squared_raw)
        ),
        "mass_dual_negative_roundoff_tolerance": float(dual_negative_tolerance),
    }
    diagnostics = np.column_stack(
        (equation_residual, backward, dual, layer_fraction, imaginary_relative)
    )
    return values, vectors, diagnostics, metadata


def potential_boundary_participation_p2(
    topology: P2Topology,
    vectors: np.ndarray,
    *,
    radius_fraction: float = 0.90,
    quadrature_order: int = 7,
) -> tuple[np.ndarray, dict[str, Any]]:
    """Integrate P2 eigenfunction mass in the frozen high-potential band."""

    if not 0.0 < radius_fraction < 1.0:
        raise ValueError("radius_fraction must lie between zero and one")
    coefficients = np.asarray(vectors)
    if coefficients.shape[0] != len(topology.interior_indices):
        raise ValueError("P2 vector row count does not match topology")
    mesh = topology.base_mesh
    barycentric, reference_weights = duffy_gauss_rule(quadrature_order)
    numerator = np.zeros(coefficients.shape[1])
    denominator = np.zeros(coefficients.shape[1])
    full = np.zeros((len(topology.q_nodes), coefficients.shape[1]), dtype=complex)
    full[topology.interior_indices] = coefficients
    radius = wall_radius(mesh.spec.wall_energy)
    threshold = 2.0 * np.pi * np.exp(
        np.pi * (radius_fraction * radius) ** 2
    )
    for triangle_index, triangle in enumerate(mesh.triangles):
        coordinates = mesh.q_vertices[triangle]
        linear_gradients, determinant = _linear_gradients(coordinates)
        points = barycentric @ coordinates
        weights = reference_weights * determinant
        basis, _ = p2_basis_and_gradients(barycentric, linear_gradients)
        values = basis @ full[topology.elements[triangle_index]]
        density = np.abs(values) ** 2
        potential, _ = henon_potential(points, mesh.spec.a)
        denominator += np.sum(weights[:, None] * density, axis=0)
        mask = potential >= threshold
        if np.any(mask):
            numerator += np.sum(weights[mask, None] * density[mask], axis=0)
    fractions = numerator / np.maximum(denominator, np.finfo(float).tiny)
    return fractions, {
        "radius_fraction": float(radius_fraction),
        "quadrature_order": int(quadrature_order),
        "threshold_potential": float(threshold),
        "mode_count": int(coefficients.shape[1]),
        "minimum_denominator": float(np.min(denominator)),
        "maximum_denominator": float(np.max(denominator)),
        "maximum_participation": float(np.max(fractions)),
        "numerators": numerator.copy(),
        "denominators": denominator.copy(),
    }
