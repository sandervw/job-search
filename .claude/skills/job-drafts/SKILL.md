---
name: job-drafts
description: Draft answers to a job post's application questions and/or a cover letter for Sander. Use when the user asks for job-post answers, application question drafts, or a cover-letter draft for a specific posting.
---

# Job application drafts

Draft application-question answers and/or a cover letter for a specific job posting. Output is a starting point Sander will revise, so write concrete, confident, non-generic drafts grounded in the files below — no filler, no invented facts.

## Which resume

The user names the resume in their prompt. Read only that one:

- Data Engineer → `resumes\SanderVanwilligen-DE.md`
- Software Engineer → `resumes/SanderVanWilligen-SE.md`

If they don't say, ask which before drafting.

## Read before drafting

1. `post-files/job-post.md` — the posting (questions live here).
2. `post-files/personal-details.md` — background on Sander.
3. The chosen resume (only one; from the *project root*).
4. Web-search the company (a couple of `WebSearch` calls) for background: what they do, product, recent news, tech stack. Weave in only what's relevant.

## Write

- **Answers** → `post-files/job-answers.md`. Each question restated as a heading, its draft below. Under 100 words each unless the user says otherwise.
- **Cover letter** → `post-files/cover-letter.md`. 250–400 words, three or four short paragraphs.

Do only what the prompt asks — answers, cover letter, or both. Overwrite the target files. After writing, tell the user word counts and note anything you were unsure about.
