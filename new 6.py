color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Remove in reverse order of index to maintain correct indexing during deletion
result = [v for i, v in enumerate(color_list) if i not in (0, 4, 5)]
print(f"Filtered List: {result}")
