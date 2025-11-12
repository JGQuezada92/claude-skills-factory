# Test Scenarios for M&A Due Diligence Expert

## Basic Scenarios

### Scenario 1: Financial Statement Analysis
**Input:** Upload quarterly financial statements (P&L, Balance Sheet, Cash Flow) for a SaaS company  
**Prompt:** "Analyze these financials and identify any quality of earnings issues or red flags."  
**Expected Output:**
- Revenue quality assessment
- Normalized EBITDA calculations
- Working capital analysis
- SaaS metrics (ARR, NRR, GRR, Rule of 40)
- Identification of any concerning trends

**Success Criteria:**
- Calculation accuracy verified
- Normalization adjustments properly documented
- Red flags clearly identified
- Benchmarking against industry standards included

### Scenario 2: Customer Concentration Analysis
**Input:** Customer list with revenue by customer for 2-3 years  
**Prompt:** "Assess customer concentration risk and analyze retention trends."  
**Expected Output:**
- Top 10 customer concentration percentage
- Customer retention analysis by cohort
- Churn rate calculations
- Risk assessment (flag if >30% from top 10)
- Customer dependency analysis

**Success Criteria:**
- Accurate concentration calculations
- Retention trends properly analyzed
- Risk level appropriately assessed
- Recommendations for mitigation provided

### Scenario 3: Simple Valuation Analysis
**Input:** Financial projections and basic market data  
**Prompt:** "Perform a DCF valuation with 10% WACC and 3% terminal growth."  
**Expected Output:**
- DCF calculation with explicit period and terminal value
- Present value calculations verified
- Enterprise value determination
- Sensitivity analysis on WACC and growth rate

**Success Criteria:**
- Mathematical accuracy of DCF model
- Proper discounting methodology
- Reasonable sensitivity ranges
- Clear presentation of valuation range

## Intermediate Scenarios

### Scenario 4: Multi-Method Valuation
**Input:** Financial projections, comparable company data, precedent transactions  
**Prompt:** "Perform comprehensive valuation using DCF, comparable companies, and precedent transactions. Provide a blended valuation range."  
**Expected Output:**
- DCF valuation with scenarios
- Comparable company analysis with peer multiples
- Precedent transaction analysis
- Valuation summary with triangulated range
- Key assumptions documented

**Success Criteria:**
- All three methodologies properly executed
- Reasonable multiple ranges vs. peers
- Blended valuation logically weighted
- Range accounts for uncertainty

### Scenario 5: Technology Stack Assessment
**Input:** Technology architecture documentation, product roadmap, dev team info  
**Prompt:** "Evaluate the technology stack for technical debt, scalability issues, and integration complexity."  
**Expected Output:**
- Architecture assessment (cloud, languages, frameworks)
- Technical debt scoring and prioritization
- Scalability analysis
- Integration complexity assessment
- Modernization cost estimate

**Success Criteria:**
- Comprehensive technology evaluation
- Technical debt properly prioritized
- Scalability risks identified
- Reasonable cost estimates for remediation

### Scenario 6: Risk Register Development
**Input:** Data room documents across all functional areas  
**Prompt:** "Create a comprehensive risk register with probability/impact scoring for all identified issues."  
**Expected Output:**
- Risk register with all material risks identified
- Probability (1-5) and impact (1-5) scoring
- Risk categorization (strategic, financial, operational, legal)
- Deal-breaker identification
- Mitigation strategies for each risk
- Top 10 risks prioritized

**Success Criteria:**
- Comprehensive risk identification across workstreams
- Consistent scoring methodology
- Deal-breakers clearly flagged
- Actionable mitigation strategies
- Risk register format suitable for IC presentation

## Advanced Scenarios

### Scenario 7: Complete Investment Committee Package
**Input:** Full data room with financial statements, customer contracts, technology docs, legal materials  
**Prompt:** "Create a complete Investment Committee package including memo (25-40 pages), PowerPoint presentation (15-20 slides), and financial model."  
**Expected Output:**
- Executive summary with clear recommendation
- Comprehensive IC memo covering all workstreams
- Professional PowerPoint presentation
- Integrated financial model (Excel)
- Risk register
- Synergy analysis
- Valuation summary
- Integration plan

