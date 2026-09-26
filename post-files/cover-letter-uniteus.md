# Unite Us - Cover Letter

Dear Unite Us hiring team,

I'm the Lead Data Engineer at Pharmacists Mutual, where I set the architectural direction for our move off on-prem SQL Server and SSIS onto a medallion lakehouse on Azure and Microsoft Fabric, and I lead the small team that owns the company's analytical reporting. I want my next stop to have a more obvious, observable effect. Your post lines up with that - a network tying healthcare/government/community organizations together, so that people actually get the care they need.

Over ten years I've owned an ETL and data warehouse stack end to end. I rebuilt enterprise reporting from scratch after our vendor collapsed, integrated Ataccama MDM so data flows through governed master records instead of straight from source, and reported architecture decisions directly to company leadership as the sole data strategist. I've since grown into leading a team. I recruited and trained a new senior data engineer - we call him "Second Dave", since we already had one. I led the planning and implementation that turned two federal/state reporting systems - systems that used to live in "First Dave's" head - into documented, team-owned products.

My personal project, Gutenberg-Fingerprint, is closer to your stack: a nightly CDC pipeline in Postgres, dbt Core, and Dagster, with SCD2 snapshots, source-freshness checks, a full test suite, all provisioned with Terraform, all running on a $5/month VPS. With all due candor, it's not Snowflake and Airflow. Same pattern though, warehouse plus dbt plus orchestrated ETL, just solo and cheap. SQL Server and dbt transfer fast, and I pick up new warehouse engines quickly. (Personally, I think learning new things is what separates human beings from oxen.)

Reach out if any of this experience and enthusiasm sounds like it would transfer to the Unite Us culture.

All the best,
Sander VanWilligen

# Question Answers

## Describe your experience working with healthcare datasets, specifically claims or clinical data.

I haven't worked with healthcare claims or clinical data directly, and I'd rather say so up front. The closest I have is years of insurance claims data at Pharmacists Mutual, including workers' comp claims with injury and accident descriptions (sensitive data / PII) that need careful handling. I've built the pipelines, SQL models, and reporting around that data, with Ataccama MDM/DQ for quality and matching, and least-privilege access keeping sensitive fields limited to the people who need them. HIPAA would NOT be new to me, and treating sensitive claims data carefully is old-hat.

## We are looking for advanced SQL and Python skills. Describe how you use these tools in your day to day.

SQL is my bread and butter, my daily grind, my oeuvre. I write and tune T-SQL for our SSIS pipelines, build Tabular/DAX models, and run ad hoc analysis on SQL Server, and I'm running dbt's SQL-plus-Jinja models for every one of my personal analytics pipelines (and begging my manager to adopt it as we move to Fabric - support is in preview last time I checked). I'm no stranger to Python: I've built several projects running FastAPI, and spaCy ingestion is what Gutenberg-Fingerprint (gufime.com) runs on.
