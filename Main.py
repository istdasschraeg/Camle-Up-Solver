

# Soll wahrscheinlichkeit von würfeln aus der Pyramide erechen 

#soll den besten Zug finden

#braucht Input für die würfel

#Spielfeld nachmachen

#input system für das spiel

import random
class dice:
    name=""
    
    
    def __init__(self,name1,colour1):
        self.name= name1
        self.colour= colour1
        pass

    def roll(self):
        self.wurf = random.randint(1-6) 
        print (self.wurf)

class camel:
    name=""
    position=1
    field=0  
    def __init__(self,colour1):
        self.colour= colour1
        pass

    def roll(self):
        self.wurf = random.randint(1-6) 
        print (self.wurf)

class pyramide:

    
    dred = dice("1","red")
    dgreen = dice ("2","green")
    dyellow =dice ("3","yellow")
    dwhite = dice ("4","white")
    dblack =dice ("5","black")
    cred = dice("red")
    cgreen = dice ("green")
    cyellow =dice ("yellow")
    cwhite = dice ("white")
    cblack =dice ("black")
    camle_list= [cred, cgreen, cyellow, cblack, cwhite]
    dice_list = [dred, dgreen, dyellow, dblack, dwhite]
    Not_pyramide =[]
    def  __init__(self):
        pass
    def move(self,camel,moves):
        new_field=camel.field + moves 
        for camle in self.camle_list:
            if camle.field == new_field:
                camel.position +=1

        camel.field = new_field
    
    def produce_dice(self):
        current_dice  = random.choice(self.dice_list)
        print(current_dice.colour)
        self.Not_pyramide.append(current_dice)

    def take_initial_input (self):
        camel=input(f"What camle was rolled first?") #camel color
        roll= input("Roll:")
        self.move(camel,roll)  
    
    def take_color_return_object(self,color):
        match color:
            case "red":
                return self.camle_list[0]
            case "green":
                return self.camle_list[1]
            case "yellow":
                return self.camle_list[2]
            case "white":
                return self.camle_list[3]
            case "black":
                return self.camle_list[4]

    def give_all_poistions(self):
        for camel in self.camle_list:
            print(camel.name,"Position:",camel.position, "Color:",camel.color)            
           
    def change_position (self,camel,poistion):


    take_initial_input()

main_Pyramide = pyramide()


