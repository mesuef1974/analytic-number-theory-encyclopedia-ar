#!/usr/bin/env python3
"""Generate the numeric coordinate macros consumed by ``manuscript/figures.tex``.

The visual layer must stay reproducible: every plotted curve is either a closed
form evaluated here, or a finite arithmetic object computed here, never a hand
drawn sketch. Running this script rewrites ``manuscript/figure-data.tex`` in
place; the emitted file is committed so a plain LaTeX run needs no Python.

Usage:
    python scripts/build_figure_data.py
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

# First ten ordinates of the nontrivial zeros of zeta on the critical line.
# Standard published values; used only to draw a truncated explicit formula.
ZETA_ZERO_ORDINATES = (
    14.134725141734693,
    21.022039638771554,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167159,
    49.773832477672302,
)

PSI_X_MIN = 2.0
PSI_X_MAX = 100.0
PSI_SAMPLES = 420


def von_mangoldt_jumps(limit: int) -> list[tuple[int, float]]:
    """Return the ordered prime powers n <= limit together with Lambda(n)."""
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for candidate in range(2, int(limit**0.5) + 1):
        if sieve[candidate]:
            for multiple in range(candidate * candidate, limit + 1, candidate):
                sieve[multiple] = False
    primes = [n for n in range(2, limit + 1) if sieve[n]]

    jumps: list[tuple[int, float]] = []
    for prime in primes:
        power = prime
        while power <= limit:
            jumps.append((power, math.log(prime)))
            power *= prime
    jumps.sort()
    return jumps


def chebyshev_psi_staircase(limit: int) -> list[tuple[float, float]]:
    """Sample points tracing the exact staircase of psi(x) - x on [2, limit]."""
    jumps = von_mangoldt_jumps(limit)
    points: list[tuple[float, float]] = []
    running = 0.0
    for position, weight in jumps:
        if position > limit:
            break
        # Value just before the jump, then just after: a genuine step plot.
        points.append((float(position), running - position))
        running += weight
        points.append((float(position), running - position))
    points.append((float(limit), running - limit))
    return points


def truncated_explicit_formula(x: float, ordinates: tuple[float, ...]) -> float:
    """Return the zero sum plus lower order terms of psi(x) - x, truncated.

    psi(x) - x = - sum_rho x^rho / rho - log(2 pi) - (1/2) log(1 - x^{-2}),
    and pairing rho = 1/2 + i gamma with its conjugate turns each pair into
    2 sqrt(x) * [ (1/2) cos(gamma log x) + gamma sin(gamma log x) ]
              / (1/4 + gamma^2).
    """
    log_x = math.log(x)
    root_x = math.sqrt(x)
    zero_sum = 0.0
    for gamma in ordinates:
        numerator = 0.5 * math.cos(gamma * log_x) + gamma * math.sin(gamma * log_x)
        zero_sum += numerator / (0.25 + gamma * gamma)
    archimedean = -math.log(2.0 * math.pi) - 0.5 * math.log1p(-1.0 / (x * x))
    return -2.0 * root_x * zero_sum + archimedean


def format_coordinates(points: list[tuple[float, float]], per_line: int = 6) -> str:
    chunks = [f"({x:.6f},{y:.6f})" for x, y in points]
    lines = [
        " ".join(chunks[index : index + per_line])
        for index in range(0, len(chunks), per_line)
    ]
    return "%\n".join(lines)


def build_zero_free_curves() -> tuple[str, str]:
    """Classical and Vinogradov--Korobov boundaries with an illustrative c = 1.

    The plotted horizontal variable is log10(t); the constants are normalised to
    one so the figure compares shapes, not published numerical constants.
    """
    classical: list[tuple[float, float]] = []
    korobov: list[tuple[float, float]] = []
    steps = 160
    low, high = 1.0, 30.0
    for index in range(steps + 1):
        log10_t = low + (high - low) * index / steps
        log_t = log10_t * math.log(10.0)
        log_log_t = math.log(log_t)
        classical.append((log10_t, 1.0 - 1.0 / log_t))
        korobov.append(
            (log10_t, 1.0 - 1.0 / (log_t ** (2.0 / 3.0) * log_log_t ** (1.0 / 3.0)))
        )
    return format_coordinates(classical), format_coordinates(korobov)


def farey_sequence(order: int) -> list[tuple[int, int]]:
    """Return the Farey sequence of the given order as (numerator, denominator)."""
    sequence: list[tuple[int, int]] = [(0, 1)]
    a, b, c, d = 0, 1, 1, order
    while c <= order:
        k = (order + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        sequence.append((a, b))
    return sequence


def build_farey_dissection(order: int) -> str:
    """Emit \\foreach-ready triples angle/p/q placing each a/q on a unit circle.

    Mapping the fraction value directly to an angle in [0, 360) turns the Farey
    sequence into the standard circle-method picture: rationals with small
    denominators are the centres of the major arcs.
    """
    entries = []
    for numerator, denominator in farey_sequence(order):
        angle = 360.0 * numerator / denominator
        entries.append(f"{angle:.4f}/{numerator}/{denominator}")
    return ",".join(entries)


def build_pair_correlation() -> str:
    """Montgomery's pair correlation density 1 - (sin(pi u) / (pi u))^2."""
    points: list[tuple[float, float]] = []
    steps = 600
    for index in range(steps + 1):
        u = 3.0 * index / steps
        if u == 0.0:
            value = 0.0
        else:
            sinc = math.sin(math.pi * u) / (math.pi * u)
            value = 1.0 - sinc * sinc
        points.append((u, value))
    return format_coordinates(points)


def build_psi_curves() -> tuple[str, str]:
    staircase = chebyshev_psi_staircase(int(PSI_X_MAX))
    smooth: list[tuple[float, float]] = []
    for index in range(PSI_SAMPLES + 1):
        x = PSI_X_MIN + (PSI_X_MAX - PSI_X_MIN) * index / PSI_SAMPLES
        smooth.append((x, truncated_explicit_formula(x, ZETA_ZERO_ORDINATES)))
    return format_coordinates(staircase), format_coordinates(smooth)


def render(output: Path) -> None:
    psi_exact, psi_explicit = build_psi_curves()
    classical, korobov = build_zero_free_curves()
    pair_correlation = build_pair_correlation()
    farey_order_5 = build_farey_dissection(5)

    body = f"""% !TeX root = main.tex
% Generated by scripts/build_figure_data.py. Do not edit by hand.
% Each macro expands to a complete \\addplot command; its single argument is
% the pgfplots option list applied at the call site. Expanding a whole command
% keeps the coordinate list literal at the moment pgfplots parses it.
\\newcommand{{\\antPlotPsiExact}}[1]{{\\addplot[#1] coordinates {{%
{psi_exact}
}};}}
\\newcommand{{\\antPlotPsiExplicit}}[1]{{\\addplot[#1] coordinates {{%
{psi_explicit}
}};}}
\\newcommand{{\\antPlotZeroFreeClassical}}[1]{{\\addplot[#1] coordinates {{%
{classical}
}};}}
\\newcommand{{\\antPlotZeroFreeKorobov}}[1]{{\\addplot[#1] coordinates {{%
{korobov}
}};}}
\\newcommand{{\\antPlotPairCorrelation}}[1]{{\\addplot[#1] coordinates {{%
{pair_correlation}
}};}}
\\newcommand{{\\antDataFareyOrderFive}}{{{farey_order_5}}}
"""
    output.write_text(body, encoding="utf-8")
    print(f"Wrote {output}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("manuscript/figure-data.tex"),
    )
    args = parser.parse_args()
    render(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
