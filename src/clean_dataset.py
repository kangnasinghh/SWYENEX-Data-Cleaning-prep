import pandas as pd

RAW_FILE = "data/adult_income_raw.csv"
OUTPUT_FILE = "data/adult_income_cleaned.csv"

df = pd.read_csv(RAW_FILE)

# Remove extra spaces around text values and turn '?' into a real missing value.
text_cols = df.select_dtypes(include="object").columns
for col in text_cols:
    df[col] = df[col].astype("string").str.strip()

df = df.replace("?", pd.NA)

# Convert columns that should be numeric.
numeric_cols = [
    "age", "fnlwgt", "education_num",
    "capital_gain", "capital_loss", "hours_per_week"
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Keep missing categorical information visible instead of inventing a category.
for col in ["workclass", "occupation", "native_country"]:
    df[col] = df[col].fillna("Unknown")

# Standardize the target label.
df["income"] = df["income"].str.strip()

# Remove exact duplicate rows.
df = df.drop_duplicates().reset_index(drop=True)

# Save the cleaned copy.
df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned file:", OUTPUT_FILE)
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Remaining missing values:", int(df.isna().sum().sum()))
print("Remaining duplicate rows:", int(df.duplicated().sum()))
print("\nData types:")
print(df.dtypes)
