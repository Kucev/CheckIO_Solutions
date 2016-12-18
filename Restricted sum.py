s = 0
def checkio(data):
    global s 
    s = 0
    def f(a):
        global s 
        s = a + s 
        return s
    map(f, data)
    return s
