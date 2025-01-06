import time
def calculate_best_turn(self,times):
        # runs the turn a number of times and uses that data to calculate the liklyhood of any given result
           #Adjust number of times U want to the programm to simulate outcomes of ur position (recommended 10000 in ca. 2,3s)
        list_of_colors=["orange","yellow","green","white","blue"] 

        counters= {f"{color}_{place}":0 for color in list_of_colors for place in range(5)} #initialises varibales for storing the results 

        start=time.time() 
        cardvalue= {"orange":5,"yellow":5,"green":5,"white":5,"blue":5}
        expected_value = {"orange":0,"yellow":0,"green":0,"white":0,"blue":0,"card":0}

 
        for i in range(times):

            self.run()
            self.sort_for_best()  
            for place in range (5):
                for color in list_of_colors:
                    if self.camle_list[place].color== color:
                        counters [f"{color}_{place}" ]+=1  


            for f in range(len(self.placements)):
                self.placements[f] = self.placements[f]/times
            expected_value["card"]=max(self.placements )


            print()
            
            #place card on field von 1-16 zählt wie oft da was raufgekommen ist
            
            self.load_safe()

        
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

        