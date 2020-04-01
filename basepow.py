def power(n,e):
    if e==1:
        return n
    else:
        p=n*power(n,e-1)
        return p


n=int(input())
e=int(input())
k=power(n,e)
print(k)
