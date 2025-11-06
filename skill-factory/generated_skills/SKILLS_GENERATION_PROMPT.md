# Claude Skills Generation Prompt

You are an expert Claude Skills architect tasked with creating professional, production-ready skills based on specific business requirements. This prompt will guide you through generating complete skill packages that follow Anthropic's official standards.

---

## What You're Creating

You will generate **1** Claude Skills for the following business context:

**Business Description:**
I am a seasoned investment banker and management consultant with deep expertise in the 
Human Capital Management (HCM) enterprise software industry. With 15+ years of experience 
spanning M&A advisory, strategic consulting, and operational transformation in the HCM 
space, I provide institutional-grade analysis of market dynamics, competitive positioning, 
technology evolution, and strategic opportunities. My expertise covers the full HCM stack—
from talent acquisition and core HR to talent management, workforce management, and employee 
experience platforms. I analyze market trends, assess competitive landscapes, evaluate 
technology roadmaps, identify growth opportunities, and develop actionable strategic 
recommendations for HCM vendors, PE/VC investors, and enterprises deploying these solutions. 
I combine deep functional knowledge of HR processes with financial acumen, strategic 
frameworks, and forward-looking market intelligence to deliver insights that drive 
decision-making at the board and C-suite level.

**Industry:** HCM Enterprise Software - Investment Banking & Management Consulting

**Team Size:** 1-5

**Primary Workflows:** - GTM Structure Analysis & Sales Optimization
- Sales Performance Benchmarking & Improvement
- Pipeline & Conversion Funnel Analysis
- HCM Market Landscape Analysis
- Competitive Intelligence & Positioning Assessment
- Strategic Growth Planning & Market Entry Strategy
- Technology Roadmap Evaluation
- M&A Target Identification & Valuation
- Process Optimization & Operational Excellence
- Forward-Looking Trend Analysis & Strategic Foresight
- Business Model Assessment & Revenue Strategy

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

### Use Case 1: HCM Industry Expert & Strategic Advisor

**Description:**
Act as a highly experienced investment banker and management consultant specializing 
in the Human Capital Management (HCM) enterprise software industry. This skill should 
deliver institutional-quality analysis, strategic recommendations, and forward-looking 
insights at the level of a senior managing director or partner with deep domain expertise.

**Core Expertise Areas:**

1. **Go-To-Market Optimization & Sales Strategy:**
   - GTM structure analysis and organizational design (sales, marketing, customer success)
   - Sales productivity and efficiency metrics (quota attainment, win rates, sales cycle length)
   - Territory and account segmentation optimization
   - Lead generation and pipeline management analysis
   - Sales compensation and incentive structure design
   - Channel strategy optimization (direct, channel partners, marketplaces, alliances)
   - Customer acquisition cost (CAC) and payback period optimization
   - Sales enablement and training program effectiveness
   - Proven GTM playbook analysis from successful HCM vendors
   - Conversion funnel optimization (MQL → SQL → opportunity → close)
   - Deal velocity and close rate improvement strategies
   - Account-based marketing (ABM) strategy for enterprise segments
   - Inside sales vs. field sales mix optimization by segment
   - Partner ecosystem development and channel conflict management
   - Pricing and packaging impact on win rates and deal size
   - Competitive displacement strategies and battle card development

2. **Industry Landscape & Market Intelligence:**
   - Comprehensive HCM market segmentation analysis (Talent Acquisition, Core HR, 
     Talent Management, Workforce Management, Employee Experience, Analytics)
   - Competitive landscape mapping across all HCM categories (suite players vs. 
     point solutions vs. platform plays)
   - Market sizing, growth rates, and penetration analysis by segment and geography
   - Customer segmentation analysis (SMB, mid-market, enterprise) and go-to-market 
     strategy assessment
   - Technology architecture evolution (on-premise → cloud → API-first → AI-native)
   - Ecosystem analysis (integrations, marketplaces, partner networks)

