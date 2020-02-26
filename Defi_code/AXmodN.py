def getExp2Array(x):    # This function returns the 2^x array which sums up to form x
    arr=[1]
    
    while arr[-1]<x:
        arr.append(arr[-1]*2)
    
    i=len(arr)-1
    
    while i>=0:
        if arr[i]<=x:
            x=x-arr[i]
            arr[i]=[arr[i],1]
        else:
            arr[i]=[arr[i],0]

        i=i-1

    return arr

def getSolution(a,x,n):
    powerTwos=getExp2Array(x)
    
    #print(powerTwos)
    powerOfA=[]

    for i in range(0,len(powerTwos)):
        if i==0:
            powerOfA.append(a%n)
        else:
            powerOfA.append((powerOfA[-1]*powerOfA[-1])%n)
    #print(powerOfA)

    solution=1
    for i in range(0,len(powerTwos)):
        if powerTwos[i][1]==1:
            solution=solution*powerOfA[i]
    
    return solution%n
    #print(solution%n)
        
    
#getSolution(150,649,221)
