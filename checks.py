
def trivial_check(state):
    return True

################### CAT & DOG SHARED STUFF #####################

def can_eat_from_bowl(state): # Used by cat & dog (since they share a food bowl)
    return state.food_bowl > 10

################### CAT STUFF ###################

def cat_is_sociable(state): # Assumes state.cat is the only cat we care about
    return state.priority(state.cat.meter["social"]) > 60

def cat_is_litter_box_full(state):
    return state.litter_box > 10

################### DOG STUFF ###################

def dog_is_sociable(state): # Assumes state.cat is the only cat we care about
    return state.priority(state.dog.meter["social"]) > 30
