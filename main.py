from room import Room
from character import Character, Enemy
from item import Item
import types

#Quick note; Ba'Alzamon, The Dark One & Soulsbane are names for the same being

# Creating Room objects
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Room")
bathroom = Room("Bathroom")

# Creating Items
ladle = Item('ladle', "a sturdy kitchen utensil, perfect for demon-banishing")
taveeren = Item("ta'veeren", "the item that will grant The Dark One complete control of the world ")

soulsbane = Enemy("Ba'alzamon", "A terrifying demon lord")
soulsbane.set_conversation([
    "I am the Lord of the Grave, the Prince of the Twilight...",
    "Your soul will be mine, mortal!",
    "This world will burn, and from its ashes, a new age will rise!",
    "Why do you resist? Join me, and rule for eternity!",
    "You cannot escape the Shadow's embrace..."
])
soulsbane.set_weakness("ladle") 

chef = Character("Chef", "A friendly-looking chef with a big hat")
chef.set_conversation("Hello there! If you're hungry I've got something for you. Unless you didn't come for food...")

def soulsbane_special_interaction(self):
    print("Ba'alzamon's eyes burn with an otherworldly fire as he regards you.")
    interaction_choice = input("Do you want to: 1) Offer a sacrifice, 2) Ask about his plans, or 3) Back away slowly? ")
    if interaction_choice == "1":
        print("Ba'alzamon's interest is piqued by the mention of a sacrifice.")
        sacrifice = input("What do you offer as a sacrifice? ")
        if sacrifice.lower() == "taveeren":
            print("Ba'alzamon is momentarily appeased. You've made a dangerous ally!")
            return "befriend"
        else:
            print("Ba'alzamon is displeased with your offering. He attacks!")
            return "fight"
    elif interaction_choice == "2":
        print("Ba'alzamon speaks of destruction and chaos, growing more agitated.")
        return "agitate"
    elif interaction_choice == "3":
        print("You back away slowly. Ba'alzamon watches you with burning eyes.")
        return "escape"
    else:
        print("Invalid choice. Ba'alzamon interprets your confusion as weakness.")
        return "fight"

soulsbane.special_interaction = types.MethodType(soulsbane_special_interaction, soulsbane)

def chef_special_interaction(self):
    print("The Chef looks at you with a twinkle in his eye.")
    
    interaction_choice = input("Do you want to: 1) Ask for help, or 2) ... sacrifice the Chef to obtain the tav'eeren? ")
    if interaction_choice == "1":
        print("The Chef hands you a sturdy ladle. 'This should help with your demon problem,' he winks.")
        return "give_ladle"
    elif interaction_choice == "2":
        print("You make a terrible choice... The Chef looks shocked as you... obtain the ta'veeren.")

        print("With his last breath, the Chef exclaims: 'You are a bloody fool!!!'")

        print("The Chef is dead. His lifeless body lies on the kitchen floor.")
        return "sacrifice"
    else:
        print("The Chef looks confused by your indecision.")
        return "none"

chef.special_interaction = types.MethodType(chef_special_interaction, chef)

# Setting room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a chandelier")
dining_hall.set_description("A large room with an oak table")
bathroom.set_description("A repugnant odor is seeped into the walls")

# Linking rooms 
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
kitchen.link_room(bathroom, "east")
bathroom.link_room(kitchen, "west")
bathroom.link_room(dining_hall, "south")
dining_hall.link_room(bathroom, "north")

# Place characters in rooms
dining_hall.set_character(soulsbane)
kitchen.set_character(chef)


current_room = kitchen
inventory = []
soulsbane_defeated = False
chef_betrayed = False


print("""
In the annals of history, the legendary battle between the Dragon Reborn and the demon lord Ba'alzamon 
shook the foundations of the world. The Dragon Reborn emerged victorious, and peace reigned for centuries.

But now, the shadow of Ba'alzamon once again looms over the land. The demon lord has returned, 
threatening to plunge the world into darkness. The prophecies speak of an unlikely hero and an 
unexpected weapon that will be key to defeating Ba'alzamon.

As you stand at the threshold of this epic quest, you wonder: How will Ba'alzamon be defeated this time? 
What unlikely tool will prove to be his downfall?

Your journey begins in a broken, abandoned house with four rooms: a ballroom, a kitchen, a dining room, 
and a bathroom. To travel between rooms, you must navigate using the cardinal directions: north, south, 
east, and west. Be wary, for danger and destiny await in every corner.

Remember, to move between rooms, simply type the direction you wish to go: 'north', 'south', 'east', or 'west'.

Now, step forward, brave hero, and face your fate...
""")




