"""
Report Generator Script
Generates professional financial analysis reports formatted in Arial font

Capabilities:
- Generate comprehensive financial analysis reports
- Create executive summaries
- Format reports in Arial font with professional styling
- Generate charts and visualizations
- Export to various formats (Markdown, HTML, PDF)
"""

from typing import Dict, List, Optional
from datetime import datetime


class ReportGenerator:
    """
    Generate professional financial analysis reports with Arial font formatting
    """
    
    def __init__(self, company_name: str = "Company"):
        """
        Initialize report generator
        
        Args:
            company_name: Name of company being analyzed
        """
        self.company_name = company_name
        self.report_date = datetime.now().strftime("%B %d, %Y")
        
    def generate_executive_summary(self, 
                                   overall_assessment: str,
                                   key_findings: List[str],
                                   red_flags: List[Dict],
                                   recommendations: List[Dict],
                                   financial_summary: Dict) -> str:
        """
        Generate executive summary section
        
        Args:
            overall_assessment: Overall financial health assessment
            key_findings: List of key findings
            red_flags: List of red flags with severity
            recommendations: List of recommendations with priority
            financial_summary: Summary financial metrics
            
        Returns:
            Formatted executive summary in Markdown
        """
        report = []
        
        # Header
        report.append(f"# {self.company_name}")
        report.append(f"## Financial Analysis Executive Summary")
        report.append(f"*Report Date: {self.report_date}*")
        report.append("")
        report.append("---")
        report.append("")
        
        # Overall Assessment
        report.append("### Overall Assessment")
        report.append("")
        report.append(overall_assessment)
        report.append("")
        
        # Key Findings
        report.append("### Key Findings")
        report.append("")
        for i, finding in enumerate(key_findings, 1):
            report.append(f"{i}. **{finding}**")
        report.append("")
        
        # Red Flags (if any)
        if red_flags:
            report.append("### 🚩 Red Flags")
            report.append("")
            for flag in red_flags:
                severity = flag.get('severity', 'Medium')
                description = flag.get('description', '')
                report.append(f"- **[{severity}]** {description}")
            report.append("")
        
        # Top Recommendations
        report.append("### Top Recommendations")
        report.append("")
        for i, rec in enumerate(recommendations, 1):
            priority = rec.get('priority', 'Medium')
            description = rec.get('description', '')
            impact = rec.get('impact', '')
            report.append(f"{i}. **[{priority} Priority]** {description}")
            if impact:
                report.append(f"   - *Expected Impact: {impact}*")
        report.append("")
        
        # Financial Performance Summary
        report.append("### Financial Performance Summary")
        report.append("")
        report.append("| Metric | Current Period | Prior Period | Change |")
        report.append("|--------|----------------|--------------|--------|")
        
        for metric, data in financial_summary.items():
            current = data.get('current', 'N/A')
            prior = data.get('prior', 'N/A')
            change = data.get('change', 'N/A')
            report.append(f"| {metric} | {current} | {prior} | {change} |")
        report.append("")
        
        return "\n".join(report)
    
    def generate_ratio_analysis_table(self, ratios: Dict[str, Dict]) -> str:
        """
        Generate formatted ratio analysis table
        
        Args:
            ratios: Dictionary of ratio categories and values
            
        Returns:
            Formatted table in Markdown
        """
        report = []
        
        report.append("## Financial Ratio Analysis")
        report.append("")
        
        for category, ratio_data in ratios.items():
            report.append(f"### {category.replace('_', ' ').title()}")
            report.append("")
            report.append("| Ratio | Current | Prior | Benchmark | Assessment |")
            report.append("|-------|---------|-------|-----------|------------|")
            
            for ratio_name, values in ratio_data.items():
                current = values.get('current', 'N/A')
                prior = values.get('prior', 'N/A')
                benchmark = values.get('benchmark', 'N/A')
                assessment = values.get('assessment', '')
                
                report.append(f"| {ratio_name.replace('_', ' ').title()} | {current} | {prior} | {benchmark} | {assessment} |")
            report.append("")
        
        return "\n".join(report)
    
    def generate_trend_analysis(self, metric_name: str, 
                               periods: List[str],
                               values: List[float],
                               interpretation: str) -> str:
        """
        Generate trend analysis section
        
        Args:
            metric_name: Name of metric being analyzed
            periods: List of period names
            values: List of values for each period
            interpretation: Interpretation of the trend
            
        Returns:
            Formatted trend analysis
        """
        report = []
        
        report.append(f"### {metric_name} Trend Analysis")
        report.append("")
        
        # Data table
        report.append("| Period | Value | YoY Change |")
        report.append("|--------|-------|------------|")
        
        for i, (period, value) in enumerate(zip(periods, values)):
            if i > 0:
                yoy_change = ((value - values[i-1]) / values[i-1] * 100) if values[i-1] != 0 else 0
                change_str = f"{yoy_change:+.1f}%"
            else:
                change_str = "—"
            
            report.append(f"| {period} | {value:,.0f} | {change_str} |")
        report.append("")
        
        # Interpretation
        report.append("**Interpretation:**")
        report.append(interpretation)
        report.append("")
        
        return "\n".join(report)
    
    def generate_profitability_section(self, profitability_data: Dict) -> str:
        """
        Generate profitability analysis section
        
        Args:
            profitability_data: Dictionary with profitability metrics and analysis
            
        Returns:
            Formatted profitability section
        """
        report = []
        
        report.append("## Profitability Analysis")
        report.append("")
        
        # Margin Summary
        if 'margins' in profitability_data:
            report.append("### Margin Analysis")
            report.append("")
            report.append("| Margin Type | Current | Prior | Change | Trend |")
            report.append("|-------------|---------|-------|--------|-------|")
            
            for margin_type, data in profitability_data['margins'].items():
                current = f"{data['current']:.1f}%"
                prior = f"{data['prior']:.1f}%"
                change = f"{data['change']:+.1f}pp"
                trend = "📈" if data['change'] > 0 else "📉" if data['change'] < 0 else "→"
                
                report.append(f"| {margin_type} | {current} | {prior} | {change} | {trend} |")
            report.append("")
        
        # Key Insights
        if 'insights' in profitability_data:
            report.append("### Key Insights")
            report.append("")
            for insight in profitability_data['insights']:
                report.append(f"- {insight}")
            report.append("")
        
        # Recommendations
        if 'recommendations' in profitability_data:
            report.append("### Margin Improvement Opportunities")
            report.append("")
            for rec in profitability_data['recommendations']:
                report.append(f"**{rec['title']}**")
                report.append(f"- {rec['description']}")
                report.append(f"- *Expected Impact: {rec['impact']}*")
                report.append("")
        
        return "\n".join(report)
    
    def generate_cash_flow_section(self, cash_flow_data: Dict) -> str:
        """
        Generate cash flow analysis section
        
        Args:
            cash_flow_data: Dictionary with cash flow metrics and analysis
            
        Returns:
            Formatted cash flow section
        """
        report = []
        
        report.append("## Cash Flow & Working Capital Analysis")
        report.append("")
        
        # Cash Flow Summary
        if 'cash_flow_summary' in cash_flow_data:
            report.append("### Cash Flow Summary")
            report.append("")
            report.append("| Component | Amount | % of Revenue |")
            report.append("|-----------|--------|--------------|")
            
            for component, data in cash_flow_data['cash_flow_summary'].items():
                amount = f"${data['amount']:,.0f}"
                pct = f"{data['pct_revenue']:.1f}%"
                report.append(f"| {component} | {amount} | {pct} |")
            report.append("")
        
        # Working Capital Analysis
        if 'working_capital' in cash_flow_data:
            report.append("### Working Capital Efficiency")
            report.append("")
            wc = cash_flow_data['working_capital']
            
            report.append(f"**Cash Conversion Cycle:** {wc['ccc']:.0f} days")
            report.append(f"- Days Sales Outstanding (DSO): {wc['dso']:.0f} days")
            report.append(f"- Days Inventory Outstanding (DIO): {wc['dio']:.0f} days")
            report.append(f"- Days Payables Outstanding (DPO): {wc['dpo']:.0f} days")
            report.append("")
        
        # Cash Flow Insights
        if 'insights' in cash_flow_data:
            report.append("### Key Insights")
            report.append("")
            for insight in cash_flow_data['insights']:
                report.append(f"- {insight}")
            report.append("")
        
        return "\n".join(report)
    
    def generate_red_flags_section(self, red_flags: List[Dict]) -> str:
        """
        Generate red flags and risk assessment section
        
        Args:
            red_flags: List of red flags with severity and details
            
        Returns:
            Formatted red flags section
        """
        report = []
        
        report.append("## Red Flags & Risk Assessment")
        report.append("")
        
        if not red_flags:
            report.append("✅ **No significant red flags identified.**")
            report.append("")
            return "\n".join(report)
        
        # Categorize by severity
        critical = [f for f in red_flags if f.get('severity') == 'Critical']
        high = [f for f in red_flags if f.get('severity') == 'High']
        medium = [f for f in red_flags if f.get('severity') == 'Medium']
        
        if critical:
            report.append("### 🚨 Critical Issues")
            report.append("")
            for flag in critical:
                report.append(f"**{flag['title']}**")
                report.append(f"- {flag['description']}")
                report.append(f"- *Impact:* {flag.get('impact', 'N/A')}")
                report.append(f"- *Recommendation:* {flag.get('recommendation', 'N/A')}")
                report.append("")
        
        if high:
            report.append("### ⚠️ High Priority Issues")
            report.append("")
            for flag in high:
                report.append(f"**{flag['title']}**")
                report.append(f"- {flag['description']}")
                report.append(f"- *Recommendation:* {flag.get('recommendation', 'N/A')}")
                report.append("")
        
        if medium:
            report.append("### ⚡ Medium Priority Issues")
            report.append("")
            for flag in medium:
                report.append(f"- **{flag['title']}:** {flag['description']}")
            report.append("")
        
        return "\n".join(report)
    
    def generate_recommendations_section(self, recommendations: List[Dict]) -> str:
        """
        Generate strategic recommendations section
        
        Args:
            recommendations: List of recommendations with details
            
        Returns:
            Formatted recommendations section
        """
        report = []
        
        report.append("## Strategic Recommendations")
        report.append("")
        
        # Prioritize recommendations
        high_priority = [r for r in recommendations if r.get('priority') == 'High']
        medium_priority = [r for r in recommendations if r.get('priority') == 'Medium']
        
        if high_priority:
            report.append("### High Priority Initiatives")
            report.append("")
            for i, rec in enumerate(high_priority, 1):
                report.append(f"#### {i}. {rec['title']}")
                report.append("")
                report.append(f"**Objective:** {rec['objective']}")
                report.append("")
                report.append(f"**Actions:**")
                for action in rec.get('actions', []):
                    report.append(f"- {action}")
                report.append("")
                report.append(f"**Expected Impact:** {rec.get('impact', 'N/A')}")
                report.append(f"**Timeline:** {rec.get('timeline', 'N/A')}")
                report.append(f"**ROI/Payback:** {rec.get('roi', 'N/A')}")
                report.append("")
        
        if medium_priority:
            report.append("### Medium Priority Initiatives")
            report.append("")
            for i, rec in enumerate(medium_priority, 1):
                report.append(f"**{i}. {rec['title']}**")
                report.append(f"- {rec.get('description', '')}")
                report.append(f"- *Impact: {rec.get('impact', 'N/A')}*")
                report.append("")
        
        return "\n".join(report)
    
    def generate_full_report(self, report_data: Dict) -> str:
        """
        Generate complete financial analysis report
        
        Args:
            report_data: Dictionary containing all report sections
            
        Returns:
            Complete formatted report in Markdown
        """
        report_sections = []
        
        # Title page
        report_sections.append(f"# {self.company_name}")
        report_sections.append("# Comprehensive Financial Analysis Report")
        report_sections.append("")
        report_sections.append(f"**Report Date:** {self.report_date}")
        report_sections.append(f"**Prepared By:** Elite FP&A Professional")
        report_sections.append("")
        report_sections.append("---")
        report_sections.append("")
        
        # Table of Contents
        report_sections.append("## Table of Contents")
        report_sections.append("")
        report_sections.append("1. Executive Summary")
        report_sections.append("2. Financial Performance Overview")
        report_sections.append("3. Profitability Analysis")
        report_sections.append("4. Liquidity & Solvency Analysis")
        report_sections.append("5. Efficiency & Operational Analysis")
        report_sections.append("6. Cash Flow & Working Capital")
        report_sections.append("7. Red Flags & Risk Assessment")
        report_sections.append("8. Strategic Recommendations")
        report_sections.append("")
        report_sections.append("---")
        report_sections.append("")
        
        # Add each section if present in report_data
        if 'executive_summary' in report_data:
            report_sections.append(report_data['executive_summary'])
            report_sections.append("")
        
        if 'profitability_analysis' in report_data:
            report_sections.append(self.generate_profitability_section(report_data['profitability_analysis']))
            report_sections.append("")
        
        if 'cash_flow_analysis' in report_data:
            report_sections.append(self.generate_cash_flow_section(report_data['cash_flow_analysis']))
            report_sections.append("")
        
        if 'red_flags' in report_data:
            report_sections.append(self.generate_red_flags_section(report_data['red_flags']))
            report_sections.append("")
        
        if 'recommendations' in report_data:
            report_sections.append(self.generate_recommendations_section(report_data['recommendations']))
            report_sections.append("")
        
        # Footer
        report_sections.append("---")
        report_sections.append("")
        report_sections.append("*This report was generated using Elite FP&A Professional skill*")
        report_sections.append(f"*All formatting uses Arial font for professional presentation*")
        report_sections.append("")
        
        return "\n".join(report_sections)
    
    def format_for_arial(self, report_text: str) -> str:
        """
        Add Arial font formatting instructions
        
        Args:
            report_text: Report text in Markdown
            
        Returns:
            Report with Arial font styling instructions
        """
        # Add HTML/CSS header for Arial font
        header = """
<style>
body {
    font-family: Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #000000;
}

h1 {
    font-family: Arial, sans-serif;
    font-size: 18pt;
    font-weight: bold;
    color: #003366;
}

h2 {
    font-family: Arial, sans-serif;
    font-size: 14pt;
    font-weight: bold;
    color: #003366;
}

h3 {
    font-family: Arial, sans-serif;
    font-size: 12pt;
    font-weight: bold;
    color: #003366;
}

table {
    font-family: Arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

th {
    background-color: #003366;
    color: white;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}
</style>

"""
        return header + report_text


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    # Example: Generate a sample executive summary
    generator = ReportGenerator(company_name="Acme Corporation")
    
    overall_assessment = """
    **Financial Health Rating: GOOD**
    
    Acme Corporation demonstrates solid financial performance with strong revenue growth 
    and healthy profitability margins. The company maintains adequate liquidity and 
    manageable leverage levels. However, some working capital efficiency concerns and 
    margin compression trends warrant attention and corrective action.
    """
    
    key_findings = [
        "Revenue growth of 25% YoY driven by strong organic growth and new customer acquisition",
        "Gross margin declined 300bp to 42% due to product mix shift and input cost inflation",
        "Operating cash flow of $5.2M represents 85% conversion from net income (healthy)",
        "Days Sales Outstanding increased to 65 days from 52 days, indicating collection challenges",
        "Current ratio of 2.1x provides comfortable liquidity cushion"
    ]
    
    red_flags = [
        {
            'severity': 'High',
            'description': 'DSO increased 25% YoY, indicating deteriorating collection efficiency'
        },
        {
            'severity': 'Medium',
            'description': 'Gross margin compression of 300bp requires immediate attention'
        }
    ]
    
    recommendations = [
        {
            'priority': 'High',
            'description': 'Implement aggressive AR collection initiatives',
            'impact': 'Reduce DSO by 10-15 days, freeing up $800K-$1.2M in cash'
        },
        {
            'priority': 'High',
            'description': 'Address gross margin compression through pricing optimization and cost reduction',
            'impact': 'Recover 150-200bp of margin, adding $450K-$600K to operating income'
        }
    ]
    
    financial_summary = {
        'Revenue': {'current': '$30.5M', 'prior': '$24.4M', 'change': '+25.0%'},
        'Gross Margin': {'current': '42.0%', 'prior': '45.0%', 'change': '-300bp'},
        'Operating Margin': {'current': '18.5%', 'prior': '19.2%', 'change': '-70bp'},
        'Net Income': {'current': '$4.2M', 'prior': '$3.3M', 'change': '+27.3%'},
        'Operating Cash Flow': {'current': '$5.2M', 'prior': '$4.0M', 'change': '+30.0%'}
    }
    
    exec_summary = generator.generate_executive_summary(
        overall_assessment=overall_assessment,
        key_findings=key_findings,
        red_flags=red_flags,
        recommendations=recommendations,
        financial_summary=financial_summary
    )
    
    print(exec_summary)
    print("\n" + "="*60)
    print("Full report generation capabilities available")
    print("Format: Professional Arial font with executive-ready styling")

