def is_family(a):
    # first step. Transform graph
    global flag
    flag = True
    d = {}
    k = 0
    for i in a:
        if i[0] not in d:
            d.update({i[0]:k})
            k += 1
        if i[1] not in d:
            d.update({i[1]:k})
            k += 1
    # Name to int, for example {'Logan': 0, 'Mike': 1, 'Jack': 2}
    ans = [[] for i in range(len(d))]
    for i in a:
        ans[d[i[0]]].append(d[i[1]])
    # index = number of peak, ans[index] contains conjugated peaks
    Color = [0] * len(d)
    def DFS(start):
        Color[start] = 1
        for u in ans[start]:
            if Color[u] == 0:
                DFS(u)
            elif Color[start] == 1:
                global flag
                flag = False
        Color[start] = 2
    for i in range(0, len(d)):
        if Color[i] == 0:
            DFS(i)
    #bypassing in depth, looking for cycles
    
    Visited = [False] * len(d)
    def DFSS(start):
        Visited[start] = True
        for v in ans[start]:
            if not Visited[v]:
                DFSS(v)

    ncomp = 0
    for i in range(0, len(d)): 
        if not Visited[i]:
            ncomp += 1
            DFSS(i)
    if ncomp != 1:
        flag = False
    #bypassing in depth, consider the connected components in graph
    return flag
