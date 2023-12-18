# Industrial Copper Modeling

## Project Domain - Manufacturing

### Problem Statement:
In the copper industry, handling sales and pricing data posed challenges due to skewness and noise. Manual efforts were time-consuming and less accurate. Machine learning regression models were proposed to enhance accuracy by employing techniques like data normalization and outlier detection. Additionally, a lead classification model aimed to assess the likelihood of leads becoming customers, using WON for success and LOST for failure.

### Problem Approach:

1) **Data Understanding:**
   - Identified variable types (continuous, categorical).
   - 
  
2) **Data Preprocessing:**
   - Handled missing values (mean/median/mode).
   - Treated outliers (IQR method).
   - Addressed skewness with transformations (log transformation).
   - Encoded categorical variables (label).

3) **EDA:**
   - Visualized outliers and skewness using Seaborn (boxplot, distplot, violinplot).

4) **Feature Engineering:**
   - Understood the feature and its importance.
   - Dropped highly correlated columns using a heatmap and coorelation factor.

5) **Model Building and Evaluation:**
   - Split dataset (training, testing).
   - Trained and evaluated by using ML algorithms (DecissionTree, RandomForest, XGBoost).
   - Optimized model hyperparameters (cross-validation, grid search).
   - Assessed performance (accuracy, precision, recall, F1, AUC).

6) **Model Pickling**
   - Used pickle to dump/load ML models.

7) **Model GUI (Streamlit):**
   - Created an interactive streamlit application for Regression/Classification model.
   - Values excluding 'Selling_Price' for regression, 'Status' for classification were taken as input.
   - Predicted output data by using ML models and then displayed results on streamlit.

### Tools Used
- Python scripting
- Data Preprocessing
- EDA
- Streamlit
