---
name: synthesis-voice-profiler
description: "Generate a structured writing-voice profile from sample texts and targeted diagnostic questions. Use when asked to analyze writing style, extract a voice, create a writing DNA or voice section, or build reusable writing instructions. Keep conclusions to observable writing patterns rather than inferred personal traits."
license: "CC0-1.0"
metadata:
  author: "Rajiv Pant"
  version: "1.0.0"
  source_repo: "github.com/synthesisengineering/synthesis-skills"
  source_type: "public"
---

# Synthesis Voice Profiler

Analyze the user's writing and produce a portable, paste-ready voice section for an agent instruction file. Describe observable choices rather than the writer's personality, and distinguish evidence from stated preferences.

## Procedure

1. Collect three to five substantial samples written primarily by the user. Prefer samples they consider representative and, when useful, include more than one content type. Read provided files or accessible URLs. Note collaboration, heavy editing, audience, or genre when known because these weaken attribution.
2. If the samples are too short, homogeneous, or heavily edited to support a reusable profile, explain the limitation and request the smallest additional sample needed.
3. Analyze recurring patterns across:
   - vocabulary, register, jargon, and concreteness;
   - sentence-length variation, fragments, voice, and paragraph shape;
   - questions, analogy, direct address, repetition, humor, and emphasis;
   - openings, transitions, section structure, lists, and endings;
   - confidence, emotional register, and relationship to the reader;
   - punctuation and formatting.
4. Record evidence for each candidate pattern: which samples show it, whether it recurs, and whether genre explains it. Do not treat a word or device that is absent from a few samples as something the user forbids.
5. Ask only the targeted diagnostic questions needed to resolve consequential ambiguity, up to five. Cover explicit dislikes or forbidden phrases directly; negative constraints must come from the user's statement or strong positive evidence of a consistent alternative. Ask questions one at a time when answers affect later questions.
6. Draft the profile, then check that every instruction is observable, actionable, and appropriately qualified. Separate stable voice traits from context-dependent variations.
7. Present the evidence summary and paste-ready profile. Ask the user to correct what feels wrong or missing, then revise. Save or edit an instruction file only when the user requests that action and identifies the target.

## Deliverable

First provide a compact evidence table with the observed pattern, sample evidence, and confidence. Then provide a Markdown section in this adaptable shape:

```markdown
## Voice & Writing Style

### Characteristics
- [Stable, observable patterns]

### Sentence and Structure
- [Sentence rhythm, paragraph shape, openings, transitions, endings]

### Vocabulary and Tone
- [Register, jargon, concreteness, confidence, humor, reader relationship]

### Context Shifts
- [How choices change by audience or format, if supported]

### Avoid
- [Only user-confirmed constraints or strongly evidenced alternatives]
```

Omit unsupported sections and include formatting preferences when they are material. Phrase the rules so another writing workflow can apply them without access to the samples. Do not claim that unrelated skills will consume the profile automatically; integration depends on whether the target runtime loads that instruction file.
