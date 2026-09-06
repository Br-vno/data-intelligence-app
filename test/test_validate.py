import pytest
import pandas as pd

from src.validate import (
    file_validate,
    FileStructureError,
    dataset_validate,
    DatasetValidationError,
)


def test_valid_csv():
    file_validate("data/titanic.csv")


def test_no_file_path():
    with pytest.raises(FileStructureError):
        file_validate("")


def test_file_does_not_exist():
    with pytest.raises(FileStructureError):
        file_validate("does_not_exist.csv")


def test_wrong_file_extension(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("test data")

    with pytest.raises(FileStructureError):
        file_validate(test_file)


def test_valid_dataset():
    dataframe = pd.DataFrame({
        "A": [1, 2],
        "B": [3, 4]
    })

    dataset_validate(dataframe)


def test_no_rows():
    dataframe = pd.DataFrame(columns=["A", "B"])

    with pytest.raises(DatasetValidationError):
        dataset_validate(dataframe)


def test_no_columns():
    dataframe = pd.DataFrame(index=[0, 1])

    with pytest.raises(DatasetValidationError):
        dataset_validate(dataframe)


