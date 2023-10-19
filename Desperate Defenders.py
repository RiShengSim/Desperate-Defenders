# Sim Ri Sheng S10239700 Programming Assignment 
import random


# Game variables
game_vars = {
    'turn': 0,                      # Current Turn
    'monster_kill_target': 20,      # Number of kills needed to win
    'monsters_killed': 0,           # Number of monsters killed so far
    'num_monsters': 0,              # Number of monsters in the field
    'gold': 10,                     # Gold for purchasing units
    }

archer = {'shortform' : 'ARCHR',
          'name': 'Archer',
          'maxHP': 5,
          'min_damage': 1,
          'max_damage': 4,
          'price': 5
          }
cannon = {'shortform' : 'CANON',
          'name': 'Cannon',
          'maxHP': 8,
          'min_damage': 3,
          'max_damage': 5,
          'price': 7
          }
custom_def1 = {'shortform' : ' ',
          'name': ' ',
          'maxHP': 0,
          'min_damage': 0,
          'max_damage': 0,
          'price': 0
          }
custom_def2 = {'shortform' : ' ',
          'name': ' ',
          'maxHP': 0,
          'min_damage': 0,
          'max_damage': 0,
          'price': 0
          }
custom_def3 = {'shortform' : ' ',
          'name': ' ',
          'maxHP': 0,
          'min_damage': 0,
          'max_damage': 0,
          'price': 0
          }
             
wall = {'shortform': 'WALL',
        'name': 'Wall',
        'maxHP': 20,
        'min_damage': 0,
        'max_damage': 0,
        'price': 3
        }

werewolf = {'shortform': 'WWolf',
          'name': 'Werewolf',
          'maxHP': 10,
          'min_damage': 1,
          'max_damage': 4,
          'moves' : 2,
          'reward': 3
          }



zombie = {'shortform': 'ZOMBI',
          'name': 'Zombie',
          'maxHP': 15,
          'min_damage': 3,
          'max_damage': 6,
          'moves' : 1,
          'reward': 2
          }
custom_mon1 = {'shortform': ' ',
          'name': ' ',
          'maxHP': 0,
          'min_damage': 0,
          'max_damage': 0,
          'moves' : 0,
          'reward': 0
          }
custom_mon2 = {'shortform': ' ',
          'name': ' ',
          'maxHP': 0,
          'min_damage': 0,
          'max_damage': 0,
          'moves' : 0,
          'reward': 0
          }
custom_mon3 = {'shortform': ' ',
          'name': ' ',
          'maxHP': 0,
          'min_damage': 0,
          'max_damage': 0,
          'moves' : 0,
          'reward': 0
          }

monster_kill = { 'killed' : 0,
                 'danger' : 1,
                 'danger_bar' : 0,
                 }
                 

field = [ [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None]]

#Lists
f_characters = [archer,wall,cannon]
monster_list = [zombie,werewolf]
total_friendly_damage = []
total_monster_damage = []
custom_monster_list = [custom_mon1,custom_mon2,custom_mon3]
custom_friendly_list = [custom_def1,custom_def2,custom_def3]

threat = '-'
#If there is 5 rows, total_friendly_damage and Total_monster_damage = [0,0,0,0,0]
#                                                                (row1,row2,row3,row4,row5)
for i in range(len(field)):
    total_friendly_damage.append(0)
    total_monster_damage.append(0)




#----------------------------------------------------------------------
# draw_field()
#
#    Draws the field of play
#    The column numbers only go to 3 since players can only place units
#      in the first 3 columns
#----------------------------------------------------------------------
#Letters in list = number of roles if there is only 3 roles, only 3 letters will be in the list( Exampleif there is 3 rows letters = [A,B,C])
letters = []
for i in range(ord('a'), ord('z')+1-26+len(field)):
    letters.append(chr(i).upper())




def draw_field():
    friendly_location = []
    for i in range(len(field)):
        friendly_location.append(0)
    for g in range(len(field)):
        for j in range(len(field[g])):
            for h in f_characters:
                if field[g][j] == h:
                    friendly_location[g] += 1
#Number of columns defender can be placed    
    print('    1     2     3')
    for i in range(len(field)):
        f_num = friendly_location[i]
        monster_taken_damage = False
        friendly_taken_damage = False
        print(' ', end = '')
