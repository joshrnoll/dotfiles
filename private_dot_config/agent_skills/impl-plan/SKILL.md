---
name: impl-plan
description: Produce a detailed TASKS.md checklist that is concrete enough for execution by a future session or another agent.
---

# Implementation Plan

## Use this when

- the desired outcome is clear
- the user wants a detailed, execution-ready checklist
- the work needs to be broken into concrete steps

## What I will do

- create a detailed checklist
- identify the files, modules, or components involved
- specify testing and validation work
- sequence the work clearly
- make the plan executable by another agent or future session

## What I will not do

- implement the plan
- produce vague or hand-wavy tasks
- mix review findings into planning

## Completion criteria

This skill is complete only when:
1. the task breakdown is concrete and complete enough to execute
2. the topic name has been proposed and approved
3. `workflow/<topic>/TASKS.md` has been written

## Artifact output

Write `workflow/<topic>/TASKS.md` with these sections:
- Implementation checklist
- File/component notes
- Testing tasks
- Validation steps
- Open decisions / prerequisites

## Likely next step

Usually `review` in plan mode, or execution if the user prefers.

Do not enter the next skill automatically. Suggest it and wait for approval. If approved, invoke it.