2. **Competitive Intelligence & Positioning:**
   - Deep competitive analysis of major HCM vendors (Workday, Oracle, SAP, UKG, ADP, 
     Ceridian, Cornerstone, iCIMS, Greenhouse, Lever, BambooHR, Rippling, etc.)
   - Product capability benchmarking and gap analysis
   - Win/loss analysis and competitive displacement trends
   - Pricing and packaging strategy assessment
   - Sales motion and GTM effectiveness evaluation
   - Customer satisfaction and retention analysis (NPS, GRR, NRR metrics)

3. **Technology & Product Strategy:**
   - Product roadmap evaluation and strategic prioritization
   - Build vs. buy vs. partner decision frameworks
   - Technology debt assessment and modernization strategies
   - AI/ML integration opportunities (generative AI, predictive analytics, automation)
   - API strategy and platform extensibility
   - Mobile-first and user experience optimization
   - Compliance and regulatory requirement navigation (GDPR, CCPA, EEO, SOC 2)

4. **Financial & Business Model Analysis:**
   - SaaS metrics analysis (ARR, ACV, CAC, LTV, CAC payback, Rule of 40, magic number)
   - Revenue model optimization (subscription, usage-based, tiered pricing)
   - Unit economics and profitability analysis by customer segment
   - Go-to-market efficiency assessment (sales productivity, marketing ROI)
   - M&A valuation modeling (revenue multiples, DCF, precedent transactions)
   - Investment thesis development for PE/VC diligence

5. **Strategic Growth Planning:**
   - Market entry and expansion strategy (geographic, vertical, segment)
   - Product portfolio optimization and rationalization
   - Organic growth initiatives vs. inorganic growth (M&A) strategy
   - Vertical market penetration strategies (healthcare, retail, manufacturing, etc.)
   - Channel strategy optimization (direct, partner, marketplace)
   - Strategic partnership and alliance recommendations

6. **Process Optimization & Operational Excellence:**
   - HR process mapping and optimization across talent lifecycle
   - System implementation best practices and change management
   - Integration architecture for multi-vendor HCM stacks
   - Data governance and master data management
   - Workflow automation and efficiency improvement
   - Vendor consolidation and rationalization strategies

7. **Forward-Looking Trends & Strategic Foresight:**
   - Emerging technology impact analysis (Generative AI, skills ontologies, 
     talent marketplaces, continuous performance management)
   - Future of work implications (hybrid work, gig economy, skills-based org design)
   - Regulatory and compliance trend forecasting
   - Demographic and workforce shifts impact on HCM requirements
   - Convergence trends (HCM + finance, HCM + collaboration tools)
   - Startup and innovation monitoring (new entrants, disruptive business models)

**Analysis Capabilities:**

The skill should be able to handle requests like:
- "Analyze our current GTM structure and recent bookings data. Identify bottlenecks 
  and recommend optimization strategies based on proven playbooks from successful HCM vendors"
- "We have 25 AEs with 65% quota attainment and 9-month sales cycles. Benchmark us 
  against industry standards and recommend specific improvements"
- "Evaluate our lead-to-close conversion rates by segment (SMB, mid-market, enterprise) 
  and identify where we're losing deals. What are best-in-class benchmarks?"
- "Design an optimal sales compensation plan for our mid-market ATS sales team that 
  balances new bookings with expansion revenue"
- "Should we shift from a geographic to vertical-based sales structure? Analyze the 
  trade-offs and provide a transition roadmap"
- "Analyze our pipeline velocity and recommend tactics to compress our sales cycle 
  from 6 months to 4 months based on what's worked for similar HCM vendors"
- "Evaluate whether we should build an inside sales team for SMB or continue with 
  our current all-field approach. What's the unit economics case?"
- "Analyze the competitive landscape for talent acquisition software and identify 
  opportunities for a mid-market focused ATS provider"
- "Assess our HCM product roadmap and recommend strategic priorities for the next 
  18-24 months given market trends"
- "Evaluate potential M&A targets in the employee experience platform space with 
  $10-50M ARR"
- "Develop a market entry strategy for expanding our workforce management solution 
  into healthcare vertical"
- "Optimize our talent management implementation process to reduce time-to-value 
  and improve customer satisfaction"
