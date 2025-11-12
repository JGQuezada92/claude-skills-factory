---
name: global-market-liquidity-analyst
description: This skill should be used when conducting comprehensive market liquidity analysis following Michael Howell's CrossBorder Capital methodology. The skill performs global liquidity cycle identification, central bank balance sheet analysis, cross-border capital flow tracking, monetary aggregates analysis, debt-liquidity interdependence assessment, collateral market health monitoring, liquidity-asset price correlation analysis, and forward-looking liquidity forecasts. The skill generates Excel models with liquidity calculations and charts, written analysis reports in Microsoft Word (.docx) format, and visualizations suitable for portfolio managers and investment committees.
license: Complete terms in LICENSE.txt
---

# Global Market Liquidity Analyst

## Overview

This skill enables comprehensive market liquidity analysis following the methodology developed by Michael Howell of CrossBorder Capital. The skill identifies and tracks 60-65 month global liquidity cycles, analyzes central bank balance sheets and monetary policy actions, monitors cross-border capital flows, tracks monetary aggregates across major economies, assesses debt-liquidity interdependence, evaluates collateral market health, and analyzes the relationship between liquidity conditions and asset prices. The skill generates professional Excel models with calculations and visualizations, comprehensive written analysis reports, and forward-looking liquidity forecasts with cycle positioning and asset price implications.

## When to Use This Skill

This skill should be invoked when:

- Analyzing global liquidity conditions and cycle positioning across major economies
- Assessing central bank policy actions and their liquidity implications
- Tracking monetary aggregates (M0, M1, M2, M3) and money supply growth rates
- Monitoring cross-border capital flows and FX liquidity conditions
- Evaluating debt-liquidity interdependence and refinancing risks
- Assessing collateral market health (bond volatility, repo spreads, margin requirements)
- Analyzing the relationship between liquidity conditions and asset prices
- Generating forward-looking liquidity forecasts and cycle turning point predictions
- Creating comprehensive liquidity analysis reports for investment committees
- Building Excel models for liquidity cycle tracking and analysis

The skill handles inputs including central bank balance sheet data, monetary aggregates time series, cross-border capital flow data, market data (bond yields, equity prices, FX rates), economic indicators, and central bank policy statements.

## How to Use This Skill

### Step 1: Gather and Prepare Input Data

Collect relevant data sources for analysis:

- Central bank balance sheet data: Obtain time series data from Federal Reserve, ECB, BOJ, PBOC, and other major central banks. Include total assets, QE/QT program sizes, policy rate changes, and forward guidance statements
- Monetary aggregates data: Collect M0, M1, M2, M3 data from central banks and statistical agencies across major economies. Ensure consistent definitions and time periods
- Cross-border capital flow data: Gather data from BIS, IMF, and central banks on international capital flows, reserve currency holdings, and FX liquidity conditions
- Market data: Obtain bond yields, equity prices, FX rates, and commodity prices with appropriate time series coverage
- Economic indicators: Collect GDP, inflation, credit growth, and money velocity data

Organize data in Excel format with clear date columns, source citations, and data quality notes. Ensure all data includes timestamps and source references.

### Step 2: Identify Global Liquidity Cycle Phase

Analyze historical liquidity data to identify the current cycle phase:

- Review historical liquidity cycles dating back at least 10-15 years to establish cycle patterns
- Calculate cycle duration and identify 60-65 month average cycle length
- Determine current cycle start date and elapsed time
- Identify current phase: expansion, peak, contraction, or trough
- Compare current positioning to historical norms and similar cycle phases
- Calculate cycle completion percentage and forecasted turning points

Use scripts/liquidity_cycle_analyzer.py to perform quantitative cycle identification and phase determination. Apply Michael Howell's framework for cycle phase classification based on liquidity growth rates, central bank actions, and market indicators.

### Step 3: Analyze Central Bank Balance Sheets

Examine major central bank balance sheets and policy actions:

