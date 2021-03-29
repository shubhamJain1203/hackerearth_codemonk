t = int(input())

for i in range(t):
    list1 = list(map(int,input().strip().split()))
    n = list1[0]
    k = list1[1]
    a = list(map(int,input().strip().split()))
    # print(list1,"\n",a)
    output = []
    if n>=k:
        for i in range(n):
            output.append(a[i-k])
        print(*output)
    if n<k:
        k = k%n
        for i in range(n):
            output.append(a[i-k])
        print(*output)