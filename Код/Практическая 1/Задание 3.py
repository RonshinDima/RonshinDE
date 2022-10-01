name=str(input("введите имя"))
if name==('Иван'):
    print("имя не подходит")
age=int(input())
if age>=16 and age<75:
    print("Поздравляем вы поступили в ВГУИТ")
elif age < 16 and age > 0:
    print("Сначала нужно окончить школу!")
else:
    print("Введите возраст корректно")
if age < 16:
    print('Вам осталось учиться в школе ',16-age,'лет')

