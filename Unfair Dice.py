import itertools

def check(enemy_die,ans):
    s = 0
    for i in ans:
        ss = 0
        for j in enemy_die:
            if i > j:
                ss += 1
            elif i < j:
                ss -= 1
        s += ss
    return s

def winning_die(enemy_die):
    l = len(enemy_die)
    summ = sum(enemy_die)
    m = max(enemy_die)

    for i in itertools.combinations_with_replacement(range(1,m * 2),l) :
        if sum(i) == summ:
            if check(enemy_die,i) > 0:
                return i
    return []
