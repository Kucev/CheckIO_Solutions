def check_pangram(text):
    flag = True
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if text.lower().find(i) == -1:
            flag = False
    return flag
