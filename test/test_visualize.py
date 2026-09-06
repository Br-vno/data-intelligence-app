import pandas as pd

from src.analyze import visualization_data
from src.visualize import create_visualizations


def test_create_visualizations(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    dataframe = pd.DataFrame({
        "age": [20, 30, 40],
        "salary": [40000, 50000, 60000],
        "name": ["Alice", "Bob", "Charlie"]
    })

    data = visualization_data(dataframe)

    create_visualizations(data)

    assert (tmp_path / "missing_values.png").exists()
    assert (tmp_path / "numerical_distributions.png").exists()


