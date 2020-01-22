def checkSmall(ele):
    if ele[i] in range(ord('a'),ord('z')+1):
        return 1
    return 0

def checkLArge(ele):
    if ele[i] in range(ord('A'),ord('Z')+1):
        return 1
    return 0

def getList():
    sarr=[]
    carr=[]

    for i in range(0,26):
        sarr.append(ord('a')+i)
        carr.append(ord('A')+i)
    return sarr,carr



if __name__=="__main__":
    small,large=getList()

    plain=input("Enter Plain Text : ")
    key=int(input("Enter Key: "))

