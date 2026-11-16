"""Exact symbolic constructions and combinatorics for Blaise Pascal's *Hexagrammum Mysticum* (1640).

The 1640 broadside *Essay pour les coniques* generalized Pappus's Hexagon
Theorem from two straight lines to any smooth conic section.
"""
from __future__ import annotations

from .hexagrammum import (
    PERMUTATIONS_S3,
    Cycle6,
    HexagrammumMysticumCatalog,
    PASCAL_PRESETS,
    PascalHexagonResult,
    PascalPresetConfig,
    PascalSteinerFamilyResult,
    Perm3,
    canonical_hexagon_cycle,
    construct_pascal_hexagon,
    construct_pascal_steiner_family,
    enumerate_hexagrammum_mysticum,
    get_pascal_preset,
    verify_pascal_symbolic,
)
from .projective import (
    PHI,
    GoldenRange,
    HarmonicRange,
    are_coconic,
    circle_stereographic_point,
    conic_cross_ratio,
    conic_equation_through_points,
    cross_ratio,
    enable_divine_analysis,
    exact_line_meet,
    find_golden_sections,
    find_harmonic_ranges,
    line_spread,
    quadrance,
)
from .render import (
    EMBEDDED_SVG_STYLE,
    export_svg,
    render_svg_string,
)

__version__ = "0.1.0"

__all__ = [
    "__version__",
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
    "Cycle6",
    "Perm3",
    "PERMUTATIONS_S3",
    "PascalPresetConfig",
    "PASCAL_PRESETS",
    "PascalHexagonResult",
    "PascalSteinerFamilyResult",
    "HexagrammumMysticumCatalog",
    "canonical_hexagon_cycle",
    "get_pascal_preset",
    "construct_pascal_hexagon",
    "construct_pascal_steiner_family",
    "enumerate_hexagrammum_mysticum",
    "verify_pascal_symbolic",
    "EMBEDDED_SVG_STYLE",
    "render_svg_string",
    "export_svg",
]
