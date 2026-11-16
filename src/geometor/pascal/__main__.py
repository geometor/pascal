"""Command-line interface for ``geometor.pascal``."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rich.console import Console
from rich.table import Table

from geometor.pascal import (
    PHI,
    PASCAL_PRESETS,
    conic_cross_ratio,
    conic_equation_through_points,
    construct_pascal_hexagon,
    construct_pascal_steiner_family,
    enumerate_hexagrammum_mysticum,
    export_svg,
    find_golden_sections,
    verify_pascal_symbolic,
)


def _cmd_inspect(args: argparse.Namespace, console: Console) -> int:
    preset = args.preset
    cycle = tuple(int(x) for x in args.cycle.split(",")) if args.cycle else None
    res = construct_pascal_hexagon(preset=preset, cycle=cycle)
    conic_poly = conic_equation_through_points(res.points[:5])

    tbl = Table(title=f"Pascal Hexagon ({preset})")
    tbl.add_column("Element", style="cyan bold")
    tbl.add_column("Exact SymPy Value", style="green")

    for idx, pt in enumerate(res.points):
        tbl.add_row(f"P{idx}", f"({pt.x}, {pt.y})")
    for mid in ("M03", "M14", "M25"):
        m_pt = res.meets[mid]
        tbl.add_row(mid, f"({m_pt.x}, {m_pt.y})" if m_pt else "∞ (parallel)")
    tbl.add_row("Pascal Line", f"{res.pascal_line.equation()} = 0")
    tbl.add_row("Conic Polynomial", f"{conic_poly} = 0")
    tbl.add_row("Collinear?", str(res.is_collinear))
    tbl.add_row("Coconic?", str(res.is_coconic))

    console.print(tbl)
    if args.output:
        out_path = Path(args.output)
        export_svg(res.model, out_path)
        console.print(f"[bold green]✓ Exported SVG to {out_path}[/bold green]")
    return 0


def _cmd_steiner(args: argparse.Namespace, console: Console) -> int:
    preset = args.preset
    fam = construct_pascal_steiner_family(preset=preset)

    tbl = Table(title=f"Pascal Bi-Triangle S_3 Steiner Family ({preset})")
    tbl.add_column("Permutation / Point", style="cyan bold")
    tbl.add_column("Line / Coordinates", style="green")

    for perm, ln in fam.pascal_lines.items():
        parity = "even" if perm in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else "odd"
        tbl.add_row(f"{perm} ({parity})", f"{ln.equation()} = 0")
    if fam.steiner_even:
        tbl.add_row("G+ (even Steiner point)", f"({fam.steiner_even.x}, {fam.steiner_even.y})")
    if fam.steiner_odd:
        tbl.add_row("G- (odd Steiner point)", f"({fam.steiner_odd.x}, {fam.steiner_odd.y})")

    console.print(tbl)
    if args.output:
        out_path = Path(args.output)
        export_svg(fam.model, out_path)
        console.print(f"[bold green]✓ Exported SVG to {out_path}[/bold green]")
    return 0


def _cmd_catalog(args: argparse.Namespace, console: Console) -> int:
    preset = args.preset
    cat = enumerate_hexagrammum_mysticum(preset=preset)

    tbl = Table(title=f"Complete 60-Line Hexagrammum Mysticum Web ({preset})")
    tbl.add_column("Geometric Stratum", style="cyan bold")
    tbl.add_column("Exact Count", justify="right", style="bold yellow")
    tbl.add_column("Notes", style="green")

    tbl.add_row("Conic Vertices", "6", "Inscribed on smooth conic")
    tbl.add_row("Chords [Pi Pj]", str(len(cat.chords)), "15 secant lines")
    tbl.add_row("Pascal Diagonal Points", str(len(set(cat.diagonal_points.values()))), "45 chord intersection points")
    tbl.add_row("Pascal Lines", str(len(set(cat.pascal_lines.values()))), "60 lines (3 diagonal points each)")
    tbl.add_row("Steiner Points", str(len(set(cat.steiner_points.values()))), "20 points (concurrence of 3 Pascal lines)")
    tbl.add_row("Kirkman Points", str(len(set(cat.kirkman_points.values()))), "60 points (concurrence of 3 Pascal lines)")
    tbl.add_row("Plücker Lines", str(len(cat.plucker_lines)), "15 lines (each carrying 4 Steiner points)")

    console.print(tbl)
    return 0


def _cmd_verify(_args: argparse.Namespace, console: Console) -> int:
    det = verify_pascal_symbolic()
    console.print(f"[bold green]✓ Universal 6-symbolic determinant det[M03, M14, M25]:[/bold green] {det}")
    return 0 if det == 0 else 1


def _cmd_build(args: argparse.Namespace, console: Console) -> int:
    out_dir = Path(args.output) if args.output else Path("docs/_static/constructions")
    out_dir.mkdir(parents=True, exist_ok=True)

    m1 = construct_pascal_hexagon(preset="hexagrammum")
    export_svg(m1.model, out_dir / "pascal_hexagrammum.svg", graphic_id="g1")

    m2 = construct_pascal_hexagon(preset="ellipse")
    export_svg(m2.model, out_dir / "pascal_ellipse.svg", graphic_id="g2")

    m3 = construct_pascal_steiner_family(preset="hexagrammum")
    export_svg(m3.model, out_dir / "pascal_steiner_family.svg", graphic_id="g3")

    m4 = construct_pascal_hexagon(preset="golden_conic", enable_divine=True)
    export_svg(m4.model, out_dir / "golden_pascal.svg", graphic_id="g4")

    console.print(f"[bold green]✓ Exported 4 SVGs to {out_dir}[/bold green]")
    return 0


def main(argv: list[str] | None = None) -> int:
    """Main CLI entrypoint for geometor.pascal."""
    parser = argparse.ArgumentParser(
        prog="pascal",
        description="Exact symbolic projective geometry and combinatorics for Blaise Pascal's Hexagrammum Mysticum (1640).",
    )
    subparsers = parser.add_subparsers(dest="command")

    # inspect
    p_insp = subparsers.add_parser("inspect", help="Construct and inspect a Pascal hexagon.")
    p_insp.add_argument("--preset", default="hexagrammum", choices=list(PASCAL_PRESETS.keys()))
    p_insp.add_argument("--cycle", default=None, help="Comma-separated 6-vertex cycle, e.g. '0,2,4,1,3,5'")
    p_insp.add_argument("-o", "--output", default=None, help="Export SVG path")

    # steiner
    p_st = subparsers.add_parser("steiner", help="Construct bi-triangle S_3 Steiner family.")
    p_st.add_argument("--preset", default="hexagrammum", choices=list(PASCAL_PRESETS.keys()))
    p_st.add_argument("-o", "--output", default=None, help="Export SVG path")

    # catalog
    p_cat = subparsers.add_parser("catalog", help="Enumerate complete 60-line web.")
    p_cat.add_argument("--preset", default="hexagrammum", choices=list(PASCAL_PRESETS.keys()))

    # verify
    subparsers.add_parser("verify", help="Prove Pascal's theorem universally over Z[t0..t5].")

    # build
    p_bld = subparsers.add_parser("build", help="Export canonical SVG diagrams.")
    p_bld.add_argument("-o", "--output", default="docsrc/_static/constructions", help="Output directory")

    args = parser.parse_args(argv)
    console = Console()

    if args.command == "inspect":
        return _cmd_inspect(args, console)
    elif args.command == "steiner":
        return _cmd_steiner(args, console)
    elif args.command == "catalog":
        return _cmd_catalog(args, console)
    elif args.command == "verify":
        return _cmd_verify(args, console)
    elif args.command == "build":
        return _cmd_build(args, console)
    else:
        # Default behavior: run inspect
        return _cmd_inspect(argparse.Namespace(preset="hexagrammum", cycle=None, output=None), console)


if __name__ == "__main__":
    sys.exit(main())
