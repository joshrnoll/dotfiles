### General Behavior

- You are an orchestrator, not an executor; When executing any task, always dispatch a **backgrounded** subagent, so that you can continue the conversation with me.
- Always clarify the desired outcome / purpose of the task. Ask if this is not clear.

### Project Awareness & Context

- When creating plans:
  - write the plan out to `PLANNING.md`
  - always create a to-do list for implementation tasks and write it to `TODO.md`
- As you work, mark completed tasks in `TODO.md`. Add discovered sub-tasks under "Discovered During Work".
- `TODO.md` and `PLANNING.md` files are gitignored and branch specific

### Git & Version Control

- **Before touching any files, run `git worktree list` and `git branch --show-current`.**
  - If not in a git directory, ignore the error and continue.
  - If on `main`/`master`: stop and create a dedicated worktree for the task before continuing. Edits should never be made directly on main unless told to do so explicitly.
  - If the current worktree/branch does not match the task: stop, warn the user, and ask
    before proceeding. Edits should always be made on a worktree that correlates to the task at hand.
  - Worktrees should live in a `.worktrees/` directory at the repo root. _This directory should be gitignored._
- **Only** push to remote **when explicitly told.**
- **Before committing**, always check for unstaged changes on the branch with `git status` and `git diff`. Ask the user if pre-existing changes should be included. Never squash-merge with origin/main changes accidentally.
- NEVER add `Co-Authored-By: Claude` or similar attributions.
- Use Conventional Commits for commit messages and PR titles.

#### Squashing Commits

When squashing a branch into a single commit, always rebase first:

```bash
git fetch origin main
git rebase origin/main                    # 1. Replay commits on top of current main
MERGE_BASE=$(git merge-base origin/main HEAD)
git reset --soft $MERGE_BASE              # 2. Collapse into staged changes
git commit -m "..."                       # 3. Single commit with only branch changes
```

**Never `git reset --soft origin/main` without rebasing first** — if main has advanced, the staged diff will include unrelated changes from main, not just branch changes.

#### Pull Requests

When asked to submit a PR:

1. Ensure changes are on a dedicated branch.
2. Rebase onto main, solving any merge conflicts that may arise.
3. Review changes (`git log -10 HEAD --pretty=%B`, `git diff --stat origin/main...HEAD`). View full diff of critical/large-change files.
4. Create a draft PR with `gh pr create --draft`. Title: conventional commit message. Body: comprehensive summary with ticket link if provided. NEVER add `Co-Authored-By: Claude` or similar attributions.
5. Open in browser: `gh pr view {PR Number} --web`

### Testing

- Tests validate requirements and desired state, not bugs or vulnerabilities.
- Never delete failing tests or modify tests just to make them pass.
- Only modify tests when testing logic is broken or requirements explicitly change.

### Design Principles

Follow KISS, YAGNI, and SOLID principles. Prefer simple, readable solutions. Only build what's currently needed.

### Documentation

- Update `README.md` and `CLAUDE.md` when features, dependencies, or setup steps change.
- Comment non-obvious code. Use inline `# Reason:` comments for complex logic.

### Behavior Rules

- Never delete or overwrite existing code unless explicitly instructed or part of a `TASK.md` task.

@RTK.md
