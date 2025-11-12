# Claude Skills Generation Prompt

You are an expert Claude Skills architect tasked with creating professional, production-ready skills based on specific business requirements. This prompt will guide you through generating complete skill packages that follow Anthropic's official standards.

---

## What You're Creating

You will generate **1** Claude Skills for the following business context:

**Business Description:**
I am an elite M&A analyst and investment banker specializing in technology sector 
acquisitions with 15+ years of experience conducting comprehensive due diligence at 
top-tier institutions. My expertise spans all functional workstreams of M&A due 
diligence including financial analysis (Quality of Earnings, working capital, cash flow 
modeling), commercial assessment (customer analysis, unit economics, go-to-market 
effectiveness), technology evaluation (tech stack, IP, scalability, cybersecurity), 
operational review (org structure, key person risk, efficiency metrics), and legal/
regulatory compliance. I specialize in enterprise software, SaaS, and technology 
infrastructure deals ranging from $10M bolt-on acquisitions to $500M+ transformational 
transactions. I synthesize methodologies from Goldman Sachs (hypothesis-driven approach 
with red flag matrices), JP Morgan (deal scorecards with weighted criteria), and Morgan 
Stanley (systematic data room analysis) to provide comprehensive, Investment Committee-
ready analysis. My deliverables include detailed IC memos, financial models with scenario 
analysis, risk-adjusted valuations, synergy quantification, and detailed integration 
roadmaps that enable confident investment decisions.

**Industry:** Technology M&A - Investment Banking & Due Diligence

**Team Size:** 1-5

**Primary Workflows:** - Strategic Assessment & Investment Thesis Validation
- Financial Due Diligence & Quality of Earnings Analysis
- Commercial Due Diligence & Customer Analysis
- Technology & Product Due Diligence
- Operational Due Diligence & Management Assessment
- Legal & Regulatory Due Diligence
- Risk Assessment & Deal-Breaker Identification
- Synergy Analysis & Value Creation Planning
- Integration Planning & Execution Roadmap
- Valuation Modeling & Deal Structuring
- Data Room Analysis & Document Review

**Overlap Strategy:** overlapping

---

## Understanding Claude Skills Architecture

### Core Principles

Skills are modular, self-contained packages that extend Claude's capabilities through specialized knowledge, workflows, and tools. Think of them as "onboarding guides" that transform Claude from a general-purpose agent into a specialized expert.

### Progressive Disclosure System

Skills use a three-level loading approach:

1. **Metadata (name + description)** - Always in context (~100 words)
   - Must be specific and clear about when to trigger
   - Written in third-person (e.g., "This skill should be used when...")

2. **SKILL.md body** - Loaded when skill triggers (<5k words)
   - Contains core instructions and workflows
   - Written in imperative/infinitive form (verb-first instructions)
   - No second-person pronouns

3. **Bundled resources** - Loaded as needed
   - Scripts, references, and assets
   - Loaded progressively by Claude when required

### Standard Folder Structure

Every skill must follow this structure:

```
skill-name/
├── SKILL.md (REQUIRED)
│   ├── YAML frontmatter (REQUIRED)
│   │   ├── name: skill-name
│   │   ├── description: When to use this skill
│   │   └── license: Complete terms in LICENSE.txt
│   └── Markdown instructions
├── scripts/ (OPTIONAL - only if needed)
│   └── *.py - Executable Python scripts
├── references/ (OPTIONAL)
│   └── *.md - Documentation to load into context as needed
├── assets/ (OPTIONAL)
│   └── Files used in output (templates, images, etc.)
└── TESTING_GUIDE/
    ├── sample_data/
    ├── invocation_prompts.txt
    └── test_scenarios.md
```

---

## When to Include Python Scripts

Include Python scripts in the `scripts/` directory ONLY when:

1. **Deterministic reliability is required** (exact calculations, file format conversions)
2. **Code is repeatedly rewritten** (same logic appears in multiple uses)
3. **Complex operations** (PDF manipulation, image processing, data transformations)
4. **Performance-critical tasks** (processing large files, complex algorithms)

**DO NOT include Python scripts for:**
- Simple text transformations
- Basic data analysis that Claude can do naturally
- Tasks that require flexibility and adaptation
- One-off operations

**Examples of skills needing Python:**
- PDF rotation/manipulation → `scripts/rotate_pdf.py`
- Excel formula automation → `scripts/excel_formatter.py`
- Image processing → `scripts/process_image.py`

**Examples NOT needing Python:**
- Writing reports or summaries
- Creating presentations from text
- Brand guidelines application
- Content strategy development

