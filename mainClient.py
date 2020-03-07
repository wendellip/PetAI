



if __name__ == "__main__":
    print("Welcome to PetAI! Please select what kind of pet you would like.")
    petList = ["Fish", "Dog", "Cat"]
    for i, pet in enumerate(petList):
        print("{}. {}".format(i+1, pet))
    choice = input().lower()
    pet_index = next(i for i, petType in enumerate(petList) if petType.lower() == choice)
    print("You have adopted a new {}, what would you like to name it?".format(petList[pet_index]))
    name = input()
    print((petList[pet_index], name))