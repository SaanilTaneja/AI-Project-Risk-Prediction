## Overview

This project leverages Artificial Intelligence (AI) and Machine Learning (ML) to predict the risk level of IT projects. By analyzing historical project data, the model classifies projects as Low, Medium, or High risk, enabling project managers to take proactive steps to avoid budget overruns and delays.

---

## Repository Contents

- `generate_data.py` — Script to generate a sample IT project dataset.  
- `train_model.py` — Script to train the Random Forest risk prediction model.  
- `project_data.csv` — Sample dataset of IT projects (generated).  
- `risk_model.pkl` — Trained ML model saved for predictions.  
- `app.py` — Streamlit app for interactive risk prediction.  
- `requirements.txt` — List of required Python packages.  

---

## Setup and Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/AI-Project-Risk-Prediction.git
    cd AI-Project-Risk-Prediction
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Generate sample dataset (optional):**

    ```bash
    python generate_data.py
    ```

4. **Train the model (optional):**

    ```bash
    python train_model.py
    ```

5. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

6. **Use the app:**

    Upload a CSV file containing IT project data to get risk level predictions in real-time.

---

## Dataset Features

| Feature            | Description                               |
|--------------------|-------------------------------------------|
| Duration_Days      | Project duration in days                   |
| Budget_Utilization | Percentage of budget utilized              |
| Scope_Changes     | Number of scope changes                     |
| Team_Experience   | Average team experience in years            |
| Methodology      | Project methodology (Agile, Waterfall, Hybrid) |
| Resource_Count   | Number of team members                      |
| Risk_Level       | Target variable: Low, Medium, or High risk  |

---

## Model Details

- Model: Random Forest Classifier  
- Training: 70% of dataset  
- Testing: 30% of dataset  
- Output: Risk classification (Low, Medium, High)

---

## Future Work

- Integration with project management tools like Jira and Trello.  
- Real-time project data ingestion and risk updates.  
- Use NLP to analyze project communications for risk signals.

