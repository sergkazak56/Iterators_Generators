from Iterator_Generator import FlatIterator, flat_generator

if __name__ == '__main__':
    if int(input('Решение каких задач хотите посмотреть? (1 - задания 1-2, 0 - допзадания 3-4: ')):
    # Список для решения заданий 1-2
        nested_list = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', False],
            [1, 2, None],
        ]
    else:
    # Список для решения допзаданий 3-4
        nested_list = [
            ['a', [8, 'jkl', 11, [100, 200]], 'b', 'c'],
            False,
            ['d', 'e', 'f'],
            [1, 2, None],
        ]

    print('Это работа Итератора')
    for item in FlatIterator(nested_list):
        print(item, end = ', ')
    print('\n')
    print('Это вызов Итератора в comprehension-выражении')
    list_ = [item for item in FlatIterator(nested_list)]
    print(list_, '\n')
    print('Это вызов функции Генератора')
    for item in flat_generator(nested_list):
        print(item, end=', ')

