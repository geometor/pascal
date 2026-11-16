"""Comprehensive test suite for ``geometor.pascal`` exact symbolic projective geometry."""
from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp
import sympy.geometry as spg

from geometor.pascal import (
    PHI,
    are_coconic,
    canonical_hexagon_cycle,
    circle_stereographic_point,
    conic_cross_ratio,
    conic_equation_through_points,
    construct_pascal_hexagon,
    construct_pascal_steiner_family,
    enumerate_hexagrammum_mysticum,
    find_golden_sections,
    get_pascal_preset,
    render_svg_string,
    verify_pascal_symbolic,
)
from geometor.pascal.__main__ import main


def test_universal_pascal_symbolic_proof() -> None:
    """Verify Pascal's Hexagrammum Mysticum vanishes identically over Z[t0..t5]."""
    assert verify_pascal_symbolic() == 0


def test_conic_equation_and_coconicity() -> None:
    """are_coconic unifies smooth circles and ellipses."""
    for t_val in (sp.Integer(0), sp.Rational(1, 3), PHI):
        pt = circle_stereographic_point(t_val)
        assert sp.simplify(pt.x**2 + pt.y**2 - 1) == 0

    x_sym, y_sym = sp.Symbol("x"), sp.Symbol("y")
    circ_pts = get_pascal_preset("hexagrammum").points
    circ_poly = conic_equation_through_points(circ_pts[:5])
    assert circ_poly != 0
    assert sp.simplify(circ_poly / (x_sym**2 + y_sym**2 - 1)).is_Rational

    ell_pts = get_pascal_preset("ellipse").points
    ell_poly = conic_equation_through_points(ell_pts[:5])
    assert sp.simplify(ell_poly / (x_sym**2 + 4 * y_sym**2 - 4)).is_Rational

    assert are_coconic(circ_pts) is True
    assert are_coconic(ell_pts) is True

    off_conic = list(circ_pts[:5]) + [spg.Point(sp.Integer(2), sp.Integer(3))]
    assert are_coconic(off_conic) is False


def test_chasles_conic_cross_ratio_observer_invariance_and_golden() -> None:
    """Chasles conic cross-ratio is observer-independent and equals PHI on golden_conic."""
    c_pts = get_pascal_preset("hexagrammum").points
    obs_extra = circle_stereographic_point(sp.Integer(2))
    cr_from_p4 = conic_cross_ratio(c_pts[0], c_pts[1], c_pts[2], c_pts[3], c_pts[4])
    cr_from_p5 = conic_cross_ratio(c_pts[0], c_pts[1], c_pts[2], c_pts[3], c_pts[5])
    cr_from_extra = conic_cross_ratio(c_pts[0], c_pts[1], c_pts[2], c_pts[3], obs_extra)
    assert sp.simplify(cr_from_p4 - cr_from_p5) == 0
    assert sp.simplify(cr_from_p4 - cr_from_extra) == 0

    g_pts = get_pascal_preset("golden_conic").points
    g_cr_4 = conic_cross_ratio(g_pts[0], g_pts[1], g_pts[2], g_pts[3], g_pts[4])
    g_cr_5 = conic_cross_ratio(g_pts[0], g_pts[1], g_pts[2], g_pts[3], g_pts[5])
    assert sp.simplify(g_cr_4 - PHI) == 0
    assert sp.simplify(g_cr_5 - PHI) == 0


@pytest.mark.parametrize(
    "cycle",
    [(0, 2, 4, 1, 3, 5), (0, 1, 2, 3, 4, 5), (0, 2, 5, 1, 3, 4)],
)
@pytest.mark.parametrize("preset_name", ["hexagrammum", "convex", "ellipse", "golden_conic"])
def test_pascal_hexagon_collinearity_all_presets_and_cycles(
    preset_name: str,
    cycle: tuple[int, int, int, int, int, int],
) -> None:
    """Every cycle across all four smooth-conic presets yields collinear Pascal meets."""
    res = construct_pascal_hexagon(preset=preset_name, cycle=cycle)
    assert res.is_coconic is True
    assert res.is_collinear is True
    assert len(res.finite_meets) >= 2
    for pt in res.finite_meets:
        assert res.pascal_line.contains(pt)
        assert not isinstance(pt.x, sp.Float)
        assert not isinstance(pt.y, sp.Float)