- Analyze Federal Reserve balance sheet: Track total assets, QE/QT program implementation, policy rate changes, and forward guidance
- Analyze ECB balance sheet: Review asset purchase programs, policy rate settings, and liquidity provision mechanisms
- Analyze BOJ balance sheet: Assess quantitative easing programs, yield curve control, and policy stance
- Analyze PBOC balance sheet: Review reserve requirements, liquidity injections, and policy rate adjustments
- Calculate aggregate central bank balance sheet changes and their liquidity implications
- Assess policy divergence and coordination across central banks

Use scripts/central_bank_analyzer.py to calculate balance sheet changes, QE/QT flows, and policy impact assessments. Create visualizations showing balance sheet evolution over time.

### Step 4: Track Monetary Aggregates

Analyze money supply metrics across major economies:

- Calculate M0 (base money) growth rates and trends across major economies
- Analyze M1 (narrow money) growth and velocity changes
- Track M2 (broad money) growth rates, velocity, and credit creation
- Review M3 (extended broad money) where available
- Compare monetary aggregate growth rates across economies
- Assess velocity of money trends and their implications
- Calculate credit creation rates and their relationship to liquidity

Use scripts/monetary_aggregates_analyzer.py to perform calculations, generate growth rate comparisons, and create visualizations. Distinguish between different monetary aggregates and their liquidity implications.

### Step 5: Monitor Cross-Border Capital Flows

Assess international liquidity flows and FX conditions:

- Track cross-border capital flows from BIS and IMF data
- Analyze reserve currency dynamics and central bank reserve accumulation
- Monitor FX liquidity conditions and swap line usage
- Assess international liquidity transmission mechanisms
- Evaluate cross-border banking flows and their liquidity impact
- Review currency swap arrangements and their effectiveness

Document cross-border flow patterns and their relationship to domestic liquidity conditions. Identify periods of liquidity stress or abundance based on flow patterns.

### Step 6: Assess Debt-Liquidity Interdependence

Analyze the symbiotic relationship between debt and liquidity:

- Calculate total debt levels and refinancing requirements
- Assess debt rollover risks and liquidity needs for debt servicing
- Analyze the relationship between debt growth and liquidity creation
- Evaluate collateral quality and its impact on liquidity capacity
- Review debt-liquidity imbalances and potential stress points
- Assess the impact of debt servicing requirements on liquidity conditions

Use scripts/debt_liquidity_analyzer.py to calculate debt metrics, refinancing schedules, and liquidity needs. Identify periods where debt refinancing pressures may strain liquidity.

### Step 7: Evaluate Collateral Market Health

Monitor collateral markets to assess system liquidity capacity:

- Track bond market volatility and its impact on collateral quality
- Monitor repo market spreads and their relationship to liquidity conditions
- Assess margin requirements and their impact on leverage and liquidity
- Evaluate collateral quality indicators and their trends
- Review stress in collateral markets and potential liquidity constraints
- Analyze the relationship between collateral market health and broader liquidity conditions

Use scripts/collateral_analyzer.py to calculate volatility metrics, repo spreads, and collateral quality indicators. Identify periods of collateral market stress.

### Step 8: Analyze Liquidity-Asset Price Correlations

Examine the relationship between liquidity conditions and asset prices:

- Calculate correlations between liquidity measures and equity prices
- Analyze the relationship between liquidity and bond yields
- Assess liquidity impact on commodity prices and FX rates
- Identify liquidity-driven asset price movements
- Evaluate historical patterns of liquidity-asset price relationships
- Assess forward-looking asset price implications based on current liquidity conditions

Use scripts/asset_price_correlation_analyzer.py to perform correlation analysis and create visualizations. Distinguish between liquidity-driven moves and fundamental-driven moves.

### Step 9: Generate Forward-Looking Liquidity Forecast

Provide forward-looking assessment of liquidity conditions:

