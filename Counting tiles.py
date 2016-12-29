import math
def checkio(radius):
    solid = 0
    partial = 0
    for i in range(int(math.ceil(radius))):
        for j in range(int(math.ceil(radius))):
            if i * i + j * j < radius * radius:
                if (i + 1) * (i + 1) + (j + 1) * (j + 1) < radius * radius:
                    solid += 1
                else:
                    partial += 1
    return [4 * solid, 4 * partial]
