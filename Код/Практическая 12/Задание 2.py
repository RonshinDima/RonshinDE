mas = []
def recurs():
    global mas
    a = int(input())
    mas.append(a)
    if a != 0:
        recurs()
recurs()
mas.remove(max(mas))
print(max(mas))