- Combine leading and lagging indicators to forecast liquidity trends
- Project cycle positioning and potential turning points
- Assess policy implications for future liquidity conditions
- Forecast cross-border flow patterns and their impact
- Project monetary aggregate growth based on policy actions
- Estimate asset price implications based on liquidity forecasts

Flag uncertainty in forward-looking projections and provide sensitivity analysis. Distinguish between high-confidence and low-confidence forecasts.

### Step 10: Create Excel Models and Visualizations

Generate comprehensive Excel workbooks with calculations and charts:

- Create liquidity cycle tracking worksheet with phase identification and turning point forecasts
- Build central bank balance sheet analysis worksheet with QE/QT calculations and policy impact metrics
- Develop cross-border flow model with capital flow tracking and FX liquidity analysis
- Construct monetary aggregates tracking worksheet with growth rates and velocity calculations
- Create asset price correlation analysis worksheet with correlation matrices and charts
- Generate summary dashboard with key liquidity metrics and cycle positioning

Use scripts/excel_model_generator.py to create Excel workbooks with formulas, charts, and formatting. Ensure all calculations are transparent and auditable.

**Output file naming:** Save the Excel model as `Global_Liquidity_Analysis_Model.xlsx` (this is the default filename in the script).

**Before finalizing the Excel model:**
- Use scripts/excel_model_generator.py's validate_excel_model() method to verify all formulas are correct
- Check that percent change formulas use correct cell references (e.g., =(B3/B2-1)*100 for MoM growth)
- Verify no division by zero errors exist in formulas
- Review the Validation worksheet that is automatically created to identify any calculation errors
- Manually verify key percent changes by recalculating: (current - previous) / previous * 100
- Fix any identified errors before proceeding to report generation

### Step 11: Generate Written Analysis Report

**REFERENCE: Review `references/example_report_structure.md` for the exact structure, content depth, and writing style required. Follow this example's format for Executive Summary, Table of Contents, historical cycles, PBOC section, asset recommendations, and risk monitoring alerts.**

Create professional liquidity analysis report with comprehensive content depth and investment-focused language:

**Report Structure (Required):**
1. Executive Summary (with BOTTOM LINE UP FRONT, Key Findings, Strategic Implications)
2. Table of Contents
3. Global Liquidity Cycle Assessment (with detailed historical context subsection)
4. Central Bank Balance Sheet Analysis (with subsections 2.1 Fed, 2.2 ECB, 2.3 BOJ, 2.4 PBOC)
5. Monetary Aggregates Review (with "Global M2: The Liquidity Paradox" subsection)
6. Cross-Border Capital Flows
7. Debt-Liquidity Interdependence (with detailed maturity wall analysis)
8. Collateral Market Health Assessment
9. Asset Price Implications (with "Specific Asset Class Recommendations" subsection)
10. Forward-Looking Liquidity Forecast
11. Risk Factors and Early Warning Indicators (with LEVEL 1/LEVEL 2 alerts)
12. Appendix: Data Sources and Methodology

**Detailed Section Requirements:**

1. **Executive Summary** - Must include:
   - **BOTTOM LINE UP FRONT:** One paragraph (1-2 sentences) summarizing critical inflection point and timing
   - **Key Findings:** Bullet list of 5-7 specific metrics with exact numbers and percentages (e.g., "G4 central bank assets: $26.0T, down 3.9% YoY", "Global M2: ~$96T growing 1.1% YoY", "Fed QT slowed from $95B/month to $30B/month")
   - **Strategic Implications for Investors:** Actionable positioning advice including:
     * Recommended strategy (e.g., "barbell strategy")
     * Specific asset positioning (late-cycle beneficiaries vs safe havens)
     * Timing guidance (e.g., "risk-on window closing but not yet shut")
     * Risk management actions (e.g., "reducing portfolio beta, taking profits")
   - Target length: 1,500-2,000 characters (comprehensive, not brief)

