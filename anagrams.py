def checkanagrams(str1,str2):
    a=sorted(str1.lower())
    b=sorted(str2.lower())
    if a==b:
        return " it is a anagram" 
    else:
        return "it is not a anagram" 
    
a="listen"   
b="silent"  
print(f"{a} & {b} {checkanagrams(a,b)}")  
            

    
    

        
