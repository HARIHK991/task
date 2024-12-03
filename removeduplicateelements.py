def removeduplicates(inputlist):
    a = set () 
    b = [] 
    for item in inputlist: 
        if item not in a: 
            b.append(item) 
            a.add(item)
    return b


inputlist = [1, 2, 3, 3, 4, 3, 5, 4]
outputlist = removeduplicates(inputlist)
print("Org list:", inputlist)
print("List after removing duplicates:", outputlist)


                  
                  
                  
                  
                

                  


        
        