2. **Table of Contents** - Must include:
   - Immediately after Executive Summary
   - Numbered list of all 10-12 major sections
   - Example format: "1. Global Liquidity Cycle Assessment"

3. **Global Liquidity Cycle Assessment** - Must include:
   - Current cycle positioning with specific dates, elapsed time, and completion percentage
   - Detailed subsection "Historical Context: Learning from Past Cycles"
   - Must analyze at least 4 major liquidity cycles since 2008 GFC:
     * Cycle 1 (2009-2014): Duration, key events (QE1/QE2/QE3, taper tantrum), peak date, market impact (S&P 500 decline, EM currency impact)
     * Cycle 2 (2014-2019): Duration, key events (Fed QT, repo crisis), peak date, market impact
     * Cycle 3 (2019-2022): Duration, key events (COVID emergency, inflation surge), peak date, market impact (historic simultaneous stock/bond declines)
     * Cycle 4 (2022-Present): Current cycle analysis with bottom date, expansion drivers, and distinguishing characteristics
   - Each cycle description should be ~100 words with specific dates and market impacts
   - Total historical context section: ~400 words minimum
   - Include analogies to explain complex concepts (e.g., "ocean tides" analogy for liquidity cycles)

4. **Central Bank Balance Sheet Analysis** - Must include:
   - **Subsection 2.1 Federal Reserve:** Detailed QT pace changes with specific monthly amounts ($95B → $60B → $40B), bathtub analogy, forward outlook with specific timeline (e.g., "Q3-Q4 2026" for balance sheet stabilization)
   - **Subsection 2.2 European Central Bank:** Fragmentation risk analysis, TPI backstop, peripheral spread analysis (e.g., "Italian 10-year yields trading 140bps above German bunds"), forward outlook
   - **Subsection 2.3 Bank of Japan:** Carry trade unwind mechanism explanation, JGB yield analysis, fiscal dominance risk, forward outlook with specific projections (e.g., "¥50-80 trillion decline through 2026")
   - **Subsection 2.4 People's Bank of China: Targeted Stimulus Without Flood** (MANDATORY dedicated section):
     * Current balance sheet size and growth rate
     * RRR cuts and their impact (specific amounts and dates, e.g., "50bps in 2024-2025, releasing ~¥1 trillion")
     * MLF operations and outstanding amounts (e.g., "¥7.5 trillion outstanding")
     * Analysis of credit demand weakness (liquidity trap concept)
     * Fiscal stimulus projections with specific amounts (e.g., "$200-350 billion annually")
     * Forward outlook on policy direction
     * Explanation of China's unique approach (RRR vs balance sheet expansion)
     * Minimum length: ~400 words

5. **Monetary Aggregates Review** - Must include:
   - **Subsection "Global M2: The Liquidity Paradox":**
     * Explain the paradox: Central banks injected trillions, yet M2 growth is only 1.1% YoY (below 4-6% norm)
     * Identify where liquidity went ("trapped in financial system"):
       - Bank reserves at Fed (specific amount, e.g., "$3.3 trillion")
       - Treasury General Account (specific amount, e.g., "$750 billion")
       - Reverse Repo facility usage (current vs peak)
       - Money market fund assets (current level, e.g., "$6.5 trillion")
     * Quantify "dormant liquidity" (e.g., "$4-5 trillion of 'dormant' liquidity")
     * Use analogy to explain (e.g., "traffic jam" analogy)
   - Separate analysis of US M2, Euro Area M3, and China M2 with specific growth rates

