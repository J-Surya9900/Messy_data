import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 2, 5],
    'age':         [25, np.nan, 35, np.nan, np.nan, 40],
    'city':        ['Mumbai', 'Delhi', np.nan, 'Mumbai', 'Delhi', np.nan],
    'gender':      ['Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
    'annual_income': [40000, 80000, 60000, 120000, 80000, 95000]
})

df_encoded = pd.get_dummies(df, columns=['city'])

le=LabelEncoder()
df_encoded['gender']=le.fit_transform(df_encoded['gender'])

print("\n Encoded df:\n",df_encoded)