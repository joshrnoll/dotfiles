### 🔄 Project Awareness & Context

- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASK.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.

### ✅ Task Completion

- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a "Discovered During Work" section.

### 🔀 Git & Version Control

- **Only commit or push to git if explicitly told** - I will generally do this myself.
- **Always check the current branch** - if on main or master, warn and confirm whether or not this is intentional before continuing with any edits.
- **Never attribute co-authorship to Claude in git commits** – do not add `Co-Authored-By: Claude` or similar attributions.
- **Always use semantic commit message style** following the Conventional Commits specification:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `chore:` for maintenance tasks (dependencies, configs, etc.)
  - `docs:` for documentation changes
  - `refactor:` for code refactoring
  - `test:` for adding or updating tests
  - `style:` for formatting changes
  - `perf:` for performance improvements
  - Examples:
    - `feat: add user authentication endpoint`
    - `fix: resolve null pointer in data validation`
    - `chore: update dependencies to latest versions`
- **Apply the same semantic style to pull request titles** for consistency.

#### Pull Requests

**Follow this sequence if asked to submit a pull requests**

1. Get a summary of changes

```bash
git fetch origin

# Review the last 10 commit messages
git log -10 HEAD --pretty=%B

# Get a summary of changes
git diff --stat origin/main...HEAD
```

2. Review the summary of changes. View a full diff of any changes to critical files, or any files that had a large amount of changes:

```bash
git diff origin/main...HEAD --- /path/to/file
```

3. Create a draft PR:

```bash
gh pr create --draft --title <title> --body <body>

```

4. For _Title:_ use a conventional commit message that properly captures the changes made. This will usually be the most recent commit message.
5. For _Body:_ write a comprehensive summary of the changes, adding a link to the ticket that it resolves if provided. _Do not attribute authorship to claude code in the body._

### Testing

- **Do not** write tests that validate bugs or security vulnerabilities. Tests are for validating requirements and desired state.
- **Do not** delete tests when they are not passing.
- **Do not** modify tests just to make them pass.
- **Only modify** existing tests when the testing logic is broken or if requirements explicitly change.

### 🎯 Design Principles

#### KISS (Keep It Simple, Stupid)

- **Write straightforward, uncomplicated solutions** – complexity should only exist when absolutely necessary.
- **Avoid over-engineering** – don't add abstractions, patterns, or features beyond what's needed.
- **Prioritize readability** – code that's easy to understand is easier to maintain and debug.
- **Question complexity** – if a solution feels complex, look for a simpler approach first.

#### YAGNI (You Aren't Gonna Need It)

- **Implement only what's currently needed** – don't build features for hypothetical future requirements.
- **Prevent speculative code** – every line of code should serve a present, concrete purpose.
- **Reduce code bloat** – less code means less maintenance, fewer bugs, and easier understanding.
- **Wait for real requirements** – when you actually need a feature, you'll have better context to build it right.

#### SOLID Principles

- **Single Responsibility Principle (SRP)**: Each class/function should have one reason to change; do one thing well.
- **Open-Closed Principle (OCP)**: Code should be open for extension but closed for modification; extend behavior without changing existing code.
- **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types without breaking functionality.
- **Interface Segregation Principle (ISP)**: Don't force classes to implement interfaces they don't use; prefer smaller, focused interfaces.
- **Dependency Inversion Principle (DIP)**: Depend on abstractions, not concretions; high-level modules shouldn't depend on low-level details.

### 📚 Documentation & Explainability

- **Update `README.md` & `CLAUDE.md` (If exists)** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.

### 🧠 AI Behavior Rules

- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.

#### Pre-Commit Security Checklist (Quick Manual Check)

Before committing, verify:

- [ ] No secrets, API keys, or credentials in code (search for: "api_key", "password", "secret", "token")
- [ ] No SQL injection risks (check for string concatenation in queries)
- [ ] No command injection (check `os.system`, `subprocess` with `shell=True`, `eval`, `exec`)
- [ ] Input validation is present for all user inputs
- [ ] Authentication/authorization checks are not bypassed
- [ ] .env files are in .gitignore
- [ ] Dependencies are pinned and not vulnerable

#### Automated Security Scanning

When available, run these tools before commits:

```bash
# Python projects
bandit -r . -ll                    # Security linter
safety check                       # Dependency vulnerabilities
semgrep --config=auto .           # Pattern-based security scanning

# Check for secrets in git history
gitleaks detect --source .
```

#### Security-First Development Practices

- **Input Validation**: Use Pydantic models for all API inputs
- **SQL Safety**: Always use parameterized queries or ORM methods (never string formatting)
- **Command Execution**: Avoid `shell=True`, sanitize all inputs
- **Secrets Management**: Use environment variables via `python-dotenv`, never hardcode
- **Dependencies**: Pin all versions in requirements.txt with `==`
- **Error Handling**: Never expose stack traces or sensitive info in error messages
- **Authentication**: Use bcrypt or argon2 for password hashing
- **Authorization**: Check permissions before every sensitive operation

#### Response to Security Findings

When you identifies issues, categorize them as follows:

1. **Critical/High severity**: Fix immediately before proceeding
2. **Medium severity**: Fix before committing
3. **Low severity**: Create a task in TASK.md to address later
4. **Document decision**: If a risk is accepted, document why in code comments or PLANNING.md
