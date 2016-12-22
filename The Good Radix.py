def checkio(number):
    for k in range(int(max(number),36)+1,37):
        if int(number,k) % (k - 1) == 0:
            return k
    return 0
