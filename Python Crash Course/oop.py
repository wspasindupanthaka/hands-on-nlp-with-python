# -*- coding: utf-8 -*-

class Fish:
    
    #Self is the reference of the same object
    def swim(self):
        print("Fish Swimming")
        
    def eat(self):
        print("Fish Eating")
        
        
fish = Fish()
fish.swim()
fish.eat()




#Override constructor
class Game:
    
    def __init__(self,name):
        self.name = name
        
    def start(self):
        print(self.name,"has started")
        
    def end(self):
        print(self.name,"has ended")


game = Game("Farcry 3")
game.start()
game.end()