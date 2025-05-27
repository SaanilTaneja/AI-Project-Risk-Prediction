import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("project_data.csv")
df['Methodology'] = LabelEncoder().fit_transform(df['Methodology'])

X = df.drop("Risk_Level", axis=1)
y = LabelEncoder().fit_transform(df["Risk_Level"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "risk_model.pkl")
print("Model trained and saved as risk_model.pkl")