6. **Debt-Liquidity Interdependence** - Must include:
   - **Subsection "The $7 Trillion Maturity Wall: The Single Biggest Risk":**
     * Total annual maturity amount ($7 trillion) and timeframe (2026-2027)
     * Breakdown by category:
       - US Treasuries: $2.2 trillion annually
       - European sovereigns: $1.8 trillion annually
       - Investment grade corporate: $1.2 trillion annually
       - High yield corporate: $400 billion annually
       - Emerging market sovereign and corporate: $800 billion annually
       - Real estate and structured finance: $600 billion annually
     * Explanation of "crowding out effect" mechanism
     * Simple example calculation (e.g., corporation refinancing $1B at 2% to 5.5% = tripled interest expense)
     * Identification of at-risk sectors:
       - Highly leveraged companies (zombie companies ~15% of US public companies)
       - Commercial real estate ($1.5T maturing into declining property values)
       - Emerging markets (facing higher rates and dollar strength)
       - Private credit markets ($600B at floating rates 3-5% above current)

7. **Asset Price Implications** - Must include:
   - **Subsection 7.1 The Liquidity-Asset Price Transmission Mechanism:** Explain lag times (Bitcoin 3-month, FX 3-month, Bonds 6-month, Equities 6-9 month, Gold immediate)
   - **Subsection 7.2 Specific Asset Class Recommendations** (MANDATORY - each asset class must have specific, actionable guidance):
     * **EQUITIES:** Specific action ("Take profits, add hedges"), positioning guidance (reduce beta to neutral), and hedging recommendations (put options, VIX calls, inverse ETFs). Include rationale (e.g., "S&P 500 gained over 50% from October 2022 bottom")
     * **GOLD:** Specific allocation target (e.g., "10-15% allocation"), price projection with timeframe (e.g., "$3,000-3,200/oz by Q2 2026"), and rationale (liquidity-crisis hedge, inflation hedge)
     * **BITCOIN/CRYPTO:** Specific timing guidance (peak Q4 2025-Q1 2026), expected correction magnitude (30-50%), and action ("Use strength to reduce exposure"). Explain 3-month lead time transmission mechanism
     * **BONDS:** Specific timing for duration extension (e.g., "starting Q3 2026"), positioning guidance (move from 2-year to 10-year Treasuries), and rationale (timing critical to avoid fighting the Fed)
   - Each asset class recommendation should be ~100-150 words with specific, actionable guidance

8. **Risk Factors and Early Warning Indicators** - Must include:
   - **Subsection "Critical Monitoring Indicators"** with two alert levels:
     * **LEVEL 1 ALERTS (Immediate attention required):**
       - TED Spread > 50bps (include current level, e.g., "current: 25bps")
       - SOFR-Fed Funds spread > 10bps (include current level, e.g., "current: 3bps")
       - VIX term structure inversion (describe current state, e.g., "current: normal contango")
       - High Yield OAS > 500bps (include current level, e.g., "current: 320bps")
     * **LEVEL 2 ALERTS (Elevated monitoring):**
       - 3-month consecutive decline in global M2 growth
       - US Treasury auction bid-to-cover ratios < 2.2x
       - Cross-currency basis swaps showing dollar funding stress
       - Systematic widening of EU peripheral spreads > 200bps
   - For each alert, provide: threshold value, current level, and significance explanation

9. **Forward-Looking Liquidity Forecast** - Must include:
   - Base Case Scenario (with probability, e.g., "60% probability")
   - Bull Case Scenario (with probability, e.g., "20% probability")
   - Bear Case Scenario (with probability, e.g., "20% probability")
   - Timeline with specific quarters and expected outcomes

**Content Quality Standards:**
- Use investment-focused language: "Take profits", "Reduce exposure", "Core holding", "Strategic positioning", "Barbell strategy"
- Include analogies and explanations to make complex concepts accessible (minimum 4-6 analogies throughout report)
- All central bank sections must include forward outlook projections with specific timelines
- Maintain analytical rigor while providing actionable investment guidance

**CRITICAL: Use scripts/word_report_generator.py to create the report as a Microsoft Word document (.docx format).**

