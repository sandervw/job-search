# River Financial - Cover Letter

Dear River hiring team,

Ten years in, I still like owning a problem tip-to-tail - the interface, the service, the database, the pipeline that sends it. That's the shape of your Staff opening. I've been building that way my entire career as a software and data engineer, most recently running data engineering at Pharmacists Mutual. The Bitcoin angle of your posting is what got me reading first (somewhat selfishly - I have a recurring buy set up daily on Coinbase, and watch the daily shift like a hawk). But your stack and the level are what kept me reading.

At Pharmacists Mutual I rebuilt our enterprise reporting platform from scratch: cut storage 50%, cut processing time over 60%, done as the sole technical decision-maker reporting straight to company leadership. I also built the security framework that got agentic coding tools cleared for prod, hired and onboarded a senior engineer, and have spent the last year turning our undocumented, single-owner federal/state reporting systems into ones any team-member can pick up. That last part is bread and butter for a Staff role, setting a bar and making sure other people can (and do) hit it.

Outside work I stay sharp by building solo, full-modern-stack projects: a Node/Express and React writing tool with a tree service handling recursive traversal and delete; a canvas-render-loop screensaver site with dynamically generated music, and a FastAPI/Postgres backend; a Dagster pipeline running the same dbt code against DuckDB and Postgres. None of it is Elixir yet. The fundamentals carry over though: web, database, prod reliability. I've picked up new languages fast in the past - I love learning, I've always loved it, and I know that would carry over into your role as a Staff SE.

I'd welcome the chance to talk about how I could contribute to River Financial.

All the best,
Sander VanWilligen

# Question Answers

## Why are you interested in this role?

Your post asks for someone comfortable across the whole stack, which is basically how I've been working for years. I own architecture end to end at Pharmacists Mutual, from database design through the specific pipelines and dashboards. Publishing your financials publicly matches an instinct I already have: replace opaque systems with ones people can verify. I keep my personal, solo work public on GitHub.

## What is your proudest achievement?

Rebuilding our enterprise reporting platform from scratch, solo. Basically, our company had gotten into a position where the old vendor logic was so tangled - with me being the only one who could trace it - that I came to the realization, "If I don't rewrite this, no one ever will." This was before the age of AI, so that 'realization' might not hold up now, but back then it motivated me to tackle the problem. The company approved. Over 4 months I replaced opaque vendor logic with documented, tested systems, cutting storage 50% and processing time more than 60%, as the sole technical decision-maker reporting to company leadership. It turned a black box the whole company depended on into something my team could read, reason about, test, and extend.

## Describe a technical problem and how you solved it.

In Leaves, my writing app, templates and story nodes both needed recursive tree traversal. They were separate Mongoose models, so I was duplicating deletion and traversal logic, with real risk of a runaway recursive delete. I built a generic `TreeService<T>` base class both models extend, added Mongoose discriminators so both node types share one collection, and implemented delete traversal so that trashing a root node also removes its recursive children.
