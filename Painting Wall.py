def checkio(num, data):
    p = []
    for k, i in enumerate(data):
        p.append(i)
        p.sort()
        j = 0
        for l in range(len(p) - 1):
            if p[j][1] >= p[j + 1][0]:
                p[j][1] = max(p[j][1], p[j + 1][1])
                p.pop(j + 1)
            else:
                j += 1
        if reduce(lambda res, l:  res + l[1] - l[0] + 1, p, 0) >= num:
            return k + 1
    return -1
