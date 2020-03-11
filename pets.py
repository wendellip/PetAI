from bt_nodes import *
from checks import *
from behaviors import *

class Pet:
    def __init__(self, name=None):
        self.name = name

    def execute(self, state):
        raise NotImplementedError


class Dog(Pet):
    def execute(self):
        pass
        
class Cat(Pet):   
    # This function will exhibit a behavior from the cat through the use of a behavior tree
    def execute(self, meters, items):
        print("My hunger is {}".format(meters["hunger"]))

    # Available actions for the owner (player) to do
    def actions(self, meters, items):
        print("Available Actions")
        print("1. Fill food bowl")
        print("2. Clean litter box")
        print("3. Play with cat")
        print("4. Do nothing")
        print("5. Sleep")
        print("6. Check items")
        print()
        try:
            choice = int(input("Enter the number of the action you want to do: "))
            print()
            if choice == 1:
                items["food_bowl"] = 100
                print("Food bowl has been filled.")
            elif choice == 2:
                items["litter_box"] = 100
                print("Litter box has been cleaned.")
            elif choice == 3:
                print(choice)
            elif choice == 4:
                pass
            elif choice == 5:
                for _ in range(47):
                    self.increase_meter(meters)
                    self.execute(meters, items)
            elif choice == 6:
                print("Food bowl is {}% filled".format(items["food_bowl"]))
                print("Litter box is {}% clean".format(items["litter_box"]))
            else:
                raise ValueError("Invalid Choice")
        except ValueError as e:
            print("Input is not a choice. Please select a valid choice.")
            self.actions(meters, items)

    # Initialize the cat's meters, this function should be called only once
    def create_meter(self):
        meter = {
            "hunger": 0,
            "energy": 0,
            "bladder": 0,
            "fun": 0,
            "hygiene": 0,
            "social": 0
        }

        return meter

    # Create items necessary for a cat, function should be called only once as well
    def create_item(self):
        item = {
            "food_bowl": 0,
            "litter_box": 100
        }

        return item

    # Increment cat meters over time to represent realistic needs of a cat
    def increase_meter(self, meter):
        for key, value in meter.items():
            meter[key] += 1

# Fish info
# Selector: What the fish do
# | Sequence: Ensure the fish is fed
# | | Check: if the tanks is clean
# | | Check: if a human is nearby
# | | Check: if I'm not already swimming slowly
# | | Action: swim slowly
# | Sequence: Ensure the tank is clean
# | | Check: if the tank is clean
# | | Check: if_not_swimming_sideways
# | | Action: swim_sideways

class Fish:
    def __init__(self):
        self.bt_root = Selector(name='What the fish do')
        # Set up the other stuff to reflect the logic above

    def tick(self, state):
        self.bt_root.execute(state)

# ---------------------------------------------------------------------

if __name__ == '__main__':
    try:
        # Read in the state. For now just set it to None
        state = None
        pets = [Dog(), Cat(), Fish()]
        while True:
            for pet in pets:
                pet.tick(state)

    except KeyboardInterrupt:
        print('\nKeyboard interrupt recieved, exiting')
