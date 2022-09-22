# Функция разворачивания вложенного списка в одномерный список
def unfold_list(list_, unfolded_list):
    """
    Функция разворачивания вложенного списка в одномерный список
    :param list_: вложенный список
    :param unfolded_list: одномерный список (в первый вызов функции попадает пустой список)
    :return: unfolded_list: возврат одномерного списка
    """
    if isinstance(list_, list):
        for item in list_:
            unfold_list(item, unfolded_list)
    else:
        unfolded_list.append(list_)
    return unfolded_list

# Функция-генератор для итераций по вложенному списку любой вложенности
def flat_generator(nested_list):
    """
    Функция-генератор для итераций по вложенному списку любой вложенности
    :param nested_list: вложенный список
    :return: каждый элемент из вложенного списка
    """
    unfolded_list = []
    unfolded_list = unfold_list(nested_list, unfolded_list)
    start = 0
    end = len(unfolded_list)
    while start < end:
        yield unfolded_list[start]
        start += 1

# Класс-итератор для итераций по вложенному списку любой вложенности
class FlatIterator:
    """
    Класс-итератор для итераций по вложенному списку любой вложенности.
    При создании экземпляра класса на вход принимаестся список любого уровня вложенности.
    """
    def __init__(self, nested_list):
        self.unfolded_list = []
        self.nested_list = unfold_list(nested_list, self.unfolded_list)
        self.start = -1
        self.end = len(self.nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.nested_list[self.start]



