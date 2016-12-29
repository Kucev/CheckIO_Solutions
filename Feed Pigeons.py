def checkio(number):
    count = 1
    k = 1
    while count <= number:
        number -= count
        k += 1
        count += k
    return max(count - k, number)
