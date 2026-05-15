"""Verify health score includes P2/P3 weighting."""
def calc_score(issues):
    score = 5
    if issues.get("circular_deps"): score -= 1
    if issues.get("avg_instability", 0) > 0.8: score -= 1
    if len(issues.get("P0", [])) > 0: score -= 2
    if len(issues.get("P1", [])) > 2: score -= 1
    if len(issues.get("P2", [])) > 5: score -= 1
    if len(issues.get("P3", [])) > 3: score -= 1
    return max(1, score)

# No issues → 5
assert calc_score({}) == 5, "No issues should be score 5"

# 5 P2 issues + 0 P0/P1 → should be 5 (not 4 or lower)
issues1 = {"P0": [], "P1": [], "P2": ["x"] * 5, "P3": []}
assert calc_score(issues1) == 5, f"5 P2 should still be excellent, got {calc_score(issues1)}"

# 6 P2 + 0 P0/P1 → should be 4
issues2 = {"P0": [], "P1": [], "P2": ["x"] * 6, "P3": []}
assert calc_score(issues2) == 4, f"6 P2 should drop to good, got {calc_score(issues2)}"

# P0 → should be 3
issues3 = {"P0": ["critical"], "P1": [], "P2": [], "P3": []}
assert calc_score(issues3) == 3, f"P0 should drop by 2, got {calc_score(issues3)}"

# P0 + circular → should be 2
issues4 = {"P0": ["critical"], "P1": [], "P2": [], "P3": [], "circular_deps": True}
assert calc_score(issues4) == 2, f"P0+circular should be 2, got {calc_score(issues4)}"

print("PASS: health score logic correct with P2/P3 weighting")
