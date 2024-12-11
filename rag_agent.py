import pandas as pd

# Load the cleaned dataset
dataset_path = "refined_jcpenney_data.csv"
data = pd.read_csv(dataset_path)

# Display a preview of the dataset
print("Dataset loaded successfully!")
print(data.head())
