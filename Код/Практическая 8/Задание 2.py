x = tuple(map(float, input("Введите координаты Х через пробел: ").split()))
y = tuple(map(float, input("Введите координаты Y через пробел: ").split()))
z = tuple(map(float, input("Введите координаты Z через пробел: ").split()))
t = tuple(map(float, input("Введите координаты T через пробел: ").split()))
name_dict = {x:"X", y:"Y", z:"Z", t:"T"}                
main_diff = {}                                       
def main_dif_calc(a, b):
    global main_diff
    main_diff[f"{name_dict[a]} - {name_dict[b]}"] = round(float((((b[0]- a[0])**2)+((b[1]-a[1])**2)+((b[2]-a[2])**2))**0.5), 4) 
def get_key(dict, value):                         
    for k, v in dict.items():
        if v == value:
            return k
def finder(dict):                             
    r = min(dict.values())
    return(r)
main_dif_calc(x, y)
main_dif_calc(x, z)
main_dif_calc(x, t)
main_dif_calc(y, z)
main_dif_calc(y, t)
main_dif_calc(z, t)
print(f"Наименьшее расстояние между точками {get_key(main_diff, finder(main_diff))} = {finder(main_diff)}")     