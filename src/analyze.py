import pandas as pd

def analyze_data(dataframe):
  rows = dataframe.shape[0]
  columns = dataframe.shape[1]
  
  tot_missing_vals = dataframe.isnull().sum().sum()
  
  numerical_columns = dataframe.select_dtypes(
    include="number"
  ).columns.tolist()
  
  categorical_columns = dataframe.select_dtypes(
    include="object"
  ).columns.tolist()
  
  descriptive_stats = dataframe.describe()
  return {
    "rows" : rows,
    "columns" : columns,
    "total missing_values" : tot_missing_vals,
    "numerical_columns" : numerical_columns,
    "categorical_columns" : categorical_columns,
    "descriptive_statistics" : descriptive_stats
  }

def visualization_data(dataframe):
    return {
        "missing_values": dataframe.isnull().sum(),
        "numerical_data": dataframe.select_dtypes(include="number")
    }
  
