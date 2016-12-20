s = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
g = ['e','y','u','i','o','a']
def translate(phrase):
    ans = ''
    i = 0
    while i < len(phrase):
        if phrase[i] in s :
            ans += phrase[i]
            i+=1
        elif phrase[i] in g:
            ans += phrase[i]
            i+=2
        else:
            ans += phrase[i]
        i+=1
    return ans
