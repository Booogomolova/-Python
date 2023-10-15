users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dictionary_of_stat = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

dictionary_of_stat["Общее количество"] = len(users)
dictionary_of_stat["Уникальные посещения"] = len(set(users))

print(dictionary_of_stat)