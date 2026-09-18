**Prompts:**

Hey claude, read the attached job post. I work for a tech company as an engineering manager. We recently posted this position to our job board. Study the job itself first, so you have a full understanding of our requirements. Let me know when you understand.

I want you to review a candidate's application. Attached is their resume (I converted it to MD for you) and their github profile. I want you to study the resume, and any public information they share in their github. https://github.com/sandervw
1. Does this candidate seem real? Is this an AI app?
2. Does the experience the candidate claims hold out?
3. Do they seem like a good fit for this job? Should we consider them?
4. Any other warning, or even anything interesting, you think I should know?
5. Is this candidate worth a call, or pass? Justify your answer.

Hey claude, what's the good/bad/over/under of working at **twilio**? Also, what's the company age and rough headcount?

**Email Replies:**

I understand, and thank you for the notice. Good luck with your candidate search - and if you ever have opening you think I'm a stronger fit for, feel free to reach out again.

Thanks,
Sander

**Question Answers:**

I write dark fantasy fiction, and that hobby quietly became my teacher in working with AI.

For years I've been writing in original settings and published them online. Somewhere along the way I started using LLMs as writing collaborators, which meant confronting their worst habit: patterns. Ask a model for atmosphere, or dialogue, and it will gladly write the same three clichés forever. Fixing that sent me down a rabbit hole, building anti-repetition toolkits, custom skills that enforce voice and constraints, and eventually a stylometrics pipeline that fingerprints authors by their measurable habits.

None of it was for work. But it taught me prompt engineering, evaluation, and human review, where the bar was "does this read like it was written by a person, with hot blood, and four chambers to pump it?" I learned that AI is about as good as it's guardrails, and that 'engineering' lives in the gaps.

That's the mindset. I build the boring scaffolding, the tests and fallbacks that keeps a system reliable. And I stay curious enough to chase a problem well after it's become a pitfall and a nuisance, because I've spent half-a-decade doing exactly that for stories nobody asked me to write.

---

I think we're living in a Golden Age. Artificial Intelligence has made it look like like there is no unsolvable problem, no restriction on Learning. Working with tools like OpenRouter, OpenCode, Claude Code, etc, has enabled me to build things (websites, data transformation, heck, even my Physical desktop) that I'd never have built in 'the time before'. I love seeing and solving problems with LLMs, learning with LLMs, and helping others solve/learn.

I introduced my company to Claude Code. I get to use Agentic Tooling in my work as a Data Engineer, and I get to teach other engineers how to use it - but I DON'T feel that our leadership sees the larger picture around LLMs: not just what they can accomplish that is Good, but what they could do that is Not. There's a 'lag' on LLMs use in enterprise companies, especially Insurance. They're moving forward at a walk. At OpenRouter, I'd get to run at my top speed.

---

Before I started campaigning, no one in leadership wanted agentic tooling. They thought Microsoft Teams Copilot was AI coding, and that was the ceiling of the conversation. I made the case that real agentic development was a different category entirely, and worth investing in.

Then I pushed the harder sell: skip GitHub Copilot, the obvious brand-name default nobody would get fired for buying, and go with Claude Code, which no one had heard of. To make that safe against a production insurance warehouse, I built the internal piece myself: a custom Warehouse SQL MCP server plus a security framework of least-privilege SQL logins scoped per environment, a locked-down managed-settings.json, and approval gates on anything touching real data. I thought about blast radius before the agent could act, not after.

The proof that flipped the skeptics: a data engineer I trained shipped a Worker's Comp data export in three days that would have taken three months the old way, and delivery on typical stories dropped roughly 60% across the team.

Now everyone reaches for it daily, my boss included. It won because it was shaped to our warehouse and our security model, things no off-the-shelf product understood. The internal path took more work, and it was worth it.

---

We have a strange Policy/Claim administration system: Some Claims flow into our PAS, and our PAS writes some of its transaction data monthly, some of it daily. Our Enterprise Data Warehouse needed to ingest from all these systems, "marry" they're data, and pick the 'best values' from among the systems. I ended up rewriting the ETL that does the import from the disparate sources, wiring the non-transaction data into a Master Data Management tool (Ataccama MDM), routing that tool's Golden Records back into our Data Warehouse,  using ETL again to connect the Golden data with our financial data in a star schema, and modelling it into a Tabular model for PowerBI consumption.

For Testing/Documentation: I stick with regular, daily (many times daily) commits to Github. By the time I was done I had a bunch of commented SQL files, and I had them all wired up. All I had to do after that was bring Claude Code into the repo, and guide it through our pipelines and source. It wrote up the initial doc - which I then told it to cut back to 60% of the 'Default AI length'. After that, I did some manual review, and some back/forth. I kept our documents in markdown format, then uploaded them into Jira for regular business user use. Our MDM tool also enabled us to do Data Lineage of the various systems.

For materialization, the golden records are SCD-2s; the financial data I managed to get to reload nightly, but with a month-end backup/write to an archive database.

The biggest challenge; myself. I shot myself in the foot early on - instead of camelCase names for our tables/fields, I used snake_case. We live in a SQL Server environment: camelCase for the fact/dim tables allows it to flow through nicely into the tabular model. I had to go back and figure out a way to convert it - everywhere. Not just in the SQL: in the SSIS xml files, in the giant tabular .json file. There were thousands of column names, so not a simple find/replace. I ended up building some powershell scripts (with AI help of course) that managed to fix 99% of it automatically. It still took a couple weeks (this was before late-Opus/Fable level smarts), but it saved us (IMO) a bunch of manual editing headaches down the road.