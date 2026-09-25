# Job Posting

```
# Staff Software Engineer, Data Platform

Boston, MA / Remote

Beacon Biosignals is transforming precision medicine for the brain, from clinical development to clinical care. For Life Sciences partners, we offer the leading at-home EEG platform for clinical development of novel therapeutics for neurological, psychiatric, and sleep disorders. Our Diagnostics business is building the most comprehensive at-home platform for precision diagnostics, combining EEG and cardiopulmonary signals to deliver reimbursable assessments for sleep and central nervous system disorders. Together, we're changing the way patients are diagnosed and treated for any disorder that affects brain physiology.

Beacon Biosignals is seeking a Software Engineer IV to join our Datastore team. The Datastore sits at the heart of Beacon's platform. It defines our foundational data model and serves as the centralized repository and API for brain data collected from clinical studies, supporting the analytical tools, services, and applications used by our scientists, clinicians, and partners.

This role emphasizes the design and scaling of backend systems for data infrastructure: PostgreSQL data models, Kafka-driven event pipelines, and the GraphQL API that makes scientific and clinical data usable - distinct from frontend development or end-user product surfaces. At this level you will lead the design of complex systems within the Datastore rather than individual components, own the pipelines that deliver dataset snapshots into our warehouse, and collaborate across platform, application and scientific teams to implement APIs that unlock new workflows in Beacon's expanding portfolio of clinical studies and digital health products.

You should have experience writing complex SQL queries by hand, and should be prepared to reason about schema design, indexes, and query behavior as a matter of course.

Two properties of our system that shape our work may influence your application. Our GraphQL API is generated from the PostgreSQL schema using PostGraphile, so a schema decision is an API decision. Secondly, row-level security is in force on effectively every table, because clinical data from different studies and partners shares one schema, with some rows shared for access by multiple internal teams. RLS predicates get injected into your queries, which makes reasoning about query plans genuinely harder here than it is in most places. If that sounds interesting rather than tedious, you'll enjoy this team.

We are hiring two engineers into this role, with two different centers of gravity. One will focus on the breadth of the Datastore: the event pipelines, the GraphQL API, core data models, and third-party integrations. The other will focus on depth in PostgreSQL (data modeling, performance tuning, operations) and supporting all engineers in developing schemas and the access controls that protect clinical data. The core requirements are the same. Tell us which one you are most drawn to in your application.

This role is 100% remote from anywhere in the U.S. Beacon's robust asynchronous work practices ensure a first-class remote work experience, but we also have in-person office hubs in Boston, New York City, and Paris.

### What success looks like

[](https://github.com/beacon-biosignals/knowledge-base/blob/4455a30e148a8932baf3ebd0fad7770636442c6d/records/job-posts/datastore-staff-software-engineer.md#what-success-looks-like)

- You lead design and architecture for complex projects and systems within the Datastore, weighing implementation trade-offs with engineering principles and backing your decisions with data rather than preference
- You partner with product managers, scientific and clinical stakeholders, and other development and support teams to translate their requirements into new integrations, services, and solutions for scaling Beacon's data platform - contributing to broader product and technical decisions, not simply implementing them
- You debug and profile ambiguous problems that cross system boundaries, including codebases beyond the Datastore's purview, and you leave what you touch better than you found it — structure, test coverage, tooling
- Peers look to your work as an example: you implement features with attention to detail, demonstrating product awareness and high standards for data integrity, design soundness, and maintainability across the lifespan of the system
- You draft RFCs to lead complex feature discovery and technical design phases, soliciting and incorporating input, and helping your team align on a set of decisions to guide development
- You plan your own work and contribute to planning the team's, making reasoned trade-offs between speed, generalizability, and technical debt, and accounting for the needs of multiple stakeholder teams
- You teach and mentor other engineers regularly, give feedback that people act on, and are sought out for it. You may act as tech lead on a project or as the coordination point for engineering practice within the team
- You leverage feedback from internal stakeholders and external partners to improve operational robustness and ease of use of the Datastore and its services via new documentation, tools, and dashboards

### What you will bring

[](https://github.com/beacon-biosignals/knowledge-base/blob/4455a30e148a8932baf3ebd0fad7770636442c6d/records/job-posts/datastore-staff-software-engineer.md#what-you-will-bring)

- 7+ years of backend development experience, including at least 3 years focused on data platforms and backend infrastructure for data-centric applications: transactional systems, event pipelines, and the APIs that serve them
- Highly proficient in at least one technical area relevant to this work: data modeling, distributed systems, API design, or database engineering, with the depth that others on a team come to you for
- Strong proficiency in SQL, with production experience working with PostgreSQL as an application database; you write and tune queries fluently and are comfortable reasoning about schema design, indexes, and query plans
- Hands-on experience with data streaming and event processing, using Kafka (our event bus) or an equivalent such as RabbitMQ, Pulsar, or a cloud-based equivalent like Amazon Kinesis
- Proficiency in Julia or Python; Julia is a core Datastore language, and experience with Julia is a strong plus, but not required — we welcome candidates eager to learn it!
- Experience deploying and operating services in containerized environments, with familiarity in Kubernetes and Infrastructure as Code (IaC) tools such as Terraform and/or Helm
- A track record of mentoring engineers and improving how a team works - practices, tooling, test coverage, or documentation that outlasted your involvement
- A collaborative mindset: you enjoy working across disciplines and believe people achieve more together than alone
- Excellent written and verbal communication skills, especially in asynchronous and remote-friendly environments
- A self-directed approach, with a track record of thriving in hybrid or fully remote teams
- Experience with, or interest in, using LLM-assisted or agentic coding tools in a production setting, with good judgment about what guardrails are needed

For the Datastore Systems role:

- You can lead design across the breadth of the platform.
- GraphQL and TypeScript/JavaScript (Node.js) - GraphQL is the Datastore's primary interface, and this profile owns significant parts of it
- Designing event-driven pipelines end to end: producers, consumers, replay, idempotency, and what happens when a consumer falls behind
- Leading the design of complex systems rather than individual components, across the API, the pipelines, and the services that depend on them

For the PostgreSQL & Data Modeling role:

- You can be the person the rest of the team comes to about the database.
- Deep PostgreSQL: you reason fluently about the query planner, index selection, and EXPLAIN (ANALYZE), and why a query that should be fast isn't
- Data modeling: you design the schema itself: entities, relationships, and the constraints that make invalid states impossible. Including how to model time, since clinical results get re-scored and corrected and we need to answer "what did this look like when the report was signed?"
- Schema evolution under load: zero-downtime migrations, dual-write transitions, lock avoidance, backfill and verification. Our schema has hundreds of migrations behind it and will have hundreds more
- Operating PostgreSQL in production, not only designing for it: upgrades, replication, backup and restore, connection pooling, bloat and vacuum behaviour, extensions
- Making others good at it: you teach, review, and document, because a schema only stays coherent if the team understands it

We don't expect every candidate to check every box. If you bring strong fundamentals, care about data infrastructure for health, and are excited to learn, we’d love to hear from you!

The US-based salary range for this role is $170,000 – $190,000. Salary ranges are determined using current market compensation data for this role and adjusted based on experience, skills, and location. The base salary is one component of the total compensation package, which includes equity, PTO and other benefits.

At Beacon, we've found that cultural and scientific impact is driven most by those that lead by example. As such, we're always seeking new contributors whose work demonstrates an avid curiosity, a bias towards simplicity, an eye for composability, a self-service mindset, and - most of all - a deep empathy towards colleagues, stakeholders, users, and patients. We believe a diverse team builds more robust systems and achieves higher impact.
```

---
# Job Questions

```
In a few sentences, provide some specific detailed examples of your work in the area of emphasis you selected in the previous question (Datastore Systems or Postgres and Data Modeling). Please include the name of the employer you did the work for.*
```