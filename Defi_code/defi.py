import json
import random
import AXmodN 


primesNumbers=[]


class Encyption:
    def __init__(self,n,g):
        self.n=n
        self.g=g

        #print("inside class :",n,g)
    def Alice(self):
        
        x=random.randrange(1,pow(10,6)+1)
        
        print("Hello Alice here !!")
        print("Value of g :",self.g)
        print("Value of x :",x)
        print("Value of n : ",self.n)
        
        return AXmodN.getSolution(self.g,x,self.n),x 
         




    def Bob(self):
        y=random.randrange(1,pow(10,6)+1)
        print("Hello Bob here !!")
        print("Value of g :",self.g)
        print("Value of y :",y)
        print("Value of n : ",self.n)

        return AXmodN.getSolution(self.g,y,self.n),y
        

class KeyGeneration:

    def generateK1(B,x,n):
        print("here B is",B,"and x is",x,"and n is",n)
        return AXmodN.getSolution(B,x,n)

    def generateK2(A,y,n):
        print("here A is",A,"and y is",y,"and n is",n)

        return AXmodN.getSolution(A,y,n)






if __name__=="__main__":
    with open("primes.txt","r") as f:

        primes=json.loads(f.read())
        for i in range(0,pow(10,6)+1):
            if primes[str(i)]==True:
                primesNumbers.append(i)
        #print(primesNumbers)
        maxRange=len(primesNumbers)
        n=random.randrange(0,maxRange+1)
        g=random.randrange(0,maxRange+1)
        while n==g:
            g=random.randrange(0,maxRange+1)
        #print("testing ",primesNumbers[n],primesNumbers[g])
        objEncrypt=Encyption(primesNumbers[n],primesNumbers[g])

        A,x=objEncrypt.Alice()
        print("A is : ",A)

        print()
        B,y=objEncrypt.Bob()
        print("B is : ",B)

        print()
        print("Generating Keys :")

        
        K1=KeyGeneration.generateK1(B,x,primesNumbers[n])
        print("Key1 generated is : ",K1)

        K2=KeyGeneration.generateK2(A,y,primesNumbers[n])
        print("Key2 generated is : ",K2)

        if(K1==K2):
            print("Success")
        else:
            print("Failure")