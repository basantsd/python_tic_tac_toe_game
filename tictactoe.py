'''
The tic tac toe project code
'''
def runtic():
    '''
    First Define Player1 and Player2
    '''
    player1 = ''
    player2 = ''
    print("First Choose Player 1")
    '''
    loop for player selection (X) or (O)
    '''
    while True:
        player1 = input('Please Choose X or O : ').upper()
        if player1 == 'X':
            player2 = 'O'
            break
        elif player1 == 'O':
            player2 = 'X'
            break
        else:
            print('Note : Please Choose X or O ')
            continue
    '''
    Section (X) or (O) loop End
    '''

    ticdict = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    # print dictionary for with blank values
    def printtic():
        print(ticdict[1] + ' | ' + ticdict[2] + ' | ' + ticdict[3])
        print(ticdict[4] + ' | ' + ticdict[5] + ' | ' + ticdict[6])
        print(ticdict[7] + ' | ' + ticdict[8] + ' | ' + ticdict[9])
    '''
    for player 1 and 2 turn boolean value for loop
    '''
    player_one_turn = True
    player_two_turn = False
    loop_run = True
    check_empty = [i for i in ticdict.values()]
    '''
    Main Loop ----> Players Entery
    '''
    while loop_run:
        '''
        Player 1 loop
        '''
        while player_one_turn:
            try:
                val = int(input(f'Player1 Select 0 to 9 index for {player1} : '))
                if val in range(1, 10) and ticdict[val] == ' ':
                    ticdict[val] = player1
                    printtic()
                    player_one_turn = False
                    player_two_turn = True
                    if (ticdict[1] == player1 and ticdict[2] == player1 and ticdict[3] == player1) or (
                    ticdict[4] == player1 and ticdict[5] == player1 and ticdict[6] == player1) or (
                    ticdict[7] == player1 and ticdict[8] == player1 and ticdict[9] == player1) or (
                    ticdict[1] == player1 and ticdict[4] == player1 and ticdict[7] == player1) or (
                    ticdict[2] == player1 and ticdict[5] == player1 and ticdict[8] == player1) or (
                    ticdict[3] == player1 and ticdict[6] == player1 and ticdict[9] == player1) or (
                    ticdict[1] == player1 and ticdict[5] == player1 and ticdict[9] == player1) or (
                    ticdict[3] == player1 and ticdict[5] == player1 and ticdict[7] == player1):
                        print('Player 1 Win !!!!')
                        player_two_turn = False
                        player_one_turn = False
                        loop_run = False
                    else:
                        pass
                else:
                    print('Warning : Your selected index is already fill !!!')
                    player_one_turn = True
            except ValueError:
                print('Note : Please enter 0 to 9 number only')
                player_one_turn = True
            except:
                pass
            check_empty = [i for i in ticdict.values()]
            if not ' ' in check_empty :
                # or you can do this -----> ticdict[1] != ' ' and ticdict[2] != ' ' and ticdict[3] != ' ' and ticdict[4] != ' ' and ticdict[5] != ' ' and ticdict[6] != ' ' and ticdict[7] != ' ' and ticdict[8] != ' ' and ticdict[9] != ' ':
                print('Draw No one Win !!!')
                player_two_turn = False
                player_one_turn = False
                loop_run = False
            else:
                pass
            '''
            Player 1 loop End
            '''
        else:
            
            if player_two_turn == True:
                try:
                    val = int(input(f'Player2 Select 0 to 9 index for {player2} : '))
                    if val in range(1, 10) and ticdict[val] == ' ':
                        ticdict[val] = player2
                        printtic()
                        player_one_turn = True
                        if (ticdict[1] == player2 and ticdict[2] == player2 and ticdict[3] == player2) or (
                        ticdict[4] == player2 and ticdict[5] == player2 and ticdict[6] == player2) or (
                        ticdict[7] == player2 and ticdict[8] == player2 and ticdict[9] == player2) or (
                        ticdict[1] == player2 and ticdict[4] == player2 and ticdict[7] == player2) or (
                        ticdict[2] == player2 and ticdict[5] == player2 and ticdict[8] == player2) or (
                        ticdict[3] == player2 and ticdict[6] == player2 and ticdict[9] == player2) or (
                        ticdict[1] == player2 and ticdict[5] == player2 and ticdict[9] == player2) or (
                        ticdict[3] == player2 and ticdict[5] == player2 and ticdict[7] == player2):
                            print('Player 2 win !!!')
                            player_two_turn = False
                            player_one_turn = False
                            loop_run = False
                        else:
                            pass
                    else:
                        print('Warning : Your selected index is already fill !!!')
                        player_one_turn = False
                except ValueError:
                    print('Note : Please enter 0 to 9 number only')
                    player_one_turn = False
                except:
                    pass
            
            else:
                pass
            if not ' ' in check_empty :
                # or you can do this -----> ticdict[1] != ' ' and ticdict[2] != ' ' and ticdict[3] != ' ' and ticdict[4] != ' ' and ticdict[5] != ' ' and ticdict[6] != ' ' and ticdict[7] != ' ' and ticdict[8] != ' ' and ticdict[9] != ' ':
                print('Draw No one Win !!!')
                player_two_turn = False
                player_one_turn = False
                loop_run = False
            else:
                pass
    # Main loop End
    else:
        '''
        Loop for Asking Play again or Exit
        '''
        while True:
            inp = input("Press 'q' for (q : quit) and 'r' to (r :play again) : ").lower()
            if inp == 'q':
                print("Game End \nThank's Players !! To join")
                break
            elif inp == 'r':
                runtic()
            else:
                print('Note : Enter q and r only')
                continue
          
runtic()

    
