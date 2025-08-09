-- total number of customers
select count(*) as total_customers 
from Large_Customer_Churn_Dataset;

-- number of churn customers
select count(*) as total_churned_customers
from Large_Customer_Churn_Dataset
where Churn = 'Yes';

-- churn rate (in %)
select round (100.0 * count(*) filter (where Churn = 'Yes') / count(*), 2) as churn_rate
from Large_Customer_Churn_Dataset;

-- churn by country
select Geography,
count(*) filter (where Churn = 'Yes') as churned,
count(*) as total,
round (100.0 * count(*) filter (where Churn = 'Yes') / count(*), 2) as churn_rate
from Large_Customer_Churn_Dataset
group by Geography
order by churn_rate desc;

-- churn by contract type
select Contract,
count(*) filter (where Churn = 'Yes') as churned,
round (100.0 * count(*) filter (where Churn = 'Yes') / count(*), 2) as churn_rate
from Large_Customer_Churn_Dataset
group by Contract
order by churn_rate desc;

-- separation by activity
select IsActiveMember,
count(*) as total_customers
from Large_Customer_Churn_Dataset
group by IsActiveMember;