t= int(input())
for i in range(t):
    size = int(input())
    M = []
    for i in range(size):
        list1 = list(map(int,input().strip().split()))
        M.append(list1)
    count = 0
    for i in range(size):
        for j in range(size):

            for k in range(i+1):
                for l in range(j+1):
                    if M[i][j]<M[k][l]:
                        count +=1
    print(count)
