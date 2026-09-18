# Sander VanWilligen

**Polk City, Iowa** | sam.vanwilligen@gmail.com | (515) 451-0262 | [GitHub](https://github.com/sandervw)

---

Lead Data Engineer with 10 years of experience designing and owning enterprise insurance analytics. Built end-to-end data pipelines, from ETL ingestion and master data management through OLAP architecture and executive dashboards, as primary data strategist reporting directly to C-suite. Now leading a data engineering team: owning hiring, architectural direction, AI training/adoption, and a lakehouse migration to Azure cloud.

---

## Experience

### Pharmacists Mutual - Algona, Iowa

**Lead Data Engineer** | March 2026 - Present
- Promoted to lead the data engineering team, owning data strategy, architectural decisions, hiring, and onboarding for the company's analytical reporting.
- Set architectural direction for the platform: migration from on-prem SQL Server and SSIS to a medallion lakehouse on Azure and Microsoft Fabric.
- Recruited and onboarded a senior data engineer, and trained the team on the Ataccama MDM/DQ platform, our end-to-end SSIS ETL, converting undocumented, single-owner knowledge into a team-owned product.
- Championed Claude Code adoption across the org; ran the initial evaluation and authored the security framework (data guardrails, approvals, custom Warehouse SQL MCP) that cleared it for production.

**Senior Software Engineer** | 2024 - March 2026
- Rebuilt enterprise analytical reporting from scratch, replacing legacy vendor logic with documented SSIS, SQL architecture, Tabular models, and Power BI, cutting storage 50% and processing time over 60%.
- Integrated Ataccama MDM into the data pipeline, redesigning ingestion to flow through master data management rather than direct from source.
- Led evaluation and recommendation of the MDM platform adopted by the organization; served as primary decision-maker for all data architecture and strategy initiatives, reporting directly to C-suite as sole owner.

**Software Engineer** | 2020 - 2024
- Assumed full ownership of the enterprise ETL, SQL data architecture, and Tabular/Power BI reporting stack, transitioning the team from a failed third-party vendor to an internal platform.
- Designed and maintained SQL Server databases, SSIS packages, and DAX-driven Tabular models powering executive dashboards.

**Developer** | 2018 - 2020
- Built a Java integration with Paymentus to enable automated payments and paperless billing.
- Initiated the rebuild of the ETL and reporting architecture after the analytical reporting vendor ceased operations, establishing the replacement platform.

**IT Contractor / Intern** | Summer 2016 - December 2017
- Developed a nightly Java process running government OFAC compliance screenings; cleared the full SSRS report backlog; supported internal and external .NET applications.

---

## Projects

**[Gutenberg-Fingerprint](https://github.com/sandervw/Gutenberg-Fingerprint)** ([gufime.com](https://gufime.com)) - Nightly change-data-capture stylometrics pipeline, designed and operated solo on one ~$5/month OVH VPS: Postgres, plain Python, and dbt Core orchestrated by Dagster OSS, published to Cloudflare Pages. A watermark table drives CDC; a dbt fact constellation adds SCD2 snapshots, source freshness, audit logging, and a full test suite, compiling against DuckDB (dev) and Postgres (prod). Backups ship to Cloudflare R2; the Evidence.dev site and Dagster UI run behind a Cloudflare Tunnel; OpenTofu provisions everything. Grew out of [Fiction-Fingerprint](https://github.com/sandervw/Fiction-Fingerprint).

---

## Education

### Iowa State University - Ames, Iowa

**B.S. Software Engineering** | Graduated December 2017
Dean's List - Fall 2013, Spring 2014, Spring 2015, Fall 2015, Spring 2016

---

## Technical Skills

**Data Platform & Architecture:** Microsoft Fabric (Lakehouse, Warehouse, Data Factory, OneLake), SQL Server, MongoDB, Medallion/Kimball modeling, semi-structured/NoSQL data, CDC, dbt Core, Dagster, DuckDB, Tabular Models, Power BI, Evidence.dev, SSIS, SSRS
**Master Data Management:** Ataccama MDM/DQ
**Cloud & Infrastructure:** Terraform, Cloudflare, Azure, Logic Apps, Bicep, Entra ID/RBAC, cost governance
**Languages & Scripting:** SQL, T-SQL, Python (spaCy, pandas), DAX, PowerShell, TypeScript, JavaScript, Java, C# (.NET)
**AI & Automation:** Claude API/SDK, OpenAI API, Claude Code, Opencode, Ollama, agentic development workflows
**Tools & Practices:** Git, GitHub Actions, CI/CD, Agile/Scrum, Visual Studio, SSMS, VS Code
