def leadersoflist(size,data):
    for i in range(0,size):
        for j in range(i,size):
            if(data[i] < data[j]):
                break
            if (j == size - 1):
                print(data[i])
size=int(input())
data=list(map(int,input().split()))
print(leadersoflist(size,data))