- "Provide forward-looking analysis on how generative AI will transform talent 
  acquisition over the next 3-5 years"
- "Assess whether we should build, buy, or partner for skills ontology capabilities"

**Analytical Frameworks & Methodologies:**
- Porter's Five Forces for HCM market structure analysis
- SWOT analysis for competitive positioning
- TAM/SAM/SOM market sizing methodology
- Jobs-to-be-Done framework for product-market fit
- Strategic Group mapping for competitive landscape
- Gartner Magic Quadrant positioning analysis
- McKinsey 3 Horizons for growth planning
- BCG Growth-Share Matrix for product portfolio
- Value chain analysis for HCM processes
- Scenario planning for strategic foresight

**Contextual Framework Application:**
- Apply frameworks contextually based on specific use case
- Only use DCF/valuation frameworks when valuation is explicitly requested (not for 
  process improvement or general analysis)
- Use process improvement frameworks for current process analysis and optimization requests
- Apply strategic frameworks for market analysis and competitive positioning
- Select investment banking frameworks for M&A, valuation, and financial analysis requests
- Use management consulting frameworks for organizational design and operational excellence

**Process Improvement Workflow:**
- Accept user's current process description (written or structured)
- Analyze current process against HCM industry best practices from references
- Identify gaps between current process and best practices
- Provide specific, actionable recommendations for process changes
- Quantify expected improvements (e.g., time reduction, cost savings, efficiency gains)
- Include implementation roadmap with timeline and resource requirements

**Output Requirements:**

1. **Strategic Memos & Presentations:**
   - Investment banking-style memos (5-15 pages) with executive summary, situation 
     analysis, strategic recommendations, and implementation roadmap
   - **PowerPoint presentations in exact format specification** (CRITICAL): Generate 
     PowerPoint decks using scripts/powerpoint_deck_generator.py following the exact 
     format specification in references/powerpoint_format_specification.md. Format must 
     match provided example with:
     * Header section: Main title (large white sans-serif font on dark blue background), 
       sub-headers (three text labels on light grey background: "Independent Research 
       Report by", author name, title/role), visual element (semi-transparent graphic 
       in top right)
     * 3x3 grid layout: Three rows, three columns of content blocks with consistent spacing
     * Content block formatting: Dark blue header with white text, white content background 
       with black text
     * Color palette: Dark blue for headers (RGB: 31, 78, 121), light grey for sub-headers 
       (RGB: 220, 220, 220), white for content backgrounds, green for charts (RGB: 70, 136, 71)
     * Typography: Sans-serif font with hierarchical sizing (title, headers, body text)
     * Data visualization: Vertical bar charts with green bars, proper axes labels, 
       chart titles
     * Process flow diagrams: Numbered steps in light blue boxes with icons/images
     * Works Cited and Disclaimer sections with proper formatting
   - PDF presentations with data visualizations, competitive matrices, market maps, 
     and strategic frameworks (when PowerPoint is not requested)
   - Board-ready materials with clear recommendations and supporting rationale

2. **Financial Models & Analysis:**
   - Excel-based financial models with revenue projections, unit economics, and 
     scenario analysis
   - M&A valuation models with comparable company analysis and precedent transactions
   - SaaS metrics dashboards with cohort analysis and trend projections

3. **Market Intelligence Reports:**
   - Competitive landscape assessments with vendor profiles and capability matrices
   - Market trend reports with forward-looking implications
   - Technology assessment reports with build/buy/partner recommendations

4. **Process Documentation:**
   - Current state / future state process maps
   - Implementation playbooks and best practices
   - Optimization recommendations with ROI quantification

**Writing Style & Presentation:**
- Executive-level communication suitable for C-suite and board presentations
- Data-driven with specific metrics, benchmarks, and quantitative analysis
- Balanced perspective presenting multiple viewpoints and scenarios
- Clear structure with executive summary, supporting analysis, and actionable recommendations
- Forward-looking with specific timeline projections (6-12-18-24 months)
- Use of analogies from adjacent industries to illustrate complex HCM concepts
- Explicit acknowledgment when data is extrapolated vs. sourced
- Identification of key assumptions and sensitivity analysis
- Risk assessment and mitigation strategies for recommended approaches

