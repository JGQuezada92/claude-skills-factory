#!/usr/bin/env python3
"""
Asset Price Correlation Analyzer

Performs correlation analysis between liquidity conditions and asset prices.
Distinguishes between liquidity-driven moves and fundamental-driven moves.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


class AssetPriceCorrelationAnalyzer:
    """Analyze correlations between liquidity and asset prices"""
    
    def __init__(self):
        self.asset_classes = ['equities', 'bonds', 'commodities', 'fx']
    
    def analyze_liquidity_asset_correlation(
        self,
        liquidity_data: pd.DataFrame,
        asset_data: pd.DataFrame,
        date_column: str = 'date',
        liquidity_column: str = 'liquidity_index',
        asset_price_column: str = 'asset_price',
        asset_class: str = 'equities'
    ) -> Dict:
        """
        Analyze correlation between liquidity and asset prices
        
        Args:
            liquidity_data: DataFrame with liquidity time series
            asset_data: DataFrame with asset price time series
            date_column: Name of date column
            liquidity_column: Name of liquidity index column
            asset_price_column: Name of asset price column
            asset_class: Type of asset (equities, bonds, commodities, fx)
            
        Returns:
            Dictionary with correlation analysis results
        """
        try:
            # Merge dataframes
            merged = pd.merge(
                liquidity_data[[date_column, liquidity_column]],
                asset_data[[date_column, asset_price_column]],
                on=date_column,
                how='inner'
            )
            
            merged = merged.sort_values(date_column).reset_index(drop=True)
            
            # Calculate returns
            merged['liquidity_return'] = merged[liquidity_column].pct_change()
            merged['asset_return'] = merged[asset_price_column].pct_change()
            
            # Calculate levels correlation
            levels_correlation = merged[liquidity_column].corr(merged[asset_price_column])
            
            # Calculate returns correlation
            returns_correlation = merged['liquidity_return'].corr(merged['asset_return'])
            
            # Rolling correlation (12-month)
            merged['rolling_correlation'] = merged['liquidity_return'].rolling(window=12).corr(merged['asset_return'])
            current_rolling_corr = merged['rolling_correlation'].iloc[-1]
            
            # Lag analysis (liquidity leading asset prices)
            lag_correlations = {}
            for lag in [1, 3, 6, 12]:
                if len(merged) > lag:
                    lag_corr = merged['liquidity_return'].shift(lag).corr(merged['asset_return'])
                    lag_correlations[f'{lag}_month_lag'] = round(lag_corr, 3)
            
            # Determine if liquidity-driven
            is_liquidity_driven = abs(returns_correlation) > 0.3 or abs(current_rolling_corr) > 0.3
            
            return {
                'asset_class': asset_class,
                'levels_correlation': round(levels_correlation, 3),
                'returns_correlation': round(returns_correlation, 3),
                'current_rolling_correlation_12m': round(current_rolling_corr, 3) if not np.isnan(current_rolling_corr) else None,
                'lag_correlations': lag_correlations,
                'is_liquidity_driven': is_liquidity_driven,
                'liquidity_sensitivity': 'high' if abs(returns_correlation) > 0.5 else 'medium' if abs(returns_correlation) > 0.3 else 'low',
                'data_points': len(merged),
                'analysis_date': datetime.now()
            }
            
        except Exception as e:
            print(f"Error in liquidity-asset correlation analysis: {e}")
            return {'error': str(e)}
    
    def analyze_multiple_assets(
        self,
        liquidity_data: pd.DataFrame,
        asset_data_dict: Dict[str, pd.DataFrame],
        date_column: str = 'date',
        liquidity_column: str = 'liquidity_index',
        price_column: str = 'price'
    ) -> Dict:
        """
        Analyze correlations for multiple asset classes
        
        Args:
            liquidity_data: Liquidity time series
            asset_data_dict: Dictionary mapping asset class names to DataFrames
            date_column: Name of date column
            liquidity_column: Name of liquidity column
            price_column: Name of price column in asset DataFrames
            
        Returns:
            Dictionary with correlations for all asset classes
        """
        results = {}
        
        for asset_class, asset_df in asset_data_dict.items():
            correlation_result = self.analyze_liquidity_asset_correlation(
                liquidity_data,
                asset_df,
                date_column,
                liquidity_column,
                price_column,
                asset_class
            )
            results[asset_class] = correlation_result
        
        # Cross-asset comparison
        correlations_summary = {
            asset: result.get('returns_correlation', 0)
            for asset, result in results.items()
        }
        
        results['summary'] = {
            'most_liquidity_sensitive': max(correlations_summary, key=lambda x: abs(correlations_summary[x])),
            'least_liquidity_sensitive': min(correlations_summary, key=lambda x: abs(correlations_summary[x])),
            'average_correlation': np.mean([abs(v) for v in correlations_summary.values()])
        }
        
        return results
    
    def identify_liquidity_driven_moves(
        self,
        liquidity_data: pd.DataFrame,
        asset_data: pd.DataFrame,
        date_column: str = 'date',
        liquidity_column: str = 'liquidity_index',
        asset_price_column: str = 'asset_price',
        threshold: float = 0.3
    ) -> List[Dict]:
        """
        Identify periods where asset price moves were liquidity-driven
        
        Args:
            liquidity_data: Liquidity time series
            asset_data: Asset price time series
            date_column: Name of date column
            liquidity_column: Name of liquidity column
            asset_price_column: Name of asset price column
            threshold: Correlation threshold for liquidity-driven moves
            
        Returns:
            List of periods with liquidity-driven moves
        """
        try:
            merged = pd.merge(
                liquidity_data[[date_column, liquidity_column]],
                asset_data[[date_column, asset_price_column]],
                on=date_column,
                how='inner'
            )
            
            merged = merged.sort_values(date_column).reset_index(drop=True)
            
            # Calculate rolling correlation
            merged['liquidity_return'] = merged[liquidity_column].pct_change()
            merged['asset_return'] = merged[asset_price_column].pct_change()
            merged['rolling_correlation'] = merged['liquidity_return'].rolling(window=6).corr(merged['asset_return'])
            
            # Identify periods with high correlation
            merged['liquidity_driven'] = merged['rolling_correlation'].abs() > threshold
            
            liquidity_periods = []
            in_period = False
            period_start = None
            
            for idx, row in merged.iterrows():
                if row['liquidity_driven'] and not in_period:
                    in_period = True
                    period_start = row[date_column]
                elif not row['liquidity_driven'] and in_period:
                    in_period = False
                    period_data = merged[(merged[date_column] >= period_start) & (merged[date_column] < row[date_column])]
                    
                    liquidity_periods.append({
                        'start_date': period_start,
                        'end_date': merged.iloc[idx-1][date_column],
                        'duration_days': (merged.iloc[idx-1][date_column] - period_start).days,
                        'avg_correlation': period_data['rolling_correlation'].mean(),
                        'liquidity_change': (period_data[liquidity_column].iloc[-1] - period_data[liquidity_column].iloc[0]) / period_data[liquidity_column].iloc[0] * 100,
                        'asset_change': (period_data[asset_price_column].iloc[-1] - period_data[asset_price_column].iloc[0]) / period_data[asset_price_column].iloc[0] * 100
                    })
            
            return liquidity_periods
            
        except Exception as e:
            print(f"Error identifying liquidity-driven moves: {e}")
            return []
    
    def forecast_asset_price_impact(
        self,
        liquidity_forecast: pd.DataFrame,
        historical_correlation: float,
        date_column: str = 'date',
        liquidity_column: str = 'liquidity_index'
    ) -> Dict:
        """
        Forecast asset price impact based on liquidity forecast
        
        Args:
            liquidity_forecast: Forecasted liquidity time series
            historical_correlation: Historical correlation coefficient
            date_column: Name of date column
            liquidity_column: Name of liquidity column
            
        Returns:
            Forecasted asset price impact
        """
        try:
            df = liquidity_forecast.copy()
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column).reset_index(drop=True)
            
            # Calculate liquidity change
            df['liquidity_change'] = df[liquidity_column].pct_change()
            
            # Estimate asset price impact based on correlation
            df['estimated_asset_return'] = df['liquidity_change'] * historical_correlation
            
            # Project cumulative impact
            df['cumulative_impact'] = (1 + df['estimated_asset_return']).cumprod() - 1
            
            return {
                'forecasted_liquidity_change': round(df['liquidity_change'].iloc[-1] * 100, 2),
                'estimated_asset_return': round(df['estimated_asset_return'].iloc[-1] * 100, 2),
                'cumulative_impact_forecast': round(df['cumulative_impact'].iloc[-1] * 100, 2),
                'forecast_horizon_months': len(df),
                'confidence_level': 'medium'  # Based on historical correlation strength
            }
            
        except Exception as e:
            print(f"Error in asset price impact forecast: {e}")
            return {'error': str(e)}


if __name__ == "__main__":
    # Example usage
    print("Asset Price Correlation Analyzer")
    print("=" * 50)
    print("This script analyzes correlations between liquidity and asset prices")
    print("Import this module and use AssetPriceCorrelationAnalyzer class in your analysis")
