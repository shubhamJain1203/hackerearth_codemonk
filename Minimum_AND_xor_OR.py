t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int,input().split()))
    A = A.sort()
    mini = float('inf')
    for j in range(N-1):
        # mini =min(mini, A[j] ^ A[j+1])
        xor = A[j] ^ A[j+1]
        if mini> xor:
            mini=xor
    print(mini)