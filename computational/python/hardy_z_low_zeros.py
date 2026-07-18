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

SCRIPT_VERSION = "1.1.0"
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


def hardy_z_complex(t: float, terms: int) -> complex:
    s = 0.5 + 1j * t
    return cmath.exp(1j * riemann_siegel_theta(t)) * zeta_from_eta(s, terms)


def hardy_z(t: float, terms: int) -> float:
    return float(hardy_z_complex(t, terms).real)


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


def find_sign_change_roots(config: dict[str, Any]) -> tuple[list[float], float]:
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
    za = hardy_z_complex(a, terms)
    fa = float(za.real)
    max_imaginary_leakage = abs(za.imag)

    for index in range(intervals):
        b = min(start + (index + 1) * step, end)
        zb = hardy_z_complex(b, terms)
        fb = float(zb.real)
        max_imaginary_leakage = max(max_imaginary_leakage, abs(zb.imag))

        if fa == 0:
            root = a
        elif fb == 0:
            root = b
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

    return roots, max_imaginary_leakage


def load_config(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    config = json.loads(raw.decode("utf-8"))
    digest = hashlib.sha256(raw).hexdigest()

    if config.get("claim_ceiling") != CLAIM_CEILING:
        raise ValueError(f"claim_ceiling must be {CLAIM_CEILING}")

    expected_count = int(config["expected_count"])
    expected_ordinates = config.get("expected_ordinates")
    if not isinstance(expected_ordinates, list):
        raise ValueError("expected_ordinates must be a list")
    if len(expected_ordinates) != expected_count:
        raise ValueError("expected_ordinates length must match expected_count")

    for key in (
        "root_xtol",
        "residual_tolerance",
        "ordinate_tolerance",
        "hardy_imag_tolerance",
    ):
        if float(config[key]) <= 0:
            raise ValueError(f"{key} must be positive")

    return config, digest


def write_outputs(
    config: dict[str, Any],
    config_digest: str,
    roots: list[float],
    max_scan_imaginary_leakage: float,
) -> dict[str, Any]:
    terms = int(config["euler_terms"])
    delta = float(config["sign_delta"])
    tolerance = float(config["residual_tolerance"])
    expected_ordinates = [float(value) for value in config["expected_ordinates"]]

    rows: list[dict[str, str | int]] = []
    residuals: list[float] = []
    opposite_signs: list[bool] = []
    root_imaginary_leakages: list[float] = []

    for index, ordinate in enumerate(roots, start=1):
        if index <= len(expected_ordinates):
            reference_ordinate = expected_ordinates[index - 1]
            ordinate_error = abs(ordinate - reference_ordinate)
        else:
            reference_ordinate = float("nan")
            ordinate_error = float("inf")
        zeta_value = zeta_from_eta(0.5 + 1j * ordinate, terms)
        hardy_value = hardy_z_complex(ordinate, terms)
        z_value = float(hardy_value.real)
        left = hardy_z(ordinate - delta, terms)
        right = hardy_z(ordinate + delta, terms)
        smooth = smooth_zero_count(ordinate)

        residual = abs(zeta_value)
        residuals.append(residual)
        opposite_signs.append(left * right < 0)
        root_imaginary_leakages.append(abs(hardy_value.imag))

        rows.append(
            {
                "index": index,
                "ordinate": f"{ordinate:.15f}",
                "reference_ordinate": f"{reference_ordinate:.15f}",
                "ordinate_error": f"{ordinate_error:.6e}",
                "Z_at_root": f"{z_value:.6e}",
                "abs_Im_Z": f"{abs(hardy_value.imag):.6e}",
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
        "reference_ordinate",
        "ordinate_error",
        "Z_at_root",
        "abs_Im_Z",
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
    max_root_imaginary_leakage = max(
        root_imaginary_leakages, default=float("inf")
    )
    max_imaginary_leakage = max(
        max_scan_imaginary_leakage,
        max_root_imaginary_leakage,
    )
    increasing = all(left < right for left, right in zip(roots, roots[1:]))
    if detected_count == len(expected_ordinates):
        ordinate_errors = [
            abs(observed - expected)
            for observed, expected in zip(roots, expected_ordinates)
        ]
        max_ordinate_error = max(ordinate_errors, default=0.0)
    else:
        max_ordinate_error = float("inf")
    passed = (
        detected_count == int(config["expected_count"])
        and max_residual <= tolerance
        and max_ordinate_error <= float(config["ordinate_tolerance"])
        and max_imaginary_leakage <= float(config["hardy_imag_tolerance"])
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
        "reference_ordinates_source": config["expected_ordinates_source"],
        "max_abs_zeta": max_residual,
        "max_abs_imag_hardy_z": max_imaginary_leakage,
        "max_ordinate_error": max_ordinate_error,
        "notes": [
            "Reference ordinates are compared with the LMFDB zeta-zero dataset.",
            "The imaginary leakage of the computed Hardy Z values is bounded.",
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
    roots, max_imaginary_leakage = find_sign_change_roots(config)
    summary = write_outputs(
        config,
        digest,
        roots,
        max_imaginary_leakage,
    )
    print(json.dumps(summary, ensure_ascii=True, sort_keys=True))
    return 0 if summary["reference_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
