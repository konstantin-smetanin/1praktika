def factorial(n):
    if n==0:
        return 1
    if n<0:
        return None
    if n>0:
        f=1
        for i in range(1,n+1):
            f*=i
        return f
print("z_______________1")
print(factorial(0))         # 1
print(factorial(5))          # 120
print(factorial(-1))         # None


def arrangements(n,k):
    if n<k:
        return 0
    s=1
    for i in range(k):
        s*= (n-i)
    return s
print("z_______________2")
print(arrangements(13, 6))   # 1235520
print(arrangements(4, 2))   # 12
print(arrangements(5, 5))   # 120
print(arrangements(3, 5))    # 0

def combinations(n,k):
    if k==0:
        return 1
    a=1
    for i in range(k):
        a=a*(n-i)//(i+1)
    return a
print("z_______________3")
print(combinations(13, 6))   # 1716
print(combinations(4, 2))  # 6
print(combinations(64, 8))   # 4426165368
print(combinations(5, 0))  # 1   
