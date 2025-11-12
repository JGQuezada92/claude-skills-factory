"""
Financial Analyzer Script
Core financial calculations, ratio analysis, and financial statement analysis

This script provides comprehensive financial analysis capabilities including:
- Financial ratio calculations (liquidity, profitability, efficiency, leverage)
- DuPont analysis for ROE decomposition
- Trend analysis and growth rate calculations
- Working capital and cash conversion cycle analysis
- Quality of earnings assessment
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from decimal import Decimal, ROUND_HALF_UP


class FinancialAnalyzer:
    """
    Comprehensive financial analysis toolkit for FP&A professionals
    """
    
    def __init__(self, income_statement: pd.DataFrame = None, 
                 balance_sheet: pd.DataFrame = None,
                 cash_flow: pd.DataFrame = None):
        """
        Initialize with financial statements
        
        Args:
            income_statement: Income statement data with periods as columns
            balance_sheet: Balance sheet data with periods as columns
            cash_flow: Cash flow statement data with periods as columns
        """
        self.income_statement = income_statement
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow
        
    # =============================================================================
    # LIQUIDITY RATIOS
    # =============================================================================
    
    def calculate_current_ratio(self, current_assets: float, current_liabilities: float) -> float:
        """
        Current Ratio = Current Assets / Current Liabilities
        Measures short-term liquidity. Healthy: > 1.5
        """
        if current_liabilities == 0:
            return None
        return current_assets / current_liabilities
    
    def calculate_quick_ratio(self, current_assets: float, inventory: float, 
                             current_liabilities: float) -> float:
        """
        Quick Ratio = (Current Assets - Inventory) / Current Liabilities
        Measures ability to meet short-term obligations without selling inventory
        Healthy: > 1.0
        """
        if current_liabilities == 0:
            return None
        return (current_assets - inventory) / current_liabilities
    
    def calculate_cash_ratio(self, cash: float, current_liabilities: float) -> float:
        """
        Cash Ratio = Cash / Current Liabilities
        Most conservative liquidity measure
        """
        if current_liabilities == 0:
            return None
        return cash / current_liabilities
    
    def calculate_working_capital(self, current_assets: float, current_liabilities: float) -> float:
        """
        Working Capital = Current Assets - Current Liabilities
        Absolute measure of liquidity
        """
        return current_assets - current_liabilities
    
    # =============================================================================
    # PROFITABILITY RATIOS
    # =============================================================================
    
    def calculate_gross_margin(self, revenue: float, cogs: float) -> float:
        """
        Gross Margin % = (Revenue - COGS) / Revenue
        Measures profitability after direct costs
        """
        if revenue == 0:
            return None
        return ((revenue - cogs) / revenue) * 100
    
    def calculate_operating_margin(self, operating_income: float, revenue: float) -> float:
        """
        Operating Margin % = Operating Income / Revenue
        Measures profitability from core operations
        """
        if revenue == 0:
            return None
        return (operating_income / revenue) * 100
    
    def calculate_net_margin(self, net_income: float, revenue: float) -> float:
        """
        Net Margin % = Net Income / Revenue
        Measures bottom-line profitability
        """
        if revenue == 0:
            return None
        return (net_income / revenue) * 100
    
    def calculate_ebitda_margin(self, ebitda: float, revenue: float) -> float:
        """
        EBITDA Margin % = EBITDA / Revenue
        Measures operating profitability before interest, taxes, depreciation, amortization
        """
        if revenue == 0:
            return None
        return (ebitda / revenue) * 100
    
    def calculate_roa(self, net_income: float, total_assets: float) -> float:
        """
        Return on Assets (ROA) % = Net Income / Total Assets
        Measures efficiency of asset utilization
        """
        if total_assets == 0:
            return None
        return (net_income / total_assets) * 100
    
    def calculate_roe(self, net_income: float, shareholders_equity: float) -> float:
        """
        Return on Equity (ROE) % = Net Income / Shareholders' Equity
        Measures return to shareholders
        """
        if shareholders_equity == 0:
            return None
        return (net_income / shareholders_equity) * 100
    
    def calculate_roic(self, nopat: float, invested_capital: float) -> float:
        """
        Return on Invested Capital (ROIC) % = NOPAT / Invested Capital
        Where NOPAT = Operating Income * (1 - Tax Rate)
        Invested Capital = Total Debt + Total Equity - Cash
        Measures return on capital invested in the business
        """
        if invested_capital == 0:
            return None
        return (nopat / invested_capital) * 100
    
    # =============================================================================
    # EFFICIENCY RATIOS
    # =============================================================================
    
    def calculate_asset_turnover(self, revenue: float, total_assets: float) -> float:
        """
        Asset Turnover = Revenue / Total Assets
        Measures efficiency of asset utilization for revenue generation
        """
        if total_assets == 0:
            return None
        return revenue / total_assets
    
    def calculate_inventory_turnover(self, cogs: float, avg_inventory: float) -> float:
        """
        Inventory Turnover = COGS / Average Inventory
        Measures how quickly inventory is sold
        """
        if avg_inventory == 0:
            return None
        return cogs / avg_inventory
    
    def calculate_days_inventory_outstanding(self, cogs: float, avg_inventory: float) -> float:
        """
        Days Inventory Outstanding (DIO) = 365 / Inventory Turnover
        = (Average Inventory / COGS) * 365
        Average days to sell inventory
        """
        if cogs == 0:
            return None
        return (avg_inventory / cogs) * 365
    
    def calculate_receivables_turnover(self, revenue: float, avg_receivables: float) -> float:
        """
        Receivables Turnover = Revenue / Average Receivables
        Measures collection efficiency
        """
        if avg_receivables == 0:
            return None
        return revenue / avg_receivables
    
    def calculate_days_sales_outstanding(self, revenue: float, avg_receivables: float) -> float:
        """
        Days Sales Outstanding (DSO) = 365 / Receivables Turnover
        = (Average Receivables / Revenue) * 365
        Average days to collect receivables
        """
        if revenue == 0:
            return None
        return (avg_receivables / revenue) * 365
    
    def calculate_payables_turnover(self, cogs: float, avg_payables: float) -> float:
        """
        Payables Turnover = COGS / Average Payables
        Measures payment frequency to suppliers
        """
        if avg_payables == 0:
            return None
        return cogs / avg_payables
    
    def calculate_days_payables_outstanding(self, cogs: float, avg_payables: float) -> float:
        """
        Days Payables Outstanding (DPO) = 365 / Payables Turnover
        = (Average Payables / COGS) * 365
        Average days to pay suppliers
        """
        if cogs == 0:
            return None
        return (avg_payables / cogs) * 365
    
    def calculate_cash_conversion_cycle(self, dso: float, dio: float, dpo: float) -> float:
        """
        Cash Conversion Cycle = DSO + DIO - DPO
        Days to convert investments in inventory and receivables into cash
        Lower is better (faster cash conversion)
        """
        return dso + dio - dpo
    
    # =============================================================================
    # LEVERAGE RATIOS
    # =============================================================================
    
    def calculate_debt_to_equity(self, total_debt: float, total_equity: float) -> float:
        """
        Debt-to-Equity Ratio = Total Debt / Total Equity
        Measures financial leverage
        """
        if total_equity == 0:
            return None
        return total_debt / total_equity
    
    def calculate_debt_to_assets(self, total_debt: float, total_assets: float) -> float:
        """
        Debt-to-Assets Ratio = Total Debt / Total Assets
        Measures proportion of assets financed by debt
        """
        if total_assets == 0:
            return None
        return total_debt / total_assets
    
    def calculate_equity_multiplier(self, total_assets: float, total_equity: float) -> float:
        """
        Equity Multiplier = Total Assets / Total Equity
        Component of DuPont analysis, measures financial leverage
        """
        if total_equity == 0:
            return None
        return total_assets / total_equity
    
    def calculate_interest_coverage(self, ebit: float, interest_expense: float) -> float:
        """
        Interest Coverage Ratio = EBIT / Interest Expense
        Measures ability to pay interest obligations
        Healthy: > 3.0
        """
        if interest_expense == 0:
            return None
        return ebit / interest_expense
    
    def calculate_debt_service_coverage(self, operating_income: float, 
                                        debt_service: float) -> float:
        """
        Debt Service Coverage Ratio = Operating Income / Total Debt Service
        Where debt service = principal + interest payments
        Measures ability to service all debt obligations
        """
        if debt_service == 0:
            return None
        return operating_income / debt_service
    
    # =============================================================================
    # DUPONT ANALYSIS
    # =============================================================================
    
    def calculate_dupont_roe(self, net_income: float, revenue: float, 
                            total_assets: float, total_equity: float) -> Dict[str, float]:
        """
        DuPont Analysis: ROE = Net Margin × Asset Turnover × Equity Multiplier
        
        Returns:
            Dictionary with:
            - roe: Overall ROE
            - net_margin: Profitability component
            - asset_turnover: Efficiency component
            - equity_multiplier: Leverage component
        """
        net_margin = (net_income / revenue * 100) if revenue != 0 else None
        asset_turnover = (revenue / total_assets) if total_assets != 0 else None
        equity_multiplier = (total_assets / total_equity) if total_equity != 0 else None
        
        roe = (net_income / total_equity * 100) if total_equity != 0 else None
        
        return {
            'roe': roe,
            'net_margin': net_margin,
            'asset_turnover': asset_turnover,
            'equity_multiplier': equity_multiplier,
            'interpretation': self._interpret_dupont(net_margin, asset_turnover, equity_multiplier)
        }
    
    def _interpret_dupont(self, net_margin: float, asset_turnover: float, 
                         equity_multiplier: float) -> str:
        """Interpret which component is driving ROE"""
        if None in [net_margin, asset_turnover, equity_multiplier]:
            return "Insufficient data for interpretation"
        
        drivers = []
        if net_margin > 15:
            drivers.append("High Profitability")
        elif net_margin < 5:
            drivers.append("Low Profitability")
            
        if asset_turnover > 1.5:
            drivers.append("Efficient Asset Utilization")
        elif asset_turnover < 0.5:
            drivers.append("Inefficient Asset Utilization")
            
        if equity_multiplier > 3:
            drivers.append("High Leverage")
        elif equity_multiplier < 1.5:
            drivers.append("Low Leverage")
        
        return " | ".join(drivers) if drivers else "Balanced ROE Components"
    
    # =============================================================================
    # GROWTH & TREND ANALYSIS
    # =============================================================================
    
    def calculate_growth_rate(self, current_value: float, prior_value: float) -> float:
        """
        Growth Rate % = ((Current - Prior) / Prior) * 100
        """
        if prior_value == 0:
            return None
        return ((current_value - prior_value) / prior_value) * 100
    
    def calculate_cagr(self, ending_value: float, beginning_value: float, 
                      num_periods: int) -> float:
        """
        Compound Annual Growth Rate (CAGR)
        CAGR = ((Ending Value / Beginning Value)^(1/n) - 1) * 100
        """
        if beginning_value == 0 or num_periods == 0:
            return None
        return (((ending_value / beginning_value) ** (1/num_periods)) - 1) * 100
    
    # =============================================================================
    # CASH FLOW ANALYSIS
    # =============================================================================
    
    def calculate_free_cash_flow(self, operating_cf: float, capex: float) -> float:
        """
        Free Cash Flow = Operating Cash Flow - Capital Expenditures
        Cash available after maintaining/expanding asset base
        """
        return operating_cf - capex
    
    def calculate_operating_cf_ratio(self, operating_cf: float, 
                                    current_liabilities: float) -> float:
        """
        Operating Cash Flow Ratio = Operating CF / Current Liabilities
        Measures ability to pay current liabilities from operating cash
        """
        if current_liabilities == 0:
            return None
        return operating_cf / current_liabilities
    
    def calculate_cash_flow_to_net_income(self, operating_cf: float, 
                                          net_income: float) -> float:
        """
        Cash Flow to Net Income Ratio = Operating CF / Net Income
        Measures quality of earnings. Ratio > 1.0 is healthy
        """
        if net_income == 0:
            return None
        return operating_cf / net_income
    
    # =============================================================================
    # COMPREHENSIVE RATIO ANALYSIS
    # =============================================================================
    
    def calculate_all_ratios(self, financial_data: Dict) -> Dict[str, Dict]:
        """
        Calculate comprehensive set of financial ratios
        
        Args:
            financial_data: Dictionary containing all necessary financial statement line items
            
        Returns:
            Dictionary organized by ratio category with all calculated ratios
        """
        ratios = {
            'liquidity': {},
            'profitability': {},
            'efficiency': {},
            'leverage': {},
            'cash_flow': {},
            'dupont': {}
        }
        
        # Liquidity Ratios
        if 'current_assets' in financial_data and 'current_liabilities' in financial_data:
            ratios['liquidity']['current_ratio'] = self.calculate_current_ratio(
                financial_data['current_assets'], 
                financial_data['current_liabilities']
            )
            
        if all(k in financial_data for k in ['current_assets', 'inventory', 'current_liabilities']):
            ratios['liquidity']['quick_ratio'] = self.calculate_quick_ratio(
                financial_data['current_assets'],
                financial_data['inventory'],
                financial_data['current_liabilities']
            )
        
        # Profitability Ratios
        if 'revenue' in financial_data and 'cogs' in financial_data:
            ratios['profitability']['gross_margin'] = self.calculate_gross_margin(
                financial_data['revenue'],
                financial_data['cogs']
            )
            
        if 'operating_income' in financial_data and 'revenue' in financial_data:
            ratios['profitability']['operating_margin'] = self.calculate_operating_margin(
                financial_data['operating_income'],
                financial_data['revenue']
            )
        
        # Add more ratio calculations...
        
        return ratios
    
    # =============================================================================
    # UTILITY FUNCTIONS
    # =============================================================================
    
    def format_percentage(self, value: float, decimals: int = 1) -> str:
        """Format value as percentage with specified decimals"""
        if value is None:
            return "N/A"
        return f"{value:.{decimals}f}%"
    
    def format_currency(self, value: float, decimals: int = 0) -> str:
        """Format value as currency"""
        if value is None:
            return "N/A"
        return f"${value:,.{decimals}f}"
    
    def format_ratio(self, value: float, decimals: int = 2) -> str:
        """Format value as ratio"""
        if value is None:
            return "N/A"
        return f"{value:.{decimals}f}x"


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    # Example: Calculate ratios for a sample company
    analyzer = FinancialAnalyzer()
    
    # Sample financial data
    financial_data = {
        'current_assets': 500000,
        'inventory': 100000,
        'current_liabilities': 250000,
        'revenue': 2000000,
        'cogs': 1200000,
        'operating_income': 400000,
        'net_income': 300000,
        'total_assets': 1500000,
        'total_equity': 800000
    }
    
    # Calculate key ratios
    print("=== LIQUIDITY RATIOS ===")
    current_ratio = analyzer.calculate_current_ratio(
        financial_data['current_assets'],
        financial_data['current_liabilities']
    )
    print(f"Current Ratio: {analyzer.format_ratio(current_ratio)}")
    
    quick_ratio = analyzer.calculate_quick_ratio(
        financial_data['current_assets'],
        financial_data['inventory'],
        financial_data['current_liabilities']
    )
    print(f"Quick Ratio: {analyzer.format_ratio(quick_ratio)}")
    
    print("\n=== PROFITABILITY RATIOS ===")
    gross_margin = analyzer.calculate_gross_margin(
        financial_data['revenue'],
        financial_data['cogs']
    )
    print(f"Gross Margin: {analyzer.format_percentage(gross_margin)}")
    
    operating_margin = analyzer.calculate_operating_margin(
        financial_data['operating_income'],
        financial_data['revenue']
    )
    print(f"Operating Margin: {analyzer.format_percentage(operating_margin)}")
    
    roe = analyzer.calculate_roe(
        financial_data['net_income'],
        financial_data['total_equity']
    )
    print(f"Return on Equity: {analyzer.format_percentage(roe)}")
    
    print("\n=== DUPONT ANALYSIS ===")
    dupont = analyzer.calculate_dupont_roe(
        financial_data['net_income'],
        financial_data['revenue'],
        financial_data['total_assets'],
        financial_data['total_equity']
    )
    print(f"ROE: {analyzer.format_percentage(dupont['roe'])}")
    print(f"Net Margin: {analyzer.format_percentage(dupont['net_margin'])}")
    print(f"Asset Turnover: {analyzer.format_ratio(dupont['asset_turnover'])}")
    print(f"Equity Multiplier: {analyzer.format_ratio(dupont['equity_multiplier'])}")
    print(f"Interpretation: {dupont['interpretation']}")

