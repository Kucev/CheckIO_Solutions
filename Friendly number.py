def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    if number < 0:
        ans = '-'
        number = abs(number)
    else:
        ans = ''
    i = 1
    while number >=  base ** i and  i < len(powers):
        i+=1
    number = float(number) / base ** (i - 1)
    if decimals:
        number = round(number, decimals) 
    else:
        number = int(number)
    ans += '{:.'+ str(decimals) + 'f}' + powers[i - 1] + suffix
    return ans.format(number) 
