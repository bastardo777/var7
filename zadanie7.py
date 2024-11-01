def check_row(row):
    # Проверяем, что четность элементов чередуется
    for i in range(len(row) - 1):
        if (row[i] % 2) == (row[i + 1] % 2):
            return False

    # Проверяем, что второй элемент в четной строке нечетный
    if len(row) > 1 and row[0] % 2 == 0 and row[1] % 2 == 0:
        return row[1] % 2 != 0

    return True

def count_valid_rows(matrix):
    count = 0
    for row in matrix:
        if check_row(row):
            count += 1
    return count

# Пример двумерных массивов
array1 = [
    [2, 3, 4, 5],
    [1, 2, 3, 4],
    [6, 7, 8, 9],
    [10, 11, 12, 13]
]

array2 = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

count1 = count_valid_rows(array1)
count2 = count_valid_rows(array2)

if count1 == 0:
    print("В первом массиве нет строк, удовлетворяющих условиям.")
else:
    print(f"В первом массиве {count1} строк(и), удовлетворяющих условиям.")

if count2 == 0:
    print("Во втором массиве нет строк, удовлетворяющих условиям.")
else:
    print(f"Во втором массиве {count2} строк(и), удовлетворяющих условиям.")
