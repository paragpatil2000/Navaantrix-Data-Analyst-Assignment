# Task 2: Descriptive & Predictive Analysis with Interactive Dashboard

This task includes:
- Descriptive analysis (EDA)
- Interactive visualizations using Plotly
- Predictive modeling using Linear Regression
- A clean Jupyter Notebook dashboard

Dataset used: **SampleSuperstore.csv**

---

## 📁 Folder Structure

task2_dashboard/
│
├── SampleSuperstore.csv
├── dashboard.ipynb
└── README.md


---

## 📌 Objectives

1. Perform **Descriptive Analysis (EDA)**
2. Create **3 interactive visualizations**
3. Build a **predictive model** to estimate sales
4. Display everything inside a **Jupyter Notebook dashboard**

---

## 🛠 Technologies Used

- Python 3.x  
- Pandas  
- NumPy  
- Plotly Express  
- Scikit-learn  
- Jupyter Notebook  

Install dependencies:
pip install pandas numpy plotly scikit-learn


---

## ✨ Descriptive Analysis (EDA)

- Category-wise Sales  
- Region-wise Profit  
- Discount vs Profit distribution  
- Summary statistics  
- Missing value check  

---

## 📊 Interactive Visualizations

### ✔ 1. Category-wise Sales (Bar Chart)
Interactive bar chart showing which category generates maximum sales.

### ✔ 2. Region vs Profit (Heatmap)
Density heatmap showing profit distribution across regions.

### ✔ 3. Discount vs Profit (Scatter Plot)
Scatter plot showing effect of discount on profit across categories.

---

## 🤖 Predictive Model

A **Linear Regression** model was built to predict **Sales** using:

- Quantity  
- Discount  

### 📌 Model Performance:
- MAE: ~275  
- RMSE: ~754  
- Coefficients show:
  - Quantity increases sales  
  - Discount reduces sales  

### 📌 Sample Prediction:
Quantity = 5
Discount = 0.1
Predicted Sales ≈ 297.77




---

## ▶️ How to Use

1. Open Jupyter Notebook  
2. Load `dashboard.ipynb`  
3. Run all cells  
4. View interactive charts and predictions  

---

## 🧩 Challenges Faced

- Large dataset required grouping before plotting  
- Discount had negative correlation with profit  
- Ensuring interactive graphs for cross-analysis  
- Handling numeric conversion for ML model  

---

## ✔ Status

All requirements completed:
✓ Descriptive Analysis  
✓ 3 Interactive Charts  
✓ Predictive Model  
✓ Dashboard Notebook  

---

