def checkio(number):
    ans = []
    for i in range(9,1,-1):
        while number > 1 and number % i == 0:
            number //= i
            ans.append(str(i))
    ans.sort()
    print ans
    return int(''.join(ans))  if number == 1 else 0
