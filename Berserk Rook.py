import numpy as np

#transform char to int. a->0, b->1 ... h->7
def word_to_tuple(a):
    return (ord(a[0]) - 97, int(a[1]) - 1) 

def find(maps,a):
    summ = 0
    x = maps[a[0],] == 1
    y = maps[0:8, a[1]] == 1
    for i in range(8):
        if y[i]:
            m = maps.copy() 
            m[i,a[1]] = 0
            k = find(m, (i, a[1]))
            mm,nn = sorted([a[0], i])
            if summ < 1 + k and  np.count_nonzero(m[mm:nn,a[1]] == 1) == 0:
                summ = 1 + k
        if x[i]:
            m = maps.copy() 
            m[a[0], i] = 0
            k = find(m, (a[0], i))   
            mm,nn = sorted([a[1], i])
            print m[a[0],0:8],mm,nn
            if summ < 1 + k and  np.count_nonzero(m[a[0],mm:nn] == 1) == 0:        
                summ = 1 + k  
    return summ

def berserk_rook(berserker, enemies):
    b = word_to_tuple(berserker)
    maps = np.zeros((8,8))
    for i in enemies:
        maps[word_to_tuple(i)] = 1
    return find(maps,b)