#Printing field
        for x in range(len(field[i])):
            print('+-----', end = '')
        print('+')
        print('{:1}'.format(letters[i],''), end ='')
        for r in range(len(field[i])):
            
            if field[i][r] == None:
                print('|{:5}'.format(''), end ='')

            else:
                print('|{:5}'.format(field[i][r]['shortform']), end ='')
        print('|')

        print(' ', end = '')
        for r in range(len(field[i])):
            if field[i][r] == None:
                print('|{:5}'.format(''), end ='')
            else:
                for p in monster_list:   
                    if field[i][r] == p:
                        #monster_taken_damage variable is here to
                        #check if the first monster in each row have taken damage.
                        #So that other monster would not be damaged
                        if monster_taken_damage == False and field[i][r] == p:
                            remain = field[i][r]['maxHP'] - total_friendly_damage[i]
                            #---------------------------
                            #Double Check if monster alive
                            if remain <= 0 :
                                field[i][r] = None
                                spawn_monster(field, monster_list)
                                total_monster_damage[i] = 0
                            #---------------------------
                            remain = field[i][r]['maxHP'] - total_friendly_damage[i]
                            print('|{:<5}'.format('{}/{}'.format(remain,field[i][r]['maxHP'])), end = '')
                            monster_taken_damage = True
                            
                            break
                        elif monster_taken_damage == True and field[i][r] == p:
                            remain = field[i][r]['maxHP']
                            print('|{:<5}'.format('{}/{}'.format(remain,field[i][r]['maxHP'])), end = '')
                            
                            break
                            
                
                #friendly_taken_damage have the same function as monster_taken_damage just that it is for defenders        
                for p in f_characters:
                    if field[i][r] == p:
                        if friendly_taken_damage == False and f_num-1 == 0:
                            remain = field[i][r]['maxHP'] - total_monster_damage[i]
                            print('|{:<5}'.format('{}/{}'.format(remain,field[i][r]['maxHP'])), end = '')
                            friendly_taken_damage = True
                            break
                        else:
                            remain = field[i][r]['maxHP']
                            print('|{:<5}'.format('{}/{}'.format(remain,field[i][r]['maxHP'])), end = '')
                            f_num -= 1

                            break

        print('|')
    print(' ', end = '')
    for i in range(len(field[0])):
        print('+-----', end = '')
    print('+')
            
            
            
                   
                   
    return

#----------------------------
# show_combat_menu()
#
#    Displays the combat menu
#----------------------------
def show_combat_menu(game_vars):
    print("1. Buy unit     2. End turn")
    print("3. Save game    4. Quit")

#----------------------------
# show_main_menu()
#
#    Displays the main menu
#----------------------------
def show_main_menu():
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Introduction & Rules")
    print("4. Custom Units")
    print("5. Quit")
    
    

#-----------------------------------------------------
# place_unit()
#
#    Places a unit at the given position
#    This function works for both defender and monster
#    Returns False if the position is invalid
#       - Position is not on the field of play
#       - Position is occupied
#       - Defender is placed past the first 3 columns
#    Returns True if placement is successful
#-----------------------------------------------------


def place_unit(field, position, unit_name):
    
    return True

#-------------------------------------------------------------------
# buy_unit()
#
#    Allows player to buy a unit and place it using place_unit()
#-------------------------------------------------------------------
def buy_unit(field, game_vars):
    unit_end = False
    position_check = False
    not_enough = True
    for i in f_characters:
    #Check if gold enough for any units, if not then not_enough will be True
    #and you will not be allowed to buy units
        if game_vars['gold'] >= i['price'] :
            not_enough = False
            
    if not_enough == True:
        print('You have insufficent gold to purchase any units')
    else:
        print('What unit do you wish to buy?')
        num = 1
    #print number of units available to buy accordingly
        for i in range(len(f_characters)):
            print('{}. {} ({} gold)'.format(num,f_characters[i]['name'],f_characters[i]['price']))
            num += 1
        print('{}. Don'.format(num)+"'"+'t buy')
        Error_check = True
        while Error_check == True:
            try:
                buy = int(input("Your choice?"))
                
                if buy <= num and buy > 0:
                    Error_check = False
                else:
                    print('Please enter a valid answer')
            except Exception:
                print('Please enter a valid answer')
        
          
        confirm = False
        while confirm == False:
            if buy == num:
                break
                
            else:
                if unit_end == True:
                    break
                
                elif game_vars['gold'] - (f_characters[buy-1]['price']) < 0:
                        print('You have insufficient ammount to buy {}'.format(f_characters[buy-1]['name']))
                        break
                else:
                    buy_check = False
                    while buy_check == False:
                        location = input('Place where?\nPress 1 to cancel')
                        position_check = False
                        
                        try:
                            if location == '1':
                                buy_check = True
                                confirm = True
                                break
                            elif int(location[1]) >3 or int(location[1]) < 0:
                                print('Please input a valid locaiton')
                                position_check = True
                            elif len(location) == 2 or location[0].isalpha() == True and location[1].isdigit() == True:
                                
                                if field[letters.index(location[0].upper())][int(location[1])-1] != None:
                                    position_check = True
                    
                        
                            if position_check == True:
                                while True:
                                    try:
                                        print('There is already a character there')
                                        again = int(input('1. Buy another unit \n2. Choose another location \n3. End Turn'))
                                        if again == 1:
                                            buy_unit(field ,game_vars)
                                            unit_end = True
                                            position_check = True
                                            break
                                        elif again == 2:
                                            #does nothing, just for me to know 
                                            print('')
                                            position_check = True
                                            break

                                        elif again == 3:
                                            buy_check = True
                                            confirm = True
                                            position_check = True
                                            break
                                    except Exception:
                                        print('Please enter a valid answer')
                            elif len(location) > 2 or len(location) < 2:
                                position_check = True
                                print('Please enter a valid location on the board')
                                    
                            if position_check == False :
                                print('*** {} placed on row {} column {}'.format(f_characters[buy-1]['name'],location[0].upper(),location[1]))                               
                                field[letters.index(location[0].upper())].pop(int(location[1])-1)
                                field[letters.index(location[0].upper())].insert(int(location[1])-1,f_characters[buy-1])
                                game_vars['gold'] -= f_characters[buy-1]['price']
                                buy_check = True
                                confirm = True
                                
                                
                                    
                        except Exception:
                            print('Please enter a valid location on the board')
                            position_check = True
         
        
    return

