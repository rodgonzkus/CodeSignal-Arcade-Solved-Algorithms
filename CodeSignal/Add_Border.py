def solution(picture):
    filas = len(picture)
    columnas = len(picture[0])
    answer = []
    answer.append('*' * (columnas+2)) #Borde superior
    for i in range(filas):
        answer.append('*'+picture[i]+'*') #Añado los '*' al inicio y final del str
    answer.append('*' * (columnas+2)) #Borde inferior  
    return answer
