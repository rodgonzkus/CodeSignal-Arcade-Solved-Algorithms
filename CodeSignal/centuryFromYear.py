def solution(year):
    if (year<=100):
        return 1
    elif year%100:
        return int(year/100)+1
    else: 
        return year/100  