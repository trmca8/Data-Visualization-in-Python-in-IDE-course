# Step 4: Creating the Grouped Bar Chart

## Introduction to Data Visualization with Seaborn
    seaborn is a Python visualization library built on top of matplotlib, designed for creating attractive and informative statistical graphics easily. The countplot function in seaborn is useful for categorical data, as it creates a bar chart where the height of each bar shows the count of data points in each category.

## Using countplot to Visualize Grouped Data
    countplot automatically counts occurrences of a categorical variable, which is why it's ideal for plotting the number of games per genre on each platform. The hue parameter is used to add a second categorical variable, genre, allowing us to see multiple genres for each platform in a single grouped chart.

## Ordering Categories
    When visualizing data, ordering categories consistently can improve readability. Here, we set order to ["PS4", "XOne", "PC", "WiiU"] to ensure platforms appear in the specified order.


## Task
1. Use `seaborn.countplot` to create a bar chart showing the number of games per genre for each platform.
2. Ensure that the platforms are ordered as: PS4, XOne, PC, WiiU.

## Hint
Set the `order` parameter to `["PS4", "XOne", "PC", "WiiU"]` when calling `countplot`.
