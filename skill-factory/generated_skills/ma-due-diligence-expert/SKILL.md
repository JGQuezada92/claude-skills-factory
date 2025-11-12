---
name: ma-due-diligence-expert
description: This skill should be used when conducting comprehensive M&A due diligence on technology sector acquisitions ranging from $10M to $500M+. Use for financial analysis (Quality of Earnings, working capital), commercial assessment (customer analysis, unit economics), technology evaluation (tech stack, IP, scalability), operational review (management, org structure), legal/regulatory compliance, risk assessment, synergy quantification, and integration planning. Creates Investment Committee memos, financial models, valuations, and integration plans using methodologies from Goldman Sachs, JP Morgan, and Morgan Stanley.
license: MIT License - Copyright (c) 2025
---

# M&A Due Diligence Expert

## Overview

This skill provides comprehensive M&A due diligence capabilities for technology sector acquisitions, synthesizing elite methodologies from Goldman Sachs (hypothesis-driven approach with red flag matrices), JP Morgan (deal scorecard with weighted criteria), and Morgan Stanley (functional workstream approach). The skill handles all aspects of institutional-quality due diligence from strategic assessment through integration planning, with adaptive frameworks for deals ranging from $10M bolt-on acquisitions to $500M+ transformational transactions.

The skill delivers Investment Committee-ready analysis including detailed IC memos (25-40 pages), financial models with scenario analysis, risk-adjusted valuations using multiple methodologies (DCF, comparable companies, precedent transactions), synergy quantification with confidence levels, and comprehensive integration roadmaps with Day 1 priorities and 100-day plans.

## When to Use This Skill

Use this skill when:
- Conducting due diligence on technology company acquisitions (SaaS, enterprise software, cloud infrastructure, vertical software)
- Analyzing financial statements to identify quality of earnings issues, working capital requirements, or revenue quality concerns
- Reviewing data rooms to identify deal-breakers, risks, and mitigation strategies
- Assessing technology stacks for technical debt, scalability issues, and modernization requirements
- Evaluating customer concentration risk, retention rates, and unit economics
- Creating Investment Committee memos with strategic rationale, risk assessment, and valuation analysis
- Building financial models with normalized adjustments, scenario analysis, and synergy quantification
- Developing integration plans with Day 1 readiness, 100-day milestones, and retention strategies
- Quantifying revenue and cost synergies with confidence levels and realization timelines
- Performing valuation analysis using DCF, comparable companies, and precedent transactions
- Assessing management teams and identifying key person risks

## How to Use This Skill

### Step 1: Understand Deal Context and Scope

Begin by clarifying the deal parameters and diligence scope:

- **Deal size and structure:** Determine deal value ($10M, $50-250M, $250M+), structure (asset vs. stock), and payment terms (cash, stock, earnouts)
- **Strategic rationale:** Understand acquirer's investment thesis and strategic fit
- **Timeline:** Confirm diligence timeline (2-4 weeks for small deals, 4-6 weeks for mid-market, 6-12 weeks for large deals)
- **Workstream focus:** Identify priority workstreams based on deal size and key risks (all workstreams for large deals, focused approach for small deals)
- **Available information:** Catalog data room contents, management presentations, and available documents

Adapt the diligence framework based on deal size:
- **Small deals ($10-50M):** Streamlined 2-4 week approach focusing on strategic fit, revenue quality, and key person risk
- **Mid-market ($50-250M):** Comprehensive 4-6 week multi-workstream diligence covering all functional areas
- **Large deals ($250M+):** Extended 6-12 week deep-dive with specialist teams per workstream

### Step 2: Conduct Strategic Assessment (Phase 1 - Week 1)

Execute strategic fit analysis to determine go/no-go decision:

**Investment Thesis Validation:**
- Articulate and validate the strategic rationale for the acquisition
- Assess alignment with acquirer's corporate strategy and portfolio
- Evaluate alternative scenarios and walk-away analysis
- Determine if deal creates unique value vs. alternatives

**Market Opportunity Sizing:**
- Calculate TAM/SAM/SOM using bottom-up and top-down methodologies
- Analyze market growth rates, trends, and penetration opportunities
- Assess competitive dynamics using Porter's Five Forces
- Evaluate barriers to entry and sustainable competitive advantages

**Competitive Positioning:**
- Map competitive landscape and strategic group positioning
- Analyze market share trends and win/loss data
- Assess product differentiation and competitive moats
- Evaluate pricing power and competitive vulnerabilities

**Deal Structure Evaluation:**
- Analyze asset vs. stock purchase implications
- Evaluate earnout structures and reps & warranties provisions
- Assess change of control provisions in material contracts
- Calculate accretion/dilution for public company acquirers

