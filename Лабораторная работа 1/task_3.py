list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
index_of_middle = int(len(list_players) // 2)
team1, team2 = list_players[:index_of_middle], list_players[index_of_middle:]
print(team1)
print(team2)
