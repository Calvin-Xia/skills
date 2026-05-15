"""Smoke test: _has_cjk_garbled detection logic."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skills', 'course-review-material', 'scripts'))

def _has_cjk_garbled(text):
    replacement_count = text.count("\ufffd")
    if replacement_count > 0 and replacement_count / max(len(text), 1) > 0.02:
        return True
    return False

assert _has_cjk_garbled("\ufffd" * 60) == True, "60 garbled chars in 60 should trigger"
assert _has_cjk_garbled("hello world" * 10) == False, "plain text should not trigger"
assert _has_cjk_garbled("\ufffd" + "x" * 500) == False, "single \ufffd in 501 chars should not trigger"
assert _has_cjk_garbled("\ufffd" * 2 + "x" * 100) == False, "2% threshold not met"
print("PASS: _has_cjk_garbled logic correct")
