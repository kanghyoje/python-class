list1 = [1, 2, 3]
list2 = list((4, 5, 6))

print(list1 + list2)
print(list1 * 3)

list1.extend(list2)
print(list1)