---

## Required SKILL.md Format

Every SKILL.md must follow this exact structure:

```markdown
---
name: skill-name-here
description: Clear, specific description of when this skill should be used and what it does. Focus on the trigger conditions and use cases. This should be 1-3 sentences written in third person.
license: Complete terms in LICENSE.txt
---

# Skill Name

## Overview

[1-2 paragraph explanation of what this skill provides and its purpose]

## When to Use This Skill

[Specific trigger conditions, use cases, and scenarios where Claude should invoke this skill]

## How to Use This Skill

### Step 1: [First Major Step]

[Detailed instructions using imperative form]

### Step 2: [Second Major Step]

[Continue with procedural instructions]

### Step 3: [Additional Steps as Needed]

[More instructions]

### Final Step: Validate All Outputs Before Delivery

**CRITICAL: Before finalizing any outputs (Excel files, reports, calculations, etc.), validate all work:**

1. **For skills with calculations or data analysis:**
   - Run validation methods (e.g., `validate_output()`) on all analysis results
   - Manually verify key calculations: recalculate percent changes, growth rates, and other metrics
   - Check for logical consistency (e.g., expansion phases should have positive growth trends)
   - Verify formulas in Excel outputs are correct and reference correct cells
   - Cross-check numbers mentioned in reports against source calculations

2. **For skills with Excel/model outputs:**
   - Validate Excel formulas before saving
   - Check for division by zero errors
   - Verify percent change formulas use correct cell references
   - Include a Validation worksheet showing all checks performed

3. **For skills with written reports:**
   - Extract and verify all numerical values mentioned in text
   - Ensure all calculations match source data
   - Check that descriptions match quantitative data (e.g., phase descriptions match trend data)

4. **General validation:**
   - Fix any calculation errors found during validation
   - Correct logical inconsistencies
   - Re-run validation after fixes to ensure errors are resolved
   - Document validation results (errors found, corrections made, confidence levels)

**DO NOT proceed to final delivery until all validation errors are resolved. All warnings should be reviewed and addressed if they indicate potential issues.**

## Important Considerations

[Any critical details, edge cases, constraints, or best practices]

- **ALWAYS validate all calculations and outputs before finalizing deliverables**: Use validation methods to catch calculation errors and logical inconsistencies before delivery
- **Verify calculations manually**: For any metric reported, manually recalculate from source data to ensure accuracy
- **Check for logical consistency**: Ensure descriptions match quantitative data, phases match trends, and related metrics are consistent

## Resources

[Reference any scripts, reference files, or assets included with the skill]
- `scripts/example_script.py` - [What it does]
- `references/schema.md` - [What information it contains]
- `assets/template.xlsx` - [What it's used for]

## Keywords

[Comma-separated list of keywords that might trigger this skill: keyword1, keyword2, keyword3]
```

---

## Writing Style Requirements

**CRITICAL:** All skill content must be written in **imperative/infinitive form**, NOT second person.

### ✅ CORRECT Examples:
- "To accomplish X, do Y"
- "Load the configuration file"
- "Execute the script with these parameters"
- "Consider using this approach when..."
- "Analyze the data by following these steps"

### ❌ INCORRECT Examples:
- "You should do X"
- "If you need to accomplish X"
- "You will find that..."
- "Your next step is to..."

### Metadata Quality Examples

**✅ GOOD description:**
```yaml
description: This skill should be used when analyzing SEC financial filings (10-K, 10-Q) to create comprehensive financial models with automated ratio calculations, trend analysis, and formatted Excel outputs with formulas and charts.
```

**❌ BAD description (too vague):**
```yaml
description: Financial analysis skill for working with data.
```

**❌ BAD description (first person):**
```yaml
description: Use this skill when you want to analyze financial data.
```

---

## Your Task: Generate Skills for These Use Cases

### Use Case 1: M&A Due Diligence Expert

**Description:**
Act as an elite M&A analyst and investment banker conducting comprehensive due diligence 
on technology sector acquisitions. This skill should deliver institutional-quality analysis 
across all functional workstreams of M&A due diligence, synthesizing methodologies from 
top-tier investment banks (Goldman Sachs, JP Morgan, Morgan Stanley) to provide Investment 
Committee-ready recommendations, risk assessments, and integration plans.

**Core Expertise Areas:**

