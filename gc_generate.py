def level(enemies,amount=12,w ="#",g =" ",s =">",e ="<",k ="+",c = "x"):
          #w #wall
          #g #ground
          #s #hero position
          #f #exit
          #k #key
          #c #chest
    #w = "⬛"
    #g = "⬜"
    
    def tileset(coordinates,tileto): #coordinates = [[1,1],[1,2],[2,1],[2,2]] tileto = [w,w,w,w]
        changing_tile = -1
        for change in coordinates:
            changing_tile += 1
            level[change[0]][change[1]] = tileto[changing_tile]
            
    def analyse(coordinates): #coordinates = [[1,1],[1,2],[2,1],[2,2]]
        outputing = [0,0,0,0]
        analysing_tile = -1
        for analysing in coordinates:
            analysing_tile += 1
            outputing[analysing_tile] = level[analysing[0]][analysing[1]]
        if outputing == [g,g,g,g]:
            return True
        else:
            return False
    
    import random
    if type(enemies) == list: # creating random seed
        enemyseed = ""
        for i in enemies:
            try:
                enemyseed += i
            except:
                enemyseed += str(i.id)+","
        seed = str(int(random.random()*10**16))+"|"+enemyseed
    else: # using given input as seed
        seed = enemies
        
    random.seed(seed) # setting the seed
    # random generation
    walls = [random.choice([0,1]),  # 0 is middle
             random.choice([0,1]),
             random.choice([0,1]),
             random.choice([0,1])]
    
    
    miniwalls = [0,0,0,0]
    deadends = [0,0,0,0]
    wall_thin = [False,False,False,False]
    
    for i in range(4): # randomly choose if you can walk by the center or by the wall
        if   walls[i-1] == 0 and walls[i] == 0: #  randomly choose deadend
            miniwalls[i] = random.choice([0,1,2,3]) # urdl,lurd,dlur,rdlu
            if   miniwalls[i] == 0:
                deadends[i] = 0
            elif miniwalls[i] == 1:
                deadends[i] = 2
            elif miniwalls[i] == 2:
                deadends[i] = 2
            elif miniwalls[i] == 3:
                deadends[i] = 0
                
        elif walls[i-1] == 0 and walls[i] == 1:
            miniwalls[i] = random.choice([1,3]) #rl,du,lr,ud
            if   miniwalls[i] == 1:
                deadends[i] = 1
            elif miniwalls[i] == 3:
                deadends[i] = 0
            
        elif walls[i-1] == 1 and walls[i] == 0:
            miniwalls[i] = random.choice([0,2]) #ud,rl,du,lr
            if   miniwalls[i] == 0:
                deadends[i] = 0
            elif miniwalls[i] == 2:
                deadends[i] = 3
            
        elif walls[i-1] == 1 and walls[i] == 1:
            miniwalls[i] = random.choice([1,2]) #rd,dl,ul,ur
            if   miniwalls[i] == 1:
                deadends[i] = 1
            elif miniwalls[i] == 2:
                deadends[i] = 3
        
    freecorners  = [0,1,2,3]
    for i in range(4): # easier way to find a deadend
        freecorners[i] = [i,abs(deadends[i]+i)%4]
    
    corner_start = random.choice(freecorners) # choose start,end,key and chest
    freecorners.remove(corner_start)
    corner_end   = random.choice(freecorners)
    freecorners.remove(corner_end)
    corner_key   = random.choice(freecorners)
    freecorners.remove(corner_key)
    corner_chest = random.choice(freecorners)
    freecorners.remove(corner_chest)
        
    if walls[0] == 1: # thin out the walls in middle
        wall_thin[0] = random.choice([0,1])
    if walls[1] == 1:
        wall_thin[1] = random.choice([0,1])
    if walls[2] == 1:
        wall_thin[2] = random.choice([0,1])
    if walls[3] == 1:
        wall_thin[3] = random.choice([0,1])
        
    level = [ # level template
        [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
        [w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
        [w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
        [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
        [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
        [w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
        [w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
        [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
        [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
        [w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
        [w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
        [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
        [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
        [w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
        [w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
        [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
    ]
    
    if walls[0] == 0: # set the basic middle walls
        tileset([[5 ,7 ],[5 ,8 ],[6 ,7 ],[6 ,8 ]],[w,w,w,w])
    else:
        tileset([[1 ,7 ],[1 ,8 ],[2 ,7 ],[2 ,8 ]],[w,w,w,w])
    if walls[1] == 0:
        tileset([[7 ,9 ],[7 ,10],[8 ,9 ],[8 ,10]],[w,w,w,w])
    else:
        tileset([[7 ,13],[7 ,14],[8 ,13],[8 ,14]],[w,w,w,w])
    if walls[2] == 0:
        tileset([[9 ,7 ],[9 ,8 ],[10,7 ],[10,8 ]],[w,w,w,w])
    else:
        tileset([[13,7 ],[13,8 ],[14,7 ],[14,8 ]],[w,w,w,w])
    if walls[3] == 0:
        tileset([[7 ,5 ],[7 ,6 ],[8 ,5 ],[8 ,6 ]],[w,w,w,w])
    else:
        tileset([[7 ,1 ],[7 ,2 ],[8 ,1 ],[8 ,2 ]],[w,w,w,w])
        
    #===========================================================================
        
    if   miniwalls[0] == 0: # set up rest of the walls
        if   deadends[0] == 0:
            tileset([[1 ,4 ],[2 ,4 ],[3 ,3 ],[4 ,3 ]],[w,w,g,g])
        elif deadends[0] == 1:
            tileset([[1 ,3 ],[2 ,3 ],[3 ,4 ],[4 ,4 ]],[w,w,g,g])
    elif miniwalls[0] == 1:
        if   deadends[0] == 1:
            tileset([[4 ,5 ],[4 ,6 ],[3 ,3 ],[3 ,4 ]],[w,w,g,g])
        elif deadends[0] == 2:
            tileset([[3 ,5 ],[3 ,6 ],[4 ,3 ],[4 ,4 ]],[w,w,g,g])
    elif miniwalls[0] == 2:
        if   deadends[0] == 2:
            tileset([[5 ,3 ],[6 ,3 ],[3 ,4 ],[4 ,4 ]],[w,w,g,g])
        elif deadends[0] == 3:
            tileset([[5 ,4 ],[6 ,4 ],[3 ,3 ],[4, 3 ]],[w,w,g,g])
    elif miniwalls[0] == 3:
        if   deadends[0] == 3:
            tileset([[4 ,1 ],[4 ,2 ],[3 ,3 ],[3 ,4 ]],[w,w,g,g])
        elif deadends[0] == 0:
            tileset([[3 ,1 ],[3 ,2 ],[4 ,3 ],[4 ,4 ]],[w,w,g,g])
    
    if   miniwalls[1] == 0:
        if   deadends[1] == 0:
            tileset([[4 ,13],[4 ,14],[3 ,11],[3 ,12]],[w,w,g,g])
        elif deadends[1] == 1:
            tileset([[3 ,13],[3 ,14],[4 ,11],[4 ,12]],[w,w,g,g])
    elif miniwalls[1] == 1:
        if   deadends[1] == 1:
            tileset([[5 ,11],[6 ,11],[3 ,12],[4 ,12]],[w,w,g,g])
        elif deadends[1] == 2:
            tileset([[5 ,12],[6 ,12],[3 ,11],[4 ,11]],[w,w,g,g])
    elif miniwalls[1] == 2:
        if   deadends[1] == 2:
            tileset([[3 ,9 ],[3 ,10],[4 ,11],[4 ,12]],[w,w,g,g])
        elif deadends[1] == 3:
            tileset([[4 ,9 ],[4 ,10],[3 ,11],[3 ,12]],[w,w,g,g])
    elif miniwalls[1] == 3:
        if   deadends[1] == 3:
            tileset([[1 ,12],[2 ,12],[3 ,11],[4 ,11]],[w,w,g,g])
        elif deadends[1] == 0:
            tileset([[1 ,11],[2 ,11],[3 ,12],[3 ,12]],[w,w,g,g])
    
    if   miniwalls[2] == 0:
        if   deadends[2] == 0:
            tileset([[13,11],[14,11],[11,12],[12,12]],[w,w,g,g])
        elif deadends[2] == 1:
            tileset([[13,11],[13,12],[14,11],[14,12]],[w,w,g,g])
    elif miniwalls[2] == 1:
        if   deadends[2] == 1:
            tileset([[11,9 ],[11,10],[12,11],[12,12]],[w,w,g,g])
        elif deadends[2] == 2:
            tileset([[13,12],[14,12],[11,11],[12,11]],[w,w,g,g])
    elif miniwalls[2] == 2:
        if   deadends[2] == 2:
            tileset([[12,9 ],[12,10],[11,11],[11,12]],[w,w,g,g])
        elif deadends[2] == 3:
            tileset([[9 ,11],[10,11],[11,12],[12,12]],[w,w,g,g])
    elif miniwalls[2] == 3:
        if   deadends[2] == 3:
            tileset([[12,13],[12,14],[11,11],[11,12]],[w,w,g,g])
        elif deadends[2] == 0:
            tileset([[11,13],[11,14],[12,11],[12,12]],[w,w,g,g])
    
    if   miniwalls[3] == 0:
        if   deadends[3] == 0:
            tileset([[11,1 ],[11,2 ],[12,3 ],[12,4 ]],[w,w,g,g])
        elif deadends[3] == 1:
            tileset([[12,1 ],[12,2 ],[11,3 ],[11,4 ]],[w,w,g,g])
    elif miniwalls[3] == 1:
        if   deadends[3] == 1:
            tileset([[9 ,4 ],[10,4 ],[11,3 ],[12,3 ]],[w,w,g,g])
        elif deadends[3] == 2:
            tileset([[9 ,3 ],[10,3 ],[11,4 ],[12,4 ]],[w,w,g,g])
    elif miniwalls[3] == 2:
        if   deadends[3] == 2:
            tileset([[12,5 ],[12,6 ],[11,3 ],[11,4 ]],[w,w,g,g])
        elif deadends[3] == 3:
            tileset([[11,5 ],[11,6 ],[12,3 ],[12,4 ]],[w,w,g,g])
    elif miniwalls[3] == 3:
        if   deadends[3] == 3:
            tileset([[13,3 ],[14,3 ],[11,4 ],[12,4 ]],[w,w,g,g])
        elif deadends[3] == 0:
            tileset([[13,4 ],[14,4 ],[11,3 ],[12,3 ]],[w,w,g,g])
    
    #===========================================================================
    
    if walls == [1,1,1,1]: # delete middle block if there's no use
        tileset([[7 ,7 ],[7 ,8 ],[8 ,7 ],[8 ,8 ]] , [g,g,g,g])
    else:
        
    #===========================================================================
        
        if corner_start==0 or corner_start==2: # thin out the walls
            if   walls[0]==0 and miniwalls[0]!=1:
                tileset([[3 ,7 ],[4 ,7 ],[5 ,7 ],[6 ,7 ]],[g,g,g,g])
            elif walls[0]==0 and miniwalls[1]!=2:
                tileset([[3 ,8 ],[4 ,8 ],[5 ,8 ],[6 ,8 ]],[g,g,g,g])
            if   walls[1]==0 and miniwalls[2]!=2:
                tileset([[8 ,9 ],[8 ,10],[8 ,11],[8 ,12]],[g,g,g,g])
            elif walls[1]==0 and miniwalls[1]!=1:
                tileset([[7 ,9 ],[7 ,10],[7 ,11],[7 ,12]],[g,g,g,g])
            if   walls[2]==0 and miniwalls[2]!=1:
                tileset([[9 ,8 ],[10,8 ],[11,8 ],[12,8 ]],[g,g,g,g])
            elif walls[2]==0 and miniwalls[3]!=2:
                tileset([[9 ,7 ],[10,7 ],[11,7 ],[12,7 ]],[g,g,g,g])
            if   walls[3]==0 and miniwalls[0]!=2:
                tileset([[7 ,3 ],[7 ,4 ],[7 ,5 ],[7 ,6 ]],[g,g,g,g])
            elif walls[3]==0 and miniwalls[3]!=1:
                tileset([[8 ,3 ],[8 ,4 ],[8 ,5 ],[8 ,6 ]],[g,g,g,g])
                
        else:
            if   walls[0]==0 and miniwalls[1]!=2:
                tileset([[3 ,8 ],[4 ,8 ],[5 ,8 ],[6 ,8 ]],[g,g,g,g])
            elif walls[0]==0 and miniwalls[0]!=1:
                tileset([[3 ,7 ],[4 ,7 ],[5 ,7 ],[6 ,7 ]],[g,g,g,g])
            if   walls[1]==0 and miniwalls[1]!=1:
                tileset([[7 ,9 ],[7 ,10],[7 ,11],[7 ,12]],[g,g,g,g])
            elif walls[1]==0 and miniwalls[2]!=2:
                tileset([[8 ,9 ],[8 ,10],[8 ,11],[8 ,12]],[g,g,g,g])
            if   walls[2]==0 and miniwalls[3]!=2:
                tileset([[9 ,7 ],[10,7 ],[11,7 ],[12,7 ]],[g,g,g,g])
            elif walls[2]==0 and miniwalls[2]!=1:
                tileset([[9 ,8 ],[10,8 ],[11,8 ],[12,8 ]],[g,g,g,g])
            if   walls[3]==0 and miniwalls[3]!=1:
                tileset([[8 ,3 ],[8 ,4 ],[8 ,5 ],[8 ,6 ]],[g,g,g,g])
            elif walls[3]==0 and miniwalls[0]!=2:
                tileset([[7 ,3 ],[7 ,4 ],[7 ,5 ],[7 ,6 ]],[g,g,g,g])
    
    #===========================================================================
    
    if   wall_thin[0] == 0: # thin out the rest of the walls
        tileset([[1 ,7 ],[2 ,7 ]],[g,g,g])
        if miniwalls[0] != 1:
            tileset([[4 ,7 ],[3 ,7 ]],[g,g])
    elif wall_thin[0] == 1:
        tileset([[1 ,8 ],[2 ,8 ]],[g,g,g])
        if miniwalls[1] != 2:
            tileset([[4 ,8 ],[3 ,8 ]],[g,g])
    if   wall_thin[1] == 0:
        tileset([[7 ,13],[7 ,14]],[g,g,g])
        if miniwalls[1] != 1:
            tileset([[7 ,12],[7 ,11]],[g,g])
    elif wall_thin[1] == 1:
        tileset([[8 ,13],[8 ,14]],[g,g,g])
        if miniwalls[2] != 2:
            tileset([[8 ,12],[8 ,11]],[g,g])
    if   wall_thin[2] == 0:
        tileset([[13,8 ],[14,8 ]],[g,g,g])
        if miniwalls[2] != 1:
            tileset([[12,8 ],[11,8 ]],[g,g])
    elif wall_thin[2] == 1:
        tileset([[13,7 ],[14,7 ]],[g,g,g])
        if miniwalls[3] != 2:
            tileset([[12,7 ],[11,7 ]],[g,g])
    if   wall_thin[3] == 0:
        tileset([[8 ,1 ],[8 ,2 ]],[g,g,g])
        if miniwalls[3] != 1:
            tileset([[8 ,4 ],[8 ,3 ]],[g,g])
    elif wall_thin[3] == 1:
        tileset([[7 ,1 ],[7 ,2 ]],[g,g,g])
        if miniwalls[0] != 2:
            tileset([[7 ,4 ],[7 ,3 ]],[g,g])
    
    
    #===========================================================================
    
    if analyse([[7 ,6 ],[6 ,7 ],[6 ,8 ],[7 ,9 ]]): # cut the corners in middle
        tileset([[7 ,7 ],[7 ,8 ]],[g,g])
        
    if analyse([[6 ,8 ],[7 ,9 ],[8 ,9 ],[9 ,8 ]]):
        tileset([[7 ,8 ],[8 ,8 ]],[g,g])
        
    if analyse([[8 ,9 ],[9 ,8 ],[9 ,7 ],[8 ,6 ]]):
        tileset([[8 ,8 ],[8 ,7 ]],[g,g])
        
    if analyse([[9 ,7 ],[8 ,6 ],[7 ,6 ],[6 ,7 ]]):
        tileset([[8 ,7 ],[7 ,7 ]],[g,g])
    
    
    #===========================================================================
    
    from gc_tools import remdupli
    from copy import deepcopy as copy
    
    possible_space = []
    banned_tiles = []
    skip = random.choice([True,False])
    for x in range(len(level)): # collect all possible spaces
        for y in range(len(level[x])):
            if level[x][y] == g and [x,y] not in banned_tiles and skip==False:
                pos_x = copy(x)
                pos_y = copy(y)
                possible_space.append([pos_x,pos_y])
                banned_tiles.extend([
                        [pos_x  ,pos_y+1],
                        [pos_x+1,pos_y  ],
                ])
                if random.choice([True,False]):
                    banned_tiles.extend([
                            [pos_x+1,pos_y+1],
                            [pos_x+1,pos_y-1],
                    ])
                remdupli(banned_tiles)
            else:
                skip = False
    
    for i in range(amount): # randomly replace the places with enemies
        replace = random.choice(possible_space)
        level[replace[0]][replace[1]] = random.choice(enemies)
        possible_space.remove(replace)
            
    #===========================================================================

    special_tiles = [corner_start,corner_end,corner_key,corner_chest]
    for i in special_tiles: # replace special tiles position with desired tiles
        working_with = []
        if   i[0] == 0:
            for x in level[0:8]:
                working_with += [x[0:8]]
                offset_x = 0
                offset_y = 0
        elif i[0] == 1:
            for x in level[0:8]:
                working_with += [x[8:16]]
                offset_x = 0
                offset_y = 1
        elif i[0] == 2:
            for x in level[8:16]:
                working_with += [x[8:16]]
                offset_x = 1
                offset_y = 1
        elif i[0] == 3:
            for x in level[8:16]:
                working_with += [x[0:8]]
                offset_x = 1
                offset_y = 0
        special_pos = []
        if   i[1] == 0:
            for x in working_with[0:4]:
                special_pos += [x[0:4]]
                minioffset_x = 0
                minioffset_y = 0
        elif i[1] == 1:
            for x in working_with[0:4]:
                special_pos += [x[4:8]]
                minioffset_x = 0
                minioffset_y = 1
        elif i[1] == 2:
            for x in working_with[4:8]:
                special_pos += [x[4:8]]
                minioffset_x = 1
                minioffset_y = 1
        elif i[1] == 3:
            for x in working_with[4:8]:
                special_pos += [x[0:4]]
                minioffset_x = 1
                minioffset_y = 0
                
        possible_space = []
        counting = [-1,-1]
        for x in special_pos:
            counting[0] += 1
            counting[1] = -1
            for y in x:
                counting[1] += 1
                if y == g:
                    possible_space += [counting[:]]
        final_space = random.choice(possible_space) 
        if   i == corner_start:
            level[final_space[0]+offset_x*8+minioffset_x*4][final_space[1]+offset_y*8+minioffset_y*4] = s
        elif i == corner_end:
            level[final_space[0]+offset_x*8+minioffset_x*4][final_space[1]+offset_y*8+minioffset_y*4] = e
        elif i == corner_key:
            level[final_space[0]+offset_x*8+minioffset_x*4][final_space[1]+offset_y*8+minioffset_y*4] = k
        elif i == corner_chest:
            level[final_space[0]+offset_x*8+minioffset_x*4][final_space[1]+offset_y*8+minioffset_y*4] = c
    
    #===========================================================================
    
    return level

#=============================================================================

def bosslevel(bossid,enemies,
    w="#",g=" ",s=">",e="!",b="X",c="+",n="="):
    #w #wall
    #g #ground
    #s #start
    #e #enemy
    #b #boss
    #c #chest
    #n #summoning point
    
    enemies = list(enemies)
    
    import random
    if type(enemies) == list:
        seed = str(int(random.random()*10**16))
    else:
        try:
            enemies = str(enemies)
            enemies = enemies.split("|",1)
            seed = enemies[0]
            enemies = list(enemies[1])
        except:
            enemies = list(enemies)
            seed = str(int(random.random()*10**16))
            
    random.seed(seed)
    
    bossid = str(bossid)
    if bossid == "0":
        level = [
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
            [w,s,g,g,g,g,g,g,g,g,w,g,g,g,g,w],
            [w,g,g,g,g,g,g,g,g,g,w,e,g,g,e,w],
            [w,g,g,g,g,g,e,g,g,g,w,g,g,g,g,w],
            [w,g,g,g,w,w,w,w,g,g,w,g,g,g,g,w],
            [w,g,g,g,w,c,g,w,g,e,g,g,g,g,w,w],
            [w,g,g,e,w,g,g,g,g,g,g,g,e,w,w,w],
            [w,g,g,g,w,w,g,g,g,g,g,g,g,w,w,w],
            [w,g,g,g,g,g,g,g,g,g,g,g,g,w,w,w],
            [w,g,g,g,g,e,g,g,g,e,w,g,g,g,w,w],
            [w,w,w,w,w,g,g,g,g,w,w,g,e,g,w,w],
            [w,g,e,g,g,g,g,g,g,g,g,g,g,g,g,w],
            [w,g,g,g,g,g,e,g,g,g,e,g,b,g,g,w],
            [w,g,g,g,g,g,w,w,w,g,g,g,g,g,g,w],
            [w,g,e,g,g,w,w,w,w,w,w,g,g,g,g,w],
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
        ]
    elif bossid == "1":
        level = [
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
            [w,s,g,g,g,g,g,g,g,g,w,g,g,g,g,w],
            [w,g,g,g,g,g,g,g,g,g,w,g,g,n,g,w],
            [w,g,g,g,g,g,g,e,g,g,w,e,g,g,g,w],
            [w,g,g,g,g,g,w,w,g,g,g,g,g,g,g,w],
            [w,g,g,g,g,g,g,w,g,g,g,g,w,w,w,w],
            [w,g,g,g,w,g,n,w,e,g,g,g,g,e,g,w],
            [w,g,g,e,w,w,w,w,w,w,w,g,g,g,g,w],
            [w,g,g,g,g,g,e,w,b,g,w,g,w,e,g,w],
            [w,g,g,g,g,g,g,w,g,g,g,g,w,g,g,w],
            [w,w,w,w,g,g,g,w,w,g,g,g,w,g,g,w],
            [w,g,g,e,g,g,g,g,g,g,g,g,w,g,g,w],
            [w,g,g,g,g,w,g,g,w,w,w,w,w,g,g,w],
            [w,g,n,g,g,w,e,g,e,g,g,g,g,g,g,w],
            [w,g,g,g,g,w,g,g,g,g,g,g,g,g,c,w],
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
        ]
    elif bossid == "2":
        level = [
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
            [w,s,g,g,g,g,e,w,w,g,g,g,g,g,g,w],
            [w,g,g,g,g,g,g,g,g,g,g,g,g,e,g,w],
            [w,g,g,g,g,g,g,g,e,g,g,w,w,g,g,w],
            [w,g,g,g,g,g,g,w,g,g,g,w,w,g,g,w],
            [w,g,g,g,g,e,g,w,g,g,g,g,g,e,g,w],
            [w,e,g,g,w,w,w,w,w,c,g,g,g,g,g,w],
            [w,g,g,g,g,g,g,w,w,g,g,g,g,g,g,w],
            [w,g,g,g,g,g,g,w,w,w,w,w,w,g,g,w],
            [w,g,g,g,g,g,g,g,w,g,g,g,g,g,g,w],
            [w,g,g,w,w,g,e,g,w,g,g,g,g,g,g,w],
            [w,g,g,e,w,g,g,g,g,g,g,b,g,g,e,w],
            [w,e,g,g,w,g,g,g,g,g,g,g,g,g,g,w],
            [w,g,g,g,w,e,g,g,g,g,g,g,g,e,g,w],
            [w,g,g,g,w,g,g,g,g,g,e,g,g,g,g,w],
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
        ]
    elif bossid == "3":
        level = [
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
            [w,s,g,g,g,g,g,g,g,g,g,g,g,g,e,w],
            [w,g,g,g,g,g,g,e,g,g,g,g,g,g,g,w],
            [w,g,g,w,w,g,e,w,w,g,g,w,w,g,g,w],
            [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
            [w,g,g,g,g,g,g,g,g,e,g,g,g,g,g,w],
            [w,g,g,e,g,g,e,g,g,g,g,g,e,g,g,w],
            [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
            [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
            [w,g,g,g,g,e,g,g,g,g,g,g,g,e,g,w],
            [w,g,e,g,g,g,g,g,g,g,b,g,g,g,g,w],
            [w,g,g,w,w,g,g,w,w,g,g,w,w,g,g,w],
            [w,g,g,w,w,g,e,w,w,g,g,w,w,g,g,w],
            [w,g,g,g,g,g,g,g,g,e,g,g,g,c,g,w],
            [w,e,g,g,g,g,g,g,g,g,g,g,g,g,g,w],
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
        ]
    elif bossid == "4":
        level = [
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
            [w,s,g,g,g,g,e,g,g,g,g,g,e,g,g,w],
            [w,g,g,g,g,g,g,g,g,g,w,g,g,g,g,w],
            [w,g,g,g,g,g,g,g,g,g,w,e,g,g,g,w],
            [w,g,g,g,g,g,w,g,g,g,w,w,w,w,w,w],
            [w,g,g,g,g,e,w,g,g,g,g,g,g,e,g,w],
            [w,e,g,g,g,g,w,g,g,g,g,e,g,g,g,w],
            [w,w,g,g,w,w,w,w,w,g,g,g,g,g,g,w],
            [w,w,g,e,g,g,w,w,w,w,w,g,g,g,g,w],
            [w,g,g,g,g,g,c,g,w,g,g,g,g,g,g,w],
            [w,g,g,g,g,g,g,g,w,g,g,g,g,g,e,w],
            [w,g,g,w,w,g,g,g,w,g,g,b,g,g,g,w],
            [w,g,g,w,w,g,g,g,w,g,g,g,g,g,g,w],
            [w,g,e,g,g,e,g,g,g,g,g,g,g,e,g,w],
            [w,g,g,g,g,g,g,g,g,g,e,g,g,g,g,w],
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
        ]
    else:
        level = level(" ")
    
    
    for row in level:
        for subtile in row:
            if subtile == e:
                enemypos = [ level.index(row),row.index(subtile) ]
                level[enemypos[0]][enemypos[1]] = random.choice(enemies)
    return level