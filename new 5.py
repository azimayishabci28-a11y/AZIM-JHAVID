def have_common_member(list1, list2):
    return any(item in list1 for item in list2)

print(have_common_member([1, 2, 3], [3, 4, 5])) # Returns True
