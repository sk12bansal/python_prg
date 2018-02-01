n=int(input())
a=map(int,input().split())
o_dict={}
for ele in a:
	o_dict[ele]=o_dict.get(ele,0)+1
v=list(o_dict.values())
k=list(o_dict.keys())
print(k[v.index(max(v))])
#print(max(v))
