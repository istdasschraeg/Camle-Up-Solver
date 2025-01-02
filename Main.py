

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
    def __init__(self,color1,position1,field1):
        self.color= color1
        self.position=position1
        self.field=field1
        pass

    def roll(self):
        self.wurf = random.randint(1-6) 
        print (self.wurf)

class pyramide:

    
    
    def  __init__(self): 
        self.dred = dice("1","red")
        self.dgreen = dice ("2","green")
        self.dyellow =dice ("3","yellow")
        self.dwhite = dice ("4","white")
        self.dblack =dice ("5","black")
        self.c1 = camel("red",0,0)
        self.c2 = camel ("green",0,0) 
        self.c3 =camel ("yellow",0,0)
        self.c4 = camel ("white",0,0)
        self.c5 =camel ("black",0,0)
        self.camle_list= [self.c1, self.c2, self.c3, self.c4, self.c5]
        self.dice_list = [self.dred, self.dgreen, self.dyellow, self.dblack, self.dwhite]   
        self.Not_pyramide =[]
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
            print(camel.name,"Position:",camel.position, "Color:",camel.color, "Field:", camel.field)            
           
    def change_field (self,camel_color,field):
        self.take_color_return_object(camel_color).field=field  #does not work with  position ignores it 
    
    def save_current_position(self):
        file1 = open("save.txt","r+")
        for camel in self.camle_list:
            file1.write(camel.color.strip()+"\n")
            file1.write(str(camel.position)+"\n")
            file1.write(str(camel.field)+"\n")

    def load_safe(self):
            
        file1 = open("save.txt","r+") 
        save=file1.readlines()
        self.camle_list=[]
        del self.c1 ,self.c2, self.c3, self.c4, self.c5
        self.c1= camel (save[0].replace("\n",""),int(save[1]),int(save[2])) 
        self.c2= camel (save[3].replace("\n",""),int(save[4]),int(save[5])) 
        self.c3= camel (save[6].replace("\n",""),int(save[7]),int(save[8])) 
        self.c4= camel (save[9].replace("\n",""),int(save[10]),int(save[11])) 
        self.c5= camel (save[12].replace("\n",""),int(save[13]),int(save[14])) 
        self.camle_list= [self.c1, self.c2, self.c3, self.c4, self.c5]
        
            

    def run(self):

        for i in 5 :
            self.produce_dice()
            wurf = random.randint(1-6) 
            self.move(self.take_color_return_object(self.current_dice.colour()),wurf)
        self.give_all_poistions()


game =pyramide()

game.load_safe()
#game.take_initial_input()
game.give_all_poistions()
game.save_current_position()




