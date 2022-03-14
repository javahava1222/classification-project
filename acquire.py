import pandas as pd
import os
from env import get_db_url


def get_telco_data(use_cache = True):
    filename = 'telco_churn.csv'

    if os.path.exists(filename) and use_cache:
        return pd.read_csv(filename)

    url = get_db_url('telco_churn')
        
    sql = '''
        SELECT * 
        FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN payment_types USING (payment_type_id)
        '''

    df = pd.read_sql(sql, url)
    df.to_csv(filename, index=False)
    return df