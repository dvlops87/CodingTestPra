N = int(input())
numList = map(int,input().split(' '))
numList = list(numList)
numList.sort()
bigNum = numList[len(numList)-1]
smallNum = numList[0]
print(smallNum, bigNum)