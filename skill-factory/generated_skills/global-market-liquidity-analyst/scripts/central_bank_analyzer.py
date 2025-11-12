#!/usr/bin/env python3
"""
Central Bank Analyzer

Calculates central bank balance sheet changes, QE/QT flows, and policy impact 
assessments for major central banks (Fed, ECB, BOJ, PBOC).
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


class CentralBankAnalyzer:
    """Analyze central bank balance sheets and policy actions"""
    
    def __init__(self):
        self.major_banks = ['Fed', 'ECB', 'BOJ', 'PBOC', 'BOE']
    
    def analyze_balance_sheet(
        self,
        balance_sheet_data: pd.DataFrame,
        date_column: str = 'date',
        asset_column: str = 'total_assets',
        bank_column: str = 'central_bank'
    ) -> Dict:
        """
        Analyze central bank balance sheet changes
        
        Args:
            balance_sheet_data: DataFrame with balance sheet time series
            date_column: Name of date column
            asset_column: Name of total assets column
            bank_column: Name of central bank identifier column
            
        Returns:
            Dictionary with balance sheet analysis results
        """
        try:
            df = balance_sheet_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values([bank_column, date_column]).reset_index(drop=True)
            
            analysis = {}
            
            for bank in df[bank_column].unique():
                bank_data = df[df[bank_column] == bank].copy()
                bank_data = bank_data.sort_values(date_column).reset_index(drop=True)
                
                # Calculate changes
                bank_data['monthly_change'] = bank_data[asset_column].diff()
                bank_data['yoy_change'] = bank_data[asset_column].pct_change(periods=12) * 100
                bank_data['yoy_change_abs'] = bank_data[asset_column] - bank_data[asset_column].shift(12)
                
                # Identify QE/QT periods
                qe_qt_analysis = self._identify_qe_qt_periods(bank_data, asset_column)
                
                # Calculate policy impact metrics
                current_assets = bank_data[asset_column].iloc[-1]
                peak_assets = bank_data[asset_column].max()
                recent_change = bank_data['monthly_change'].iloc[-1]
                yoy_change = bank_data['yoy_change'].iloc[-1]
                
                analysis[bank] = {
                    'current_assets': current_assets,
                    'peak_assets': peak_assets,
                    'peak_date': bank_data.loc[bank_data[asset_column].idxmax(), date_column],
                    'recent_monthly_change': recent_change,
                    'yoy_change_percent': round(yoy_change, 2),
                    'yoy_change_absolute': bank_data['yoy_change_abs'].iloc[-1],
                    'qe_qt_analysis': qe_qt_analysis,
                    'policy_stance': self._determine_policy_stance(recent_change, yoy_change),
                    'data_points': len(bank_data)
                }
            
            # Aggregate analysis
            aggregate = self._aggregate_analysis(df, date_column, asset_column)
            
            return {
                'by_bank': analysis,
                'aggregate': aggregate,
                'analysis_date': datetime.now()
            }
            
        except Exception as e:
            print(f"Error in balance sheet analysis: {e}")
            return {'error': str(e)}
    
    def _identify_qe_qt_periods(
        self,
        bank_data: pd.DataFrame,
        asset_column: str,
        threshold: float = 0.01
    ) -> Dict:
        """Identify quantitative easing and tightening periods"""
        monthly_changes = bank_data[asset_column].diff()
        monthly_changes_pct = bank_data[asset_column].pct_change()
        
        # QE: sustained positive growth
        # QT: sustained negative growth
        qe_periods = []
        qt_periods = []
        
        current_period_type = None
        period_start = None
        
        for i, (idx, row) in enumerate(bank_data.iterrows()):
            if i == 0:
                continue
            
            change_pct = monthly_changes_pct.iloc[i]
            
            if change_pct > threshold:
                if current_period_type != 'QE':
                    if current_period_type == 'QT' and period_start:
                        qt_periods.append({
                            'start': period_start,
                            'end': bank_data.iloc[i-1]['date'],
                            'duration_months': (bank_data.iloc[i-1]['date'] - period_start).days / 30.44
                        })
                    current_period_type = 'QE'
                    period_start = bank_data.iloc[i]['date']
            elif change_pct < -threshold:
                if current_period_type != 'QT':
                    if current_period_type == 'QE' and period_start:
                        qe_periods.append({
                            'start': period_start,
                            'end': bank_data.iloc[i-1]['date'],
                            'duration_months': (bank_data.iloc[i-1]['date'] - period_start).days / 30.44
                        })
                    current_period_type = 'QT'
                    period_start = bank_data.iloc[i]['date']
        
        return {
            'qe_periods': qe_periods,
            'qt_periods': qt_periods,
            'current_policy': current_period_type or 'neutral'
        }
    
    def _determine_policy_stance(
        self,
        recent_change: float,
        yoy_change: float
    ) -> str:
        """Determine current policy stance based on balance sheet changes"""
        if recent_change > 0 and yoy_change > 5:
            return 'expansive'
        elif recent_change < 0 and yoy_change < -5:
            return 'contractive'
        elif abs(recent_change) < 0.01 and abs(yoy_change) < 1:
            return 'neutral'
        else:
            return 'mixed'
    
    def _aggregate_analysis(
        self,
        df: pd.DataFrame,
        date_column: str,
        asset_column: str
    ) -> Dict:
        """Calculate aggregate metrics across all central banks"""
        latest_date = df[date_column].max()
        latest_data = df[df[date_column] == latest_date]
        
        total_assets = latest_data[asset_column].sum()
        
        # Calculate year-over-year aggregate change
        one_year_ago = latest_date - pd.DateOffset(years=1)
        year_ago_data = df[df[date_column] <= one_year_ago]
        
        if not year_ago_data.empty:
            year_ago_date = year_ago_data[date_column].max()
            year_ago_total = df[df[date_column] == year_ago_date].groupby(date_column)[asset_column].sum().iloc[0]
            yoy_change = ((total_assets - year_ago_total) / year_ago_total) * 100
        else:
            yoy_change = None
        
        return {
            'total_assets': total_assets,
            'yoy_change_percent': round(yoy_change, 2) if yoy_change else None,
            'analysis_date': latest_date,
            'banks_analyzed': len(latest_data)
        }
    
    def calculate_policy_impact(
        self,
        balance_sheet_data: pd.DataFrame,
        policy_rate_data: Optional[pd.DataFrame] = None,
        date_column: str = 'date',
        asset_column: str = 'total_assets',
        rate_column: str = 'policy_rate'
    ) -> Dict:
        """
        Assess policy impact by combining balance sheet and rate changes
        
        Args:
            balance_sheet_data: Balance sheet time series
            policy_rate_data: Optional policy rate data
            date_column: Name of date column
            asset_column: Name of assets column
            rate_column: Name of rate column
            
        Returns:
            Policy impact assessment
        """
        try:
            balance_analysis = self.analyze_balance_sheet(
                balance_sheet_data, date_column, asset_column
            )
            
            impact_assessment = {
                'balance_sheet_impact': balance_analysis,
                'rate_impact': None
            }
            
            if policy_rate_data is not None:
                rate_analysis = self._analyze_rate_changes(
                    policy_rate_data, date_column, rate_column
                )
                impact_assessment['rate_impact'] = rate_analysis
            
            return impact_assessment
            
        except Exception as e:
            print(f"Error in policy impact calculation: {e}")
            return {'error': str(e)}
    
    def _analyze_rate_changes(
        self,
        rate_data: pd.DataFrame,
        date_column: str,
        rate_column: str
    ) -> Dict:
        """Analyze policy rate changes"""
        df = rate_data.copy()
        df[date_column] = pd.to_datetime(df[date_column])
        df = df.sort_values(date_column).reset_index(drop=True)
        
        df['rate_change'] = df[rate_column].diff()
        df['rate_change_bps'] = df['rate_change'] * 10000
        
        return {
            'current_rate': df[rate_column].iloc[-1],
            'recent_change_bps': df['rate_change_bps'].iloc[-1],
            'total_change_12m_bps': (df[rate_column].iloc[-1] - df[rate_column].iloc[-12]) * 10000 if len(df) >= 12 else None
        }
    
    def validate_balance_sheet_calculations(
        self,
        analysis_results: Dict,
        balance_sheet_data: pd.DataFrame,
        date_column: str = 'date',
        asset_column: str = 'total_assets',
        bank_column: str = 'central_bank'
    ) -> ValidationResult:
        """
        Validate balance sheet calculations by manual recalculation
        
        Args:
            analysis_results: Results from analyze_balance_sheet()
            balance_sheet_data: Original balance sheet data
            date_column: Name of date column
            asset_column: Name of assets column
            bank_column: Name of bank column
            
        Returns:
            ValidationResult object
        """
        if not VALIDATOR_AVAILABLE:
            return ValidationResult()
        
        result = ValidationResult()
        validator = OutputValidator()
        
        try:
            if 'by_bank' not in analysis_results:
                result.add_warning('balance_sheet_calculations', 'No bank data found in analysis results')
                return result
            
            df = balance_sheet_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values([bank_column, date_column]).reset_index(drop=True)
            
            for bank, bank_data in analysis_results['by_bank'].items():
                bank_df = df[df[bank_column] == bank].copy()
                bank_df = bank_df.sort_values(date_column).reset_index(drop=True)
                
                if len(bank_df) < 13:
                    result.add_warning(
                        f'{bank}_calculations',
                        f'Insufficient data for {bank} validation (need at least 13 periods)'
                    )
                    continue
                
                # Validate YoY change calculation
                if 'yoy_change_percent' in bank_data:
                    current_assets = bank_df[asset_column].iloc[-1]
                    assets_12m_ago = bank_df[asset_column].iloc[-13]
                    
                    if assets_12m_ago != 0:
                        reported_yoy = bank_data['yoy_change_percent']
                        is_valid, message = validator.validate_percent_change(
                            current_assets,
                            assets_12m_ago,
                            reported_yoy
                        )
                        
                        if is_valid:
                            result.add_passed(f'{bank}_yoy_change', f'{bank} YoY change validated: {reported_yoy:.2f}%')
                        else:
                            result.add_error(
                                f'{bank}_yoy_change',
                                f'{bank} YoY change: {message}',
                                {'reported': reported_yoy, 'bank': bank}
                            )
                
                # Validate policy stance consistency
                if 'policy_stance' in bank_data and 'recent_monthly_change' in bank_data:
                    policy_stance = bank_data['policy_stance']
                    monthly_change = bank_data['recent_monthly_change']
                    yoy_change = bank_data.get('yoy_change_percent', 0)
                    
                    stance_result = validator.validate_policy_stance_consistency(
                        policy_stance,
                        monthly_change,
                        yoy_change
                    )
                    result.errors.extend(stance_result.errors)
                    result.warnings.extend(stance_result.warnings)
                    result.passed.extend(stance_result.passed)
            
        except Exception as e:
            result.add_error('balance_sheet_calculations_validation', f'Error validating balance sheet calculations: {str(e)}')
        
        return result
    
    def validate_output(
        self,
        analysis_results: Dict,
        balance_sheet_data: pd.DataFrame,
        date_column: str = 'date',
        asset_column: str = 'total_assets',
        bank_column: str = 'central_bank'
    ) -> ValidationResult:
        """
        Validate all output from central bank analysis
        
        Args:
            analysis_results: Results from analyze_balance_sheet()
            balance_sheet_data: Original balance sheet data
            date_column: Name of date column
            asset_column: Name of assets column
            bank_column: Name of bank column
            
        Returns:
            ValidationResult object with all validation checks
        """
        if not VALIDATOR_AVAILABLE:
            return ValidationResult()
        
        result = ValidationResult()
        
        try:
            # Validate balance sheet calculations
            calc_result = self.validate_balance_sheet_calculations(
                analysis_results,
                balance_sheet_data,
                date_column,
                asset_column,
                bank_column
            )
            result.errors.extend(calc_result.errors)
            result.warnings.extend(calc_result.warnings)
            result.passed.extend(calc_result.passed)
            
            result.is_valid = len(result.errors) == 0
            
        except Exception as e:
            result.add_error('output_validation', f'Error validating output: {str(e)}')
        
        return result


if __name__ == "__main__":
    # Example usage
    print("Central Bank Analyzer")
    print("=" * 50)
    print("This script analyzes central bank balance sheets and policy actions")
    print("Import this module and use CentralBankAnalyzer class in your analysis")
