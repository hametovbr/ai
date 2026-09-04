---
name: find-skills
description: Discover and compare installable agent skills when the user asks to find a skill, extend the agent with reusable capability, or search the agent-skills ecosystem. Do not activate merely because a general task could conceivably have a skill, and do not install anything unless the user requests installation.
---

# Find Skills

Find a small set of relevant, trustworthy skills and distinguish discovery from installation.

## Procedure

1. Identify the concrete capability, runtime, and any source or owner constraint. Ask only when the answer would materially change the search.
2. Search the runtime's available skill catalog first. For external skills, use an available skill discovery tool or:

   ```bash
   npx skills find <focused query> [--owner <owner>]
   ```

   Try a small number of specific synonyms if the first query is weak.
3. Inspect each candidate's current manifest and `SKILL.md` before recommending it. Verify that its trigger, workflow, runtime dependencies, license, source repository, and requested permissions fit the user's need.
4. Treat popularity, install counts, stars, and publisher reputation as supporting signals rather than proof of quality. Verify any such numbers live before reporting them.
5. Present one to three best matches. For each, give the package identifier, what it covers, important dependencies or permissions, evidence of maintenance or trust, and the source or catalog link.
6. If nothing suitable exists, say what was searched and offer to handle the task directly or help create a skill.

Install only after the user chooses a package or explicitly delegates the choice. Use the package manager supported by the target runtime; for the Skills CLI this is typically:

```bash
npx skills add <owner/repo@skill> -g -y
```

After installation, report the installed package and location and surface any warnings. Do not imply that search results were installed.