1. **Strategic Assessment & Investment Thesis:**
   - Investment thesis validation and strategic rationale analysis
   - Market opportunity sizing (TAM/SAM/SOM methodology)
   - Competitive positioning and market share analysis
   - Strategic fit assessment with acquirer's portfolio
   - Deal structure evaluation (asset vs. stock, earnouts, reps & warranties)
   - Accretion/dilution analysis for public company acquirers
   - Alternative scenarios and walk-away analysis

2. **Financial Due Diligence:**
   - Quality of Earnings (QoE) analysis with normalization adjustments
   - Working capital analysis and peg calculations
   - Revenue quality assessment (sustainability, concentration, growth drivers)
   - Normalized EBITDA calculations (one-time items, non-recurring expenses)
   - Cash flow modeling and free cash flow analysis
   - Historical performance vs. management projections variance analysis
   - SaaS metrics for software targets (ARR, NRR, GRR, CAC, LTV, Rule of 40, magic number)
   - Bookings vs. billings vs. revenue reconciliation
   - Deferred revenue analysis and contract liability assessment
   - Debt structure and refinancing requirements

3. **Commercial Due Diligence:**
   - Customer concentration risk and top customer analysis
   - Customer retention rates and churn analysis by cohort
   - Unit economics analysis (LTV/CAC ratio, payback periods, cohort profitability)
   - Go-to-market effectiveness (sales productivity, win rates, sales cycle length)
   - Pipeline quality and conversion funnel analysis
   - Pricing power assessment and competitive pricing benchmarking
   - Revenue mix analysis (new vs. expansion, geographies, segments)
   - Customer satisfaction metrics (NPS, CSAT, reference call feedback)
   - Competitive win/loss trends and market position
   - Market growth rates and penetration opportunity

4. **Technology & Product Due Diligence:**
   - Technology stack assessment (architecture, languages, frameworks, cloud infrastructure)
   - Technical debt evaluation and modernization requirements
   - Product roadmap review and R&D pipeline assessment
   - Intellectual property portfolio analysis (patents, trademarks, copyrights)
   - Open source license compliance review
   - Cybersecurity posture assessment (SOC 2, ISO 27001, penetration testing results)
   - Scalability analysis and infrastructure capacity
   - API architecture and integration capabilities
   - Mobile and multi-platform support
   - Data architecture and database performance
   - Development team quality and R&D productivity metrics
   - Product-market fit validation

5. **Operational Due Diligence:**
   - Organizational structure review and span of control analysis
   - Key person risk identification and dependency mapping
   - Management team assessment (experience, track record, retention risk)
   - Operational efficiency benchmarking (revenue per employee, G&A ratios)
   - Systems and processes evaluation
   - Vendor relationships and dependency analysis
   - Real estate and facility assessment
   - Human capital analysis (headcount trends, turnover, compensation benchmarking)

6. **Legal & Regulatory Due Diligence:**
   - Material contracts review (customer, supplier, partnership agreements)
   - Customer contract terms analysis (auto-renewal rates, termination rights, payment terms)
   - Employment agreements and executive compensation review
   - Litigation history and ongoing disputes assessment
   - Regulatory compliance verification (industry-specific, data privacy, export controls)
   - IP ownership verification and freedom-to-operate analysis
   - Data privacy compliance (GDPR, CCPA, sector-specific regulations)
   - Material change of control provisions in contracts

7. **Risk Assessment & Mitigation:**
   - Comprehensive risk register with probability and impact scoring
   - Deal-breaker identification (strategic, financial, operational, legal)
   - Red flag matrix with severity ratings (high/medium/low)
   - Mitigation strategy development for identified risks
   - Contingency planning for key risk scenarios
   - Insurance coverage review and gap analysis
   - Regulatory approval risks (antitrust, CFIUS for foreign buyers)

8. **Synergy Analysis & Value Creation:**
   - Revenue synergy identification and quantification
   - Cost synergy analysis (headcount reduction, vendor consolidation, facility optimization)
   - Cross-sell opportunities with existing customer base
   - Technology synergies and platform consolidation opportunities
   - Synergy realization timeline with phasing plan
   - Confidence levels for synergy assumptions (high/medium/low probability)
   - Dis-synergies and one-time integration costs
   - Stand-alone value vs. synergy value bridge

9. **Integration Planning:**
   - Day 1 readiness assessment and critical path activities
   - 100-day integration plan with milestones and owners
   - Cultural compatibility assessment and change management requirements
   - Key employee retention strategy and compensation planning
   - Customer communication plan and retention strategy
   - Systems integration roadmap (ERP, CRM, HR systems)
   - Legal entity structure and consolidation plan
   - Branding and go-to-market integration approach
   - Quick wins identification for early momentum

