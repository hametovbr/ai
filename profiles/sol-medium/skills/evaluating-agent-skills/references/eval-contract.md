# Provider-neutral skill eval contract

Use these semantic fields as a checklist or adapt them to the available runner. They are not a required file format or universal adapter API.

## Contents

1. Decision contract
2. Intervention modes
3. Case and run records
4. Graders
5. Analysis and verdicts
6. Trigger and selection evals
7. Maintenance
8. Risk controls
9. Evidence basis

## 1. Decision contract

Record before running:

```yaml
decision:
  question: "Which choice will this evidence change?"
  candidate: "exact skill version or bundle"
  counterfactual: "no skill, frozen incumbent, or named alternative"
  approved_claim: "narrow claim the design can identify"
  prohibited_claims: []
  threshold: "decision rule fixed before decision evidence"
  error_costs: {false_positive: "...", false_negative: "..."}
scope:
  kind: fixed_suite | target_population
  target_population: "or null for a fixed-suite claim"
  sampling_frame: "source and selection method"
  strata: []
  weights: "prespecified weights or null"
evidence:
  tuning_use: "none or disclosed use"
  decision_set: "frozen set or declared low-risk validation-as-decision"
  sufficiency_rule: "PASS/FAIL/INSUFFICIENT_EVIDENCE conditions"
```

Use an untouched final set for repeated optimization or consequential release decisions. For small low-risk work, preregistered validation-as-decision or cross-validation may be sufficient when reuse and weaker independence are explicit. Create regression coverage from accepted behavior; do not confuse it with capability discovery.

## 2. Intervention modes

| Mode | Intervention | Supported claim | Unsupported claim |
|---|---|---|---|
| Natural selection / end-to-end | Make the skill available to the normal runtime | Total configured-system effect, including selection | Conditional instruction quality or selection quality alone |
| Selection-only | Observe the runtime's direct activation/selection signal | Selection behavior for the observed signal | Downstream task success |
| Forced-loaded | Load the skill before task execution | Behavior conditional on loading | Natural selection quality |

Use multiple modes only when the decision requires decomposing effects. When activation is unobservable, record it as unavailable—not false—and restrict the verdict to observable downstream behavior.

## 3. Case and run records

Minimum case record:

```yaml
case:
  id: "stable identifier"
  input: "realistic task"
  should_select: true | false | unknown
  expected_outcome: "observable end state or artifact"
  mandatory_invariants: []
  forbidden_side_effects: []
  reference_solution: "known-good solution or solvability proof"
  tags: [capability, boundary, failure-mode, risk]
  grader_ids: []
```

Review cases for ambiguity, impossibility, contamination, shortcuts, duplicates, hidden dependencies, and target-distribution coverage. Include paraphrases, hard adjacent negatives, edge conditions, missing inputs, conflicts, and costly failures where relevant.

Minimum run record:

```yaml
run:
  case_id: "..."
  variant: "candidate or counterfactual"
  intervention_mode: natural_selection | selection_only | forced_loaded
  skill_version: "digest or immutable reference"
  model: "actual identifier/version when observable"
  agent_runtime: "name/version/config digest"
  tools_environment: "versions, fixtures, permissions, state"
  budgets: "time, tokens, retries, tool limits"
  randomness: "settings/seed when supported"
  repetition: 1
observation:
  activation_signal: true | false | unavailable
  output_or_artifact: "reference"
  external_end_state: "reference or unavailable"
  invariant_evidence: []
  errors_side_effects: []
  resource_use: {}
  trace: "minimum necessary observable trace or unavailable"
```

Start each comparable trial from clean isolated state. Keep fixtures, budgets, tools, grader versions, and other material factors fixed or report the confound. Separate task failure, agent/model variance, harness failure, invalid case, and grader failure.

## 4. Graders

Use the least subjective trustworthy grader for each dimension:

1. Deterministic checks for files, schemas, exact required fields, state, permissions, and side effects.
2. Model graders for irreducibly semantic dimensions.
3. Human judgment to define rubrics, calibrate subjective graders, adjudicate material disagreements, and inspect novel failures.

Each grader contract states:

