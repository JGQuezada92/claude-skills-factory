#!/usr/bin/env python3
"""
Liquidity Cycle Analyzer

Performs quantitative cycle identification and phase determination based on 
Michael Howell's CrossBorder Capital methodology. Identifies 60-65 month 
liquidity cycles and determines current cycle phase.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta
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


class LiquidityCycleAnalyzer:
    """Analyze global liquidity cycles using Michael Howell's framework"""
    
    def __init__(self):
        self.typical_cycle_length = 62  # 60-65 month average
        self.cycle_phases = ['expansion', 'peak', 'contraction', 'trough']
    
    def identify_cycles(
        self,
        liquidity_data: pd.DataFrame,
        date_column: str = 'date',
        value_column: str = 'liquidity_index'
    ) -> Dict:
        """
        Identify liquidity cycles from historical data
        
        Args:
            liquidity_data: DataFrame with date and liquidity index
            date_column: Name of date column
            value_column: Name of liquidity value column
            
        Returns:
            Dictionary with cycle identification results
        """
        try:
            df = liquidity_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            # Calculate year-over-year growth rate
            df['yoy_growth'] = df[value_column].pct_change(periods=12) * 100
            
            # Identify peaks and troughs
            peaks = self._find_peaks(df, value_column)
            troughs = self._find_troughs(df, value_column)
            
            # Identify cycle turning points
            turning_points = sorted(peaks + troughs, key=lambda x: x['date'])
            
            # Calculate cycle characteristics
            cycles = self._calculate_cycle_metrics(df, turning_points, date_column, value_column)
            
            # Determine current cycle phase
            current_phase = self._determine_current_phase(df, cycles, date_column, value_column)
            
            return {
                'cycles': cycles,
                'current_phase': current_phase,
                'turning_points': turning_points,
                'average_cycle_length': np.mean([c['length_months'] for c in cycles]) if cycles else None,
                'total_cycles_identified': len(cycles)
            }
            
        except Exception as e:
            print(f"Error in cycle identification: {e}")
            return {'error': str(e)}
    
    def _find_peaks(self, df: pd.DataFrame, value_column: str, window: int = 6) -> List[Dict]:
        """Find local peaks in liquidity data"""
        peaks = []
        for i in range(window, len(df) - window):
            if (df[value_column].iloc[i] > df[value_column].iloc[i-window:i].max() and
                df[value_column].iloc[i] > df[value_column].iloc[i+1:i+window+1].max()):
                peaks.append({
                    'date': df.iloc[i]['date'],
                    'value': df[value_column].iloc[i],
                    'type': 'peak'
                })
        return peaks
    
    def _find_troughs(self, df: pd.DataFrame, value_column: str, window: int = 6) -> List[Dict]:
        """Find local troughs in liquidity data"""
        troughs = []
        for i in range(window, len(df) - window):
            if (df[value_column].iloc[i] < df[value_column].iloc[i-window:i].min() and
                df[value_column].iloc[i] < df[value_column].iloc[i+1:i+window+1].min()):
                troughs.append({
                    'date': df.iloc[i]['date'],
                    'value': df[value_column].iloc[i],
                    'type': 'trough'
                })
        return troughs
    
    def _calculate_cycle_metrics(
        self,
        df: pd.DataFrame,
        turning_points: List[Dict],
        date_column: str,
        value_column: str
    ) -> List[Dict]:
        """Calculate metrics for each identified cycle"""
        cycles = []
        
        for i in range(len(turning_points) - 1):
            start = turning_points[i]
            end = turning_points[i + 1]
            
            start_idx = df[df[date_column] == start['date']].index[0]
            end_idx = df[df[date_column] == end['date']].index[0]
            
            cycle_data = df.iloc[start_idx:end_idx+1]
            
            length_months = (end['date'] - start['date']).days / 30.44
            
            cycles.append({
                'cycle_number': i + 1,
                'start_date': start['date'],
                'end_date': end['date'],
                'start_value': start['value'],
                'end_value': end['value'],
                'length_months': length_months,
                'peak_value': cycle_data[value_column].max(),
                'trough_value': cycle_data[value_column].min(),
                'amplitude': cycle_data[value_column].max() - cycle_data[value_column].min(),
                'avg_growth_rate': cycle_data['yoy_growth'].mean() if 'yoy_growth' in cycle_data.columns else None
            })
        
        return cycles
    
    def _determine_current_phase(
        self,
        df: pd.DataFrame,
        cycles: List[Dict],
        date_column: str,
        value_column: str
    ) -> Dict:
        """Determine current cycle phase and positioning"""
        if not cycles:
            return {'phase': 'unknown', 'confidence': 'low'}
        
        current_date = df[date_column].max()
        current_value = df[value_column].iloc[-1]
        
        # Find most recent cycle
        recent_cycle = cycles[-1] if cycles else None
        
        if not recent_cycle:
            return {'phase': 'unknown', 'confidence': 'low'}
        
        # Calculate position in current cycle
        cycle_start = recent_cycle['start_date']
        months_elapsed = (current_date - cycle_start).days / 30.44
        cycle_length = recent_cycle['length_months']
        cycle_completion = (months_elapsed / cycle_length) * 100 if cycle_length > 0 else 0
        
        # Determine phase based on position and trend
        recent_trend = df[value_column].iloc[-6:].pct_change().mean() if len(df) >= 6 else 0
        
        if cycle_completion < 25:
            phase = 'expansion'
        elif cycle_completion < 50:
            phase = 'peak' if recent_trend < 0 else 'expansion'
        elif cycle_completion < 75:
            phase = 'contraction'
        else:
            phase = 'trough' if recent_trend > 0 else 'contraction'
        
        # Forecast next turning point
        months_to_turning_point = cycle_length - months_elapsed if cycle_length > months_elapsed else None
        forecasted_turning_point = current_date + timedelta(days=months_to_turning_point * 30.44) if months_to_turning_point else None
        
        return {
            'phase': phase,
            'cycle_completion_percent': round(cycle_completion, 2),
            'months_elapsed': round(months_elapsed, 2),
            'current_value': current_value,
            'recent_trend': round(recent_trend * 100, 2),
            'forecasted_turning_point': forecasted_turning_point,
            'months_to_turning_point': round(months_to_turning_point, 2) if months_to_turning_point else None,
            'confidence': 'high' if cycle_completion > 20 else 'medium'
        }
    
    def forecast_cycle_turning_point(
        self,
        cycles: List[Dict],
        current_phase: Dict
    ) -> Dict:
        """
        Forecast next cycle turning point based on historical patterns
        
        Args:
            cycles: List of identified cycles
            current_phase: Current phase information
            
        Returns:
            Forecast dictionary with turning point predictions
        """
        if not cycles:
            return {'error': 'No cycles available for forecasting'}
        
        avg_cycle_length = np.mean([c['length_months'] for c in cycles])
        
        return {
            'average_cycle_length_months': round(avg_cycle_length, 2),
            'current_phase': current_phase.get('phase'),
            'forecasted_turning_point': current_phase.get('forecasted_turning_point'),
            'months_to_turning_point': current_phase.get('months_to_turning_point'),
            'confidence_level': current_phase.get('confidence', 'medium')
        }
    
    def validate_cycle_identification(
        self,
        cycles: List[Dict],
        liquidity_data: pd.DataFrame,
        date_column: str = 'date'
    ) -> ValidationResult:
        """
        Validate cycle identification results
        
        Args:
            cycles: List of identified cycles
            liquidity_data: Original liquidity data
            date_column: Name of date column
            
        Returns:
            ValidationResult object
        """
        if not VALIDATOR_AVAILABLE:
            return ValidationResult()
        
        result = ValidationResult()
        validator = OutputValidator()
        
        try:
            # Validate cycle lengths are reasonable (55-70 months)
            for i, cycle in enumerate(cycles, 1):
                length = cycle.get('length_months', 0)
                is_valid, message = validator.validate_cycle_length(length)
                
                if not is_valid:
                    result.add_error(
                        'cycle_length_validation',
                        f'Cycle {i}: {message}',
                        {'cycle_number': i, 'length_months': length}
                    )
                else:
                    result.add_passed(f'cycle_{i}_length', f'Cycle {i} length validated: {length:.2f} months')
                
                # Verify cycle dates are consistent
                start_date = cycle.get('start_date')
                end_date = cycle.get('end_date')
                
                if start_date and end_date:
                    manual_length = (end_date - start_date).days / 30.44
                    length_diff = abs(manual_length - length)
                    
                    if length_diff > 1.0:  # 1 month tolerance
                        result.add_error(
                            'cycle_date_consistency',
                            f'Cycle {i}: Length mismatch between calculation ({length:.2f}) and dates ({manual_length:.2f})',
                            {'calculated': length, 'from_dates': manual_length, 'difference': length_diff}
                        )
                    else:
                        result.add_passed(f'cycle_{i}_dates', f'Cycle {i} dates are consistent')
            
            # Validate average cycle length
            if cycles:
                avg_length = np.mean([c['length_months'] for c in cycles])
                is_valid, message = validator.validate_cycle_length(avg_length)
                
                if not is_valid:
                    result.add_warning('average_cycle_length', f'Average cycle length: {message}')
                else:
                    result.add_passed('average_cycle_length', f'Average cycle length validated: {avg_length:.2f} months')
            
        except Exception as e:
            result.add_error('cycle_identification_validation', f'Error validating cycles: {str(e)}')
        
        return result
    
    def validate_output(
        self,
        analysis_results: Dict,
        liquidity_data: pd.DataFrame,
        date_column: str = 'date',
        value_column: str = 'liquidity_index'
    ) -> ValidationResult:
        """
        Validate all output from cycle analysis
        
        Args:
            analysis_results: Results from identify_cycles()
            liquidity_data: Original liquidity data
            date_column: Name of date column
            value_column: Name of value column
            
        Returns:
            ValidationResult object with all validation checks
        """
        if not VALIDATOR_AVAILABLE:
            return ValidationResult()
        
        result = ValidationResult()
        validator = OutputValidator()
        
        try:
            # Validate cycles if available
            if 'cycles' in analysis_results:
                cycle_result = self.validate_cycle_identification(
                    analysis_results['cycles'],
                    liquidity_data,
                    date_column
                )
                result.errors.extend(cycle_result.errors)
                result.warnings.extend(cycle_result.warnings)
                result.passed.extend(cycle_result.passed)
            
            # Validate cycle phase consistency
            if 'current_phase' in analysis_results:
                phase_result = validator.validate_cycle_phase_consistency(
                    analysis_results,
                    liquidity_data,
                    value_column,
                    date_column
                )
                result.errors.extend(phase_result.errors)
                result.warnings.extend(phase_result.warnings)
                result.passed.extend(phase_result.passed)
            
            result.is_valid = len(result.errors) == 0
            
        except Exception as e:
            result.add_error('output_validation', f'Error validating output: {str(e)}')
        
        return result


if __name__ == "__main__":
    # Example usage
    print("Liquidity Cycle Analyzer")
    print("=" * 50)
    print("This script analyzes liquidity cycles using Michael Howell's methodology")
    print("Import this module and use LiquidityCycleAnalyzer class in your analysis")
