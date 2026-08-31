#!/usr/bin/env python3
"""
Kavodax CAGD vs. Legacy SWIFT Wire / FX Savings Calculator
Accepts dynamic CLI arguments for live CFO executive demos.
"""
import argparse

def calculate_cagd_savings(annual_volume_cad, avg_transfer_size_cad, current_fx_markup_pct, current_wire_fee):
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
    savings_pct = (annual_savings / total_legacy_cost) * 100 if total_legacy_cost > 0 else 0
    
    return {
        "annual_volume": annual_volume_cad,
        "legacy_total": total_legacy_cost,
        "cagd_total": total_cagd_cost,
        "annual_savings": annual_savings,
        "savings_pct": savings_pct
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate CFO savings switching from SWIFT to Kavodax CAGD.")
    parser.add_argument("--volume", type=float, default=5000000.0, help="Annual cross-border volume in CAD (Default: $5,000,000)")
    parser.add_argument("--avg-payout", type=float, default=50000.0, help="Average payout size in CAD (Default: $50,000)")
    parser.add_argument("--markup", type=float, default=0.03, help="Current bank FX markup decimal (Default: 0.03 for 3.0%)")
    parser.add_argument("--wire-fee", type=float, default=35.0, help="Current bank wire fee per transfer (Default: $35.00)")
    
    args = parser.parse_args()
    res = calculate_cagd_savings(args.volume, args.avg_payout, args.markup, args.wire_fee)
    
    print("\n" + "="*50)
    print("      KAVODAX CAGD COMMERCIAL ROI MODEL")
    print("="*50)
    print(f"Annual CAD Volume:          ${res['annual_volume']:,.2f}")
    print(f"Legacy Bank/SWIFT Cost:     ${res['legacy_total']:,.2f}")
    print(f"Kavodax CAGD Total Cost:    ${res['cagd_total']:,.2f}")
    print("-" * 50)
    print(f"NET ANNUAL SAVINGS:         ${res['annual_savings']:,.2f} ({res['savings_pct']:.1f}% Reduction)")
    print("="*50 + "\n")
