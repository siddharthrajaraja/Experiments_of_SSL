import numpy as np

smallCases=[]
largeCases=[]


def getList():
    
    for i in range(0,26):
        smallCases.append(chr(ord('a')+i))
        largeCases.append(chr(ord('A')+i))
    print(smallCases)
    print(largeCases)

def checkSmall(ele):
    if ord(ele) in range(ord('a'),ord('z')+1):
        return 1
    return 0

def checkLarge(ele):
    if ord(ele) in range(ord('A'),ord('Z')+1):
        return 1
    return 0

def returnSumCipher(plain,key):
    sumEncryptText=[]

    for i in range(0,len(plain)):
        if checkSmall(plain[i]):
            
            sumEncryptText.append( smallCases[ abs(ord(plain[i])-ord('a')+key)%26 ])
        elif checkLarge(plain[i]) :
            sumEncryptText.append( largeCases[ abs(ord(plain[i])-ord('A')+key)%26 ])
        else:
            sumEncryptText.append(plain[i])
    return sumEncryptText    

def isPrime(n):
    c=1
    for i in range(2,n+1):
        if n%i==0:
            c=c+1
        if c>2:
            return 0
    return 1


def getRowsnCols(length):
    rows=1
    for i in range(length,1,-1):
        if length%i==0 and isPrime(i)==1:
            rows=i
            break

    columns=length//i

    
    return rows,columns


def senderEncrypts(plain,key):
    sumCipher=returnSumCipher(plain,key)

    rows,columns=getRowsnCols(len(sumCipher))

    sumCipher= np.array(sumCipher)

        
    sumCipher= sumCipher.reshape((rows,columns))

    print(sumCipher,rows,columns)
    
    sumCipher=list(sumCipher)

    
    sumCipher=list(zip(*sumCipher))


    print(sumCipher,rows,columns)
        
    encryptedText=""
    for i in range(0,len(sumCipher)):
        encryptedText+="".join(list(sumCipher[i]))
    
    print("Encrypted Text is : ",encryptedText)

    return encryptedText,key


def returnPlainText(cipherText,key):
    print(cipherText)
    plainText=""
    for i in range(0,len(cipherText)):
        if checkSmall(cipherText[i]):
            if( ord(cipherText[i]) - ord('a')-key<0):
                plainText+=smallCases[25-abs(ord(cipherText[i]) - ord('a')-key)]
            else:
                plainText+=smallCases[abs(ord(cipherText[i]) - ord('a')-key)]
        elif checkLarge(cipherText[i]):
            if( ord(cipherText[i]) - ord('A')<0):
                plainText+=largeCases[25-abs(ord(cipherText[i]) - ord('A')-key)]
            else:
                plainText+=largeCases[abs(ord(cipherText[i]) - ord('A')-key)]
        else:
            plainText+=cipherText[i]
    print("Plain Text Decrypted : ",plainText)    

            

def receiverDecrypts(cipherText,key):
    rows,columns=getRowsnCols(len(cipherText))
    
    cipherText=list(cipherText)

    cipherTextList=[]

    i=0
    while i<len(cipherText):
        cipherTextList.append(cipherText[i:i+rows+1])

        i=i+rows
    

    print( cipherTextList ,rows,columns)

    cipherTextList=list(zip(*cipherTextList))

    for i in range(0,len(cipherTextList)):
        cipherTextList[i]=list(cipherTextList[i])
    
    cipherTextList=np.array(cipherTextList)
    print( cipherTextList ,rows,columns)

    cipherTextList=cipherTextList.reshape((1,len(cipherText)))
    
    cipherText=list(cipherTextList[0])
    print(cipherText)

    returnPlainText(cipherText,key)

if __name__=="__main__":
    getList()

    plain=input("Enter Plain Text : ")
    key=int(input("Enter Key: "))
    cipherText,key=senderEncrypts(plain,key)
    receiverDecrypts(cipherText,key)