def test_pascal_exact_coordinates_circle_and_ellipse() -> None:
    """Verify exact rational coordinates on Pythagorean circle and affine ellipse."""
    hex_res = construct_pascal_hexagon(preset="hexagrammum")
    assert hex_res.meets["M03"] == spg.Point(sp.Rational(2, 5), sp.Rational(3, 5))
    assert hex_res.meets["M14"] == spg.Point(sp.Rational(-3, 10), sp.Rational(1, 10))
    assert hex_res.meets["M25"] == spg.Point(sp.Rational(9, 5), sp.Rational(8, 5))

    ell_res = construct_pascal_hexagon(preset="ellipse")
    assert ell_res.meets["M03"] == spg.Point(sp.Rational(4, 5), sp.Rational(3, 5))
    assert ell_res.meets["M14"] == spg.Point(sp.Rational(-3, 5), sp.Rational(1, 10))
    assert ell_res.meets["M25"] == spg.Point(sp.Rational(18, 5), sp.Rational(8, 5))

    with pytest.raises(KeyError):
        get_pascal_preset("unknown_conic")


def test_pascal_steiner_family_concurrency() -> None:
    """Bi-triangle S_3 Pascal lines concur 3-by-3 at Steiner points G+ and G-."""
    fam = construct_pascal_steiner_family(preset="hexagrammum")
    assert len(fam.pascal_lines) == 6
    assert fam.steiner_even == spg.Point(sp.Rational(78, 25), sp.Rational(1, 25))
    assert fam.steiner_odd == spg.Point(sp.Rational(498, 1565), sp.Rational(281, 1565))
    assert fam.steiner_line is not None
    for ln in fam.even_pascal_lines:
        assert ln.contains(fam.steiner_even)
    for ln in fam.odd_pascal_lines:
        assert ln.contains(fam.steiner_odd)


def test_hexagrammum_mysticum_complete_60_line_catalog() -> None:
    """Enumerate all 15 chords, 45 diagonal pts, 60 Pascal lines, 20 Steiner, 60 Kirkman, 15 Plucker."""
    base = (0, 2, 4, 1, 3, 5)
    canon = canonical_hexagon_cycle(base)
    for shift in range(6):
        rot = base[shift:] + base[:shift]
        assert canonical_hexagon_cycle(rot) == canon
        assert canonical_hexagon_cycle(tuple(reversed(rot))) == canon

    cat = enumerate_hexagrammum_mysticum(preset="hexagrammum")
    assert len(cat.chords) == 15
    assert len(set(cat.chords.values())) == 15
    assert len(cat.diagonal_points) == 45
    assert len(set(cat.diagonal_points.values())) == 45
    assert len(cat.pascal_lines) == 60
    assert len(set(cat.pascal_lines.values())) == 60
    assert len(cat.steiner_points) == 20
    assert len(set(cat.steiner_points.values())) == 20
    assert len(cat.kirkman_points) == 60
    assert len(set(cat.kirkman_points.values())) == 60
    assert len(cat.plucker_lines) == 15
    assert len(set(cat.plucker_lines)) == 15


def test_golden_pascal_emergent_divine_section_and_conic_svg() -> None:
    """Golden conic discovers / M25 P4 P0 / with ratio PHI and renders circle/ellipse."""
    gold = construct_pascal_hexagon(preset="golden_conic", enable_divine=True)
    m25 = gold.meets["M25"]
    assert m25 is not None
    assert sp.simplify(m25.x - (-1 / PHI)) == 0
    assert sp.simplify(m25.y - (-PHI)) == 0

    secs = find_golden_sections(gold.model, register_sections=True)
    sec_ids = {gs.point_ids for gs in secs}
    assert ("M25", "P4", "P0") in sec_ids or ("P0", "P4", "M25") in sec_ids
    for gs in secs:
        assert sp.simplify(gs.ratio - PHI) == 0

    svg_gold = ET.fromstring(render_svg_string(gold.model, graphic_id="g4"))
    gold_refs = {el.attrib["data-ref"] for el in svg_gold.iter() if "data-ref" in el.attrib}
    assert "( O P0 )" in gold_refs
    assert "/ M25 P4 P0 /" in gold_refs

    ell = construct_pascal_hexagon(preset="ellipse")
    svg_ell = ET.fromstring(render_svg_string(ell.model, graphic_id="g2"))
    tags = {el.tag.split("}")[-1] for el in svg_ell.iter()}
    assert "ellipse" in tags


def test_cli_subcommands(tmp_path: Path) -> None:
    """Exercise Pascal CLI commands."""
    assert main(["inspect", "--preset", "hexagrammum"]) == 0
    assert main(["steiner", "--preset", "hexagrammum"]) == 0
    assert main(["catalog", "--preset", "hexagrammum"]) == 0
    assert main(["verify"]) == 0
    gallery_dir = tmp_path / "gallery"
    assert main(["build", "-o", str(gallery_dir)]) == 0
    svgs = sorted(gallery_dir.glob("*.svg"))
    assert len(svgs) == 4
    for svg_file in svgs:
        ET.fromstring(svg_file.read_text(encoding="utf-8"))
