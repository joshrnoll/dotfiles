---
name: workflow
description: Optional index skill for choosing among manual collaboration modes in the personal skills framework.
---

# Personal Workflow

## Overview

This skill is the index for the personal skills framework. It explains the available workflow modes, when to use them, and how artifacts are organized.

This framework is:
- manual only
- strict when invoked
- invisible when not invoked
- modular rather than monolithic

## What I will do

- explain the available skills
- help choose the right skill for the current situation
- explain artifact naming and folder layout
- explain how next-step suggestions work

## What I will not do

- automatically enter another skill
- force a sequence of stages
- treat the framework as globally active
- impose workflow structure unless the user explicitly asks for it

## Available skills

1. `understand` — investigate and clarify the problem space
2. `brainstorm` — discuss options and tradeoffs conversationally
3. `define` — articulate the desired outcome and high-level plan
4. `impl-plan` — write a detailed, execution-ready checklist
5. `review` — critically review either a plan or code, but never both at once

## Artifact layout

Artifacts live under:

```text
workflow/<topic>/
  PROBLEM.md
  PLANNING.md
  TASKS.md
  plan/REVIEW.md
  code/REVIEW.md
```

## Topic naming

When an invoked skill needs an artifact and no topic exists yet:
1. propose a kebab-case topic name
2. wait for user approval or rename
3. create artifacts only after approval

## Stage transitions

The framework never advances automatically.

At the end of a skill:
- suggest the most logical next skill
- wait for approval
- if approved, invoke the next skill
- if not approved, stop or follow the user's direction
