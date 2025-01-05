

import random
import time
class dice:
    name=""
    
    
    def __init__(self,name1,colour1):
        self.name= name1
        self.colour= colour1
        pass

    def roll(self):
        self.wurf = random.randint(1,3) 
        #print (self.wurf)

class camel:
    name=""
    def __init__(self,color1,position1,field1):
        self.color= color1
        self.position=position1
        self.field=field1
        pass

    def roll(self):
        self.wurf = random.randint(1,6) 
        #print (self.wurf)

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

        self.list_plus_one_fields=[]
        self.list_minus_one_fields=[]
        
        pass 
 

    def move(self,camel,moves):
        new_field=self.new_field(camel,moves)
        camels_on_field= self.camels_on_same_field(camel.field)
        is_minus_field= self.see_if_it_is_minus_field(new_field)       
        if is_minus_field :
            for camel in self.camels_on_same_field(new_field):
                camels_on_field.append(camel) 
        self.move_all_camels_to_new_field(camels_on_field,new_field)

    def see_if_it_is_minus_field(self,field):
        for tested_field in self.list_minus_one_fields:   
            if field == tested_field:
                return True
        return False

    def new_field(self,camel,moves):
        new_field=camel.field + int(moves) 
        for field in self.list_plus_one_fields:
            if new_field == field:
                new_field+=1
        for field in self.list_minus_one_fields:
            if new_field == field:
                new_field-=1
        return new_field

    def camels_on_same_field (self,field):
        camels_on_field = [c for c in self.camle_list if c.field == field ] #and camel.position<c.position
        camels_on_field.sort(key=lambda camel: camel.position)
        return camels_on_field

    def move_all_camels_to_new_field(self,list_camels,new_field):
        new_poition=len(list_camels) 
        list_camels.sort(key=lambda camel: -camel.position)
        for i in range(len(list_camels)):          
            camels_on_field_new = [c for c in self.camle_list if c.field == new_field]
            new_poition=len(camels_on_field_new) 
            list_camels[i].field = new_field
            list_camels[i].position= new_poition        
    
    def produce_dice(self):
        #print("Dice List:", len(self.dice_list))
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
        for dice in range(5) :
            wurf = random.randint(1,3)
            self.move(self.take_color_return_object(self.produce_dice()),wurf)
        self.dice_list = [self.dred, self.dgreen, self.dyellow, self.dblack, self.dwhite] 
        #self.give_all_poistions()

    def calculate_probability(self):
        times=10000    #Adjust number of times U want to the programm to simulate outcomes of ur position (recommended 10000 in ca. 2,3s)
        list_of_colors=["red","yellow","green","white","black"]

        counters= {f"{color}_{place}":0 for color in list_of_colors for place in range(5)}

        start=time.time() 
 
        for i in range(times):

            self.run()
            self.sort_for_best()  
            for place in range (5):
                for color in list_of_colors:
                    if self.camle_list[place].color== color:
                        counters [f"{color}_{place}" ]+=1 
            
            self.load_safe()

        place_list=["First","Second","Third","Fourth","Fived"] #
        for place in range (5):
            print("") 
            print("")
            print (f"Probability of {place_list[place]} Place")
            for color in list_of_colors:
                count =counters[f"{color}_{place}"]/times 
                print (f"{color}:",round(count,2)*100,"%",end=" ")

        end= time.time()
        print("")
        print("Calculated in",(end-start),"seconds") 

    def sort_for_best(self): 
        self.camle_list.sort(key=lambda camel: (-camel.field, camel.position))   

game =pyramide()
#game.take_initial_input()
#game.save_current_position()  
#game.load_safe()
#game.give_all_poistions()
#game.save_current_position()
#game.run()
#game.sort_for_best()
game.calculate_probability()
