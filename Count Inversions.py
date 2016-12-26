def count_inversion(sequence):
    count = 0
    for ii,i in enumerate(sequence):
        count += sum(x > i for x in sequence[:ii])
    return count
