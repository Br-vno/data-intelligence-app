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


