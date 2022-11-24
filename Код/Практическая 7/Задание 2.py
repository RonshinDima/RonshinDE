def add():
    n=int(input('введите длину массива'))
    x = []
    y=[]
    for i in range(n):
        print('введите',i,'элемент')
        x.append(int(input()))
        print('исходный массив', x)
    for el in x:
        if el % 2 != 0:
            y.append(el)
            print('новый массив', x)
    if len(y) == 0:
        print('No numbers')

    print(sorted(y, reverse=True))
    return
y=add()
print (y)