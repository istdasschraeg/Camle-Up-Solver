

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
    def __init__(self,color1):
        self.color= color1
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
    c1 = camel("red")
    c2 = camel ("green") 
    c3 =camel ("yellow")
    c4 = camel ("white")
    c5 =camel ("black")
    camle_list= [cred, cgreen, cyellow, cblack, cwhite]
    dice_list = [dred, dgreen, dyellow, dblack, dwhite]   
    Not_pyramide =[]
    def  __init__(self): 
        pass
    def move(self,camel,moves):
        new_field=camel.field + int(moves) 
        for camle in self.camle_list:
            if camle.field == new_field:
                camel.position +=1

        camel.field = new_field
    
    def produce_dice(self):
        current_dice  = random.choice(self.dice_list)
        
        self.Not_pyramide.append(current_dice)
        return current_dice.colour

    def take_initial_input (self):
        for camel in self.camle_list:
            camel_color=input(f"What camle was rolled?") 
            roll= input("Roll:")
            self.move(self.take_color_return_object(camel_color),roll)  

    
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
           
    def change_field (self,camel_color,field):
        self.take_color_return_object(camel_color).field=field  #does not work with  position ignores it 
    
    def save_current_position(self):
        file1 = open("save.txt","r+")
        for camel in self.camle_list:
            file1.write(camel.name+"\n")
            file1.write(camel.position+"\n")
            file1.write(camel.color+"\n")
            file1.write(camel.name+"\n")
            file1.write(camel.field+"\n")

    def load_safe(self):
        file1 = open("save.txt","r+")
        for i in 25:
            c1= camel (file1.readline(1))
            

    def run(self):

        for i in 5 :
            self.produce_dice()
            wurf = random.randint(1-6) 
            self.move(self.take_color_return_object(self.current_dice.colour()),wurf)
        self.give_all_poistions()


game =pyramide()

game.take_initial_input()
game.give_all_poistions()




