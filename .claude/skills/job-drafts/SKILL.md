---
name: job-drafts
description: Orchestrate cover-letter and application-answer drafts for every job post in post-files/. Picks a resume per post, spawns a Sonnet drafting agent and a job-voice agent per post, then reviews the results. Use when the user asks for cover letters, job-post answers, or application drafts.
---

# Job application drafts (orchestrator)

Drafts are starting points Sander will revise. Leave all output uncommitted. Don't move or delete the post files.

## 1. Pick resumes

- Glob `post-files/job-post-*.md` and skip the blank `job-post.md` template. `COMPANY` comes from the filename suffix, e.g. `job-post-stripe.md` → `stripe`.
- Read both resumes: `resumes/SanderVanwilligen-DE.md` (data engineering) and `resumes/SanderVanWilligen-SE.md` (software engineering).
- Read each post. Pick the resume that best fits that post's role and requirements. Choose separately for each run, from the posts that exist at that time. Don't assume.

## 2. Drafting agents

Launch one agent per post, all in parallel, with `subagent_type: general-purpose` and `model: sonnet`. Keep the prompt to this, with the placeholders filled in:

> Draft a cover letter and application answers for Sander. Read ONLY these files: `post-files/job-post-COMPANY.md`, `personal-details.md`, `RESUME`, `post-files/cover-letter-answers.md` (output template). Research the company with at most 4 WebSearch and 4 WebFetch calls. Use only what's relevant (product, recent news, tech stack).
> Write `post-files/cover-letter-COMPANY.md` following the template. Cover letter: 300-450 words, 3–4 short paragraphs. Answers: one `##` heading per question from the post's "Job Questions" section, each answer UNDER 125 words. If the post has no questions, write "None" under that heading.
> Be concrete and confident. Nothing generic, no filler, and don't make up any facts. No invented anecdotes either: every story, detail, and lesson learned must come from the files you read. If a question needs something they don't cover, write `[TODO: Sander to fill]` instead. Check the word counts with `wc -w` (per section) and trim until they meet the limits. Reply with only the word counts and anything you weren't sure about.

## 3. Voice agents

When a drafting agent finishes, launch `subagent_type: job-voice` with the prompt: `Edit post-files/cover-letter-COMPANY.md.`

## 4. Review

Read each final `post-files/cover-letter-COMPANY.md`. Give Sander a short list for each company: which resume you used, word counts, and 2–4 notes or things to consider (weak claims, facts to verify, missing hooks, questions that need his own input).
