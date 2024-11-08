list = [1, 2, 3, 4, 5, 6, 7]

def revoflist(x):
    reversed_list = []
    for item in x:
        reversed_list.insert(0, item)
    return reversed_list

revlist = revoflist(list)

print("Org list is :", list)
print("Rev  list is :", revlist)





