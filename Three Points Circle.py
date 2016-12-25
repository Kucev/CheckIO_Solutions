import re
import math
def checkio(data):
    s = re.sub('[\(\)]','',data).split(',')
    x1 = float(s[0])
    x2 = float(s[2])
    x3 = float(s[4])
    y1 = float(s[1])
    y2 = float(s[3])
    y3 = float(s[5])
    d = 2.0 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2)
         * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
    y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2)
         * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
    r = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    return "(x-%g)^2+(y-%g)^2=%g^2" %(round(x,2), round(y,2), round(r,2))
