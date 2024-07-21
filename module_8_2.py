def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        for j in i:
            try:
                if type(i) == int or float:
                    result += j
            except TypeError:
                incorrect_data += 1
                print(f'некорректный тип данных для подсчета суммы - {j}')
    tuple_data = result, incorrect_data
    return tuple_data
def calculate_average(*numbers):
    try:
        if isinstance(*numbers, int):
            print(None)
        tuple_data = personal_sum(*numbers)
        return tuple_data[0] / (len(*numbers) - tuple_data[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return f'В numbers записан некорректный тип данных'


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')