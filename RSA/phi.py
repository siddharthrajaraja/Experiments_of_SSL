import json
import get_primes_array

#print(get_primes_array.array_of_primes)

def phi(n):
    if n==1:
        return 0
    if get_primes_array.object[str(n)]==True:
        return n-1
    else:
        i=0

        dic={}

        while n!=1:
            if n%get_primes_array.array_of_primes[i]==0:
                if get_primes_array.array_of_primes[i] not in dic:
                    dic[get_primes_array.array_of_primes[i]]=1
                else:
                    dic[get_primes_array.array_of_primes[i]]+=1
                n=n//get_primes_array.array_of_primes[i]
            else:
                i=i+1
        #print(dic)
        key=dic.keys()
        net_phi=1
        for each_key in key:
            net_phi=net_phi*(pow(each_key,dic[each_key])-pow(each_key,dic[each_key]-1))
        return net_phi


             

