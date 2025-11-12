"""
Valuation Models Module for M&A Due Diligence

This module provides comprehensive valuation methodologies including:
- DCF (Discounted Cash Flow) valuation with WACC calculation
- Comparable Company Analysis with trading multiples
- Precedent Transaction Analysis with M&A multiples
- Scenario analysis (base/upside/downside)
- Sensitivity analysis on key value drivers

Usage:
    from valuation_models import ValuationAnalyzer
    
    analyzer = ValuationAnalyzer(financial_projections, market_data)
    dcf_value = analyzer.dcf_valuation(wacc=0.10, terminal_growth=0.03)
    comp_value = analyzer.comparable_company_analysis(peer_companies)
    precedent_value = analyzer.precedent_transaction_analysis(transactions)
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional


class ValuationAnalyzer:
    """
    Comprehensive valuation analysis using multiple methodologies.
    """
    
    def __init__(self, projections: pd.DataFrame, market_data: Dict = None):
        """
        Initialize valuation analyzer.
        
        Args:
            projections: DataFrame with financial projections by year
            market_data: Dictionary with market data (risk-free rate, beta, etc.)
        """
        self.projections = projections
        self.market_data = market_data or {}
        
    def dcf_valuation(self, 
                     wacc: float,
                     terminal_growth: float = 0.025,
                     explicit_period_years: int = 5) -> Dict:
        """
        Calculate DCF valuation with sensitivity analysis.
        
        Args:
            wacc: Weighted Average Cost of Capital
            terminal_growth: Perpetual growth rate for terminal value
            explicit_period_years: Number of years for explicit forecast period
            
        Returns:
            Dictionary with DCF valuation results
        """
        results = {
            'pv_explicit_period': {},
            'terminal_value': 0,
            'pv_terminal_value': 0,
            'enterprise_value': 0,
            'equity_value': 0,
            'sensitivity_analysis': {}
        }
        
        # Calculate present value of explicit period cash flows
        total_pv_fcf = 0
        years = self.projections.columns[:explicit_period_years]
        
        for i, year in enumerate(years, 1):
            fcf = self.projections.loc['Free Cash Flow', year]
            pv_factor = 1 / ((1 + wacc) ** i)
            pv_fcf = fcf * pv_factor
            results['pv_explicit_period'][year] = pv_fcf
            total_pv_fcf += pv_fcf
        
        # Calculate terminal value using perpetuity growth method
        last_year_fcf = self.projections.loc['Free Cash Flow', years[-1]]
        terminal_fcf = last_year_fcf * (1 + terminal_growth)
        terminal_value = terminal_fcf / (wacc - terminal_growth)
        results['terminal_value'] = terminal_value
        
        # Present value of terminal value
        pv_terminal = terminal_value / ((1 + wacc) ** explicit_period_years)
        results['pv_terminal_value'] = pv_terminal
        
        # Enterprise value
        results['enterprise_value'] = total_pv_fcf + pv_terminal
        
        # Sensitivity analysis
        wacc_range = [wacc - 0.02, wacc - 0.01, wacc, wacc + 0.01, wacc + 0.02]
        growth_range = [terminal_growth - 0.01, terminal_growth - 0.005, terminal_growth, 
                       terminal_growth + 0.005, terminal_growth + 0.01]
        
        sensitivity_matrix = {}
        for w in wacc_range:
            sensitivity_matrix[f"WACC_{w:.1%}"] = {}
            for g in growth_range:
                ev = self._calculate_dcf_ev(w, g, explicit_period_years)
                sensitivity_matrix[f"WACC_{w:.1%}"][f"Growth_{g:.1%}"] = ev
        
        results['sensitivity_analysis'] = sensitivity_matrix
        
        return results
    
    def _calculate_dcf_ev(self, wacc: float, terminal_growth: float, years: int) -> float:
        """Helper method to calculate enterprise value for sensitivity analysis."""
        total_pv = 0
        for i, year in enumerate(self.projections.columns[:years], 1):
            fcf = self.projections.loc['Free Cash Flow', year]
            pv = fcf / ((1 + wacc) ** i)
            total_pv += pv
        
        last_fcf = self.projections.loc['Free Cash Flow', self.projections.columns[years-1]]
        terminal_fcf = last_fcf * (1 + terminal_growth)
        terminal_value = terminal_fcf / (wacc - terminal_growth)
        pv_terminal = terminal_value / ((1 + wacc) ** years)
        
        return total_pv + pv_terminal
    
    def comparable_company_analysis(self, peer_data: pd.DataFrame) -> Dict:
        """
        Perform comparable company analysis using trading multiples.
        
        Args:
            peer_data: DataFrame with peer company metrics
                      Expected columns: Company, EV, Revenue, EBITDA, Growth_Rate, EBITDA_Margin
            
        Returns:
            Dictionary with comparable company analysis
        """
        results = {
            'peer_multiples': {},
            'valuation_by_multiple': {},
            'statistics': {}
        }
        
        # Calculate multiples for each peer
        peer_data['EV/Revenue'] = peer_data['EV'] / peer_data['Revenue']
        peer_data['EV/EBITDA'] = peer_data['EV'] / peer_data['EBITDA']
        
        # Calculate statistics
        results['statistics'] = {
            'EV/Revenue': {
                'mean': peer_data['EV/Revenue'].mean(),
                'median': peer_data['EV/Revenue'].median(),
                'min': peer_data['EV/Revenue'].min(),
                'max': peer_data['EV/Revenue'].max(),
                '25th_percentile': peer_data['EV/Revenue'].quantile(0.25),
                '75th_percentile': peer_data['EV/Revenue'].quantile(0.75)
            },
            'EV/EBITDA': {
                'mean': peer_data['EV/EBITDA'].mean(),
                'median': peer_data['EV/EBITDA'].median(),
                'min': peer_data['EV/EBITDA'].min(),
                'max': peer_data['EV/EBITDA'].max(),
                '25th_percentile': peer_data['EV/EBITDA'].quantile(0.25),
                '75th_percentile': peer_data['EV/EBITDA'].quantile(0.75)
            }
        }
        
        # Apply multiples to target metrics
        target_year = self.projections.columns[0]  # Use first projected year
        target_revenue = self.projections.loc['Revenue', target_year]
        target_ebitda = self.projections.loc['EBITDA', target_year] if 'EBITDA' in self.projections.index else 0
        
        results['valuation_by_multiple'] = {
            'EV_Revenue_Low': target_revenue * results['statistics']['EV/Revenue']['25th_percentile'],
            'EV_Revenue_Mid': target_revenue * results['statistics']['EV/Revenue']['median'],
            'EV_Revenue_High': target_revenue * results['statistics']['EV/Revenue']['75th_percentile'],
            'EV_EBITDA_Low': target_ebitda * results['statistics']['EV/EBITDA']['25th_percentile'],
            'EV_EBITDA_Mid': target_ebitda * results['statistics']['EV/EBITDA']['median'],
            'EV_EBITDA_High': target_ebitda * results['statistics']['EV/EBITDA']['75th_percentile']
        }
        
        # Store peer data for reference
        results['peer_multiples'] = peer_data[['Company', 'EV/Revenue', 'EV/EBITDA', 'Growth_Rate', 'EBITDA_Margin']].to_dict('records')
        
        return results
    
    def precedent_transaction_analysis(self, transaction_data: pd.DataFrame) -> Dict:
        """
        Perform precedent transaction analysis using M&A multiples.
        
        Args:
            transaction_data: DataFrame with comparable M&A transactions
                            Expected columns: Target, Acquirer, EV, Revenue, EBITDA, Date
            
        Returns:
            Dictionary with precedent transaction analysis
        """
        results = {
            'transaction_multiples': {},
            'valuation_by_multiple': {},
            'statistics': {}
        }
        
        # Calculate multiples for each transaction
        transaction_data['EV/Revenue'] = transaction_data['EV'] / transaction_data['Revenue']
        transaction_data['EV/EBITDA'] = transaction_data['EV'] / transaction_data['EBITDA']
        
        # Calculate statistics
        results['statistics'] = {
            'EV/Revenue': {
                'mean': transaction_data['EV/Revenue'].mean(),
                'median': transaction_data['EV/Revenue'].median(),
                'min': transaction_data['EV/Revenue'].min(),
                'max': transaction_data['EV/Revenue'].max()
            },
            'EV/EBITDA': {
                'mean': transaction_data['EV/EBITDA'].mean(),
                'median': transaction_data['EV/EBITDA'].median(),
                'min': transaction_data['EV/EBITDA'].min(),
                'max': transaction_data['EV/EBITDA'].max()
            }
        }
        
        # Apply multiples to target metrics
        target_year = self.projections.columns[0]
        target_revenue = self.projections.loc['Revenue', target_year]
        target_ebitda = self.projections.loc['EBITDA', target_year] if 'EBITDA' in self.projections.index else 0
        
        results['valuation_by_multiple'] = {
            'EV_Revenue_Low': target_revenue * results['statistics']['EV/Revenue']['min'],
            'EV_Revenue_Mid': target_revenue * results['statistics']['EV/Revenue']['median'],
            'EV_Revenue_High': target_revenue * results['statistics']['EV/Revenue']['max'],
            'EV_EBITDA_Low': target_ebitda * results['statistics']['EV/EBITDA']['min'],
            'EV_EBITDA_Mid': target_ebitda * results['statistics']['EV/EBITDA']['median'],
            'EV_EBITDA_High': target_ebitda * results['statistics']['EV/EBITDA']['max']
        }
        
        # Store transaction data for reference
        results['transaction_multiples'] = transaction_data[['Target', 'Acquirer', 'EV/Revenue', 'EV/EBITDA', 'Date']].to_dict('records')
        
        return results
    
    def calculate_wacc(self, 
                      risk_free_rate: float,
                      equity_beta: float,
                      market_risk_premium: float,
                      debt_cost: float,
                      tax_rate: float,
                      debt_weight: float,
                      equity_weight: float) -> float:
        """
        Calculate Weighted Average Cost of Capital (WACC).
        
        Args:
            risk_free_rate: Risk-free rate (e.g., 10-year Treasury)
            equity_beta: Company's equity beta
            market_risk_premium: Expected market return - risk-free rate
            debt_cost: Pre-tax cost of debt
            tax_rate: Corporate tax rate
            debt_weight: Debt / (Debt + Equity)
            equity_weight: Equity / (Debt + Equity)
            
        Returns:
            WACC as decimal
        """
        # Cost of equity using CAPM
        cost_of_equity = risk_free_rate + (equity_beta * market_risk_premium)
        
        # After-tax cost of debt
        after_tax_cost_debt = debt_cost * (1 - tax_rate)
        
        # WACC
        wacc = (equity_weight * cost_of_equity) + (debt_weight * after_tax_cost_debt)
        
        return wacc
    
    def scenario_valuation(self, scenarios: Dict) -> Dict:
        """
        Calculate valuation across multiple scenarios (base/upside/downside).
        
        Args:
            scenarios: Dictionary with 'base', 'upside', 'downside' scenario parameters
            
        Returns:
            Dictionary with valuations for each scenario
        """
        results = {}
        
        for scenario_name, params in scenarios.items():
            dcf = self.dcf_valuation(
                wacc=params['wacc'],
                terminal_growth=params['terminal_growth']
            )
            results[scenario_name] = {
                'enterprise_value': dcf['enterprise_value'],
                'assumptions': params
            }
        
        return results
    
    def valuation_summary(self, 
                         dcf_results: Dict,
                         comp_results: Dict,
                         precedent_results: Dict) -> Dict:
        """
        Synthesize valuation results across methodologies.
        
        Args:
            dcf_results: Results from DCF valuation
            comp_results: Results from comparable company analysis
            precedent_results: Results from precedent transaction analysis
            
        Returns:
            Dictionary with valuation summary and ranges
        """
        summary = {
            'dcf_value': dcf_results['enterprise_value'],
            'comp_value_range': {
                'low': min(comp_results['valuation_by_multiple']['EV_Revenue_Low'],
                          comp_results['valuation_by_multiple']['EV_EBITDA_Low']),
                'mid': (comp_results['valuation_by_multiple']['EV_Revenue_Mid'] +
                       comp_results['valuation_by_multiple']['EV_EBITDA_Mid']) / 2,
                'high': max(comp_results['valuation_by_multiple']['EV_Revenue_High'],
                           comp_results['valuation_by_multiple']['EV_EBITDA_High'])
            },
            'precedent_value_range': {
                'low': min(precedent_results['valuation_by_multiple']['EV_Revenue_Low'],
                          precedent_results['valuation_by_multiple']['EV_EBITDA_Low']),
                'mid': (precedent_results['valuation_by_multiple']['EV_Revenue_Mid'] +
                       precedent_results['valuation_by_multiple']['EV_EBITDA_Mid']) / 2,
                'high': max(precedent_results['valuation_by_multiple']['EV_Revenue_High'],
                           precedent_results['valuation_by_multiple']['EV_EBITDA_High'])
            }
        }
        
        # Calculate blended valuation (weighted average)
        # Typical weighting: DCF 40%, Comps 30%, Precedents 30%
        summary['blended_valuation'] = (
            0.40 * summary['dcf_value'] +
            0.30 * summary['comp_value_range']['mid'] +
            0.30 * summary['precedent_value_range']['mid']
        )
        
        # Valuation range across methodologies
        all_values = [
            summary['dcf_value'],
            summary['comp_value_range']['low'],
            summary['comp_value_range']['mid'],
            summary['comp_value_range']['high'],
            summary['precedent_value_range']['low'],
            summary['precedent_value_range']['mid'],
            summary['precedent_value_range']['high']
        ]
        
        summary['valuation_range'] = {
            'low': min(all_values),
            'mid': np.median(all_values),
            'high': max(all_values)
        }
        
        return summary


# Example usage
if __name__ == "__main__":
    # Sample projection data
    projection_data = {
        'Year 1': [50000, 10000, 8000],
        'Year 2': [60000, 13000, 10500],
        'Year 3': [72000, 16000, 13000],
        'Year 4': [86000, 19500, 16000],
        'Year 5': [103000, 23500, 19500]
    }
    
    projections = pd.DataFrame(projection_data, index=['Revenue', 'EBITDA', 'Free Cash Flow'])
    
    analyzer = ValuationAnalyzer(projections)
    
    # DCF valuation
    dcf = analyzer.dcf_valuation(wacc=0.10, terminal_growth=0.03)
    print(f"DCF Enterprise Value: ${dcf['enterprise_value']:,.0f}")
    print(f"Terminal Value: ${dcf['terminal_value']:,.0f}")
    print(f"PV of Terminal Value: ${dcf['pv_terminal_value']:,.0f}")
    
    # Calculate WACC
    wacc = analyzer.calculate_wacc(
        risk_free_rate=0.04,
        equity_beta=1.2,
        market_risk_premium=0.06,
        debt_cost=0.05,
        tax_rate=0.25,
        debt_weight=0.3,
        equity_weight=0.7
    )
    print(f"\nCalculated WACC: {wacc:.2%}")

