def enemymove(level,walls=["#","<","+","x"]):
    from gc_pathfind import pathfind
    
    
    selected = [-1,-1] #find hero
    for row in level:
         selected[0] += 1
         selected[1] = -1
         for subtile in row:
             selected[1] += 1
             if subtile == ">":
                 heropos = selected[:]
                 
    current_enemies = [] #find enemies
    selected = [-1,-1]
    for row in level:
         selected[0] += 1
         selected[1] = -1
         for subtile in row:
             selected[1] += 1
             if type(subtile) != str:
                current_enemies.append([subtile,selected[:]][:])
    print(current_enemies)
    
    turns = []
    for enemy_list in current_enemies: #create path for enemies
        enemyname = enemy_list[0]
        enemypos  = enemy_list[1]
        print(enemypos,"->",heropos," | ",enemyname.range,"x",enemyname.speed) #some info
        full_path = pathfind(enemypos,heropos,level,walls)
        print(full_path,"\n")
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
        
    
    for i in turns:
        print(i)
    
    completelevel = []
    for cycle in range(5): #start cycle for all steps (animation)
        for current in current_enemies: #go for each entity one by one
            turn = turns[current_enemies.index(current)] #take the turn linked with entity
            if type(level[turn[cycle+1][0]] [turn[cycle+1][1]]) == str: #check if stepping on a block
                level[turn[cycle  ][0]] [turn[cycle  ][1]] = " "        #delete entity
                level[turn[cycle+1][0]] [turn[cycle+1][1]] = current[0] #create entity
                print([turn[cycle  ][0]],[turn[cycle  ][1]],"  ->",
                      [turn[cycle+1][0]],[turn[cycle+1][1]])
            else:
                turn = [turn[cycle+1],turn[cycle+1],turn[cycle+1],turn[cycle+1],turn[cycle+1]] #stop if the path if blocked
        print()
        completelevel.append(level[:]) #append thenew level
    
        
    if completelevel[0]==completelevel[-1]: #raise exception if the code is bad (idk just it does)
        class Failed(Exception):
            pass
        raise Failed("first and last output are the same")
    return completelevel #RETURN

from gc_generate import level as gen #generation of levels
from gc_character import *
output = enemymove(gen(enemies))
print("\n\n")
for z in output:
    for x in z:
        for y in x:
            if type(y) == str:
                print(y,end="")
            else:
                print(list(str(y.id))[0],end="")
            print(" ",end="")
        print("")
    print("\n")


# =============================================================================
# PLEASE READ:
#     code has an error that was found but not resolved
#     in line 68 appending just copies the first item in list instead of apending the required list
#     this makes the level always stay the same
#     for faster checking, an excpetion is raised if the level is same
#     if you want to see the print, comment the raise command at line 74
#     there is no need to chec the pathfinding algorithm, as there is no error there
#         
#     there are 3 imported files: gc_generate, gc_characters and gc_pathfind
#     gc_generate = file that creates levels
#     gc_characters = database of characters, enemies and bosses
#     gc_pathfind = A* pathfinding algorithm
#     
#     if you can fix this, please tell me
# =============================================================================