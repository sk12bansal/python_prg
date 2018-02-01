#code

t=int(input())
for i in range(0,t):
    n=int(input())
    arr=map(int,input().split())
    ans,res=1,0;
    for ele in arr:
        ans=ans*ele;
        res=res+ans;
        print(res)
    res=str(res)
    print(res[0])