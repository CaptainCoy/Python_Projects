#
#  Python: 3.10.1
#
#
#  Author: Alex Coy
#
#
#  Purpose: The Tech Academy - Python Course,  Creating a game assignment.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#



def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new game, get user's name.
        if it isn't, thank the player for playing again and continue
    """
    # meaning if we do not already have this user's name
    # then they are a new player and we need their info

    if name != "":
        print ("\nThank you for playing again, {}.".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat's your name fool? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game you will be greeted \nby several different people. \nIt's up to you if you want to be nice or mean.")
                    print("At the end of the game your fate will be determined by \nyour actions.")
                    stop = False
        return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? \n(N/M) \n>>> ").lower()
        if pick == "n":
            print ("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares menacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current score: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the value stored within the 3 variables
    if nice > 2: # if condition is valid, call win function and pass in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # same as above comment, but for lose function
        lose(nice,mean,name)
    else: # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # wildcards {} substitute variable values
    print("\n\nNicely done {}, you're a real sweetheart. \nEverybody loves you!".format(name))
    #call again function and pass along variables
    again(nice,mean,name)


def lose(nice,mean,name):
    # similar to win comment
    print("\n\nMan {}, you're a dick".format(name))
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\n\nDo you want to give it another whirl? \n(Y/N) \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nUntil next time...")
            stop = False
            quit()

        else:
            print("\nWhat's it going to be? \n(Y/N) \n>>>")

            

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # notice, we don't need to reset the name variable
    start(nice,mean,name)
        












if __name__ == "__main__":
    start()
