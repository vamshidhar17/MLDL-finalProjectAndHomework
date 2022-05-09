def fun(n):  
    if(n==0):
        return 1
    if(n==1):
        return 10
       
    c=0
    x=0
    n=2000
    for i in range(10**n):
        j=str(i)
        for k in j:
            if(j.count(k)>1):
                x=1
                break
        if(x==1):
            x=0
            continue
        else:
            c+=1
        
    return c        

print(fun(8))
