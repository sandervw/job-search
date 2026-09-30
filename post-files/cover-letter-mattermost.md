# Mattermost - Cover Letter

Dear Mattermost hiring team,

Secure, self-hosted collaboration is my kind of challenge - it's why I want to join your team, and why I'm applying for the Senior Full Stack Engineer role.

I've shipped software for ten years: I like owning a thing from schema to deploy. Your post calls for a full-stack senior, and my personal projects cover every piece of it. Leaves (https://github.com/sandervw/LeavesApp) is a Node/TypeScript/Express API with a React front end. Zod checks every request, refresh tokens rotate through httpOnly cookies, test suites run Vitest, Supertest, and React Testing Library. Dying Skies (https://github.com/sandervw/dying-skies) is a React/TypeScript Canvas front end on FastAPI and Postgre, with auth and rate limiting. Go is my one gap. I haven't shipped it professionally. I pick up stacks fast though, and your post says you'd rather hire people who get things done.

At Pharmacists Mutual, I get things done. Right now I lead the data engineering team. Architecture, hiring, mentoring, training, one-on-ones, and code standards are the leadership side of my responsibilities - I'm about 36% leader, 64% hands-on. I pushed agentic coding tooling (Claude Code) across the company, for both the software and data engineering teams: I ran the training, ran the evaluation, and wrote the security framework that cleared Claude for prod: guardrails, approval flows, and a custom SQL Server MCP. Agentic development is my bread and butter now. I also rebuilt our enterprise reporting platform from scratch. Storage dropped 50% and processing time over 60%.

If anything of this sounds like it would be a good fit in your team, I'd be happy to chat. Thanks for reading.

All the best,
Sander VanWilligen

# Question Answers

## Describe one specific way you've used an AI coding agent in your daily work.

I use Claude Code every day for Agile story delivery on our data platform. I built a custom SQL Server MCP so it can reach DEV, UAT, and PRD with least-privilege logins and managed settings. It inspects schemas and runs queries, nothing broader. I keep a library of custom skills for the recurring tasks, and everything it writes gets my review before it ships. Since we implemented agent-augmented coding, story delivery time has been halved across the team.