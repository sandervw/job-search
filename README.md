# job-search

Source-controlled north star for Sander's job search.

- `SanderVanwilligen-DE.md` — current resume.
- `sectors.py` — the sector list, plus a random draw. The daily search routine
  runs `python sectors.py` to pick the 3 industries it searches that day; it
  does not get to choose them itself. **Insurance is excluded on purpose and
  never goes back in.**
- `data_eng_job_search.csv` — running prospect list (jobs to consider).
- `job_applications.csv` — application tracker (source of truth for the
  "Daily Job Tracker" Claude Routine, which reads, updates, commits, and emails it).
- `routines/` — the prompt text for each scheduled Claude Routine.

Roles are sought in priority order: **AI Engineer**, then **Analytics
Engineer**, then **Data Engineer** last.

## Branching

**`main` is the only branch.** Everything is committed directly to `main` — no
feature branches, no pull requests, no merges to approve. See `CLAUDE.md`.
