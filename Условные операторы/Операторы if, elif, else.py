first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first == second and second == third:
    print("Все числа равны")
elif first == second or second == third or first == third:
    print("Два числа равны")
else:
    print("Все числа разные")
