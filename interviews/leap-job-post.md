

## About Leap

Leap builds the software home improvement contractors run their business on: CRM, sales and estimating, project execution, payments, and financing. **Leap Pay and Leap Lend** are the payments and lending services inside that suite today, and contractors run real financing volume through them every day. We are rebuilding them as **a standalone, API-first fintech platform** that runs on its own for contractors and partners and embeds inside Leap’s products. It unifies more than a dozen home improvement lenders behind one application experience: multi-lender waterfall routing, predictive lender matching, stipulation handling, funding disbursement, and the regulatory compliance that goes with all of it.

## About the Role

You lead the FinTech engineering team, and you stay in the code. The team is a pod: a product manager who owns what we build, and you, the lead, who owns how it gets built and who distributes the work. Today that is five to six engineers on the lending and payment services running in production, plus a partner engineering team building the new platform, whose technical direction you set and whose work you review.

Leap is an AI-native company, and this codebase is built for it. We do not permit AI-assisted development, we build around it: an agent-oriented skills architecture, MCP tooling, spec-driven work, and agents running in parallel are how the team ships every day. This role carries a high bar for how you personally build with AI, and a second bar for how you bring a team to that way of working. We want an engineer who hands whole features to autonomous agents, runs several at once, reviews and directs their output rather than hand-typing most of the code, and builds the skills, tools, and guardrails that make agents effective. Engineers who use AI for autocomplete or the occasional prompt are not who we are looking for, and if this is not already how you work, this is not the right role.

The role is deliberately sequenced. You start inside the services contractors use today: the lender integrations, the credit application flow, the Leap Pay path, and the data model under both. You ship improvements there, write down how it actually works, and teach it back to the rest of engineering. In parallel, you review and contribute to the new platform as it stands up. As you ramp, ownership of the new build transfers to you, from contributor, to owner of the major domains (lender integration and orchestration, application submission and waterfall, onboarding and compliance capture), to accountable owner of the platform. **Legacy and new will run side by side for a year or more, and you own the seam between them: the contracts, the migration path, what retires, and what runs in parallel.**

You sit inside Leap Engineering. Our SDLC, release process, code review, alerting and on-call, and delivery review apply to FinTech the same way they apply to every team. The Head of FinTech is your daily product and business partner: lender relationships, compliance obligations, and the commercial commitments the build is made against. You bring that context into engineering and carry engineering decisions back.

## What You Will Do

- **Lead the FinTech engineering team**: planning, technical design review, code review standards, mentorship, and interviewing as the team grows
- Write production code in critical-path systems; roughly **70% of your time is hands-on**
- Ship with agents, not around them: **delegate whole features to autonomous agents, run several in parallel**, and own the spec, the review, and the bar for everything they produce
- Bring the FinTech team and the partner team to the same way of working: the skills architecture, MCP tools, specs, and guardrails that let agents ship safely, and the standard for where to trust them and where a human stays in the loop
- Codify context and patterns so both engineers and agents move faster, and keep raising the ceiling of what can be delegated
- Build a working command of the lending and payment services in Leap SalesPro and Leap CRM, improve them, and document them so the knowledge does not live in one person
- **Set technical direction for the partner team**’s work on the new platform and hold the bar through standards, review, and early escalation rather than org-chart authority
- Own major domains of the new platform end to end: data model, API surface, service boundaries, and production operation
- Own the integration seam between the new platform and Leap’s products: API contracts, event boundaries, the migration path off legacy implementations, and consolidation of duplicated payment code into shared services
- Handle money and sensitive data with rigor: integer-cents arithmetic, idempotency, reconciliation, immutable audit trails, KYC and KYB, and PII
- **Keep Eastern hours**; the engineers you lead are in India and daily overlap is part of the job

## The Work

**Today’s systems.** Lending and payment services embedded in Leap SalesPro and Leap CRM, built over years with varying documentation. Lender integrations that are partial and being rebuilt against a canonical contract. Payment functionality that exists in more than one implementation and needs consolidating.

**The new platform.** Multi-lender waterfall routing with async dispatch, retries, and webhook ingestion. Application, lender-application, and funding state machines across long-running processes. Consumer disclosure delivery and cryptographic consent capture with a seven-year audit trail. PayFac integration: sub-merchant provisioning, split settlement, milestone and stage funding. File-based reconciliation with lender partners. Multi-tenant role-based access across standalone and embedded modes.

**Stack.** TypeScript across the stack: Node on the backend, React on the frontend. PostgreSQL. Event-driven flows (queues, webhooks, scheduled jobs) with first-class observability in New Relic. Containerized on AWS. Spec-driven, component-driven, and built for agents as much as for people.

## What We Are Looking For

**Required**

