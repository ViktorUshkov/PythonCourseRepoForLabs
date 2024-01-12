# TODO Напишите функцию для поиска индекса товара
def first_index_of_item(items, needed_item):
    # т.к. нам нужен первый индекс нужного предмета, используем цикл for с enumerate
    for index, item in enumerate(items):
        # если нужный предмет, нашелся возвращаем его индекс
        if item == needed_item:
            return index
    # если цикл прошел весь список, но не нашел нужный товар, возвращаем None
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = first_index_of_item(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
