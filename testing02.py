import tkinter as tk
from tkinter import messagebox
import random
import time

class Dice:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def roll(self):
        self.wurf = random.randint(1, 3)

class Camel:
    def __init__(self, color, position, field):
        self.color = color
        self.position = position
        self.field = field

    def roll(self):
        self.wurf = random.randint(1, 6)

class Pyramide:
    def __init__(self):
        self.dorange = Dice("1", "orange")
        self.dgreen = Dice("2", "green")
        self.dyellow = Dice("3", "yellow")
        self.dwhite = Dice("4", "white")
        self.dblue = Dice("5", "blue")

        self.c1 = Camel("orange", 0, 0)
        self.c2 = Camel("green", 0, 0)
        self.c3 = Camel("yellow", 0, 0)
        self.c4 = Camel("white", 0, 0)
        self.c5 = Camel("blue", 0, 0)

        self.camel_list = [self.c1, self.c2, self.c3, self.c4, self.c5]
        self.dice_list = [self.dorange, self.dgreen, self.dyellow, self.dblue, self.dwhite]
        self.not_pyramide = []

        self.list_plus_one_fields = []
        self.list_minus_one_fields = []
        self.list_potential_fields = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        self.portfolio = {"orange": 5, "green": 5}

        self.placements = {f"{place+1}": 0 for place in range(16)}

    def move(self, camel, moves):
        new_field = self.new_field(camel, moves)
        camels_on_field = self.camels_above(camel)
        is_minus_field = self.see_if_it_is_minus_field(new_field)
        if is_minus_field:
            for camel in self.camels_on_same_field(new_field):
                camels_on_field.append(camel)
        self.move_all_camels_to_new_field(camels_on_field, new_field)

    def see_if_it_is_minus_field(self, field):
        for tested_field in self.list_minus_one_fields:
            if field == tested_field:
                return True
        return False

    def new_field(self, camel, moves):
        new_field = camel.field + int(moves)
        for field in self.list_plus_one_fields:
            if new_field == field:
                new_field += 1
        for field in self.list_minus_one_fields:
            if new_field == field:
                new_field -= 1
        for field in self.list_potential_fields:
            if new_field == field:
                self.placements[f"{field}"] += 1
        return new_field

    def camels_on_same_field(self, field):
        return sorted(
            [c for c in self.camel_list if c.field == field],
            key=lambda camel: camel.position
        )

    def camels_above(self, camel):
        return sorted(
            [c for c in self.camel_list if c.field == camel.field and camel.position <= c.position],
            key=lambda camel: camel.position
        )

    def move_all_camels_to_new_field(self, list_camels, new_field):
        list_camels.sort(key=lambda camel: camel.position)
        for i in range(len(list_camels)):
            for i, camel in enumerate(list_camels):
                camel.field = new_field
                camel.position = len([c for c in self.camel_list if c.field == new_field]) + i - 1

    def produce_dice(self):
        current_dice = random.choice(self.dice_list)
        self.dice_list.remove(current_dice)
        return current_dice.colour

    def take_initial_input(self):
        for camel in self.camel_list:
            camel_color = input("What camel was rolled?")
            roll = input("Roll:")
            self.move(self.take_color_return_object(camel_color), roll)
        input1 = input("Do any more fields have plus cards?y/n")
        while input1 == "y":
            self.list_minus_one_fields.append(input("What field have plus cards on them"))
            input1 = input("Do any more fields have plus cards?y/n")
        input2 = input("Do any more fields have minus cards?y/n")
        while input2 == "y":
            self.list_minus_one_fields.append(input("What field have minus cards on them"))
            input2 = input("Do any more fields have minus cards?y/n")

    def take_color_return_object(self, color):
        match color:
            case "orange":
                return self.camel_list[0]
            case "green":
                return self.camel_list[1]
            case "yellow":
                return self.camel_list[2]
            case "white":
                return self.camel_list[3]
            case "blue":
                return self.camel_list[4]

    def give_all_positions(self):
        for camel in self.camel_list:
            print(camel.name, "Position:", camel.position, "Color:", camel.color, "Field:", camel.field)

    def save_current_position(self):
        with open("save.txt", "w") as file1:
            for camel in self.camel_list:
                file1.write(camel.color.strip() + "\n")
                file1.write(str(camel.position) + "\n")
                file1.write(str(camel.field) + "\n")

    def load_save(self):
        with open("save.txt", "r") as file1:
            save = file1.readlines()
        self.camel_list = []
        self.c1 = Camel(save[0].replace("\n", ""), int(save[1]), int(save[2]))
        self.c2 = Camel(save[3].replace("\n", ""), int(save[4]), int(save[5]))
        self.c3 = Camel(save[6].replace("\n", ""), int(save[7]), int(save[8]))
        self.c4 = Camel(save[9].replace("\n", ""), int(save[10]), int(save[11]))
        self.c5 = Camel(save[12].replace("\n", ""), int(save[13]), int(save[14]))
        self.camel_list = [self.c1, self.c2, self.c3, self.c4, self.c5]
        self.give_all_positions()

    def run(self):
        for dice in range(5):
            wurf = random.randint(1, 3)
            color = self.produce_dice()
            self.move(self.take_color_return_object(color), wurf)
        self.dice_list = [self.dorange, self.dgreen, self.dyellow, self.dblue, self.dwhite]

    def calculate_probability(self, times):
        list_of_colors = ["orange", "yellow", "green", "white", "blue"]
        counters = {f"{color}_{place}": 0 for color in list_of_colors for place in range(5)}
        start = time.time()

        for i in range(times):
            self.run()
            self.sort_for_best()
            for place in range(5):
                for color in list_of_colors:
                    if self.camel_list[place].color == color:
                        counters[f"{color}_{place}"] += 1
            self.load_save()

        place_list = ["First", "Second", "Third", "Fourth", "Fifth"]
        for place in range(5):
            print("")
            print(f"Probability of {place_list[place]} Place")
            for color in list_of_colors:
                count = counters[f"{color}_{place}"] / times
                print(f"{color}:", round(count * 100, 2), "%", end=" ")

        end = time.time()
        print("")
        print("Calculated in", (end - start), "seconds")

    def sort_for_best(self):
        self.camel_list.sort(key=lambda camel: (-camel.field, camel.position))

    def calculate_best_turn(self, times):
        list_of_colors = ["orange", "yellow", "green", "white", "blue"]
        counters = {f"{color}_{place}": 0 for color in list_of_colors for place in range(5)}
        start = time.time()
        cardvalue = {"orange": 5, "yellow": 5, "green": 5, "white": 5, "blue": 5}
        expected_value = {"orange": 0, "yellow": 0, "green": 0, "white": 0, "blue": 0, "card": 0}
        self.check_possible_fields()

        for i in range(times):
            self.run()
            self.sort_for_best()
            for place in range(5):
                for color in list_of_colors:
                    if self.camel_list[place].color == color:
                        counters[f"{color}_{place}"] += 1
            self.load_save()

        for f in range(16):
            if not self.placements[f"{f+1}"] == 0:
                self.placements[f"{f+1}"] = self.placements[f"{f+1}"] / times
        max_key = max(self.placements, key=self.placements.get)
        expected_value["card"] = self.placements[max_key]
        print(expected_value["card"], "per turn value on field:", max_key)

        for color in list_of_colors:
            probability_1 = counters[f"{color}_0"] / times
            probability_2 = counters[f"{color}_1"] / times
            probability_345 = (counters[f"{color}_2"] + counters[f"{color}_3"] + counters[f"{color}_4"]) / times
            expected_outcome = probability_1 * cardvalue[f"{color}"] + probability_2 * 1 + probability_345 * -1
            if expected_outcome >= 1:
                expected_value[color] = expected_outcome
                print(f"Expected Value of highest card {color}", round(expected_outcome, 2))

        end = time.time()
        print("")
        print("Calculated in", (end - start), "seconds")

    def check_possible_fields(self):
        unavailable_fields = []

        for f in self.list_minus_one_fields:
            unavailable_fields.extend([f, f+1, f-1])

        for f in self.list_plus_one_fields:
            unavailable_fields.extend([f, f+1, f-1])

        for c in self.camel_list:
            unavailable_fields.append(c.field)

        self.list_potential_fields = [f for f in self.list_potential_fields if f not in unavailable_fields]

class CamelUpSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camel Up Solver")
        self.game = Pyramide()

        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.load_button = tk.Button(self.root, text="Load Game", command=self.load_game)
        self.load_button.pack()

        self.save_button = tk.Button(self.root, text="Save Game", command=self.save_game)
        self.save_button.pack()

        self.run_button = tk.Button(self.root, text="Run Turn", command=self.run_turn)
        self.run_button.pack()

        self.calculate_button = tk.Button(self.root, text="Calculate Best Turn", command=self.calculate_best_turn)
        self.calculate_button.pack()

        self.output_text = tk.Text(self.root, height=20, width=50)
        self.output_text.pack()

    def start_game(self):
        self.game.take_initial_input()
        self.output_text.insert(tk.END, "Game started.\n")

    def load_game(self):
        self.game.load_save()
        self.output_text.insert(tk.END, "Game loaded.\n")

    def save_game(self):
        self.game.save_current_position()
        self.output_text.insert(tk.END, "Game saved.\n")

    def run_turn(self):
        self.game.run()
        self.output_text.insert(tk.END, "Turn run.\n")
        self.display_positions()

    def calculate_best_turn(self):
        self.game.calculate_best_turn(10000)
        self.output_text.insert(tk.END, "Best turn calculated.\n")

    def display_positions(self):
        self.output_text.insert(tk.END, "Current positions:\n")
        for camel in self.game.camel_list:
            self.output_text.insert(tk.END, f"{camel.color} - Position: {camel.position}, Field: {camel.field}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CamelUpSolverApp(root) 
    root.mainloop()
