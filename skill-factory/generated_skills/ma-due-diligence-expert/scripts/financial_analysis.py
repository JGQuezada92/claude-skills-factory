"""
Financial Analysis Module for M&A Due Diligence

This module provides comprehensive financial analysis capabilities including:
- Quality of Earnings (QoE) analysis with normalization adjustments
- Working capital analysis and peg calculations
- SaaS metrics calculation (ARR, NRR, GRR, CAC, LTV, Rule of 40)
- Cash flow analysis and free cash flow generation
- Financial ratio analysis and benchmarking

Usage:
    from financial_analysis import FinancialAnalyzer
    
    analyzer = FinancialAnalyzer(financial_data)
    qoe_results = analyzer.quality_of_earnings_analysis()
    working_capital = analyzer.calculate_working_capital()
    saas_metrics = analyzer.calculate_saas_metrics()
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class FinancialAnalyzer:
    """
    Comprehensive financial analysis for M&A due diligence.
    """
    
    def __init__(self, financial_data: pd.DataFrame):
        """
        Initialize analyzer with financial statement data.
        
        Args:
            financial_data: DataFrame with financial statement line items by period
        """
        self.data = financial_data
        self.adjustments = []
        
    def quality_of_earnings_analysis(self, 
                                     one_time_items: List[Dict] = None,
                                     non_recurring: List[Dict] = None,
                                     related_party: List[Dict] = None) -> Dict:
        """
        Perform Quality of Earnings analysis with normalization adjustments.
        
        Args:
            one_time_items: List of one-time expense/revenue items
            non_recurring: List of non-recurring items
            related_party: List of related party transactions
            
        Returns:
            Dictionary with normalized EBITDA and adjustment details
        """
        results = {
            'reported_ebitda': {},
            'adjustments': [],
            'normalized_ebitda': {},
            'adjustment_summary': {}
        }
        
        # Calculate reported EBITDA by period
        for period in self.data.columns:
            revenue = self.data.loc['Revenue', period]
            cogs = self.data.loc['COGS', period] if 'COGS' in self.data.index else 0
            opex = self.data.loc['Operating Expenses', period] if 'Operating Expenses' in self.data.index else 0
            depreciation = self.data.loc['D&A', period] if 'D&A' in self.data.index else 0
            
            ebitda = revenue - cogs - opex + depreciation
            results['reported_ebitda'][period] = ebitda
        
        # Apply adjustments
        adjustment_categories = {
            'One-time Items': one_time_items or [],
            'Non-recurring': non_recurring or [],
            'Related Party': related_party or []
        }
        
        total_adjustments_by_period = {period: 0 for period in self.data.columns}
        
        for category, items in adjustment_categories.items():
            for item in items:
                adjustment = {
                    'category': category,
                    'description': item.get('description'),
                    'amount': item.get('amount'),
                    'period': item.get('period'),
                    'rationale': item.get('rationale')
                }
                results['adjustments'].append(adjustment)
                
                period = item.get('period')
                if period in total_adjustments_by_period:
                    total_adjustments_by_period[period] += item.get('amount', 0)
        
        # Calculate normalized EBITDA
        for period in self.data.columns:
            normalized = results['reported_ebitda'][period] + total_adjustments_by_period[period]
            results['normalized_ebitda'][period] = normalized
        
        # Adjustment summary
        results['adjustment_summary'] = {
            'total_adjustments': sum(total_adjustments_by_period.values()),
            'number_of_adjustments': len(results['adjustments']),
            'avg_adjustment_impact': sum(total_adjustments_by_period.values()) / len(total_adjustments_by_period) if total_adjustments_by_period else 0
        }
        
        return results
    
    def calculate_working_capital(self) -> Dict:
        """
        Calculate working capital metrics and normalized peg.
        
        Returns:
            Dictionary with working capital analysis
        """
        results = {
            'working_capital_by_period': {},
            'wc_as_percent_revenue': {},
            'normalized_wc_peg': 0,
            'day_1_funding_need': 0
        }
        
        for period in self.data.columns:
            # Calculate working capital components
            ar = self.data.loc['Accounts Receivable', period] if 'Accounts Receivable' in self.data.index else 0
            inventory = self.data.loc['Inventory', period] if 'Inventory' in self.data.index else 0
            prepaid = self.data.loc['Prepaid Expenses', period] if 'Prepaid Expenses' in self.data.index else 0
            ap = self.data.loc['Accounts Payable', period] if 'Accounts Payable' in self.data.index else 0
            accrued = self.data.loc['Accrued Liabilities', period] if 'Accrued Liabilities' in self.data.index else 0
            
            wc = ar + inventory + prepaid - ap - accrued
            results['working_capital_by_period'][period] = wc
            
            # Calculate as % of revenue
            revenue = self.data.loc['Revenue', period]
            results['wc_as_percent_revenue'][period] = (wc / revenue * 100) if revenue != 0 else 0
        
        # Calculate normalized working capital peg (average of last 3-4 quarters)
        wc_percentages = list(results['wc_as_percent_revenue'].values())
        results['normalized_wc_peg'] = np.mean(wc_percentages[-4:]) if len(wc_percentages) >= 4 else np.mean(wc_percentages)
        
        return results
    
    def calculate_saas_metrics(self, customer_data: pd.DataFrame = None) -> Dict:
        """
        Calculate comprehensive SaaS metrics.
        
        Args:
            customer_data: DataFrame with customer-level data for cohort analysis
            
        Returns:
            Dictionary with SaaS metrics
        """
        metrics = {}
        
        # ARR/MRR calculation
        if 'Subscription Revenue' in self.data.index:
            latest_period = self.data.columns[-1]
            quarterly_revenue = self.data.loc['Subscription Revenue', latest_period]
            metrics['ARR'] = quarterly_revenue * 4
            metrics['MRR'] = quarterly_revenue / 3
        
        # Calculate growth rates
        if len(self.data.columns) >= 2:
            current = self.data.loc['Revenue', self.data.columns[-1]]
            prior = self.data.loc['Revenue', self.data.columns[-2]]
            metrics['QoQ_growth'] = ((current / prior) - 1) * 100 if prior != 0 else 0
            
            if len(self.data.columns) >= 5:
                year_ago = self.data.loc['Revenue', self.data.columns[-5]]
                metrics['YoY_growth'] = ((current / year_ago) - 1) * 100 if year_ago != 0 else 0
        
        # Rule of 40 (growth rate + profit margin)
        if 'YoY_growth' in metrics:
            latest_period = self.data.columns[-1]
            revenue = self.data.loc['Revenue', latest_period]
            ebitda = self.data.loc['EBITDA', latest_period] if 'EBITDA' in self.data.index else 0
            ebitda_margin = (ebitda / revenue * 100) if revenue != 0 else 0
            metrics['Rule_of_40'] = metrics['YoY_growth'] + ebitda_margin
        
        # CAC and LTV (requires customer data)
        if customer_data is not None:
            metrics['CAC'] = self._calculate_cac(customer_data)
            metrics['LTV'] = self._calculate_ltv(customer_data)
            metrics['LTV_CAC_ratio'] = metrics['LTV'] / metrics['CAC'] if metrics['CAC'] != 0 else 0
            metrics['CAC_payback_months'] = self._calculate_cac_payback(customer_data)
        
        # Magic Number (ARR growth / S&M spend)
        if 'Sales & Marketing' in self.data.index and len(self.data.columns) >= 2:
            current_arr = metrics.get('ARR', 0)
            prior_period = self.data.columns[-2]
            prior_arr = self.data.loc['Subscription Revenue', prior_period] * 4 if 'Subscription Revenue' in self.data.index else 0
            arr_growth = current_arr - prior_arr
            
            sm_spend = self.data.loc['Sales & Marketing', self.data.columns[-1]]
            metrics['Magic_Number'] = arr_growth / sm_spend if sm_spend != 0 else 0
        
        return metrics
    
    def _calculate_cac(self, customer_data: pd.DataFrame) -> float:
        """Calculate Customer Acquisition Cost."""
        # Simplified calculation - would need actual customer acquisition data
        latest_period = self.data.columns[-1]
        sm_spend = self.data.loc['Sales & Marketing', latest_period] if 'Sales & Marketing' in self.data.index else 0
        new_customers = customer_data['New Customers'].sum() if 'New Customers' in customer_data.columns else 1
        return sm_spend / new_customers if new_customers > 0 else 0
    
    def _calculate_ltv(self, customer_data: pd.DataFrame) -> float:
        """Calculate Customer Lifetime Value."""
        # Simplified LTV calculation
        avg_revenue_per_customer = customer_data['Revenue'].mean() if 'Revenue' in customer_data.columns else 0
        avg_gross_margin = 0.75  # Typical SaaS gross margin
        avg_customer_lifetime_years = 5  # Assumption
        return avg_revenue_per_customer * avg_gross_margin * avg_customer_lifetime_years
    
    def _calculate_cac_payback(self, customer_data: pd.DataFrame) -> float:
        """Calculate CAC payback period in months."""
        cac = self._calculate_cac(customer_data)
        monthly_revenue_per_customer = customer_data['Revenue'].mean() / 12 if 'Revenue' in customer_data.columns else 0
        gross_margin = 0.75
        monthly_gross_profit = monthly_revenue_per_customer * gross_margin
        return cac / monthly_gross_profit if monthly_gross_profit > 0 else 0
    
    def calculate_cash_flow(self) -> Dict:
        """
        Calculate free cash flow and cash conversion metrics.
        
        Returns:
            Dictionary with cash flow analysis
        """
        results = {}
        
        for period in self.data.columns:
            ebitda = self.data.loc['EBITDA', period] if 'EBITDA' in self.data.index else 0
            capex = self.data.loc['Capex', period] if 'Capex' in self.data.index else 0
            wc_change = self.data.loc['WC Change', period] if 'WC Change' in self.data.index else 0
            taxes = self.data.loc['Cash Taxes', period] if 'Cash Taxes' in self.data.index else 0
            
            fcf = ebitda - capex - wc_change - taxes
            results[period] = {
                'EBITDA': ebitda,
                'Capex': capex,
                'WC_Change': wc_change,
                'Cash_Taxes': taxes,
                'Free_Cash_Flow': fcf,
                'FCF_Conversion': (fcf / ebitda * 100) if ebitda != 0 else 0
            }
        
        return results
    
    def validate_output(self) -> Dict:
        """
        Validate financial calculations for accuracy and consistency.
        
        Returns:
            Dictionary with validation results (errors, warnings, passed checks)
        """
        validation = {
            'errors': [],
            'warnings': [],
            'passed': []
        }
        
        # Check for negative margins
        for period in self.data.columns:
            revenue = self.data.loc['Revenue', period]
            ebitda = self.data.loc['EBITDA', period] if 'EBITDA' in self.data.index else 0
            margin = (ebitda / revenue * 100) if revenue != 0 else 0
            
            if margin < -50:
                validation['errors'].append(f"Period {period}: EBITDA margin {margin:.1f}% is unusually negative")
            elif margin < 0:
                validation['warnings'].append(f"Period {period}: Negative EBITDA margin {margin:.1f}%")
            else:
                validation['passed'].append(f"Period {period}: EBITDA margin {margin:.1f}% is reasonable")
        
        # Check for data consistency
        if 'Gross Profit' in self.data.index:
            for period in self.data.columns:
                revenue = self.data.loc['Revenue', period]
                cogs = self.data.loc['COGS', period] if 'COGS' in self.data.index else 0
                reported_gp = self.data.loc['Gross Profit', period]
                calculated_gp = revenue - cogs
                
                if abs(reported_gp - calculated_gp) / revenue > 0.01:  # >1% difference
                    validation['errors'].append(f"Period {period}: Gross Profit mismatch - reported {reported_gp:.0f}, calculated {calculated_gp:.0f}")
                else:
                    validation['passed'].append(f"Period {period}: Gross Profit reconciles")
        
        # Check for reasonable growth rates
        if len(self.data.columns) >= 2:
            for i in range(1, len(self.data.columns)):
                current = self.data.loc['Revenue', self.data.columns[i]]
                prior = self.data.loc['Revenue', self.data.columns[i-1]]
                growth = ((current / prior) - 1) * 100 if prior != 0 else 0
                
                if growth > 200:
                    validation['warnings'].append(f"Period {self.data.columns[i]}: Unusually high revenue growth of {growth:.1f}%")
                elif growth < -50:
                    validation['warnings'].append(f"Period {self.data.columns[i]}: Unusually large revenue decline of {growth:.1f}%")
        
        return validation


def generate_financial_summary(analyzer: FinancialAnalyzer) -> str:
    """
    Generate a text summary of financial analysis.
    
    Args:
        analyzer: FinancialAnalyzer instance with loaded data
        
    Returns:
        Formatted string with financial summary
    """
    summary = "FINANCIAL ANALYSIS SUMMARY\n"
    summary += "=" * 50 + "\n\n"
    
    # Get latest period metrics
    latest_period = analyzer.data.columns[-1]
    revenue = analyzer.data.loc['Revenue', latest_period]
    
    summary += f"Latest Period: {latest_period}\n"
    summary += f"Revenue: ${revenue:,.0f}\n"
    
    if 'EBITDA' in analyzer.data.index:
        ebitda = analyzer.data.loc['EBITDA', latest_period]
        margin = (ebitda / revenue * 100) if revenue != 0 else 0
        summary += f"EBITDA: ${ebitda:,.0f} ({margin:.1f}% margin)\n"
    
    # Calculate growth
    if len(analyzer.data.columns) >= 2:
        prior_period = analyzer.data.columns[-2]
        prior_revenue = analyzer.data.loc['Revenue', prior_period]
        growth = ((revenue / prior_revenue) - 1) * 100 if prior_revenue != 0 else 0
        summary += f"QoQ Growth: {growth:.1f}%\n"
    
    summary += "\n"
    return summary


# Example usage
if __name__ == "__main__":
    # Sample financial data
    data = {
        'Q1 2024': [10000, 2000, 6000, 500, 1500],
        'Q2 2024': [12000, 2200, 6500, 500, 2800],
        'Q3 2024': [14000, 2400, 7000, 500, 4100],
        'Q4 2024': [16000, 2600, 7500, 500, 5400]
    }
    
    df = pd.DataFrame(data, index=['Revenue', 'COGS', 'Operating Expenses', 'D&A', 'EBITDA'])
    
    analyzer = FinancialAnalyzer(df)
    
    # Quality of Earnings analysis
    adjustments = [
        {'description': 'One-time legal settlement', 'amount': 500, 'period': 'Q2 2024', 'rationale': 'Non-recurring expense'},
        {'description': 'Restructuring costs', 'amount': 300, 'period': 'Q3 2024', 'rationale': 'One-time reorganization'}
    ]
    
    qoe = analyzer.quality_of_earnings_analysis(one_time_items=adjustments)
    print("Quality of Earnings Analysis:")
    print(f"Reported EBITDA (Q4 2024): ${qoe['reported_ebitda']['Q4 2024']:,.0f}")
    print(f"Normalized EBITDA (Q4 2024): ${qoe['normalized_ebitda']['Q4 2024']:,.0f}")
    print(f"Total Adjustments: ${qoe['adjustment_summary']['total_adjustments']:,.0f}")
    
    # Validation
    validation = analyzer.validate_output()
    print(f"\nValidation: {len(validation['passed'])} checks passed, {len(validation['warnings'])} warnings, {len(validation['errors'])} errors")

