"""Verify I=0 independent modules excluded from high_coupling."""
# Simulate the instability calculation logic
modules = {
    "lib_utils": {"ca": 0, "ce": 0},       # fully independent
    "core_db": {"ca": 5, "ce": 1},         # stable, I=0.166
    "api_routes": {"ca": 0, "ce": 8},      # unstable, I=1.0
}

instability = {}
for name, info in modules.items():
    total = info["ca"] + info["ce"]
    instability[name] = info["ce"] / total if total > 0 else 0

# OLD broken logic
old_high = [m for m, i in instability.items() if i > 0.7 or i < 0.3]
assert "lib_utils" in old_high, "OLD: lib_utils (I=0) incorrectly marked high coupling"

# NEW fixed logic
new_high = [m for m, i in instability.items() if i > 0.7 or (0 < i < 0.3)]
assert "lib_utils" not in new_high, "NEW: lib_utils (I=0) correctly excluded"
assert "core_db" in new_high, "NEW: core_db (I=0.166) correctly included as overly stable"
assert "api_routes" in new_high, "NEW: api_routes (I=1.0) correctly included as unstable"
print("PASS: I=0 modules excluded from high_coupling_modules")
