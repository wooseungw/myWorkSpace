import sys
weight =[]
height =[]
n = int(sys.stdin.readline())

rank = []

for i in range(n):
    weight, height = list(map(int,sys.stdin.readline().split()))

print(weight)
print(height)

sort_weight = []

sort_weight = weight.sort(reverse=True)

#몸무게 정렬 후 번호 부여할것 정렬 

print(sort_weight)
#이차원 배열이라 인덱스값이 하나가 아님
k = 0
while(len(rank)<= n):
    if(sort_weight.index(weight[k])):#data의 값과 sortdata값을 비교후 같으면 sortdata의 index 리턴
        k = 0
        rank.append(sort_data.index(data[0][k]))
    else:
        k = k + 1
         
    
print(rank)