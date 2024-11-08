def fibseries(x):
    n1 = 0
    n2 = 1
    count = 0
    
    if x <= 0:
        print(" enter a positive number")
    elif x ==1:    
        print(" fibonocci sequence upto", x, ":")
        print(n1)
    else:

        print("fibonocci series:")   
    while count < x:
        print(n1)
        n3 = n1 + n2    

        n1 = n2 
        n2 = n3
        count = count+1

fibseries(int(input("enter the limit:")))        
    



        
    


        

    
