# Beacon Biosignals - Cover Letter

Dear Beacon Biosignals hiring team,

Beacon's Datastore challenge is my favorite kind. Row-level security, GraphQL surface, answers to questions like, "what did this re-scored data look like before?" That's why I'm applying for the PostgreSQL & Data Modeling side of this role.

At Pharmacists Mutual I lead a small data engineering team. My current project is setting and implementing the architectural direction for a migration off on-prem SQL Server/SSIS to a medallion Azure lakehouse. I also rebuilt the company's enterprise analytical reporting from scratch, replacing legacy vendor logic with documented SQL architecture and Tabular models, cutting storage 50% and processing time over 60%. I ALSO redesigned ingestion to route through a Master Data Management platform (instead of landing straight from source) which meant planning out schema constraints and relationships.

Outside of work, I designed and operate Gutenberg-Fingerprint, a nightly CDC stylometrics pipeline running in production on my own VPS. A dbt fact constellation adds SCD2 snapshots so I can answer point-in-time questions, backed by a full test suite and audit logging, compiling against DuckDB in dev and Postgres in prod.

I write SQL daily (by hand and with an agent), reason about indexes and query plans, and would welcome going deeper into Julia. I'd like to bring my experience (and enthusiasm) to Beacon's Datastore.

All the best,
Sander VanWilligen

# Question Answers

## In a few sentences, provide some specific detailed examples of your work in the area of emphasis you selected in the previous question (Datastore Systems or Postgres and Data Modeling). Please include the name of the employer you did the work for.

At Pharmacists Mutual, I redesigned data ingestion to route through Ataccama MDM instead of landing directly from source, which meant planning out schema constraints and relationships. I set the architectural direction for our ongoing migration off on-prem SQL Server/SSIS to a medallion lakehouse on Azure. On my own time, I built and operate Gutenberg-Fingerprint, a Postgres-in-production pipeline with a dbt fact constellation using SCD2 snapshots.
