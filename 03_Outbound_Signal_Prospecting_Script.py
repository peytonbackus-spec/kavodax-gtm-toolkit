"""
Kavodax Founding GTM — Signal Enrichment & Outreach Generator
Simulates account scoring and AI-driven outreach personalization for Kavodax prospects.
"""

import json

def evaluate_prospect_signal(company_name: str, open_roles: list, current_stack: list) -> dict:
    has_gtm_hiring = any(role in ["SDR", "AE", "RevOps Leader"] for role in open_roles)
    score = 90 if has_gtm_hiring else 65
    
    return {
        "company": company_name,
        "active_gtm_expansion": has_gtm_hiring,
        "priority_score": score,
        "outreach_focus": "Outbound Acceleration & Signal Automation" if has_gtm_hiring else "Pipeline Efficiency Audit"
    }

def build_personalized_email(evaluation: dict) -> str:
    company = evaluation["company"]
    focus = evaluation["outreach_focus"]
    
    return f"""
    Hi Team,

    Noticed {company} is actively expanding its commercial operations.
    Kavodax helps revenue teams scale faster through {focus}, turning intent signals into qualified pipeline.

    Best,
    Peyton Backus | Kavodax Founding GTM
    """.strip()

if __name__ == "__main__":
    prospect = evaluate_prospect_signal("Apex Solutions", ["SDR", "Account Executive"], ["Salesforce", "Outreach"])
    email = build_personalized_email(prospect)
    
    print("\n" + "="*50)
    print(" KAVODAX GTM SIGNAL ENGINE TEST")
    print("="*50)
    print("PROSPECT EVALUATION:\n", json.dumps(prospect, indent=2))
    print("\nOUTREACH DRAFT:\n", email)
    print("="*50 + "\n")
