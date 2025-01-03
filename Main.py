

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
        self.wurf = random.randint(1,3) 
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

        if not camel.position== 0:
                new_poition=0
                new_field=0
                new_field=camel.field + int(moves) 
                camels_on_field = [c for c in self.camle_list if c.field == new_field]
                camels_on_field.sort(key=lambda camel: camel.position)
                for camle in camels_on_field:
                    camels_on_field_new = [c for c in self.camle_list if c.field == new_field]
                    print(len(camels_on_field_new))
                    new_poition=len(camels_on_field_new) 
                    print (new_field)
                    camle.field = new_field
                    camle.position= new_poition
        
        else:
            new_poition=0
            new_field=0
            new_field=camel.field + int(moves) 
            camels_on_field = [c for c in self.camle_list if c.field == new_field]
            print(len(camels_on_field))
            new_poition=len(camels_on_field) 
            print (new_field)
            camel.field = new_field
            camel.position= new_poition  
    
    def produce_dice(self):
        current_dice  = random.choice(self.dice_list)
        current_dice1 =current_dice
        self.dice_list.remove(current_dice)
        self.Not_pyramide.append(current_dice)
        return current_dice1.colour

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

        for dice in self.dice_list :
            print ("lol")
            wurf = random.randint(1,3)
            print(wurf) 
            print(self.produce_dice())
            self.move(self.take_color_return_object(self.produce_dice()),wurf)
        self.dice_list = [self.dred, self.dgreen, self.dyellow, self.dblack, self.dwhite] 
        self.give_all_poistions()

    def calculate_probability(self):
        times=10
        red_1 =0;red_2 =0; red_3 =0;red_4 =0;red_5 =0
        green_1= 0;green_2= 0;green_3= 0;green_4= 0;green_5= 0
        yellow_1=0;yellow_2=0;yellow_3=0;yellow_4=0;yellow_5=0
        white_1=0;white_2=0;white_3=0;white_4=0;white_5=0
        black_1=0; black_2=0; black_3=0; black_4=0; black_5=0

        for i in range(times):
            self.run()
            self.sort_for_best()
            if self.camle_list[0].color == "red":
                red_1+=1
            elif self.camle_list[0].color == "yellow":
                yellow_1+=1
            elif self.camle_list[0].color == "green":
                green_1+=1
            elif self.camle_list[0].color == "white":
                white_1+=1
            elif self.camle_list[0].color == "black":
                black_1+=1
            if self.camle_list[1].color == "red":
                red_2+=1
            elif self.camle_list[1].color == "yellow":
                yellow_2+=1
            elif self.camle_list[1].color == "green":
                green_2+=1
            elif self.camle_list[1].color == "white":
                white_2+=1
            elif self.camle_list[1].color == "black":
                black_2+=1
            if self.camle_list[2].color == "red":
                red_3+=1
            elif self.camle_list[2].color == "yellow":
                yellow_3+=1
            elif self.camle_list[2].color == "green":
                green_3+=1
            elif self.camle_list[2].color == "white":
                white_3+=1
            elif self.camle_list[2].color == "black":
                black_3+=1
            if self.camle_list[3].color == "red":
                red_4+=1
            elif self.camle_list[3].color == "yellow":
                yellow_4+=1
            elif self.camle_list[3].color == "green":
                green_4+=1
            elif self.camle_list[3].color == "white":
                white_4+=1
            elif self.camle_list[3].color == "black":
                black_4+=1
            if self.camle_list[4].color == "red":
                red_5+=1
            elif self.camle_list[4].color == "yellow":
                yellow_5+=1
            elif self.camle_list[4].color == "green":
                green_5+=1
            elif self.camle_list[4].color == "white":
                white_5+=1
            elif self.camle_list[4].color == "black":
                black_5+=1

            self.load_safe()

            
            times +=1

        print()



    def sort_for_best(self):
        self.camle_list.sort(key=lambda camel: (-camel.field, camel.position)) 
        
    
    


game =pyramide()

#game.take_initial_input()
game.load_safe()
#game.give_all_poistions()
#game.save_current_position()
game.run()
game.sort_for_best()
#game.calculate_probability()


