# Elite FP&A Professional - Test Scenarios

This document provides comprehensive test scenarios organized by complexity level to validate the Elite FP&A Professional skill.

---

## Test Scenario Structure

Each scenario includes:
- **Objective:** What to test
- **Input:** Data and context to provide
- **Expected Output:** What the analysis should include
- **Success Criteria:** How to evaluate the response

---

## BASIC TEST SCENARIOS

### Scenario 1: Basic Financial Statement Analysis

**Objective:** Test ability to analyze financial statements and provide high-level insights

**Input:**
- Income statement, balance sheet, cash flow statement (1 period)
- Company description: "$50M revenue technology company"

**Invocation Prompt:**
```
"Analyze these financial statements and provide an executive summary of the company's 
financial health. Identify 3 key strengths and 3 key concerns."
```

**Expected Output:**
- Overall financial health assessment (Excellent/Good/Concerning/Poor)
- 3 specific strengths with supporting metrics
- 3 specific concerns with supporting metrics
- Clear, executive-level language
- Formatted in Arial font

**Success Criteria:**
- ✓ Provides clear overall assessment
- ✓ Identifies specific, relevant strengths and concerns
- ✓ Supports findings with specific numbers/ratios
- ✓ Professional formatting and tone
- ✓ Actionable insights

---

### Scenario 2: Ratio Calculation & Interpretation

**Objective:** Test comprehensive ratio calculation and interpretation

**Input:**
- Complete financial statements (2 periods for comparison)
- Request for ratio analysis

**Invocation Prompt:**
```
"Calculate comprehensive financial ratios (liquidity, profitability, efficiency, leverage) 
and interpret what they tell us about this company's financial position."
```

**Expected Output:**
- 15+ financial ratios calculated correctly
- Ratios organized by category (liquidity, profitability, etc.)
- Interpretation of each ratio
- Comparison to benchmarks where applicable
- Trend analysis (current vs. prior period)

**Success Criteria:**
- ✓ Accurate ratio calculations
- ✓ Proper formulas used
- ✓ Clear interpretation of each ratio
- ✓ Identifies which ratios are strong vs. weak
- ✓ Organized presentation

---

### Scenario 3: Red Flag Identification

**Objective:** Test ability to identify financial warning signs

**Input:**
- Financial statements with planted red flags:
  - Declining gross margins
  - Rising DSO
  - Cash flow < net income
  - High customer concentration

**Invocation Prompt:**
```
"Identify any financial red flags in these statements. What concerns should management 
be aware of?"
```

**Expected Output:**
- Identifies all major red flags
- Assigns severity levels (Critical/High/Medium/Low)
- Explains why each is a concern
- Quantifies impact where possible
- Recommends corrective actions

**Success Criteria:**
- ✓ Catches all planted red flags
- ✓ Appropriate severity assessments
- ✓ Clear explanations
- ✓ Actionable recommendations
- ✓ No false positives

---

## INTERMEDIATE TEST SCENARIOS

### Scenario 4: Variance Analysis

**Objective:** Test budget vs. actual variance analysis capabilities

**Input:**
- Actual P&L results
- Budgeted P&L
- Request for variance analysis

**Invocation Prompt:**
```
"Perform comprehensive variance analysis for Q3 results vs. budget. Identify material 
variances, explain drivers, and recommend corrective actions."
```

**Expected Output:**
- Line-by-line variance analysis
- Identification of material variances (>5%)
- Favorable vs. unfavorable designation
- Root cause analysis for each material variance
- Specific recommendations for unfavorable variances
- Variance bridge/waterfall visualization

**Success Criteria:**
- ✓ Accurate variance calculations
- ✓ Correct favorable/unfavorable designation
- ✓ Identifies material vs. immaterial variances
- ✓ Plausible explanations for variances
- ✓ Actionable recommendations

---

### Scenario 5: Profitability Deep Dive

**Objective:** Test deep profitability analysis capabilities

**Input:**
- Financial statements with product/customer detail
- Gross margin, operating margin trends

