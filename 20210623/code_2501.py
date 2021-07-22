N, K = map(int, input().split(' '))
numList = [0]*N
j=0
for i in range(1,N+1):
    if (N%i)==0:
        numList[j]=i
        j+=1

if len(numList) !=0:
    print(numList[K-1])
else :
    print(0) 
