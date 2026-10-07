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

## Website

`web/` contains the static ProxyPad visual copy with a terracotta theme and seven generated
replacement images. The copy includes the home page, Docs, Launch, Arena, and two linked coin
pages. Wallet features and live market data are not connected.

To deploy permanently, import this repository into Vercel. The root `vercel.json` points Vercel to
the `web/` output directory; no build command or environment variables are required. A deployment
made through a signed-in Vercel account will not expire after an hour like anonymous deployments.