#-----------------------------------------------------------
# defender_attack()
#
#    Defender unit attacks.
#
#-----------------------------------------------------------
def defender_attack(field):
    friendly = []
    lane = []
    cannon_push_lane = []
    for y in range(len(field)):
        lane.append(0)
    for e in range(len(f_characters)):
        friendly.append([])
        for x in range(len(field)):
            friendly[e].append(0)
    for r in range(len(field)):
        for c in range(len(field[r])):
            for q in f_characters:
                if field [r][c] == q:
                    friendly[f_characters.index(q)][r] += 1

    


    
    for i in range(len(friendly)):
        for p in range(len(field)):
                for x in range(friendly[i][p]):
                    minimun_dmg = f_characters[i]['min_damage']
                    maximun_dmg = f_characters[i]['max_damage']
                    number = random.randint(minimun_dmg,maximun_dmg)
                    lane[p] += number
    #Check if there is a cannon on the specific lane example there is cannon on lane one, cannon_push_lane list will be [1,,0,0,0,0]                
    for y in range(len(field)):
        cannon_push_lane.append(0)
    for i in range(len(cannon_push_lane)):
        for r in range(len(field[i])):
            if field[i][r] == cannon:
                cannon_push_lane[i] += 1
    #See if cannon got luck and push zombies back, check one by one          
    for i in range(len(cannon_push_lane)):
        for q in range(cannon_push_lane[i]):
            check_if_mon_pushed = False
            if cannon_push_lane[i] >= 1:
                push_chance = random.randint(1,2)
                if push_chance == 1:
                    for r in range(len(field[i])):
                        for x in monster_list:
                            try:
                                if field[i][r] == x and field[i][r+1] == None:
                                    field[i][r] = None
                                    field[i][r+1] = x
                                    check_if_mon_pushed = True
                                break
                            except Exception:
                                field[i][r] = x
                                break
                        if check_if_mon_pushed == True:
                            break
   #Damaging monsters                 
    for i in range(len(lane)):
        for r in range(len(field[i])):
            for x in monster_list:
                if field[i][r] == x:
                    total_friendly_damage[i] += lane[i]                   
                    
                    if total_friendly_damage[i] >= x['maxHP']:   
                        monster_kill['killed'] += 1
                        monster_kill['danger'] += 1
                        monster_kill['danger_bar'] += 1
                        total_friendly_damage[i] = 0
                        field[i].remove(x)
                        field[i].append(None)
                        spawn_monster(field, monster_list)
                        game_vars['gold'] += x['reward']
                        if monster_kill['danger_bar'] == 10:
                            spawn_monster(field, monster_list)
                            monster_kill['danger_bar'] = 0
    
                
                
        
                        
                    
                
        
    
    
    return

#-----------------------------------------------------------
# monster_advance()
#
#    Monster unit advances.
#       - If it lands on a defender, it deals damage
#       - If it lands on a monster, it does nothing
#       - If it goes out of the field, player loses 
#-----------------------------------------------------------


