# Vendor Invoice Intelligence System
### Freight cost prediction & Invoice risk flagging

---
## Project Overview
This project implements an end-to-end machine learning system designed to support finance teams by:

- Predicting expected freight cost for vendor invoives.

- Flagging high-risk invoices that require manual review due to abnormal cost, freight, or operational patterns.


---
## Business Objective
1. Freight Cost Prediction (Regression)
*Objective:* Predict the expected freight cost for a vendor invoice using quantity, invoice value, and historical behavior.

- Freight is a non-trival component of landed cost
- Poos freight estimation impacts margin analysis and budget.
- Early prediction improves procrument planning and vendor negotiation.

<img height="800" alt="Screenshot (394)" src="https://github.com/user-attachments/assets/25983c6a-c287-46a9-a55b-0c3f1f6e12bb" />


2. Invoice Risk Flagging (Classification)
*Objective:* Predict whether a vendor invoice should be flagged for manual approval due to abnormal cost, freight, or delivery patterns.

- Manual invoice review does not scale.
- Financial leakage often occurs in large or complex invoices.
- Early risk detection improves audit effciency and operational control.

<img  height="800" alt="Screenshot (395)" src="https://github.com/user-attachments/assets/89bc1599-ff5d-41dd-b3c4-dab360586cb1" />


---
## Streamlit application

The Streamlit application demonstrates the complete pipeline:

- Input invoice details
- Predict expected freight
- Flag invoices in real time
- Provide human-readable explanations


---
## Project Structure 

vendor-invoice-system/
│
├── data/
│   ├── inventory.db
│
│
├── freight_cost_prediction/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│  
│
├── invoice_flagging/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│  
│
├── inference/
│   ├── predict_freight.py
│   ├── predict_invoice_flag.py
│   
│
├── models/
│   ├── predict_freight_model.pkl
│   ├── predict_flag_invoice.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── Invoice Flagging.ipynb
│   ├── Predicting Freight Cost.ipynb
│   └── .ipynb_checkpoints/
│
├── app.py
├── README.md

---
## Data Sources
Data stored in a relational SQLite database (inventory.db). 


---
## Model Used

### *Regression (Freight Prediction)*

- Linear Regression (baseline)
- Decision Tree Regressor
- Random Forest Regressor (final model)

### *Classification (Invoice Flagging)*

- Logistic Regression (baseline)
- Decision Tree Classifier
- Random Forest Classifier (Final model with GridSearchCV)


---
## Evaluation Metrics

#### Freight Prediction - 

- MAE
- RMSE
- R2 Score

#### Invoice Flagging

- Accuracy 
- Precision, Recall, F1-Score
- Classification  report

---
## Run the Project

1. Clone the repository:

git clone https://github.com/bhawnakushwaha/vendor-invoice-system.git

2. Train and save Best fit models:

python freight_cost_prediction/train.py
python invoice_flagging/train.py

3. Test models:

python inference/predict_freight.py
python inference.predict_invoice_flag.py

4. Run application:

streamlit run app.py