### Step 3: Execute Financial Due Diligence (Phase 2 - Weeks 2-4)

Conduct comprehensive financial analysis using `scripts/financial_analysis.py` and `scripts/qoe_analyzer.py`:

**Quality of Earnings Analysis:**
- Normalize EBITDA for one-time items, non-recurring expenses, stock-based compensation, and related party transactions
- Reconcile bookings vs. billings vs. revenue for SaaS companies
- Analyze deferred revenue and contract liability trends
- Assess revenue recognition policies and practices
- Identify historical performance vs. management projections variance
- Document all normalization adjustments with clear rationale

**Working Capital Analysis:**
- Calculate historical working capital as % of revenue
- Determine normalized working capital peg for purchase agreement
- Analyze DSO, DIO, DPO trends and working capital cycle
- Estimate Day 1 working capital funding requirements
- Identify seasonal working capital fluctuations

**Revenue Quality Assessment:**
- Analyze customer concentration (flag if top 10 customers >30% of revenue)
- Assess revenue sustainability and growth drivers
- Evaluate pricing power through price realization analysis
- Analyze revenue mix (new vs. expansion, geographies, segments)
- Review contract terms, auto-renewal rates, and pricing escalations

**SaaS Metrics Analysis (for software targets):**
- Calculate ARR/MRR with historical trends
- Analyze Net Revenue Retention (NRR) and Gross Retention (GRR) by cohort
- Calculate Rule of 40 (growth rate + profit margin)
- Evaluate magic number (ARR growth / S&M spend)
- Assess CAC, LTV, LTV/CAC ratio (benchmark: 3:1), and payback period (benchmark: 12-18 months)
- Analyze cohort economics and retention curves

**Cash Flow and Debt Analysis:**
- Build free cash flow bridge from EBITDA
- Analyze cash conversion cycle and cash generation capability
- Review debt structure, covenants, and refinancing requirements
- Assess off-balance sheet liabilities and contingent obligations

Use `scripts/financial_analysis.py` to automate calculations and generate financial schedules with validation.

### Step 4: Perform Commercial Due Diligence (Phase 2 - Weeks 2-4)

Analyze commercial aspects using `scripts/customer_analyzer.py`:

**Customer Analysis:**
- Review top 20-50 customer contracts for terms, renewal dates, and pricing
- Calculate customer concentration risk (red flag if >30% from top 10)
- Analyze customer retention rates and churn by cohort
- Conduct customer reference calls using scoring rubrics
- Assess customer satisfaction metrics (NPS, CSAT scores)
- Evaluate customer dependencies and switching costs

**Unit Economics:**
- Calculate customer lifetime value (LTV) by segment and cohort
- Analyze customer acquisition cost (CAC) by channel
- Evaluate LTV/CAC ratio (target: 3:1 minimum)
- Calculate CAC payback period (target: 12-18 months)
- Assess cohort profitability and contribution margins

**Go-to-Market Effectiveness:**
- Analyze sales productivity (quota attainment, win rates, sales cycle length)
- Evaluate pipeline coverage ratios (healthy: 3-4x coverage)
- Assess lead conversion metrics through the funnel
- Review sales compensation structure and incentive alignment
- Evaluate channel strategy and partner ecosystem

**Market Position:**
- Analyze competitive win/loss trends and battle card effectiveness
- Evaluate market share and share of wallet with customers
- Assess brand strength and market perception
- Review analyst coverage and market positioning (Gartner MQ, etc.)

### Step 5: Conduct Technology & Product Due Diligence (Phase 2 - Weeks 2-4)

Evaluate technology aspects using `scripts/tech_stack_analyzer.py`:

**Technology Stack Assessment:**
- Document architecture (cloud infrastructure, languages, frameworks)
- Assess technology choices and architectural patterns
- Evaluate API architecture and integration capabilities
- Review mobile and multi-platform support
- Analyze data architecture and database performance

**Technical Debt Evaluation:**
- Assess code quality, test coverage, and documentation
- Identify technical debt and modernization requirements
- Estimate cost and timeline for technical debt remediation
- Evaluate development practices and CI/CD maturity
- Review infrastructure scalability and performance bottlenecks

**Intellectual Property Analysis:**
- Review patent portfolio, trademarks, and copyrights
- Assess IP ownership and freedom-to-operate
- Review open source license compliance
- Evaluate trade secrets and proprietary technology
- Identify IP risks and potential infringement issues

