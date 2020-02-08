import json
object={}    
    
with open('primes_dict','r') as f:
    object=json.loads(f.read())

array_of_primes=[]
for i in range(0,pow(10,7)+1):
    if object[str(i)]==True:
        array_of_primes.append(i)

