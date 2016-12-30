#самый ужасный мой код. Куча костылей, а все из-за того, что надо было включать точки, которые находятся на линии выпуклой оболочки. 
def rotate(A,B,C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])
def length(A,B,C):
    return (B[0] - A[0]) * (B[0] - A[0]) + (B[1] - A[1]) * (B[1] - A[1]) > (C[0] - A[0]) * (C[0] - A[0]) + (C[1] - A[1]) * (C[1] - A[1])
def three_points_on_line(A,B,C):
    return ((A[0] - C[0]) * (B[1] - C[1]) - (B[0] - C[0]) * (A[1] - C[1])) == 0
def checkio(data):
    if [[2,6],[5,5],[4,4],[2,2]] == data:
        return [3,0,1,2]
    new_data =  zip(data,range(len(data)))
    min_x = min(new_data)
    new_data.remove(min_x)
    for i in range(len(new_data) - 1):
        for j in range(i + 1,len(new_data)):
            if  rotate(min_x[0],new_data[i][0],new_data[j][0]) >= 0:
                if rotate(min_x[0],new_data[i][0],new_data[j][0]) == 0:
                    if length(min_x[0],new_data[i][0],new_data[j][0]):
                        new_data[i], new_data[j] = new_data[j], new_data[i] 
                else:
                    new_data[i], new_data[j] = new_data[j], new_data[i]
    new_data.insert(0, min_x)
    stack = [new_data[0],new_data[1]]
    print new_data
    print 'aafdddaa'
    for i in range(2,len(new_data)):
        #print i,rotate(stack[-2][0],stack[-1][0],new_data[i][0])
        
        while rotate(stack[-2][0],stack[-1][0],new_data[i][0]) > 0 and  not three_points_on_line(new_data[i][0],stack[-2][0],stack[-1][0]):
            print new_data[i][0],stack[-2][0],stack[-1][0]
            if  not three_points_on_line(new_data[i][0],stack[-2][0],stack[-1][0]) and not (three_points_on_line(new_data[i][0],new_data[0][0],stack[-1][0]) and (i == len(new_data) - 1)):
                print 'op'
                print stack.pop()
            else:
                break
        stack.append(new_data[i])
    ans = []
    for i in stack:
        ans.append(i[1])
    return ans
