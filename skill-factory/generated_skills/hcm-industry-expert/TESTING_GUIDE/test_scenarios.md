# Test Scenarios for HCM Industry Expert

## Basic Scenarios

### Scenario 1: GTM Structure Analysis with Word and Markdown Output
**Input:** Request for GTM structure analysis with sales performance data (25 AEs, 65% quota attainment, 9-month sales cycle, $150K ACV)
**Expected Output:** Word document and Markdown file with GTM analysis, benchmark comparisons, and optimization recommendations
**Success Criteria:** 
- Word document generated with correct formatting (Arial font, wide margins 1.5 inches, table of contents, clear headers)
- Markdown file generated with proper formatting (heading hierarchy, bold formatting for key insights)
- Industry benchmarks included (quota attainment 70-85%, sales cycle 3-9 months by segment) with bold formatting
- Three specific optimization recommendations provided with bold formatting for emphasis
- Recommendations are actionable and quantified
- High-value strategic insights are bolded in both formats
- No DCF or valuation frameworks applied (GTM analysis use case)

### Scenario 2: Process Improvement Analysis
**Input:** User describes current recruiting process, requests best practices and improvement recommendations
**Expected Output:** Word document and Markdown file analyzing current process, comparing to best practices, providing recommendations
**Success Criteria:**
- Current process properly analyzed
- Best practices identified from HCM industry knowledge
- Gap analysis completed
- Specific, actionable recommendations provided with bold formatting
- Quantified improvements (time reduction, cost savings, efficiency gains) bolded
- Word document formatted correctly (Arial font, wide margins, TOC, headers)
- Markdown file formatted correctly (heading hierarchy, bold formatting)
- No DCF or valuation frameworks applied (process improvement use case)

### Scenario 3: Competitive Landscape Analysis
**Input:** Request for competitive landscape analysis of mid-market talent acquisition platforms
**Expected Output:** PowerPoint deck with competitive analysis, vendor positioning, and opportunity identification
**Success Criteria:**
- Competitive landscape mapped (suite players vs. point solutions)
- Key vendors analyzed (iCIMS, Greenhouse, Lever, etc.)
- Market positioning assessed
- White space opportunities identified
- PowerPoint formatted correctly
- Strategic frameworks applied (Porter's Five Forces, Strategic Group mapping)

## Intermediate Scenarios

### Scenario 4: Forward-Looking Strategic Analysis
**Input:** Request for market opportunity analysis in HCM space with 3-5 year outlook
**Expected Output:** PowerPoint deck with strategic analysis, market trends, and capitalization opportunities
**Success Criteria:**
- Market trends identified and analyzed (AI integration, skills-based hiring, etc.)
- Opportunities clearly articulated with timeline projections
- Strategic recommendations provided
- PowerPoint formatted correctly
- Appropriate frameworks applied (market sizing, competitive analysis - not DCF unless valuation requested)

### Scenario 5: Enterprise Software Company Analysis with Valuation
**Input:** Request for comprehensive analysis of HCM vendor including valuation (M&A target with $25M ARR)
**Expected Output:** PowerPoint deck with company analysis AND DCF/valuation framework (only because valuation was explicitly requested)
**Success Criteria:**
- Company analysis includes market positioning, competitive dynamics, financial analysis
- DCF valuation included ONLY because valuation was explicitly requested
- Comparable company analysis included
- PowerPoint formatted correctly
- All frameworks applied contextually

### Scenario 6: Sales Process Optimization
**Input:** Sales cycle analysis request (6 months vs. 4-month industry average)
**Expected Output:** PowerPoint deck with pipeline analysis, benchmark comparison, and cycle compression recommendations
**Success Criteria:**
- Pipeline stages analyzed
- Industry benchmarks compared (sales cycle 3-9 months by segment)
- Specific tactics provided based on proven HCM vendor playbooks
- PowerPoint formatted correctly
- Process improvement frameworks applied (not valuation frameworks)

## Advanced Scenarios

### Scenario 7: Multi-Framework Analysis
**Input:** Request for market entry strategy with build/buy/partner decision
**Expected Output:** PowerPoint deck with strategic analysis combining multiple frameworks
**Success Criteria:**
- Market sizing framework applied (TAM/SAM/SOM)
- Competitive analysis framework applied
- Build/buy/partner decision framework applied
- Financial implications quantified
- PowerPoint formatted correctly
- No DCF unless valuation explicitly requested

### Scenario 8: Channel Strategy Analysis
**Input:** Request to assess channel partner vs. direct sales strategy
**Expected Output:** PowerPoint deck with channel strategy analysis and recommendations
**Success Criteria:**
- Channel partner economics analyzed
- Direct sales economics analyzed
- Optimal mix recommended
- Industry examples cited (what similar vendors have done)
- PowerPoint formatted correctly
- Strategic frameworks applied appropriately

## Edge Cases to Verify

- **Contextual framework selection**: DCF only used when valuation explicitly requested
- **Process improvement workflow**: Accepts current process description, compares to best practices
- **Word/Markdown formatting**: Consistent formatting across all scenarios (Arial font, wide margins, TOC, bold formatting for insights)
- **Emerging vendors**: Ability to analyze new or niche market players
- **Cross-industry analysis**: HCM insights applied to related industries
- **Vertical-specific analysis**: Healthcare, retail, manufacturing vertical expertise
- **Geographic analysis**: NA, EMEA, APAC market dynamics

## Common Issues and Solutions

- **Issue:** DCF included when not needed for process improvement
  **Solution:** Skill must check use case before applying valuation frameworks - only use DCF when valuation explicitly requested

- **Issue:** Word/Markdown formatting inconsistent
  **Solution:** Always use word_report_generator.py - verify Arial font, wide margins (1.5 inches), table of contents, clear headers, bold formatting for high-value insights

- **Issue:** Process improvement recommendations too generic
  **Solution:** Compare current process to specific HCM industry best practices from references, provide quantified improvements with specific metrics

- **Issue:** Missing industry benchmarks
  **Solution:** Reference hcm-industry-landscape.md for specific benchmarks (quota attainment 70-85%, win rates 20-30% enterprise/40-50% mid-market, sales cycle 3-9 months)

- **Issue:** High-value insights not bolded
  **Solution:** Ensure all key strategic insights, important metrics, critical recommendations are bolded in both Word and Markdown formats using word_report_generator.py formatting functions

