

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
        self.dorange = dice("1","orange")
        self.dgreen = dice ("2","green")
        self.dyellow =dice ("3","yellow")
        self.dwhite = dice ("4","white")
        self.dblue =dice ("5","blue")
        self.c1 = camel("orange",0,0)
        self.c2 = camel ("green",0,0) 
        self.c3 =camel ("yellow",0,0)
        self.c4 = camel ("white",0,0)
        self.c5 =camel ("blue",0,0)
        self.camle_list= [self.c1, self.c2, self.c3, self.c4, self.c5]
        self.dice_list = [self.dorange, self.dgreen, self.dyellow, self.dblue, self.dwhite]   
        self.Not_pyramide =[]

        self.list_plus_one_fields=[]
        self.list_minus_one_fields=[]
        self.list_potential_fields=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

        self.portfolio = {"orange": 5, "green": 5}  # Example portfolio with values

        #remove all already down cards and also adjacent fields

        self.placements={f"{place+1}":0 for place in range(16)}
        
        pass 
 

    def move(self,camel,moves):
        new_field=self.new_field(camel,moves)
        camels_on_field= self.camels_above(camel)
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

        for field in self.list_potential_fields:
            if new_field == field:
                self.placements[f"{field}"]+=1
                

        return new_field

    def camels_on_same_field (self,field):
            return sorted([c for c in self.camle_list if c.field == field], key=lambda camel: camel.position) #and camel.position<c.position

    def camels_above(self,camel):
        return sorted([c for c in self.camle_list if c.field == camel.field and camel.position<=c.position], key=lambda camel: camel.position)

    def move_all_camels_to_new_field(self,list_camels,new_field):
        list_camels.sort(key=lambda camel: camel.position) 
        #for c in list_camels:
            #print ("Camel Positions:",c.color)
        for i in range(len(list_camels)):               
            for i, camel in enumerate(list_camels):
                camel.field = new_field
                
                camel.position = len([c for c in self.camle_list if c.field == new_field]) + i-1     
     
    def produce_dice(self):
        #print("Dice List:", len(self.dice_list))
        current_dice  = random.choice(self.dice_list)
        self.dice_list.remove(current_dice)
        return current_dice.colour

    def take_initial_input (self):  
        for camel in self.camle_list:
            camel_color=input(f"What camle was rolled?") 
            roll= input("Roll:")
            self.move(self.take_color_return_object(camel_color),roll)  
        input=input("Do any more fields have plus cards?y/n")
        while  input== "y":
            self.list_minus_one_fields.append(input("What field have plus cards on them"))
            input=input("Do any more fields have plus cards?y/n")
        input=input("Do any more fields have minus cards?y/n")
        while  input== "y":
            self.list_minus_one_fields.append(input("What field have minus cards on them"))
            input=input("Do any more fields have minus cards?y/n")
        
  
    def take_color_return_object(self,color):
        match color:
            case "orange":
                return self.camle_list[0]
            case "green":
                return self.camle_list[1]
            case "yellow":
                return self.camle_list[2] 
            case "white":
                return self.camle_list[3]
            case "blue":
                return self.camle_list[4]

    def give_all_poistions(self):
        for camel in self.camle_list:
            print(camel.name,"Position:",camel.position, "Color:",camel.color, "Field:", camel.field)            
    
    def save_current_position(self): #safes by writing down the attributes of all 5 camels in the order off: color position field
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
        self.give_all_poistions
         
    def run(self): #runs a single gameturn 
        
        for dice in range(5) :
            wurf = random.randint(1,3)
            
            color= self.produce_dice()
            #print ("Wurf",wurf,"color",color)
            self.move(self.take_color_return_object(color),wurf)
        self.dice_list = [self.dorange, self.dgreen, self.dyellow, self.dblue, self.dwhite] 
        #self.give_all_poistions()

    def calculate_probability(self,times):    
        # runs the turn a number of times and uses that data to calculate the liklyhood of any given result
           #Adjust number of times U want to the programm to simulate outcomes of ur position (recommended 10000 in ca. 2,3s)
        list_of_colors=["orange","yellow","green","white","blue"] 

        counters= {f"{color}_{place}":0 for color in list_of_colors for place in range(5)} #initialises varibales for storing the results 

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
                print (f"{color}:",round(count*100,2),"%",end=" ")

        end= time.time()
        print("")
        print("Calculated in",(end-start),"seconds") 

    def sort_for_best(self): 
        self.camle_list.sort(key=lambda camel: (-camel.field, camel.position))     


    def calculate_best_turn(self,times):
        # runs the turn a number of times and uses that data to calculate the liklyhood of any given result
           #Adjust number of times U want to the programm to simulate outcomes of ur position (recommended 10000 in ca. 2,3s)
        list_of_colors=["orange","yellow","green","white","blue"] 

        counters= {f"{color}_{place}":0 for color in list_of_colors for place in range(5)} #initialises varibales for storing the results 

        start=time.time() 
        cardvalue= {"orange":5,"yellow":5,"green":5,"white":5,"blue":5}
        expected_value = {"orange":0,"yellow":0,"green":0,"white":0,"blue":0,"card":0}
        self.check_possible_fields()
 
        for i in range(times):
            

            self.run()
            self.sort_for_best()  
            for place in range (5):
                for color in list_of_colors:
                    if self.camle_list[place].color== color:
                        counters [f"{color}_{place}" ]+=1  
            
            self.load_safe()

        for f in range(16):
            if not self.placements[f"{f+1}"]==0: 
                self.placements[f"{f+1}"] = self.placements[f"{f+1}"]/times
                #print(self.placements[f"{f+1}"]/times)
                
        max_key = max(self.placements, key=self.placements.get)

        expected_value["card"] = self.placements[max_key]

        print(expected_value["card"], "per turn value on field:", max_key)
        
        for color in list_of_colors:
            probability_1 =counters[f"{color}_0"]/times
            probability_2 = counters[f"{color}_1"]/times
            probability_345= counters[f"{color}_2"]/times + counters[f"{color}_3"]/times +counters[f"{color}_4"]/times
            expected_outcome= probability_1* cardvalue[f"{color}"] + probability_2 *1 + probability_345 *-1
            if expected_outcome >= 1:
                expected_value[color]= expected_outcome
                print(f"Expected Value of highest card {color}", round(expected_outcome,2) )

        end= time.time()
        print("")
        print("Calculated in",(end-start),"seconds") 

    def check_possible_fields(self):
        unavailable_fields=[]

        for f in self.list_minus_one_fields:
            unavailable_fields.append(f,f+1,f-1)

        for f in self.list_plus_one_fields:
            unavailable_fields.append(f,f+1,f-1)
        
        for c in self.camle_list:
            unavailable_fields.append(c.field)

        self.list_potential_fields = [f for f in self.list_potential_fields if f not in unavailable_fields]
        #print(*self.list_potential_fields)   




                




game =pyramide()
#game.take_initial_input()
#game.save_current_position()  
game.load_safe()
#game.give_all_poistions()
#game.save_current_position()
#game.run() 
#game.give_all_poistions()
#game.sort_for_best()
#game.calculate_probability(10000) #sooo  
game.calculate_best_turn(100000) 
