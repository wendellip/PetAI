from bt import *
from checks import *
from behaviors import *

class Dog:
    def __init__(self):
        # Set up the behavior tree in here, similar to setup_behavior_tree in P4
         pass

    def tick(self, state):
        pass

class Cat:
    def __init__(self):
        # Set up the behavior tree in here, similar to setup_behavior_tree in P4
         pass

    def tick(self, state):
        pass

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
