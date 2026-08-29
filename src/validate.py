from pathlib import path
import pandas as pd


class FileStructureError(Exception):
  pass
class DatasetValidationError(Exception):
	pass


def file_validate(filename):
    file= path(filename)
    
    if not filename:
      raise FileStructureError(
        "No file path provided. Please enter a file path."
      )
      
    if not file.is_file():
      raise FileStructureError(
        "File does not exist. Please enter a different file."
      )

    if file.suffix.lower() != "csv":
      raise FileStructureError(
        "Invalid file type. Please enter a csv file"
			)
			
  try:
    with open(file, r):
      pass
  except PermissionError:
    raise PermissionError(
      "File cannot be accepted. Check the file permissions."
    )


def dataset_validate(dataframe):
	if dataframe.shape[0] == 0:
		raise DatasetValidationError("Dataset contains no rows.")
	elif dataframe.shape[1] == 0:
		raise DatasetValidationError("Dataset contains no columns.")

