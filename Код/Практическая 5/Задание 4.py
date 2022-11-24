def add():
    x=int(input())
    y=int(input())
    i=1
    while y-x > 0:
        x=x+(x*0.1)
        i+=1
    print(i)
    return
c=add()
print(c)