def add():
    a = int(input())
    b = int(input())
    c = int(input())
    if b >= a <= c:
        print(a)
    elif a >= b <= c:
        print(b)
    else:
        print(c)
    return
y=add()
print(y)
