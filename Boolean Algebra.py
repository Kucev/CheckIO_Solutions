OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
def boolean(x, y, operation):
    op = OPERATION_NAMES.index(operation)
    if op == 0: return x & y
    elif op == 1: return x | y
    elif op == 2: return x <= y
    elif op == 3: return x ^ y
    elif op == 4: return x == y
