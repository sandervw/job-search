# Question Answers

## Why are you interested in joining Tala?

I want out of insurance, plain and simple. Tala's focus on credit access for people the banking system ignores is something I can actually get behind. The role also fits how I like to work: architecture and hands-on building in the same job. I've spent the past year pushing my own team toward AI-native analytics, so that part of your post landed easily too.

## How many years of experience do you have as a tech lead or tech lead manager (as opposed to individual contributor without lead scope)?

About six months with an actual lead title. I got promoted to Lead Data Engineer in March 2026, where I run a small team and own hiring, onboarding, mentoring, and architecture calls. Before that, starting in 2024, I was the sole architecture decision-maker for the company's data platform and reported straight to company leadership, just without the formal title or direct reports.

## Do you have strong hands-on Python & SQL experience?

Yes. SQL and T-SQL have been my daily bread and butter for 10 years, including deep SQL Server internals work. Python came later but I use it hands-on now: I've written extensive raw-text cleaning/ingestion models in it. One specific example - Gutenberg-Fingerprint (gufime.com) uses spaCy to pull and process raw text files from the Project Gutenberg source of public domain works, stores it in a Postgres DB, and uses dbt for the modelling, plus tests and CDC logic included.

## Describe a data/analytics platform or semantic-layer initiative you personally took from architecture through production. What did you personally own or build, and who used it?

I rebuilt Pharmacists Mutual's enterprise reporting stack from scratch after the vendor platform collapsed: SQL Server architecture, SSIS ETL, DAX-driven SSAS Tabular models, and Power BI dashboards. I designed the schema myself, built the pipelines, built the semantic models, later folded in Ataccama Master-Data-Management and Data Quality, so that all of our customer/policy/claim records have a single source of truth. The new platform replaced undocumented vendor logic, cut storage 50%, cut processing time over 60%, and it's what executives and company leadership use directly today.
