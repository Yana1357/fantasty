from itertools import permutations

def get_permutations(s, n):
    A=[]
    for i in permutations(s,n):
        stroka=''
        for el in i:
            stroka+=el
        A.append(stroka)
    A.sort()
    return A
