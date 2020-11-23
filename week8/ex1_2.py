
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
def copy_map(func,a):
    for i in a:
        yield func(i)

def copy_enumerate(a):
    s=0
    for i in a:
        yield (s,i)
        s+=1
