original_list = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates
unique_list = list(set(original_list))

# Check if empty
is_empty = len(unique_list) == 0

# Clone list
cloned_list = unique_list[:] 
