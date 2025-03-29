a = int(input("Введите количество строк: "))
b = int(input("Введите количество столбцов: "))

matrix = []
for i in range(a):  # Создаем пустую строку
    row = []
    for j in range(b):  # Запрашиваем элемент для каждой ячейки
        element = int(input(f"Введите элемент [{i + 1}][{j + 1}]: "))
        row.append(element)  # Добавляем строку в матрицу
    matrix.append(row)

print("Матрица:")
for row in matrix:
    print(row)
