n = int(input("введите строки"))
m = int(input("введите столбцы"))
mas = []
with open ('vvod.txt', "r") as r:
    r.seek(0)
    for line in r:
        a = line
        print(a)
        mas.append(list(map(int, a.split())))
print(mas)
c = int(input("введите число"))
d = int(input("введите умножение"))
for i in range(len(mas)):
    for j in range(len(mas[i])):
        if mas[i][j] == c:
            mas[i] = [f*d for f in mas[i]]
            break
with open("vivod.txt", "w") as w:
    for i in mas:
        w.write(f"{i}\n")
print(mas)
