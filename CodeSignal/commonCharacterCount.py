def solution(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)
    common_count = 0
    common_letters = list()
    for i in s1_list:
        for j in s2_list:
            if i == j:
                common_count += 1
                common_letters.append(j)
                s2_list.remove(j)
                break
    return len(common_letters)   