# Python code​​​​​​‌‌‌​​​​‌‌‌‌​​​‌​​‌‌​‌‌​​​ below

import pandas as pd

def analyze_penguins(df):
    # Drop rows with missing Sex value
    df = df.dropna()

    # New dataframe and summary values
    result_df = pd.DataFrame()

    result_df["Unique Islands"] = df.groupby('Species')['Island'].count()
    result_df['Avg Culmen Length'] = df.groupby('Species')['Culmen_Length_mm'].mean()
    result_df['Median Flipper Length'] = df.groupby('Species')['Flipper_Length_mm'].median()
    result_df['Total Body Mass'] = df.groupby('Species')['Body_Mass_g'].sum()
    
    return result_df