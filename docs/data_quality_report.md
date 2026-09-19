# Data Quality Report

## Dataset
Adult / Census Income — UCI Machine Learning Repository.

The original UCI dataset contains 48,842 records and 14 features. This repository uses a small working sample for the cleaning demonstration.

## Before cleaning

- Rows: 21
- Columns: 15
- Exact duplicate rows: 1
- Coded missing markers (`?`): 0

### Issues found

| Issue | Where | Action |
|---|---|---|
| Missing/coded values | workclass, occupation, native_country | Convert `?` to missing and fill with `Unknown` |
| Duplicate row | exact duplicate record | Remove duplicate |
| Type handling | numeric columns | Convert explicitly to integer |
| Extra whitespace | text fields | Strip leading/trailing spaces |
| Inconsistent income formatting | income | Trim whitespace and standardize labels |

## After cleaning

- Rows: 20
- Columns: 15
- Remaining missing values: 0
- Remaining duplicate rows: 0

## Final numeric types

- `age` → `int64`
- `fnlwgt` → `int64`
- `education_num` → `int64`
- `capital_gain` → `int64`
- `capital_loss` → `int64`
- `hours_per_week` → `int64`

## Note
The raw file is kept unchanged inside the project so the reviewer can compare the before/after data. The cleaned CSV is the file intended for analysis.