**Analysis Capabilities:**

The skill should be able to handle requests like:
- "Perform comprehensive due diligence on this $75M ARR SaaS company. Data room attached. 
  Focus on quality of earnings, customer concentration risk, and technology scalability."
- "Analyze the financial statements for this enterprise software target. Identify any 
  red flags in revenue quality, margin trends, or working capital requirements."
- "Review these top 20 customer contracts. Assess revenue concentration, churn risk, 
  auto-renewal rates, and any concerning terms or commitments."
- "Create an Investment Committee memo for this $150M acquisition of a mid-market CRM 
  platform. Include strategic rationale, key risks, valuation analysis, and integration plan."
- "Build a 3-statement financial model for this target with base/upside/downside scenarios. 
  Include normalized EBITDA adjustments and synergy assumptions."
- "Assess the technology stack for this cloud infrastructure company. Evaluate technical 
  debt, scalability, cybersecurity posture, and R&D productivity."
- "Quantify potential revenue and cost synergies from acquiring this competitor. Provide 
  confidence levels and 3-year realization timeline."
- "Evaluate management team quality and identify key person risks. Recommend retention 
  packages for critical employees."
- "Analyze customer cohorts and unit economics. What's the true customer lifetime value 
  and payback period?"
- "Review this data room for deal-breakers. Create a prioritized list of top 10 risks 
  with mitigation strategies."
- "Assess go-to-market efficiency. How does CAC, win rate, and sales cycle compare to 
  industry benchmarks?"
- "Develop a 100-day integration plan with Day 1 priorities, quick wins, and critical 
  path activities."
- "Conduct Quality of Earnings analysis on these financials. Normalize for one-time items, 
  non-recurring expenses, and related party transactions."
- "Evaluate this target's competitive position. Analyze win/loss trends, market share, 
  and sustainable competitive advantages."
- "Assess integration complexity for this acquisition. What are the key risks and what 
  resources will be required?"

**Analytical Frameworks & Methodologies:**
- Goldman Sachs hypothesis-driven due diligence with red flag matrices
- JP Morgan deal scorecard methodology with weighted criteria
- Morgan Stanley functional workstream approach
- Quality of Earnings (QoE) normalization adjustments framework
- Working capital peg analysis and target setting
- Scenario-based financial modeling (base/upside/downside)
- Comparable company analysis (trading multiples, growth/margin profiles)
- Precedent transaction analysis (deal multiples, synergy assumptions)
- DCF valuation with WACC calculations and terminal value analysis
- Customer reference call frameworks and scoring rubrics
- Management assessment rubrics (experience, track record, cultural fit)
- Risk assessment matrices (probability x impact scoring)
- Synergy waterfall analysis (revenue, cost, one-time costs)
- Integration complexity assessment frameworks
- Porter's Five Forces for market structure analysis
- TAM/SAM/SOM market sizing for growth opportunities
- Technology maturity assessment (technical debt scoring)
- Cybersecurity maturity models (NIST, CIS frameworks)

**Deal-Size Adaptive Framework:**
- **Small Deals ($10-50M):** Focused 2-4 week diligence, emphasis on strategic fit, 
  revenue quality, and key person risk. Streamlined deliverables with executive summary 
  and top 5 risks/opportunities.
- **Mid-Market ($50-250M):** Comprehensive 4-6 week multi-workstream diligence covering 
  all functional areas. Full IC memo, detailed financial model, and integration plan.
- **Large Deals ($250M+):** Extended 6-12 week deep-dive with specialist teams per 
  workstream. Extensive scenario analysis, detailed synergy models, and complex 
  integration planning with cultural assessment.

**Phased Diligence Approach:**
- **Phase 1 (Week 1):** Strategic assessment and preliminary fit analysis. Go/no-go decision.
- **Phase 2 (Weeks 2-4):** Deep functional diligence across all workstreams. Risk identification.
- **Phase 3 (Weeks 4-6):** Integration planning, synergy quantification, and deal structuring.
- **Phase 4 (Week 6):** IC materials preparation and final recommendation.

**Output Requirements:**

1. **Investment Committee Memos (25-40 pages):**
   - Executive summary (2-3 pages) with investment recommendation, deal rationale, 
     key risks, valuation summary, and synergy overview
   - Strategic assessment section (market opportunity, competitive position, strategic fit)
   - Financial analysis section (QoE findings, normalized metrics, historical performance)
   - Commercial diligence findings (customer analysis, unit economics, market position)
   - Technology assessment (tech stack, IP, scalability, technical debt)
   - Operational review (management team, org structure, key person risks)
   - Risk register with mitigation strategies (prioritized by severity)
   - Synergy analysis (revenue and cost synergies with confidence levels)
   - Valuation summary (standalone and with synergies, multiple scenarios)
   - Integration plan overview (Day 1 priorities, 100-day plan, critical success factors)
   - Appendices (detailed financial schedules, customer lists, org charts)

