# =======================================================
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
# =======================================================

print('Введите значение X: ')
x = int(input())
print('Введите значение Y: ')
y = int(input())
print('Введите значение Z: ')
z = int(input())

firstPart = not (x or y or z)
secondPart = not x and not y and not z
if firstPart == secondPart:
    print("Истинное утверждение")
else:
    print("Ложное утверждение")