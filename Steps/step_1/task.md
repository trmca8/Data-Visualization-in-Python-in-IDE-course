# Step 1: Loading and Inspecting Data

## Theory
    Importance of Loading Data
    The first step in any data analysis or visualization project is to load the dataset. Without correctly loading the data, we can’t proceed with the subsequent steps. In Python, pandas is a powerful library used for data manipulation and analysis. pandas allows us to load data from various sources, including CSV files, databases, and Excel files.

## Using pd.read_csv
    The function pd.read_csv() reads a CSV file into a pandas DataFrame. This function is essential for quickly loading and inspecting the structure of our data. After loading, it's useful to display the first few rows of the DataFrame using .head() to ensure the data was loaded correctly and to understand its structure (columns, types of values, etc.).


## Task
1. Load the CSV file into a `pandas` DataFrame.
2. Display the first few rows of the DataFrame to understand the structure.

## Hint
Use `pd.read_csv()` to load the file and `df.head()` to view the data.
