import pandas as pd
import pytest

from src.load import load_data


def test_load_data():
  dataframe = load_data("data/titanic.csv")
  
  assert isinstance(dataframe, pd)


def test_data_loaded_correctly():
  dataframe = load_data("data/titanic.csv")
  
  assert len(dataframe) == 891
  assert len(dataframe.columns) == 15
  



