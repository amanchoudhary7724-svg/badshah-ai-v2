# BADSHAH-AI v2 — Phase 25 Local LLM Router

Adds:
- Multiple Ollama model routing
- Auto model selection
- Fallback model support
- Model health/list command
- Model router dashboard tab

## Commands

```text
models
model health
model use coding
model use fast
ask coding create python function
ask fast hello
ask smart explain AI agents
```

## Setup

Pull models as needed:

```bat
ollama pull llama3.2:1b
ollama pull qwen2.5-coder:1.5b
```

## Push

```bash
git add .
git commit -m "Add BADSHAH-AI v2 phase 25 llm router"
git push origin main
```
