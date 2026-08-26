# Working in this repo

This is a personal job-search repo. It has one user, no reviewers, no CI, and
nothing here is precious except the two CSVs. Optimize for finishing the job
without the owner having to log in and click things.

## Commit straight to main. Never open a pull request.

- `main` is the only branch. Work on it directly: `git checkout main`.
- Commit and `git push origin main` when you're done. That's the whole workflow.
- **Do not create a pull request.** Not for routine runs, not for changes to the
  routine prompts, not for anything. A PR here is a bug — it means the owner has
  to go merge it by hand, which is the exact thing this file exists to prevent.
- Do not push `claude/*` branches. If you find yourself on one, switch to `main`
  and commit there.
- If a push is rejected because the remote moved: `git pull --rebase origin main`
  and push again (retry up to 3 times).

## Don't ask for approval

Make the obvious call and proceed. Editing the CSVs, adding prospects, changing
a routine prompt, deleting rows that no longer apply — all pre-approved, just do
it and say what you did. Only stop and ask if something would destroy
application history that can't be reconstructed.

## Hard rule: no insurance

Sander does not want insurance work in any form — carriers, health-insurance
payers, reinsurers, insurtech, brokers/MGAs, claims platforms, actuarial firms,
or any role whose core domain is insurance, claims, underwriting, or actuarial
data. This holds no matter how well the tech stack matches. Never suggest one,
never add one to `data_eng_job_search.csv`, and never add an insurance sector
back to `sectors.py`.

## Files

- `SanderVanwilligen-DE.md` — resume.
- `sectors.py` — the sector list + random draw. The daily search routine runs
  this to pick its 3 sectors; it does not choose them itself.
- `data_eng_job_search.csv` — prospect list (jobs to consider).
- `job_applications.csv` — application tracker. This one is real history:
  update rows, never drop or reword them.
- `routines/` — the prompt text for the scheduled Claude Routines. Keep these in
  sync with the live routines; if you change a routine, update its file here too.
