# Industrial Copper Modeling

## Project Domain - Manufacturing

### Problem Statement:
In the copper industry, handling sales and pricing data posed challenges due to skewness and noise. Manual efforts were time-consuming and less accurate. Machine learning regression models were proposed to enhance accuracy by employing techniques like data normalization and outlier detection. Additionally, a lead classification model aimed to assess the likelihood of leads becoming customers, using WON for success and LOST for failure.

### Problem Approach:

1) **Data Understanding:**
   - Identified variable types (continuous, categorical).
   - Converted '00000' values in 'Material_Reference' to null.
   - Treated reference columns as categorical; INDEX was deemed not useful.

2) **Data Preprocessing:**
   - Handled missing values (mean/median/mode).
   - Treated outliers (IQR or Isolation Forest).
   - Addressed skewness with transformations (log, boxcox).
   - Encoded categorical variables (one-hot, label, ordinal).

3) **EDA:**
   - Visualized outliers and skewness using Seaborn (boxplot, distplot, violinplot).

4) **Feature Engineering:**
   - Engineered new features.
   - Dropped highly correlated columns using a heatmap.

5) **Model Building and Evaluation:**
   - Split dataset (training, testing).
   - Trained and evaluated classification models (ExtraTrees, XGB, Logistic Regression).
   - Optimized model hyperparameters (cross-validation, grid search).
   - Assessed performance (accuracy, precision, recall, F1, AUC).

6) **Model GUI (Streamlit):**
   - Created an interactive page for Regression/Classification.
   - Inputted values (excluding 'Selling_Price' for regression, 'Status' for classification).
   - Performed feature engineering, scaling, log transformation used in training.
   - Predicted new data with Streamlit and displayed results.

7) **Tips:**
   - Used pickle to dump/load models (encoder, scaling, ML).
   - Fitted and transformed separately; transformed only for unseen data.

### Tools Used
- Python scripting
- Data Preprocessing
- EDA
- Streamlit
