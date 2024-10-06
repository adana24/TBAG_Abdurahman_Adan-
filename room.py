class Room(): 
    # Constructor method to initialize room objects
    def __init__(self, room_name):
        self.name = room_name  # Assign the name of the room
        self.description = None  # Room description initialized to None; can be set later
        self.linked_rooms = {}  # Dictionary to store rooms linked by direction (e.g., 'north': Room1, 'east': Room2)
        self.character = None

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character 

    # Getter method for room description
    def get_description(self):
        return self.description  # Returns the current description of the room
    
    # Setter method to assign a description to the room
    def set_description(self, room_description):
        self.description = room_description  # Sets the room's description to the provided value

    # Prints out the room's description
    def describe(self):
        print(self.description)  # Outputs the room's description to the console

    # Setter method for the room name
    def set_name(self, room_name):
        self.name = room_name  # Sets the room's name to the provided value

    # Getter method for the room name
    def get_name(self):
        return self.name  # Returns the current name of the room

    # Method to link one room to another in a specific direction
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link  # Adds a room to the dictionary with a key for the direction (e.g., 'north': Room2)

    # Method to print out the room's details in a formatted way
    def get_details(self):
        print(self.name)  # Prints the name of the room
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  # Prints a line separator to add a visual break
        print(self.description)  # Prints the room's description
        
        # Loop through each linked room and display the room name and the direction
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]  # Get the room object linked in the specific direction
            print(f"The {room.get_name()} is {direction}")  # Print which room is in a certain direction

    def get_details(self):
     print(f"You are in the {self.name}")
     print("-------------------------")
     print(self.description)
     for direction in self.linked_rooms:
        room = self.linked_rooms[direction]
        print("The " + room.get_name()+ " is "+direction) 

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self 
