#!/usr/bin/env python3
"""Minimal evaluator for Recall@N against a gold set."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_domains(path: Path) -> set[str]:
    return {x.strip().lower() for x in path.read_text(encoding='utf-8').splitlines() if x.strip() and not x.startswith('#')}


def recall_at_n(pred: list[str], gold: set[str], n: int) -> float:
    top = set(pred[:n])
    return (len(top & gold) / len(gold)) if gold else 0.0


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--pred-json', required=True)
    p.add_argument('--gold', required=True)
    p.add_argument('--n', type=int, default=50)
    args = p.parse_args()

    pred_obj = json.loads(Path(args.pred_json).read_text(encoding='utf-8'))
    pred = [a['asset'].lower() for a in pred_obj.get('assets', [])]
    gold = load_domains(Path(args.gold))
    score = recall_at_n(pred, gold, args.n)
    print(f"Recall@{args.n}: {score:.4f} ({len(set(pred[:args.n]) & gold)}/{len(gold)})")


if __name__ == '__main__':
    main()
