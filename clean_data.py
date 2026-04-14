from os import remove
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 2, 5],
    'age':         [25, np.nan, 35, np.nan, np.nan, 40],
    'city':        ['Mumbai', 'Delhi', np.nan, 'Mumbai', 'Delhi', np.nan],
    'gender':      ['Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
    'annual_income': [40000, 80000, 60000, 120000, 80000, 95000]
})

df['age'].fillna(df['age'].median(), inplace=True)

df['city'].fillna(df['city'].mode()[0], inplace=True)

df=df.drop_duplicates()

print("Cleaned df:\n",df)