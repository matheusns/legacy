#!/usr/bin/env python3
"""Validate Legavia's controlled candidate business baseline without third-party dependencies."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
M = json.loads((ROOT/"traceability/manifest.json").read_text(encoding="utf-8"))
B = json.loads((ROOT/"traceability/business_baseline.json").read_text(encoding="utf-8"))
def unique(items, label):
    ids = [x["id"] for x in items]
    assert len(ids)==len(set(ids)), f"Duplicate {label} IDs"
    return set(ids)
for key in ("schema_version","project","requirements","functionalities","artifacts"):
    assert key in M, f"Missing GUI manifest key {key}"
req=unique(M["requirements"],"requirement")
caps=unique(M["functionalities"],"functionality")
wps=unique(M["work_packages"],"work package")
ucs=unique(B["use_cases"],"use case")
fvts=unique(B["verification_definitions"],"FVT")
for r in M["requirements"]:
    assert r["statement"] and r["functionality_ids"] and set(r["functionality_ids"])<=caps
    assert r["status"]=="Candidate", f"Unexpected approval status: {r['id']}"
for f in M["functionalities"]:
    assert set(f["requirement_ids"])<=req
    assert set(f.get("depends_on_functionality_ids",[]))<=caps
for w in M["work_packages"]:
    assert set(w["functionality_ids"])<=caps
    assert set(w.get("depends_on",[]))<=wps
    assert w["status"]=="Backlog"
    assert (ROOT/w["path"]).is_file(), f"Missing WP document {w['path']}"
    assert all(repo.startswith("matheusns/") for repo in w["target_repositories"])
for u in B["use_cases"]:
    assert set(u["requirements"])<=req and u["main_flow"] and u["alternate_flows"]
for t in B["verification_definitions"]:
    assert set(t["requirement_ids"])<=req
    assert t["status"].startswith("Planned")
for a in M["artifacts"]:
    assert (ROOT/a["path"]).is_file(), f"Missing controlled artifact {a['path']}"
def visit_graph(items, edge, label):
    m={x["id"]:x.get(edge,[]) for x in items}
    visiting,done=set(),set()
    def visit(k):
        if k in done: return
        assert k not in visiting, f"{label} dependency cycle at {k}"
        visiting.add(k)
        for d in m[k]:
            assert d in m, f"{label} missing predecessor {d}"
            visit(d)
        visiting.remove(k);done.add(k)
    for k in m:visit(k)
visit_graph(M["functionalities"],"depends_on_functionality_ids","capability")
visit_graph(M["work_packages"],"depends_on","work package")
print(f"Valid candidate baseline: {len(req)} requirements, {len(caps)} capabilities, {len(ucs)} use cases, {len(fvts)} planned FVTs, {len(wps)} work packages; all links resolved.")
