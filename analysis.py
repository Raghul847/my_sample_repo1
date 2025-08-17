# analysis.py
import matplotlib.pyplot as plt
import pandas as pd

# Quarterly Data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Turnover": [-1.57, 5.43, 4.45, 11.43]
}
industry_target = 8

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Average
average_turnover = df["Turnover"].mean()
print(f"Average Inventory Turnover Ratio: {average_turnover:.2f}")

# Visualization
plt.figure(figsize=(8,5))
plt.plot(df["Quarter"], df["Turnover"], marker="o", label="Company Turnover")
plt.axhline(y=industry_target, color="red", linestyle="--", label="Industry Target (8)")

plt.title("Inventory Turnover Ratio - 2024")
plt.xlabel("Quarter")
plt.ylabel("Turnover Ratio")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("turnover_trend.png", dpi=300)
plt.show()
