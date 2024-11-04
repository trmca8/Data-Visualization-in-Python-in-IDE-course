# Step 5: Customizing the Chart

## The Importance of Customizing Data Visualizations
    Customizing visualizations enhances readability and makes them more informative. Adding labels and adjusting elements such as the legend can significantly improve the viewer’s understanding.

## Adding Labels
    Labels for the x-axis and y-axis describe what each axis represents, allowing readers to quickly grasp the meaning of each axis. In this case, we set "platform" as the x-axis label and "count" as the y-axis label to show what each axis represents.

## Positioning the Legend
    Legends identify each color or symbol in a plot. By positioning the legend outside the plot area, we ensure it doesn’t overlap with data, making it easier to read the information on the chart. Using bbox_to_anchor=(1.05, 1) places the legend slightly to the right of the plot, and loc='upper left' ensures it stays aligned with the top of the plot.

## Using plt.tight_layout()
    plt.tight_layout() adjusts the spacing of elements in the plot to prevent overlaps, which is especially useful when we have multiple elements (like a legend) near the plot area.


## Task
1. Add x-axis and y-axis labels to the chart.
2. Move the legend outside the plot area to the upper left.
3. Use `plt.tight_layout()` to ensure the layout fits well.

## Hint
Use `plt.legend(title='genre', bbox_to_anchor=(1.05, 1), loc='upper left')` to adjust the legend.
