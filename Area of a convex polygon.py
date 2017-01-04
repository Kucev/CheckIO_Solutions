def checkio(data):
    ans = 0
    data.append(data[0])
    for i in range(len(data) - 1):
        ans += (data[i][0] + data[i + 1][0]) * (data[i][1] - data[i + 1][1])
    return abs(ans / 2.0)
