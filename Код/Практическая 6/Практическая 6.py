def add():
    s = input("введите строчку")
    t = 0
    for i in s:
        if i == "т":
            t += 1
    print(t)
    return
y=add()
print (y)