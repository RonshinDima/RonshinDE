x = tuple(map(float, input("Введите координаты Х через пробел: ").split()))
y = tuple(map(float, input("Введите координаты Y через пробел: ").split()))
z = tuple(map(float, input("Введите координаты Z через пробел: ").split()))
t = tuple(map(float, input("Введите координаты T через пробел: ").split()))
name_dict = {x:"X", y:"Y", z:"Z", t:"T"}                
coord_diff = {}                                       
def coord_dif_calc(a, b):
    global coord_diff
    coord_diff[f"{name_dict[a]} - {name_dict[b]}"] = round(float((((b[0]- a[0])**2)+((b[1]-a[1])**2)+((b[2]-a[2])**2))**0.5), 4) 
def get_key(dict, value):                         
    for k, v in dict.items():
        if v == value:
            return k
def finder(dict):                             
    r = min(dict.values())
    return(r)
coord_dif_calc(x, y)
coord_dif_calc(x, z)
coord_dif_calc(x, t)
coord_dif_calc(y, z)
coord_dif_calc(y, t)
coord_dif_calc(z, t)
print(f"Наименьшее расстояние между точками {get_key(coord_diff, finder(coord_diff))} = {finder(coord_diff)}")     