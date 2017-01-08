#this is my first completed class on a kite

import itertools 
class Friends:
    def __init__(self, connections):
        self.connections = []
        for i in connections:
            if i not in self.connections:
                self.connections.append(i)
                
    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True
    
    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False
    
    def names(self):
        return set(itertools.chain(*self.connections))
        
    def connected(self, name):
        friends = []
        for i in self.connections:
            i_list = list(i)
            if name == i_list[0]:
                if i_list[1] not in friends:
                    friends.append(i_list[1])
            elif name == i_list[1]:
                if i_list[0] not in friends:
                    friends.append(i_list[0])
        return set(friends)
