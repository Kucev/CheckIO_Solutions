def checkio(numbers):
    x = 0
    y = 0
    for i in numbers:
        y, x = i + max(x, y), y
    return max(x, y)