2. **PowerPoint Presentations:**
   - Executive summary deck (15-20 slides) for IC presentation
   - Professional investment banking formatting
   - Key slides: Investment thesis, financial highlights, risk matrix, valuation bridge, 
     synergy waterfall, integration roadmap
   - Data visualizations (charts, tables, matrices)
   - Use scripts/powerpoint_generator.py for consistent formatting

3. **Financial Models (Excel):**
   - Integrated 3-statement model (P&L, balance sheet, cash flow)
   - Historical financials (3-5 years) with normalization adjustments
   - Projections with base/upside/downside scenarios
   - Synergy models with revenue and cost synergies by year
   - Working capital schedule and calculation
   - DCF valuation with sensitivity analysis
   - Comparable company analysis with multiples
   - Precedent transaction analysis
   - Accretion/dilution analysis
   - Returns analysis (IRR, MOIC for PE buyers)
   - Audit trails and assumption documentation

4. **Due Diligence Findings Database:**
   - Comprehensive issues list with tracking status
   - Risk register with probability/impact scoring
   - Deal-breaker flags and mitigation strategies
   - Open items requiring additional diligence
   - Data room document index with key findings

5. **Integration Planning Materials:**
   - Day 1 readiness checklist
   - 100-day integration plan with milestones
   - Synergy realization roadmap
   - Key employee retention plan
   - Customer communication strategy
   - Systems integration timeline

**Writing Style & Presentation:**
- Investment banking-quality communication for IC and board consumption
- Data-driven analysis with specific metrics, comparables, and quantitative benchmarking
- Balanced perspective with explicit risks and upside/downside scenarios
- Clear structure: Executive summary → Strategic rationale → Detailed findings → Risks 
  → Valuation → Integration → Recommendation
- Explicit distinction between facts (sourced from data room) vs. assumptions/estimates
- Quantification of uncertainties and data gaps requiring additional diligence
- Deal-size appropriate depth (streamlined for small deals, comprehensive for large deals)
- Professional formatting consistent with Goldman Sachs/JP Morgan standards
- Use of comps, precedent transactions, and industry benchmarks for context
- Clear identification of deal-breakers vs. manageable risks

**Domain Knowledge Coverage:**

- **M&A Due Diligence Methodologies:** Goldman Sachs hypothesis-driven approach with 
  red flag matrices, JP Morgan deal scorecard with weighted criteria, Morgan Stanley 
  functional workstream methodology, systematic data room analysis protocols, management 
  assessment frameworks, customer reference call methodologies

- **Financial Analysis:** Quality of Earnings normalization adjustments (stock-based 
  comp, one-time items, related party transactions, non-recurring expenses), working 
  capital peg calculations and target setting, normalized EBITDA calculations, revenue 
  quality assessment (concentration, growth sustainability, pricing power), cash conversion 
  analysis, deferred revenue and billings analysis for SaaS

- **SaaS Metrics & Unit Economics:** ARR/MRR analysis, net revenue retention (NRR) and 
  gross retention (GRR), customer lifetime value (LTV), customer acquisition cost (CAC), 
  LTV/CAC ratios (3:1 benchmark), CAC payback period (12-18 months benchmark), Rule of 40 
  (growth rate + profit margin), magic number (ARR growth / sales & marketing spend), 
  cohort analysis and retention curves

- **Valuation Methodologies:** DCF modeling with WACC calculations, comparable company 
  analysis (trading multiples - EV/Revenue, EV/EBITDA), precedent transaction analysis 
  (M&A multiples with synergy assumptions), revenue multiple ranges by growth/margin profile, 
  accretion/dilution analysis for public acquirers, IRR and MOIC returns for PE buyers

- **Technology Due Diligence:** Cloud architecture assessment (AWS, Azure, GCP), API 
  architecture and integration capabilities, technical debt scoring and modernization costs, 
  scalability and infrastructure capacity, cybersecurity maturity (SOC 2, ISO 27001, 
  penetration testing), IP portfolio analysis, open source license compliance, mobile 
  and multi-platform support, data architecture and performance

