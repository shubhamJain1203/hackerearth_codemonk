t = int(input())
for i in range(t):
	N,K = (map(int,input().split()))
	bin_num = (input())
	maximum = bin_num
	intial_bin = bin_num
	a=0
	b=0
	rotation=0
	for i in range(N):
		bin_num =  bin_num[1:] + bin_num[0]
		rotation+=1
		if maximum<bin_num:
			a=rotation
			maximum = bin_num
		if bin_num == intial_bin:
			b=rotation
			break
	print(a+b*(K-1))
