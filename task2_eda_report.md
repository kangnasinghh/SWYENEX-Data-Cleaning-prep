# Task 2 – Exploratory Data Analysis

## Objective
This task uses the cleaned dataset from Task 1 to perform exploratory analysis, calculate descriptive statistics, identify patterns and anomalies, and communicate useful findings with charts.

## Dataset
- Dataset: UCI Adult / Census Income (working sample used in this project)
- Rows analysed: 20
- Columns analysed: 15
- Tool: Python/Pandas, with an Excel workbook for review

> The repository uses a small working sample of the public dataset. The findings below describe this sample only and should not be generalized to the full UCI Adult dataset.

## Important Statistics

| Measure | Result |
|---|---:|
| Mean age | 37.65 |
| Median age | 37.50 |
| Mean education number | 10.60 |
| Mean weekly hours | 40.95 |
| Median weekly hours | 40.00 |
| Minimum weekly hours | 13 |
| Maximum weekly hours | 80 |
| People <=50K | 13 (65.0%) |
| People >50K | 7 (35.0%) |

## Five Useful Insights

### 1. Most observations are in the <=50K income group
In this sample, 65.0% of records are <=50K, while 35.0% are >50K. This gives the sample an uneven income distribution.

### 2. Higher-income observations work more hours on average
The >50K group averages 48.57 hours per week compared with 36.85 hours for the <=50K group. The difference is about 11.72 hours per week in this sample.

### 3. Weekly working hours contain a notable high value
The maximum is 80 hours per week, while the median is 40. The 80-hour observation is substantially above the typical 40–45 hour range and is worth checking as a potential anomaly or unusually long working week.

### 4. The sample contains more male than female observations
There are 14 male and 6 female records. Within the sample, 42.9% of male records are >50K compared with 16.7% of female records. This is a descriptive pattern in the sample, not a causal conclusion.

### 5. Education groups show different observed income shares
Among the education groups with at least two observations, Masters has 66.7% above 50K, Bachelors has 33.3%, and HS-grad has 25.0%. Small group sizes mean these percentages should be interpreted cautiously.

## Additional Pattern
The mean age is 37.65 years. The >50K group has a mean age of 39.29, compared with 36.77 for the <=50K group. The difference is modest in this small sample.

## Anomalies / Checks
- `hours_per_week = 80` is the clearest high-value observation relative to the sample's median of 40.
- `capital_gain` is highly concentrated at zero, with one observation at 14,084 and another at 5,178, so its distribution is strongly skewed.
- `native_country` is dominated by United-States (15 of 20 records), while several countries have only one observation.

## Charts
The `charts/` folder contains five charts:
1. Income group distribution
2. Average weekly hours by income
3. Income share by sex
4. Income share by education
5. Age versus weekly working hours

## Conclusion
The exploratory analysis shows that the sample is dominated by <=50K observations and that higher-income observations in this sample tend to have higher average weekly hours. Education categories show different observed income shares, while the 80-hour workweek and highly skewed capital-gain values are useful points for further checking. Because the working sample is small, these findings are descriptive and should not be treated as conclusions about the entire population.