**Cybersecurity Assessment:**
- Review SOC 2, ISO 27001, and other security certifications
- Analyze penetration testing results and vulnerability assessments
- Evaluate data privacy compliance (GDPR, CCPA)
- Assess incident response capabilities and history
- Review third-party security audits

**Product Roadmap Review:**
- Evaluate product strategy and roadmap prioritization
- Assess R&D productivity and development velocity
- Analyze product-market fit and customer validation
- Review feature requests and competitive gaps
- Evaluate development team quality and retention

### Step 6: Execute Operational Due Diligence (Phase 2 - Weeks 2-4)

Assess operational aspects:

**Organizational Structure:**
- Review org charts and span of control
- Analyze headcount trends and growth trajectory
- Evaluate organizational efficiency (revenue per employee)
- Assess reporting structures and decision-making processes
- Identify organizational gaps and redundancies

**Management Team Assessment:**
- Evaluate executive team experience, track record, and cultural fit
- Identify key person dependencies and retention risks
- Assess management depth and succession planning
- Conduct reference checks on key executives
- Evaluate compensation and equity structures

**Operational Efficiency:**
- Benchmark G&A ratios against comparables
- Analyze operational leverage and scalability
- Review systems and process maturity
- Evaluate vendor relationships and dependencies
- Assess real estate and facility requirements

### Step 7: Perform Legal & Regulatory Due Diligence (Phase 2 - Weeks 2-4)

Review legal aspects using `scripts/contract_analyzer.py`:

**Material Contracts Review:**
- Analyze top customer contracts (terms, auto-renewal rates, termination rights)
- Review supplier and vendor agreements
- Evaluate partnership and reseller agreements
- Identify change of control provisions
- Assess unusual or concerning contract terms

**Employment and Compensation:**
- Review executive employment agreements
- Analyze severance and change of control provisions
- Evaluate equity plans and option grants
- Assess employee retention risks
- Review non-compete and IP assignment agreements

**Litigation and Compliance:**
- Review litigation history and ongoing disputes
- Assess regulatory compliance (industry-specific, data privacy)
- Evaluate export control and trade compliance
- Review insurance coverage and claims history
- Identify potential regulatory approval risks

### Step 8: Develop Risk Assessment (Phase 2-3 - Weeks 3-5)

Create comprehensive risk register using `scripts/risk_analyzer.py`:

**Risk Identification and Scoring:**
- Identify all material risks across functional workstreams
- Score each risk using probability (1-5) x impact (1-5) methodology
- Categorize risks as strategic, financial, operational, or legal
- Flag deal-breakers vs. manageable risks
- Develop mitigation strategies for each identified risk

**Red Flag Matrix:**
- Create high/medium/low severity classification
- Prioritize top 10 risks requiring immediate attention
- Identify risks requiring additional diligence
- Assess residual risk after mitigation
- Document risk tolerance and acceptance criteria

**Deal-Breaker Assessment:**
- Evaluate if any issues constitute deal-breakers
- Assess if risks can be mitigated through price adjustment, earnouts, or indemnities
- Consider walk-away scenarios if deal-breakers identified
- Document reasoning for proceed/pass recommendation

### Step 9: Quantify Synergies (Phase 3 - Weeks 4-6)

Analyze value creation opportunities using `scripts/synergy_analyzer.py`:

**Revenue Synergies:**
- Cross-sell opportunities with existing customer base
- Geographic expansion and channel leverage
- Product bundling and upsell opportunities
- Pricing optimization and premiumization
- Accelerated product development and time-to-market

**Cost Synergies:**
- Headcount reduction and organizational efficiencies
- Vendor consolidation and purchasing power
- Facility consolidation and real estate optimization
- Technology and systems consolidation
- G&A overhead reduction

**Synergy Quantification:**
- Estimate annual synergy value by category
- Assign confidence levels (high/medium/low)
- Develop realization timeline (Year 1/2/3)
- Estimate one-time implementation costs
- Calculate net present value of synergies

**Dis-synergies:**
- Identify potential customer or revenue loss
- Estimate employee retention costs
- Calculate stranded costs and transition services
- Assess integration disruption impact

### Step 10: Conduct Valuation Analysis (Phase 3 - Weeks 4-6)

Perform multi-method valuation using `scripts/valuation_models.py`:

**DCF Valuation:**
- Build 5-10 year DCF model with explicit period projections
- Calculate WACC using capital structure and market data
- Estimate terminal value using perpetuity growth or exit multiple
- Perform sensitivity analysis on key assumptions (revenue growth, margins, WACC, terminal growth)
- Calculate standalone value range

