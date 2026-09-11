from src.validate import file_validate, dataset_validate
from src.load import load_data
from src.analyze import analyze_data, visualization_data
from src.visualize import create_visualizations


def test_full_pipeline(tmp_path, monkeypatch):
  
  monkeypatch.chdir(tmp_path)
  
  filename = "/workspaces/data-intelligence-app/data/titanic.csv" 
  
  file_validate(filename) 
  dataframe = load_data(filename) 
  dataset_validate(dataframe)
  
  results = analyze_data(dataframe) 
  assert isinstance(results, dict) 
  
  data = visualization_data(dataframe) 
  assert isinstance(data, dict) 

  create_visualizations(data, tmp_path)
  assert (tmp_path / "missing_values.png").exists() 
  assert (tmp_path / "numerical_distributions.png").exists()
