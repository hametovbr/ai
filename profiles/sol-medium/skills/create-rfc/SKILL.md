---
name: create-rfc
description: Use when drafting or revising a Request for Comments (RFC) to compare options and align stakeholders on a significant technical, product, policy, vendor, or process decision. Do not use for implementation-only design documents, READMEs, or routine notes.
license: CC-BY-4.0
metadata:
  author: Tech Leads Club - github.com/tech-leads-club
  version: '1.0.0'
---

# RFC Creator

Create a decision document that makes the problem, criteria, alternatives, recommendation, and eventual outcome inspectable.

## Boundary

Use an RFC when the decision itself needs review or approval. If the direction is already decided and the user needs implementation detail, use the repository's technical-design workflow. For an architecture choice that is not yet supported, use `making-architecture-decisions` before recording the recommendation.

Write in the language of the user's request. Keep established technical terms and names unchanged where that reads naturally.

## Workflow

1. Extract the title, current state, problem, urgency, impact, scope, stakeholders, assumptions, decision criteria, options, evidence, and desired decision date from supplied context. Do not ask for information already present.
2. Ask only for a missing fact that blocks a useful RFC and cannot be represented honestly as `TBD`. If the topic and decision are clear, draft immediately and mark unknown owners, dates, costs, or evidence as `TBD` with their decision impact.
3. State decision criteria before comparing options. Separate must-haves from preferences.
4. Compare at least two credible choices when a decision is open. Include the status quo when inaction is viable or has material cost. Do not invent a weak alternative to make a preferred option win.
5. Tie the recommendation to the criteria and evidence. Mark assumptions, confidence, rough estimates, and unresolved questions explicitly.
6. Leave the outcome as pending until the decision is actually made. Action items should describe the decision process; implementation detail belongs downstream.
7. Check the draft against the quality gate, then stop.

## Minimum document

- Header: title, status, impact, driver/approver and decision date when known
- Background: current state, problem, why now, and cost of inaction
- Assumptions: confidence and invalidation trigger for material assumptions
- Decision criteria: ordered or weighted before the options
- Options: credible alternatives evaluated on the same criteria, with costs and risks
- Recommendation: rationale, trade-offs, and unresolved evidence
- Action items: review and decision steps with owners when known
- Outcome: pending placeholder, then final decision and rationale after approval
- References: evidence and related work when available

Read [section templates](references/section-templates.md) when generating a full RFC or when the organization has no local template. Prefer an existing repository or company template when one exists; adapt the reference rather than forcing every field.

## Quality gate

The RFC is ready for review only when:

- the problem and decision are distinct from the proposed implementation;
- criteria precede options and every option is judged against them;
- the recommendation does not overstate evidence;
- disadvantages, migration/rollback effects, and the cost of inaction are visible when material;
- assumptions and `TBD` fields show who or what can resolve them;
- the outcome is not presented as approved without evidence of approval.

Return the RFC itself. Add a short list of blocking `TBD` items only when they prevent a decision; do not append generic publishing or meeting suggestions.
