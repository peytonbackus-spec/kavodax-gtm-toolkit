"""
Kavodax GTM — Business Value Assessment (BVA) & ROI Calculator
Models outbound pipeline velocity, rep capacity gains, and CAC payback period.
"""

def calculate_kavodax_bva(reps: int, avg_deal_size: float, monthly_tool_cost: float) -> dict:
    hours_saved_per_rep_weekly = 8.5
    hourly_rate = 60.0  # Fully loaded rep cost
    
    monthly_hours_saved = reps * hours_saved_per_rep_weekly * 4
    monthly_labor_cost_saved = monthly_hours_saved * hourly_rate
    annual_labor_savings = monthly_labor_cost_saved * 12
    
    annual_tool_cost = monthly_tool_cost * 12
    net_annual_roi = ((annual_labor_savings - annual_tool_cost) / annual_tool_cost) * 100
    payback_months = (annual_tool_cost / (annual_labor_savings / 12))
    
    return {
        "active_sales_reps": reps,
        "monthly_labor_hours_reclaimed": round(monthly_hours_saved, 1),
        "annual_efficiency_savings_usd": round(annual_labor_savings, 2),
        "annual_platform_cost_usd": round(annual_tool_cost, 2),
        "net_roi_percent": f"{round(net_roi_percent, 1)}%",
        "payback_period_months": round(payback_months, 1)
    }

if __name__ == "__main__":
    bva_results = calculate_kavodax_bva(reps=5, avg_deal_size=30000, monthly_tool_cost=1500)
    print("\n" + "="*50)
    print(" KAVODAX BVA & ROI FINANCIAL MODEL")
    print("="*50)
    for key, value in bva_results.items():
        print(f"{key}: {value}")
    print("="*50 + "\n")
