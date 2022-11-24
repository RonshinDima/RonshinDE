m=int(input('ввести количество строк'))
n=int(input('ввести количество столбцов'))
x=[]
helper=[]
c=int(input())
d=int(input())
for i in range(m):
    b=[]
    for j in range(n):
        print('введите [',i,',',j,'] элемент')
        b.append(int(input()))
    x.append(b)
print('исходный массив')
for i in range (m):
    for j in range(n):
        print(x[i][j], end=' ')
    print()
for i in range (len(x)):
    if c in x[i]:
        helper.append(i)
print(helper)
for i in helper:
    for j in range(len(x[i])):
        x[i][j] *= d
print(x)
