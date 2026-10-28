#!/usr/bin/env python3
"""Pure-Python invariant checks for the controlled Legavia business baseline."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "traceability/manifest.json").read_text())
ucs = json.loads((ROOT / "traceability/use_cases.json").read_text())["use_cases"]
seed = json.loads((ROOT / "traceability/verification_seed_catalog.json").read_text())
assert manifest["schema_version"] == "1.0"
assert isinstance(manifest["project"], dict)
for key in ("requirements", "functionalities", "work_packages", "artifacts"):
    assert isinstance(manifest[key], list), key
for coll in [manifest["requirements"], manifest["functionalities"], manifest["work_packages"], ucs, seed["tests"]]:
    ids = [x["id"] for x in coll]
    assert len(ids) == len(set(ids)), "duplicate identifiers"
R = {r["id"] for r in manifest["requirements"]}
F = {f["id"] for f in manifest["functionalities"]}
W = {w["id"] for w in manifest["work_packages"]}
for f in manifest["functionalities"]:
    assert set(f["requirement_ids"]) <= R, f["id"]
    assert set(f.get("depends_on_functionality_ids", [])) <= F, f["id"]
for r in manifest["requirements"]:
    assert set(r.get("functionality_ids", [])) <= F, r["id"]
for w in manifest["work_packages"]:
    assert set(w.get("functionality_ids", [])) <= F, w["id"]
    assert set(w.get("depends_on", [])) <= W, w["id"]
    assert (ROOT / w["path"]).is_file(), w["path"]
for u in ucs:
    assert set(u["trace"]) <= F, u["id"]
for t in seed["tests"]:
    assert set(t["trace"]) <= F, t["id"]
assert seed["execution_enabled"] is False
assert manifest["functionality_verification"]["tests"] == []
for prefix,n in [("LEGACY-BIZ-",5),("LEGACY-FNC-",28),("LEGACY-UX-",12),("LEGACY-NFR-",8)]:
    assert len([x for x in R if x.startswith(prefix)]) > n
assert len([x for x in ucs if x["id"].startswith("UC-")]) >= 33
print(f"Valid control baseline: {len(R)} requirements; {len(F)} functionalities; {len(W)} work packages; {len(ucs)} use cases; {len(seed['tests'])} design-only verification seeds")
