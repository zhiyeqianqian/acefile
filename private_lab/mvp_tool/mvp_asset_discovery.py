#!/usr/bin/env python3
"""Passive MVP: company name -> attributable asset inventory.

No exploit behavior. Uses passive sources only.
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List


DOMAIN_RE = re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b")


@dataclass
class Evidence:
    source_type: str
    source: str
    detail: str


@dataclass
class AssetRecord:
    asset: str
    confidence: int
    evidence: List[Evidence]


def load_profiles(path: Path) -> Dict[str, dict]:
    # minimal yaml-like parser to avoid external deps
    text = path.read_text(encoding="utf-8")
    profiles: Dict[str, dict] = {}
    current = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" ") and line.endswith(":"):
            current = line[:-1]
            profiles[current] = {"aliases": [], "seed_domains": []}
        elif current and line.strip().startswith("- "):
            value = line.strip()[2:].strip()
            if "aliases:" in prev:  # type: ignore[name-defined]
                profiles[current]["aliases"].append(value)
            elif "seed_domains:" in prev:  # type: ignore[name-defined]
                profiles[current]["seed_domains"].append(value)
        elif current and ":" in line:
            prev = line.strip()  # type: ignore[assignment]
    return profiles


def query_crtsh(keyword: str, limit: int = 200) -> List[str]:
    q = urllib.parse.quote(f"%{keyword}%")
    url = f"https://crt.sh/?q={q}&output=json"
    try:
        with urllib.request.urlopen(url, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="ignore"))
    except Exception:
        return []

    found = set()
    for item in data[:limit]:
        names = str(item.get("name_value", "")).splitlines()
        for n in names:
            n = n.strip().lstrip("*.").lower()
            if DOMAIN_RE.fullmatch(n):
                found.add(n)
    return sorted(found)


def discover(company: str, profile: dict, use_crtsh: bool) -> List[AssetRecord]:
    scores: Dict[str, int] = defaultdict(int)
    evidences: Dict[str, List[Evidence]] = defaultdict(list)

    for domain in profile.get("seed_domains", []):
        d = domain.lower()
        scores[d] += 60
        evidences[d].append(Evidence("seed_domain", "profile", f"seed domain: {d}"))

    for alias in profile.get("aliases", []):
        if use_crtsh:
            for d in query_crtsh(alias):
                scores[d] += 25
                evidences[d].append(Evidence("certificate", "crt.sh", f"matched alias '{alias}'"))

    # promote subdomains of seed domains
    seeds = tuple(profile.get("seed_domains", []))
    for d in list(scores):
        if any(d.endswith("." + s) for s in seeds):
            scores[d] += 15
            evidences[d].append(Evidence("attribution_rule", "suffix_match", "subdomain of seed"))

    records: List[AssetRecord] = []
    for asset, score in scores.items():
        records.append(AssetRecord(asset=asset, confidence=min(score, 100), evidence=evidences[asset]))

    records.sort(key=lambda r: (-r.confidence, r.asset))
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="MVP passive asset discovery")
    parser.add_argument("--company", required=True, help="company key in profile")
    parser.add_argument("--profiles", default="private_lab/mvp_tool/company_profiles.yaml")
    parser.add_argument("--out", default="private_lab/mvp_tool/output.json")
    parser.add_argument("--with-crtsh", action="store_true")
    args = parser.parse_args()

    profiles = load_profiles(Path(args.profiles))
    if args.company not in profiles:
        raise SystemExit(f"Unknown company: {args.company}. Available: {', '.join(sorted(profiles))}")

    records = discover(args.company, profiles[args.company], args.with_crtsh)
    out = {
        "company": args.company,
        "count": len(records),
        "assets": [
            {
                "asset": r.asset,
                "confidence": r.confidence,
                "evidence": [asdict(e) for e in r.evidence],
            }
            for r in records
        ],
    }
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(records)} assets -> {args.out}")


if __name__ == "__main__":
    main()