#Monster moving forward
def monster_advance(monster_list, field, total_friendly_damage):
    monster_on_field = 0
    moves = 0
    for r in range(len(field)):
        for c in range(len(field[r])):
            for q in monster_list:

                if field[r][c] == q:
                    for i in f_characters:
                        if field[r][c-1] == i:
                            min_dmg = q['min_damage']
                            max_dmg = q['max_damage']
                            random_dmg = random.randint(min_dmg,max_dmg)
                            total_monster_damage[r] += random_dmg
                            print(random_dmg)
                            
                            if total_monster_damage[r] >= i['maxHP']:
                                
                                total_monster_damage[r] = 0
                                field[r][c-1] = None
                                
                                
                                
                            
                  
                            
    for r in range(len(field)):
        for c in range(len(field[r])):
            for q in monster_list:
                if field[r][c] == q:
                    monster_on_field += 1 
    for r in range(len(field)):
        for c in range(len(field[r])):
                for q in monster_list:
                    if field[r][c] == q:
                        if field[r][c-1] != None:
                            if moves != 0:
                                field[r][c-moves] = q
                                field[r][c] = None
                            break
                        else:
                        #Monster move one by one so that it cannot go behind the defenders
                            for i in range(q['moves']):
                                if field[r][c-moves-1] == None:
                                    moves += 1
                                elif field[r][c-moves-1] != None:
                                    break
                            if moves != 0:
                                for o in range(moves):
                                    
                                    if c - moves < 0:
                                        moves -= 1
                                    else:
                                        
                                        field[r][c-moves] = q
                                        field[r][c] = None
                                        print('{} in lane {} advances!'.format(q['name'],letters[r]))
                                        moves = 0
                                        break
                    
                        
     
            
                     
    
                
    
            
    
    
    return

#---------------------------------------------------------------------
# spawn_monster()
#
#    Spawns a monster in a random lane on the right side of the field.
#    Assumes you will never place more than 5 monsters in one turn.
#---------------------------------------------------------------------
def spawn_monster(field, monster_list):
    for i in range(len(field)):
        monster_at_last = False
        if field[i][0] == None:
            monter_at_last = True
            break
    if monster_at_last == False:    
        monster = random.randint(0, len(monster_list)-1)
        place = random.randint(0, len(field)-1)
        #If the row is occupied by another monster, it will run the random number 
        #generator again to find an empty slot
        while field[place][len(field[place])-1] != None:
            place = random.randint(0, len(field)-1)
            
        field[place][-1] = monster_list[monster]
        monster_spawned = monster_list[monster]
    
    return

#-----------------------------------------
# save_game()
#
#    Saves the game in the file 'save.txt'
#-----------------------------------------
def save_game():
    file = open("save_game.txt", "w")
               #0    1   2     3    4   5     6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   
    file.write('{}\n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} '.\
               format(game_vars['turn'],game_vars['monster_kill_target'],#0-1
                      monster_kill['killed'],game_vars['gold'],#2-3
                      field,#4
                      monster_kill['danger'],monster_kill['danger_bar'],#5-6
                      total_friendly_damage,total_monster_damage,#7-8
                      
                      custom_def1['shortform'],custom_def1['name'],#9-10
                      custom_def1['maxHP'],custom_def1['min_damage'],#11-12
                      custom_def1['max_damage'],custom_def1['price'],#13-14
                      
                      custom_def2['shortform'],custom_def2['name'],#15-16
                      custom_def2['maxHP'],custom_def2['min_damage'],#17-18
                      custom_def2['max_damage'],custom_def2['price'],#19-20
                      
                      custom_def3['shortform'],custom_def3['name'],#21-22
                      custom_def3['maxHP'],custom_def3['min_damage'],#23-24
                      custom_def3['max_damage'],custom_def3['price'],#25-26
                      
                      custom_mon1['shortform'],custom_mon1['name'],#27-28
                      custom_mon1['maxHP'],custom_mon1['min_damage'],#29-30
                      custom_mon1['max_damage'],custom_mon1['moves'],#31-32
                      custom_mon1['reward'],#33
                      
                      custom_mon2['shortform'],custom_mon2['name'],#34-35
                      custom_mon2['maxHP'],custom_mon2['min_damage'],#36-37
                      custom_mon2['max_damage'],custom_mon2['moves'],#38-39
                      custom_mon2['reward'],#40
                      
                      custom_mon3['shortform'],custom_mon3['name'],#41-42
                      custom_mon3['maxHP'],custom_mon3['min_damage'],#43-44
                      custom_mon3['max_damage'],custom_mon3['moves'],#45-46
                      custom_mon3['reward']))#47
    
    
    print("Game saved.")


#-----------------------------------------
# load_game()
#
#    Loads the game from 'save.txt'
#-----------------------------------------
def load_game(game_vars):
    print(' ')
    

#-----------------------------------------------------
# initialize_game()
#
#    Initializes all the game variables for a new game
#-----------------------------------------------------
def initialize_game():
    game_vars['turn'] = 0
    game_vars['monster_kill_target'] = 20
    game_vars['monsters_killed'] = 0
    game_vars['num_monsters'] = 0
    game_vars['gold'] = 10
