
# Parent Class
class Player:
    name = input('Name: ')
    a_button = 'jump'
    b_button ='special'
    lives = 3
    # Parent Class Method   
    def mission(save):            
        save = input('\ncan you rescue the princess Y/N\n>>>').lower()
        if save == 'y':
            print('\n\nYou saved the princess!')
        if save == 'n':
            print ('\n\nGame Over')
            
        


# Child Class
class Mario(Player):
    player_1 = True
    color = 'red'
    b_button = 'fireball'

    # Child Method
    def mission(save):            
        save = input('\ncan you rescue the princess Y/N\n>>>').lower()
        if save == 'y':
            print('Thanks ' + Player(name) + '\n\nYou saved the princess!')
        if save == 'n':
            print ('\n\nGame Over')


# Child Class
class Luigi(Player):
    player_2 = True
    color = 'green'
    b_button = 'extra jump'

    # Child Method
    def mission(save):            
        save = input('\ncan you rescue the princess Y/N\n>>>').lower()
        if save == 'y':
            print('Congratulations ' + Player(name) + '\n\nYou saved the princess!')
        if save == 'n':
            print ('\n\nGame Over')
    


# This gets the method going
Player.mission('save')

