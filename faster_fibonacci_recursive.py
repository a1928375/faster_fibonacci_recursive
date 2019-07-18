def fibonacci(n):
    L=[0,1]
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        i=2
        while i<=n:
            a=L[i-2]+L[i-1]
            L.append(a)
            i=i+1
        return L[-1]

print fibonacci(0)
print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(5)
print fibonacci(36)
