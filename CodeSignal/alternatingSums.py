def solution (a):
    team_1 = list()
    team_2 = list()
    team_1_weights = 0
    team_2_weights = 0
    for i in range(0, len(a)):
        if i % 2 == 0:
            team_1.append(a[i])
            team_1_weights += a[i]
        else:
            team_2.append(a[i])
            team_2_weights += a[i]
    return [team_1_weights, team_2_weights]