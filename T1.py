given_list=[4, 9, 1, 17, 11, 26, 28, 54, 69, 7, 14, 21, 35, 42, 49, 1, 9]
first_set=set(given_list)
second_set={num for num in range(1, 51) if num % 7 == 0}
intersection_set = first_set.intersection(second_set)
result=sorted(list(intersection_set))
print(result)
