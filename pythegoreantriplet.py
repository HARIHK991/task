a=[3,4,5]
num1=a[0]
num2=a[1]
num3=a[2]

num3xq=num3*num3
print("third number square: ",num3xq)

def triplet():
    num1xq=num1*num1
    num2xq=num2*num2
    sum=num1xq+num2xq

    print(" first two value square sum: ",sum)
    return sum

def checkequal():
    sum=triplet()

    if(sum==num3xq):
        print("is pythagorus")
    
    else:
        
        print("is not a pythagorus")
        

checkequal()     




        


        

    




    


















    


