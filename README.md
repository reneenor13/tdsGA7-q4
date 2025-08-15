# Supply Chain Analytics: Correlation Matrix Visualization

**OptimalFlow Logistics** - Supply chain consulting firm analyzing supplier performance data.

## Project Overview
This project analyzes relationships between key supply chain metrics for a major automotive manufacturer using 63 procurement transactions from the past quarter.

## Dataset Variables
- **Supplier_Lead_Time:** Days from order placement to delivery
- **Inventory_Levels:** Current stock quantities (units)
- **Order_Frequency:** Number of orders placed per month
- **Delivery_Performance:** On-time delivery rate (%)
- **Cost_Per_Unit:** Unit cost in dollars ($)

## Files Description
- `correlation.csv` - Correlation matrix values generated from Excel Data Analysis ToolPak
- `heatmap.png` - Excel conditional formatting visualization (Red-White-Green color scheme)
- `q-excel-correlation-heatmap.xlsx` - Original Excel workbook with data and analysis
- `generate_files.py` - Python script to generate sample data and correlation matrix

## Contact
Email: 23f3003731@ds.study.iitm.ac.in

## Analysis Method
1. Data imported into Excel
2. Correlation matrix created using: Data → Data Analysis → Correlation
3. Conditional formatting applied with Red-White-Green color scale
4. Results exported for validation

## Key Findings
- Strong negative correlation between Supplier Lead Time and Delivery Performance
- Positive correlation between Cost Per Unit and Lead Time
- Inventory Levels show moderate correlation with Order Frequency
