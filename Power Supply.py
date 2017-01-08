import itertools  
def power_supply(network, power_plants):
    list_of_cities = list(set(itertools.chain(*network)))
    energy = [0] * len(list_of_cities)
    for i in power_plants:
        energy[list_of_cities.index(i)] = power_plants[i] + 1
    flag = True
    while flag == True:
        flag = False
        for i in network:
            if energy[list_of_cities.index(i[0])] > 1  and energy[list_of_cities.index(i[1])] < energy[list_of_cities.index(i[0])] - 1:
                energy[list_of_cities.index(i[1])] = energy[list_of_cities.index(i[0])] - 1
                flag = True
            if energy[list_of_cities.index(i[1])] > 1 and energy[list_of_cities.index(i[0])] < energy[list_of_cities.index(i[1])] - 1:
                energy[list_of_cities.index(i[0])] = energy[list_of_cities.index(i[1])] - 1
                flag = True
    ans = []
    for i,ii in enumerate(energy):
        if ii == 0:
            ans.append(list_of_cities[i])
    return set(ans)
