import Animal

print("Welcome to the animal generator!")
print("This program creates Animal objects.")

animals = []


while True: 
    animal_type = input("What type of animal would you like to create?")

    name = input("What do you want to name the animal?")


    next_animal = Animal.Animal(animal_type, name)
    animals.append(next_animal)

    again = input("\nWould you like to add more animals, (y/n)?")
    if(again != "y"):
        break
        
   
print("\nAnimal List")

for x in animals:
    print(x.get_name(), "the", x.get_animal_type(), "is", x.check_mood())
    





