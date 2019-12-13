""" an AI (A Ifstatement) that lets enemies move automaticly """
def enemymove(level,heropos,walls=["#","<","+","x"]):
    import copy
    from gc_pathfind import pathfind
    
    
    heropos = gc.heropos(level)
                 
    current_enemies = [] #find enemies
    selected = [-1,-1]
    for row in level:
         selected[0] += 1
         selected[1] = -1
         for subtile in row:
             selected[1] += 1
             if type(subtile) != str:
                current_enemies.append([subtile,selected[:]][:])
    
    turns = []
    for enemy_list in current_enemies: #create path for enemies
        enemyname = enemy_list[0]
        enemypos  = enemy_list[1]
        full_path = pathfind(enemypos,heropos,level,walls)
        if full_path != False and full_path != None: #test for a valid pathfind
            for i in range(enemyname.range):
                try:
                    full_path.pop() #remove landing on hero
                except:
                    pass
            while len(full_path) > enemyname.speed+1: #check if the entity can go the entire path
                try:
                    full_path.pop() #remove landing on hero
                except:
                    pass
        try:
            full_path[1] #check if path is bigger than 1
        except:
            full_path = [tuple(enemypos)] #else copy path
        staying_at = full_path[-1]  #remember last move for copying
        while len(full_path) < 6: #check if path is too short
            full_path.append(staying_at[:]) #make path longer
        turns.append(full_path[:]) #finally append path
        
    
    completelevel = []
    level_copy = copy.deepcopy(level) #copy the level for in-cycle mutation
    for cycle in range(5): #start cycle for all steps (animation)
        for current in current_enemies: #go for each entity one by one
            turn = turns[current_enemies.index(current)] #take the turn linked with entity
            if type(level_copy[turn[cycle+1][0]] [turn[cycle+1][1]]) == str: #check if stepping on a block
                level_copy = copy.deepcopy(level_copy)
                level_copy[turn[cycle  ][0]][turn[cycle  ][1]] = " "        #delete entity
                level_copy[turn[cycle+1][0]][turn[cycle+1][1]] = current[0] #create entity
                level_copy[turn[cycle  ][0]][turn[cycle  ][1]],level_copy[turn[cycle+1][0]][turn[cycle+1][1]] = " ",current[0]
            else:
                turn = [turn[cycle+1],turn[cycle+1],turn[cycle+1],turn[cycle+1],turn[cycle+1]] #stop if the path if blocked
        completelevel.append(level_copy) #append the new level
        
    return completelevel #RETURN
    

""" lets the hero do his moves with player input"""
def heromove(level,heropos,walkreach,walkto,walls=["#"]):
    print(walkreach)
    if walkto in walkreach and level[walkto[0]][walkto[1]] not in walls and type(level[walkto[0]][walkto[1]]) in [str,int]:
        level[heropos[0]][heropos[1]] = " "
        level[walkto[0]][walkto[1]] = ">"
        
    else:
        return False
    
    return level

# =============================================================================
    
    
import gc_generate as gen  
from time import sleep  
from copy import deepcopy as copy
import gc_tools as gc
from gc_character import *

level = gen.level(enemies)
heropos = gc.heropos(level)
count = 5
for x in enemymove(level,heropos):
    print("  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5  ")
    for i in x:
        if count < 9:
            count += 1
        else:
            count = 0
        print(count,end=" ")
        for ii in i:
            if type(ii) == str:
                print(ii,end=" ")
            else:
                print(str(ii.id)[0],end=" ")
        print(count)
    print("  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5  ")
    print("\n")
    
movingrange = gc.movingrange(level,heropos,5)

pos_x = int(input("height: "))
pos_y = int(input("lenght: "))
level_copy = copy(level)
frick = True
while frick:
    pos_x = int(input("height: "))
    pos_y = int(input("lenght: "))
    new_level = heromove(level,heropos,movingrange,[pos_x,pos_y])
    frick = True if new_level==False else False
level = copy(new_level)
if level==level_copy:
    raise ValueError("you didn't move")
count = -1
print("  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5  ")
for i in x:
    if count < 9:
        count += 1
    else:
        count = 0
    print(count,end=" ")
    for ii in i:
        if type(ii) == str:
            print(ii,end=" ")
        else:
            print(str(ii.id)[0],end=" ")
    print(count)
print("  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5  ")
print("\n")