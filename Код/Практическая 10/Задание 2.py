def is_odd(line):
    for k in line:
        k = abs(k)
        if not k%2: 
            return(False)
    return(True)
mas = []
with open ("1.txt", "r") as r:
    for line in r:
        mas.append(list(map(int,line.split())))
max = 0
max_line = []
for i in range(len(mas)):
    sum = 0
    if is_odd(mas[i]) == True:
        m = list(map(abs, mas[i]))
        for j in mas[i]:
            j = abs(j)
            sum +=j
        if sum > max:
            max = sum
            max_line = mas[i]
with open("4.txt", 'w') as w:
    w.write(str(max_line))
