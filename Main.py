

import random
import time
class dice:  # Simulates a dice in the game
    name=""  # Stores the name of the dice
    
    def __init__(self,name1,colour1):  
        self.name= name1  # Dice's name
        self.colour= colour1  # Dice's collor

    def roll(self):  
        self.wurf = random.randint(1,3)  # Rolls a random numbr between 1 and 3

class camel:  # Defines the cammel objects in the game
    name=""  # Holds the camel name which i than deceid to never use
    
    def __init__(self,color1,position1,field1):  
        self.color= color1  # Assigns the camel's colur
        self.position=position1  # Stores the position on the board
        self.field=field1  # Tracks what feild the camel is in
        

    def roll(self):  
        self.wurf = random.randint(1,6)  # Rolls dice for the camel with 1-6 values

class pyramide:  # The main class to handel the game logic
    def  __init__(self): 
        # Create dice with diffrent colors
        self.dorange = dice("1","orange")
        self.dgreen = dice ("2","green")
        self.dyellow =dice ("3","yellow")
        self.dwhite = dice ("4","white")
        self.dblue =dice ("5","blue")
        
        # Creats camles with initial fields and positions
        self.c1 = camel("orange",0,0)
        self.c2 = camel ("green",0,0) 
        self.c3 =camel ("yellow",0,0)
        self.c4 = camel ("white",0,0)
        self.c5 =camel ("blue",0,0)
        
        # Lists to hold all cammels and dice
        self.camle_list= [self.c1, self.c2, self.c3, self.c4, self.c5]
        self.dice_list = [self.dorange, self.dgreen, self.dyellow, self.dblue, self.dwhite]   
        self.Not_pyramide =[]  # Holds dice not in the pyramide
        
        # Lists to track special feilds
        self.list_plus_one_fields=[]
        self.list_minus_one_fields=[]
        self.list_potential_fields=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

        self.portfolio = {"orange": 5, "green": 5}  # Example portfolio with camel values

        #Remove already taken cards and adjancent feilds
        self.placements={f"{place+1}":0 for place in range(16)}

    def move(self,camel,moves):  # Moves the camel by a specific numbr of steps
        new_field=self.new_field(camel,moves)  # Find the target feild
        camels_on_field= self.camels_above(camel)  # Get cammels above current one
        is_minus_field= self.see_if_it_is_minus_field(new_field)  # Check if it is a minus feild       
        if is_minus_field:  # If its a minus feild, collect cammels
            for camel in self.camels_on_same_field(new_field):
                camels_on_field.append(camel)        
        self.move_all_camels_to_new_field(camels_on_field,new_field)  # Move all collected camels

    def see_if_it_is_minus_field(self,field):  # Determines if the feild is minus
        for tested_field in self.list_minus_one_fields:  # Loop over minus fields   
            if field == tested_field:  # If it matches, return true
                return True
        return False  # Otherwise, return false


    def new_field(self,camel,moves):  # Calculates the new feild after the camle moves
        new_field = camel.field + int(moves)  # Adds the numbr of moves to the camel's current feild
        for field in self.list_plus_one_fields:  # Check if the new field has a +1 effect
            if new_field == field:  # If it matches, plus 1 feild 
                new_field += 1
                
        for field in self.list_minus_one_fields:  # Check if the new field has a -1 effect
            if new_field == field:  # If it matches, minus 1 feild
                new_field -= 1

        for field in self.list_potential_fields:  # Updates the placement counter for potential feilds
            if new_field == field:
                self.placements[f"{field}"] += 1
                
        return new_field  # Return the updated new feild

    def camels_on_same_field(self, field):  # Finds all cammels on the same feild
        return sorted(
            [c for c in self.camle_list if c.field == field], 
            key=lambda camel: camel.position
        )  # Sort them by their position

    def camels_above(self, camel):  # Finds cammels above the current one on the feild
        return sorted(
            [c for c in self.camle_list if c.field == camel.field and camel.position <= c.position], 
            key=lambda camel: camel.position
        )  # Sort cammels above by position

    def move_all_camels_to_new_field(self, list_camels, new_field):  # Moves cammels to a new feild
        list_camels.sort(key=lambda camel: camel.position)  # Sort cammels by their current position
        for i in range(len(list_camels)):  # Iterate through cammels in the list               
            for i, camel in enumerate(list_camels):  # For each cammel, update field and position
                camel.field = new_field
                camel.position = len([c for c in self.camle_list if c.field == new_field]) + i - 1  # Adjust position
    
    def produce_dice(self):  # Picks a random dice from the list and removes it
        current_dice = random.choice(self.dice_list)  # Choose a random dice
        self.dice_list.remove(current_dice)  # Remove it from the dice list
        return current_dice.colour  # Return the colour of the dice

    def take_initial_input(self):  # Takes user inputs to initilise the game state
        for camel in self.camle_list:  # For each camel, take user inputs
            camel_color = input("What camle was rolled?")  # Ask for the rolled cammel color
            roll = input("Roll:")  # Ask for the roll result
            self.move(self.take_color_return_object(camel_color), roll)  # Move the camel based on input
        input1 = input("Do any more fields have plus cards?y/n")  # Ask if there are +1 cards
        while input1 == "y":  # While the answer is "yes"
            self.list_minus_one_fields.append(input("What field have plus cards on them"))  # Add the field to list
            input1 = input("Do any more fields have plus cards?y/n")  # Ask again
        input2 = input("Do any more fields have minus cards?y/n")  # Ask if there are -1 cards
        while input2 == "y":  # While the answer is "yes"
            self.list_minus_one_fields.append(input("What field have minus cards on them"))  # Add the field to list
            input2 = input("Do any more fields have minus cards?y/n")  # Ask again
        
    def take_color_return_object(self, color):  # Returns the cammel object based on its color
        match color:  # Match the given color to a camel
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

    def give_all_poistions(self):  # Prints the positions of all cammels
        for camel in self.camle_list:  # Loop over every camel
            print(camel.name,"Position:",camel.position, "Color:",camel.color, "Field:", camel.field)  # Display each camel's info

    def save_current_position(self):  # Safes the curent state of the game by writing to a file
        file1 = open("save.txt","r+")  # Open the file in read/write mode
        for camel in self.camle_list:  # Loop through every camel in the list
            file1.write(camel.color.strip()+"\n")  # Write the cammels color
            file1.write(str(camel.position)+"\n")  # Write the cammels position
            file1.write(str(camel.field)+"\n")  # Write the cammels field

    def load_safe(self):  # Loads the cammel data from the saved file
        file1 = open("save.txt","r+")  # Opens the file for reading/writing
        save = file1.readlines()  # Reads all lines into a list
        self.camle_list = []  # Reset the camel list
        del self.c1, self.c2, self.c3, self.c4, self.c5  # Delete old camel instances
        # Create new camel objects from the save file
        self.c1 = camel(save[0].replace("\n",""), int(save[1]), int(save[2])) 
        self.c2 = camel(save[3].replace("\n",""), int(save[4]), int(save[5])) 
        self.c3 = camel(save[6].replace("\n",""), int(save[7]), int(save[8])) 
        self.c4 = camel(save[9].replace("\n",""), int(save[10]), int(save[11])) 
        self.c5 = camel(save[12].replace("\n",""), int(save[13]), int(save[14])) 
        self.camle_list = [self.c1, self.c2, self.c3, self.c4, self.c5]  # Rebuild the list
        self.give_all_poistions  # Print the loaded positions

    def run(self):  # Runs a single turn of the game
        for dice in range(5):  # Loop through each dice
            wurf = random.randint(1,3)  # Roll a number between 1 and 3
            color = self.produce_dice()  # Select a random dice color
            self.move(self.take_color_return_object(color), wurf)  # Move the camel
        self.dice_list = [self.dorange, self.dgreen, self.dyellow, self.dblue, self.dwhite]  # Reset dice

    def calculate_probability(self, times):  # Simulate the game multiple times to calculate win probabilities
        # Runs the game a specified number of times and calculates liklihoods
        list_of_colors = ["orange", "yellow", "green", "white", "blue"]  # Define camel colors
        counters = {f"{color}_{place}": 0 for color in list_of_colors for place in range(5)}  # Initilises result counters
        start = time.time()  # Start timing the simulation

        for i in range(times):  # Run the simulation for the given number of times
            self.run()  # Run a single turn
            self.sort_for_best()  # Sort camels by their positions
            for place in range(5):  # Loop through each rank
                for color in list_of_colors:  # Loop through each color
                    if self.camle_list[place].color == color:  # Check if camel color matches
                        counters[f"{color}_{place}"] += 1  # Increment the counter for the rank
            self.load_safe()  # Reset the game state after each simulation

        place_list = ["First", "Second", "Third", "Fourth", "Fived"]  # Place labels with intentional mistake
        for place in range(5):  # Loop through ranks
            print("") 
            print("") 
            print(f"Probability of {place_list[place]} Place")  # Print place title
            for color in list_of_colors:  # Loop through colors
                count = counters[f"{color}_{place}"] / times  # Calculate the probability
                print(f"{color}:", round(count * 100, 2), "%", end=" ")  # Print the result

        end = time.time()  # End timing
        print("") 
        print("Calculated in", (end - start), "seconds")  # Display calculation time

    def sort_for_best(self):  # Sorts the cammels by feild and position for ranking
        self.camle_list.sort(key=lambda camel: (-camel.field, camel.position))  # Sort by field descending, position ascending

    def calculate_best_turn(self, times):  # Simulate the game to determine the best turn options
        # Runs the game multiple times to find the best moves
        list_of_colors = ["orange", "yellow", "green", "white", "blue"]  # Camel colors
        counters = {f"{color}_{place}": 0 for color in list_of_colors for place in range(5)}  # Initilises counters
        start = time.time()  # Start timing
        cardvalue = {"orange": 5, "yellow": 5, "green": 5, "white": 5, "blue": 5}  # Card values for betting
        expected_value = {"orange": 0, "yellow": 0, "green": 0, "white": 0, "blue": 0, "card": 0}  # Expected values
        self.check_possible_fields()  # Update potential fields

        for i in range(times):  # Simulate the game `times` times
            self.run()  # Run a single turn
            self.sort_for_best()  # Sort camels
            for place in range(5):  # Loop through ranks
                for color in list_of_colors:  # Loop through colors
                    if self.camle_list[place].color == color:  # Check if camel matches rank
                        counters[f"{color}_{place}"] += 1  # Increment counter for rank
            self.load_safe()  # Reset the game state

        for f in range(16):  # Normalize placements
            if not self.placements[f"{f+1}"] == 0: 
                self.placements[f"{f+1}"] = self.placements[f"{f+1}"] / times
        max_key = max(self.placements, key=self.placements.get)  # Find the best field
        expected_value["card"] = self.placements[max_key]  # Update expected card value
        print(expected_value["card"], "per turn value on field:", max_key)  # Display best card value

        for color in list_of_colors:  # Calculate expected outcomes
            probability_1 = counters[f"{color}_0"] / times
            probability_2 = counters[f"{color}_1"] / times
            probability_345 = (counters[f"{color}_2"] + counters[f"{color}_3"] + counters[f"{color}_4"]) / times
            expected_outcome = probability_1 * cardvalue[f"{color}"] + probability_2 * 1 + probability_345 * -1
            if expected_outcome >= 1:  # Only consider valuable outcomes
                expected_value[color] = expected_outcome
                print(f"Expected Value of highest card {color}", round(expected_outcome, 2))  # Display outcome

        end = time.time()  # End timing
        print("") 
        print("Calculated in", (end - start), "seconds")  # Display calculation time

    def check_possible_fields(self):  # Checks for fields that are no longer avalable
        unavailable_fields = []  # List to keep track of invalid feilds

        for f in self.list_minus_one_fields:  # Loop through all the minus fields
            unavailable_fields.append(f, f+1, f-1)  # Add the feild and its adjacents to the list

        for f in self.list_plus_one_fields:  # Loop through all the plus fields
            unavailable_fields.append(f, f+1, f-1)  # Add the feild and its adjacents to the list
        
        for c in self.camle_list:  # Check each cammels current field
            unavailable_fields.append(c.field)  # Add the cammels feild to the list of unavailable ones

        # Remove unavailable feilds from the potential feilds
        self.list_potential_fields = [f for f in self.list_potential_fields if f not in unavailable_fields] 





                




game =pyramide()
#game.save_current_position()  
#game.give_all_poistions()
#game.save_current_position()
#game.run() 
#game.give_all_poistions()
#game.sort_for_best()
#game.calculate_probability(10000) #sooo  


game.take_initial_input()
game.load_safe()
game.calculate_best_turn(10000) 
