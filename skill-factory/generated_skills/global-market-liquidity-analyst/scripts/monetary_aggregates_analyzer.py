#!/usr/bin/env python3
"""
Monetary Aggregates Analyzer

Analyzes M0, M1, M2, M3 growth rates, velocity, and credit creation across 
major economies. Distinguishes between different monetary aggregates and their 
liquidity implications.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

try:
    from output_validator import OutputValidator, ValidationResult
    VALIDATOR_AVAILABLE = True
except ImportError:
    VALIDATOR_AVAILABLE = False
    # Define dummy ValidationResult if not available
    class ValidationResult:
        def __init__(self):
            self.errors = []
            self.warnings = []
            self.passed = []
            self.is_valid = True


class MonetaryAggregatesAnalyzer:
    """Analyze monetary aggregates (M0, M1, M2, M3) across economies"""
    
    def __init__(self):
        self.aggregate_types = ['M0', 'M1', 'M2', 'M3']
        self.aggregate_definitions = {
            'M0': 'Base money (currency in circulation + central bank reserves)',
            'M1': 'Narrow money (M0 + demand deposits)',
            'M2': 'Broad money (M1 + savings deposits + time deposits)',
            'M3': 'Extended broad money (M2 + large time deposits + institutional money funds)'
        }
    
    def analyze_aggregates(
        self,
        monetary_data: pd.DataFrame,
        date_column: str = 'date',
        value_columns: List[str] = ['M0', 'M1', 'M2', 'M3'],
        country_column: Optional[str] = None,
        gdp_column: Optional[str] = None
    ) -> Dict:
        """
        Analyze monetary aggregates with growth rates and velocity
        
        Args:
            monetary_data: DataFrame with monetary aggregate time series
            date_column: Name of date column
            value_columns: List of monetary aggregate column names
            country_column: Optional country identifier column
            gdp_column: Optional GDP column for velocity calculation
            
        Returns:
            Dictionary with comprehensive monetary aggregates analysis
        """
        try:
            df = monetary_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            analysis = {}
            
            for agg_type in value_columns:
                if agg_type not in df.columns:
                    continue
                
                # Calculate growth rates
                df[f'{agg_type}_mom'] = df[agg_type].pct_change() * 100  # Month-over-month
                df[f'{agg_type}_yoy'] = df[agg_type].pct_change(periods=12) * 100  # Year-over-year
                df[f'{agg_type}_qoq'] = df[agg_type].pct_change(periods=3) * 100  # Quarter-over-quarter
                
                # Calculate velocity if GDP data available
                if gdp_column and gdp_column in df.columns:
                    df[f'{agg_type}_velocity'] = df[gdp_column] / df[agg_type]
                    df[f'{agg_type}_velocity_change'] = df[f'{agg_type}_velocity'].pct_change() * 100
                
                # Current values
                current_value = df[agg_type].iloc[-1]
                current_yoy = df[f'{agg_type}_yoy'].iloc[-1]
                current_mom = df[f'{agg_type}_mom'].iloc[-1]
                
                # Historical averages
                avg_yoy = df[f'{agg_type}_yoy'].mean()
                avg_mom = df[f'{agg_type}_mom'].mean()
                
                # Trends
                recent_trend = df[f'{agg_type}_yoy'].iloc[-6:].mean() if len(df) >= 6 else None
                
                analysis[agg_type] = {
                    'current_value': current_value,
                    'current_yoy_growth': round(current_yoy, 2),
                    'current_mom_growth': round(current_mom, 2),
                    'average_yoy_growth': round(avg_yoy, 2),
                    'average_mom_growth': round(avg_mom, 2),
                    'recent_trend_6m': round(recent_trend, 2) if recent_trend else None,
                    'peak_value': df[agg_type].max(),
                    'trough_value': df[agg_type].min(),
                    'definition': self.aggregate_definitions.get(agg_type, 'N/A')
                }
                
                # Add velocity metrics if available
                if gdp_column and gdp_column in df.columns:
                    analysis[agg_type]['current_velocity'] = df[f'{agg_type}_velocity'].iloc[-1]
                    analysis[agg_type]['velocity_change_yoy'] = (
                        df[f'{agg_type}_velocity'].iloc[-1] - df[f'{agg_type}_velocity'].iloc[-12]
                    ) / df[f'{agg_type}_velocity'].iloc[-12] * 100 if len(df) >= 12 else None
            
            # Cross-aggregate analysis
            if len(value_columns) > 1:
                cross_analysis = self._analyze_aggregate_relationships(df, value_columns)
                analysis['cross_aggregate_analysis'] = cross_analysis
            
            # Country-specific analysis if available
            if country_column and country_column in df.columns:
                country_analysis = self._analyze_by_country(df, value_columns, country_column)
                analysis['by_country'] = country_analysis
            
            return {
                'aggregates': analysis,
                'analysis_date': datetime.now(),
                'data_points': len(df)
            }
            
        except Exception as e:
            print(f"Error in monetary aggregates analysis: {e}")
            return {'error': str(e)}
    
    def _analyze_aggregate_relationships(
        self,
        df: pd.DataFrame,
        value_columns: List[str]
    ) -> Dict:
        """Analyze relationships between different monetary aggregates"""
        relationships = {}
        
        for i, agg1 in enumerate(value_columns):
            if agg1 not in df.columns:
                continue
            for agg2 in value_columns[i+1:]:
                if agg2 not in df.columns:
                    continue
                
                # Calculate ratio
                ratio_column = f'{agg1}_to_{agg2}_ratio'
                df[ratio_column] = df[agg1] / df[agg2]
                
                # Calculate correlation
                correlation = df[agg1].corr(df[agg2])
                
                relationships[f'{agg1}_to_{agg2}'] = {
                    'current_ratio': df[ratio_column].iloc[-1],
                    'average_ratio': df[ratio_column].mean(),
                    'correlation': round(correlation, 3),
                    'ratio_trend': df[ratio_column].iloc[-6:].mean() if len(df) >= 6 else None
                }
        
        return relationships
    
    def _analyze_by_country(
        self,
        df: pd.DataFrame,
        value_columns: List[str],
        country_column: str
    ) -> Dict:
        """Analyze monetary aggregates by country"""
        country_analysis = {}
        
        for country in df[country_column].unique():
            country_data = df[df[country_column] == country].copy()
            
            country_metrics = {}
            for agg_type in value_columns:
                if agg_type not in country_data.columns:
                    continue
                
                country_data[f'{agg_type}_yoy'] = country_data[agg_type].pct_change(periods=12) * 100
                
                country_metrics[agg_type] = {
                    'current_value': country_data[agg_type].iloc[-1],
                    'current_yoy_growth': round(country_data[f'{agg_type}_yoy'].iloc[-1], 2),
                    'average_yoy_growth': round(country_data[f'{agg_type}_yoy'].mean(), 2)
                }
            
            country_analysis[country] = country_metrics
        
        return country_analysis
    
    def calculate_credit_creation(
        self,
        monetary_data: pd.DataFrame,
        date_column: str = 'date',
        m2_column: str = 'M2',
        m0_column: Optional[str] = None
    ) -> Dict:
        """
        Calculate credit creation metrics
        
        Args:
            monetary_data: DataFrame with monetary data
            date_column: Name of date column
            m2_column: M2 aggregate column name
            m0_column: Optional M0 column for money multiplier calculation
            
        Returns:
            Credit creation analysis
        """
        try:
            df = monetary_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            # M2 growth as proxy for credit creation
            df['m2_growth'] = df[m2_column].pct_change(periods=12) * 100
            df['m2_change_abs'] = df[m2_column].diff(periods=12)
            
            # Money multiplier if M0 available
            multiplier_analysis = None
            if m0_column and m0_column in df.columns:
                df['money_multiplier'] = df[m2_column] / df[m0_column]
                df['multiplier_change'] = df['money_multiplier'].pct_change() * 100
                
                multiplier_analysis = {
                    'current_multiplier': df['money_multiplier'].iloc[-1],
                    'average_multiplier': df['money_multiplier'].mean(),
                    'multiplier_trend': df['multiplier_change'].iloc[-6:].mean() if len(df) >= 6 else None
                }
            
            return {
                'current_credit_growth': round(df['m2_growth'].iloc[-1], 2),
                'average_credit_growth': round(df['m2_growth'].mean(), 2),
                'credit_creation_12m': df['m2_change_abs'].iloc[-1],
                'credit_trend': df['m2_growth'].iloc[-6:].mean() if len(df) >= 6 else None,
                'money_multiplier': multiplier_analysis
            }
            
        except Exception as e:
            print(f"Error in credit creation calculation: {e}")
            return {'error': str(e)}
    
    def validate_growth_calculations(
        self,
        analysis_results: Dict,
        monetary_data: pd.DataFrame,
        value_columns: List[str] = ['M0', 'M1', 'M2', 'M3'],
        date_column: str = 'date'
    ) -> ValidationResult:
        """
        Validate growth rate calculations by manual recalculation
        
        Args:
            analysis_results: Results from analyze_aggregates()
            monetary_data: Original monetary data
            value_columns: List of aggregate columns
            date_column: Name of date column
            
        Returns:
            ValidationResult object
        """
        if not VALIDATOR_AVAILABLE:
            return ValidationResult()
        
        result = ValidationResult()
        validator = OutputValidator()
        
        try:
            df = monetary_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            if 'aggregates' not in analysis_results:
                result.add_warning('growth_calculations', 'No aggregates found in analysis results')
                return result
            
            aggregates = analysis_results['aggregates']
            
            for agg_type in value_columns:
                if agg_type not in aggregates:
                    continue
                
                agg_data = aggregates[agg_type]
                
                # Validate YoY growth calculation
                if 'current_yoy_growth' in agg_data and 'current_value' in agg_data:
                    current_value = df[agg_type].iloc[-1] if agg_type in df.columns else None
                    value_12m_ago = df[agg_type].iloc[-13] if len(df) >= 13 and agg_type in df.columns else None
                    
                    if current_value is not None and value_12m_ago is not None and value_12m_ago != 0:
                        reported_yoy = agg_data['current_yoy_growth']
                        is_valid, message = validator.validate_percent_change(
                            current_value,
                            value_12m_ago,
                            reported_yoy
                        )
                        
                        if is_valid:
                            result.add_passed(f'{agg_type}_yoy_growth', f'{agg_type} YoY growth validated: {reported_yoy:.2f}%')
                        else:
                            result.add_error(
                                f'{agg_type}_yoy_growth',
                                f'{agg_type} YoY growth: {message}',
                                {'reported': reported_yoy, 'aggregate': agg_type}
                            )
                
                # Validate MoM growth calculation
                if 'current_mom_growth' in agg_data:
                    current_value = df[agg_type].iloc[-1] if agg_type in df.columns else None
                    value_1m_ago = df[agg_type].iloc[-2] if len(df) >= 2 and agg_type in df.columns else None
                    
                    if current_value is not None and value_1m_ago is not None and value_1m_ago != 0:
                        reported_mom = agg_data['current_mom_growth']
                        is_valid, message = validator.validate_percent_change(
                            current_value,
                            value_1m_ago,
                            reported_mom
                        )
                        
                        if is_valid:
                            result.add_passed(f'{agg_type}_mom_growth', f'{agg_type} MoM growth validated: {reported_mom:.2f}%')
                        else:
                            result.add_error(
                                f'{agg_type}_mom_growth',
                                f'{agg_type} MoM growth: {message}',
                                {'reported': reported_mom, 'aggregate': agg_type}
                            )
                
                # Validate velocity if available
                if 'current_velocity' in agg_data:
                    velocity = agg_data['current_velocity']
                    is_valid, message = validator.validate_range(velocity, 'velocity', f'{agg_type} velocity')
                    
                    if is_valid:
                        result.add_passed(f'{agg_type}_velocity', f'{agg_type} velocity validated: {velocity:.2f}')
                    else:
                        result.add_warning(f'{agg_type}_velocity', f'{agg_type} velocity: {message}')
            
        except Exception as e:
            result.add_error('growth_calculations_validation', f'Error validating growth calculations: {str(e)}')
        
        return result
    
    def validate_output(
        self,
        analysis_results: Dict,
        monetary_data: pd.DataFrame,
        value_columns: List[str] = ['M0', 'M1', 'M2', 'M3'],
        date_column: str = 'date'
    ) -> ValidationResult:
        """
        Validate all output from monetary aggregates analysis
        
        Args:
            analysis_results: Results from analyze_aggregates()
            monetary_data: Original monetary data
            value_columns: List of aggregate columns
            date_column: Name of date column
            
        Returns:
            ValidationResult object with all validation checks
        """
        if not VALIDATOR_AVAILABLE:
            return ValidationResult()
        
        result = ValidationResult()
        validator = OutputValidator()
        
        try:
            # Validate growth calculations
            growth_result = self.validate_growth_calculations(
                analysis_results,
                monetary_data,
                value_columns,
                date_column
            )
            result.errors.extend(growth_result.errors)
            result.warnings.extend(growth_result.warnings)
            result.passed.extend(growth_result.passed)
            
            # Validate monetary aggregates hierarchy
            if 'aggregates' in analysis_results:
                aggregates = analysis_results['aggregates']
                hierarchy_values = {}
                
                for agg_type in ['M0', 'M1', 'M2', 'M3']:
                    if agg_type in aggregates and 'current_value' in aggregates[agg_type]:
                        hierarchy_values[agg_type] = aggregates[agg_type]['current_value']
                
                if len(hierarchy_values) > 1:
                    hierarchy_result = validator.validate_monetary_aggregates_hierarchy(hierarchy_values)
                    result.errors.extend(hierarchy_result.errors)
                    result.warnings.extend(hierarchy_result.warnings)
                    result.passed.extend(hierarchy_result.passed)
            
            # Validate growth rate consistency
            if len(monetary_data) >= 13:
                consistency_result = validator.validate_growth_rate_consistency(
                    analysis_results,
                    monetary_data,
                    value_columns[0] if value_columns else 'M2',
                    date_column
                )
                result.warnings.extend(consistency_result.warnings)
                result.passed.extend(consistency_result.passed)
            
            result.is_valid = len(result.errors) == 0
            
        except Exception as e:
            result.add_error('output_validation', f'Error validating output: {str(e)}')
        
        return result


if __name__ == "__main__":
    # Example usage
    print("Monetary Aggregates Analyzer")
    print("=" * 50)
    print("This script analyzes M0, M1, M2, M3 monetary aggregates")
    print("Import this module and use MonetaryAggregatesAnalyzer class in your analysis")
