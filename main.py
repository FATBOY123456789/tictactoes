theboard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '}

board_keys=[]

for keys in theboard:
    board_keys.append(keys)

def Printboard(board):
    print(board['7']+'|', board['8']+'|', board['9']+'|')
    print('-+-+-')
    print(board['4']+'|', board['5']+'|', board['6']+'|')
    print('-+-+-')    
    print(board['1']+'|', board['2']+'|', board['3']+'|')


def game():
    turn='X'
    count=0
    for i in range(10):
        Printboard(theboard)
        print('its your turn,',turn,'choose a place to move')
        move=input()
        if theboard[move]==' ':
            theboard[move] = turn
            count+=1
        else:
            print('oops invalid move, space is already filled, choose an empty space.')
            continue
        if count >= 5:
            if theboard['7']==theboard['8']==theboard['9']!=' ':
                print('game over')
                print(turn,'won')
                break
            elif theboard['4']==theboard['5']==theboard['6']!=' ':
                print('game over')
                print(turn,'won')
                break
            elif theboard['1']==theboard['2']==theboard['3']!=' ':
                print('game over')
                print(turn,'won')
                break        
            elif theboard['1']==theboard['4']==theboard['7']!=' ':
                print('game over')
                print(turn,'won')
                break
            elif theboard['3']==theboard['6']==theboard['9']!=' ':
                print('game over')
                print(turn,'won')
                break
            elif theboard['2']==theboard['5']==theboard['8']!=' ':
                print('game over')
                print(turn,'won')
                break
            elif theboard['7']==theboard['5']==theboard['3']!=' ':
                print('game over')
                print(turn,'won')
                break
            elif theboard['1']==theboard['5']==theboard['9']!=' ':
                print('game over')
                print(turn,'won')
                break
        if count==9:
         print('game over')
         print('its a tie :(')
        if turn=='X':
         turn='O'
        else:
         turn='X'

    restart=input('do you want to restart? y or n: ')
    if restart=='Y' or restart=='y':
     for key in board_keys:
        theboard[key]=' '
     game()

game()
