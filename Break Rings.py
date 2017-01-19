import itertools
def break_rings(rings):
    m = len(rings)
    for i in itertools.product(*rings):
        if m > len(set(i)):
            m = len(set(i))
    return m
