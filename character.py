import random

class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            if isinstance(self.conversation, list):
                print(f"[{self.name} says]: {random.choice(self.conversation)}")
            else:
                print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")

    def special_interaction(self):
        print(f"{self.name} doesn't have any special interactions.")
        return "none"


    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer")
            return False

    def special_interaction(self):
        print(f"{self.name} doesn't have any special interactions.")
        return "none"

                 

        
