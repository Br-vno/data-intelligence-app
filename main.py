from src.analyze import analyze_data

results = analyze_data(dataframe)

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
