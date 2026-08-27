---
name: evaluating-agent-skills
description: Use when designing, reviewing, comparing, releasing, or maintaining evaluations of agent skills; when measuring skill activation or selection, task outcomes, process invariants, graders, regressions, or cross-runtime evidence.
---

# Evaluating Agent Skills

## Core principle

Treat an eval as repeatable evidence for a named decision. Measure the configured system—skill, model, agent/runtime, tools, environment, budgets, and graders—not the skill alone.

Read [references/eval-contract.md](references/eval-contract.md) before creating or auditing eval work.

## Use the lowest sufficient intervention

Design evidence before automation. Default to reviewed decision/case/run/report records executed through manual or native mechanisms:

`manual review → configuration/native runner → bounded script → larger harness`

Move right only for a demonstrated requirement. Reproducibility, multiple runtimes, future models, architecture requests, or budget do not prove one.

Before proposing eval code, state:

1. the lower mechanism already tried;
2. the repeated observed defect, not a possibility;
3. the evidence invariant it violates;
4. why reviewed records or the existing facility cannot satisfy it.

If any item is missing, return `NO_CODE`. Reuse existing cases and minimum records; sections may share one file. Any new repository, runner/adapter, schema/validator/compiler, CI, storage service, database, queue, dashboard, registry, or telemetry requires the same proof. Provider neutrality belongs in semantic evidence fields, not a provider framework.

Obey repository and data-authority rules. If the current repository forbids eval artifacts, use an authorized external location; if unknown, report the placement decision—never invent a repository or bypass policy.

## Workflow

1. **Name the decision:** claim, target population or fixed suite, threshold, error costs, sufficiency rule.
2. **Choose the intervention:** natural-selection/end-to-end, selection-only with a direct activation signal, or forced-loaded conditional behavior. Do not merge their causal claims.
3. **Choose the counterfactual:** normally no skill for a safe additive skill or the frozen incumbent for a revision. Hold other material configuration fixed.
4. **Design evidence:** realistic solvable cases, hard near-misses, costly failures, tagged slices, and risk-proportionate tuning/decision separation.
5. **Grade observables:** deterministic outcome/end-state checks first; calibrated model graders for semantic dimensions; proportionate human review. Grade exact trajectories only when the path is required.
6. **Run paired clean conditions:** reset state, equalize fixtures/budgets, preserve provenance, record errors/side effects, and repeat only for a named reliability question.
7. **Analyze the estimand:** separate fixed-suite from population claims and case-sampling from trial uncertainty. Never count dependent trials as independent.
8. **Report a bounded verdict:** case/slice evidence, regressions, grader/harness health, limitations, unsupported claims, and `PASS`, `FAIL`, or `INSUFFICIENT_EVIDENCE`.
9. **Maintain the suite:** version, revalidate, rebaseline, preserve retired cases/results, and deny longitudinal comparability when the measured construct changed.

## Attribution and safety boundaries

- Without a direct activation signal, issue no selection verdict; downstream behavior supports only a downstream claim.
- Interpret trigger precision only at a stated prevalence; show confusion counts and slices.
- Use whole-skill A/B for bundle value; ablate only for a named component-level causal question.
- Validate model judges; do not treat them as ground truth.
- Scale data, external-grader, credential, tool, side-effect, stop, and cleanup controls to sensitivity and impact. Production effects require separate authorization.
