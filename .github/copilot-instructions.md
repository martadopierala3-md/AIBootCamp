# Copilot instructions

## Repository shape and architecture

This is a Python learning workspace rather than an installable application or package. The repository contains several independent exercise sets and notes:

- `Py_Basic_Project_Work/` contains beginner-to-intermediate Python exercises, including functions, control flow, file handling, and simple project tasks.
- `week2/` contains NumPy and pandas exercises covering arrays, data loading, cleaning, grouping, aggregation, and reshaping.
- `interviews/` contains interview-preparation notes and exercises that are separate from the runnable scripts.
- `.vscode/` selects the repository-local `.venv` interpreter and includes debug settings for Python exercises.

Most `.py` files are directly executable teaching examples. They usually create small in-memory data, print intermediate results, and do not expose an application entry point. Some scripts read or write files next to the exercise (for example, `week2/data.csv`, `output.csv`, or files under `Py_Basic_Project_Work/`), while task-oriented examples may persist data in files such as `week2/task.txt` or `Py_Basic_Project_Work/...`.

When extending an exercise, preserve its standalone nature and keep inputs, transformations, and printed demonstrations easy to follow. Do not introduce package-wide application structure or framework dependencies for a single lesson.

## Environment and commands

Use the checked-in local virtual environment from the repository root:

```powershell
.\.venv\Scripts\python.exe --version
```

Run an individual exercise from the repository root:

```powershell
.\.venv\Scripts\python.exe .\week2\day5_exec2.py
```

For a beginner exercise under `Py_Basic_Project_Work/`:

```powershell
.\.venv\Scripts\python.exe .\Py_Basic_Project_Work\day3_exc1.py
```

Use the repository root as the working directory when an exercise uses relative files like `task.txt` or `output.csv`. Scripts that load a colocated input file should prefer `Path(__file__).with_name(...)` when working with local data files.

There is no configured build system, test runner, linter, formatter, `requirements.txt`, `pyproject.toml`, or CI workflow in this repository. There are currently no automated tests, so there is no single-test selector. For a focused syntax check, compile only the changed script:

```powershell
.\.venv\Scripts\python.exe -m py_compile .\week2\day5_exec2.py
```

For behavior validation, run the changed exercise directly and inspect its printed output. Do not assume that every historical exercise is production-quality or mutually importable; validate the specific lesson being changed.

The virtual environment currently provides the numerical/data-science dependencies used by the Python lessons, notably NumPy and pandas. If a new exercise needs another dependency, update the repository's dependency documentation or project configuration rather than relying on a globally installed package.

## Code conventions specific to this workspace

- Follow the existing naming pattern used in each exercise set, such as `week2/day...` or descriptive filenames in `Py_Basic_Project_Work/`.
- Keep examples explicit and print-oriented. Existing lessons commonly print the original data, an intermediate transformation, and the result.
- Use NumPy for array/matrix demonstrations and pandas for tabular data. Keep DataFrame column names and grouping keys visible in the example code.
- Keep small reusable functions in a local module when an exercise demonstrates imports (for example, a utility file next to its script), but do not create a package solely to share one lesson.
- Use `Path` for paths that must be relative to a script's location. Older examples may still rely on simple relative filenames, so be aware of the working directory assumption.
- Preserve the repository's simple top-level script style. Add `if __name__ == "__main__":` when a script has reusable functions and should only execute its demo when run directly.
- Keep generated artifacts such as pandas CSV output out of source changes unless the exercise explicitly requires a checked-in fixture.
- Existing comments are often instructional and may include spelling or wording inconsistencies; improve them when touching the surrounding example, but avoid broad unrelated rewrites.
