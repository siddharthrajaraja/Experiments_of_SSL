import json

primes=[]
primes_dic={}

def sieve_of_erastos():
    
    for i in range(0,pow(10,7)+1):
        primes.append(True)
    primes[1]=False
    for i in range(2,pow(10,7)+1):
        if primes[i]==True:
            j=2
            while j*i<pow(10,7)+1:
                if primes[i*j]==True:
                    primes[i*j]=False
                j=j+1
    for i in range(0,pow(10,7)+1):
        if primes[i]==True:

            primes_dic[i]=True
        else:
            primes_dic[i]=False   

if __name__=="__main__":
    sieve_of_erastos()
    with open('primes_dict','w') as f:
        f.write(json.dumps(primes_dic))
        print("Done")