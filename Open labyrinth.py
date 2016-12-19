#Your code here
#You can import some modules or create additional functions


def checkio(maze_map):
    visited=[[0 for col in range(12)] for row in range(12)]
    def func(pos,maze_map,ans):
        visited[pos[0]][pos[1]]=1
        if pos == (10,10):
            return ans
        print ans,pos
        if maze_map[pos[0] + 1][pos[1]] == 0 and visited[pos[0] + 1][pos[1]]==0:
            result=func((pos[0] + 1 , pos[1]),maze_map,ans + 'S')
            if result:
                return result
        if maze_map[pos[0] - 1][pos[1]] == 0 and visited[pos[0] - 1 ][pos[1]]==0:
            result=func((pos[0] - 1 , pos[1]),maze_map,ans + 'N')
            if result:
                return result
        if maze_map[pos[0] ][pos[1] + 1] == 0 and visited[pos[0]][pos[1]+1]==0:
            result=func((pos[0]  , pos[1] + 1),maze_map,ans + 'E')
            if result:
                return result
        if maze_map[pos[0] ][pos[1] - 1] == 0 and visited[pos[0]][pos[1]-1]==0:
            result=func((pos[0]  , pos[1] - 1),maze_map,ans + 'W')
            if result:
                return result
        return ''
        
    return func((1, 1),maze_map,'')
