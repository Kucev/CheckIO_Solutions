def largest_histogram(histogram):
    ans = 0
    for i in range(len(histogram)):
        for k in range(histogram[i] + 1):
            for j in range(i,len(histogram)):
                if histogram[j] < k :
                    break
                if ans < (j - i + 1 ) * k :
                    ans = (j - i + 1 ) * k    
    return ans