#-----------------------------------------------------
# Custom units programme
# Make your own character
#
#-----------------------------------------------------
def custom_unit():
    characters5 = False
    while True:
        try:
            custom_choice = int(input('Which custom unit do you want to modify?\n\
1.Defenders\n\
2.Monsters\n\
3.Back'))
            if custom_choice > 3 or custom_choice < 0:
                print('Please input a valid answer')
            elif custom_choice == 1:
                print('Which custom defender do you want to customise?\n\n')
                for i in range(len(custom_friendly_list)):
                    print('{}.Custom Defender{}\n\
shortform : {}\n\
name : {}\n\
maxHP : {}\n\
min_damage: {}\n\
max_damage: {}\n\
price: {}\n\n\n'.format(i+1,i+1,\
                        custom_friendly_list[i]['shortform'],\
                        custom_friendly_list[i]['name'],\
                        custom_friendly_list[i]['maxHP'],\
                        custom_friendly_list[i]['min_damage'],\
                        custom_friendly_list[i]['max_damage'],\
                        custom_friendly_list[i]['price']))
            elif custom_choice == 2:
                print('Which custom monster do you want to customise?\n\n')
                for i in range(len(custom_monster_list)):
                    print('{}.Custom Monster{}\n\
shortform : {}\n\
name : {}\n\
maxHP : {}\n\
min_damage: {}\n\
max_damage: {}\n\
moves : {},\n\
reward: {}\n\n\n'.format(i+1,i+1,\
                   custom_monster_list[i]['shortform'],\
                   custom_monster_list[i]['name'],\
                   custom_monster_list[i]['maxHP'],\
                   custom_monster_list[i]['min_damage'],\
                   custom_monster_list[i]['max_damage'],\
                   custom_monster_list[i]['moves'],\
                   custom_monster_list[i]['reward']))
        except Exception:
            print('Please input a valid answer')
        if custom_choice == 1:
            while True:
                try:
                    friendly_choice = int(input('Your choice?'))
                    if friendly_choice <1 or friendly_choice >3:
                        print('Please input a valid answer')
                    else:
                        break
                            
                except Exception:
                    print('Please input a valid answer')
            while characters5 == False:
                try:
                    custom_friendly_list[friendly_choice-1]['shortform'] = input('Input name shortform (5 characters no more no less)')
                    if len(custom_friendly_list[friendly_choice-1]['shortform']) == 5:
                        characters5 = True
                    else:
                        print('Please input a valid answer')
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:
                    custom_friendly_list[friendly_choice-1]['name'] = input('Input name')
                    break
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:
                    custom_friendly_list[friendly_choice-1]['maxHP'] = int(input('Input maxHP'))
                    if custom_friendly_list[friendly_choice-1]['maxHP'] <= 0:
                        print('Please give a HP higher than 0')
                    else:
                        break
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:    
                    custom_friendly_list[friendly_choice-1]['min_damage'] = int(input('Input min_damage'))
                    break
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:
                    custom_friendly_list[friendly_choice-1]['max_damage'] = int(input('Input max_damage'))
                    break
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:
                    custom_friendly_list[friendly_choice-1]['price'] = int(input('Input price'))
                    break
                except Exception:
                    print('Please input a valid answer')
            print('You have successfully customised Defender{}'.format(friendly_choice))
            for i in f_characters:
                if custom_friendly_list[friendly_choice-1] == i:
                    print('')
                else:
                    f_characters.append(custom_friendly_list[friendly_choice-1])
                    break
                    
            break
        elif custom_choice == 2:
            while True:
                try:
                    monster_choice = int(input('Your choice?'))
                    if monster_choice <1 or monster_choice >3:
                        print('Please input a valid answer')
                    else:
                        break
                            
                except Exception:
                    print('Please input a valid answer')
            while characters5 == False:
                try:
                    custom_monster_list[monster_choice-1]['shortform'] = input('Input name shortform (5 characters no more no less)')
                    if len(custom_monster_list[monster_choice-1]['shortform']) == 5:
                        characters5 = True
                    else:
                        print('Please input a valid answer')
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:
                    custom_monster_list[monster_choice-1]['name'] = input('Input name')
                    break
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:
                    custom_monster_list[monster_choice-1]['maxHP'] = int(input('Input maxHP'))
                    if custom_monster_list[monster_choice-1]['maxHP'] <= 0:
                        print('Please give a HP higher than 0')
                    else:
                        break
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:    
                    custom_monster_list[monster_choice-1]['min_damage'] = int(input('Input min_damage'))
                    break
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:
                    custom_monster_list[monster_choice-1]['max_damage'] = int(input('Input max_damage'))
                    break
                except Exception:
                    print('Please input a valid answer')
            while True:
                try:
                    custom_monster_list[monster_choice-1]['moves'] = int(input('Input moves'))
                    break
                except Exception:
                    print('Please input a valid answer')
                        
            while True:
                try:
                    custom_monster_list[monster_choice-1]['reward'] = int(input('Input reward'))
                    break
                except Exception:
                    print('Please input a valid answer')
            print('You have successfully customised Monster{}'.format(monster_choice))
            for i in monster_list:
                if custom_monster_list[monster_choice-1] == i:
                    print('')
                else:
                    monster_list.append(custom_monster_list[monster_choice-1])
                    break
                    
            
            break
        if custom_choice == 3:
            break
    return


