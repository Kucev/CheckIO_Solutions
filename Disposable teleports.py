def fun(k,data,path):
    if k == '1' and len(path) > 7:
        ans = True
        for i in range(1,9):
            if not (str(i) in path):
                ans = False
        if ans:
            #print 'eererwerr',path
            return path + '1'
    if len(data) == 0:
        return 
    for  i in data:
        if k == i[0]:
            temp = list(data)
            p = i[1]
            temp.remove(i)
            temp.remove(i[::-1])
            a = fun(p, temp, path + k)
            if a :
                return a
        if k == i[1]:
            temp = list(data)
            p = i[0]
            temp.remove(i)
            temp.remove(i[::-1])
            a = fun(p, temp, path + k)
            if a :
                return a

def checkio(teleports_string):
    t = teleports_string.split(',')
    tt =[]
    for i in t:
        tt.append(i[::-1])
    t.extend(tt)
    return fun('1',t,'')
