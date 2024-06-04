tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
tuple3 = (4, 6, 7, 8)

set1 = set(tuple1)
set2 = set(tuple2)
set3 = set(tuple3)

common_elements = set1.intersection(set2, set3)

unique_elements1 = set1 - common_elements
unique_elements2 = set2 - common_elements
unique_elements3 = set3 - common_elements

result1 = tuple(unique_elements1)
result2 = tuple(unique_elements2)
result3 = tuple(unique_elements3)

print("Уникальные элементы в кортеже 1:", result1)
print("Уникальные элементы в кортеже 2:", result2)
print("Уникальные элементы в кортеже 3:", result3)
