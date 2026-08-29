from src.validate import file_validate, dataset_validate
from src.load import load_data
from src.analyze import analyze_data, visualization_data
from src.visualize import create_visualizations


def report(results, filename):
    print(
        "=" * 30 + "\n"
        + "       DATASET ANALYSIS\n"
        + "=" * 30 + "\n\n"
        + f"Dataset: {filename}\n\n"
        + f"Rows: {results['rows']}\n"
        + f"Columns: {results['columns']}\n\n"
        + "Missing Values\n"
        + "-" * len("Missing Values") + "\n"
        + f"Total: {results['total_missing_values']}\n\n"
        + "Numerical Columns\n"
        + "-" * len("Numerical Columns") + "\n"
        + f"{', '.join(results['numerical_columns'])}\n\n"
        + "Categorical Columns\n"
        + "-" * len("Categorical Columns") + "\n"
        + f"{', '.join(results['categorical_columns'])}\n\n"
        + "Descriptive Statistics\n"
        + "-" * len("Descriptive Statistics") + "\n"
        + f"{results['descriptive_statistics']}\n"
        + "=" * 30
    )


filename = input("Please enter a file name.")

try:
    file_validate(filename)              #file-level validation
    dataframe = load_data(filename)      #loads file and retruns a dataframe
    dataset_validate(dataframe)          #data-level validation
    results = analyze_data(dataframe)    #analyze data and returns a dictionary
    report(results, filename)            #loads dictionary and retuns a terminal build report
    data = visualization_data(dataframe) #loads dataframe and returns dictionary 
    create_visualizations(data)          #create and saves plots 

except FileNotFoundError as error:
    print(error)

except FileStructureError as error:
    print(error)

except DatasetValidationError as error:
    print(error)
