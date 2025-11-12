"""
KPI Calculator Script
Industry-agnostic KPI calculations and performance metrics

Capabilities:
- Calculate financial KPIs
- Calculate operational KPIs
- Calculate customer/revenue KPIs
- Industry-specific metrics (SaaS, Retail, Manufacturing, etc.)
- Performance benchmarking
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class KPI:
    """Data class for KPI metrics"""
    name: str
    value: float
    unit: str
    target: Optional[float] = None
    benchmark: Optional[float] = None
    status: Optional[str] = None  # 'good', 'warning', 'poor'
    interpretation: Optional[str] = None


class KPICalculator:
    """
    Calculate comprehensive set of KPIs across different categories
    """
    
    def __init__(self):
        """Initialize KPI calculator"""
        pass
    
    # =============================================================================
    # FINANCIAL KPIs
    # =============================================================================
    
    def calculate_revenue_growth(self, current_revenue: float, prior_revenue: float) -> KPI:
        """Revenue Growth Rate"""
        growth_rate = ((current_revenue - prior_revenue) / prior_revenue * 100) if prior_revenue != 0 else None
        
        status = 'good' if growth_rate and growth_rate > 10 else 'warning' if growth_rate and growth_rate > 0 else 'poor'
        
        return KPI(
            name="Revenue Growth Rate",
            value=growth_rate,
            unit="%",
            interpretation=f"{'Strong' if growth_rate and growth_rate > 15 else 'Moderate' if growth_rate and growth_rate > 5 else 'Slow'} revenue growth"
        )
    
    def calculate_ebitda_margin(self, ebitda: float, revenue: float) -> KPI:
        """EBITDA Margin"""
        margin = (ebitda / revenue * 100) if revenue != 0 else None
        
        status = 'good' if margin and margin > 20 else 'warning' if margin and margin > 10 else 'poor'
        
        return KPI(
            name="EBITDA Margin",
            value=margin,
            unit="%",
            status=status,
            interpretation=f"{'Strong' if margin and margin > 20 else 'Adequate' if margin and margin > 10 else 'Weak'} operating profitability"
        )
    
    def calculate_operating_leverage(self, operating_income_growth: float, 
                                    revenue_growth: float) -> KPI:
        """Operating Leverage = Operating Income Growth / Revenue Growth"""
        leverage = (operating_income_growth / revenue_growth) if revenue_growth != 0 else None
        
        status = 'good' if leverage and leverage > 1.0 else 'warning'
        
        return KPI(
            name="Operating Leverage",
            value=leverage,
            unit="x",
            status=status,
            interpretation="Positive operating leverage" if leverage and leverage > 1.0 else "Negative operating leverage"
        )
    
    # =============================================================================
    # OPERATIONAL KPIs
    # =============================================================================
    
    def calculate_revenue_per_employee(self, revenue: float, employee_count: int) -> KPI:
        """Revenue per Employee"""
        rev_per_emp = revenue / employee_count if employee_count > 0 else None
        
        return KPI(
            name="Revenue per Employee",
            value=rev_per_emp,
            unit="$",
            interpretation=f"Employee productivity: ${rev_per_emp:,.0f} per employee" if rev_per_emp else "N/A"
        )
    
    def calculate_operating_expense_ratio(self, operating_expenses: float, 
                                         revenue: float) -> KPI:
        """Operating Expense Ratio"""
        opex_ratio = (operating_expenses / revenue * 100) if revenue != 0 else None
        
        status = 'good' if opex_ratio and opex_ratio < 30 else 'warning' if opex_ratio and opex_ratio < 40 else 'poor'
        
        return KPI(
            name="Operating Expense Ratio",
            value=opex_ratio,
            unit="%",
            status=status,
            interpretation=f"{'Efficient' if opex_ratio and opex_ratio < 30 else 'Adequate' if opex_ratio and opex_ratio < 40 else 'High'} operating cost structure"
        )
    
    # =============================================================================
    # CUSTOMER / REVENUE KPIs
    # =============================================================================
    
    def calculate_customer_lifetime_value(self, avg_revenue_per_customer: float,
                                         gross_margin_pct: float,
                                         retention_rate: float) -> KPI:
        """
        Customer Lifetime Value (LTV)
        LTV = (Avg Revenue per Customer × Gross Margin %) / Churn Rate
        Where Churn Rate = 1 - Retention Rate
        """
        churn_rate = 1 - (retention_rate / 100)
        ltv = (avg_revenue_per_customer * (gross_margin_pct / 100)) / churn_rate if churn_rate > 0 else None
        
        return KPI(
            name="Customer Lifetime Value (LTV)",
            value=ltv,
            unit="$",
            interpretation=f"Average customer worth ${ltv:,.0f} over lifetime" if ltv else "N/A"
        )
    
    def calculate_customer_acquisition_cost(self, sales_marketing_spend: float,
                                          new_customers: int) -> KPI:
        """Customer Acquisition Cost (CAC)"""
        cac = sales_marketing_spend / new_customers if new_customers > 0 else None
        
        return KPI(
            name="Customer Acquisition Cost (CAC)",
            value=cac,
            unit="$",
            interpretation=f"Cost to acquire new customer: ${cac:,.0f}" if cac else "N/A"
        )
    
    def calculate_ltv_cac_ratio(self, ltv: float, cac: float) -> KPI:
        """
        LTV/CAC Ratio
        Healthy: > 3.0x
        """
        ratio = ltv / cac if cac > 0 else None
        
        status = 'good' if ratio and ratio > 3.0 else 'warning' if ratio and ratio > 1.0 else 'poor'
        
        return KPI(
            name="LTV/CAC Ratio",
            value=ratio,
            unit="x",
            target=3.0,
            status=status,
            interpretation=f"{'Healthy' if ratio and ratio > 3.0 else 'Marginal' if ratio and ratio > 1.0 else 'Unprofitable'} unit economics"
        )
    
    def calculate_customer_concentration(self, top_10_revenue: float, 
                                        total_revenue: float) -> KPI:
        """Customer Concentration Risk"""
        concentration = (top_10_revenue / total_revenue * 100) if total_revenue > 0 else None
        
        status = 'good' if concentration and concentration < 30 else 'warning' if concentration and concentration < 50 else 'poor'
        
        return KPI(
            name="Top 10 Customer Concentration",
            value=concentration,
            unit="%",
            status=status,
            interpretation=f"{'Low' if concentration and concentration < 30 else 'Moderate' if concentration and concentration < 50 else 'High'} customer concentration risk"
        )
    
    # =============================================================================
    # SaaS-SPECIFIC KPIs
    # =============================================================================
    
    def calculate_arr(self, mrr: float) -> KPI:
        """Annual Recurring Revenue from MRR"""
        arr = mrr * 12
        
        return KPI(
            name="Annual Recurring Revenue (ARR)",
            value=arr,
            unit="$",
            interpretation=f"ARR: ${arr:,.0f}"
        )
    
    def calculate_net_revenue_retention(self, starting_arr: float, 
                                       expansion_arr: float,
                                       contraction_arr: float,
                                       churn_arr: float) -> KPI:
        """
        Net Revenue Retention (NRR)
        NRR = (Starting ARR + Expansions - Contractions - Churn) / Starting ARR × 100
        """
        ending_arr = starting_arr + expansion_arr - contraction_arr - churn_arr
        nrr = (ending_arr / starting_arr * 100) if starting_arr > 0 else None
        
        status = 'good' if nrr and nrr > 110 else 'warning' if nrr and nrr > 100 else 'poor'
        
        return KPI(
            name="Net Revenue Retention (NRR)",
            value=nrr,
            unit="%",
            target=110,
            status=status,
            interpretation=f"{'Excellent' if nrr and nrr > 120 else 'Good' if nrr and nrr > 100 else 'Concerning'} revenue retention and expansion"
        )
    
    def calculate_gross_revenue_retention(self, starting_arr: float,
                                         contraction_arr: float,
                                         churn_arr: float) -> KPI:
        """
        Gross Revenue Retention (GRR)
        GRR = (Starting ARR - Contractions - Churn) / Starting ARR × 100
        """
        retained_arr = starting_arr - contraction_arr - churn_arr
        grr = (retained_arr / starting_arr * 100) if starting_arr > 0 else None
        
        status = 'good' if grr and grr > 90 else 'warning' if grr and grr > 85 else 'poor'
        
        return KPI(
            name="Gross Revenue Retention (GRR)",
            value=grr,
            unit="%",
            target=90,
            status=status,
            interpretation=f"{'Strong' if grr and grr > 90 else 'Adequate' if grr and grr > 85 else 'Weak'} logo retention"
        )
    
    def calculate_cac_payback_period(self, cac: float, 
                                    avg_revenue_per_customer: float,
                                    gross_margin_pct: float) -> KPI:
        """
        CAC Payback Period (months)
        Payback = CAC / (Monthly Revenue per Customer × Gross Margin %)
        Target: < 12-18 months
        """
        monthly_revenue = avg_revenue_per_customer / 12
        monthly_gross_profit = monthly_revenue * (gross_margin_pct / 100)
        payback = cac / monthly_gross_profit if monthly_gross_profit > 0 else None
        
        status = 'good' if payback and payback < 12 else 'warning' if payback and payback < 18 else 'poor'
        
        return KPI(
            name="CAC Payback Period",
            value=payback,
            unit="months",
            target=12,
            status=status,
            interpretation=f"{'Fast' if payback and payback < 12 else 'Acceptable' if payback and payback < 18 else 'Slow'} payback on customer acquisition"
        )
    
    def calculate_rule_of_40(self, revenue_growth_rate: float, 
                            profit_margin: float) -> KPI:
        """
        Rule of 40 for SaaS
        Rule of 40 = Revenue Growth Rate % + Profit Margin %
        Healthy: > 40%
        """
        rule_of_40 = revenue_growth_rate + profit_margin
        
        status = 'good' if rule_of_40 > 40 else 'warning' if rule_of_40 > 30 else 'poor'
        
        return KPI(
            name="Rule of 40",
            value=rule_of_40,
            unit="%",
            target=40,
            status=status,
            interpretation=f"{'Excellent' if rule_of_40 > 40 else 'Adequate' if rule_of_40 > 30 else 'Underperforming'} SaaS efficiency"
        )
    
    def calculate_magic_number(self, net_new_arr: float, 
                               prior_period_sales_marketing: float) -> KPI:
        """
        Magic Number
        Magic Number = Net New ARR / Prior Period Sales & Marketing Spend
        Healthy: > 0.75
        """
        magic_number = net_new_arr / prior_period_sales_marketing if prior_period_sales_marketing > 0 else None
        
        status = 'good' if magic_number and magic_number > 0.75 else 'warning' if magic_number and magic_number > 0.5 else 'poor'
        
        return KPI(
            name="Magic Number",
            value=magic_number,
            unit="",
            target=0.75,
            status=status,
            interpretation=f"{'Efficient' if magic_number and magic_number > 0.75 else 'Moderate' if magic_number and magic_number > 0.5 else 'Inefficient'} sales and marketing efficiency"
        )
    
    # =============================================================================
    # RETAIL KPIs
    # =============================================================================
    
    def calculate_same_store_sales(self, current_sss: float, prior_sss: float) -> KPI:
        """Same-Store Sales Growth"""
        sss_growth = ((current_sss - prior_sss) / prior_sss * 100) if prior_sss > 0 else None
        
        status = 'good' if sss_growth and sss_growth > 3 else 'warning' if sss_growth and sss_growth > 0 else 'poor'
        
        return KPI(
            name="Same-Store Sales Growth",
            value=sss_growth,
            unit="%",
            status=status,
            interpretation=f"{'Strong' if sss_growth and sss_growth > 5 else 'Modest' if sss_growth and sss_growth > 0 else 'Declining'} comparable store performance"
        )
    
    def calculate_inventory_turnover_days(self, cogs: float, avg_inventory: float) -> KPI:
        """Inventory Turnover in Days"""
        days = (avg_inventory / cogs * 365) if cogs > 0 else None
        
        status = 'good' if days and days < 60 else 'warning' if days and days < 90 else 'poor'
        
        return KPI(
            name="Days Inventory Outstanding",
            value=days,
            unit="days",
            status=status,
            interpretation=f"{'Fast' if days and days < 60 else 'Moderate' if days and days < 90 else 'Slow'} inventory turns"
        )
    
    # =============================================================================
    # MANUFACTURING KPIs
    # =============================================================================
    
    def calculate_capacity_utilization(self, actual_output: float, 
                                      max_capacity: float) -> KPI:
        """Capacity Utilization Rate"""
        utilization = (actual_output / max_capacity * 100) if max_capacity > 0 else None
        
        status = 'good' if utilization and 75 < utilization < 90 else 'warning'
        
        return KPI(
            name="Capacity Utilization",
            value=utilization,
            unit="%",
            target=80,
            status=status,
            interpretation=f"{'Optimal' if utilization and 75 < utilization < 90 else 'Underutilized' if utilization and utilization < 75 else 'Overcapacity'} production efficiency"
        )
    
    def calculate_oee(self, availability: float, performance: float, quality: float) -> KPI:
        """
        Overall Equipment Effectiveness (OEE)
        OEE = Availability % × Performance % × Quality %
        World-class: > 85%
        """
        oee = (availability / 100) * (performance / 100) * (quality / 100) * 100
        
        status = 'good' if oee > 85 else 'warning' if oee > 70 else 'poor'
        
        return KPI(
            name="Overall Equipment Effectiveness (OEE)",
            value=oee,
            unit="%",
            target=85,
            status=status,
            interpretation=f"{'World-class' if oee > 85 else 'Good' if oee > 70 else 'Needs improvement'} manufacturing efficiency"
        )
    
    # =============================================================================
    # COMPREHENSIVE KPI DASHBOARD
    # =============================================================================
    
    def generate_kpi_dashboard(self, financial_data: Dict, 
                              industry: str = 'general') -> Dict[str, List[KPI]]:
        """
        Generate comprehensive KPI dashboard
        
        Args:
            financial_data: Dictionary with all relevant financial and operational data
            industry: Industry type (general, saas, retail, manufacturing, etc.)
            
        Returns:
            Dictionary organized by KPI category
        """
        dashboard = {
            'financial': [],
            'operational': [],
            'customer': []
        }
        
        # Financial KPIs (always calculated)
        if 'current_revenue' in financial_data and 'prior_revenue' in financial_data:
            dashboard['financial'].append(
                self.calculate_revenue_growth(
                    financial_data['current_revenue'],
                    financial_data['prior_revenue']
                )
            )
        
        if 'ebitda' in financial_data and 'revenue' in financial_data:
            dashboard['financial'].append(
                self.calculate_ebitda_margin(
                    financial_data['ebitda'],
                    financial_data['revenue']
                )
            )
        
        # Industry-specific KPIs
        if industry == 'saas':
            dashboard['saas'] = self._calculate_saas_kpis(financial_data)
        elif industry == 'retail':
            dashboard['retail'] = self._calculate_retail_kpis(financial_data)
        elif industry == 'manufacturing':
            dashboard['manufacturing'] = self._calculate_manufacturing_kpis(financial_data)
        
        return dashboard
    
    def _calculate_saas_kpis(self, data: Dict) -> List[KPI]:
        """Calculate SaaS-specific KPIs"""
        kpis = []
        
        if 'revenue_growth' in data and 'profit_margin' in data:
            kpis.append(self.calculate_rule_of_40(data['revenue_growth'], data['profit_margin']))
        
        # Add more SaaS KPIs...
        
        return kpis
    
    def _calculate_retail_kpis(self, data: Dict) -> List[KPI]:
        """Calculate retail-specific KPIs"""
        kpis = []
        
        if 'current_sss' in data and 'prior_sss' in data:
            kpis.append(self.calculate_same_store_sales(data['current_sss'], data['prior_sss']))
        
        # Add more retail KPIs...
        
        return kpis
    
    def _calculate_manufacturing_kpis(self, data: Dict) -> List[KPI]:
        """Calculate manufacturing-specific KPIs"""
        kpis = []
        
        if all(k in data for k in ['actual_output', 'max_capacity']):
            kpis.append(self.calculate_capacity_utilization(data['actual_output'], data['max_capacity']))
        
        # Add more manufacturing KPIs...
        
        return kpis


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    calculator = KPICalculator()
    
    print("=== KPI Calculator - Example Usage ===")
    print()
    
    # Financial KPIs
    print("FINANCIAL KPIs:")
    rev_growth = calculator.calculate_revenue_growth(10000000, 8000000)
    print(f"{rev_growth.name}: {rev_growth.value:.1f}{rev_growth.unit} - {rev_growth.interpretation}")
    
    ebitda_margin = calculator.calculate_ebitda_margin(2500000, 10000000)
    print(f"{ebitda_margin.name}: {ebitda_margin.value:.1f}{ebitda_margin.unit} - {ebitda_margin.interpretation}")
    
    # SaaS KPIs
    print("\nSaaS KPIs:")
    rule_of_40 = calculator.calculate_rule_of_40(25.0, 20.0)
    print(f"{rule_of_40.name}: {rule_of_40.value:.1f}{rule_of_40.unit} - {rule_of_40.interpretation}")
    
    ltv = calculator.calculate_customer_lifetime_value(5000, 70, 90)
    cac = calculator.calculate_customer_acquisition_cost(100000, 50)
    ltv_cac = calculator.calculate_ltv_cac_ratio(ltv.value, cac.value)
    print(f"{ltv_cac.name}: {ltv_cac.value:.1f}{ltv_cac.unit} - {ltv_cac.interpretation}")

