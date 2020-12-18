def maxsubarrayproduct(arr):
    # arr.sort()
    res=1
    re=1
    q=0
    f=0
    max=-1001
    n=len(arr)-1
    k=n
    p=0
    while(k>=0):
        if arr[k]>0:
            res=res*arr[k]
            p+=1
        elif arr[k]<0 :
            re=re*arr[k]
            f+=1
            if(arr[k]>max):
                max=arr[k]
        else:
            q+=1
        k-=1


    if q==len(arr):
        return str(0)
    if re<0 and len(arr)==1:
        return str(re)
    if p==0:
        return str(0)
    if(f%2==0):
        return str(res*re)
    else:
        re=re//max
        return str(re*res)

arr = [0,1]
print(maxsubarrayproduct(arr))
