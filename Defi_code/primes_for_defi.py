import json
primesDic={}

for i in range(0,pow(10,6)+1):
    if i not in primesDic:
        primesDic[i]=True
primesDic[0]=False
primesDic[1]=False


def sieve_of_erastos():
    for i in range(2,pow(10,6)+1):
        if primesDic[i]==True:
            j=2
            while i*j<=pow(10,6):
                if primesDic[i*j]==True:
                    primesDic[i*j]=False
                j=j+1
    
if __name__=="__main__":
    sieve_of_erastos()
    f=open("primes.txt","w")
    f.write(json.dumps(primesDic))
    print("Done")
    
    
