def checkio(first, second):
    ans = []
    second = second.split(',')
    for word in first.split(','):
        if word in second :
            ans.append(word)
    ans.sort()
    return ','.join(ans)
