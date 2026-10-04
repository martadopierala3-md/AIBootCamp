import os
import sys
from pathlib import Path

print("=== VS Code / Python Setup Check ===")
print()

# 1. Current working directory
cwd = Path.cwd()
print("Current folder:", cwd)

# 2. Check if file exists
project_file = cwd / "new.py"
if project_file.exists():
    print("new.py exists: YES")
else:
    print("new.py exists: NO")
    print("Tip: save your Python file before expecting AI help.")

# 3. Python version
print("Python version:", sys.version)

# 4. Check if .venv exists
venv = cwd / ".venv"
if venv.exists():
    print(".venv exists: YES")
else:
    print(".venv exists: NO")
    print("Tip: create it with: uv venv")

# 5. Check common VS Code workspace files
files_to_look_for = [".vscode", "requirements.txt", "pyproject.toml", ".venv"]
for item in files_to_look_for:
    path = cwd / item
    if path.exists():
        print(f"{item} exists: YES")
    else:
        print(f"{item} exists: NO")

# 6. Check if script file is valid Python
script_path = cwd / "new.py"
if script_path.exists():
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            content = f.read()
        compile(content, str(script_path), "exec")
        print("Python syntax check: OK")
    except Exception as e:
        print("Python syntax check: FAILED")
        print("Error:", e)

# 7. Print environment info
print()
print("Python executable:", sys.executable)
print()

print("=== Quick diagnosis ===")
if not project_file.exists():
    print("Problem: file is not saved yet.")
elif not venv.exists():
    print("Problem: no virtual environment found.")
else:
    print("Your project folder and Python environment look okay.")
    print("If AI suggestions still do not appear, check:")
    print("1. GitHub Copilot extension installed")
    print("2. GitHub account signed in")
    print("3. Copilot plan active")
    print("4. VS Code language mode is Python")