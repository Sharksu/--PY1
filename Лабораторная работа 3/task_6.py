list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = list_numbers[0]  # Изначально зададим максимальному элементу значение первого элемента из списка
count = 0
count_max = 0  # Счетчик индекса максимального элемента

for i in list_numbers:
    if i >= max_:
        max_ = i
        count_max = count
    count += 1

list_numbers[19], list_numbers[count_max] = list_numbers[count_max], list_numbers[19]
print(list_numbers)
