import matplotlib.pyplot as plt

def create_visualizations(data):
    missing_values = data["missing_values"]
    numerical_data = data["numerical_data"]

    
    missing_values.plot(kind="bar")
    plt.title("Missing Values by Column")
    plt.xlabel("Column")
    plt.ylabel("Number of Missing Values")
    plt.tight_layout()
    plt.savefig("missing_values.png")
    plt.close()

    numerical_data.hist()
    plt.tight_layout()
    plt.savefig("numerical_distributions.png")
    plt.close()
