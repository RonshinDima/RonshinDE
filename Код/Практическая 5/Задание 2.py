def add():
    N = int(input())
    i = 2
    while N % i != 0:
        i += 1
    print(i)
    return
y=add()
print(y)