- **Commercial Due Diligence:** Customer concentration thresholds (top 10 customers >30% 
  is high risk), cohort retention analysis, go-to-market efficiency metrics (quota attainment, 
  win rates, sales cycle length), pipeline coverage ratios (3-4x for healthy pipeline), 
  pricing power assessment, competitive win/loss analysis, market sizing (TAM/SAM/SOM)

- **Integration Planning:** Day 1 readiness checklists, 100-day plan with milestones and 
  owners, synergy quantification with confidence levels, retention packages for key employees 
  (1.5-2x annual comp), cultural compatibility assessment, systems integration roadmap 
  (ERP, CRM, HR systems), legal entity structure planning, customer communication strategies

- **Risk Assessment:** Probability x impact scoring matrices, deal-breaker identification 
  frameworks, regulatory approval risks (antitrust thresholds, CFIUS for foreign buyers), 
  customer/employee retention risks, technology migration risks, integration complexity scoring

- **Technology Sectors:** Enterprise SaaS, cloud infrastructure, cybersecurity, developer 
  tools, data/analytics platforms, vertical SaaS (fintech, healthtech, edtech), marketplaces, 
  IT infrastructure, collaboration software

**Input Types Handled:**
- Financial statements (P&L, balance sheet, cash flow statements)
- Management presentations and business plans
- Data room documents (contracts, agreements, policies, compliance docs)
- Customer lists and contract details (terms, renewal dates, ARR by customer)
- Sales pipeline and CRM data (opportunities, win rates, sales cycles)
- Product roadmaps and technical documentation
- Technology architecture diagrams and infrastructure docs
- Organizational charts and employee lists
- Compensation and benefits data
- Cap tables and ownership structures
- Market research and competitive intelligence reports
- IP documentation (patents, trademarks, licenses)
- Compliance and audit reports (SOC 2, ISO certifications, pen test results)
- Legal documents (customer contracts, vendor agreements, employment agreements)
- Historical board materials and management reports
- Integration plans and synergy assumptions

**Success Criteria:**
- Clear investment recommendation (proceed/pass/additional diligence) with supporting rationale
- Comprehensive risk identification with probability/impact scoring and mitigation strategies
- Quantified valuation with multiple methodologies (DCF, comps, precedents)
- Synergy analysis with confidence levels and realistic realization timelines
- Integration plan with specific Day 1 priorities and 100-day milestones
- All financial analysis includes normalized adjustments with clear documentation
- Data gaps and areas requiring additional diligence are explicitly flagged
- Deliverables are Investment Committee-ready (executive summary, supporting analysis, appendices)
- Deal-breakers are identified early with clear rationale
- Analysis is balanced with both upside opportunities and downside risks
- Comps and benchmarks provide market context for all key metrics
- Assumptions are clearly stated with sensitivity analysis on key drivers


**Requirements:**
- Python scripts needed: Yes
- Sample data type for testing: excel

**What to create:**
- Skill name: `m&a-due-diligence-expert`
- Include `scripts/` folder: Yes
- Testing materials: Provide realistic excel sample data


---

## For Each Skill, You Must Create:

### 1. Complete Folder Structure
- Create the skill folder with proper naming (lowercase, hyphens)
- Include SKILL.md with proper YAML frontmatter
- Add scripts/ folder ONLY if Python execution is needed
- Add references/ folder if detailed documentation should be separate
- Add assets/ folder if templates or resources are needed for output

### 2. SKILL.md Content
Following the exact format specified above with:
- Proper YAML frontmatter (name, description, license)
- Clear overview and purpose
- Specific trigger conditions
- Step-by-step procedural instructions
- Resource references
- Keywords for discoverability

### 3. Python Scripts (if applicable)
- Well-documented, production-ready code
- Clear docstrings explaining purpose and usage
- Error handling and input validation
- **Output Validation: For skills that generate calculations, reports, or data outputs:**
  - Include validation methods that verify calculation accuracy before delivering outputs
  - Add `validate_output()` methods to analysis/calculation classes that:
    - Recalculate key metrics manually to verify accuracy
    - Check for logical consistency (e.g., growth rates match trends, phases match data)
    - Validate ranges and expected values
    - Cross-check related calculations for consistency
  - Create validation scripts (e.g., `output_validator.py`) for comprehensive validation
  - Return validation results with errors, warnings, and passed checks
- Example usage in comments

### 4. Reference Files (if applicable)
- Detailed documentation that would clutter SKILL.md
- Database schemas, API specs, or domain knowledge
- Examples and use case walkthroughs

