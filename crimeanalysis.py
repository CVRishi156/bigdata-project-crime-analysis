import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------
# LOAD DATASET
# ---------------------
data_path = os.path.join("data", "crime_data.csv")
df = pd.read_csv(data_path)

print("Dataset loaded!")
print(df.head())
print(df.info())

# ---------------------
# PARSE DATE COLUMN
# ---------------------
# Our Date format: "MM/dd/YYYY hh:mm:ss AM/PM"
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %I:%M:%S %p")

# ---------------------
# ADD YEAR, MONTH, HOUR
# ---------------------
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Hour"] = df["Date"].dt.hour

print("Date parsed and new columns added (Year, Month, Hour).")
print(df[["Date", "Year", "Month", "Hour"]].head())

# ---------------------
# ANALYSIS 1 – Crime Count by Year
# ---------------------
crimes_by_year = df.groupby("Year").size().reset_index(name="count")
print("\nCrime Count by Year:")
print(crimes_by_year)

# ---------------------
# ANALYSIS 2 – Top Crime Types
# ---------------------
crime_types = df.groupby("Primary Type").size().reset_index(name="count")
crime_types = crime_types.sort_values(by="count", ascending=False)
print("\nTop Crime Types:")
print(crime_types.head(10))

# ---------------------
# SAVE OUTPUTS AS CSV
# ---------------------
os.makedirs("output", exist_ok=True)

crimes_by_year.to_csv(os.path.join("output", "crimes_by_year.csv"), index=False)
crime_types.to_csv(os.path.join("output", "crime_types.csv"), index=False)

print("\nCSV files saved to output/ folder:")

print(" - output/crimes_by_year.csv")
print(" - output/crime_types.csv")

# ---------------------
# VISUALIZATION – Crimes per Year
# ---------------------
plt.figure(figsize=(10, 5))
plt.plot(crimes_by_year["Year"], crimes_by_year["count"], marker="o")
plt.title("Crime Count by Year")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.grid(True)

plot_path = os.path.join("output", "crime_by_year.png")
plt.savefig(plot_path, bbox_inches="tight")

print(f"\nPlot saved as {plot_path}")

print("\nAnalysis complete")
