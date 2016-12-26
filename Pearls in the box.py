def fun(w,b,k,p,n):
    if n == 0:
        a.append((w / k) * p)
        return
    if w > 0:
        fun(w - 1,b + 1,k,p * (w / k),n - 1)
    if b > 0:
        fun(w + 1,b - 1,k,p * (b / k),n - 1)
  
def checkio(marbles, step):
    global a 
    a = []
    w = float(marbles.count('w'))
    b = float(marbles.count('b'))
    k = len(marbles)
    fun(w,b,k,1.0,step -1) 
    return round(sum(a),2)
