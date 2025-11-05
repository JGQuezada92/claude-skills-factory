#!/usr/bin/env python3
"""
Debt-Liquidity Interdependence Analyzer

Calculates debt metrics, refinancing schedules, and liquidity needs for debt 
servicing. Analyzes the symbiotic relationship between debt and liquidity.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


class DebtLiquidityAnalyzer:
    """Analyze debt-liquidity interdependence"""
    
    def __init__(self):
        self.debt_maturities = ['short_term', 'medium_term', 'long_term']
    
    def analyze_debt_liquidity(
        self,
        debt_data: pd.DataFrame,
        liquidity_data: pd.DataFrame,
        date_column: str = 'date',
        debt_column: str = 'total_debt',
        liquidity_column: str = 'liquidity_index',
        gdp_column: Optional[str] = None
    ) -> Dict:
        """
        Analyze the relationship between debt and liquidity
        
        Args:
            debt_data: DataFrame with debt time series
            liquidity_data: DataFrame with liquidity time series
            date_column: Name of date column
            debt_column: Name of total debt column
            liquidity_column: Name of liquidity index column
            gdp_column: Optional GDP column for debt-to-GDP calculation
            
        Returns:
            Dictionary with debt-liquidity interdependence analysis
        """
        try:
            # Merge dataframes
            merged = pd.merge(
                debt_data[[date_column, debt_column]],
                liquidity_data[[date_column, liquidity_column]],
                on=date_column,
                how='inner'
            )
            
            if gdp_column and gdp_column in debt_data.columns:
                merged = pd.merge(
                    merged,
                    debt_data[[date_column, gdp_column]],
                    on=date_column,
                    how='left'
                )
                merged['debt_to_gdp'] = merged[debt_column] / merged[gdp_column] * 100
            
            merged = merged.sort_values(date_column).reset_index(drop=True)
            
            # Calculate metrics
            merged['debt_growth'] = merged[debt_column].pct_change(periods=12) * 100
            merged['liquidity_growth'] = merged[liquidity_column].pct_change(periods=12) * 100
            merged['debt_liquidity_ratio'] = merged[debt_column] / merged[liquidity_column]
            
            # Correlation analysis
            correlation = merged[debt_column].corr(merged[liquidity_column])
            growth_correlation = merged['debt_growth'].corr(merged['liquidity_growth'])
            
            # Current metrics
            current_debt = merged[debt_column].iloc[-1]
            current_liquidity = merged[liquidity_column].iloc[-1]
            current_ratio = merged['debt_liquidity_ratio'].iloc[-1]
            
            return {
                'current_debt': current_debt,
                'current_liquidity': current_liquidity,
                'debt_liquidity_ratio': round(current_ratio, 3),
                'debt_growth_yoy': round(merged['debt_growth'].iloc[-1], 2),
                'liquidity_growth_yoy': round(merged['liquidity_growth'].iloc[-1], 2),
                'correlation_level': round(correlation, 3),
                'growth_correlation': round(growth_correlation, 3),
                'debt_to_gdp': round(merged['debt_to_gdp'].iloc[-1], 2) if 'debt_to_gdp' in merged.columns else None,
                'average_ratio': round(merged['debt_liquidity_ratio'].mean(), 3),
                'ratio_trend': merged['debt_liquidity_ratio'].iloc[-6:].mean() if len(merged) >= 6 else None,
                'analysis_date': datetime.now()
            }
            
        except Exception as e:
            print(f"Error in debt-liquidity analysis: {e}")
            return {'error': str(e)}
    
    def calculate_refinancing_schedule(
        self,
        debt_maturity_data: pd.DataFrame,
        date_column: str = 'date',
        maturity_columns: Dict[str, str] = None
    ) -> Dict:
        """
        Calculate debt refinancing schedule and liquidity needs
        
        Args:
            debt_maturity_data: DataFrame with debt maturity information
            date_column: Name of date column
            maturity_columns: Dictionary mapping maturity buckets to column names
            
        Returns:
            Refinancing schedule and liquidity needs analysis
        """
        try:
            df = debt_maturity_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            if maturity_columns is None:
                maturity_columns = {
                    'short_term': 'debt_0_1yr',
                    'medium_term': 'debt_1_5yr',
                    'long_term': 'debt_5yr_plus'
                }
            
            # Calculate upcoming refinancing needs
            refinancing_needs = {}
            
            for term, column in maturity_columns.items():
                if column not in df.columns:
                    continue
                
                current_value = df[column].iloc[-1]
                avg_value = df[column].mean()
                
                refinancing_needs[term] = {
                    'current_outstanding': current_value,
                    'average_outstanding': avg_value,
                    'upcoming_refinancing': current_value * 0.2  # Assume 20% matures annually
                }
            
            total_refinancing = sum(r['upcoming_refinancing'] for r in refinancing_needs.values())
            
            return {
                'refinancing_needs_by_term': refinancing_needs,
                'total_upcoming_refinancing': total_refinancing,
                'estimated_annual_refinancing': total_refinancing,
                'liquidity_requirement_ratio': total_refinancing / df['total_debt'].iloc[-1] if 'total_debt' in df.columns else None
            }
            
        except Exception as e:
            print(f"Error in refinancing schedule calculation: {e}")
            return {'error': str(e)}
    
    def assess_refinancing_risk(
        self,
        debt_data: pd.DataFrame,
        liquidity_data: pd.DataFrame,
        interest_rate_data: Optional[pd.DataFrame] = None,
        date_column: str = 'date',
        debt_column: str = 'total_debt',
        liquidity_column: str = 'liquidity_index',
        rate_column: str = 'interest_rate'
    ) -> Dict:
        """
        Assess refinancing risks based on liquidity conditions and interest rates
        
        Args:
            debt_data: Debt time series
            liquidity_data: Liquidity time series
            interest_rate_data: Optional interest rate data
            date_column: Name of date column
            debt_column: Debt column name
            liquidity_column: Liquidity column name
            rate_column: Interest rate column name
            
        Returns:
            Refinancing risk assessment
        """
        try:
            # Merge all data
            merged = pd.merge(
                debt_data[[date_column, debt_column]],
                liquidity_data[[date_column, liquidity_column]],
                on=date_column,
                how='inner'
            )
            
            if interest_rate_data is not None:
                merged = pd.merge(
                    merged,
                    interest_rate_data[[date_column, rate_column]],
                    on=date_column,
                    how='left'
                )
            
            merged = merged.sort_values(date_column).reset_index(drop=True)
            
            # Calculate risk metrics
            current_liquidity = merged[liquidity_column].iloc[-1]
            avg_liquidity = merged[liquidity_column].mean()
            liquidity_ratio = current_liquidity / avg_liquidity
            
            # Debt servicing capacity
            if rate_column in merged.columns:
                current_rate = merged[rate_column].iloc[-1]
                avg_rate = merged[rate_column].mean()
                servicing_cost = merged[debt_column].iloc[-1] * current_rate / 100
                servicing_cost_avg = merged[debt_column].iloc[-1] * avg_rate / 100
            else:
                servicing_cost = None
                servicing_cost_avg = None
            
            # Risk assessment
            if liquidity_ratio < 0.8:
                risk_level = 'high'
            elif liquidity_ratio < 1.0:
                risk_level = 'medium'
            else:
                risk_level = 'low'
            
            return {
                'liquidity_ratio': round(liquidity_ratio, 3),
                'risk_level': risk_level,
                'current_liquidity': current_liquidity,
                'average_liquidity': avg_liquidity,
                'debt_servicing_cost': servicing_cost,
                'debt_servicing_cost_avg': servicing_cost_avg,
                'interest_rate_impact': (current_rate - avg_rate) if rate_column in merged.columns else None,
                'recommendation': self._generate_refinancing_recommendation(risk_level, liquidity_ratio)
            }
            
        except Exception as e:
            print(f"Error in refinancing risk assessment: {e}")
            return {'error': str(e)}
    
    def _generate_refinancing_recommendation(
        self,
        risk_level: str,
        liquidity_ratio: float
    ) -> str:
        """Generate recommendation based on risk assessment"""
        if risk_level == 'high':
            return "Consider extending maturities and reducing near-term refinancing needs"
        elif risk_level == 'medium':
            return "Monitor liquidity conditions closely and prepare contingency plans"
        else:
            return "Current liquidity conditions support normal refinancing operations"


if __name__ == "__main__":
    # Example usage
    print("Debt-Liquidity Interdependence Analyzer")
    print("=" * 50)
    print("This script analyzes debt metrics and refinancing schedules")
    print("Import this module and use DebtLiquidityAnalyzer class in your analysis")
