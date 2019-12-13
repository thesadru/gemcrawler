""" find out the position of ">" in a list map """
def heropos(level,herotile=">"):
    selected = [-1,-1] #find hero
    for row in level:
         selected[0] += 1
         selected[1] = -1
         for subtile in row:
             selected[1] += 1
             if subtile == herotile:
                 return selected[:]
       
""" a quick tool to remove duplicate items in a list """
def remdupli(x):
    output = list()
    for i in x:
        if i not in output:
            output.append(i)
    return output


""" an algorith that searches all possible tiles reachable with the vision variable 
    (expand variable is for higher precision) """
def visible(level,position,vision,walls=["#"]):
    import copy
    possible_spaces = []
    for ray in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
        cursor = position[:]
        hitwall = False
        for cycle in range(vision):
            if not hitwall:
                cursor[0] += ray[0]
                cursor[1] += ray[1]
                if level[cursor[0]][cursor[1]] not in walls:
                    cursor_copy = copy.deepcopy(cursor)
                    possible_spaces.append(cursor_copy)
                else:
                    hitwall = True
    
    for rays in [[[-1,1 ],[-1,0 ]],[[-1,1 ],[0 ,1 ]],[[1 ,1 ],[0 ,1 ]],[[1 ,1 ],[1 ,0 ]],
                 [[1 ,-1],[1 ,0 ]],[[1 ,-1],[0 ,-1]],[[-1,-1],[0 ,-1]],[[-1,-1],[-1,0 ]]]:
        cursor = position[:]
        hitwall = False
        for cycle in range(vision//2):
            if not hitwall:
                cursor[0] += rays[0][0]
                cursor[1] += rays[0][1]
                if level[cursor[0]][cursor[1]] not in walls and hitwall == False:
                    cursor_copy = copy.deepcopy(cursor)
                    possible_spaces.append(cursor_copy)
                    cursor[0] += rays[1][0]
                    cursor[1] += rays[1][1]
                    if level[cursor[0]][cursor[1]] not in walls and hitwall == False:
                        cursor_copy = copy.deepcopy(cursor)
                        possible_spaces.append(cursor_copy)
                    else:
                        hitwall = True
                else:
                    hitwall = True
                    
    for i in range(2): #for higher precision, mostly unused | remove for 0.03s faster code
        for seeing in possible_spaces:
            for combine in [[1,1],[1,-1],[-1,1],[-1,-1]]:
                seeing
                if [seeing[0]+combine[0],seeing[1]+combine[1]] in possible_spaces:
                    
                    if level[seeing[0]+combine[0]][seeing[1]] not in walls and [seeing[0]+combine[0],seeing[1]] not in possible_spaces:
                        possible_spaces.append([seeing[0]+combine[0],seeing[1]])
                    if level[seeing[0]][seeing[1]+combine[1]] not in walls and [seeing[0],seeing[1]+combine[1]] not in possible_spaces:
                        possible_spaces.append([seeing[0],seeing[1]+combine[1]])
    
    possible_spaces.remove(position)
    possible_spaces = remdupli(possible_spaces)
    
    return possible_spaces

""" uses an algorith to find out where a player can step """
def movingrange(level,position,steps):
    output = list()
    for i in [[position[0]-1,position[1]],[position[0]-1,position[1]+1],
              [position[0],position[1]+1],[position[0]+1,position[1]+1],
              [position[0]+1,position[1]],[position[0]+1,position[1]-1],
              [position[0],position[1]-1],[position[0]-1,position[1]-1]]:
        if level[i[0]][i[1]] != "#":
            output.append(i)
    movedto = output[:]
    
    for step in range(steps-1):
        movedto = output[:]
        for tile in movedto:
            output = remdupli(output)
            if tile[0]<0 or tile[1]<0 or tile[0]>15 or tile[1]>15:
                movedto.remove(tile)
                output.remove(tile)
            else:
                for direction in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
                    if level[tile[0]+direction[0]][tile[1]+direction[1]] != "#" and []==[
                  ]and level[tile[0]][tile[1]] != "#" and []==[
                  ]and [tile[0]+direction[0],tile[1]+direction[1]] not in movedto:
                        output.append([tile[0]+direction[0],tile[1]+direction[1]])
        
    
    output = remdupli(output)
    try:
        output.remove(position)
    except:
        pass
        
    return output