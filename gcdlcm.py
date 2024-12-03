
def gcd(a, b):
     while b:
        a, b = b, a % b  
        return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)  


print("GCD of 7 and 5:", gcd(7, 5))      
print("LCM of 7 and 5:", lcm(7, 5))  


