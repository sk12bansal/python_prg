s="WINDHOEKCISCOVIDEO"
t="LINGUACISCOSYSTEM"
for i in range(0,len(s)):
	for j in range(0,len(s)-i):
		print(s[j],end=" ")
	if i!=len(s)-1:
		print()
for i in range(0,len(t)+1):
	for j in range(0,i):
		print(t[j],end=" ")
	print()