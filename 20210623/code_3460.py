T = int(input())
nList = []
numList = []
locate=0
for i in range(T): 
    n = int(input())
    nList.append(n)
    n=nList[i]
    while(True):
        if (n%2)==1:
            numList.append(locate)
        if n==1:
            break
        n=n//2
        locate+=1
    print(" ".join(map(str,numList)))
    numList.clear()
    locate=0