**Invocation Prompt:**
```
"Conduct a detailed profitability analysis. Where are we making money? Where are we 
losing money? Why are margins declining?"
```

**Expected Output:**
- Gross margin analysis with trends
- Operating margin analysis
- Margin decomposition (product, customer, channel if data available)
- Root cause analysis for margin changes
- Comparison to industry benchmarks
- Margin improvement recommendations with expected impact

**Success Criteria:**
- ✓ Comprehensive margin analysis
- ✓ Identifies margin drivers
- ✓ Root cause determination
- ✓ Quantified improvement opportunities
- ✓ Prioritized recommendations

---

### Scenario 6: Cash Flow Analysis

**Objective:** Test cash flow and working capital analysis

**Input:**
- Cash flow statement
- Balance sheet with A/R, inventory, A/P details
- Income statement

**Invocation Prompt:**
```
"Analyze our cash flow and working capital. Why is our cash balance declining despite 
profitable operations? What should we do about it?"
```

**Expected Output:**
- Operating cash flow analysis
- Free cash flow calculation
- Working capital trend analysis
- Cash conversion cycle calculation
- DSO, DIO, DPO analysis
- Reconciliation of net income to cash flow
- Specific recommendations for improvement

**Success Criteria:**
- ✓ Identifies cash flow issues accurately
- ✓ Explains profit vs. cash divergence
- ✓ Calculates working capital metrics correctly
- ✓ Identifies improvement opportunities
- ✓ Quantifies potential cash impact

---

### Scenario 7: KPI Framework Development

**Objective:** Test ability to develop relevant KPI frameworks

**Input:**
- Company description with industry, size, stage
- Financial statements
- Request for KPI framework

**Invocation Prompt:**
```
"Develop a comprehensive KPI framework for our SaaS business. What metrics should we 
track monthly/quarterly?"
```

**Expected Output:**
- 15-20 relevant KPIs organized by category
- KPI definitions and calculation methods
- Target ranges for each KPI
- Monitoring frequency recommendations
- Leading vs. lagging indicator classification
- Dashboard design recommendations

**Success Criteria:**
- ✓ Industry-appropriate KPIs
- ✓ Mix of financial and operational metrics
- ✓ Clear definitions
- ✓ Realistic targets
- ✓ Actionable framework

---

## ADVANCED TEST SCENARIOS

### Scenario 8: Multi-Period Trend Analysis

**Objective:** Test trend analysis over multiple periods

**Input:**
- Financial statements for 8 quarters
- Request for trend analysis

**Invocation Prompt:**
```
"Analyze financial trends over the past 2 years. What patterns emerge? Are trends 
improving or deteriorating? What's driving the changes?"
```

