import re
def check_command(pattern, command):
    return int(re.sub('\D',r'1',re.sub('\d',r'0',command))) == int(bin(pattern)[2:])
