import os
import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# 1. Initialize FRED using the secure environment variable
api_key = os.getenv("FRED_API_KEY")
if not api_key:
    raise ValueError("FRED_API_KEY environment variable not set!")

fred = Fred(api_key=api_key)

# 2. Fetch multiple series (e.g., Unemployment Rate & CPI Inflation proxy)
print("Fetching data from FRED API...")
unemployment = fred.get_series("UNRATE")
cpi = fred.get_series("CPIAUCSL")

# 3. Combine into a clean pandas DataFrame
df = pd.DataFrame({"Unemployment_Rate": unemployment, "CPI": cpi})
df = df.dropna()  # Clean missing values for plotting

# Display sample output in terminal
print(df.tail())

# 4. Generate a simple visualization chart
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Unemployment_Rate"], label="Unemployment Rate (%)", color="teal")
plt.title("US Macroeconomic Indicator Tracker (FRED Data)")
plt.xlabel("Year")
plt.ylabel("Percent")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Save figure for your GitHub README
plt.savefig("fred_analysis_output.png", dpi=300, bbox_inches="tight")
print("Chart successfully saved as fred_analysis_output.png!")