**Comparable Company Analysis:**
- Identify 5-10 publicly traded comparable companies
- Calculate trading multiples (EV/Revenue, EV/EBITDA, P/E)
- Adjust for differences in growth, margins, and scale
- Apply multiple ranges to target financials
- Benchmark target metrics against comps

**Precedent Transaction Analysis:**
- Identify 5-10 relevant M&A transactions in sector
- Calculate transaction multiples with premiums
- Assess synergy assumptions in precedent deals
- Adjust for market conditions and strategic rationale
- Apply multiple ranges to target

**Valuation Synthesis:**
- Triangulate valuation range across methodologies
- Weight methodologies based on applicability and reliability
- Calculate standalone value and value with synergies
- Develop base/upside/downside scenario valuations
- Document key valuation assumptions and sensitivities

For public company acquirers, calculate accretion/dilution analysis.
For PE buyers, calculate IRR and MOIC returns analysis.

### Step 11: Develop Integration Plan (Phase 3 - Weeks 4-6)

Create detailed integration roadmap using `scripts/integration_planner.py`:

**Day 1 Readiness:**
- Define Day 1 priorities and critical path activities
- Establish integration governance and decision rights
- Plan legal entity structure and regulatory notifications
- Prepare employee and customer communications
- Set up integration management office (IMO)

**100-Day Integration Plan:**
- Define integration milestones and deliverables by week
- Assign owners and accountability for each workstream
- Identify quick wins for early momentum
- Plan systems integration approach (ERP, CRM, HR)
- Establish integration metrics and tracking

**Key Employee Retention:**
- Identify critical employees across technical, sales, and product functions
- Design retention packages (typically 1.5-2x annual compensation)
- Plan communication and offer timing
- Develop career pathing and integration into parent company
- Monitor retention risk indicators

**Customer Retention Strategy:**
- Develop customer communication plan and timing
- Assign relationship owners for top customers
- Plan product roadmap communication
- Address customer concerns proactively
- Establish customer success metrics

**Cultural Integration:**
- Assess cultural compatibility and differences
- Develop change management plan
- Plan cultural workshops and team building
- Address cultural integration risks
- Monitor cultural integration progress

**Synergy Realization:**
- Build detailed implementation plans for each synergy
- Assign owners and timelines for synergy capture
- Establish tracking metrics and reporting
- Plan communication of synergy progress
- Adjust plans based on execution learnings

### Step 12: Prepare Investment Committee Materials (Phase 4 - Week 6)

Create comprehensive IC package:

**Executive Summary (2-3 pages):**
- Clear investment recommendation (proceed/pass/additional diligence)
- Deal rationale and strategic fit in 3-5 bullets
- Valuation summary with range and methodology
- Top 5 risks with mitigation strategies
- Synergy overview with confidence levels
- Key deal terms and structure

**Full IC Memo (25-40 pages):**
- Strategic assessment (market opportunity, competitive position, strategic fit)
- Financial analysis (QoE findings, normalized metrics, historical performance, SaaS metrics)
- Commercial diligence (customer analysis, unit economics, go-to-market assessment)
- Technology assessment (tech stack, IP, scalability, technical debt)
- Operational review (management team, org structure, key person risks)
- Legal and regulatory findings
- Comprehensive risk register with mitigation strategies
- Synergy analysis with confidence levels and realization timeline
- Valuation summary using multiple methodologies
- Integration plan overview
- Detailed appendices (financial schedules, customer lists, org charts, contract summaries)

**PowerPoint Presentation (15-20 slides):**
Use `scripts/powerpoint_generator.py` to create professional IC deck with:
- Investment thesis and strategic rationale
- Market opportunity and competitive landscape
- Financial highlights and QoE summary
- Customer and commercial analysis
- Technology and product assessment
- Risk matrix with top risks highlighted
- Valuation bridge (standalone to synergy value)
- Synergy waterfall with realization timeline
- Integration roadmap with Day 1 and 100-day priorities
- Investment recommendation with key decision points

**Financial Model (Excel):**
Use `scripts/excel_model_builder.py` to create:
- Integrated 3-statement model (P&L, balance sheet, cash flow)
- Historical financials with normalization adjustments
- Projections with base/upside/downside scenarios
- Synergy models by category and year
- Working capital schedule
- DCF valuation with sensitivity analysis
- Comparable company analysis
- Precedent transaction analysis
- Accretion/dilution or IRR/MOIC analysis
- Audit trails and assumption documentation

### Step 13: Validate All Outputs Before Delivery

**CRITICAL: Before finalizing IC materials, validate all analysis:**

