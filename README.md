# SWYNEX Task 1 – Data Cleaning & Preparation

## Project
**Dataset:** Adult / Census Income dataset  
**Source:** UCI Machine Learning Repository  
**Tool:** Python + Pandas

I selected the UCI Adult dataset because it contains a mix of numeric and categorical fields and real-world data-quality issues such as coded missing values. The UCI page describes 48,842 records and 14 input features, with missing values in fields including `workclass`, `occupation`, and `native-country`.

For this repository I used a small working sample from the public dataset so that the cleaning steps are easy to inspect and reproduce.

## What I checked

### 1. Missing values
Some categorical fields use `?` to represent unavailable information.

Action:
- Trimmed spaces.
- Converted `?` to missing values.
- Replaced missing categorical values with `Unknown`.

### 2. Duplicate records
The raw working file contains one exact repeated row.

Action:
- Used Pandas `drop_duplicates()` to remove the repeated record.

### 3. Incorrect / unclear data types
The raw CSV is first read without forcing a schema, and the numeric fields are explicitly converted before analysis.

Action:
- Converted `age`, `fnlwgt`, `education_num`, `capital_gain`, `capital_loss`, and `hours_per_week` to integer columns.

### 4. Inconsistent values
A few text fields contain extra spaces, for example around the income label and education value.

Action:
- Used `strip()` on text columns.
- Standardized the income labels after trimming whitespace.

## Files

```text
SWYNEX-Data-Cleaning-Preparation/
├── data/
│   ├── adult_income_raw.csv
│   └── adult_income_cleaned.csv
├── docs/
│   └── data_quality_report.md
├── src/
│   └── clean_dataset.py
└── README.md
```

## How to run

Install Pandas:

```bash
pip install pandas
```

From the project folder:

```bash
python src/clean_dataset.py
```

The cleaned file will be created at:

```text
data/adult_income_cleaned.csv
```

## Dataset source and credit

Becker, B. & Kohavi, R. (1996). **Adult**. UCI Machine Learning Repository.  
DOI: 10.24432/C5XW20

Source page:
https://uci-ics-mlr-prod.aws.uci.edu/dataset/2/adult

The UCI dataset is licensed under CC BY 4.0.

## Result

The cleaned working sample has:
- no coded `?` values,
- no exact duplicate rows,
- numeric columns stored as integers,
- standardized text values,
- and a separate raw file so the cleaning process is transparent.
