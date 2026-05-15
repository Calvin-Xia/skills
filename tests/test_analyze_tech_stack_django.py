"""Verify Django detection from dependency files."""
import re
import tempfile
import os

def check_django_in_deps(project_path):
    req_path = os.path.join(project_path, 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, encoding='utf-8', errors='ignore') as f:
            if re.search(r'^[Dd]jango\b', f.read(), re.MULTILINE):
                return True

    toml_path = os.path.join(project_path, 'pyproject.toml')
    if os.path.exists(toml_path):
        with open(toml_path, encoding='utf-8', errors='ignore') as f:
            if re.search(r'[Dd]jango', f.read()):
                return True

    return os.path.exists(os.path.join(project_path, 'settings.py'))


with tempfile.TemporaryDirectory() as tmpdir:
    # Test 1: requirements.txt
    with open(os.path.join(tmpdir, 'requirements.txt'), 'w') as f:
        f.write('django==4.2\nrest-framework==3.14\n')
    assert check_django_in_deps(tmpdir) == True, "Should detect Django in requirements.txt"

with tempfile.TemporaryDirectory() as tmpdir:
    # Test 2: pyproject.toml
    with open(os.path.join(tmpdir, 'pyproject.toml'), 'w') as f:
        f.write('[tool.poetry.dependencies]\ndjango = "^4.2"\n')
    assert check_django_in_deps(tmpdir) == True, "Should detect Django in pyproject.toml"

with tempfile.TemporaryDirectory() as tmpdir:
    # Test 3: settings.py only
    open(os.path.join(tmpdir, 'settings.py'), 'w').close()
    assert check_django_in_deps(tmpdir) == True, "Should detect Django from settings.py"

with tempfile.TemporaryDirectory() as tmpdir:
    # Test 4: no django
    with open(os.path.join(tmpdir, 'requirements.txt'), 'w') as f:
        f.write('flask==3.0\n')
    assert check_django_in_deps(tmpdir) == False, "Should not detect Django in Flask project"

print("PASS: Django detection from dependency files correct")
