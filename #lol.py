#lol

def move(self,camel,moves):

        if not camel.position== 0:
                camels_on_field = [c for c in self.camle_list if c.field == camel.field and camel.position<c.position]
                new_poition=0
                new_field=0
                reverse=False
                new_field=camel.field + int(moves) 
                for field in self.list_plus_one_fields:
                    if new_field == field:
                        new_field+=1
                for field in self.list_plus_one_fields:
                    if new_field == field:
                        new_field+=1        
                camels_on_field.sort(key=lambda camel: -camel.position)
                for i in range(len(camels_on_field)): 
                    camels_on_field_new = [c for c in self.camle_list if c.field == new_field]
                    new_poition=len(camels_on_field_new) 
                    camels_on_field[i].field = new_field
                    camels_on_field[i].position= new_poition   
        else:
            for field in self.list_plus_one_fields:
                    if new_field == field:
                        new_field+=1
            for field in self.list_minus_one_fields:
                    if new_field == field:
                        new_field-=1
                        reverse=True 
            new_poition=0
            new_field=0
            new_field=camel.field + int(moves) 
            camels_on_field = [c for c in self.camle_list if c.field == new_field]
            if not reverse == True:

                self.move_all_camels_to_new_field(camels_on_field,new_field) 
            
            if reverse == True:
                camels_on_old-field = [c for c in self.camle_list if c.field == camel.field]
                new_poition=len(camels_on_field) 
                camels_on_field.sort(key=lambda camel: -camel.position)
                for i in range(len(camels_on_field)): 
                    
                    camels_on_field_new = [c for c in self.camle_list if c.field == new_field]
                    new_poition=len(camels_on_field_new) 
                    camels_on_field[i].field = new_field
                    camels_on_field[i].position= new_poition

            
            camel.field = new_field
            camel.position= new_poition  
            reverse= False

def move_all_camels_to_new_field(self,list_camels,new_field):
        new_poition=len(list_camels) 
        list_camels.sort(key=lambda camel: -camel.position)
        for i in range(len(list_camels)):          
            camels_on_field_new = [c for c in self.camle_list if c.field == new_field]
            new_poition=len(camels_on_field_new) 
            list_camels[i].field = new_field
            list_camels[i].position= new_poition


# def move sudo script 

#detect field + or -
# calculate camels that will also be moved 
# calculate new field 
# if minus one that camels on new field go over moving camels 
#

def new_field