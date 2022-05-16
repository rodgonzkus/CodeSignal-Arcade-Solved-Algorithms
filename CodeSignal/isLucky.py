# lucky = Dado un ticket n, será lucky si la suma de la primera mitad de los números es equivalente a la segunda mitad.

def solution(n):
    n = str(n)
    size = len(n) 
    half_size = int(size/2)
    mitad_1 = 0
    mitad_2 = 0
    for i in range(0, half_size):
        mitad_1 += int(n[i])
    for j in range(half_size, size):
        mitad_2 += int(n[j])
    if mitad_1 == mitad_2:
        return True
    else:
        return False  