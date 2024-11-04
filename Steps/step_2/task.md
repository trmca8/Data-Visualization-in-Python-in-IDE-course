# Step 2: Filtering Data

## Why Filter Data?
    Filtering data allows us to focus only on the relevant subset, improving the efficiency of our analysis. By narrowing down to specific categories, we can ensure that the final visualization presents the most meaningful information. In this case, we are only interested in four platforms (PS4, XOne, PC, and WiiU), so filtering the dataset to include only those platforms is necessary.

## Using isin() for Filtering
    In pandas, we can filter data based on values in a column by using .isin(). This method checks whether each entry in a column matches any value from a list. For example, df[df['platform'].isin([...])] allows us to include only the rows where the platform column has one of the specified values. This creates a new DataFrame containing only the relevant data for our analysis.


## Task
1. Filter the dataset to include only games for the platforms: PS4, XOne, PC, and WiiU.

## Hint
Use `df[df['platform'].isin([...])]` to filter for specific platforms.
