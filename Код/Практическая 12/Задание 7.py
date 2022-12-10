import time
def main(a, b):
    if a-1>b:
        print(b+1, end= " ")
        b+=1
        if a > b:
            main(a, b)
    if a < b-1:
        print(a+1, end = " ")
        a+=1
        if a < b:
            main(a, b)
def second(a, b):
    while a < b:
        a + 1



a = int(input("Введите первое число: "))
b = int(input("Введито второе число"))

main(a, b)