### 5. Asset Files (if applicable)
- Templates (Excel, PowerPoint, etc.)
- Images, icons, or design resources
- Boilerplate code or configuration files

### 6. Testing Materials
Create a `TESTING_GUIDE/` folder with:

**a) `sample_data/` folder containing:**
- Realistic sample data files appropriate to the skill type
- For data analysis: CSV or Excel files with realistic business data
- For API skills: JSON response examples
- For document skills: Sample PDFs or documents
- For image skills: Sample images
- Multiple examples covering different scenarios

**b) `invocation_prompts.txt` with:**
Multiple example prompts following this format:
```
Hey Claude—I just added the "[skill-name]" skill. Can you make something amazing with it?

[Additional context or specific request]
---

Hey Claude—I just added the "[skill-name]" skill. Can you [specific task]?

[Sample data reference or additional details]
---

[3-5 different invocation examples covering various use cases]
```

**c) `test_scenarios.md` with:**
```markdown
# Test Scenarios for [Skill Name]

## Basic Scenarios

### Scenario 1: [Name]
**Input:** [What data/prompt to use]
**Expected Output:** [What should be generated]
**Success Criteria:** [How to verify success]

### Scenario 2: [Name]
[Continue...]

## Intermediate Scenarios

### Scenario 3: [Name]
[More complex test case]

## Advanced Scenarios

### Scenario 4: [Name]
[Edge cases and complex situations]

## Edge Cases to Verify

- [Edge case 1]
- [Edge case 2]
- [Edge case 3]

## Common Issues and Solutions

- **Issue:** [Potential problem]
  **Solution:** [How to fix it]
```

---

## Integration and Overlap Guidance

**Strategy:** overlapping


**Since you're creating overlapping skills:**
- Skills may share some functionality and complement each other
- Design skills to work together (e.g., one skill generates data, another visualizes it)
- It's okay for skills to reference or build upon each other
- Consider creating a skill ecosystem where skills can be composed
- Document in each SKILL.md how it works with other skills


---

## Domain-Specific Considerations


### Domain Knowledge to Incorporate

The following domain-specific terminology and knowledge should be incorporated into skills:

- M&A due diligence methodologies from Goldman Sachs, JP Morgan, and Morgan Stanley
- Quality of Earnings analysis and normalization adjustments (one-time items, non-recurring, related party)
- Working capital analysis and peg calculations for target setting
- Technology due diligence for SaaS and enterprise software companies
- Commercial due diligence and unit economics analysis (LTV/CAC, cohort retention)
- SaaS business model metrics (ARR, NRR, GRR, Rule of 40, magic number, CAC payback)
- Integration planning and synergy quantification methodologies
- Risk assessment frameworks (probability x impact matrices, Monte Carlo simulation)
- Valuation methodologies (DCF with WACC, comparable companies, precedent transactions)
- Deal structuring considerations (asset vs. stock, earnouts, reps & warranties)
- Post-merger integration best practices and Day 1 readiness planning
- Data room analysis and systematic document review protocols
- Management assessment frameworks and reference call methodologies
- Customer and vendor reference call frameworks with scoring rubrics
- Regulatory and antitrust considerations for technology deals
- IP due diligence and patent portfolio analysis
- Technology stack assessment (cloud architecture, APIs, scalability, infrastructure)
- Cybersecurity and data privacy compliance (SOC 2, ISO 27001, GDPR, CCPA)
- Financial modeling for SaaS companies (ARR builds, cohort models, retention curves)
- Revenue quality assessment and sustainability analysis
- Retention risk analysis for key employees and customers
- Market sizing and TAM/SAM/SOM analysis for technology sectors
- Competitive landscape analysis for enterprise software markets
- Product-market fit assessment and customer validation frameworks
- Go-to-market strategy evaluation (sales productivity, win rates, pipeline coverage)
- Comparable company analysis (identifying comps, calculating multiples, adjustments)
- Precedent transaction analysis (deal multiples, synergy assumptions, market context)
- Accretion/dilution analysis for public company acquirers
- Returns analysis for PE buyers (IRR, MOIC, cash-on-cash returns)
- Working capital normalization and target balance sheet creation
- Contract review frameworks (customer, vendor, employment agreements)
- Litigation and regulatory risk assessment
- Integration complexity scoring and resource planning
- Cultural compatibility assessment and change management
- Key employee retention strategies and compensation planning (1.5-2x annual comp)
- Systems integration roadmap (ERP, CRM, HR platforms)
- Customer communication strategies and retention planning
- Synergy realization tracking and value capture methodologies

Ensure these concepts are properly explained in SKILL.md or reference files.



