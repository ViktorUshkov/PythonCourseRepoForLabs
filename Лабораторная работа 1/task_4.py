users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict_of_visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}

dict_of_visits["Общее количество"] = len(users)
dict_of_visits["Уникальные посещения"] = len(set(users))

print(dict_of_visits)
