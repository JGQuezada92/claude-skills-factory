"""
Variance Analyzer Script
Budget vs actual variance analysis and performance attribution

Capabilities:
- Calculate variances (actual vs budget/forecast/prior period)
- Decompose variances (volume, price, mix effects)
- Generate variance bridges and waterfall analysis
- Root cause analysis for material variances
- Forecast accuracy assessment
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import pandas as pd


@dataclass
class Variance:
    """Data class for variance analysis"""
    line_item: str
    actual: float
    budget: float
    variance_amount: float
    variance_percent: float
    is_favorable: bool
    materiality: str  # 'high', 'medium', 'low'
    explanation: Optional[str] = None


class VarianceAnalyzer:
    """
    Comprehensive variance analysis toolkit
    """
    
    def __init__(self, materiality_threshold: float = 5.0):
        """
        Initialize variance analyzer
        
        Args:
            materiality_threshold: Variance % threshold for flagging (default: 5%)
        """
        self.materiality_threshold = materiality_threshold
    
    # =============================================================================
    # BASIC VARIANCE ANALYSIS
    # =============================================================================
    
    def calculate_variance(self, actual: float, budget: float, 
                          line_item: str, 
                          favorable_when_higher: bool = True) -> Variance:
        """
        Calculate variance for a single line item
        
        Args:
            actual: Actual value
            budget: Budgeted/forecasted value
            line_item: Name of line item
            favorable_when_higher: True for revenue, False for expenses
            
        Returns:
            Variance object with analysis
        """
        variance_amount = actual - budget
        variance_percent = (variance_amount / budget * 100) if budget != 0 else None
        
        # Determine if favorable
        if favorable_when_higher:
            is_favorable = variance_amount > 0
        else:
            is_favorable = variance_amount < 0
        
        # Determine materiality
        if variance_percent is None:
            materiality = 'unknown'
        elif abs(variance_percent) > self.materiality_threshold * 2:
            materiality = 'high'
        elif abs(variance_percent) > self.materiality_threshold:
            materiality = 'medium'
        else:
            materiality = 'low'
        
        return Variance(
            line_item=line_item,
            actual=actual,
            budget=budget,
            variance_amount=variance_amount,
            variance_percent=variance_percent,
            is_favorable=is_favorable,
            materiality=materiality
        )
    
    def calculate_income_statement_variances(self, actual: Dict, 
                                           budget: Dict) -> List[Variance]:
        """
        Calculate variances for all income statement line items
        
        Args:
            actual: Dictionary with actual P&L values
            budget: Dictionary with budgeted P&L values
            
        Returns:
            List of Variance objects
        """
        variances = []
        
        # Revenue (favorable when higher)
        if 'revenue' in actual and 'revenue' in budget:
            variances.append(
                self.calculate_variance(
                    actual['revenue'],
                    budget['revenue'],
                    'Revenue',
                    favorable_when_higher=True
                )
            )
        
        # COGS (favorable when lower)
        if 'cogs' in actual and 'cogs' in budget:
            variances.append(
                self.calculate_variance(
                    actual['cogs'],
                    budget['cogs'],
                    'Cost of Goods Sold',
                    favorable_when_higher=False
                )
            )
        
        # Gross Profit (favorable when higher)
        if 'gross_profit' in actual and 'gross_profit' in budget:
            variances.append(
                self.calculate_variance(
                    actual['gross_profit'],
                    budget['gross_profit'],
                    'Gross Profit',
                    favorable_when_higher=True
                )
            )
        
        # Operating Expenses (favorable when lower)
        if 'operating_expenses' in actual and 'operating_expenses' in budget:
            variances.append(
                self.calculate_variance(
                    actual['operating_expenses'],
                    budget['operating_expenses'],
                    'Operating Expenses',
                    favorable_when_higher=False
                )
            )
        
        # Operating Income (favorable when higher)
        if 'operating_income' in actual and 'operating_income' in budget:
            variances.append(
                self.calculate_variance(
                    actual['operating_income'],
                    budget['operating_income'],
                    'Operating Income',
                    favorable_when_higher=True
                )
            )
        
        # Net Income (favorable when higher)
        if 'net_income' in actual and 'net_income' in budget:
            variances.append(
                self.calculate_variance(
                    actual['net_income'],
                    budget['net_income'],
                    'Net Income',
                    favorable_when_higher=True
                )
            )
        
        return variances
    
    # =============================================================================
    # REVENUE VARIANCE DECOMPOSITION
    # =============================================================================
    
    def decompose_revenue_variance(self, 
                                   actual_volume: float,
                                   budget_volume: float,
                                   actual_price: float,
                                   budget_price: float) -> Dict[str, float]:
        """
        Decompose revenue variance into volume and price effects
        
        Revenue Variance = (Actual Volume × Actual Price) - (Budget Volume × Budget Price)
        
        Volume Variance = (Actual Volume - Budget Volume) × Budget Price
        Price Variance = (Actual Price - Budget Price) × Actual Volume
        
        Args:
            actual_volume: Actual units sold
            budget_volume: Budgeted units
            actual_price: Actual average price
            budget_price: Budgeted average price
            
        Returns:
            Dictionary with volume and price variances
        """
        actual_revenue = actual_volume * actual_price
        budget_revenue = budget_volume * budget_price
        total_variance = actual_revenue - budget_revenue
        
        volume_variance = (actual_volume - budget_volume) * budget_price
        price_variance = (actual_price - budget_price) * actual_volume
        
        return {
            'total_variance': total_variance,
            'volume_variance': volume_variance,
            'price_variance': price_variance,
            'volume_effect_pct': (volume_variance / total_variance * 100) if total_variance != 0 else 0,
            'price_effect_pct': (price_variance / total_variance * 100) if total_variance != 0 else 0
        }
    
    def decompose_revenue_variance_with_mix(self,
                                           actual_data: List[Dict],
                                           budget_data: List[Dict]) -> Dict:
        """
        Decompose revenue variance including mix effects for multiple products
        
        Args:
            actual_data: List of dicts with keys: product, volume, price
            budget_data: List of dicts with keys: product, volume, price
            
        Returns:
            Comprehensive variance decomposition
        """
        # Calculate totals
        actual_revenue = sum(item['volume'] * item['price'] for item in actual_data)
        budget_revenue = sum(item['volume'] * item['price'] for item in budget_data)
        total_variance = actual_revenue - budget_revenue
        
        # This is a simplified version - full mix variance requires more complex calculations
        return {
            'total_variance': total_variance,
            'actual_revenue': actual_revenue,
            'budget_revenue': budget_revenue,
            'variance_percent': (total_variance / budget_revenue * 100) if budget_revenue != 0 else None
        }
    
    # =============================================================================
    # MARGIN VARIANCE ANALYSIS
    # =============================================================================
    
    def analyze_margin_variance(self,
                               actual_revenue: float,
                               actual_cogs: float,
                               budget_revenue: float,
                               budget_cogs: float) -> Dict:
        """
        Analyze gross margin variance
        
        Returns:
            Dictionary with margin variance analysis
        """
        actual_margin = actual_revenue - actual_cogs
        budget_margin = budget_revenue - budget_cogs
        margin_variance = actual_margin - budget_margin
        
        actual_margin_pct = (actual_margin / actual_revenue * 100) if actual_revenue > 0 else 0
        budget_margin_pct = (budget_margin / budget_revenue * 100) if budget_revenue > 0 else 0
        margin_pct_variance = actual_margin_pct - budget_margin_pct
        
        return {
            'actual_margin': actual_margin,
            'budget_margin': budget_margin,
            'margin_variance': margin_variance,
            'actual_margin_pct': actual_margin_pct,
            'budget_margin_pct': budget_margin_pct,
            'margin_pct_variance': margin_pct_variance,
            'is_favorable': margin_variance > 0
        }
    
    # =============================================================================
    # COST VARIANCE ANALYSIS
    # =============================================================================
    
    def analyze_cost_variance(self,
                            actual_cost: float,
                            budget_cost: float,
                            actual_volume: float,
                            budget_volume: float) -> Dict:
        """
        Decompose cost variance into spending and efficiency components
        
        Spending Variance = (Actual Rate - Budget Rate) × Actual Volume
        Efficiency Variance = (Actual Volume - Budget Volume) × Budget Rate
        
        Args:
            actual_cost: Total actual cost
            actual_volume: Actual production/activity volume
            budget_cost: Total budgeted cost
            budget_volume: Budgeted volume
            
        Returns:
            Dictionary with cost variance components
        """
        actual_rate = actual_cost / actual_volume if actual_volume > 0 else 0
        budget_rate = budget_cost / budget_volume if budget_volume > 0 else 0
        
        spending_variance = (actual_rate - budget_rate) * actual_volume
        efficiency_variance = (actual_volume - budget_volume) * budget_rate
        total_variance = actual_cost - budget_cost
        
        return {
            'total_variance': total_variance,
            'spending_variance': spending_variance,
            'efficiency_variance': efficiency_variance,
            'actual_rate': actual_rate,
            'budget_rate': budget_rate,
            'rate_variance': actual_rate - budget_rate,
            'volume_variance': actual_volume - budget_volume
        }
    
    # =============================================================================
    # VARIANCE BRIDGE ANALYSIS
    # =============================================================================
    
    def create_variance_bridge(self,
                              starting_value: float,
                              components: List[Dict]) -> Dict:
        """
        Create waterfall/bridge analysis showing how components bridge from budget to actual
        
        Args:
            starting_value: Starting value (budget)
            components: List of dicts with 'name' and 'value' keys
            
        Returns:
            Bridge analysis dictionary
        """
        bridge = {
            'starting_value': starting_value,
            'components': components,
            'ending_value': starting_value + sum(c['value'] for c in components),
            'total_variance': sum(c['value'] for c in components)
        }
        
        return bridge
    
    # =============================================================================
    # FORECAST ACCURACY ANALYSIS
    # =============================================================================
    
    def calculate_forecast_accuracy(self,
                                    actual_values: List[float],
                                    forecast_values: List[float]) -> Dict:
        """
        Calculate forecast accuracy metrics
        
        Args:
            actual_values: List of actual values
            forecast_values: List of forecasted values
            
        Returns:
            Dictionary with accuracy metrics
        """
        if len(actual_values) != len(forecast_values):
            raise ValueError("Actual and forecast lists must be same length")
        
        # Mean Absolute Percentage Error (MAPE)
        mape_values = []
        for actual, forecast in zip(actual_values, forecast_values):
            if actual != 0:
                mape_values.append(abs((actual - forecast) / actual))
        
        mape = (sum(mape_values) / len(mape_values) * 100) if mape_values else None
        
        # Mean Absolute Error (MAE)
        mae = sum(abs(a - f) for a, f in zip(actual_values, forecast_values)) / len(actual_values)
        
        # Bias (tendency to over or under forecast)
        bias = sum(f - a for a, f in zip(actual_values, forecast_values)) / len(actual_values)
        
        return {
            'mape': mape,  # Mean Absolute Percentage Error
            'mae': mae,    # Mean Absolute Error
            'bias': bias,  # Average forecast bias
            'accuracy': 100 - mape if mape else None,  # Accuracy percentage
            'periods_analyzed': len(actual_values)
        }
    
    # =============================================================================
    # VARIANCE REPORTING
    # =============================================================================
    
    def generate_variance_report(self, variances: List[Variance]) -> str:
        """
        Generate formatted variance report
        
        Args:
            variances: List of Variance objects
            
        Returns:
            Formatted report string
        """
        report = []
        
        report.append("=" * 80)
        report.append("VARIANCE ANALYSIS REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Material variances only
        material_variances = [v for v in variances if v.materiality in ['high', 'medium']]
        
        if material_variances:
            report.append("MATERIAL VARIANCES:")
            report.append("-" * 80)
            report.append(f"{'Line Item':<30} {'Actual':>12} {'Budget':>12} {'Variance':>12} {'%':>8} {'Status':>10}")
            report.append("-" * 80)
            
            for v in material_variances:
                status = "✓ Fav" if v.is_favorable else "✗ Unfav"
                report.append(
                    f"{v.line_item:<30} "
                    f"{v.actual:>12,.0f} "
                    f"{v.budget:>12,.0f} "
                    f"{v.variance_amount:>12,.0f} "
                    f"{v.variance_percent:>7.1f}% "
                    f"{status:>10}"
                )
            report.append("")
        
        # Summary statistics
        total_favorable = sum(v.variance_amount for v in variances if v.is_favorable)
        total_unfavorable = sum(v.variance_amount for v in variances if not v.is_favorable)
        net_variance = total_favorable + total_unfavorable
        
        report.append("SUMMARY:")
        report.append(f"  Total Favorable Variances:   ${total_favorable:>12,.0f}")
        report.append(f"  Total Unfavorable Variances: ${total_unfavorable:>12,.0f}")
        report.append(f"  Net Variance:                ${net_variance:>12,.0f}")
        report.append("")
        
        return "\n".join(report)
    
    def flag_material_variances(self, variances: List[Variance]) -> List[Variance]:
        """
        Filter to only material variances requiring attention
        
        Args:
            variances: List of all variances
            
        Returns:
            List of material variances only
        """
        return [v for v in variances if v.materiality in ['high', 'medium']]
    
    def generate_variance_explanations(self, variance: Variance) -> str:
        """
        Generate potential explanations for variance
        
        Args:
            variance: Variance object
            
        Returns:
            Suggested explanations text
        """
        explanations = []
        
        if variance.line_item == 'Revenue':
            if variance.variance_amount > 0:
                explanations.append("- Higher than expected sales volume")
                explanations.append("- Favorable pricing or mix")
                explanations.append("- New customer wins or expansion")
            else:
                explanations.append("- Lower than expected sales volume")
                explanations.append("- Price concessions or discounting")
                explanations.append("- Customer churn or delays")
        
        elif 'Cost' in variance.line_item or 'Expense' in variance.line_item:
            if variance.variance_amount > 0 and not variance.is_favorable:
                explanations.append("- Higher input costs or inflation")
                explanations.append("- Operational inefficiencies")
                explanations.append("- Unplanned spending or investments")
            elif variance.variance_amount < 0 and variance.is_favorable:
                explanations.append("- Cost reduction initiatives delivering results")
                explanations.append("- Favorable vendor pricing")
                explanations.append("- Lower than expected activity levels")
        
        return "\n".join(explanations) if explanations else "Requires further investigation"


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    analyzer = VarianceAnalyzer(materiality_threshold=5.0)
    
    print("=== Variance Analyzer - Example Usage ===")
    print()
    
    # Example 1: Simple P&L variance analysis
    actual_pl = {
        'revenue': 10500000,
        'cogs': 6300000,
        'gross_profit': 4200000,
        'operating_expenses': 2800000,
        'operating_income': 1400000,
        'net_income': 1050000
    }
    
    budget_pl = {
        'revenue': 10000000,
        'cogs': 6000000,
        'gross_profit': 4000000,
        'operating_expenses': 2500000,
        'operating_income': 1500000,
        'net_income': 1125000
    }
    
    variances = analyzer.calculate_income_statement_variances(actual_pl, budget_pl)
    
    print(analyzer.generate_variance_report(variances))
    
    # Example 2: Revenue variance decomposition
    print("\n" + "=" * 80)
    print("REVENUE VARIANCE DECOMPOSITION")
    print("=" * 80)
    
    rev_decomp = analyzer.decompose_revenue_variance(
        actual_volume=10500,
        budget_volume=10000,
        actual_price=1000,
        budget_price=1000
    )
    
    print(f"Total Revenue Variance: ${rev_decomp['total_variance']:,.0f}")
    print(f"  Volume Effect: ${rev_decomp['volume_variance']:,.0f} ({rev_decomp['volume_effect_pct']:.1f}%)")
    print(f"  Price Effect:  ${rev_decomp['price_variance']:,.0f} ({rev_decomp['price_effect_pct']:.1f}%)")
    
    # Example 3: Forecast accuracy
    print("\n" + "=" * 80)
    print("FORECAST ACCURACY ANALYSIS")
    print("=" * 80)
    
    actual_monthly = [800000, 850000, 900000, 920000, 950000, 1000000]
    forecast_monthly = [820000, 840000, 880000, 900000, 970000, 980000]
    
    accuracy = analyzer.calculate_forecast_accuracy(actual_monthly, forecast_monthly)
    
    print(f"Forecast Accuracy: {accuracy['accuracy']:.1f}%")
    print(f"MAPE: {accuracy['mape']:.1f}%")
    print(f"MAE: ${accuracy['mae']:,.0f}")
    print(f"Bias: ${accuracy['bias']:,.0f} ({'over-forecasting' if accuracy['bias'] > 0 else 'under-forecasting'})")

