def inttwo(a):
    mas= []
    while a != 0:
        b=a%2
        mas.append(b)
        a = a//2
        inttwo(a)
    mas.reverse()
    string = ""
    for i in mas:
        string+="".join(str(i))
    return(string)

def palindrom(a):
    for i in range(len(a)):
        if a[i]!=a[-1-i]:
            return(False)
    return(True)

def simple(a):
    for i in range(2, a):
        if not a%i: return(False)
    return(True)

array = []
n = int(input("Введите число: "))
for i in range(n+1):
    if simple(i) == True:
        if palindrom(inttwo(i)) == True:
            array.append(i)
print(array)
