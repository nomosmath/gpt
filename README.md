# nomosmath/gpt

A compact Python 3.12 foundation for GPT-related tools. The repository starts with a typed,
installable CLI and a complete local quality gate, without requiring API keys or external services.

## Development

Install the locked development environment:

```bash
uv sync --locked --dev
```

Run the complete quality gate:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run pytest
uv build
```

Try the CLI:

```bash
uv run gpt --version
uv run gpt
```

Use the existing checkout in `/workspace/gpt` in Codex cloud tasks. A separate Git worktree is not
needed unless the task explicitly asks for one.

