def sort_tuples(lst, index):
    return sorted(lst, key=lambda x: x[index])


list = [(1, 2), (3, 1), (2, 3)]
index = 1
result = sort_tuples(list, index)
print(result)  
