import pandas as pd
import numpy as np

np.random.seed(42)

# Generate synthetic data
n_samples = 200

data = {
    "Duration_Days": np.random.randint(30, 720, size=n_samples),
    "Budget_Utilization": np.random.uniform(50, 120, size=n_samples),
    "Scope_Changes": np.random.poisson(2, size=n_samples),
    "Team_Experience": np.random.uniform(1, 10, size=n_samples),
    "Methodology": np.random.choice(["Agile", "Waterfall", "Hybrid"], size=n_samples),
    "Resource_Count": np.random.randint(2, 30, size=n_samples),
}

df = pd.DataFrame(data)

# Define a function to assign risk level based on conditions
def assign_risk(row):
    score = 0
    if row["Duration_Days"] > 365:
        score += 1
    if row["Budget_Utilization"] > 100:
        score += 1
    if row["Scope_Changes"] > 3:
        score += 1
    if row["Team_Experience"] < 3:
        score += 1
    if row["Methodology"] == "Waterfall":
        score += 1

    if score <= 1:
        return "Low"
    elif score <= 3:
        return "Medium"
    else:
        return "High"

# Apply the function to create the target variable
df["Risk_Level"] = df.apply(assign_risk, axis=1)

# Save both versions
df.to_csv("project_data_with_labels.csv", index=False)
df.drop(columns=["Risk_Level"]).to_csv("project_data.csv", index=False)

print("✅ Dataset generated successfully:")
print("- project_data.csv (for prediction)")
print("- project_data_with_labels.csv (for training)")
