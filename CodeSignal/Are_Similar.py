def solution(a, b):
    if a == b:
        return True
    elif sorted(a) != sorted(b):
        return False    
    for i in a:
        if i not in b:
            return False
    cnt = 0
    for i, j in zip(a, b):
        if i != j:
            cnt += 1
            if cnt > 2:
                return False
    if cnt <=2:
        return True