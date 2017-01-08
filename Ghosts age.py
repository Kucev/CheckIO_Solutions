def checkio(opacity):
    x = 1
    y = 1
    z = 0
    while opacity != 10000:
        z += 1
        if z != y:
            opacity -= 1
        else:
            opacity += y
            x, y = y, x + y            
    return z
