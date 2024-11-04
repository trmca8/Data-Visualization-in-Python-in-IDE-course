# Step 3: Grouping Data by Platform and Genre

## Grouping and Aggregation
    In data analysis, grouping is a way to organize data by certain categories. In this step, we are interested in understanding how many games belong to each genre for each platform. pandas provides a powerful tool for grouping with the groupby function, which allows us to specify one or more columns to group by. By grouping by both platform and genre, we can see the count of games within each combination of platform and genre.

## Using size() and unstack()
    After grouping, we use .size() to count the number of rows in each group, which gives us the total number of games in each platform-genre combination. unstack() is a method that reshapes the result, converting one level of the index (in this case, genre) into columns. This makes the data easier to read and plot.


## Task
1. Group the filtered DataFrame by `platform` and `genre`.
2. Count the number of games for each platform-genre combination.

## Hint
Use `df.groupby(['platform', 'genre']).size().unstack(fill_value=0)` to group and count.
