import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/adult_income_cleaned.csv")

print("Dataset shape:", df.shape)
print("\nDescriptive statistics:")
print(df[["age", "education_num", "capital_gain", "capital_loss", "hours_per_week"]].describe())

print("\nIncome distribution:")
print(df["income"].value_counts())
print((df["income"].value_counts(normalize=True) * 100).round(1))

print("\nAverage hours by income:")
print(df.groupby("income")["hours_per_week"].agg(["mean", "median", "min", "max"]).round(2))

print("\nIncome share by sex:")
print(pd.crosstab(df["sex"], df["income"], normalize="index").mul(100).round(1))

print("\nIncome by education:")
print(df.groupby("education")["income"].agg(
    total="size",
    high_income=lambda s: (s == ">50K").sum()
))

# Example chart
df["income"].value_counts().plot(kind="bar", title="Income Group Distribution")
plt.xlabel("Income group")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
