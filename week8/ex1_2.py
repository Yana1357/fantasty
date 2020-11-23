
def copy_zip(*a):
    k=0
    s = 0
    while s!=None:
        A=[]
        for i in a:
            A.append(i[s])
            if i[s] == i[-1]:
                k = None
        yield tuple(A)
        if k != None:
            s += 1
        else:
            s = None
