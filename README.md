"# Customer_Churn_Analysis" 
📉 Customer Churn Prediction System
🚀 Overview

This project uses Machine Learning (Random Forest Classifier) to predict whether a telecom customer is likely to churn or stay.
The goal is to help businesses identify at-risk customers early and reduce churn through targeted retention strategies.

🎯 Problem Statement

Customer churn is one of the biggest challenges in subscription-based businesses.

We aim to:

Predict customer churn (Yes/No)
Identify key factors influencing churn
Provide actionable business insights
📊 Dataset

The dataset used is the Telco Customer Churn dataset, which includes:

Customer demographics
Account information
Services subscribed
Billing details
Churn label (target variable)
🧠 Machine Learning Approach
Model Used:
🌲 Random Forest Classifier
Why Random Forest?
Handles mixed data types well
Reduces overfitting
Provides feature importance
Strong performance on tabular data
🔧 Workflow
1. Data Preprocessing
Removed irrelevant columns (Customer ID)
Handled missing values
Converted categorical variables using One-Hot Encoding
Encoded target variable (Churn: Yes → 1, No → 0)
2. Exploratory Data Analysis (EDA)
Churn distribution analysis
Tenure vs Churn relationship
Monthly charges impact on churn
3. Model Training
Train-test split (80/20)
Random Forest training with:
Class balancing
Tuned hyperparameters
4. Evaluation
Accuracy Score
Confusion Matrix
Precision, Recall, F1-score
Threshold tuning for optimal recall
📈 Model Performance
Metric	Score
Accuracy	~0.75
Recall (Churn Class)	~0.82
Precision	~0.51

Focus was placed on recall, as missing a churner is more costly than a false alarm.

🔥 Key Insights
Customers with low tenure are more likely to churn
Month-to-month contracts have the highest churn rate
Higher monthly charges increase churn probability
Long-term contracts significantly reduce churn
📊 Feature Importance

Top drivers of churn:

Tenure
Monthly Charges
Total Charges
Contract Type
Internet Service Type
💾 Model Export

The trained model is saved as:

churn_model.pkl
🚀 How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/churn-prediction.git
cd churn-prediction
2. Install dependencies
pip install -r requirements.txt
3. Run Jupyter Notebook
jupyter notebook

Open:

churn_prediction_final.ipynb
🌐 Future Improvements
Try XGBoost / LightGBM for better performance
Deploy using Streamlit dashboard
Add real-time prediction API
Integrate customer segmentation
🧠 Tech Stack
Python 🐍
Pandas / NumPy
Scikit-learn
Matplotlib / Seaborn
Streamlit (for deployment)
Jupyter Notebook
👨‍💻 Author

Anish Tamang

Passionate about Machine Learning & AI systems
Building real-world predictive models
⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!