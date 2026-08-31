# Signal-Based Prospecting & Automation Architecture

Outbound campaigns target explicit timing triggers rather than static database lists.

---

## 3 Primary Buying Signals

| Trigger Signal | Data Source / Method | Automated Action |
| :--- | :--- | :--- |
| **Active Cross-Border Hiring** | LinkedIn Jobs / Indeed API searching "International Procurement," "Logistics Manager," or "Offshore Engineering." | Enriches hiring manager in Clay → Triggers *Remote Payroll / Supplier FX* sequence. |
| **High Trade Corridor Activity** | Customs / Import-Export bills of lading data (Canada ↔ LATAM/Asia/Africa). | Extracts VP Logistics / CFO email → Triggers *Supply Chain Wire Savings* sequence. |
| **Cross-Border Expansion / Funding** | Crunchbase / PitchBook Series A/B announcements in Canadian tech/agri. | Triggers founder/CFO outreach focusing on treasury efficiency and non-dilutive capital preservation. |

---

## Clay + Python Workflow Stack

1. **Signal Ingestion:** Webhook / API feed into Clay table.
2. **Data Enrichment:** Waterfall verification (Clearbit → People Data Labs → Findymail).
3. **Dynamic Messaging Prompting:** AI synthesizes job posting keywords or import volumes into personalized email line 1.
4. **CRM Sync:** Automatic lead creation in HubSpot / Salesforce with tagged source corridor.
