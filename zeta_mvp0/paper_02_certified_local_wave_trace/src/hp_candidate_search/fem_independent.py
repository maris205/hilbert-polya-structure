"""Independent polygonal-domain P1 finite elements for the R108-S smoke.

This module intentionally does not import the finite-difference or classical
Hénon implementations in this project.  Geometry, potential, quadrature, and
the magnetic weak form are assembled independently for the R108-S audit.
The straight-edged domain is the frozen polygonal approximation defined in
``research/R108_FEM_SMOKE_PROTOCOL.md``; it is not the exact curved preimage.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
from math import log, pi, sqrt
from pathlib import Path
from typing import Any, Callable

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy import sparse
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import eigsh, splu
from scipy.spatial import Delaunay, cKDTree


TWO_PI = 2.0 * pi


@dataclass(frozen=True)
class FEMMeshSpec:
    """Frozen geometric inputs for one Hénon-preimage mesh."""

    h_u: float
    a: float = 1.02
    wall_energy: float = 45_000.0
    boundary_vertices: int = 256


@dataclass
class FEMMesh:
    """A conforming triangulation in u-space and its mapped q-space image."""

    spec: FEMMeshSpec
    u_vertices: np.ndarray
    q_vertices: np.ndarray
    triangles: np.ndarray
    boundary_mask: np.ndarray
    interior_indices: np.ndarray
    global_to_dof: np.ndarray
    lattice_ij: np.ndarray
    metadata: dict[str, Any]


@dataclass
class FEMAssembly:
    """Interior-DOF generalized eigenproblem and audit matrices."""

    stiffness: sparse.csr_matrix
    mass: sparse.csr_matrix
    boundary_layer_mass: sparse.csr_matrix
    metadata: dict[str, Any]


def file_sha256(path: str | Path) -> str:
    digest = sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def centered_fixed_point(a: float) -> float:
    """Positive fixed point, independently implemented for R108."""

    if a < -1.0:
        raise ValueError("real centered branch requires a >= -1")
    if abs(a) < 1.0e-14:
        return 0.5
    return 1.0 / (1.0 + sqrt(1.0 + a))


def centered_henon_forward(points: np.ndarray, a: float) -> np.ndarray:
    """Apply the centered area-preserving Hénon map to (...,2) points."""

    values = np.asarray(points, dtype=float)
    x = values[..., 0]
    y = values[..., 1]
    fixed = centered_fixed_point(a)
    return np.stack((-2.0 * a * fixed * x - a * x * x - y, x), axis=-1)


def centered_henon_inverse(points: np.ndarray, a: float) -> np.ndarray:
    """Apply the exact centered inverse to (...,2) points."""

    values = np.asarray(points, dtype=float)
    u = values[..., 0]
    v = values[..., 1]
    fixed = centered_fixed_point(a)
    return np.stack((v, -2.0 * a * fixed * v - a * v * v - u), axis=-1)


def wall_radius(wall_energy: float) -> float:
    if wall_energy <= TWO_PI:
        raise ValueError("wall_energy must exceed 2*pi")
    return sqrt(log(wall_energy / TWO_PI) / pi)


def duffy_gauss_rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    """Return P1 barycentric points and weights on the reference triangle."""

    if order < 1:
        raise ValueError("quadrature order must be positive")
    nodes, weights = leggauss(order)
    nodes = 0.5 * (nodes + 1.0)
    weights = 0.5 * weights
    barycentric: list[tuple[float, float, float]] = []
    output_weights: list[float] = []
    for r, wr in zip(nodes, weights, strict=True):
        for s, ws in zip(nodes, weights, strict=True):
            xi = r
            eta = (1.0 - r) * s
            barycentric.append((1.0 - xi - eta, xi, eta))
            output_weights.append(float(wr * ws * (1.0 - r)))
    return np.asarray(barycentric), np.asarray(output_weights)


def _orientation(points: np.ndarray, triangles: np.ndarray) -> np.ndarray:
    p0 = points[triangles[:, 0]]
    p1 = points[triangles[:, 1]]
    p2 = points[triangles[:, 2]]
    return (p1[:, 0] - p0[:, 0]) * (p2[:, 1] - p0[:, 1]) - (
        p1[:, 1] - p0[:, 1]
    ) * (p2[:, 0] - p0[:, 0])


def _segment_orientation(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> float:
    return float((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))


def _strict_segments_intersect(
    a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray, tolerance: float
) -> bool:
    o1 = _segment_orientation(a, b, c)
    o2 = _segment_orientation(a, b, d)
    o3 = _segment_orientation(c, d, a)
    o4 = _segment_orientation(c, d, b)
    return o1 * o2 < -(tolerance**2) and o3 * o4 < -(tolerance**2)


def _simple_boundary_polygon(points: np.ndarray) -> bool:
    count = len(points)
    scale = max(1.0, float(np.max(np.abs(points))))
    tolerance = 1.0e-14 * scale * scale
    for first in range(count):
        a = points[first]
        b = points[(first + 1) % count]
        for second in range(first + 1, count):
            if second in {first, (first + 1) % count}:
                continue
            if first == 0 and second == count - 1:
                continue
            c = points[second]
            d = points[(second + 1) % count]
            if _strict_segments_intersect(a, b, c, d, tolerance):
                return False
    return True


def _edge_counts(triangles: np.ndarray) -> dict[tuple[int, int], int]:
    counts: dict[tuple[int, int], int] = {}
    for triangle in triangles:
        for start, stop in (
            (int(triangle[0]), int(triangle[1])),
            (int(triangle[1]), int(triangle[2])),
            (int(triangle[2]), int(triangle[0])),
        ):
            edge = (start, stop) if start < stop else (stop, start)
            counts[edge] = counts.get(edge, 0) + 1
    return counts


def _mesh_quality(points: np.ndarray, triangles: np.ndarray) -> dict[str, float]:
    coordinates = points[triangles]
    edge_lengths = np.stack(
        (
            np.linalg.norm(coordinates[:, 1] - coordinates[:, 0], axis=1),
            np.linalg.norm(coordinates[:, 2] - coordinates[:, 1], axis=1),
            np.linalg.norm(coordinates[:, 0] - coordinates[:, 2], axis=1),
        ),
        axis=1,
    )
    if np.any(edge_lengths <= 0.0):
        raise RuntimeError("mesh contains a zero-length edge")
    angles = np.empty_like(edge_lengths)
    # Angle opposite each edge, obtained by the cosine law.
    for opposite in range(3):
        adjacent1 = edge_lengths[:, (opposite + 1) % 3]
        adjacent2 = edge_lengths[:, (opposite + 2) % 3]
        cosine = np.clip(
            (adjacent1**2 + adjacent2**2 - edge_lengths[:, opposite] ** 2)
            / (2.0 * adjacent1 * adjacent2),
            -1.0,
            1.0,
        )
        angles[:, opposite] = np.degrees(np.arccos(cosine))
    ratios = np.max(edge_lengths, axis=1) / np.min(edge_lengths, axis=1)
    minimum_angles = np.min(angles, axis=1)
    return {
        "minimum_edge_length": float(np.min(edge_lengths)),
        "maximum_edge_length": float(np.max(edge_lengths)),
        "minimum_angle_degrees": float(np.min(minimum_angles)),
        "minimum_angle_p01_degrees": float(np.quantile(minimum_angles, 0.01)),
        "minimum_angle_median_degrees": float(np.median(minimum_angles)),
        "maximum_edge_ratio": float(np.max(ratios)),
        "edge_ratio_p99": float(np.quantile(ratios, 0.99)),
        "quality_warning_below_one_degree": bool(np.min(minimum_angles) < 1.0),
    }


def _point_in_triangle_strict(
    point: np.ndarray, coordinates: np.ndarray, tolerance: float
) -> bool:
    return all(
        _segment_orientation(
            coordinates[index], coordinates[(index + 1) % 3], point
        )
        > tolerance
        for index in range(3)
    )


def _triangle_overlap_audit(
    points: np.ndarray, triangles: np.ndarray
) -> dict[str, float | int | bool]:
    """Audit nonlocal overlaps with deterministic AABB binning."""

    extent = np.ptp(points, axis=0)
    scale = max(1.0, float(np.max(extent)))
    length_tolerance = 256.0 * np.finfo(float).eps * scale
    area_tolerance = 1024.0 * np.finfo(float).eps * scale * scale
    twice_areas = _orientation(points, triangles)
    if np.any(twice_areas <= area_tolerance):
        raise RuntimeError("mapped triangle area is below the frozen tolerance")

    coordinates = points[triangles]
    lower = np.min(coordinates, axis=1)
    upper = np.max(coordinates, axis=1)
    bins_per_axis = max(8, int(np.ceil(np.sqrt(len(triangles) / 2.0))))
    domain_lower = np.min(points, axis=0)
    bin_width = np.maximum(extent / bins_per_axis, length_tolerance)
    buckets: dict[tuple[int, int], list[int]] = {}
    for triangle_index in range(len(triangles)):
        first = np.floor((lower[triangle_index] - domain_lower) / bin_width).astype(int)
        last = np.floor((upper[triangle_index] - domain_lower) / bin_width).astype(int)
        first = np.clip(first, 0, bins_per_axis - 1)
        last = np.clip(last, 0, bins_per_axis - 1)
        for ix in range(int(first[0]), int(last[0]) + 1):
            for iy in range(int(first[1]), int(last[1]) + 1):
                buckets.setdefault((ix, iy), []).append(triangle_index)

    candidate_pairs: set[tuple[int, int]] = set()
    for members in buckets.values():
        unique = sorted(set(members))
        for left_index, left in enumerate(unique):
            for right in unique[left_index + 1 :]:
                candidate_pairs.add((left, right))

    checked_nonadjacent = 0
    for left, right in sorted(candidate_pairs):
        left_vertices = set(int(value) for value in triangles[left])
        right_vertices = set(int(value) for value in triangles[right])
        shared = left_vertices & right_vertices
        left_coordinates = coordinates[left]
        right_coordinates = coordinates[right]
        if len(shared) == 2:
            shared_vertices = sorted(shared)
            first_point = points[shared_vertices[0]]
            second_point = points[shared_vertices[1]]
            left_third = points[next(iter(left_vertices - shared))]
            right_third = points[next(iter(right_vertices - shared))]
            side_product = _segment_orientation(
                first_point, second_point, left_third
            ) * _segment_orientation(first_point, second_point, right_third)
            if side_product >= -area_tolerance**2:
                raise RuntimeError("triangles adjacent to one edge lie on the same side")
            continue

        # For zero- or one-vertex adjacency, strict crossings away from a
        # shared endpoint and strict vertex containment indicate overlap.
        checked_nonadjacent += int(len(shared) == 0)
        for left_edge in range(3):
            a = left_coordinates[left_edge]
            b = left_coordinates[(left_edge + 1) % 3]
            left_edge_vertices = {
                int(triangles[left, left_edge]),
                int(triangles[left, (left_edge + 1) % 3]),
            }
            for right_edge in range(3):
                c = right_coordinates[right_edge]
                d = right_coordinates[(right_edge + 1) % 3]
                right_edge_vertices = {
                    int(triangles[right, right_edge]),
                    int(triangles[right, (right_edge + 1) % 3]),
                }
                if left_edge_vertices & right_edge_vertices:
                    continue
                if _strict_segments_intersect(a, b, c, d, area_tolerance):
                    raise RuntimeError("mapped triangles have crossing nonshared edges")
        for local, vertex in enumerate(triangles[left]):
            if int(vertex) not in shared and _point_in_triangle_strict(
                left_coordinates[local], right_coordinates, area_tolerance
            ):
                raise RuntimeError("mapped triangle vertex lies inside another triangle")
        for local, vertex in enumerate(triangles[right]):
            if int(vertex) not in shared and _point_in_triangle_strict(
                right_coordinates[local], left_coordinates, area_tolerance
            ):
                raise RuntimeError("mapped triangle vertex lies inside another triangle")

    return {
        "triangle_overlap_audit_pass": True,
        "aabb_bins_per_axis": int(bins_per_axis),
        "candidate_triangle_pair_count": int(len(candidate_pairs)),
        "checked_nonadjacent_pair_count": int(checked_nonadjacent),
        "length_tolerance": float(length_tolerance),
        "double_area_tolerance": float(area_tolerance),
    }


def generate_preimage_mesh(spec: FEMMeshSpec) -> FEMMesh:
    """Generate the deterministic disk mesh and map it to q coordinates."""

    if spec.h_u <= 0.0:
        raise ValueError("h_u must be positive")
    if spec.boundary_vertices < 16:
        raise ValueError("boundary_vertices must be at least 16")
    radius = wall_radius(spec.wall_energy)
    angles = np.linspace(0.0, TWO_PI, spec.boundary_vertices, endpoint=False)
    boundary = radius * np.column_stack((np.cos(angles), np.sin(angles)))

    vertical_spacing = 0.5 * sqrt(3.0) * spec.h_u
    j_limit = int(np.ceil(radius / vertical_spacing))
    interior_records: list[tuple[int, int, float, float]] = []
    # Retain precisely the triangular-lattice points lying strictly inside
    # the regular boundary polygon, not merely inside its circumcircle.
    edge_mid_angles = angles + pi / spec.boundary_vertices
    edge_normals = np.column_stack(
        (np.cos(edge_mid_angles), np.sin(edge_mid_angles))
    )
    polygon_apothem = radius * np.cos(pi / spec.boundary_vertices)
    polygon_tolerance = 128.0 * np.finfo(float).eps * max(1.0, radius)
    for j in range(-j_limit, j_limit + 1):
        y = j * vertical_spacing
        i_limit = int(np.ceil(2.0 * radius / spec.h_u)) + abs(j) + 2
        for i in range(-i_limit, i_limit + 1):
            x = (i + 0.5 * j) * spec.h_u
            point = np.array([x, y])
            if np.max(edge_normals @ point) < polygon_apothem - polygon_tolerance:
                interior_records.append((j, i, x, y))
    interior_records.sort(key=lambda item: (item[0], item[1]))
    interior = np.asarray([(item[2], item[3]) for item in interior_records])
    u_vertices = np.vstack((boundary, interior))
    boundary_mask = np.zeros(len(u_vertices), dtype=bool)
    boundary_mask[: spec.boundary_vertices] = True
    lattice_ij = np.full((len(u_vertices), 2), np.iinfo(np.int32).min, dtype=np.int64)
    lattice_ij[spec.boundary_vertices :] = np.asarray(
        [(item[1], item[0]) for item in interior_records], dtype=np.int64
    )

    nearest = cKDTree(u_vertices).query(u_vertices, k=2)[0][:, 1]
    minimum_separation = float(np.min(nearest))
    if minimum_separation <= 1.0e-12 * max(1.0, radius):
        raise RuntimeError("duplicate or numerically coincident mesh vertices")

    triangulation = Delaunay(u_vertices, qhull_options="Qbb Qc Qz Q12")
    triangles = np.asarray(triangulation.simplices, dtype=int)
    triangles = triangles[np.all(triangles < len(u_vertices), axis=1)]
    u_orientation = _orientation(u_vertices, triangles)
    negative = u_orientation < 0.0
    triangles[negative] = triangles[negative][:, [0, 2, 1]]
    u_orientation = _orientation(u_vertices, triangles)
    if np.any(u_orientation <= 0.0):
        raise RuntimeError("nonpositive u-space triangle orientation")

    q_vertices = centered_henon_inverse(u_vertices, spec.a)
    q_orientation = _orientation(q_vertices, triangles)
    if np.any(q_orientation <= 0.0):
        raise RuntimeError("mapped piecewise-affine mesh contains an inverted triangle")

    counts = _edge_counts(triangles)
    if max(counts.values(), default=0) > 2:
        raise RuntimeError("nonmanifold mesh edge")
    actual_boundary_edges = {edge for edge, count in counts.items() if count == 1}
    expected_boundary_edges = {
        tuple(sorted((index, (index + 1) % spec.boundary_vertices)))
        for index in range(spec.boundary_vertices)
    }
    if actual_boundary_edges != expected_boundary_edges:
        raise RuntimeError("Delaunay hull does not match the frozen boundary polygon")

    incidence = np.bincount(triangles.ravel(), minlength=len(u_vertices))
    if np.any(incidence == 0):
        raise RuntimeError("isolated mesh vertex")
    row = np.concatenate((triangles[:, 0], triangles[:, 1], triangles[:, 2]))
    col = np.concatenate((triangles[:, 1], triangles[:, 2], triangles[:, 0]))
    graph = sparse.coo_matrix(
        (np.ones(2 * len(row)), (np.concatenate((row, col)), np.concatenate((col, row)))),
        shape=(len(u_vertices), len(u_vertices)),
    ).tocsr()
    component_count = connected_components(graph, directed=False, return_labels=False)
    if component_count != 1:
        raise RuntimeError("mesh graph is disconnected")
    if not _simple_boundary_polygon(q_vertices[: spec.boundary_vertices]):
        raise RuntimeError("mapped boundary polygon self-intersects")

    interior_indices = np.flatnonzero(~boundary_mask)
    global_to_dof = np.full(len(u_vertices), -1, dtype=int)
    global_to_dof[interior_indices] = np.arange(len(interior_indices))
    mapped_area = 0.5 * float(np.sum(q_orientation))
    disk_polygon_area = 0.5 * float(np.sum(u_orientation))
    euler_characteristic = len(u_vertices) - len(counts) + len(triangles)
    if euler_characteristic != 1:
        raise RuntimeError("triangulated disk fails the Euler V-E+T=1 identity")
    canonical_triangles = np.sort(triangles, axis=1)
    canonical_triangles = canonical_triangles[
        np.lexsort(
            (
                canonical_triangles[:, 2],
                canonical_triangles[:, 1],
                canonical_triangles[:, 0],
            )
        )
    ]
    connectivity_hash = sha256(canonical_triangles.astype("<i8").tobytes()).hexdigest()
    u_hash = sha256(np.asarray(u_vertices, dtype="<f8").tobytes()).hexdigest()
    q_hash = sha256(np.asarray(q_vertices, dtype="<f8").tobytes()).hexdigest()

    # Straight mapped boundary chords are not exact level-set curves.  Store
    # their maximum wall-potential deviation as a geometry-bias diagnostic.
    boundary_q = q_vertices[: spec.boundary_vertices]
    interpolation = np.linspace(0.0, 1.0, 33)
    boundary_samples = []
    for index in range(spec.boundary_vertices):
        start = boundary_q[index]
        stop = boundary_q[(index + 1) % spec.boundary_vertices]
        boundary_samples.append(
            (1.0 - interpolation[:, None]) * start
            + interpolation[:, None] * stop
        )
    sampled_boundary = np.vstack(boundary_samples)
    sampled_potential, _ = henon_potential(sampled_boundary, spec.a)
    boundary_wall_deviation = float(
        np.max(np.abs(sampled_potential / spec.wall_energy - 1.0))
    )
    u_quality = _mesh_quality(u_vertices, triangles)
    q_quality = _mesh_quality(q_vertices, triangles)
    overlap_audit = _triangle_overlap_audit(q_vertices, triangles)
    metadata: dict[str, Any] = {
        "spec": asdict(spec),
        "wall_radius": float(radius),
        "vertex_count": int(len(u_vertices)),
        "boundary_vertex_count": int(np.sum(boundary_mask)),
        "interior_dof_count": int(len(interior_indices)),
        "triangle_count": int(len(triangles)),
        "minimum_vertex_separation": minimum_separation,
        "minimum_u_twice_area": float(np.min(u_orientation)),
        "minimum_q_twice_area": float(np.min(q_orientation)),
        "maximum_q_twice_area": float(np.max(q_orientation)),
        "u_polygon_area": disk_polygon_area,
        "mapped_polygon_area": mapped_area,
        "relative_area_change": float(
            abs(mapped_area - disk_polygon_area) / disk_polygon_area
        ),
        "edge_count": int(len(counts)),
        "boundary_edge_count": int(len(actual_boundary_edges)),
        "component_count": int(component_count),
        "euler_characteristic": int(euler_characteristic),
        "boundary_polygon_simple": True,
        "positive_orientation_all_triangles": True,
        "piecewise_affine_global_injectivity_check": (
            "connected conforming disk topology + simple mapped boundary + "
            "strictly positive mapped triangle orientations"
        ),
        "qhull_options": "Qbb Qc Qz Q12",
        "lattice_basis": "u_ij=i*(h,0)+j*(h/2,sqrt(3)h/2)",
        "lattice_order": "lexicographic (j,i), after boundary vertices",
        "interior_filter": "strict half-space interior of regular boundary polygon",
        "connectivity_sha256": connectivity_hash,
        "u_vertices_sha256": u_hash,
        "q_vertices_sha256": q_hash,
        "boundary_wall_relative_deviation_33_samples_per_edge": boundary_wall_deviation,
        "u_mesh_quality": u_quality,
        "q_mesh_quality": q_quality,
        "triangle_overlap_audit": overlap_audit,
    }
    return FEMMesh(
        spec=spec,
        u_vertices=u_vertices,
        q_vertices=q_vertices,
        triangles=triangles,
        boundary_mask=boundary_mask,
        interior_indices=interior_indices,
        global_to_dof=global_to_dof,
        lattice_ij=lattice_ij,
        metadata=metadata,
    )


def henon_potential(points: np.ndarray, a: float) -> tuple[np.ndarray, np.ndarray]:
    mapped = centered_henon_forward(points, a)
    exponent = pi * np.sum(mapped * mapped, axis=-1)
    maximum_safe_exponent = log(np.finfo(float).max / TWO_PI)
    if np.any(exponent >= maximum_safe_exponent):
        raise FloatingPointError("uncapped Hénon potential exceeds the safe exponent range")
    return TWO_PI * np.exp(exponent), exponent


def _p1_gradients(coordinates: np.ndarray) -> tuple[np.ndarray, float]:
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    x2, y2 = coordinates[2]
    determinant = (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)
    if determinant <= 0.0:
        raise RuntimeError("P1 assembly received a nonpositive triangle")
    gradients = np.array(
        [
            [y1 - y2, x2 - x1],
            [y2 - y0, x0 - x2],
            [y0 - y1, x1 - x0],
        ],
        dtype=float,
    ) / determinant
    return gradients, determinant


def assemble_p1_problem(
    mesh: FEMMesh,
    *,
    magnetic_field: float,
    quadrature_order: int = 5,
    potential_function: Callable[[np.ndarray], np.ndarray] | None = None,
    constant_potential_shift: float = 0.0,
) -> FEMAssembly:
    """Assemble the consistent-mass P1 generalized eigenproblem."""

    barycentric, reference_weights = duffy_gauss_rule(quadrature_order)
    rows: list[int] = []
    columns: list[int] = []
    stiffness_data: list[complex] = []
    mass_data: list[float] = []
    layer_data: list[float] = []
    maximum_exponent = -np.inf
    maximum_potential = 0.0
    integrated_area = 0.0
    boundary_layer_triangle_count = 0
    boundary_layer_area = 0.0

    for triangle in mesh.triangles:
        coordinates = mesh.q_vertices[triangle]
        gradients, determinant = _p1_gradients(coordinates)
        area = 0.5 * determinant
        physical_points = barycentric @ coordinates
        physical_weights = reference_weights * determinant
        if potential_function is None:
            potential, exponent = henon_potential(physical_points, mesh.spec.a)
            maximum_exponent = max(maximum_exponent, float(np.max(exponent)))
        else:
            potential = np.asarray(potential_function(physical_points), dtype=float)
            if potential.shape == ():
                potential = np.full(len(physical_points), float(potential))
            if potential.shape != (len(physical_points),):
                raise ValueError("potential_function must return one value per point")
        potential = potential + constant_potential_shift
        maximum_potential = max(maximum_potential, float(np.max(potential)))

        mass_local = np.einsum(
            "q,qi,qj->ij", physical_weights, barycentric, barycentric
        )
        kinetic_local = 0.5 * area * (gradients @ gradients.T)
        x = physical_points[:, 0]
        y = physical_points[:, 1]
        vector_potential = 0.5 * magnetic_field * np.column_stack((-y, x))
        scalar = potential + 0.5 * np.sum(vector_potential**2, axis=1)
        scalar_local = np.einsum(
            "q,q,qi,qj->ij",
            physical_weights,
            scalar,
            barycentric,
            barycentric,
        )
        a_dot_grad = vector_potential @ gradients.T
        magnetic_bracket = np.einsum(
            "q,qi,qj->ij", physical_weights, barycentric, a_dot_grad
        )
        magnetic_bracket = magnetic_bracket - magnetic_bracket.T
        local_stiffness = kinetic_local + scalar_local + 0.5j * magnetic_bracket

        is_boundary_layer = bool(np.any(mesh.boundary_mask[triangle]))
        if is_boundary_layer:
            boundary_layer_triangle_count += 1
            boundary_layer_area += area
        integrated_area += area
        local_dofs = mesh.global_to_dof[triangle]
        for local_i in range(3):
            dof_i = int(local_dofs[local_i])
            if dof_i < 0:
                continue
            for local_j in range(3):
                dof_j = int(local_dofs[local_j])
                if dof_j < 0:
                    continue
                rows.append(dof_i)
                columns.append(dof_j)
                stiffness_data.append(local_stiffness[local_i, local_j])
                mass_data.append(float(mass_local[local_i, local_j]))
                layer_data.append(
                    float(mass_local[local_i, local_j]) if is_boundary_layer else 0.0
                )

    dof_count = len(mesh.interior_indices)
    # Use one complex assembly path for B=0 and B=+-1.
    dtype = complex
    stiffness = sparse.coo_matrix(
        (np.asarray(stiffness_data, dtype=dtype), (rows, columns)),
        shape=(dof_count, dof_count),
        dtype=dtype,
    ).tocsr()
    mass = sparse.coo_matrix(
        (np.asarray(mass_data, dtype=float), (rows, columns)),
        shape=(dof_count, dof_count),
        dtype=float,
    ).tocsr()
    boundary_layer_mass = sparse.coo_matrix(
        (np.asarray(layer_data, dtype=float), (rows, columns)),
        shape=(dof_count, dof_count),
        dtype=float,
    ).tocsr()
    for matrix in (stiffness, mass, boundary_layer_mass):
        matrix.sum_duplicates()
        matrix.eliminate_zeros()

    stiffness_defect = stiffness - stiffness.conjugate().T
    mass_defect = mass - mass.T
    stiffness_scale = max(
        float(np.max(np.abs(stiffness.data), initial=0.0)), np.finfo(float).tiny
    )
    mass_scale = max(
        float(np.max(np.abs(mass.data), initial=0.0)), np.finfo(float).tiny
    )
    smallest_mass_eigenvalue = float(
        eigsh(mass, k=1, which="SA", return_eigenvectors=False, tol=1.0e-11)[0]
    )
    metadata: dict[str, Any] = {
        "magnetic_field": float(magnetic_field),
        "quadrature_order": int(quadrature_order),
        "dof_count": int(dof_count),
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
            np.max(np.abs(stiffness_defect.data), initial=0.0) / stiffness_scale
        ),
        "raw_mass_symmetry_relative_max": float(
            np.max(np.abs(mass_defect.data), initial=0.0) / mass_scale
        ),
        "smallest_mass_eigenvalue": smallest_mass_eigenvalue,
        "mass_positive_definite": bool(smallest_mass_eigenvalue > 0.0),
        "boundary_layer_triangle_count": int(boundary_layer_triangle_count),
        "boundary_layer_area": float(boundary_layer_area),
        "boundary_layer_area_fraction": float(boundary_layer_area / integrated_area),
        "potential_function": (
            "independent centered Henon exponential"
            if potential_function is None
            else "caller-supplied test potential"
        ),
        "constant_potential_shift": float(constant_potential_shift),
    }
    return FEMAssembly(
        stiffness=stiffness,
        mass=mass,
        boundary_layer_mass=boundary_layer_mass,
        metadata=metadata,
    )


def deterministic_start(size: int) -> np.ndarray:
    index = np.arange(size, dtype=float)
    vector = np.sin((index + 1.0) * sqrt(2.0)) + 0.5 * np.cos(
        (index + 1.0) * sqrt(3.0)
    )
    return vector / np.linalg.norm(vector)


def solve_generalized_eigensystem(
    assembly: FEMAssembly,
    count: int,
    *,
    tolerance: float = 2.0e-10,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, Any]]:
    """Solve Kc=lambda Mc and return generalized audit diagnostics."""

    stiffness = assembly.stiffness
    mass = assembly.mass
    if count >= stiffness.shape[0] - 1:
        raise ValueError("count must be smaller than the interior DOF count minus one")
    start = deterministic_start(stiffness.shape[0]).astype(stiffness.dtype)
    start /= sqrt(float(np.real(start.conjugate() @ (mass @ start))))
    ncv = min(stiffness.shape[0] - 1, max(2 * count + 1, 20))
    values, vectors = eigsh(
        stiffness,
        k=count,
        M=mass,
        sigma=0.0,
        which="LM",
        tol=tolerance,
        maxiter=max(5000, 30 * count),
        v0=start,
        ncv=ncv,
    )
    order = np.argsort(values.real, kind="mergesort")
    values = np.asarray(values.real[order], dtype=float)
    vectors = np.asarray(vectors[:, order])
    kv = stiffness @ vectors
    mv = mass @ vectors
    residual_matrix = kv - mv * values[np.newaxis, :]
    residual_norms = np.linalg.norm(residual_matrix, axis=0)
    equation_scale = np.maximum(
        1.0, np.abs(values) * np.linalg.norm(mv, axis=0)
    )
    residuals = residual_norms / equation_scale
    backward_scale = np.maximum(
        np.linalg.norm(kv, axis=0)
        + np.abs(values) * np.linalg.norm(mv, axis=0),
        np.finfo(float).tiny,
    )
    backward_residuals = residual_norms / backward_scale
    gram = vectors.conjugate().T @ mv
    orthogonality_defect = float(
        np.max(np.abs(gram - np.eye(count)), initial=0.0)
    )
    # Protocol gate: M^{-1}-dual residual, evaluated for all retained and
    # guard Ritz vectors without forming an inverse.
    mass_factor = splu(mass.astype(complex).tocsc())
    dual_solutions = mass_factor.solve(np.asarray(residual_matrix, dtype=complex))
    dual_squared = np.real(
        np.einsum("ik,ik->k", residual_matrix.conjugate(), dual_solutions)
    )
    dual_squared = np.maximum(dual_squared, 0.0)
    mass_norms = np.sqrt(
        np.real(np.einsum("ik,ik->k", vectors.conjugate(), mv))
    )
    dual_residuals = np.sqrt(dual_squared) / (
        np.maximum(np.abs(values), 1.0) * mass_norms
    )
    layer_mass = assembly.boundary_layer_mass
    layer_fractions = np.real(
        np.einsum("ik,ik->k", vectors.conjugate(), layer_mass @ vectors)
    ) / np.real(np.einsum("ik,ik->k", vectors.conjugate(), mv))
    layer_area_fraction = float(assembly.metadata["boundary_layer_area_fraction"])
    anomaly = (layer_fractions > 0.50) & (
        layer_fractions / max(layer_area_fraction, np.finfo(float).tiny) > 5.0
    )
    orthogonality_matrix = gram - np.eye(count)
    metadata: dict[str, Any] = {
        "count": int(count),
        "lowest_eigenvalue": float(values[0]),
        "highest_eigenvalue": float(values[-1]),
        "monotone": bool(np.all(np.diff(values) >= 0.0)),
        "maximum_equation_scaled_residual": float(np.max(residuals)),
        "median_equation_scaled_residual": float(np.median(residuals)),
        "maximum_backward_residual": float(np.max(backward_residuals)),
        "maximum_mass_dual_relative_residual": float(np.max(dual_residuals)),
        "mass_dual_residual_definition": (
            "sqrt(r^* M^-1 r)/(max(abs(lambda),1)*sqrt(c^* M c)); all Ritz pairs"
        ),
        "maximum_mass_orthogonality_defect": orthogonality_defect,
        "mass_orthogonality_frobenius_defect": float(
            np.linalg.norm(orthogonality_matrix)
        ),
        "mass_orthogonality_spectral_defect": float(
            np.linalg.norm(orthogonality_matrix, ord=2)
        ),
        "maximum_boundary_layer_mass_fraction": float(np.max(layer_fractions)),
        "maximum_first80_boundary_layer_mass_fraction": float(
            np.max(layer_fractions[: min(80, len(layer_fractions))])
        ),
        "boundary_localization_threshold": 0.50,
        "boundary_localization_area_ratio_threshold": 5.0,
        "boundary_layer_area_fraction": layer_area_fraction,
        "anomalous_boundary_localized_mode": bool(
            np.any(anomaly[: min(80, len(anomaly))])
        ),
        "solver": "scipy.sparse.linalg.eigsh generalized shift-invert",
        "solver_tolerance": float(tolerance),
        "deterministic_start": True,
        "ncv": int(ncv),
    }
    arrays = np.column_stack(
        (residuals, backward_residuals, dual_residuals, layer_fractions)
    )
    return values, vectors, arrays, metadata


def potential_boundary_participation(
    mesh: FEMMesh,
    vectors: np.ndarray,
    *,
    radius_fraction: float = 0.90,
    quadrature_order: int = 7,
) -> tuple[np.ndarray, dict[str, Any]]:
    """Measure eigenfunction mass in the high-potential boundary band."""

    if not 0.0 < radius_fraction < 1.0:
        raise ValueError("radius_fraction must lie between zero and one")
    coefficient_matrix = np.asarray(vectors)
    if coefficient_matrix.shape[0] != len(mesh.interior_indices):
        raise ValueError("vector row count does not match the mesh DOF count")
    barycentric, reference_weights = duffy_gauss_rule(quadrature_order)
    numerator = np.zeros(coefficient_matrix.shape[1], dtype=float)
    denominator = np.zeros(coefficient_matrix.shape[1], dtype=float)
    full_coefficients = np.zeros(
        (len(mesh.u_vertices), coefficient_matrix.shape[1]), dtype=complex
    )
    full_coefficients[mesh.interior_indices] = coefficient_matrix
    radius = wall_radius(mesh.spec.wall_energy)
    threshold_potential = TWO_PI * np.exp(
        pi * (radius_fraction * radius) ** 2
    )

    for triangle in mesh.triangles:
        coordinates = mesh.q_vertices[triangle]
        _, determinant = _p1_gradients(coordinates)
        physical_points = barycentric @ coordinates
        physical_weights = reference_weights * determinant
        potential, _ = henon_potential(physical_points, mesh.spec.a)
        values = barycentric @ full_coefficients[triangle]
        density = np.abs(values) ** 2
        denominator += np.sum(physical_weights[:, None] * density, axis=0)
        mask = potential >= threshold_potential
        if np.any(mask):
            numerator += np.sum(
                physical_weights[mask, None] * density[mask], axis=0
            )
    fractions = numerator / np.maximum(denominator, np.finfo(float).tiny)
    metadata: dict[str, Any] = {
        "radius_fraction": float(radius_fraction),
        "quadrature_order": int(quadrature_order),
        "threshold_potential": float(threshold_potential),
        "mode_count": int(coefficient_matrix.shape[1]),
        "minimum_denominator": float(np.min(denominator)),
        "maximum_denominator": float(np.max(denominator)),
        "maximum_participation": float(np.max(fractions)),
        "localization_threshold": 0.10,
    }
    return fractions, metadata


def structured_square_mesh(subdivisions: int) -> FEMMesh:
    """Return a unit-square test mesh with counter-clockwise triangles."""

    if subdivisions < 2:
        raise ValueError("subdivisions must be at least two")
    axis = np.linspace(0.0, 1.0, subdivisions + 1)
    xx, yy = np.meshgrid(axis, axis, indexing="xy")
    vertices = np.column_stack((xx.ravel(), yy.ravel()))
    triangles: list[tuple[int, int, int]] = []
    width = subdivisions + 1
    for j in range(subdivisions):
        for i in range(subdivisions):
            lower_left = j * width + i
            lower_right = lower_left + 1
            upper_left = lower_left + width
            upper_right = upper_left + 1
            triangles.append((lower_left, lower_right, upper_right))
            triangles.append((lower_left, upper_right, upper_left))
    triangles_array = np.asarray(triangles, dtype=int)
    boundary_mask = (
        np.isclose(vertices[:, 0], 0.0)
        | np.isclose(vertices[:, 0], 1.0)
        | np.isclose(vertices[:, 1], 0.0)
        | np.isclose(vertices[:, 1], 1.0)
    )
    interior = np.flatnonzero(~boundary_mask)
    global_to_dof = np.full(len(vertices), -1, dtype=int)
    global_to_dof[interior] = np.arange(len(interior))
    return FEMMesh(
        spec=FEMMeshSpec(
            h_u=1.0 / subdivisions,
            a=0.0,
            wall_energy=100.0,
            boundary_vertices=int(np.sum(boundary_mask)),
        ),
        u_vertices=vertices.copy(),
        q_vertices=vertices.copy(),
        triangles=triangles_array,
        boundary_mask=boundary_mask,
        interior_indices=interior,
        global_to_dof=global_to_dof,
        lattice_ij=np.full((len(vertices), 2), np.iinfo(np.int32).min, dtype=np.int64),
        metadata={
            "mapped_polygon_area": 1.0,
            "interior_dof_count": int(len(interior)),
            "triangle_count": int(len(triangles_array)),
            "test_mesh": "unit square",
        },
    )
