# 🧠 E-Commerce Customer Churn Prediction (Module 3)

This project aims to identify customers who are likely to churn (stop using the platform) based on their behavior and engagement patterns.  
By predicting churn early, businesses can take proactive measures to retain valuable customers through targeted marketing and improved service strategies.

---

## 📊 1. Project Overview

Customer churn is a major challenge for e-commerce platforms, as acquiring new customers often costs more than retaining existing ones.  
This project uses **machine learning models** to analyze customer data and predict churn probability, allowing for actionable insights that support customer retention efforts.

---

## 🧩 2. Dataset Summary

The dataset includes demographic and behavioral variables such as:

| Feature | Description |
|----------|-------------|
| `Tenure` | Number of months a customer has been with the platform |
| `WarehouseToHome` | Distance (in km) between customer home and warehouse |
| `NumberOfDeviceRegistered` | Number of devices registered per customer |
| `SatisfactionScore` | Customer satisfaction rating (1–5) |
| `Complain` | Whether a customer has filed complaints |
| `DaySinceLastOrder` | Days since the last order |
| `CashbackAmount` | Cashback received by the customer |
| `PreferedOrderCat` | Most frequently purchased product category |
| `MaritalStatus` | Customer marital status |
| `Churn` | Target variable (1 = Churned, 0 = Retained) |

---

## ⚙️ 3. Data Preprocessing

Steps performed:
- **Missing value treatment** using median for numeric features.  
- **Encoding categorical variables** (`PreferedOrderCat`, `MaritalStatus`) using **OneHotEncoder**.  
- **Feature scaling** with **RobustScaler** for numeric columns (`Tenure`, `CashbackAmount`, `DaySinceLastOrder`).  
- **Resampling** using **RandomUnderSampler** and **SMOTE** to handle class imbalance.  
- **Train–test split** with `stratify=y` to preserve churn ratio.

---

## 📈 4. Exploratory Data Analysis (EDA)

Key findings:
- **Tenure** and **CashbackAmount** have the strongest negative correlation with churn.  
- **Complain** shows a strong positive correlation (+26%), indicating dissatisfied customers are more likely to churn.  
- Customers with longer engagement and higher cashback tend to remain loyal.  
- **Preferred categories** like *Mobile* and *Mobile Phone* show higher churn rates, likely due to infrequent purchases.  
- **Married customers** form the majority user base (52.1%), suggesting potential for loyalty-focused offers.

---

## 🤖 5. Model Development

Several classification models were tested with different resampling techniques:

| Model | Resampler | Mean F2 (CV) | F2 (Test Set) |
|--------|------------|--------------|----------------|
| **XGBoostClassifier** | RandomUnderSampler | **0.805** | **0.763** |
| RandomForestClassifier | RandomUnderSampler | 0.790 | 0.752 |
| GradientBoostingClassifier | RandomUnderSampler | 0.746 | 0.717 |
| DecisionTreeClassifier | RandomUnderSampler | 0.752 | 0.709 |

✅ **Best Model:** XGBoost Classifier (RandomUnderSampler)

The F2 score emphasizes recall, aligning with business needs to **capture more actual churners**, even if precision slightly decreases.

---

## 💡 6. Feature Importance (XGBoost)

| Rank | Feature | Importance |
|------|----------|-------------|
| 1 | `Tenure` | 0.2016 |
| 2 | `Complain` | 0.1960 |
| 3 | `PreferedOrderCat_Laptop & Accessory` | 0.0830 |
| 4 | `CashbackAmount` | 0.0686 |
| 5 | `DaySinceLastOrder` | 0.0631 |
| 6 | `MaritalStatus_Single` | 0.0615 |

Key takeaway:  
**Customer tenure** and **complaint behavior** are the strongest indicators of churn. Customers who stay for shorter periods or lodge complaints are at higher risk of leaving.

---

## 🧾 7. Model Evaluation

| Metric | Train Set | Test Set |
|---------|------------|-----------|
| **F2 Score** | 0.871 | 0.738 |
| **Recall** | 0.980 | 0.837 |
| **Precision** | 0.630 | 0.500 |

The model prioritizes recall to ensure more churners are captured — a desirable trait for customer retention-focused use cases.

---

## 🔍 8. Confusion Matrix Insights

| | Predicted No | Predicted Yes |
|--|---------------|---------------|
| **Actual No** | 490 | 164 |
| **Actual Yes** | 28 | 107 |

- The model correctly identified **107 churners** and **490 loyal customers**.  
- **164 customers** were incorrectly flagged as churners (False Positives).  
- **28 churners** were missed (False Negatives) — these are the highest priority for retention efforts.

---

## 🚀 9. Actionable Insights

- **Customer Retention:**  
  Focus on identifying and re-engaging customers with short tenure or unresolved complaints through loyalty campaigns and proactive outreach.  

- **Model Refinement:**  
  Further optimize the XGBoost model through hyperparameter tuning or hybrid resampling (e.g., SMOTE + UnderSampler) to improve precision.  

- **Business Strategy:**  
  Analyze customers incorrectly flagged as churners to identify loyalty patterns, and address common issues among true churners such as complaint resolution or delayed delivery.  

---

## 🏁 10. Conclusion

- The **XGBoost Classifier** emerged as the **best-performing model**, achieving an F2 score of **0.76** and strong recall performance.  
- Tenure, complaint history, and cashback incentives are the most influential features affecting churn.  
- The findings provide valuable direction for improving **customer retention, satisfaction, and engagement** in the e-commerce platform.

---

## 🧰 Tools & Libraries
- **Python 3.12**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Scikit-learn**, **Imbalanced-learn**
- **XGBoost**

---

## 👩‍💻 Author
**Lily Lily**  
Data Science & Machine Learning Enthusiast  
📧 *[Add your contact or LinkedIn link here]*  
