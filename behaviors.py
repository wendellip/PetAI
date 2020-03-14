
def trivial_behavior(state):
    return True

################### CAT STUFF ###################

# Maybe we make these behaviors update other factors (eg. play increases tiredness)?

def cat_meow(state):
    print("Your cat meows!")
    return True

def cat_play_alone(state):
    print("Your cat tries to catch an imaginary bug")
    return True

def cat_groom_self(state):
    print("Your cat is grooming itself")
    return True

def cat_sleep(state):
    print("Your cat is sleeping")
    return True

################### FISH STUFF ###################

def fish_idle(state):
    print("Your fish doesn't appear to be doing anything out of the ordinary")
    return True
