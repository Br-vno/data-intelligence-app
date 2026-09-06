import pytest
import pandas as pd

from src.analyze import (
    analyze_data,
    visualization_data
)


def test_analyze_return_structure():
    dataframe = pd.DataFrame({
        "age": [20, 30, 40],
        "name": ["Alice", "Bob", "Charlie"]
    })

    results = analyze_data(dataframe)

    assert isinstance(results, dict)

    assert set(results.keys()) == {
        "rows",
        "columns",
        "total_missing_values",
        "numerical_columns",
        "categorical_columns",
        "descriptive_statistics"
    }


def test_dataset_dimensions():
    dataframe = pd.DataFrame({
        "age": [20, 30, 40],
        "name": ["Alice", "Bob", "Charlie"]
    })

    results = analyze_data(dataframe)

    assert results["rows"] == 3
    assert results["columns"] == 2


def test_total_missing_values():
    dataframe = pd.DataFrame({
        "age": [20, None, 40],
        "name": ["Alice", "Bob", None]
    })

    results = analyze_data(dataframe)

    assert results["total_missing_values"] == 2


def test_column_classification():
    dataframe = pd.DataFrame({
        "age": [20, 30, 40],
        "salary": [40000, 50000, 60000],
        "name": ["Alice", "Bob", "Charlie"]
    })

    results = analyze_data(dataframe)

    assert results["numerical_columns"] == ["age", "salary"]
    assert results["categorical_columns"] == ["name"]


def test_descriptive_statistics():
    dataframe = pd.DataFrame({
        "age": [20, 30, 40]
    })

    results = analyze_data(dataframe)

    assert isinstance(
        results["descriptive_statistics"],
        pd.DataFrame
    )

def test_visualization_missing_values():
    dataframe = pd.DataFrame({
        "age": [20, None, 40],
        "salary": [50000, 60000, None],
        "name": ["Alice", "Bob", "Charlie"]
    })

    results = visualization_data(dataframe)

    assert results["missing_values"]["age"] == 1
    assert results["missing_values"]["salary"] == 1
    assert results["missing_values"]["name"] == 0


def test_visualization_numerical_data():
    dataframe = pd.DataFrame({
        "age": [20, 30, 40],
        "salary": [50000, 60000, 70000],
        "name": ["Alice", "Bob", "Charlie"]
    })

    results = visualization_data(dataframe)

    assert list(results["numerical_data"].columns) == [
        "age",
        "salary"
    ]


def test_visualization_data_structure():
    dataframe = pd.DataFrame({
        "score": [80, 90, 70],
        "category": ["A", "B", "C"]
    })

    results = visualization_data(dataframe)

    assert isinstance(results, dict)

    assert set(results.keys()) == {
        "missing_values",
        "numerical_data"
    }