**Financial Validation:**
- Recalculate all normalized EBITDA adjustments manually
- Verify working capital calculations and peg formula
- Cross-check all SaaS metrics (ARR, NRR, GRR, CAC, LTV)
- Validate DCF model formulas and calculations
- Verify comparable company multiples and adjustments
- Check that all scenarios are internally consistent

**Analytical Validation:**
- Verify customer concentration calculations
- Recalculate unit economics (LTV, CAC, payback)
- Validate synergy quantification and timing
- Check risk scoring methodology consistency
- Verify valuation triangulation across methodologies

**Document Validation:**
- Ensure executive summary numbers match detailed analysis
- Verify all charts and tables have accurate data
- Check that PowerPoint matches memo findings
- Validate Excel model references and formulas
- Confirm appendices support main findings

**Quality Checks:**
- Verify all assumptions are documented
- Confirm data sources are cited
- Check that risks have mitigation strategies
- Ensure recommendations are supported by analysis
- Validate that deal-breakers are clearly flagged

Run `scripts/validation_checks.py` to perform automated validation of calculations and consistency checks.

Document validation results including any errors found and corrections made.

## Important Considerations

- **Deal-size adaptive approach:** Scale diligence depth and resource allocation to deal size ($10M requires focused approach, $250M+ requires comprehensive multi-workstream analysis)
- **Data gaps:** Clearly flag missing information, assumptions made, and areas requiring additional diligence or post-close follow-up
- **Deal-breaker identification:** Identify potential deal-breakers early (Phase 1-2) to enable timely decision-making on proceed/pass
- **Risk prioritization:** Focus on material risks with high probability and high impact; use probability x impact scoring methodology
- **Synergy realism:** Apply appropriate confidence levels to synergies (high/medium/low); be conservative on timing and realization
- **Integration complexity:** Assess integration complexity upfront and factor into valuation and decision-making
- **Customer concentration:** Flag as high risk if top 10 customers represent >30% of revenue
- **Key person risk:** Identify critical employees and develop retention strategies as part of integration planning
- **Scenario analysis:** Always provide base/upside/downside scenarios for key metrics and valuation
- **Benchmarking:** Use comparable companies and industry benchmarks to validate assumptions and identify outliers
- **Documentation:** Maintain clear audit trails for all assumptions, calculations, and conclusions
- **Balanced perspective:** Present both opportunities (synergies, growth) and risks objectively
- **Investment Committee quality:** Ensure all deliverables are board-quality with executive summaries and supporting details

## Resources

This skill includes the following resources:

**Python Scripts:**
- `scripts/financial_analysis.py` - Quality of Earnings analysis, working capital calculations, EBITDA normalization, SaaS metrics
- `scripts/qoe_analyzer.py` - Specialized Quality of Earnings normalization engine
- `scripts/customer_analyzer.py` - Customer concentration analysis, cohort retention, unit economics calculations
- `scripts/tech_stack_analyzer.py` - Technology assessment framework and technical debt scoring
- `scripts/contract_analyzer.py` - Contract review automation and terms extraction
- `scripts/risk_analyzer.py` - Risk scoring, probability x impact matrices, risk register generation
- `scripts/synergy_analyzer.py` - Synergy quantification models with confidence levels and timing
- `scripts/valuation_models.py` - DCF, comparable company, and precedent transaction analysis
- `scripts/integration_planner.py` - 100-day plan generation, retention analysis, synergy tracking
- `scripts/powerpoint_generator.py` - Investment Committee presentation generation
- `scripts/excel_model_builder.py` - Integrated financial model creation
- `scripts/validation_checks.py` - Automated validation of calculations and consistency

**Reference Documents:**
- `references/ma_frameworks.md` - Goldman Sachs, JP Morgan, and Morgan Stanley due diligence methodologies
- `references/saas_metrics.md` - Comprehensive guide to SaaS metrics and benchmarks
- `references/valuation_methods.md` - DCF, comps, and precedent transactions detailed methodology
- `references/integration_playbook.md` - Best practices for post-merger integration
- `references/risk_frameworks.md` - Risk assessment and mitigation strategy frameworks

## Keywords

M&A, due diligence, technology acquisition, SaaS, enterprise software, Quality of Earnings, QoE, working capital, financial analysis, valuation, DCF, comparable companies, precedent transactions, customer analysis, unit economics, LTV, CAC, tech stack, technical debt, IP analysis, risk assessment, synergy analysis, integration planning, Investment Committee, IC memo, deal structuring, Goldman Sachs, JP Morgan, Morgan Stanley, buy-side diligence, sell-side diligence, data room analysis, management assessment, commercial diligence, technology diligence, operational diligence, legal diligence

