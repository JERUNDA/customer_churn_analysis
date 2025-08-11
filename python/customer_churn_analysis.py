'''
Customer Churn Dataset - Basic EDA and Visualization
- Data loading and validation
- Preprocessing
- Calculating basic churn metrics
- Visualizing distributions and correlations
'''

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload CSV and checking the first lines
df = pd.read_csv(r'C:\temp\Large_Customer_Churn_Dataset.csv', sep =',', encoding = 'utf-8')
print(df.head())
   CustomerID  Gender  Age Geography  Tenure  ... MonthlyCharges  TotalCharges  PaymentMethod IsActiveMember  Churn
0     1000001    Male   34    France      14  ...          21.58       7933.34  Bank transfer              1     No
1     1000002  Female   26     Spain      14  ...          27.71       5869.34    Credit card              0    Yes
2     1000003    Male   50   Germany      57  ...         111.12       6321.20  Bank transfer              1     No
3     1000004    Male   37     Spain      34  ...          55.49       7956.44  Bank transfer              0    Yes
4     1000005    Male   30     Spain      53  ...          62.48       4922.75   Direct debit              1     No

[5 rows x 11 columns]

# Checking the structure and data types
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   CustomerID      1000 non-null   int64
 1   Gender          1000 non-null   object
 2   Age             1000 non-null   int64
 3   Geography       1000 non-null   object
 4   Tenure          1000 non-null   int64
 5   Contract        1000 non-null   object
 6   MonthlyCharges  1000 non-null   float64
 7   TotalCharges    1000 non-null   float64
 8   PaymentMethod   1000 non-null   object
 9   IsActiveMember  1000 non-null   int64
 10  Churn           1000 non-null   object
dtypes: float64(2), int64(4), object(5)
memory usage: 86.1+ KB

# Checking for passes
df.isnull().sum()
CustomerID        0
Gender            0
Age               0
Geography         0
Tenure            0
Contract          0
MonthlyCharges    0
TotalCharges      0
PaymentMethod     0
IsActiveMember    0
Churn             0
dtype: int64

# Convert 'Churn' column values from 'Yes'/'No' to 1/0 for numerical analysis
df['Churn'] = df['Churn'].map({'Yes' : 1, 'No' : 0})

# Checking the uniqueness of CustomerID
print('There are duplicates in CustomerID' if df['CustomerID'].duplicated().any() else 'CustomerIDs are unique')
CustomerIDs are unique

# Removing or processing lines with passes
df.dropna(inplace=True)
df.dtypes
CustomerID          int64
Gender             object
Age                 int64
Geography          object
Tenure              int64
Contract           object
MonthlyCharges    float64
TotalCharges      float64
PaymentMethod      object
IsActiveMember      int64
Churn               int64
dtype: object

# Overall churn rate
churn_rate = df['Churn'].mean() * 100
print(f'Churn rate : {churn_rate:.2f}%')
Churn rate : 50.20%

# Churn by country
geo_churn = df.groupby('Geography')['Churn'].mean().sort_values(ascending = False)
print(geo_churn)
Geography
France     0.533333
UK         0.519048
Spain      0.497143
Germany    0.492147
Italy      0.467290
Name: Churn, dtype: float64

# Churn by contracts
contract_churn = df.groupby('Contract')['Churn'].mean().sort_values(ascending = False)
print(contract_churn)
Contract
One-year          0.538462
Two-year          0.488095
Month-to-month    0.482955
Name: Churn, dtype: float64

# Churn by tenure
tenure_churn = df.groupby('Tenure')['Churn'].mean()
print(tenure_churn)
Tenure
1     0.692308
2     0.615385
3     0.388889
4     0.520000
5     0.214286
6     0.380952
7     0.400000
8     0.733333
9     0.411765
10    0.250000
11    0.611111
12    0.555556
13    0.400000
14    0.470588
15    0.571429
16    0.545455
17    0.692308
18    0.625000
19    0.450000
20    0.434783
21    0.500000
22    0.444444
23    0.571429
24    0.714286
25    0.615385
26    0.500000
27    0.533333
28    0.666667
29    0.454545
30    0.300000
31    0.666667
32    1.000000
33    0.500000
34    0.368421
35    0.318182
36    0.384615
37    0.578947
38    0.368421
39    0.823529
40    0.562500
41    0.500000
42    0.428571
43    0.692308
44    0.500000
45    0.480000
46    0.285714
47    0.526316
48    0.352941
49    0.576923
50    0.500000
51    0.578947
52    0.266667
53    0.647059
54    0.769231
55    0.350000
56    0.350000
57    0.545455
58    0.312500
59    0.555556
Name: Churn, dtype: float64

# Barplot: Churn rate by countries
plt.figure(figsize=(10, 6))
sns.barplot( x = geo_churn.index, y = geo_churn.values)
plt.title('Churn Rate by Country', fontsize = 16)
plt.xlabel('Country', fontsize = 14)
plt.ylabel('Churn Rate', fontsize = 14)
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()

# Lineplot: Churn rate by tenure
plt.figure(figsize=(10, 6))
sns.lineplot(x=tenure_churn.index, y=tenure_churn.values, marker='o')
plt.title('Churn Rate by Tenure (months)', fontsize = 16)
plt.xlabel('Tenure (Months)', fontsize = 14)
plt.ylabel('Churn Rate', fontsize = 14)
plt.xticks(rotation = 30)
plt.tight_layout()
plt.show()

# Boxplot: Monthly Charges vs Churn
plt.figure(figsize=(8, 6))
sns.boxplot(data = df, x = 'Churn', y = 'MonthlyCharges')
plt.title('Monthly Charges vs Churn', fontsize = 16)
plt.xlabel('Churn (0=No, 1=Yes)', fontsize = 14)
plt.ylabel('Monthly Charges', fontsize = 14)
plt.tight_layout()
plt.show()

# Heatmap: Correlations
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only = True), annot = True, cmap = 'coolwarm', fmt = '.2f', linewidths = 0.5)
plt.title('Correlation Heatmap', fontsize = 16)
plt.tight_layout()
plt.show()
