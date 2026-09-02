# Internal Audit & Risk Analytics Dashboard

A transaction risk monitoring dashboard built using Python and Tableau to identify potential financial and operational risks through data analysis and visualization.

## Project Overview

This project simulates an internal audit analytics workflow using 10,000 synthetic financial transactions.

The objective is to demonstrate how transaction-level data can be analyzed to identify potential risk indicators, including high-risk transactions, duplicate invoices, payment method patterns, and vendor transaction concentration.

## Objectives

- Identify and monitor high-risk transactions
- Detect potential duplicate invoices
- Analyze transaction volume by payment method
- Identify vendors with high transaction volumes
- Visualize transaction distribution by country
- Build an interactive dashboard for risk monitoring

## Tools & Technologies

- **Python**
  - Pandas
  - NumPy
  - Faker
  - Random
- **Tableau Public**
- **Microsoft Excel**
- **GitHub**

## Dashboard

The Tableau dashboard provides an interactive view of transaction risk indicators, including:

- Total transaction count
- Total transaction amount
- High-risk transaction count
- Duplicate invoice count
- Risk level distribution
- Payment method distribution
- Transaction distribution by country
- Top vendors by transaction volume

### Tableau Public

[View the Interactive Tableau Dashboard](https://public.tableau.com/views/auditanalyticsdashboard_v1/Dashboard4?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Key Risk Indicators

### High-Risk Transactions

The dashboard identifies transactions classified as high risk to support further review and investigation.

### Duplicate Invoices

Potential duplicate invoices are flagged as a key control risk indicator that may require additional validation.

### Payment Method Analysis

Transaction volume is analyzed across ACH, wire, check, and credit card payment methods to identify unusual concentration or transaction patterns.

### Vendor Concentration

Top vendors are ranked by transaction volume to highlight areas that may warrant additional audit attention.

## Dataset

The project uses a synthetic dataset containing 10,000 financial transactions.

The dataset includes transaction-level attributes such as:

- Transaction ID
- Vendor
- Department
- Transaction Amount
- Transaction Date
- Payment Method
- Country
- Risk Level
- Duplicate Invoice Indicator
- Payment Delay

## Files

| File | Description |
|------|-------------|
| `generate_data.py` | Python script used to generate the synthetic transaction dataset |
| `transactions.csv` | Synthetic transaction dataset containing 10,000 records |
| `Internal Audit & Risk Analytics Dashboard.png` | Tableau dashboard screenshot |

## Data Generation

The transaction dataset was generated using Python and the Faker library.

The generated data was designed to simulate realistic financial transaction patterns while intentionally including risk indicators such as:

- High-risk transactions
- Potential duplicate invoices
- Payment delays
- Vendor transaction concentration
- Different payment methods
- Multiple countries

All data used in this project is synthetic.

## Dashboard Preview

![Internal Audit & Risk Analytics Dashboard](Internal%20Audit%20%26%20Risk%20Analytics%20Dashboard.png)

## Disclaimer

This project was created for portfolio and educational purposes.

All transaction data is synthetic and does not represent real company, customer, vendor, or financial information.
