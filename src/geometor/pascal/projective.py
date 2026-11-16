"""Exact symbolic projective geometry and conic primitives for Blaise Pascal's constructions.

Provides 100% exact SymPy implementations of rational stereographic circle
parameterization, five-point Veronese conic equations, coconicity tests,
Michel Chasles's cross-ratio on conics, line meets, and integration with
:mod:`geometor.divine` for emergent golden section detection.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

import sympy as sp
import sympy.geometry as spg
from geometor.divine import register_divine_hook
from geometor.model import Model
from geometor.model.sections import Section
from geometor.model.utils import clean_expr, sort_points

PHI: sp.Expr = sp.Rational(1, 2) + sp.sqrt(5) / 2

__all__ = [
    "PHI",
    "HarmonicRange",
    "GoldenRange",
    "quadrance",
    "line_spread",
    "exact_line_meet",
    "cross_ratio",
    "circle_stereographic_point",
    "conic_equation_through_points",
    "are_coconic",
    "conic_cross_ratio",
    "find_harmonic_ranges",
    "find_golden_sections",
    "enable_divine_analysis",
]


@dataclass(frozen=True)
class HarmonicRange:
    """Represents four ordered collinear points forming a harmonic range (P1, P3; P2, P4) = -1.

    Attributes:
        points: Ordered tuple (P1, P2, P3, P4) along the carrier line.
        point_ids: Corresponding model IDs of the four points.
        line: Carrier line in the model, if associated with one.
        line_id: Model ID of the carrier line.
        value: Exact symbolic cross-ratio (P1, P3; P2, P4) = -1.
    """

    points: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    point_ids: tuple[str, str, str, str]
    line: spg.Line | None
    line_id: str
    value: sp.Expr = sp.Integer(-1)


@dataclass(frozen=True)
class GoldenRange:
    r"""Represents three ordered collinear points dividing a segment in the Golden Ratio \phi.

    Attributes:
        section: Underlying Section object.
        point_ids: Ordered model IDs (P1, P2, P3) of the three points.
        line: Carrier line in the model, if associated with one.
        line_id: Model ID of the carrier line.
        ratio: Exact symbolic ratio of longer to shorter segment (\phi).
    """

    section: Section
    point_ids: tuple[str, str, str]
    line: spg.Line | None
    line_id: str
    ratio: sp.Expr


def quadrance(pt_1: spg.Point, pt_2: spg.Point) -> sp.Expr:
    """Compute the exact rational-trigonometric quadrance Q(P1, P2)."""
    return clean_expr((pt_2.x - pt_1.x) ** 2 + (pt_2.y - pt_1.y) ** 2)


def line_spread(line_1: spg.Line, line_2: spg.Line) -> sp.Expr:
    r"""Compute the exact rational-trigonometric spread s(l1, l2) = sin^2(theta)."""
    a1, b1, _ = line_1.coefficients
    a2, b2, _ = line_2.coefficients
    num = (a1 * b2 - a2 * b1) ** 2
    den = (a1**2 + b1**2) * (a2**2 + b2**2)
    return clean_expr(sp.cancel(num / den))


def exact_line_meet(line_1: spg.Line, line_2: spg.Line) -> spg.Point | None:
    """Compute the exact intersection of two lines via Cramer's rule.

    Returns None when the two lines are parallel or coincident.
    """
    a1, b1, c1 = line_1.coefficients
    a2, b2, c2 = line_2.coefficients
    det = sp.cancel(a1 * b2 - a2 * b1)
    if not det.free_symbols:
        if det.is_Rational:
            if det == 0:
                return None
        elif abs(complex(det.evalf(30))) < 1e-22 and sp.simplify(det) == 0:
            return None
    elif sp.simplify(det) == 0:
        return None

    x_coord = clean_expr(sp.cancel((b1 * c2 - b2 * c1) / det))
    y_coord = clean_expr(sp.cancel((c1 * a2 - c2 * a1) / det))
    return spg.Point(x_coord, y_coord)


def cross_ratio(
    a: spg.Point,
    b: spg.Point,
    c: spg.Point,
    d: spg.Point,
) -> sp.Expr:
    r"""Compute the exact collinear cross-ratio (A, B; C, D) = (AC/CB) / (AD/DB)."""
    dx = b.x - a.x
    if sp.simplify(dx) != 0:
        coord_fn = lambda pt: pt.x
    else:
        coord_fn = lambda pt: pt.y

    xa, xb, xc, xd = coord_fn(a), coord_fn(b), coord_fn(c), coord_fn(d)
    num = (xc - xa) * (xb - xd)
    den = (xb - xc) * (xd - xa)

    if sp.simplify(den) == 0:
        return sp.oo
    return clean_expr(sp.cancel(num / den))


def _line_contains_fast(line: spg.Line, pt: spg.Point) -> bool:
    a, b, c = line.coefficients
    val = sp.simplify(a * pt.x + b * pt.y + c)
    return val == 0


def find_harmonic_ranges(
    model: Model,
    *,
    include_guides: bool = False,
) -> list[HarmonicRange]:
    """Scan collinear points in model for harmonic tetrads (P1, P3; P2, P4) = -1."""
    candidate_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    candidate_points = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]

    discovered: list[HarmonicRange] = []
    seen_tetrads: set[tuple[spg.Point, spg.Point, spg.Point, spg.Point]] = set()

    for ln in candidate_lines:
        pts_on_line = [pt for pt in candidate_points if _line_contains_fast(ln, pt)]
        if len(pts_on_line) < 4:
            continue

        ordered_pts = sort_points(pts_on_line)
        ln_id = model[ln].ID if ln in model else ""

        for p1, p2, p3, p4 in combinations(ordered_pts, 4):
            key = (p1, p2, p3, p4)
            if key in seen_tetrads:
                continue
            cr = cross_ratio(p1, p3, p2, p4)
            if cr != sp.oo and sp.simplify(cr - (-1)) == 0:
                seen_tetrads.add(key)
                discovered.append(
                    HarmonicRange(
                        points=key,
                        point_ids=(
                            model[p1].ID,
                            model[p2].ID,
                            model[p3].ID,
                            model[p4].ID,
                        ),
                        line=ln,
                        line_id=ln_id,
                    )
                )

    return discovered


def find_golden_sections(
    model: Model,
    *,
    register_sections: bool = False,
    include_guides: bool = False,
) -> list[GoldenRange]:
    r"""Scan collinear points in model for golden sections with ratio \phi."""
    candidate_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    candidate_points = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]

    discovered: list[GoldenRange] = []
    seen_triples: set[tuple[spg.Point, spg.Point, spg.Point]] = set()

    for ln in candidate_lines:
        pts_on_line = [pt for pt in candidate_points if _line_contains_fast(ln, pt)]
        if len(pts_on_line) < 3:
            continue

        ordered_pts = sort_points(pts_on_line)
        ln_id = model[ln].ID if ln in model else ""

        for p1, p2, p3 in combinations(ordered_pts, 3):
            key = (p1, p2, p3)
            if key in seen_triples:
                continue
            sec = Section([p1, p2, p3])
            if sec.is_golden:
                seen_triples.add(key)
                if register_sections:
                    model.set_section([p1, p2, p3], classes=["golden"])
                exact_ratio = PHI if sp.simplify(sec.ratio - PHI) == 0 else clean_expr(sec.ratio)
                discovered.append(
                    GoldenRange(
                        section=sec,
                        point_ids=(model[p1].ID, model[p2].ID, model[p3].ID),
                        line=ln,
                        line_id=ln_id,
                        ratio=exact_ratio,
                    )
                )

    return discovered


def enable_divine_analysis(model: Model) -> Model:
    """Attach geometor.divine hook to model and return it."""
    register_divine_hook(model)
    return model


def circle_stereographic_point(
    t: sp.Expr | int,
    *,
    center: spg.Point | tuple[sp.Expr | int, sp.Expr | int] = (0, 0),
    radius: sp.Expr | int = 1,
) -> spg.Point:
    r"""Compute an exact point on (x - x0)^2 + (y - y0)^2 = R^2 via rational stereographic slope t.

    P(t) = (x0 + R * (1 - t^2) / (1 + t^2), y0 + R * (2t) / (1 + t^2)).
    """
    t_sym = sp.sympify(t)
    r_sym = sp.sympify(radius)
    c_pt = center if isinstance(center, spg.Point) else spg.Point(sp.sympify(center[0]), sp.sympify(center[1]))
    denom = 1 + t_sym**2
    x_coord = sp.simplify(c_pt.x + r_sym * (1 - t_sym**2) / denom)
    y_coord = sp.simplify(c_pt.y + r_sym * (2 * t_sym) / denom)
    return spg.Point(x_coord, y_coord)


def conic_equation_through_points(
    points: Sequence[spg.Point | tuple[sp.Expr | int, sp.Expr | int]],
) -> sp.Expr:
    r"""Construct the exact quadratic conic polynomial C(x, y) through five points."""
    if len(points) != 5:
        raise ValueError(f"Expected exactly 5 points to determine a conic, got {len(points)}.")
    x_sym, y_sym = sp.Symbol("x"), sp.Symbol("y")
    rows: list[list[sp.Expr]] = [[x_sym**2, x_sym * y_sym, y_sym**2, x_sym, y_sym, sp.Integer(1)]]
    for raw in points:
        pt = raw if isinstance(raw, spg.Point) else spg.Point(sp.sympify(raw[0]), sp.sympify(raw[1]))
        rows.append([pt.x**2, pt.x * pt.y, pt.y**2, pt.x, pt.y, sp.Integer(1)])
    return sp.expand(sp.Matrix(rows).det())


def are_coconic(
    points: Sequence[spg.Point | tuple[sp.Expr | int, sp.Expr | int]],
) -> bool:
    r"""Return True iff all given points lie on a single conic."""
    if len(points) <= 5:
        return True
    rows: list[list[sp.Expr]] = []
    for raw in points:
        pt = raw if isinstance(raw, spg.Point) else spg.Point(sp.sympify(raw[0]), sp.sympify(raw[1]))
        rows.append([pt.x**2, pt.x * pt.y, pt.y**2, pt.x, pt.y, sp.Integer(1)])
    return int(sp.Matrix(rows).rank()) <= 5


def conic_cross_ratio(
    p1: spg.Point,
    p2: spg.Point,
    p3: spg.Point,
    p4: spg.Point,
    observer: spg.Point,
) -> sp.Expr:
    r"""Compute Michel Chasles's projective cross-ratio (P1, P2; P3, P4) on a conic."""
    pts5 = (p1, p2, p3, p4, observer)
    if len(set(pts5)) != 5:
        raise ValueError("All four target points and observer must be distinct.")
    if not are_coconic(pts5):
        raise ValueError("Points do not lie on a common conic.")

    rays = [spg.Line(observer, pk) for pk in (p1, p2, p3, p4)]
    candidates = (
        spg.Line(spg.Point(0, 0), spg.Point(1, 0)),
        spg.Line(spg.Point(0, 1), spg.Point(1, 1)),
        spg.Line(spg.Point(0, 2), spg.Point(1, 5)),
    )
    transversal = next(ln for ln in candidates if not ln.contains(observer))
    cuts = [exact_line_meet(ray, transversal) for ray in rays]
    return cross_ratio(cuts[0], cuts[1], cuts[2], cuts[3])
