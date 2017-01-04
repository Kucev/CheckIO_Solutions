#full bust
import numpy as np
def checkio(landing_map):
    maps = np.zeros((len(landing_map),len(landing_map[0])),dtype=np.int)
    for i in range(len(landing_map)):
        for j in range(len(landing_map[0])):
            if not (landing_map[i][j] == 'S' or landing_map[i][j] == 'G'):
                maps[i,j] = 1 
    maxx = 0
    for i in range(len(landing_map)):
        for j in range(len(landing_map[0])):
            for ii in range(i + 1,len(landing_map) + 1):
                for jj in range(j + 1,len(landing_map[0]) + 1):
                    if (ii - i) * (jj - j) > maxx and not maps[i:ii,j:jj].any():
                        maxx = (ii - i) * (jj - j)
    return maxx