1. **Import and use the Word generator:**
   ```python
   from word_report_generator import WordReportGenerator
   
   generator = WordReportGenerator()
   report_data = {
       'executive_summary': '...',
       'liquidity_cycle': '...',
       'central_bank_policy': '...',
       'cross_border_flows': '...',
       'monetary_aggregates': '...',
       'collateral_market': '...',
       'asset_price_implications': '...',
       'forward_looking_forecast': '...',
       'data_sources': ['Source 1', 'Source 2', ...]
   }
   
   output_path = generator.create_liquidity_report(report_data, 'Global_Liquidity_Analysis_Report.docx')
   ```

2. **Output file naming:** Save the Word report as `Global_Liquidity_Analysis_Report.docx` (this is the default filename in the script).

3. **Format requirements:**
   - Professional styling with Calibri font
   - Proper section headings (Heading 1, Heading 2)
   - Data tables with appropriate formatting
   - Charts and visualizations embedded where appropriate
   - All data sources cited with timestamps

**DO NOT create a Markdown (.md) file. The report MUST be delivered as a Word document suitable for investment committee review.**

**Before finalizing the report:**
- Verify all numerical values in the report match the source calculations from the analysis scripts
- Use scripts/output_validator.py's validate_report_numerical_accuracy() to cross-check numbers mentioned in text
- Manually verify all percent changes mentioned in the report by recalculating from source data
- Ensure growth rates are consistent (e.g., YoY growth should match cumulative MoM over 12 months within tolerance)
- Check that cycle phases described match the quantitative trend data
- Verify policy stance descriptions match balance sheet direction (expansive = growing, contractive = shrinking)

### Step 12: Validate All Calculations and Outputs

**CRITICAL STEP: Before delivering any outputs, validate all calculations and check for errors.**

Use scripts/output_validator.py to perform comprehensive validation:

1. **Validate Cycle Analysis:**
   - Run liquidity_cycle_analyzer.validate_output() on cycle analysis results
   - Verify cycle lengths are reasonable (55-70 months)
   - Check that cycle phase matches data trends (expansion = positive trend, contraction = negative trend)
   - Validate cycle completion percentage matches elapsed time / cycle length

2. **Validate Monetary Aggregates:**
   - Run monetary_aggregates_analyzer.validate_output() on aggregates analysis
   - Verify all percent change calculations are correct by manual recalculation
   - Check M0 ≤ M1 ≤ M2 ≤ M3 hierarchy is maintained
   - Validate velocity calculations are within reasonable range (0.5-15)
   - Ensure YoY growth rates match manual calculation: (current - 12m_ago) / 12m_ago * 100

3. **Validate Central Bank Analysis:**
   - Run central_bank_analyzer.validate_output() on balance sheet analysis
   - Verify YoY changes match manual calculations
   - Check policy stance consistency (expansive stance should match growing balance sheet)
   - Validate QE/QT identification matches balance sheet trends

4. **Validate Excel Formulas:**
   - Use excel_model_generator.validate_excel_model() before saving
   - Check for division by zero errors
   - Verify percent change formulas use correct cell references
   - Review Validation worksheet in Excel for flagged issues

5. **Validate Report Numerical Accuracy:**
   - Extract all numerical values from report text
   - Compare against source calculations from analysis scripts
   - Verify percent changes match source data calculations
   - Check for logical inconsistencies (e.g., expansion phase with negative growth)

6. **Cross-Check Consistency:**
   - Verify growth rates are consistent across time periods
   - Check that cycle phase descriptions match quantitative data
   - Ensure policy stance matches balance sheet direction
   - Validate correlations are between -1 and 1

7. **Fix Identified Errors:**
   - Correct any calculation errors found during validation
   - Update Excel formulas if incorrect
   - Revise report text if numerical values are wrong
   - Re-run validation after fixes to ensure errors are resolved

8. **Document Validation Results:**
   - Create a validation summary noting all checks performed
   - List any errors found and corrections made
   - Note confidence levels for key metrics
   - Include in Excel Validation worksheet or as appendix to report

**DO NOT proceed to final delivery until all validation errors are resolved. All warnings should be reviewed and addressed if they indicate potential issues.**

