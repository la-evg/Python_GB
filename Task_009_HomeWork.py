# =====================================================================
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)
# =====================================================================


a = int(input('Введите номер чертвети: '))

if a == 1:
    print(f'Диапазон значений в {a} чертвети: х > 0, y > 0')
elif a==2:
    print(f'Диапазон значений в {a} четверти: х < 0, y > 0')
elif a==3:
    print(f'Диапазон значений в {a} четверти: х < 0, y < 0')
elif a== 4:
    print(f'Диапазон значений в {a} четверти: х > 0, y < 0')
else:
    print('Введено неверное значение')

    