while not soulsbane_defeated:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

        if not (chef_betrayed and inhabitant.name == "Chef"):
            print(f"Do you want to interact with {inhabitant.name}? (yes/no)")
            choice = input("> ").lower()
        else:
            choice = "no"
        
        if choice == "yes":
            while True:
                inhabitant.talk()
                print("\nChoose an action by entering the corresponding number:")
                print("1. Continue talking")
                print("2. End interaction")
                print("3. Special interaction")
                if inhabitant.name != "Chef":
                    print("4. Fight")
                print("Enter the number of your chosen action:")
                action_choice = input("> ")
                
                if action_choice == "1":
                    print("You decide to continue the conversation.")
                    continue
                elif action_choice == "2":
                    print("You end the interaction.")
                    break
                elif action_choice == "3":
                    print("You attempt a special interaction.")
                    result = inhabitant.special_interaction()
                    if result == "fight":
                        print("What will you fight with? Enter the name of the item:")
                        fight_with = input("> ")
                        if fight_with in [item.get_name() for item in inventory]:
                            if inhabitant.name == "Ba'alzamon":
                                if fight_with == "ladle":
                                    print(f"You defeated {inhabitant.name} with the legendary ladle!")
                                    current_room.set_character(None)
                                    soulsbane_defeated = True
                                    break
                                else:
                                    print(f"Your {fight_with} is ineffective against Ba'alzamon! He laughs at your futile attempt.")
                                    print("Ba'alzamon attacks you, and you barely escape with your life.")
                                    break
                            elif inhabitant.fight(fight_with):
                                current_room.set_character(None)
                                print(f"You defeated {inhabitant.name}!")
                                break
                            else:
                                print("Your attack was ineffective!")
                        else:
                            print(f"You don't have {fight_with} in your inventory!")
                    elif result == "befriend":
                        print(f"You've made an uneasy alliance with {inhabitant.name}!")
                        current_room.set_character(None)
                        if inhabitant.name == "Ba'alzamon":
                            soulsbane_defeated = True
                            break
                    elif result == "give_ladle":
                        inventory.append(ladle)
                        print("You received a ladle!")
                    elif result == "sacrifice":
                        inventory.append(taveeren)
                        print("You obtained tav'eeren... at a terrible cost.")
                        current_room.set_character(None)
                        chef_betrayed = True
                        break
                    elif result == "escape":
                        print("You manage to escape the interaction.")
                        break
                elif action_choice == "4" and inhabitant.name != "Chef":
                    print("You choose to fight. What will you fight with? Enter the name of the item:")
                    fight_with = input("> ")
                    inventory_item_names = [item.get_name() for item in inventory]
                    if fight_with in inventory_item_names:
                        if inhabitant.name == "Ba'alzamon":
                            if fight_with == "ladle":
                                print(f"You defeated {inhabitant.name} with the legendary ladle!")
                                current_room.set_character(None)
                                soulsbane_defeated = True
                                break
                            else:
                                print(f"Your {fight_with} is ineffective against Ba'alzamon! He laughs at your futile attempt.")
                                print("Ba'alzamon attacks you, and you barely escape with your life.")
                                break
                        elif inhabitant.fight(fight_with):
                            current_room.set_character(None)
                            print(f"You defeated {inhabitant.name}!")
                            break
                        else:
                            print("Your attack was ineffective!")
                    else:
                        print(f"You don't have {fight_with} in your inventory!")
                else:
                    print("Invalid choice. Please choose a valid option by entering its number.")
        elif choice == "no":
            print("You decide not to interact.")
        else:
            print("Invalid choice. Moving on.")

        if chef_betrayed and inhabitant.name == "Chef":
            print("You can't bear to look at the Chef's body after what you've done. You must leave this room.")
            while current_room == kitchen:
                print("Enter the direction you want to go (north, south, east, or west):")
                command = input("> ")
                current_room = current_room.move(command)

    if not soulsbane_defeated:
        print("Enter the direction you want to go (north, south, east, or west):")
        command = input("> ")
        current_room = current_room.move(command)

print("\nGame Over. You've resolved the situation with Ba'alzamon, the demon lord.")
if chef_betrayed:
    print("As you reflect on your journey, you can't help but feel the weight of your choices...")
    print("The Chef's death will haunt you forever.")
else:
    print("You return to the kitchen, grateful for the Chef's help in your perilous adventure.")
print("Thanks for playing!")