## Important Considerations

- Always use current, verifiable data sources with timestamps. Avoid using stale or unverified data
- Clearly distinguish between different liquidity measures (M2, M3, base money, etc.) and their specific implications
- Explicitly identify cycle phase and positioning with quantitative support
- Present both leading and lagging liquidity indicators to provide comprehensive view
- Cite all data sources and calculation methodologies for transparency
- Flag uncertainty in forward-looking projections and provide sensitivity analysis
- Handle multiple central bank data formats and time zones appropriately
- Distinguish between liquidity supply and demand in all analyses
- Maintain analytical objectivity and present balanced views of liquidity conditions
- Consider both domestic and international liquidity transmission mechanisms
- Account for shadow banking system and non-traditional liquidity creation
- Recognize that liquidity cycles can vary in duration and intensity across economies
- **ALWAYS validate all calculations before finalizing outputs**: Use scripts/output_validator.py and validate_output() methods on all analyzers to catch calculation errors and logical inconsistencies before delivery
- **Verify percent changes manually**: For any percent change reported, manually calculate (current - previous) / previous * 100 to ensure accuracy
- **Check for logical consistency**: Ensure cycle phases match data trends, policy stances match balance sheet directions, and growth rates are consistent across time periods
- **Review validation results**: Always review validation output from validate_output() methods and the Excel Validation worksheet before considering work complete

## Resources

- `scripts/liquidity_cycle_analyzer.py` - Performs quantitative cycle identification and phase determination based on historical liquidity data
- `scripts/central_bank_analyzer.py` - Calculates central bank balance sheet changes, QE/QT flows, and policy impact assessments
- `scripts/monetary_aggregates_analyzer.py` - Analyzes M0, M1, M2, M3 growth rates, velocity, and credit creation across major economies
- `scripts/debt_liquidity_analyzer.py` - Calculates debt metrics, refinancing schedules, and liquidity needs
- `scripts/collateral_analyzer.py` - Monitors collateral market health through volatility metrics, repo spreads, and quality indicators
- `scripts/asset_price_correlation_analyzer.py` - Performs correlation analysis between liquidity conditions and asset prices
- `scripts/excel_model_generator.py` - Creates comprehensive Excel workbooks with liquidity calculations, formulas, and charts (output: `Global_Liquidity_Analysis_Model.xlsx`)
- `scripts/word_report_generator.py` - Creates professional Word (.docx) reports with proper formatting and styling (output: `Global_Liquidity_Analysis_Report.docx`)
- `scripts/output_validator.py` - Validates calculations, logical consistency, and numerical accuracy for all outputs (MANDATORY before finalizing deliverables)
- `references/example_report_structure.md` - Example report structure showing required content depth, section organization, investment-focused language, and comprehensive analysis style (REFERENCE THIS WHEN GENERATING REPORTS)
- `references/michael_howell_framework.md` - Detailed explanation of Michael Howell's liquidity cycle framework and methodology
- `references/monetary_aggregates_definitions.md` - Definitions and calculations for M0, M1, M2, M3 monetary aggregates
- `references/central_bank_policy_tools.md` - Explanation of QE, QT, policy rates, forward guidance, and other central bank tools

## Keywords

liquidity analysis, market liquidity, liquidity cycles, Michael Howell, CrossBorder Capital, central bank balance sheets, monetary aggregates, M2, M3, quantitative easing, quantitative tightening, QE, QT, cross-border capital flows, FX liquidity, debt-liquidity interdependence, collateral markets, repo markets, bond volatility, liquidity-asset price correlation, liquidity forecasting, global liquidity, money supply, base money, velocity of money, credit creation, liquidity cycle phases, expansion, peak, contraction, trough, liquidity cycle identification, cycle positioning, liquidity forecasts, Federal Reserve, ECB, BOJ, PBOC, central bank policy, monetary policy, liquidity conditions, asset prices, liquidity analysis report

