#!/usr/bin/env python3
"""
Kavodax CAGD vs. Legacy SWIFT Wire / FX Savings Calculator
Calculates basis-point savings, transaction fee reductions, and annualized ROI.
"""

def calculate_cagd_savings(annual_volume_cad, avg_transfer_size_cad, current_fx_markup_pct=0.03, current_wire_fee=35.0):
    cagd_spread_pct = 0.005  # 50 bps average CAGD spread
    cagd_payout_fee = 1.50   # Flat per-payout rail fee
    
    num_transactions = annual_volume_cad / avg_transfer_size_cad
    
    # Legacy Costs
    legacy_fx_cost = annual_volume_cad * current_fx_markup_pct
    legacy_wire_cost = num_transactions * current_wire_fee
    total_legacy_cost = legacy_fx_cost + legacy_wire_cost
    
    # CAGD Costs
    cagd_fx_cost = annual_volume_cad * cagd_spread_pct
    cagd_rail_cost = num_transactions * cagd_payout_fee
    total_cagd_cost = cagd_fx_cost + cagd_rail_cost
    
    # Savings
    annual_savings = total_legacy_cost - total_cagd_cost
    savings_pct = (annual_savings / total_legacy_cost) * 100
    
    return {
        "annual_volume": annual_volume_cad,
        "legacy_total": total_legacy_cost,
        "cagd_total": total_cagd_cost,
        "annual_savings": annual_savings,
        "savings_pct": savings_pct
    }

if __name__ == "__main__":
    # Example: Importer processing $5M/year in $50k average payouts
    res = calculate_cagd_savings(5_000_000, 50_000)
    print(f"--- CAGD Commercial ROI Model ---")
    print(f"Annual Volume: ${res['annual_volume']:,.2f} CAD")
    print(f"Legacy Bank/SWIFT Cost: ${res['legacy_total']:,.2f}")
    print(f"Kavodax CAGD Cost: ${res['cagd_total']:,.2f}")
    print(f"Net Annualized Savings: ${res['annual_savings']:,.2f} ({res['savings_pct']:.1f}% Reduction)")
