import math
def simple_areas(*args):
    if len(args) == 1:
        return args[0] * args[0] * math.pi / 4.0
    elif len(args) == 2:
        return args[0] * args[1]
    p = (args[0] + args[1] + args[2]) / 2.0
    return math.sqrt(p * (p - args[0]) * (p - args[1]) * (p - args[2]))
