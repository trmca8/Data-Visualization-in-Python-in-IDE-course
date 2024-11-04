# Correct solution for grouping data
grouped_data = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)
print(grouped_data)