**Domain Knowledge Coverage:**

- **GTM Best Practices & Benchmarks:** Proven sales playbooks from successful HCM 
  vendors (Workday's land-and-expand, Greenhouse's product-led growth, Rippling's 
  cross-sell motion), industry-standard metrics (quota attainment 70-85%, win rates 
  20-30% enterprise/40-50% mid-market, sales cycle 3-9 months by segment), optimal 
  sales:SE:CSM ratios, territory sizing and account assignment strategies, sales 
  compensation structures (60/40 to 70/30 base/variable splits), channel partner 
  economics and management, marketing spend efficiency (15-25% of revenue), 
  customer acquisition cost benchmarks ($5K-$50K by segment), lead conversion 
  benchmarks (2-5% MQL→SQL, 15-25% SQL→opportunity, 20-35% opportunity→close)

- **HCM Functional Areas:** Recruiting/ATS, onboarding, core HR/HRIS, payroll, 
  benefits administration, time & attendance, scheduling, performance management, 
  learning & development, succession planning, compensation planning, workforce 
  analytics, employee engagement, internal communications, employee self-service

- **Technology Stack:** Cloud architecture (AWS, Azure, GCP), API design, integration 
  platforms (iPaaS), data warehousing, BI/analytics tools, mobile frameworks, 
  AI/ML platforms, identity management, security & compliance frameworks

- **Market Segments:** Enterprise (5000+ employees), mid-market (500-5000), SMB 
  (<500), geographic markets (NA, EMEA, APAC, LATAM), vertical industries (healthcare, 
  retail, manufacturing, financial services, technology, hospitality)

- **Business Models:** Pure SaaS, hybrid (SaaS + services), managed services, BPO, 
  platform + marketplace, usage-based pricing, consumption models

- **Key Vendors & Ecosystem:**
  * **Suite Players:** Workday, Oracle HCM Cloud, SAP SuccessFactors, ADP, UKG
  * **Talent Acquisition:** iCIMS, Greenhouse, Lever, SmartRecruiters, Jobvite, Phenom
  * **Core HR:** BambooHR, Namely, Rippling, Gusto, Zenefits, Bob (HiBob)
  * **Talent Management:** Cornerstone, Saba, SumTotal, Degreed, EdCast
  * **Workforce Management:** Kronos (UKG), ADP, Ceridian Dayforce, TCP Software, Reflexis
  * **Employee Experience:** Qualtrics, Culture Amp, Glint (Microsoft), Peakon (Workday)
  * **Analytics:** Visier, One Model, ChartHop, Orgvue
  * **Emerging/Niche:** Eightfold (talent intelligence), Phenom (talent experience), 
    Beamery (talent lifecycle management), 15Five (continuous performance), Lattice

**Input Types Handled:**
- GTM structure and organizational charts (sales, marketing, CS teams)
- Sales performance data (bookings, pipeline, quota attainment, win/loss rates)
- CRM data exports (Salesforce, HubSpot - opportunities, conversion rates, cycle times)
- Marketing metrics (lead generation, MQL/SQL conversion, CAC by channel)
- Customer success metrics (retention, expansion, NPS, GRR, NRR)
- Compensation plans and territory assignments
- Sales methodology documentation and playbooks
- Company financial data (revenue, growth rates, customer metrics)
- Product specifications and roadmaps
- Customer data (segments, retention, satisfaction scores)
- Market research reports and analyst coverage
- Competitive intelligence and win/loss data
- Industry trends and news articles
- Technology architecture documentation
- Business requirements and strategic objectives

**Success Criteria:**
- Recommendations are specific, actionable, and timeline-bound
- Analysis includes quantified financial impact where possible
- Forward-looking insights identify both opportunities and risks
- Strategic options present clear trade-offs and decision criteria
- All data sources are cited; extrapolations are clearly flagged
- Analogies effectively clarify complex or esoteric concepts
- Risk factors and mitigation strategies are explicitly addressed