#-----------------------------------------------
# Intro and Rules
#
#
#-----------------------------------------------
def rules():
    print('-----------------------Introduction-----------------------\n \
Welcome to a tower defense game created by Sim Ri Sheng.\n \
This game is made for his assignment which is due on \n\
7/8/2022.It is made so that you can add up to 3 customiseable\n \
characters each on both defenders and attacker' + "'s" + ' team.\n \
AIMING FOR A+ and above')
    print('-----------------------Rules-----------------------\n\
1. You will get 1 gold at the end of each round\n \n\
2.The monster will only attack the defender when it is \n\
trying to enter a defender' + "'s" +  ' spot (It will move in \n\
front of the defender first then attack next turn\n \n\
3. When the monster spawns, it will be instantly attack\n\
if there are defenders in the same row\n \n\
4.Gold will be rewarded for each kill, different monsters\n\
gives different amount of gold\n\n\
5.You can only create up to 6 custom monsters, but monsters\n\
will only be available for use when all requirements\n\
are given\n\n\
6. After every 10 kills, the threat bar will be filled,\n\
one kill 1 bar, increasing the number of monsters on field\n\
by 1 each time\n\n\
7. Cannon have a 50% chance to push a monster back 1 square\n\
and if there is 2 or more, it will have a chance to move back\n\
2 or 3 times\n\n\
8. Enjoy the game!\n\n\n')
    









#-----------------------------------------
#               MAIN GAME
#-----------------------------------------

