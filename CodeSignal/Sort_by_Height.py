def solution(a):
    size = len(a)
    tree_position = list()
    person_height = list()
    for i in range (0, size):
        if a[i] == -1:
            tree_position.append(i)
        else:
            person_height.append(a[i])
    person_height = sorted(person_height)
    for j in tree_position:
        person_height.insert(j, -1)
    return person_height 