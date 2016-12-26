import datetime
def broken_clock(starting_time, wrong_time, error_description):
    first = datetime.datetime.strptime(starting_time, '%H:%M:%S')
    second = datetime.datetime.strptime(wrong_time, '%H:%M:%S')
    dic = {'second':1, 'minute':60, 'hour':3600, 'seconds':1, 'minutes':60, 'hours':3600}
    s1 = int(error_description.split()[0]) * dic[error_description.split()[1]]
    s2 = int(error_description.split()[3]) * dic[error_description.split()[4]]
    return (first + (second - first) * s2 / (s1 + s2)).strftime('%X')
