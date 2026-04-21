---
name: queue
description: Use when user asks to work a task, create a task, view the backlog, or manage a file-based task queue. Triggers on "work task", "next task", "create task", "show queue", "list tasks", "backlog".
---

# Task Queue

File-based task queue for AI coding agents. Tasks are markdown files in an Obsidian vault with YAML frontmatter for lifecycle tracking.

## Queue location

`/Users/josh/Documents/Obsidian/agent-tasks/`

Template: `templates/task.md`

## Operations

### 1. Work a task

User says: "work task X", "pick up next task", "work the queue" etc.

Steps:

1. Scan queue dir for `*.md` files (exclude `templates/`, `CLAUDE.md`, `AGENTS.md`, `PROMPT.md`)
2. Parse frontmatter — filter to `status: backlog`
3. If user named a specific task, use that. Otherwise pick highest priority unblocked task.
4. Check `## Depends On` section — all wikilinked tasks must have `status: done`. Skip blocked tasks.
5. Update frontmatter: `status: working`, `updated: <today>`
6. Dispatch a **backgrounded** subagent (use `subagent` field if set, otherwise `general-purpose`)
   - Subagent prompt = full task file content (Objective, Context, Requirements, Constraints)
   - Subagent should write results to `## Result` section and check off requirements
7. When subagent completes: set `status: done`, `completed: <today>`

Priority order: critical > high > medium > low

### 2. Create a task

User says: "create a task to...", "add task", "queue up"

Steps:

1. Ask user for description if not provided
2. Generate frontmatter — infer `type`, `priority`, `tags` from description
3. Set `created: <today>`, `status: backlog`
4. Write file as `YYYY-MM-DD-short-slug.md` in queue dir
5. Populate Objective from user description. Leave other sections for user to fill or fill if enough context.

### 3. Show queue

User says: "show queue", "list tasks", "backlog", "what's next"

Steps:

1. Scan queue dir for task files
2. Parse frontmatter from each
3. Display grouped by status: working first, then backlog (by priority), then done
4. Flag blocked tasks (unmet dependencies from `## Depends On` section)
5. Show summary: counts per status, next actionable task

## What I will not do

- Automatically work tasks without being asked
- Delete or archive task files
- Modify tasks that are already `status: done` unless asked
- Skip the dependency check

## Frontmatter reference

| Field     | Values                                                   | Notes                              |
| --------- | -------------------------------------------------------- | ---------------------------------- |
| status    | backlog, working, done                                   | Update as you work                 |
| type      | work, plan, info                                         | Task category                      |
| priority  | low, medium, high, critical                              | Queue ordering                     |
| subagent  | general-purpose, Explore, code-review, Plan, test-writer | Optional, defaults general-purpose |
| created   | YYYY-MM-DD                                               | Set on creation                    |
| updated   | YYYY-MM-DD                                               | Set when work begins               |
| completed | YYYY-MM-DD                                               | Set when done                      |

## For Pi agents

Pi has no built-in subagent dispatch. Instead:

1. Ignore `subagent` field in task frontmatter
2. Dispatch work by spawning a new pi instance in a tmux session:
   ```bash
   tmux new-session -d -s "task-<slug>" "pi --print '<task prompt>'"
   ```
3. Monitor with `tmux list-sessions` and `tmux capture-pane -t "task-<slug>" -p`
4. Pi tools: use `read`, `write`, `edit`, `bash` (no dedicated glob/grep — use bash equivalents)
