Dear Unanet hiring team,

The Russians have a saying for things that match perfectly: "like two drops of water." From what I can see of your company, that's how close Champ AI's answers and the ERP's system of record need to be before a GovCon firm will entrust its books to copilot. Getting them there is the work in your posting. For ten years I've decided how data gets organized, governed, trusted; then implemented that system of organization/governing/trust.

At my current company I moved the team off a failed third-party vendor and onto a platform we built ourselves. Then for two years I was the only person making data architecture calls at a 200-person company, answering straight to company leadership. I evaluated and picked the master data management platform we adopted, then rerouted ingestion so everything flows through it instead of coming straight from source. I also rebuilt the enterprise reporting stack from scratch. Storage dropped 50% and processing time dropped over 60%. In March I got promoted to Lead Data Engineer. Now I steer our move from on-prem SQL Server to a medallion lakehouse on Azure and Microsoft Fabric, and I run hiring and onboarding for the team.

Lately most of my time goes to the AI side. I ran the first evaluation of Claude Code at my company and wrote the security framework that cleared it for prod: data guardrails, approval flows, and a custom SQL MCP server for our warehouse. Your post talks about giving AI safe, scoped access to source systems. I've done a version of that. I also build agent workflows on the Claude and OpenAI APIs and run local models through Ollama.

Unstructured data doesn't scare me either. Gutenberg-Fingerprint pulls Project Gutenberg's sci-fi, fantasy, and horror corpus every night: plain text typed up by decades of volunteers, with no consistent format. My ingestion diffs the catalog against a hash-keyed watermark, falls back across mirror URL patterns, handles mixed encodings, and flags copyrighted donations so they're never retried. Then it strips two eras of boilerplate, front matter, transcriber notes, and contents lists before spaCy measures 63 stylometric series per book. It runs alone on a ~$5/month server with dbt Core and Dagster.

OpportuneAI and ProposalAI follow another old Russian rule: "measure seven times, cut once." Make the go/no-go call first, then write the proposal. An AI data foundation should be built the same way. If it sounds like I might be a fit for the role, reach out - that data foundation is something I'd be happy to contribute to.

All the best,
Sander VanWilligen