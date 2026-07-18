#!/usr/bin/env python3
"""Reproduce ANT-COMP-06-01.

This is a low-height implementation check for Hardy's Z function. It scans
for sign changes only. It does not certify that every zeta zero in the
interval was found and provides no evidence for the Riemann hypothesis.
"""

from __future__ import annotations

import argparse
import cmath
import csv
import hashlib
import json
import math
import platform
from pathlib import Path
from typing import Any

import scipy
from scipy.optimize import brentq
from scipy.special import loggamma

SCRIPT_VERSION = "1.0.0"
CLAIM_CEILING = "NO_RH_EVIDENCE"


def euler_transformed_eta(s: complex, terms: int) -> complex:
    """Evaluate eta(s) with the Euler transformation of an alternating sum."""
    if terms < 2:
        raise ValueError("euler_terms must be at least 2")

    differences = [complex((k + 1) ** (-s)) for k in range(terms + 1)]
    total = 0j
    weight = 0.5

    for _ in range(terms + 1):
        total += weight * differences[0]
        differences = [
            differences[k] - differences[k + 1]
            for k in range(len(differences) - 1)
        ]
        weight *= 0.5

    return total


def zeta_from_eta(s: complex, terms: int) -> complex:
    denominator = 1 - 2 ** (1 - s)
    if abs(denominator) < 1e-14:
        raise ZeroDivisionError("eta-to-zeta denominator is too small")
    return euler_transformed_eta(s, terms) / denominator


def riemann_siegel_theta(t: float) -> float:
    return float(loggamma(0.25 + 0.5j * t).imag - 0.5 * t * math.log(math.pi))


def hardy_z(t: float, terms: int) -> float:
    s = 0.5 + 1j * t
    value = cmath.exp(1j * riemann_siegel_theta(t)) * zeta_from_eta(s, terms)
    return float(value.real)


def smooth_zero_count(t: float) -> float:
    return (
        t / (2 * math.pi) * math.log(t / (2 * math.pi))
        - t / (2 * math.pi)
        + 7 / 8
    )


def sign(value: float) -> int:
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def find_sign_change_roots(config: dict[str, Any]) -> list[float]:
    start = float(config["scan_start"])
    end = float(config["scan_end"])
    step = float(config["scan_step"])
    terms = int(config["euler_terms"])
    xtol = float(config["root_xtol"])

    if not start < end:
        raise ValueError("scan_start must be smaller than scan_end")
    if step <= 0:
        raise ValueError("scan_step must be positive")

    roots: list[float] = []
    intervals = math.ceil((end - start) / step)
    a = start
    fa = hardy_z(a, terms)

    for index in range(intervals):
        b = min(start + (index + 1) * step, end)
        fb = hardy_z(b, terms)

        if fa == 0:
            root = a
        elif fa * fb < 0:
            root = brentq(
                lambda t: hardy_z(t, terms),
                a,
                b,
                xtol=xtol,
                rtol=1e-14,
                maxiter=100,
            )
        else:
            root = None

        if root is not None and (
            not roots or abs(root - roots[-1]) > 10 * xtol
        ):
            roots.append(float(root))

        a, fa = b, fb

    return roots


def load_config(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    config = json.loads(raw.decode("utf-8"))
    digest = hashlib.sha256(raw).hexdigest()

    if config.get("claim_ceiling") != CLAIM_CEILING:
        raise ValueError(f"claim_ceiling must be {CLAIM_CEILING}")

    return config, digest


def write_outputs(
    config: dict[str, Any],
    config_digest: str,
    roots: list[float],
) -> dict[str, Any]:
    terms = int(config["euler_terms"])
    delta = float(config["sign_delta"])
    tolerance = float(config["residual_tolerance"])

    rows: list[dict[str, str | int]] = []
    residuals: list[float] = []
    opposite_signs: list[bool] = []

    for index, ordinate in enumerate(roots, start=1):
        zeta_value = zeta_from_eta(0.5 + 1j * ordinate, terms)
        z_value = hardy_z(ordinate, terms)
        left = hardy_z(ordinate - delta, terms)
        right = hardy_z(ordinate + delta, terms)
        smooth = smooth_zero_count(ordinate)

        residual = abs(zeta_value)
        residuals.append(residual)
        opposite_signs.append(left * right < 0)

        rows.append(
            {
                "index": index,
                "ordinate": f"{ordinate:.12f}",
                "Z_at_root": f"{z_value:.6e}",
                "abs_zeta": f"{residual:.6e}",
                "sign_left": sign(left),
                "sign_right": sign(right),
                "smooth_N": f"{smooth:.9f}",
                "index_minus_smooth": f"{index - smooth:.9f}",
            }
        )

    output_csv = Path(config["output_csv"])
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "index",
        "ordinate",
        "Z_at_root",
        "abs_zeta",
        "sign_left",
        "sign_right",
        "smooth_N",
        "index_minus_smooth",
    ]
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    detected_count = len(roots)
    max_residual = max(residuals, default=float("inf"))
    increasing = all(left < right for left, right in zip(roots, roots[1:]))
    passed = (
        detected_count == int(config["expected_count"])
        and max_residual <= tolerance
        and increasing
        and all(opposite_signs)
    )

    summary = {
        "algorithm": "Euler-transformed eta; SciPy loggamma; Brent sign brackets",
        "claim_ceiling": CLAIM_CEILING,
        "config_sha256": config_digest,
        "detected_count": detected_count,
        "experiment_id": config["experiment_id"],
        "expected_count": int(config["expected_count"]),
        "max_abs_zeta": max_residual,
        "notes": [
            "Sign changes detect odd-multiplicity critical-line zeros only.",
            "This run does not certify completeness in the scan interval.",
            "This run is not evidence for the Riemann hypothesis.",
        ],
        "python_version": platform.python_version(),
        "reference_status": "PASS" if passed else "FAIL",
        "scipy_version": scipy.__version__,
        "script_version": SCRIPT_VERSION,
        "strictly_increasing": increasing,
        "all_brackets_change_sign": all(opposite_signs),
    }

    output_summary = Path(config["output_summary"])
    output_summary.parent.mkdir(parents=True, exist_ok=True)
    output_summary.write_text(
        json.dumps(summary, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Path to the preregistered JSON configuration.",
    )
    args = parser.parse_args()

    config, digest = load_config(args.config)
    roots = find_sign_change_roots(config)
    summary = write_outputs(config, digest, roots)
    print(json.dumps(summary, ensure_ascii=True, sort_keys=True))
    return 0 if summary["reference_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
