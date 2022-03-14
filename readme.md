# Telco Churn Classification Project

### Project Descriptions
This project is to analyze the customer data and identify the key driver for customer churning. 
I will be exploring the customer data, make an ML classification model, and predict the customers who are likely to churn.

###  Goals
-Find the key drivers for customer churning
-Create classification models
-Predict the customers who are likely to churn

### Initial Questions

- What are the correlation between customer data and churn rate?
- Do demographies affect churn rate?
- Do additional services affect churn rate?
- Do contract type affect churn rate?
- Do payment type affect churn rate?
- Do internet service type affect churn rate?


### Data Dictionary
|Column                                  |Values|
|------                                  |------ |
|partner                                 |int64 (0= No, 1= Yes)|
|dependents                              |int64 (0= No, 1= Yes)|
|phone_service                           |int64 (0= No, 1= Yes)|
|multiple_lines                          |int64 (0= No, 1= Yes)|
|online_security                         |int64 (0= No, 1= Yes)|
|online_backup                           |int64 (0= No, 1= Yes)|
|device_protection                       |int64 (0= No, 1= Yes)|
|tech_support                            |int64 (0= No, 1= Yes)|
|streaming_tv                            |int64 (0= No, 1= Yes)|
|streaming_movies                        |int64 (0= No, 1= Yes)|
|paperless_billing                       |int64 (0= No, 1= Yes)|
|churn                                   |int64 (0= No, 1= Yes)|
|is_male                                 |int64 (0= female, 1= male)|
|contract_type_Month-to-month            |int64 (0= No, 1= Yes)|
|contract_type_One year                  |int64 (0= No, 1= Yes)|
|contract_type_Two year                  |int64 (0= No, 1= Yes)|
|internet_service_type_DSL               |int64 (0= No, 1= Yes)|
|internet_service_type_Fiber optic       |int64 (0= No, 1= Yes)|
|internet_service_type_None              |int64 (0= No, 1= Yes)|
|payment_type_Bank transfer (automatic)  |int64 (0= No, 1= Yes)|
|payment_type_Credit card (automatic)    |int64 (0= No, 1= Yes)|
|payment_type_Electronic check           |int64 (0= No, 1= Yes)|
|payment_type_Mailed check               |int64 (0= No, 1= Yes)|
|tenure                                  |int64|
|monthly_charges                         |float64|
|total_charges                           |float64|
|customer_id                             |object|
|senior_citizen                          |int64 (0= No, 1= Yes)|

### Steps to Reproduce

1. acquire telco_churn.csv from Codeup database. Using the env.py which contains login credential, ensure hostname, username, and password are in the env.py file to connect and rerieve data from the Codeup database.Save it in the same directory you are working on before acquiring.
2. Ensure pandas, numpy, matplotlib, and sklearn libraries are installed.
3. Clone the repo in the same directory.
4. Execute the final_report.ipynb and follow along to reproduce the project.


### The Plan

1. Acquire the telco_churn.csv data
2. Prepare the telco_churn.csv for analysis
- remove redundant features and duplicates
- clean the data that is missing
- encode the features 
3. Explore the data
- explore mainly using correlation of churn rates against other features.
- come up with key drivers for churning, mainly the ones with high churn rate.
4. Model using the following methods:
- Random Forest
- K-Nearest Neighbor
- Logistic Regression
5. Get accuracy score on train, validate datasets and pick the best model, and run the test dataset
6. Predict the churn probability and produce prediction dataset.

### Summary
Key drivers for the churning were identified and models were developed. Logistic regression predicted the best out of other models used. The logistic regression model was used as the difference in train and validate dataset was the lowest. The model was able to predict the churn rate at a 80.62% accuracy level on a test dataset. This is greater than the baseline accuracy level, which is 73.47%.

### Key Findings

Some customer attributes that increase their probability of churn include:
- being earlier in their tenure, in particular in approximately their first year
- having higher monthly charges
- being a senior citizen
- having a partner and dependants

### Recommendations

Since higher monthly charges and early tenure are major drivers of churn, consider offering discounted reates in the first year of tenure. 

### Next Steps

Given more time, I would test models using additional combinations of features. Given enough time and computational resources, I would like to run each of the model types above using all possible combinations of features. 

Additionally, further exploration into those features found to have the largest effect on the model could prove useful|.