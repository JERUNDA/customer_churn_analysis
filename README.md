# Customer Churn Analysis

## Overview
This repository contains scripts and artifacts for analyzing customer churn using the **Large Customer Churn Analysis Dataset** from Kaggle (1,000 records).  
It includes:
- **Python** scripts for loading, preprocessing, calculating metrics, and creating visualizations
- **SQL** queries for aggregations and churn calculations
- **Power BI** dashboard (.pbix) with interactive views
- **Presentation** (PDF/PPTX) with key findings and recommendations

## Dataset
Source: **Large Customer Churn Analysis Dataset** – [Kaggle link](https://www.kaggle.com/datasets/hajraamir21/large-customer-churn-analysis-dataset/data)  
Contains:
- **Customer demographics**
- **Contract type**
- **Payment details**
- **Churn status**

Key analysis columns: `Geography`, `Contract`, `Tenure`, `MonthlyCharges`, `Churn`  
Data is clean: no missing values, all `CustomerID` values are unique.

---

## Quick Start

### Clone the repository
```bash
git clone https://github.com/JERUNDA/customer_churn_analysis.git
cd customer_churn_analysis
```

Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

(Optional) Install necessary Python libraries:
```bash
pip install pandas matplotlib seaborn
```

Place the CSV file in data/ and run the Python analysis
```bash
python python/customer_churn_analysis.py
```

Repository Structure
```bash
customer_churn_analysis/
│
├── data/               # Raw dataset (CSV)
├── python/             # Python scripts and notebooks
├── sql/                # SQL queries
├── presentation/       # PDF presentation, Power BI dashboard (.pbix)
├── README.md
└── .gitignore
```

Python Workflow
Main script: python/customer_churn_analysis.py
-Loads data/Large_Customer_Churn_Dataset.csv
-Validates data (missing values, duplicates, types)
-Calculates churn metrics:
     -Overall churn rate
     -Churn by geography, contract type, tenure
-Generates visualizations:
     -Barplot: churn by country
     -Lineplot: churn by tenure
     -Boxplot: monthly charges vs churn
     -Heatmap: numeric correlations

Example:
```python
churn_rate = df['Churn'].mean() * 100
geo_churn = df.groupby('Geography')['Churn'].mean().sort_values(ascending=False)
plt.savefig('presentation/figures/cr_by_country.png', dpi=150)
```
SQL scripts: sql/eda_queries.sql
```sql
-- Overall churn rate
SELECT ROUND(100.0 * COUNT(*) FILTER (WHERE Churn = 'Yes') / COUNT(*), 2) AS churn_rate
FROM Large_Customer_Churn_Dataset;

-- Churn by country
SELECT Geography,
       ROUND(100.0 * COUNT(*) FILTER (WHERE Churn = 'Yes') / COUNT(*), 2) AS churn_rate
FROM Large_Customer_Churn_Dataset
GROUP BY Geography
ORDER BY churn_rate DESC;
```

Power BI Dashboard
File: powerbi/customer_churn_analysis_dashboard.pbix
     -Features:
     -Churn rate by geography, contract type, and tenure
     -Overall churn rate card
     -Interactive filters for deeper insights
License & Usage
Dataset is provided by Kaggle for educational and analytical purposes.
Scripts, queries, and presentation materials are free to use with attribution.