# TO DO: ADD YOUR CODE FOR THE MAIN GAME HERE!
control = False
loop =  False
check = False
end_game = False
stop_game = False
while stop_game == False:
    while check == False:
        print("Desperate Defenders")
        print("-------------------")
        print("Defend the city from undead monsters!")
        print()
        show_main_menu()
        
        try:
            choice = int(input('Your choice?'))
            if choice == 1:
                
                while True:
                    try:
                        ask_for_edit = int(input('Do you want to edit your playing field?\n1. Yes\n2. No'))
                        if ask_for_edit == 1:
                            field = []
                            row_editor = True
                            column_editor = True
                            while column_editor == True:
                                try:
                                    column = int(input('How many columns do you want your field to have?'))
                                    column_editor = False
                                except Exception:
                                    print('Please input a valid answer')
                            while row_editor == True:
                                try:
                                    row = int(input('How many rows do you want your field to have?'))
                                    row_editor = False
                                except Exception:
                                    print('Please input a valid answer')
                            for i in range(row):
                                field.append([])
                            for i in range(row):
                                for r in range(column):
                                    field[i].append(None)
                            letters = []
                            for i in range(ord('a'), ord('z')+1-26+len(field)):
                                letters.append(chr(i).upper())
                            for i in range(len(field)):
                                total_friendly_damage.append(0)
                                total_monster_damage.append(0)
                            break
                        if ask_for_edit == 2:
                            break
                    except Exception:
                        print('Please input a valid answer')
                while True:
                    try:
                        asking_for_edit_kill = int(input('Do you want to edit monster kill target?\n1. Yes \n2. No'))
                        if asking_for_edit_kill == 1:
                            game_vars['monster_kill_target'] = int(input('Please input how many kills to win the game'))
                            break
                        if asking_for_edit_kill == 2:
                            break
                        else:
                            print('Please input a valid answer')
                    except Exception:
                        print('Please input a valid answer')
                spawn_monster(field, monster_list)
                check = True

            elif choice == 2:
                try:
                    f_characters = [archer,wall,cannon]
                    monster_list = [zombie,werewolf]
                    check = True
        
                    file = open("save_game.txt", "r")
                    game = []
                    for line in file:
                        line = line.strip("\n") # strip the new line
                        line_list = line.split(",") # convert string to a list
                        game.append(line_list) # append each line_list to sales

                    file.close()
                    field = []
                    total_friendly_damage = []
                    total_monster_damage = []
                    start_stop = True
                    game_vars['turn'] = int(game[0][0])-1
                    game_vars['monster_kill_target'] = int(game[1][0])
                    monster_kill['killed'] = int(game[2][0])
                    game_vars['gold'] = int(game[3][0])
                    monster_kill['danger'] = int(game[5][0])
                    monster_kill['danger_bar'] = int(game[6][0])
                    field_num = 0
                    for r in range(len(game[7])):
                        if game[7][r][-1] == ']':
                            total_friendly_damage.append(int(game[7][r][0:-1]))
                        elif game[7][r][-2] == ']':
                            total_friendly_damage.append(int(game[7][r][0:-2]))
                        elif game[7][r][0] == ' ':
                            total_friendly_damage.append(int(game[7][r][1:]))
                        elif game[7][r][0] == '[':
                            total_friendly_damage.append(int(game[7][r][1:]))        

                    field_num = 0
                    for r in range(len(game[8])):
                        if game[8][r][-1] == ']':
                            total_monster_damage.append(int(game[8][r][0:-1]))
                        elif game[8][r][-2] == ']':
                            total_monster_damage.append(int(game[8][r][0:-2]))
                        elif game[8][r][0] == ' ':
                            total_monster_damage.append(int(game[8][r][1:]))
                        elif game[8][r][0] == '[':
                            total_monster_damage.append(int(game[8][r][1:]))
                            
                    custom_def1['shortform'] = game[9][0][:-1]
                    custom_def1['name'] = game[10][0][:-1]
                    custom_def1['maxHP'] = int(game[11][0][:-1])
                    custom_def1['min_damage'] = int(game[12][0][:-1])
                    custom_def1['max_damage'] = int(game[13][0][:-1])
                    custom_def1['price'] = int(game[14][0][:-1])
                    
                    custom_def2['shortform'] = game[15][0][:-1]
                    custom_def2['name'] = game[16][0][:-1]
                    custom_def2['maxHP'] = int(game[17][0][:-1])
                    custom_def2['min_damage'] = int(game[18][0][:-1])
                    custom_def2['max_damage'] = int(game[19][0][:-1])
                    custom_def2['price'] = int(game[20][0][:-1])
                    
                    custom_def3['shortform'] = game[21][0][:-1]
                    custom_def3['name'] = game[22][0][:-1]
                    custom_def3['maxHP'] = int(game[23][0][:-1])
                    custom_def3['min_damage'] = int(game[24][0][:-1])
                    custom_def3['max_damage'] = int(game[25][0][:-1])
                    custom_def3['price'] = int(game[26][0][:-1])
                    
                    custom_mon1['shortform'] = game[27][0][:-1]
                    custom_mon1['name'] = game[28][0][:-1]
                    custom_mon1['maxHP'] = int(game[29][0][:-1])
                    custom_mon1['min_damage'] = int(game[30][0][:-1])
                    custom_mon1['max_damage'] = int(game[31][0][:-1])
                    custom_mon1['moves'] = int(game[32][0][:-1])
                    custom_mon1['reward'] = int(game[33][0][:-1])
                    
                    custom_mon2['shortform'] = game[34][0][:-1]
                    custom_mon2['name'] = game[35][0][:-1]
                    custom_mon2['maxHP'] = int(game[36][0][:-1])
                    custom_mon2['min_damage'] = int(game[37][0][:-1])
                    custom_mon2['max_damage'] = int(game[38][0][:-1])
                    custom_mon2['moves'] = int(game[39][0][:-1])
                    custom_mon2['reward'] = int(game[40][0][:-1])
                    
                    custom_mon3['shortform'] = game[41][0][:-1]
                    custom_mon3['name'] = game[42][0][:-1]
                    custom_mon3['maxHP'] = int(game[43][0][:-1])
                    custom_mon3['min_damage'] = int(game[44][0][:-1])
                    custom_mon3['max_damage'] = int(game[45][0][:-1])
                    custom_mon3['moves'] = int(game[46][0][:-1])
                    custom_mon3['reward'] = int(game[47][0][:-1])
                    for i in custom_monster_list:
                        if i['shortform'] != ' ':
                            monster_list.append(i)
                    for i in custom_friendly_list:
                        if i['shortform'] != ' ':
                            f_characters.append(i)
                    for i in range(len(game[4])):
                        if game[4][i][0] == '[':
                            field.append([])
                        elif game[4][i][1] == '[':
                            field.append([])
                    field_num = 0
                    for r in range(len(game[4])):
                        if game[4][r][0] == '[':
                            if game[4][r][2:] == 'None':
                                field[field_num].append(None)
                        elif game[4][r][1] == '[':
                            if game[4][r][2:] == 'None':
                                field[field_num].append(None)
                        elif game[4][r][0] == ' ':  
                            if game[4][r][1:5] == 'None':
                                field[field_num].append(None)
                        if game[4][r][2:6] == 'name':
                            for q in monster_list:
                                if q['name'] == game[4][r][10:-1]:
                                    field[field_num].append(q)
                        if game[4][r][2:6] == 'name':
                            for q in f_characters:
                                if q['name'] == game[4][r][10:-1]:
                                    field[field_num].append(q)
                        if len(game[4][r]) >= 6:
                            if game[4][r][-1] == ']':
                                field_num += 1
                    letters = []
                    for i in range(ord('a'), ord('z')+1-26+len(field)):
                        letters.append(chr(i).upper())
                except Exception:
                    print('There is no saved progress, starting a new game.')
                    field = [ [None, None, None, None, None, None, None],
                              [None, None, None, None, None, None, None],
                              [None, None, None, None, None, None, None],
                              [None, None, None, None, None, None, None],
                              [None, None, None, None, None, None, None]]
                    game_vars['gold'] = 10
                    game_vars['turn'] = 0
                    game_vars['monster_kill_target'] = 20
                    monster_kill['killed'] = 0
                    monster_kill['danger'] = 1
                    monster_kill['danger_bar'] = 0
                    letters = []
                    for i in range(ord('a'), ord('z')+1-26+len(field)):
                        letters.append(chr(i).upper())

                    for i in range(len(field)):
                        total_friendly_damage.append(0)
                        total_monster_damage.append(0)
                    spawn_monster(field, monster_list)
                    for i in range(len(field)):
                        total_friendly_damage.append(0)
                        total_monster_damage.append(0)
                    check = True
            elif choice == 3:
                rules()
            elif choice == 4:
                custom_unit()
            elif choice == 5:
                check = True
                loop = True
                control = True
                
                print('See you next time!')
                
            else:
                print('Please give a valid answer')
                show_main_menu()
        except Exception:
            print('Please give a valid answer')
    game_vars['turn'] += 1
    while control == False:
        while loop == False:
            draw_field()
            for r in range(len(field)):
                for i in range(len(monster_list)):
                    if field[r][0] == monster_list[i]:
                        print('A {} has reached the city! All is lost!'.format(monster_list[i]['name']))
                        loop = True
                        control = True
                        end_game = True
                        game = 4
                        break
            if end_game == False:
                print('Turn {}     Threat = [{:<10}]   Danger Level {}\n Gold = {}   Monters killed = {}/{}'.format\
                      (game_vars['turn'],threat*(monster_kill['danger_bar']),\
                       monster_kill['danger'],game_vars['gold'],monster_kill['killed'],game_vars['monster_kill_target']))
                try:
                    game = int(input('1. Buy Unit     2. End turn \n3. Save game    4. Quit \n5. Return to main menu \nYour choice?'))
                    if game == 1:
                            buy_unit(field, game_vars)
                            
                    
                    elif game == 2:
                            print('You ended your turn')
                            break
                    elif game == 3:
                        save_game()
                    elif game == 4:
                        print('See you next time!')
                        break
                    elif game == 5:
                        while True:
                            try:
                                ask = int(input('Do you want to save the game?\n\
1.Yes\n\
2.No'))
                                if ask == 1:
                                    save_game()
                                    print('Returning to main menu')
                                    break
                                elif ask == 2:
                                    field = [ [None, None, None, None, None, None, None],
                                              [None, None, None, None, None, None, None],
                                              [None, None, None, None, None, None, None],
                                              [None, None, None, None, None, None, None],
                                              [None, None, None, None, None, None, None]]
                                    game_vars['gold'] = 10
                                    game_vars['turn'] = 0
                                    game_vars['monster_kill_target'] = 20
                                    monster_kill['killed'] = 0
                                    monster_kill['danger'] = 1
                                    monster_kill['danger_bar'] = 0
                                    letters = []
                                    for i in range(ord('a'), ord('z')+1-26+len(field)):
                                        letters.append(chr(i).upper())
                                    print('Returning to main menu')
                                    for i in range(len(field)):
                                        total_friendly_damage.append(0)
                                        total_monster_damage.append(0)
                                    break
                                else:
                                    print('Please input a valid answer')
                            except Exception:
                                print('Please input a valid answer')
                        break
                                          
                        
                    else:
                        print('Please input a valid answer')
                except Exception:
                    print('Please give a valid answer')
            
        if game == 4 :
            stop_game = True
            break
        elif game == 5 :
            control = False
            loop =  False
            check = False
            break
        elif end_game == True:
            break
        else:
            monster_advance(monster_list, field ,total_friendly_damage)                            
            defender_attack(field)
            
            game_vars['turn'] += 1
            game_vars['gold'] += 1
            if game_vars['monster_kill_target'] == monster_kill['killed']:
                loop = True
                control = True
                print('You beat the game!')
                break




















    

    
    
