---
name: understand
description: Investigate the problem space, explain context, and produce PROBLEM.md once understanding is solid.
---

# Understand the Problem

## Use this when

- the problem is not fully understood
- the user wants help understanding code, architecture, concepts, or constraints
- investigation should happen before ideation or planning

## What I will do

- explore relevant files and code for context
- explain code and concepts clearly
- answer questions directly
- identify constraints, assumptions, and unknowns
- help refine the problem statement

## What I will not do

- propose implementation changes prematurely
- write high-level or detailed plans
- execute code changes
- create the artifact before understanding is solid

## Completion criteria

This skill is complete only when:
1. the problem is clearly articulated
2. the topic name has been proposed and approved
3. `workflow/<topic>/PROBLEM.md` has been written

## Artifact output

Write `workflow/<topic>/PROBLEM.md` with these sections:
- Problem statement
- Current context
- Constraints
- Unknowns / open questions
- Out of scope

## Likely next step

Usually `brainstorm` or `define`.

Do not enter the next skill automatically. Suggest it and wait for approval. If approved, invoke it.