**Success Criteria:**
- IC memo meets investment banking quality standards
- All sections comprehensive and well-organized
- PowerPoint follows professional formatting
- Financial model includes scenarios and sensitivities
- Clear proceed/pass/additional diligence recommendation
- Supporting analysis for all key conclusions

### Scenario 8: Synergy Quantification & Integration Planning
**Input:** Target company info, acquirer info, overlap analysis  
**Prompt:** "Quantify revenue and cost synergies with confidence levels, develop realization timeline, and create 100-day integration plan."  
**Expected Output:**
- Revenue synergy identification and quantification
- Cost synergy analysis by category
- Confidence levels (high/medium/low) assigned
- 3-year realization timeline
- One-time implementation costs
- NPV of synergies
- Day 1 priorities
- 100-day integration plan with milestones
- Key employee retention strategy
- Customer communication plan

**Success Criteria:**
- Realistic synergy estimates with clear rationale
- Confidence levels appropriate to assumptions
- Implementation costs properly estimated
- Integration plan detailed and actionable
- Critical path activities identified
- Retention strategy addresses key person risks

### Scenario 9: Complex Deal Structure Analysis
**Input:** Deal terms, earnout structure, reps & warranties insurance  
**Prompt:** "Analyze the deal structure including earnout provisions, evaluate if structure addresses key risks, and calculate earnout scenarios."  
**Expected Output:**
- Deal structure assessment (asset vs. stock)
- Earnout analysis with scenarios
- Assessment of risk allocation
- Change of control provision analysis
- Tax implications overview
- Recommendation on deal structure optimization

**Success Criteria:**
- Thorough deal structure analysis
- Earnout scenarios properly modeled
- Risk allocation assessed
- Tax implications identified
- Recommendations supported by analysis

### Scenario 10: Multi-Deal Comparison
**Input:** Due diligence materials for 2-3 potential acquisition targets  
**Prompt:** "Compare these three acquisition targets across financial quality, strategic fit, risk profile, and valuation. Provide a prioritized recommendation."  
**Expected Output:**
- Side-by-side comparison matrix
- Scoring across key dimensions
- Relative valuation analysis
- Risk comparison
- Strategic fit assessment
- Clear prioritization with rationale

**Success Criteria:**
- Objective comparison framework
- Consistent evaluation methodology
- Fair assessment of each target
- Clear prioritization with supporting logic
- Consideration of strategic fit, financial attractiveness, and risk

## Edge Cases to Verify

- **Negative EBITDA target:** Can handle loss-making companies with path to profitability
- **High customer concentration (>50%):** Properly flags as high risk with mitigation strategies
- **Multiple currencies:** Handles international targets with currency conversion
- **Complex ownership structures:** Addresses earnouts, rollover equity, minority stakes
- **Missing data:** Clearly flags data gaps and areas requiring additional diligence
- **Recent business model changes:** Adjusts analysis for companies transitioning (e.g., perpetual to subscription)
- **Pending litigation:** Incorporates litigation risk into valuation and risk register
- **Regulatory approval risks:** Addresses antitrust, CFIUS, or other regulatory hurdles
- **Technology platform migrations:** Evaluates mid-migration technology transformation risks
- **Founder/key person dependency:** Identifies and quantifies retention risk

## Common Issues and Solutions

- **Issue:** DCF valuation produces unrealistic values (too high or too low)  
  **Solution:** Review WACC calculation, terminal growth rate assumptions, and cash flow projections for reasonableness. Conduct sensitivity analysis to understand key drivers.

- **Issue:** Comparable company analysis has wide valuation range  
  **Solution:** Refine peer selection based on size, growth, and margin profile. Adjust for differences in business model or market position. Use quartile ranges.

- **Issue:** Risk register becomes too long and unfocused  
  **Solution:** Focus on material risks with >5% impact on deal value. Categorize by workstream. Prioritize top 10 risks for executive attention.

- **Issue:** Integration plan is too generic  
  **Solution:** Customize based on specific deal dynamics, target size, and integration complexity. Include specific milestones, owners, and timelines.

- **Issue:** Synergy estimates appear overly optimistic  
  **Solution:** Apply appropriate confidence levels. Benchmark against similar transactions. Be conservative on timing. Include implementation costs.

- **Issue:** Data gaps prevent complete analysis  
  **Solution:** Clearly flag areas with insufficient data. Provide analysis based on available information with caveats. List additional diligence requirements.

