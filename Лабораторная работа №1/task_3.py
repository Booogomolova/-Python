list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_index = len(list_players) // 2  # 2

left_team = list_players[:middle_index]  # list_players[:2]
right_team = list_players[middle_index:]  # list_players[2:]

print(left_team)
print(right_team)