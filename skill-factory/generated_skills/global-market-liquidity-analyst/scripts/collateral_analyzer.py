#!/usr/bin/env python3
"""
Collateral Analyzer

Monitors collateral market health through volatility metrics, repo spreads, 
and collateral quality indicators. Identifies periods of collateral market stress.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


class CollateralAnalyzer:
    """Analyze collateral market health and stress indicators"""
    
    def __init__(self):
        self.stress_thresholds = {
            'high_volatility': 0.20,  # 20% volatility threshold
            'wide_repo_spread': 50,  # 50 bps repo spread threshold
            'low_quality_ratio': 0.8  # 80% quality threshold
        }
    
    def analyze_collateral_health(
        self,
        bond_data: pd.DataFrame,
        repo_data: Optional[pd.DataFrame] = None,
        date_column: str = 'date',
        bond_yield_column: str = 'bond_yield',
        volatility_window: int = 30
    ) -> Dict:
        """
        Analyze collateral market health through bond volatility and repo spreads
        
        Args:
            bond_data: DataFrame with bond yield time series
            repo_data: Optional DataFrame with repo market data
            date_column: Name of date column
            bond_yield_column: Name of bond yield column
            volatility_window: Window for volatility calculation (days)
            
        Returns:
            Dictionary with collateral health analysis
        """
        try:
            df = bond_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            # Calculate volatility
            df['yield_change'] = df[bond_yield_column].diff()
            df['volatility'] = df['yield_change'].rolling(window=volatility_window).std() * np.sqrt(252) * 100
            
            # Current metrics
            current_yield = df[bond_yield_column].iloc[-1]
            current_volatility = df['volatility'].iloc[-1]
            avg_volatility = df['volatility'].mean()
            
            # Volatility stress indicator
            volatility_stress = current_volatility / avg_volatility if avg_volatility > 0 else 1.0
            
            # Repo analysis if available
            repo_analysis = None
            if repo_data is not None:
                repo_analysis = self._analyze_repo_markets(repo_data, date_column)
            
            # Overall health assessment
            health_score = self._calculate_health_score(current_volatility, repo_analysis)
            
            return {
                'current_yield': current_yield,
                'current_volatility': round(current_volatility, 2),
                'average_volatility': round(avg_volatility, 2),
                'volatility_stress_ratio': round(volatility_stress, 2),
                'volatility_stress_level': 'high' if volatility_stress > 1.5 else 'medium' if volatility_stress > 1.2 else 'low',
                'repo_analysis': repo_analysis,
                'health_score': round(health_score, 2),
                'health_status': 'healthy' if health_score > 70 else 'moderate' if health_score > 50 else 'stressed',
                'analysis_date': datetime.now()
            }
            
        except Exception as e:
            print(f"Error in collateral health analysis: {e}")
            return {'error': str(e)}
    
    def _analyze_repo_markets(
        self,
        repo_data: pd.DataFrame,
        date_column: str = 'date',
        repo_rate_column: str = 'repo_rate',
        risk_free_column: Optional[str] = None
    ) -> Dict:
        """Analyze repo market conditions"""
        df = repo_data.copy()
        df[date_column] = pd.to_datetime(df[date_column])
        df = df.sort_values(date_column).reset_index(drop=True)
        
        # Calculate repo spread if risk-free rate available
        if risk_free_column and risk_free_column in df.columns:
            df['repo_spread'] = (df[repo_rate_column] - df[risk_free_column]) * 10000  # Convert to bps
            current_spread = df['repo_spread'].iloc[-1]
            avg_spread = df['repo_spread'].mean()
            spread_stress = current_spread / avg_spread if avg_spread > 0 else 1.0
        else:
            current_spread = None
            avg_spread = None
            spread_stress = None
        
        current_repo_rate = df[repo_rate_column].iloc[-1]
        
        return {
            'current_repo_rate': current_repo_rate,
            'current_repo_spread_bps': round(current_spread, 2) if current_spread else None,
            'average_repo_spread_bps': round(avg_spread, 2) if avg_spread else None,
            'spread_stress_ratio': round(spread_stress, 2) if spread_stress else None,
            'repo_stress_level': 'high' if current_spread and current_spread > 50 else 'medium' if current_spread and current_spread > 25 else 'low' if current_spread else 'unknown'
        }
    
    def _calculate_health_score(
        self,
        volatility: float,
        repo_analysis: Optional[Dict]
    ) -> float:
        """Calculate overall collateral health score (0-100)"""
        # Base score from volatility (lower volatility = higher score)
        volatility_score = max(0, 100 - (volatility * 10))
        
        # Adjust for repo conditions if available
        if repo_analysis and repo_analysis.get('repo_stress_level'):
            repo_stress = repo_analysis['repo_stress_level']
            if repo_stress == 'high':
                volatility_score *= 0.7
            elif repo_stress == 'medium':
                volatility_score *= 0.85
        
        return volatility_score
    
    def identify_stress_periods(
        self,
        bond_data: pd.DataFrame,
        repo_data: Optional[pd.DataFrame] = None,
        date_column: str = 'date',
        bond_yield_column: str = 'bond_yield',
        stress_threshold: float = 1.5
    ) -> List[Dict]:
        """
        Identify periods of collateral market stress
        
        Args:
            bond_data: Bond yield time series
            repo_data: Optional repo market data
            date_column: Name of date column
            bond_yield_column: Name of bond yield column
            stress_threshold: Threshold multiplier for stress detection
            
        Returns:
            List of stress period dictionaries
        """
        try:
            df = bond_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            # Calculate rolling volatility
            df['volatility'] = df[bond_yield_column].diff().rolling(window=30).std() * np.sqrt(252) * 100
            avg_volatility = df['volatility'].mean()
            
            # Identify stress periods
            df['stress_indicator'] = df['volatility'] > (avg_volatility * stress_threshold)
            
            stress_periods = []
            in_stress = False
            stress_start = None
            
            for idx, row in df.iterrows():
                if row['stress_indicator'] and not in_stress:
                    in_stress = True
                    stress_start = row[date_column]
                elif not row['stress_indicator'] and in_stress:
                    in_stress = False
                    stress_periods.append({
                        'start_date': stress_start,
                        'end_date': df.iloc[idx-1][date_column],
                        'duration_days': (df.iloc[idx-1][date_column] - stress_start).days,
                        'peak_volatility': df.iloc[stress_start:idx]['volatility'].max()
                    })
            
            # Handle ongoing stress period
            if in_stress:
                stress_periods.append({
                    'start_date': stress_start,
                    'end_date': df[date_column].iloc[-1],
                    'duration_days': (df[date_column].iloc[-1] - stress_start).days,
                    'peak_volatility': df.loc[df[date_column] >= stress_start, 'volatility'].max(),
                    'ongoing': True
                })
            
            return stress_periods
            
        except Exception as e:
            print(f"Error in stress period identification: {e}")
            return []
    
    def calculate_margin_requirements_impact(
        self,
        volatility_data: pd.DataFrame,
        margin_data: Optional[pd.DataFrame] = None,
        date_column: str = 'date',
        volatility_column: str = 'volatility'
    ) -> Dict:
        """
        Assess impact of margin requirements on liquidity
        
        Args:
            volatility_data: Volatility time series
            margin_data: Optional margin requirement data
            date_column: Name of date column
            volatility_column: Name of volatility column
            
        Returns:
            Margin requirement impact analysis
        """
        try:
            df = volatility_data.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            # Estimate margin requirements based on volatility (higher volatility = higher margins)
            df['estimated_margin'] = df[volatility_column] * 2  # Simplified estimation
            
            if margin_data is not None:
                merged = pd.merge(
                    df[[date_column, volatility_column]],
                    margin_data,
                    on=date_column,
                    how='inner'
                )
                current_margin = merged['margin_requirement'].iloc[-1] if 'margin_requirement' in merged.columns else None
            else:
                current_margin = None
            
            current_volatility = df[volatility_column].iloc[-1]
            estimated_margin = df['estimated_margin'].iloc[-1]
            
            return {
                'current_volatility': round(current_volatility, 2),
                'estimated_margin_requirement': round(estimated_margin, 2),
                'actual_margin_requirement': current_margin,
                'liquidity_impact': 'high' if estimated_margin > 40 else 'medium' if estimated_margin > 20 else 'low'
            }
            
        except Exception as e:
            print(f"Error in margin requirement impact calculation: {e}")
            return {'error': str(e)}


if __name__ == "__main__":
    # Example usage
    print("Collateral Analyzer")
    print("=" * 50)
    print("This script monitors collateral market health and stress indicators")
    print("Import this module and use CollateralAnalyzer class in your analysis")
