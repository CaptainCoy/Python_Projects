from abc import ABC, abstractmethod  # Imporing abstract method
class jump(ABC):  # Building the jump class
    def sendIt(self, trick):  # Creating the sendIt function
        print("You sent a {}, crazy".format(trick))
# This function allows us to pass in an argument where we don't know the data type yet
    @abstractmethod
    def air(self, trick):
        pass

class sickMove(jump):
    # Here we decide what we are doing off the jump
    def air(self,trick):
        print("throw your head back, spot your landing, follow through, stomp, ride away.  {}s are easy peasy".format(trick))

obj = sickMove()
obj.sendIt('backflip')
obj.air('backflip')
