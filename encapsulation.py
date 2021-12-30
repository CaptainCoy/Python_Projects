# Creating a class
class deepThought(object):
    def __init__(self):  # Defining the protected variable
        self._protectedVar = 0

    def getTowel(self):  # Defining private variables
        print(self.__privateVar)

    def setTowel(self, dolphin):
        self.__privateVar = dolphin
        
answer = deepThought()  # naming the variable
answer._protectedVar = 42 # Setting the variable value
answer.setTowel("So long and thanks for all the fish...")
answer.getTowel()
print("The answer to life the universe and everything is {}".format(answer._protectedVar))
