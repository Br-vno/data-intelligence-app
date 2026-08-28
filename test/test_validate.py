import pytest

from src.validate import file_validate, FileStructureError

def test_valid_csv():
    file_validate("data/titanic.csv")

def test_no_file_path():
    with pytest.raises(FileStructureError):
        file_validate("")

def test_file_does_not_exist():
    with pytest.raises(FileStructureError):
        file_validate("does_not_exist.csv")

def test_wrong_file_extension():
    with pytest.raises(FilestructureError):
        file_validate("test.txt)
