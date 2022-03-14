import pandas as pd
import numpy as np

def prep_telco(df):
    #drop duplicates
    df.drop_duplicates(inplace=True)
    #drop columns that are redundant
    df.drop(columns =['contract_type_id', 'internet_service_type_id', 'payment_type_id'])

    #convert total charges(dtype = 'object') to float type
    df['total_charges'] = df.total_charges.replace(' ', np.nan).astype(float)

    #store values not changed
    keep_var = ['customer_id','senior_citizen']
    #store numerical variable
    num_var = ['tenure', 'monthly_charges', 'total_charges']

    #encode using map function
    new_df = pd.DataFrame()

    map1 = {'No':0, 'Yes':1, 'No phone service':0, 'No internet service':0}
    col1 = ['partner', 'dependents', 'phone_service', 'multiple_lines', 
                'online_security', 'online_backup', 'device_protection', 'tech_support', 
                'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn']
    
    # append encoded variables into new_df
    for col in col1:
        new_df[col] = df[col].map(map1)
    new_df['is_male'] = df.gender.map({'Male':1,'Female':0})

    #create dummy_df for data that have more than two options
    dummy_df = pd.get_dummies(df[[
                              'contract_type',
                              'internet_service_type',
                              'payment_type',]], dummy_na=False, drop_first=False)
    #cocat everything together
    df = pd.concat([new_df, dummy_df, df[num_var], df[keep_var]], axis=1)

    return df