def factor(n,i):
    if n==1:
        return 1
    else:
        if n%i==0:
            print(i)
            factor(n/i,i)
        else:
            i=i+1
            factor(n,i)

n=int(input())
factor(n,2)
        
            
