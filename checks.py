
def trivial_check(state):
    return True

def can_eat_from_bowl(state): # Used by cat & dog (since they share a food bowl)
    for bowl in state.food_bowls:
        if bowl > 10:
            return true
    return false

def is_cat_sociable(state): # Assumes state.cat is the only cat we care about
    return state.priority(state.cat.meter["social"]) > 60

def is_dog_sociable(state): # Assumes state.cat is the only cat we care about
    return state.priority(state.dog.meter["social"]) > 30

print(moo)