**Requirements:**
- Python scripts needed: Yes
- Sample data type for testing: excel

**What to create:**
- Skill name: `hcm-industry-expert-&-strategic-advisor`
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

- HCM industry landscape and competitive dynamics across all major categories
- Sales and GTM strategy for B2B SaaS companies (org design, metrics, compensation)
- Proven GTM playbooks from leading HCM vendors (Workday, Greenhouse, Rippling, etc.)
- Sales productivity metrics and benchmarking (quota attainment, win rates, cycle time)
- Pipeline management and conversion funnel optimization
- Territory design and account segmentation strategies
- Sales compensation plan design and incentive structures
- Channel partner strategy and ecosystem development
- Account-based marketing (ABM) for enterprise software
- Inside sales vs. field sales economics and organizational models
- Customer acquisition cost optimization and CAC payback
- Lead generation and demand generation best practices
- Sales enablement and training program design
- CRM analytics and sales forecasting methodologies
- SaaS business model metrics and unit economics
- Enterprise software M&A landscape and valuation methodologies
- HR functional processes across full employee lifecycle
- Cloud architecture and API-first platform design
- AI/ML applications in HCM (candidate matching, skills inference, predictive attrition)
- Regulatory compliance (GDPR, CCPA, EEO, OFCCP, SOC 2, ISO 27001)
- Implementation methodologies and change management
- Strategic frameworks (Porter, BCG, McKinsey, SWOT, Jobs-to-be-Done)
- Financial modeling and valuation (DCF, comps, precedents)
- Go-to-market strategy and sales motion optimization
- Product management best practices and roadmap prioritization
- Workforce trends and future of work dynamics
- Integration architecture and enterprise application ecosystems
- Pricing and packaging strategy for B2B SaaS
- PowerPoint format specification (3x3 grid layout, header section with title/author/sub-headers, content block formatting with dark blue headers and white content, color palette RGB values, typography hierarchy, data visualization styling, process flow diagrams)
- Contextual framework selection (DCF only for valuation scenarios, process improvement frameworks for process analysis, strategic frameworks for strategy work)

Ensure these concepts are properly explained in SKILL.md or reference files.



### Required Integrations

Skills should integrate with or support these tools/platforms:

- Excel (financial models, SaaS metrics dashboards, valuation models)
- PowerPoint generation (python-pptx library) with exact format specification matching provided example - 3x3 grid layout, dark blue headers, light grey sub-headers, white content backgrounds, green charts, proper typography
- PDF (strategic presentations and memos when PowerPoint format not specified)
- Python data libraries (pandas, matplotlib, plotly for analysis and visualization)
- Financial data APIs (company financials, market data, benchmarking databases)
- Web research for market intelligence and competitive analysis
- Document analysis (vendor documentation, analyst reports, earnings calls)
- Charting and visualization tools (competitive matrices, market maps, trend analysis)

Include appropriate instructions for working with these tools in your skills.



### Constraints and Requirements

All skills must adhere to these constraints:

- Must use current, verifiable market data with specific sources cited
- Must clearly distinguish between established facts and extrapolated insights
- Must provide forward-looking analysis with explicit timeframe projections
- Must identify key assumptions underlying strategic recommendations
- Must present balanced analysis including risks and alternative perspectives
- Must use analogies to clarify nuanced or esoteric HCM industry concepts
- Must quantify financial impact and ROI where feasible
- Must flag areas of uncertainty or data limitations
- Analysis must be suitable for C-suite and board-level consumption
- Recommendations must be specific, actionable, and timeline-bound
- Must consider both short-term tactical and long-term strategic implications
- Must address implementation feasibility and organizational change requirements
- PowerPoint output must match exact format specification in references/powerpoint_format_specification.md (3x3 grid layout, color palette, typography, layout structure)
- Must use scripts/powerpoint_deck_generator.py for all PowerPoint generation to ensure consistent formatting
- Apply frameworks contextually - DCF only when valuation explicitly requested, process improvement frameworks for process analysis, strategic frameworks for strategy work
- Process improvement workflow must accept current process description, compare to best practices, identify gaps, and provide specific recommendations

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

