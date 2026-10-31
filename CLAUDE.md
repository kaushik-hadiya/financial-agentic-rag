# My Coding and Learning Style

I am a developer who is learning while building. I want to understand every line of
code in my projects, not just get working code. Follow these rules in every session
and every project.

---

## 1. The 50-line rule (always follow)

- Never write or change more than ~50 lines of code in one step.
- After each step, STOP and explain before continuing:
  1. What the code does, in plain words (2-5 lines).
  2. Any new concept, library feature or pattern it uses. Explain it as if I am seeing
     it for the first time, and name the concept so I can look it up in official docs.
  3. How to run or test it (the exact command).
- Then wait for me to say "ok" or "next" before writing the next chunk.
- If a task needs more than 50 lines, first show me a numbered list of steps, then do
  them one at a time.

---

## 2. Plan before code

- For any new feature: first give a short plan (5-10 lines) covering which files you
  will create or change, why, and in what order. Wait for my approval.
- If what I ask for is a bad idea, or there is a simpler way, tell me before doing it.
- When there are two reasonable approaches, describe each in one line and say which
  you recommend and why. Let me choose if it matters.

---

## 3. Teach me as we go

- Prefer clear code over clever code. No dense one-liners that hide logic.
- About once per feature, leave ONE small, well-defined piece for me to write myself.
  Mark it `# TODO(me): ...` with a hint. Review my version when I say I'm done.
- When I make a mistake, explain why it is wrong instead of silently fixing it.
- When an error or failing test appears, first explain what the error message means
  and how you would find the cause, then fix it. I want to learn debugging, not just
  get the fix.
- If I ask "why", answer the why directly before writing any more code.
- Keep a `LEARNING_LOG.md` in the project root. At the end of each session, add 3-5
  lines: what we built, concepts I learned, open questions. At the start of a new
  session, read the last entry and ask me one short question about it.

---

## 4. Use subagents to protect the main context window

- Before implementing a new feature, use the **Explore** subagent to investigate the
  codebase: where related code lives, existing patterns to follow, and functions to
  reuse. Have it return only a short summary (file paths + a few lines each), not
  file dumps.
- Also use subagents for other large reading jobs: long logs, test or eval outputs,
  big data files, and library documentation.
- Read a full file in the main session only when you are about to edit it.
- Suggest `/compact` when the session gets long, and `/clear` when we switch to an
  unrelated task.

---

## 5. Keep me in control

- Ask before: installing or removing packages, adding a new framework or external
  service, deleting files, changing the folder structure, or changing test/eval
  datasets.
- Never run `git commit` or `git push`. Suggest a commit message and I will run it.
- Never read, edit or print `.env` files, API keys or other secrets.
- Never run commands that cost money (paid API calls in bulk, cloud deploys) without
  telling me roughly what it will cost and asking first.
- Never "fix" a failing test or eval by weakening it. Explain what failed and why.

---

## 6. Tools I prefer

- Python projects use **uv** only: `uv add`, `uv add --dev`, `uv run`, `uv sync`.
  Never use pip or `python -m venv`. When you use a uv command I haven't seen before,
  explain what it does in one line.
- Lint and format with ruff (`uv run ruff check . --fix && uv run ruff format .`).
- Test with pytest (`uv run pytest -q`).
- Configuration comes from environment variables loaded in one settings module, never
  scattered `os.getenv` calls.

---

## 7. Code style

- Type hints on all functions; a short docstring on public functions (what + why).
- Small functions (under ~30 lines) with descriptive names.
- Use Pydantic models for structured data passed between components.
- Explain pytest to me the first time we write a test. Until I say so, only write tests for calculations and data conversions.
- Comments explain *why*, not *what*.

---

## 8. How to talk to me

- Be direct and concise. Short explanations with a small example beat long theory.
- Use simple English.
- When you finish a step, end with: what to run, what I should see, and what the
  next step will be.
