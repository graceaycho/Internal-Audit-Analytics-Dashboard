from pathlib import Path
from datetime import timedelta
import random

import pandas as pd
from faker import Faker

# Project setting
NUM_TRANSACTIONS = 10000
DUPLICATE_SOURCE_RATE = 0.05

random.seed(42)
Faker.seed(42)

fake = Faker()

# Master Data
vendors = [
    "Dell Technologies",
    "Microsoft",
    "Apple",
    "Amazon",
    "IBM",
    "Oracle",
    "Cisco",
    "Google",
    "Adobe",
    "SAP",
    "Intel",
    "NVIDIA",
    "Lenovo",
    "HP",
    "Accenture",
    "KPMG",
    "Deloitte",
    "PwC",
    "EY",
    "CDW"
]

departments = [
    "Finance",
    "Accounting",
    "Marketing",
    "Sales",
    "IT",
    "HR",
    "Legal",
    "Procurement",
    "Supply Chain",
    "Customer Service",
    "Operations",
    "Engineering",
    "R&D",
    "Compliance"
]

payment_methods = [
    "ACH",
    "Wire",
    "Check",
    "Credit Card"
]

countries = [
    "United States",
    "Canada",
    "Mexico",
    "Germany",
    "United Kingdom",
    "Japan",
    "South Korea"
]

country_currency = {
    "United States": "USD",
    "Canada": "CAD",
    "Mexico": "MXN",
    "Germany": "EUR",
    "United Kingdom": "GBP",
    "Japan": "JPY",
    "South Korea": "KRW"
}

# Generate transaction data

transactions = []

for i in range(NUM_TRANSACTIONS):
    transaction_id = f"TRX{100001 + i}"
    invoice_number = f"INV{200001 + i}"
    vendor = random.choice(vendors)
    department = random.choice(departments)
    
    chance = random.random()

    if chance < 0.70:
        amount = round(random.uniform(100, 10000), 2)

    elif chance < 0.90:
        amount = round(random.uniform(10000, 50000), 2)

    else:
        amount = round(random.uniform(50000, 200000), 2)
        
    invoice_date = fake.date_between(
        start_date = "-1y",
        end_date = "today"
    )
    due_date = invoice_date + timedelta(days=30)
    
    # Simulate realistic payment behavior
    chance = random.random()

    if chance < 0.70:
        # Paid on time or early
        payment_delay_days = random.randint(-10, 0)

    elif chance < 0.90:
        # Slightly late
        payment_delay_days = random.randint(1, 15)

    else:
        # Significantly late
        payment_delay_days = random.randint(16, 45)

    payment_date = due_date + timedelta(days=payment_delay_days)
    
    payment_method = random.choices(
        payment_methods,
        weights=[65, 20, 10, 5]
    )[0]
    
    po_status = random.choices(
        ["Yes", "No"],
        weights=[95, 5]
    )[0]
    
    country = random.choices(
        countries,
        weights=[70, 10, 8, 5, 4, 2, 1]
    )[0]

    currency = country_currency[country]
    
    transactions.append({
        "Transaction_ID": transaction_id,
        "Invoice_Number": invoice_number,
        "Vendor": vendor,
        "Department": department,
        "Amount": amount,
        "Invoice_Date": invoice_date,
        "Due_Date": due_date,
        "Payment_Date": payment_date,
        "Payment_Method": payment_method,
        "PO_Status": po_status,
        "Country": country,
        "Currency": currency,
        "High_Value": amount >= 50000
    })

# DataFrame    
df = pd.DataFrame(transactions)

# Create duplicate invoices

num_duplicate_sources = int(
    NUM_TRANSACTIONS * DUPLICATE_SOURCE_RATE
)

duplicate_indices = random.sample(
    df.index.tolist(),
    num_duplicate_sources
)

for idx in duplicate_indices:
    possible_sources = df.index[df.index != idx].tolist()
    source_idx = random.choice(possible_sources)

    df.loc[idx, "Invoice_Number"] = df.loc[
        source_idx,
        "Invoice_Number"
    ]

# Audit Logic
df["Missing_PO"] = df["PO_Status"] == "No"
df["Late_Payment"] = df["Payment_Date"] > df["Due_Date"]
df["Duplicate_Invoice"] = df["Invoice_Number"].duplicated(keep=False)
df["Risk_Score"] = 0

df.loc[df["High_Value"], "Risk_Score"] += 1
df.loc[df["Missing_PO"], "Risk_Score"] += 2
df.loc[df["Payment_Method"] == "Wire", "Risk_Score"] += 1
df.loc[df["Late_Payment"], "Risk_Score"] += 1
df.loc[df["Duplicate_Invoice"], "Risk_Score"] += 3

# Risk Level
def assign_risk_level(score):
    if score == 0:
        return "Low"
    elif score <= 2:
        return "Medium"
    else:
        return "High"

df["Risk_Level"] = df["Risk_Score"].apply(assign_risk_level)

# Save dataset
output_path = Path("data") / "transactions.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

""""
# Validation
print(f"Successfully created {len(df):,} transactions")
print(f"csv saved to: {output_path}")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nUnique Transaction IDs")
print(df["Transaction_ID"].nunique())

print("\nDuplicate Transaction IDs")
print(df["Transaction_ID"].duplicated().sum())

print("\nRisk Level Distribution")
print(df["Risk_Level"].value_counts())

print("\nDuplicate Invoice Distribution")
print(df["Duplicate_Invoice"].value_counts())

print("\nUnique Invoice Numbers")
print(df["Invoice_Number"].nunique())

print("\nDuplicate Invoice Records")
print(
    df.loc[
        df["Duplicate_Invoice"],
        ["Transaction_ID", "Invoice_Number"]
    ].sort_values("Invoice_Number")
)
"""