```yaml
grader:
  id_version: "..."
  dimension: "one primary quality dimension"
  evidence_required: true
  labels_scale: "defined labels and anchors"
  abstention: "unknown/insufficient evidence behavior"
  blind_fields: [candidate_identity]
  order_handling: "randomized/counterbalanced when pairwise"
  validation: "known-good/bad anchors and human comparison"
  failure_policy: "invalid, abstain, retry, or manual review"
```

Do not let fluency, length, style, model identity, or answer order stand in for the target criterion. Periodically revalidate model graders after model, rubric, domain, or task-distribution changes.

## 5. Analysis and verdicts

Name before choosing statistics:

```yaml
analysis:
  estimand: "quantity the comparison estimates"
  scope: fixed_suite | target_population
  sampling_unit: "case, trial, user, session, or cluster"
  dependency: "repeated trials, shared fixtures, paired variants, clusters"
  trial_reducer: "first try, mean probability, any-success, all-success, etc."
  effect: "paired difference or other decision-relevant contrast"
  uncertainty: "method and the uncertainty source it represents"
  missing_invalid: "predeclared handling"
```

Select the reducer from the user-facing reliability question. Use paired comparisons when variants share cases. Do not treat repeated trials nested within a case as new independent cases. A fixed curated suite supports a descriptive fixed-suite estimand; population claims require a defensible sampling frame, stratification, or prespecified weighting.

Report raw counts, case-level results, slices, uncertainty or an explicit insufficiency limitation, worst regressions, grader evidence, costs, and side effects. Avoid an aggregate that lets one surface hide another.

Verdict contract:

```yaml
report:
  decision: "..."
  verdict: PASS | FAIL | INSUFFICIENT_EVIDENCE
  supported_claim: "..."
  unsupported_claims: []
  configuration_scope: "versions and conditions"
  primary_effect: "estimate plus uncertainty/limitation"
  critical_regressions: []
  grader_harness_health: "..."
  residual_risks: []
  next_smallest_evidence: "only when insufficient"
```

## 6. Trigger and selection evals

Maintain two distributions when operational triggering matters:

- A balanced diagnostic set of positives and hard near-miss negatives for boundary stress.
- A representative set, or an explicitly reweighted estimate, for operational claims.

Report TP/FP/TN/FN, recall, false-positive rate, and slices. Interpret precision only at a stated target prevalence. Record full selected sets, co-activation, rank, or load order only when the runtime exposes them and the decision needs them.

If no direct activation signal exists, do not construct a selection confusion matrix from final answers or tool calls. Call the metric behavioral and weaken the claim.

## 7. Maintenance

Version the suite, graders, rubrics, case membership, thresholds, runner/configuration, and result snapshots. Trigger review when any of these changes:

- skill, model, agent/runtime, tools, environment, policy, grader, or target task distribution;
- observed production or support failure;
- unexplained score shift, grader drift, contamination, or shortcut;
- safety, privacy, permission, or external-service boundary.

On refresh: revalidate tasks/reference solutions and graders; rerun relevant counterfactuals; add new failure cases; retire cases with reasons rather than erasing history; preserve old suite snapshots and results. A bridge run can estimate overlap/discontinuity, but it cannot restore longitudinal comparability after the measured construct changes.

## 8. Risk controls

Scale controls to data sensitivity, tool capability, and impact. For real/private data, external graders/log destinations, credentials, or side-effecting tools:

- prefer synthetic, minimized, or redacted data;
- approve destinations, retention, and permitted endpoints;
- isolate state and credentials with least privilege;
- define forbidden effects, side-effect budgets, and stop conditions;
- capture enough audit evidence to detect unintended interactions;
- clean up and verify end state;
- obtain separate authorization before production effects or real-data expansion.

## 9. Evidence basis

Transferable principles were synthesized from primary and official sources; their provider/framework mechanics are examples, not requirements:

- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills: evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills)
- [Agent Skills: optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)
- [Anthropic: demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [OpenAI: contextual eval methodology](https://openai.com/index/evals-drive-next-chapter-of-ai/)
- [Google ADK: evaluating agents](https://adk.dev/evaluate/)
- [UK AISI Inspect: tasks, scoring, model grading, and metrics](https://inspect.aisi.org.uk/metrics.html)
- [Zheng et al.: LLM-as-a-judge biases](https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf)
- [NIST AI TEVV](https://www.nist.gov/ai-test-evaluation-validation-and-verification-tevv)
