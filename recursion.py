def add(n):
    sum=0
    if(n==0):
        return n
    else:   
        sum=sum+add(n-1)
        return sum
    


n=int(input())
k=add(n)
print(k)
