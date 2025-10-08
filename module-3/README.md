# 🧠 Customer Churn Prediction — Random Forest Model

## 📋 Project Overview
This project focuses on predicting **customer churn** using machine learning.  
The objective is to identify customers who are likely to stop using the service, allowing the business to take proactive actions such as offering discounts, cashback, or loyalty programs to retain them.  

Among the models tested, **Random Forest Classifier** delivered the most stable and interpretable results, balancing performance and business applicability.

---

## ⚙️ Model Used: Random Forest Classifier

### **1. Model Explanation**
Random Forest is an **ensemble learning algorithm** that constructs multiple decision trees and combines their outputs to improve prediction accuracy and reduce overfitting.  
It performs well for both categorical and numerical data, providing high stability and interpretability through feature importance analysis.

---

### **2. Best Parameters Used**
```python
RandomForestClassifier(
    criterion='entropy',
    max_depth=10,
    max_features=None,
    min_samples_leaf=1,
    min_samples_split=2,
    n_estimators=50,
)
```

- **Criterion = 'entropy'** → Splits based on information gain.  
- **Max depth = 10** → Prevents overfitting.  
- **n_estimators = 50** → Ensures stability and efficiency.  
- **max_features = None** → Considers all features at each split.  
- **min_samples_split = 2, min_samples_leaf = 1** → Allows fine granularity in node formation.

---

## 📊 Model Evaluation

### **Confusion Matrix**

| Actual / Predicted | Non-Churn (0) | Churn (1) |
|--------------------|---------------|-----------|
| **Non-Churn (0)**  | 518 (True Negative) | 136 (False Positive) |
| **Churn (1)**      | 17 (False Negative) | 118 (True Positive) |

---

### **Classification Report**

| Metric | Class 0 (Non-Churn) | Class 1 (Churn) |
|:-------|:-------------------:|:----------------:|
| **Precision** | 0.9682 | 0.4646 |
| **Recall** | 0.7920 | 0.8741 |
| **F1-Score** | 0.8713 | 0.6067 |
| **Accuracy** | **0.8061** | |
| **F2-Score** | **0.7431** | *(recall-focused metric)* |

**Interpretation:**  
- The model achieves **high recall (0.87)**, successfully identifying most customers at risk of churn.  
- The **F2-Score (0.74)** emphasizes recall importance, making this model suitable for churn prevention where missing actual churners is costly.  
- Accuracy (80.6%) and balanced performance indicate strong generalization.

---

## 🔑 Feature Importance (Top 10)

| Rank | Feature | Insight |
|:--:|:--|:--|
| 1 | RS__Tenure | Shorter customer relationships correlate with higher churn. |
| 2 | RS__CashbackAmount | Low cashback values reduce customer loyalty. |
| 3 | RS__DaySinceLastOrder | Longer inactivity indicates disengagement. |
| 4 | RS__SatisfactionScore | Lower satisfaction scores are linked to churn. |
| 5 | RS__Complain | Customers who complain are more likely to churn. |
| 6 | RS__NumberOfDeviceRegistered | More devices registered = higher engagement. |
| 7 | OHE__MaritalStatus_Single | Singles show different spending consistency. |
| 8 | OHE__PreferedOrderCat_Laptop & Accessory | Certain product categories affect retention. |
| 9 | OHE__MaritalStatus_Married | Marital status influences loyalty behavior. |
| 10 | OHE__PreferedOrderCat_Mobile Phone | Product type affects engagement level. |

---

## 💰 Cost Analysis

### **Assumptions**
- **Cost of acquiring a new customer:** $315  
- **Cost of retaining a customer:** $63 (1/5 of acquisition cost)

| Metric | Value |
|:--------|:------:|
| False Negatives (FN) | 17 |
| False Positives (FP) | 136 |
| True Positives (TP) | 118 |
| True Negatives (TN) | 518 |

---

### **Cost of False Negatives (FN)**
Customers who churn but are not predicted to churn.  
- **Cost = 17 × $315 = $5,355**

### **Cost of False Positives (FP)**
Customers who do not churn but are predicted to churn.  
- **Cost = 136 × $63 = $8,568**

### **Total Cost with the Model**
- **Cost = $5,355 + $8,568 = $13,923**

### **Total Cost without the Model**
If no predictive model was used:  
- **Cost = 135 × $315 = $42,525**

### **Savings from the Model**
| Scenario | Total Cost (USD) |
|:----------|----------------:|
| Without the model | $42,525 |
| With the model | $13,923 |
| **Savings** | **$28,602** |

---

## 🧠 Business Interpretation
- The Random Forest model **saves approximately $28,600** in churn-related costs.  
- Although it spends slightly more on retention (due to false positives), this is far cheaper than reacquiring churned customers.  
- By proactively targeting customers predicted to churn, the business can **increase retention, lower acquisition costs**, and maintain long-term profitability.  

---

## ✅ Conclusion
The **Random Forest model** provides:
- Strong **recall** (0.87) and **F2-score** (0.74).  
- Clear **feature importance insights** to guide retention strategies.  
- Measurable **financial savings** through reduced churn losses.  

This model is recommended for deployment as a reliable churn prediction system and can serve as a foundation for future model improvements and automation.
