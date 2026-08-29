import pandas as pd

def analyze_data(dataframe):
  rows = dataframe.shape[0]
  columns = dataframe.shape[1]
  
  tot_missing_vals = dataframe.isnull().sum()
  
  numerical_columns = dataframe.select_dtypes(
    include="number"
  ).columns.tolist()
  
  categorical_columns = dataframe.select_dtypes(
    include="object"
  ).columns.tolist()
  
  descriptive_stats = dataframe.describe()
  return {
    "Rows" : rows,
    "Columns" : columns,
    "Total Missing Values" : tot_missing_vals,
    "Numerical Columns" : numerical_columns,
    "Categorical Columns" : categorical_columns,
    "descriptive_statistics" : descriptive_statistics
  }

def visualization_data(dataframe):
    return {
        "missing_values": dataframe.isnull().sum(),
        "numerical_data": dataframe.select_dtypes(include="number")
    }
  
