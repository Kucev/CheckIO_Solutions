import re
alf = "ADFGVX"
def encode(message, secret_alphabet, keyword):
    message = re.sub(r'\W','', message).lower()
    ans = ''
    for k in message:
        n = secret_alphabet.find(k)
        i = n / 6
        j = n % 6
        ans = ans + alf[i] + alf[j]
    while re.search(r'([a-z])(.*)\1', keyword):
        keyword= re.sub(r'([a-z])(.*)\1', r'\1\2', keyword)
    array = []
    print ans
    for ii,i in enumerate(keyword):
        a = ''
        for j in range(len(ans) // (len(keyword) - 1 )  + 1):
            if (j * len(keyword) + ii) < len(ans):
                a += ans[j * len(keyword) + ii]
        array.append([i,a])
    array.sort()
    code = ''
    for i in range(len(array)):
        code += array[i][1]
    return code
        
def decode(message, secret_alphabet, keyword):
    while re.search(r'([a-z])(.*)\1', keyword):
        keyword= re.sub(r'([a-z])(.*)\1', r'\1\2', keyword)
    key = list(keyword)
    key.sort()
    t = []
    k = (len(message) // len(keyword)) + 1
    for i in range(len(keyword)):
        if ((k - 1)  * len(keyword) + i) < len(message):
            t.append(k)
        else:
            t.append(k - 1)
    a = zip(list(keyword),t)  
    a.sort()
    array = []
    p = 0
    for i in a:
        array.append([i[0],message[p:p + i[1]]])
        p += i[1]
    array = dict(array)
    text = ''
    for i in keyword :
        text = text + array[i]
    p = 0
    new_text = ''
    for i in range(len(text)):
        k = i // len(t)
        new_text = new_text + text[(p + k)  % len(text)] 
        p += t[i % len(t)]
    ans = ''
    for i in range(len(new_text) / 2):
        ifirst = alf.find(new_text[2 * i])
        isecond = alf.find(new_text[2 * i + 1])
        ans = ans + secret_alphabet[ifirst * 6 + isecond] 
    return ans
