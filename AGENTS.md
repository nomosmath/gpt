# Repository guidance

- Work from the existing checkout; do not create a Git worktree unless the user requests one.
- Use Python 3.12 and `uv` for dependency and environment management.
- Install dependencies with `uv sync --locked --dev`.
- Before handing off changes, run Ruff checks, Pyright, pytest, and `uv build` as documented in
  `README.md`.
- Do not commit credentials, local environment files, generated distributions, or virtual
  environments.