- 8+ years of professional software engineering experience, with at least 3 at senior or above
- You have led engineers while still shipping: design review, sprint planning, code review, honest feedback, and production code in the same week
- Full-stack depth in TypeScript: deep on Node and PostgreSQL or on React, and competent in both
- You have built systems that integrate third-party financial APIs with complex asynchronous flows: applications, decisioning, webhooks, stipulations, e-signature, and disbursement
- You have learned an unfamiliar, under-documented codebase fast and explained it back to others; this is the first thing you will do here
- You have owned production systems end to end: on-call, post-mortems, and the trade-offs you can defend
- You have been accountable for work you do not line-manage: partner teams, contractors, or other squads
- You are comfortable in regulated environments: you understand why audit trails, retention rules, and versioned records matter, and you do not cut corners on them
- AI is central to how you ship, and you already work at a high level of autonomy with it: you hand whole tasks to agents, run several at once (parallel sessions and worktrees, not one branch at a time), and build the tooling that makes them effective. This is a hard requirement, and we will ask you to show us how you work, live
- Authorized to work in the US and able to keep Eastern time zone hours

**Preferred**

- Consumer lending, loan origination, point-of-sale financing, or fintech marketplace experience
- Payment facilitator or merchant provisioning experience: Stripe Connect, Justifi, Finix, or similar
- Legacy modernization: you have run old and new in parallel or executed a strangler-fig migration without breaking the business on the old path
- Internal technical lead alongside an outsourced or partner engineering team
- Compliance frameworks such as TILA and Reg Z, ECOA and Reg B, FCRA, and E-Sign, from direct fintech work or from working with counsel
- You have built the tooling side of agentic development: skills, MCP servers, evals, or guardrails that other engineers and agents now rely on
- Home services or contractor-facing SaaS

## What Success Looks Like

- **Early:** you can whiteboard how a credit application moves through today’s implementation, including where it breaks, and someone else on the team can too, because you wrote it down
- **Building:** your domains in the new platform ship on schedule with a test and observability story you would defend, and design review is a real forum, not a formality
- **Taking over:** the handoff of platform ownership is a non-event, because you have already been the person answering the hard questions about it
- **Integrating:** a new fintech service can be consumed by Leap SalesPro or Leap CRM without an archaeology exercise first
- **Throughout:** the engineers on the team are visibly better than when they joined, the partner team ships to a bar you set, and FinTech knowledge is not concentrated in one person
- **Throughout:** the FinTech team and the partner team ship the way Leap Crew ships: agents doing the bulk of the typing, people owning the spec, the review, and the bar

## What This Role Is Not

- **Not greenfield.** The blueprints exist and the build is moving. Ownership transfers to you as you ramp, and accountability tracks that handoff, not your start date.
- **Not day-one work on the new app.** You start in the services running today, deliberately. If that reads as a detour rather than the foundation, we are probably not the right fit for each other.
- **Not a hands-off management role, and not a pure IC role that stays IC.** You will be in the code, and as the team grows, you lead engineers.
- **Not a place where AI is optional.** If most of your code is still hand-typed, this will feel foreign, and we will see it in the exercise.
- **Not a LeetCode interview.** We run practical exercises drawn from the actual work: reading a spec, extending a schema, tracing a bug through an async waterfall.

Compensation will be determined based on experience, skills, and qualifications.

Pay Range

$180,000—$200,000 USD

**Benefits**

We believe in supporting our employees holistically - your health, financial well-being, time to recharge, and overall happiness matter to us. Here’s what you can look forward to:

- **Affordable Health & Wellness Coverage** – comprehensive and competitive benefits package, starting the first of the month following your hire date.
- **Invest in Your Future** – 401(k) company match to help you build financial security.
- **Time to Recharge** – We believe time to rest and recharge matters. Leap offers a Flexible Time Off (FTO) policy, 10 paid sick days, and 8 paid company holidays.
- **Comprehensive Employee Assistance Program (EAP)** – resources to support your mental health, financial well-being, and everyday challenges.
- **Exclusive Discounts with LifeMart (via ADP)** – save on groceries, restaurants, entertainment, pet insurance, cell phones, child care, and more!
- **MoveSpring Wellness App** – stay active and engaged with company step challenges, workout content, meditation tools, and wellness blogs for a healthier you!
- **Culture & Team-Building Activities** – we love to connect, celebrate, and grow together through team events, fun challenges, and company traditions like our Annual Summit!

Join us and experience a company that truly invests in **YOU**!

Leap is an Equal Employment Opportunity and Affirmative Action Employer. We are committed to providing an environment of mutual respect where equal employment opportunities are available to all applicants and teammates without regard to race, religion, color, sex, gender identity, sexual orientation, age, non-disqualifying physical or mental disability, national origin, veteran status or any other basis covered by appropriate law. All employment decisions are made based on qualifications, merit, and business needs.

Leap, LLC collects personal information from job applicants as part of our recruiting and hiring process. This information is collected directly from you and from third parties such as background check providers and professional references. It is shared only with Greenhouse Software Inc. (our recruiting platform) and others as required by law. We do not sell your personal information. 

The categories of information we collect, and the purposes for which we use them, include: 

- **Identifiers** (name, email, phone, address) — to contact you and manage your application 

- **Professional** **information** (resume, work history, skills, references) — to evaluate your qualifications 

- **Education** **information** (degrees, certifications) — to verify credentials required for the role 

- **Background** **check** **data** (criminal history, employment verification) — to complete pre-employment screening as permitted by law 

- **Voluntary** **demographic** **information** (EEO data) — for legally required reporting only; not used in hiring decisions