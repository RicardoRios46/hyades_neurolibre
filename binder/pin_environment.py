"""Pin binder/environment.yml to the exact linux-64 versions in pixi.lock.

`pixi workspace export conda-environment` writes the version ranges from pixi.toml. Binder/NeuroLibre build on
linux-64, so each direct dependency is pinned to the version pixi.lock resolves there (the versions reported in the
Methods). Run through `pixi run binder-env`, which exports the environment first.
"""
import json
import re
import subprocess
import sys

ENV_FILE = "binder/environment.yml"

locked = json.loads(subprocess.run(
    ["pixi", "list", "--platform", "linux-64", "--explicit", "--json"],
    check=True, capture_output=True, text=True).stdout)
versions = {p["name"]: p["version"] for p in locked}

lines = open(ENV_FILE).read().splitlines()
out, missing = [], []
in_deps = False
for line in lines:
    if not line.startswith("- "):
        in_deps = line.startswith("dependencies:")
    m = re.match(r"^- ([A-Za-z0-9_.\-]+)(?:\s.*)?$", line) if in_deps else None
    if m and m.group(1) in versions:
        line = f"- {m.group(1)} ={versions[m.group(1)]}"
    elif m:
        missing.append(m.group(1))
    out.append(line)
if missing:
    sys.exit(f"Not in pixi.lock (linux-64): {', '.join(missing)}")
open(ENV_FILE, "w").write("\n".join(out) + "\n")
print(f"{ENV_FILE}: pinned {sum(1 for l in out if l.startswith('- ') and ' =' in l)} packages")
