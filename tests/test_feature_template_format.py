"""Verify feature-templates.md stories conform to SKILL.md format."""
import re
import os

base = os.path.dirname(__file__)
path = os.path.join(base, '..', 'skills', 'prd-generator', 'references', 'feature-templates.md')
with open(path, encoding='utf-8') as f:
    content = f.read()

# Each story should have these markers
required_patterns = [
    r'\*\*As (a|an)\*\*', # As a/an [user type]
    r'\*\*I want to\*\*',  # I want to [action]
    r'\*\*So that\*\*',    # So that [benefit]
    r'\*\*Priority:\*\*',  # Priority field
    r'\*\*Story Points:\*\*', # Story Points field
]

# Find all code blocks (the templates)
blocks = re.findall(r'```markdown\n(.*?)```', content, re.DOTALL)
assert len(blocks) > 0, "No markdown template blocks found"

issues = []
for i, block in enumerate(blocks):
    for pattern in required_patterns:
        if not re.search(pattern, block):
            issues.append(f"Block {i+1}: missing {pattern}")

if issues:
    print("FAIL: " + "; ".join(issues[:5]))
    exit(1)

print(f"PASS: all {len(blocks)} template blocks have required format fields")