**Expected Output:**
- Revenue trend analysis with growth rates
- Margin trend analysis
- Cash flow trends
- Ratio trends over time
- Pattern identification (seasonal, cyclical, structural)
- Performance attribution (what's driving changes)
- Forward-looking perspective

**Success Criteria:**
- ✓ Identifies meaningful trends
- ✓ Distinguishes signal from noise
- ✓ Explains trend drivers
- ✓ Visualizes trends effectively
- ✓ Forward-looking insights

---

### Scenario 9: Industry Benchmarking

**Objective:** Test benchmarking against industry standards

**Input:**
- Company financial statements
- Industry sector specified
- Request for competitive analysis

**Invocation Prompt:**
```
"How do our financial metrics compare to industry benchmarks? Where are we 
overperforming or underperforming? What explains the gaps?"
```

**Expected Output:**
- Key metrics compared to industry benchmarks
- Identification of overperformance areas
- Identification of underperformance areas
- Gap analysis with quantification
- Explanations for gaps (structural, strategic, operational)
- Recommendations to close gaps

**Success Criteria:**
- ✓ Uses appropriate industry benchmarks
- ✓ Accurate gap calculations
- ✓ Thoughtful explanations
- ✓ Distinguishes strategic from operational gaps
- ✓ Realistic improvement recommendations

---

### Scenario 10: Comprehensive Financial Model

**Objective:** Test financial modeling capabilities

**Input:**
- Historical financial statements (3 years)
- Growth assumptions and strategic initiatives
- Request for forward-looking model

**Invocation Prompt:**
```
"Build a 3-year financial model with base/upside/downside scenarios. Include revenue 
drivers, cost structure assumptions, and cash flow projections."
```

**Expected Output:**
- Integrated 3-statement model (P&L, BS, CF)
- Base case scenario with detailed assumptions
- Upside scenario with different assumptions
- Downside scenario
- Sensitivity analysis on key drivers
- Key metrics dashboard
- Assumption documentation

**Success Criteria:**
- ✓ Statements integrate properly (balance!)
- ✓ Realistic assumptions
- ✓ Clear scenario differentiation
- ✓ Comprehensive but not overly complex
- ✓ Actionable insights from scenarios

---

### Scenario 11: Root Cause Analysis

**Objective:** Test deep diagnostic capabilities

**Input:**
- Financial statements showing declining performance
- Request for root cause analysis

**Invocation Prompt:**
```
"Our EBITDA margin has declined from 25% to 18% over the past 2 years. Perform a root 
cause analysis. What's driving the deterioration and what should we do about it?"
```

**Expected Output:**
- Margin bridge showing changes
- Decomposition of margin decline into components:
  - Revenue mix effects
  - Pricing effects
  - Cost inflation
  - Volume/scale effects
  - Operating leverage
- Quantification of each factor's contribution
- Root cause determination
- Prioritized corrective actions

**Success Criteria:**
- ✓ Comprehensive decomposition
- ✓ Accurate attribution
- ✓ Identifies true root causes vs. symptoms
- ✓ Quantifies each driver
- ✓ Actionable recommendations

---

### Scenario 12: Strategic Financial Analysis

**Objective:** Test strategic financial planning capabilities

**Input:**
- Current financial position
- Strategic initiative details (product expansion, market entry, etc.)
- Request for financial analysis

**Invocation Prompt:**
```
"We're considering launching a new product line requiring $5M investment. Analyze the 
financial implications: expected ROI, payback period, impact on key metrics, and risks."
```

**Expected Output:**
- Investment analysis (NPV, IRR, payback)
- Impact on financial statements
- Impact on key metrics (margins, cash flow, etc.)
- Scenario analysis (success vs. failure)
- Risk assessment
- Go/no-go recommendation with supporting rationale

**Success Criteria:**
- ✓ Comprehensive investment analysis
- ✓ Realistic assumptions
- ✓ Multiple scenario consideration
- ✓ Risk-adjusted perspective
- ✓ Clear recommendation

---

## INDUSTRY-SPECIFIC TEST SCENARIOS

### Scenario 13: SaaS Metrics Analysis

**Objective:** Test SaaS-specific metric calculations

**Input:**
- SaaS company financial data
- Subscription metrics (ARR, churn, expansion, etc.)

**Invocation Prompt:**
```
"Calculate and analyze our SaaS metrics: ARR growth, NRR, GRR, CAC, LTV, CAC payback, 
Rule of 40, and Magic Number. How healthy is our business?"
```

**Expected Output:**
- All requested metrics calculated correctly
- Interpretation of each metric
- Comparison to SaaS benchmarks
- Assessment of business health
- Identification of strengths and weaknesses
- Specific recommendations for improvement

**Success Criteria:**
- ✓ Accurate SaaS metric calculations
- ✓ Proper formulas and definitions
- ✓ Appropriate benchmarking
- ✓ Holistic assessment
- ✓ SaaS-relevant recommendations

---

### Scenario 14: Retail Operations Analysis

**Objective:** Test retail-specific analysis

**Input:**
- Retail company financials
- Store-level data if available

**Invocation Prompt:**
```
"Analyze our retail operations: same-store sales growth, inventory turnover, gross 
margins, and working capital efficiency. What's working and what needs improvement?"
```

**Expected Output:**
- Same-store sales analysis
- Inventory turnover and aging
- Gross margin analysis
- Working capital metrics
- Store productivity metrics
- Retail-specific recommendations

**Success Criteria:**
- ✓ Retail-appropriate analysis
- ✓ Accurate calculations
- ✓ Operational insights
- ✓ Actionable recommendations
- ✓ Industry context

---

## EDGE CASE TEST SCENARIOS

### Scenario 15: Incomplete Data

**Objective:** Test handling of incomplete data

**Input:**
- Financial statements with missing line items
- Some periods missing

**Invocation Prompt:**
```
"Analyze these financial statements. Note: some data is missing."
```

**Expected Output:**
- Analysis of available data
- Clear notation of missing data
- Limitations acknowledged
- Recommendations for additional data
- Qualifications on conclusions

**Success Criteria:**
- ✓ Doesn't fabricate missing data
- ✓ Clearly states limitations
- ✓ Provides value despite gaps
- ✓ Identifies critical missing items
- ✓ Professional handling

---

### Scenario 16: Turnaround Situation

**Objective:** Test analysis of distressed situation

**Input:**
- Declining revenue, negative margins
- Negative cash flow, liquidity concerns

**Invocation Prompt:**
```
"This company is in distress. Perform a diagnostic analysis and develop a turnaround 
roadmap."
```

**Expected Output:**
- Assessment of severity
- Root cause diagnosis
- Prioritized turnaround initiatives
- Financial projections with turnaround
- Funding needs assessment
- Timeline and milestones

**Success Criteria:**
- ✓ Realistic assessment
- ✓ Prioritized actions
- ✓ Feasible turnaround plan
- ✓ Considers liquidity constraints
- ✓ Actionable roadmap

---

### Scenario 17: High-Growth Company

**Objective:** Test analysis of high-growth, unprofitable company

**Input:**
- 100% YoY revenue growth
- Negative EBITDA
- High burn rate

**Invocation Prompt:**
```
"We're growing 100% YoY but burning $3M/month. Analyze our path to profitability, 
cash runway, and growth sustainability."
```

**Expected Output:**
- Growth sustainability assessment
- Unit economics analysis
- Path to profitability modeling
- Cash runway calculation
- Capital needs assessment
- Growth vs. profitability tradeoffs

**Success Criteria:**
- ✓ Appropriate for high-growth context
- ✓ Focus on unit economics
- ✓ Realistic profitability path
- ✓ Clear cash runway analysis
- ✓ Strategic perspective

---

## TESTING CHECKLIST

Use this checklist when testing the skill:

### Core Capabilities
- [ ] Basic financial statement analysis
- [ ] Ratio calculation and interpretation
- [ ] Red flag identification
- [ ] Variance analysis
- [ ] Profitability analysis
- [ ] Cash flow analysis
- [ ] Working capital analysis
- [ ] KPI framework development
- [ ] Trend analysis
- [ ] Benchmarking
- [ ] Financial modeling
- [ ] Strategic financial analysis

### Quality Attributes
- [ ] Accuracy of calculations
- [ ] Appropriate analysis depth
- [ ] Clear communication
- [ ] Professional formatting (Arial font)
- [ ] Actionable recommendations
- [ ] Industry-appropriate insights
- [ ] Appropriate for company size/stage
- [ ] Balanced perspective

### Output Quality
- [ ] Executive-ready presentation
- [ ] Comprehensive yet concise
- [ ] Well-structured reports
- [ ] Professional charts/tables
- [ ] Clear prioritization
- [ ] Quantified impacts
- [ ] Implementation roadmaps

---

## Success Metrics

Overall success criteria for the Elite FP&A Professional skill:

1. **Accuracy:** 95%+ accuracy on financial calculations and ratios
2. **Relevance:** Analysis addresses the specific question asked
3. **Insight:** Goes beyond numbers to provide strategic insights
4. **Clarity:** Findings clearly communicated for executive audience
5. **Actionability:** Recommendations are specific and implementable
6. **Professionalism:** Output quality suitable for board/investor consumption
7. **Adaptability:** Works across industries and company sizes
8. **Completeness:** Addresses all aspects of request comprehensively

---

*Test systematically across basic, intermediate, and advanced scenarios to ensure comprehensive validation.*

