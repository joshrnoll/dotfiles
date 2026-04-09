---
name: review
description: Critically review either a plan or code and produce REVIEW.md in the matching review folder.
---

# Critical Review

## Use this when

- the user wants a skeptical review of a plan before implementation
- the user wants a skeptical review of code after implementation

## Review modes

This skill supports exactly one review mode per invocation:
- `plan`
- `code`

If the target is unclear, ask the user to choose before reviewing.

## What I will do

- review critically and directly
- identify weaknesses, omissions, risks, and unclear assumptions
- separate major concerns from secondary concerns
- document findings clearly

## What I will not do

- review both plan and code in the same invocation
- become performatively agreeable
- shift into execution unless explicitly asked later

## Completion criteria

This skill is complete only when:
1. the review mode is explicit
2. the topic name has been proposed and approved if needed
3. the correct review artifact has been written

## Artifact output

For plan review, write:
- `workflow/<topic>/plan/REVIEW.md`

For code review, write:
- `workflow/<topic>/code/REVIEW.md`

Suggested sections:
- Review target
- Overall assessment
- Major concerns
- Secondary concerns
- Recommended changes

## Review focus

In `plan` mode, focus on:
- missing steps
- feasibility gaps
- risky assumptions
- test strategy gaps
- scope problems

In `code` mode, focus on:
- correctness
- edge cases
- maintainability
- architecture fit
- test gaps
- regressions

## Likely next step

After plan review, revise planning artifacts.
After code review, revise implementation.

Do not enter the next skill automatically. Suggest it and wait for approval. If approved, invoke it.
