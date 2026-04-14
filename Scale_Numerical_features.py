import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler, StandardScaler

from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 2, 5],
    'age':         [25, np.nan, 35, np.nan, np.nan, 40],
    'city':        ['Mumbai', 'Delhi', np.nan, 'Mumbai', 'Delhi', np.nan],
    'gender':      ['Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
    'annual_income': [40000, 80000, 60000, 120000, 80000, 95000]
})

features = ['age','annual_income']

minmax_scaler = MinMaxScaler()
df_encoded = pd.get_dummies(df, columns=['city'])
df_minmax = df_encoded.copy()
df_minmax[features] = minmax_scaler.fit_transform(df_minmax[features])

standard_scaler = StandardScaler()
df_standard = df_encoded.copy()
df_standard[features] = standard_scaler.fit_transform(df_standard[features])

print("\n Standardized data:\n", df_standard)