from itertools import permutations, chain
def checkio(crossword, words):  
    f = []
    crossword_t  = zip(*crossword)
    for i in range(0,len(crossword),2):
        for j in range(len(crossword)):
            f.append(crossword[i][j])
    for i in range(0,len(crossword),2):
        for j in range(len(crossword)):
            f.append(crossword_t[i][j])
    w = ''.join(words)
    d = {}
    for i in w:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    e = len(d)
    p = []
    for w in permutations(words):
        p.append(set(zip(f, chain.from_iterable(w))))
    for i in p:
        if len(i)  == e:
            ans = i
            break
    dict_ans = {}
    for i in ans:
        dict_ans[i[0]] = i[1]
    return [[dict_ans[x] if x else ' ' for x in row] for row in crossword]
