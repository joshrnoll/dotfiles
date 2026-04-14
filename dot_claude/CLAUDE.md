### Project Awareness & Context

- When creating plans, always create a to-do list and write it to `TODO.md`
- Mark completed tasks in `TODO.md`. Add discovered sub-tasks under "Discovered During Work".
- `TODO.md` files are gitignored and branch specific
- If there is a `PLANNING.md` file, ask if we should review the plan or if it is ready for implementation

### Git & Version Control

- **Before touching any files, run `git worktree list` and `git branch --show-current`.**
  - If on `main`/`master`: stop, warn the user. Edits should never be made directly on main without explicit permission.
  - If the current worktree/branch does not match the task: stop, warn the user, and ask
    before proceeding. Edits should always be made on a worktree that correlates to the task at hand.
  - Do not make any edits until the correct worktree is confirmed.
  - Worktrees should live in a `.worktrees/` directory at the repo root. _This directory should be gitignored._
- **Only** push to remote **when explicitly told.**
- **Before committing**, always check for unstaged changes on the branch with `git status` and `git diff`. Ask the user if pre-existing changes should be included. Never squash-merge with origin/main changes accidentally.
- NEVER add `Co-Authored-By: Claude` or similar attributions.
- Use Conventional Commits for commit messages and PR titles.

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
