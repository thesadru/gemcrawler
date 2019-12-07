class hero:
    def __init__(self,id,name,health,armor,strengh,stamina,speed,super):
        self.id = id
        self.name = name
        self.health = health
        self.armor = armor
        self.strengh = strengh
        self.stamina = stamina
        self.speed = speed
        self.super = super
        self.hp = health
        self.st = stamina
class enemy:
    def __init__(self,id,name,health,strengh,speed,range):
        self.id = id
        self.name = name
        self.health = health
        self.strengh = strengh
        self.speed = speed
        self.range = range
        self.hp = health
class boss:
    def __init__(self,id,name,health,strengh,speed,range,super):
        self.id = id
        self.name = name
        self.health = health
        self.strengh = strengh
        self.speed = speed
        self.range = range
        self.super = super
        self.hp = health

heroes = [
    hero(0,"robot"   ,4,3,3,180,3,"drone"     ), # special challenge | sets a turret that damages enemies in range
    hero(1,"knight"  ,6,5,4,200,4,"bleed"     ), # basic +2 +2 +1 +20 +1 | makes all the enemies around bleed
    hero(2,"werewolf",8,3,3,180,3,"shapeshift"), # health +4 | higher speed and heals hp
    hero(3,"paladin" ,4,7,3,180,3,"restore"   ), # armor +4 | sets armor higher then max
    hero(4,"viking"  ,4,3,6,180,3,"punch"     ), # strengh +3 | jumps to area and damages all enemies there
    hero(5,"wizard"  ,4,3,3,240,3,"fire ball" ), # stamina +60 | damages all enemies in range of fireball
    hero(6,"rogue"   ,4,3,3,180,5,"speed"     ), # speed +2 | higher speed and range
]

enemies = [
    enemy(0 ,"blocade" ,10,10,0,1), # 0
     
    enemy(1 ,"worm"    ,1,2,1,1), # 1
    enemy(2 ,"crab"    ,1,4,2,1), # 2
    enemy(3 ,"beetle"  ,2,6,2,1), # 3
    enemy(4 ,"slime"   ,3,8,2,1), # 4
    enemy(5 ,"zombie"  ,4,8,3,1), # 5
    enemy(6 ,"spider"  ,4,10,4,1),# 6
    enemy(7 ,"miner"   ,6,10,4,1),# 7
    enemy(8 ,"knight"  ,6,12,5,1),# 8
    enemy(9 ,"guard"   ,7,14,5,1),# 9
    
    enemy(10,"goblin"  ,3,2,2,2), # 10
    enemy(11,"skeleton",4,2,2,3), # 11
    enemy(12,"witch"   ,5,4,2,3), # 12
    enemy(13,"wizard"  ,5,6,2,4), # 13
    enemy(14,"alien"   ,4,8,4,4), # 14
    enemy(15,"phantom" ,4,8,5,5), # 15
    enemy(16,"soldier" ,5,10,5,5),# 16
]

bosses = [
    boss(0,"grand wizard" ,5,20,5,5,"fireball"), # can summon a fireball anywhere
    boss(1,"skeleton king",5,20,5,5,"summon"  ), # can deploy worms crabs and beetles
    boss(2,"goblin priest",5,20,5,5,"heal"    ), # can heal
    boss(3,"alien UFO"    ,5,20,5,5,"teleport"), # can teleport anywhere where it can see
    boss(4,"sandworm"     ,5,20,5,5,"dig"     ), # can go underground and speed up
]