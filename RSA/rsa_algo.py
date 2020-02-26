# values of n this algo can be 10^4
import random
import get_primes_array
import phi
from math import gcd 

import eulers_multiplicative_inverse

# This calculates power() in O(log n) time complexity: 
def optimal_power(x,n):  
    temp=1
    if n==0 :
        return 1
    temp=optimal_power(x,n//2)
    if n%2==0:
        return temp*temp
    return x*temp*temp
    

def generate_key(range):
    arr=[]
    while len(arr)!=2:
        ele=random.randint(2,range)
        try:

            if get_primes_array.object[str(ele)]==True:
                arr.append(ele)
        except:
            pass
    p=arr[0]
    q=arr[1]
    #p,q=3,11 here you can reinitialize p and q for sample cases 
    print("p and q are : ",p,q)

    n=p*q
    phi_n=phi.phi(n)

    i=2
    while i<phi_n:
        if gcd(i,phi_n)==1:
            break
        i=i+1
    e=i
    d=eulers_multiplicative_inverse.mul_inverse(e,phi_n)
    public_key=[e,n]
    private_key=[d,p,q]
    return public_key,private_key

def encryption(public):
    while True:
        M=int(input("Enter Message(integer_required) : ")) # the message has to be lesser than n
        if M<public[1]:
            return optimal_power(M,public[0])%public[1]

def decryption(cipher,private):
    return optimal_power(cipher,private[0])%(private[1]*private[2])


        

if __name__=="__main__":
    range=int(input("Enter max range of p and q (valid till 10^3) : "))
    public,private=generate_key(range)
    print("Public_key",public)
    print("Private_key",private)
    cipher=encryption(public)
    print("Cipher Text : ",cipher)
    print("Decrypted Text : ",decryption(cipher,private))