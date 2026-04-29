# Importing Necessary Libraries For Data Handling, Model Training, Balancing & Evaluation.
import os
import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Function To Display Key Metrics For Fraud Detection Models In A Clear Format.
def display_fraud_metrics(model_title, actual_labels, predicted_labels):

    matrix = confusion_matrix(actual_labels, predicted_labels)
    
    print("\n")
    print(f"{model_title.upper()}")
    print("-" * 45)
    print(f"Accuracy  :  {accuracy_score(actual_labels, predicted_labels):.4f}")
    print(f"F1 Score  :  {f1_score(actual_labels, predicted_labels):.4f}")
    print(f"Precision :  {precision_score(actual_labels, predicted_labels):.4f} (Valid Frauds / Total Flagged)")
    print(f"Recall    :  {recall_score(actual_labels, predicted_labels):.4f} (Caught Frauds / Total Actual Frauds)")
    
    print("\n")
    print("Breakdown (Confusion Matrix) :")
    print(f"Correctly Ignored (True Negative) : {matrix[0][0]}")
    print(f"False Alarms (False Positive)     : {matrix[0][1]}")
    print(f"Missed Frauds (False Negative)    : {matrix[1][0]}")
    print(f"Caught Frauds (True Positive)     : {matrix[1][1]}")
    print("-" * 45)

# Fetching The Credit Card Fraud Dataset From Kaggle Using KaggleHub Library. 
print("Fetching The Credit Card Dataset From Kaggle...")
dataset_path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
# Loading The Dataset Into A Pandas DataFrame For Analysis & Model Training.
fraud_data = pd.read_csv(os.path.join(dataset_path, "creditcard.csv"))

# Scaling The 'Amount' & 'Time' Features To Ensure They Are On A Similar Scale As The PCA Components, 
# Which Helps The Logistic Regression Model Perform Better.
print("\n")
print("Scaling The Money & Time Features...")
scaler = StandardScaler()
fraud_data[['Amount', 'Time']] = scaler.fit_transform(fraud_data[['Amount', 'Time']])

# Separating The Features From The Target Variable 'Class', Then Splitting The Data Into Training & Testing Sets.
features = fraud_data.drop('Class', axis=1)
labels = fraud_data['Class']

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2, random_state=42, stratify=labels)

# Displaying The Distribution Of Fraud Cases In The Training Set To Highlight The Imbalance.
print("\n")
print("Training The Baseline Model On Imbalanced Data...")
baseline_model = LogisticRegression(max_iter=1000, random_state=42)
baseline_model.fit(train_features, train_labels)

# Evaluating The Baseline Model To Show The Impact Of Class Imbalance On Fraud Detection Performance.
display_fraud_metrics("Baseline Model (No SMOTE)", test_labels, baseline_model.predict(test_features))

# Applying SMOTE To The Training Data To Create Synthetic Fraud Cases, Which Helps The Model Learn To Detect Frauds Better.
print("\n")
print("Balancing The Training Data With SMOTE...")
oversampler = SMOTE(random_state=42)
balanced_train_features, balanced_train_labels = oversampler.fit_resample(train_features, train_labels)

# Displaying The Change In Fraud Case Distribution After Applying SMOTE To Highlight The Balancing Effect.
print("\n")
print(f"Original Fraud Cases In Training : {sum(train_labels == 1)}")
print(f"New Fraud Cases After Balancing  : {sum(balanced_train_labels == 1)}")

# Training A New Logistic Regression Model On The Balanced Dataset To See The Improvement In Fraud Detection Metrics.
print("\n")
print("Training The New Model On The Balanced Dataset...")
smote_model = LogisticRegression(max_iter=1000, random_state=42)
smote_model.fit(balanced_train_features, balanced_train_labels)

# Evaluating The SMOTE Model To Show The Improvement In Metrics Like Recall & Precision For Fraud Detection.
display_fraud_metrics("SMOTE Model (Balanced Data)", test_labels, smote_model.predict(test_features))