from character import Character, Enemy 
import types

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
chef.set_conversation("Hello there! Need any help in the kitchen?")

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