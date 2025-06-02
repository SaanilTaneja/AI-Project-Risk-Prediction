# AI Risk Prediction for IT Project Management

## 🧠 Project Overview

This project builds an AI/ML model that predicts the **risk level** (Low, Medium, High) of IT projects based on historical data. It aims to help project managers proactively identify and mitigate potential risks — improving the chances of successful project delivery.

---

## 📦 Repository Contents

```
AI-Project-Risk-Prediction/
├── generate_data.py               # Generates synthetic data
├── train_model.py                 # Trains the model and saves it as a .pkl
├── app.py                         # Streamlit app for uploading and predicting
├── requirements.txt               # Required Python libraries
├── risk_model.pkl                 # Trained model
├── project_data.csv               # Test data without labels (for predictions)
├── project_data_with_labels.csv   # Data with labels (for training)
└── README.md                      # Project documentation
```

---

## ⚙️ Setup and Usage (with Commands)

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Project-Risk-Prediction.git
cd AI-Project-Risk-Prediction
```

---

### 🛠️ Step 2: Create a Virtual Environment

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\activate
```

---

### 📥 Step 3: Install Required Python Packages

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 🧪 Step 4: Generate Sample Project Dataset (Optional)

If you want to create a fresh dataset for training/testing:

```bash
python generate_data.py
```

This will create two files in your project directory:

project_data_with_labels.csv – includes labels (for training)

project_data.csv – features only (for prediction)

---

### 🤖 Step 5: Train the AI Model (Optional)

Use this command to train the model and save it as `risk_model.pkl`:

```bash
python train_model.py
```

You can skip this if the trained model already exists.

---

### 💻 Step 6: Run the Streamlit App

```bash
streamlit run app.py
```

This will launch the dashboard in your browser, where you can:

- Upload a CSV file with project data
- View predicted risk levels (Low, Medium, High)

---

### 🔚 Step 7: Deactivate the Virtual Environment (When Done)

```bash
deactivate
```

---

## 🧾 Dataset Features

| Feature             | Description                                      |
|---------------------|--------------------------------------------------|
| `Duration_Days`     | Duration of the project in days                  |
| `Budget_Utilization`| % of allocated budget used                       |
| `Scope_Changes`     | Number of times project scope changed            |
| `Team_Experience`   | Average team experience in years                 |
| `Methodology`       | Agile, Waterfall, or Hybrid                      |
| `Resource_Count`    | Number of resources involved                     |
| `Risk_Level`        | Target variable: Low, Medium, or High (Label)    |

---

## 📊 Streamlit Dashboard Features

- CSV Upload for project data
- Interactive prediction and classification
- Visual feedback on project risk levels

---

## 🔮 Future Enhancements

- Integration with Jira, Trello APIs
- Real-time project risk updates
- NLP analysis of project discussions and tickets

---

## 👤 Author

**Contact**  
📧 saaniltaneja@gmail.com  
🌐 https://www.linkedin.com/in/saaniltaneja/

---

## Future Work

- Integration with project management tools like Jira and Trello.  
- Real-time project data ingestion and risk updates.  
- Use NLP to analyze project communications for risk signals.

