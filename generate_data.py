import pandas as pd
import numpy as np

np.random.seed(42)
n = 300

data = {
    "Duration_Days": np.random.randint(30, 365, size=n),
    "Budget_Utilization": np.random.randint(50, 120, size=n),
    "Scope_Changes": np.random.randint(0, 10, size=n),
    "Team_Experience": np.random.uniform(1, 10, size=n).round(1),
    "Methodology": np.random.choice(["Agile", "Waterfall", "Hybrid"], size=n),
    "Resource_Count": np.random.randint(3, 20, size=n)
}

def assign_risk(row):
    score = 0
    if row['Duration_Days'] > 200: score += 1
    if row['Budget_Utilization'] > 100: score += 1
    if row['Scope_Changes'] > 5: score += 1
    if row['Team_Experience'] < 3: score += 1
    if row['Resource_Count'] < 5: score += 1
    if score >= 3:
        return "High"
    elif score == 2:
        return "Medium"
    else:
        return "Low"

df = pd.DataFrame(data)
df["Risk_Level"] = df.apply(assign_risk, axis=1)
df.to_csv("project_data.csv", index=False)
print("Dataset created: project_data.csv")
