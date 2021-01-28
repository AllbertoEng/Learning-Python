import os

def playerx_o():
    global player1
    global player2
    player1 = "placeholder"
    
    while player1 not in ['X','O']:
        player1 = input("Player 1: do you want to be X or O? ")  
        
        if player1 not in ['X','O']:
            print("Choose X or O only.")
            
    if player1 == 'X':
        player2 = 'O'
    else:
        player2='X'
        

        
    print("Player 1 will go first.")

def ready():
    ready = 'YesNo'
    
    while ready not in ['Yes']:
        ready = input('Are you ready to play? Enter Yes or No: ')
        
        if ready not in ['Yes', 'No']:
            print('Yes or no?')           

positions = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

def board(positions):
    print(f" {positions['1']} | {positions['2']} | {positions['3']}")
    print(f"-----------")
    print(f" {positions['4']} | {positions['5']} | {positions['6']}")
    print(f"-----------")
    print(f" {positions['7']} | {positions['8']} | {positions['9']}")
    
def choises():
    vic_x = False
    vic_o = False
    choise = '11'
    choise2 = '11'
    positions = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
    valid_positions = ['1','2','3','4','5','6','7','8','9']
    
    while not vic_x and not vic_o:       
        choise = '11'
        choise2 = '11'
                        
        while choise not in valid_positions:
       
            choise = input('Choose your next position: (1-9) ')
            if choise not in valid_positions:
                print('Choose: '+" ".join(valid_positions))
                
        positions[choise] = player1
        valid_positions.remove(choise)
        
        os.system('cls')
        
        board(positions)
        
        if positions['1']=='X' and positions['2']=='X' and positions['3']=='X':
            vic_x = True
        elif positions['4']=='X' and positions['5']=='X' and positions['6']=='X':
            vic_x = True
        elif positions['7']=='X' and positions['8']=='X' and positions['9']=='X':
            vic_x = True
        elif positions['1']=='X' and positions['4']=='X' and positions['7']=='X':
            vic_x = True
        elif positions['2']=='X' and positions['5']=='X' and positions['8']=='X':
            vic_x = True
        elif positions['3']=='X' and positions['6']=='X' and positions['9']=='X':
            vic_x = True
        elif positions['1']=='X' and positions['5']=='X' and positions['9']=='X':
            vic_x = True
        elif positions['7']=='X' and positions['5']=='X' and positions['3']=='X':
            vic_x = True
        else:
            vic_x = False
        
        if vic_o or vic_x:
            break
            
        if len(valid_positions) == 0:
            break
        
        while choise2 not in valid_positions:
        
            choise2 = input('Choose your next position: (1-9) ')
            if choise2 not in valid_positions:
                print('Choose: '+" ".join(valid_positions))
        
        positions[choise2] = player2
        valid_positions.remove(choise2)
        
        
        os.system('cls')
        
        board(positions)
        
        if positions['1']=='O' and positions['2']=='O' and positions['3']=='O':
            vic_o = True
        elif positions['4']=='O' and positions['5']=='O' and positions['6']=='O':
            vic_o = True
        elif positions['7']=='O' and positions['8']=='O' and positions['9']=='O':
            vic_o = True
        elif positions['1']=='O' and positions['4']=='O' and positions['7']=='O':
            vic_o = True
        elif positions['2']=='O' and positions['5']=='O' and positions['8']=='O':
            vic_o = True
        elif positions['3']=='O' and positions['6']=='O' and positions['9']=='O':
            vic_o = True
        elif positions['1']=='O' and positions['5']=='O' and positions['9']=='O':
            vic_o = True
        elif positions['7']=='O' and positions['5']=='O' and positions['3']=='O':
            vic_o = True
        else:
            vic_o = False
            
    if vic_x:
        print('Congratulations Player 1 you won the game!')
    elif vic_o: 
        print('Congratulations Player 2 you won the game!')
    elif len(valid_positions) == 0:
        print("Thats a drawn!")

def repl():
    global replay
       
    replay = 'YESNO'
    while replay not in ['Yes', 'No']:
        replay = input('Do you want to play again? Enter Yes or No:')
        
        if replay not in ['Yes', 'No']:
            print('Enter "Yes" or "No"')
            
    if replay == 'Yes':
        replay = True
    else:
        replay = False     

replay = True

while replay:
       
    playerx_o()
    
    ready()
    
    board(positions)
        
    choises()
    
    repl()
        
    os.system('cls')                                        