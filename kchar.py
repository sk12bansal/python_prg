t=input()
for i in range(0,t):
	n,k,it=map(int,input().split())
	n=bin(n)
	n=n.split('b')[1]
	s=""
	for itr in range(0,it):
		for ele in n:
			if ele=='1':
				s+='10'
			else:
				s+='01'
	n=s
print(n[k])