### Required Integrations

Skills should integrate with or support these tools/platforms:

- Excel (complex financial models, valuation analysis, scenario planning, working capital schedules)
- PowerPoint generation (Investment Committee presentations with professional formatting)
- PDF analysis (data room document review, contract analysis, financial statement parsing)
- Python data analysis (pandas, numpy for financial modeling, statistical analysis)
- Document parsing and text extraction (for contract review and data room analysis)
- Data visualization libraries (matplotlib, plotly, seaborn for charts and graphs)
- Financial data APIs (for comparable company data, market multiples, benchmarking)
- Web research for market intelligence, competitive analysis, and precedent transactions

Include appropriate instructions for working with these tools in your skills.



### Constraints and Requirements

All skills must adhere to these constraints:

- Must adapt framework complexity based on deal size ($10M requires different depth than $250M+)
- Must clearly flag data gaps, missing information, and areas requiring additional diligence
- Must provide probability-weighted risk assessments with specific mitigation strategies
- Must quantify synergies with confidence levels (high/medium/low) and realization timelines
- Must distinguish between strategic deal-breakers vs. tactical issues manageable post-close
- Must produce Investment Committee-ready materials with executive summaries
- Analysis must be suitable for board and senior management consumption
- Must identify integration complexity and execution risks upfront
- Financial analysis must include normalized adjustments with clear documentation of changes
- Must use verifiable data sources and clearly flag assumptions vs. sourced facts
- Must provide scenario analysis (base/upside/downside) for key financial metrics
- Must assess cultural fit and change management requirements for integration
- Must evaluate retention risk for key personnel (technical, sales, product leadership)
- PowerPoint output must follow professional investment banking formatting standards
- Excel models must include audit trails, assumption documentation, and sensitivity analysis
- Must benchmark key metrics against comparable companies and industry standards
- Must clearly identify deal-breakers early in diligence process (within Phase 1-2)
- Valuation must use multiple methodologies (DCF, comps, precedents) with range of outcomes
- Risk assessment must use probability x impact scoring with quantified financial impact
- Integration plans must include specific Day 1 priorities and 100-day milestones with owners
- Must balance acquirer perspective (opportunities/synergies) with objective risk assessment
- Customer concentration risk must be explicitly assessed (>30% from top 10 is high risk)
- Technology assessment must evaluate both current state and modernization requirements
- All synergy assumptions must be validated with specific implementation plans

Consider these constraints when designing workflows and selecting approaches.


---

## Quality Standards

Each skill must meet these standards:

1. **Professional Quality**
   - Production-ready code with error handling
   - Clear, comprehensive documentation
   - Follows all formatting requirements exactly
   - **Output Accuracy**: All calculations and outputs are validated for accuracy before delivery
   - **Validation Mechanisms**: Skills that generate calculations or data outputs include validation methods

2. **Practical Utility**
   - Solves real business problems
   - Includes concrete examples
   - Provides clear value over general Claude usage

3. **Maintainability**
   - Well-organized file structure
   - Clear separation of concerns
   - Easy to update and extend

4. **Testability**
   - Comprehensive testing materials included
   - Multiple realistic scenarios covered
   - Clear success criteria defined

5. **Output Validation**
   - **For calculation/analysis skills**: Include validation methods that verify calculation accuracy
   - **For Excel/model skills**: Validate formulas and calculations before saving
   - **For report skills**: Verify all numerical values match source calculations
   - **Mandatory validation step**: Always include a final validation step in the workflow before delivering outputs
   - **Validation results**: Document validation checks performed and any errors found/corrected

---

## Output Format

For each skill, provide:

1. A clear summary of what the skill does
2. The complete file structure
3. Full contents of SKILL.md
4. Any Python scripts with complete code
5. Reference files if applicable
6. Asset files descriptions
7. Complete testing guide with sample data

Present each skill in a clear, organized manner that can be directly implemented.

---

## Additional Notes

- Keep SKILL.md under 5,000 words
- Use references/ for detailed docs to keep SKILL.md lean
- Scripts should be token-efficient alternatives to repeated generation
- Assets are files used IN outputs, not loaded into context
- Testing materials should be comprehensive enough to validate all functionality
- **Output Validation**: Skills that generate calculations, reports, or data outputs MUST include validation mechanisms:
  - Validation methods in Python scripts (e.g., `validate_output()`)
  - Validation step in workflow instructions
  - Instructions to manually verify key calculations
  - Validation results documentation

---

Begin generating the 1 skills now, following all specifications above.

