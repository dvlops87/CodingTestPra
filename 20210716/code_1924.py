#x,y입력받기
x,y=map(int,input().split())

#각 달의 일수 딕셔너리로 초기화하기
month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#몇일 있는지 나타낼 변수 초기화하기
date=0
#몇일있는지 구하기
for i in range(1,x):
  date+=month[i]

date+=y
#날들을 7로나눠서 나오는 나머지 값을 키로한 요일 초기화하기
day={1:'MON',2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT',0:'SUN'}

print(day[date%7])