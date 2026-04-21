---
name: mcporter
description: Use mcporter to discover, authenticate against, inspect, and call MCP servers from the shell when the task requires MCP tools that are not already exposed as native pi tools.
---

# MCPorter

Use this skill when the user wants to use an MCP server or MCP tool, especially when pi does not already have that MCP wired in as a native tool.

## Goal

Use `mcporter` as the bridge between pi and MCP servers via shell commands.

Prefer `mcporter` for:
- discovering configured MCP servers
- listing tools and schemas for a server
- authenticating OAuth-backed MCP servers
- calling MCP tools from the CLI
- trying ad-hoc MCP endpoints over HTTP or stdio

## What I will do

1. Clarify the user's goal and identify the target MCP server/tool if possible.
2. Check whether `mcporter` is available.
3. Inspect available servers/tools before calling anything destructive.
4. Authenticate if required.
5. Call the needed tool with explicit arguments.
6. Summarize the result for the user, including any errors or follow-up actions.

## Safety rules

- Treat MCP tools as potentially side-effecting.
- For any mutating/destructive tool, ask for confirmation before calling it unless the user has already clearly authorized the action.
- Prefer read-only/list/search tools first when exploring a server.
- When a call fails, inspect the server/tool signature again before retrying.
- Do not invent tool names or parameter names; inspect them with `mcporter list <server>` first.

## Availability check

First determine how to invoke mcporter:

```bash
command -v mcporter
```

If present, use `mcporter`.

If not present, prefer `npx mcporter`:

```bash
npx mcporter --version
```

If neither works, tell the user `mcporter` is unavailable and suggest one of:

```bash
npm install -g mcporter
# or
brew tap steipete/tap && brew install steipete/tap/mcporter
# or use directly with
npx mcporter ...
```

## Core workflow

### 1) Discover servers

Start here when the server is unknown:

```bash
mcporter list
# or
npx mcporter list
```

This discovers servers from mcporter config plus imported editor configs such as Cursor, Claude, Codex, Windsurf, OpenCode, and VS Code.

### 2) Inspect one server before calling tools

```bash
mcporter list <server>
mcporter list <server> --all-parameters
mcporter list <server> --schema
```

Use this to learn:
- exact tool names
- required and optional parameters
- descriptions and signatures

### 3) Authenticate if needed

For OAuth or auth failures:

```bash
mcporter auth <server>
# or for ad-hoc URLs
mcporter auth https://example.com/mcp
```

If the tool/server is hosted and returns auth-related errors, try auth before assuming the server is broken.

### 4) Call the tool

Prefer function-call syntax because it matches `mcporter list` output and is easier to review:

```bash
mcporter call 'server.toolName(param1: "value", param2: 123)'
```

Other valid forms:

```bash
mcporter call server.toolName key=value otherKey=value
mcporter server.toolName key=value
```

When structured output will help, prefer:

```bash
mcporter call 'server.toolName(...)' --output json
```

If you need the raw MCP envelope:

```bash
mcporter call 'server.toolName(...)' --output raw
```

### 5) Ad-hoc servers

If the server is not configured yet, use mcporter directly against a URL or stdio command:

```bash
mcporter list --http-url https://example.com/mcp --name example
mcporter call 'https://example.com/mcp.some_tool(arg: "value")'

mcporter list --stdio "bun run ./local-server.ts" --name local-tools
mcporter call --stdio "bun run ./local-server.ts" --name local-tools some_tool key=value
```

Notes:
- Ad-hoc definitions are ephemeral unless persisted.
- Reuse the URL or stdio flags on later calls unless the server has been persisted.
- Use `--allow-http` only if the endpoint is plain HTTP and the user explicitly wants that.

## Preferred command patterns

### List all servers

```bash
mcporter list
```

### Show one server with full parameters

```bash
mcporter list linear --all-parameters
```

### Call a tool with readable syntax

```bash
mcporter call 'context7.resolve-library-id(libraryName: "react")'
```

### Call a tool with shell-friendly syntax

```bash
mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'
```

### Save image outputs if relevant

```bash
mcporter call 'server.tool(...)' --save-images ./tmp/mcporter-images
```

## How to interpret results

After a successful call:
- summarize the tool output in plain language
- quote key fields when precision matters
- note any files saved or artifacts produced
- mention whether the action was read-only or mutating

If output is JSON, inspect and summarize the important fields instead of dumping large raw payloads unless the user asked for raw output.

## Troubleshooting

### Server not found

Run:

```bash
mcporter list
```

Then verify whether the server exists in:
- project `config/mcporter.json`
- home `~/.mcporter/mcporter.json` or `.jsonc`
- imported editor configs

### Unsure of tool name or args

Run:

```bash
mcporter list <server> --all-parameters
```

### Auth/offline/http issues

Use:

```bash
mcporter auth <server>
mcporter call 'server.tool(...)' --output json
```

`--output json` can make connection failures easier to inspect programmatically.

### Unknown flags becoming bad arguments

Prefer one of:

```bash
mcporter call 'server.toolName(...)'
mcporter call server.toolName key=value
mcporter call server.toolName -- key-that-starts-with-dashes
```

## Decision rules

- If the user only names a goal, first identify the relevant MCP server with `mcporter list`.
- If the user names a server but not a tool, inspect the server with `mcporter list <server>`.
- If the user names a tool, still inspect its signature unless parameters are already known with confidence.
- If a tool mutates external state, ask before calling.
- If repeated calls are needed, reuse the same invocation style consistently.

## Example session outline

1. `mcporter list`
2. `mcporter list <server> --all-parameters`
3. `mcporter auth <server>` if needed
4. `mcporter call 'server.toolName(...)' --output json`
5. Summarize result for the user

## References

mcporter project: https://github.com/steipete/mcporter
