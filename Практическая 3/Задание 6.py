def add():
    d= int(input())
    a= int(input())
    b= int(input())
    c= int(input())
    if (a+b+c+d) % 2 == 0:
        print('YES')
    else:
        print('NO')
    return
y=add()
print(y)