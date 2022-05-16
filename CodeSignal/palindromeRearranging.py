def solution(inputString):
    letters = list(set(inputString)) #Me dice las letras que tiene el str: ['a', 'b', 'c']
    evenCnt = 0
    for i in range(len(letters)): #3
        count = 0
        for j in range(len(inputString)): #7
            if(letters[i] == inputString[j]):
                count += 1
        if(count % 2 == 1): #Si el contador es impar
            evenCnt += 1 
    return True if (evenCnt < 2) else False