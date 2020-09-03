from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

def parse_move(player,move):
    room = player.current_room
    try:
        if move == 'n': 
            return room.n_to
        elif move == 's':
            return room.s_to
        elif move == 'e':
            return room.e_to
        elif move == 'w':
            return room.w_to
    except:
        print("There is no room. Try it again!")
        return room
  

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def get_user_choice(w_string):
    choice = input(w_string)
    return choice
# Make a new player object that is currently in the 'outside' room.
user = input("Enter your name: ")
player = Player(user, room['outside'])
print(player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

welcome_message = "Please enter: \nNorth n\nSouth s\nEast  e\nWest  w\nQuit  q\n"
user_input = get_user_choice(welcome_message).lower()

while True:
    if user_input == 'q':
        print("The game is over")
        break
    else:
        if parse_move(player, user_input) is not None:
            print(parse_move(player, user_input))
            player.current_room = parse_move(player, user_input)
        else:
           print("There is no room. Try it again!") 

    user_input = get_user_choice(welcome_message).lower()


# while True:
#     if user_input == 'q':
#         print("The game is over")
#         break
#     elif user_input in {'n','s','e','w'}:
#         if hasattr(player.current_room, f"{user_input}_to"):
#             player.current_room = getattr(player.current_room, f"{user_input}_to")
#         else:
#             print("somthing")
#     else:
#         print(parse_move(player, user_input))
#     #     player.current_room = parse_move(player, user_input)
    
#     user_input = get_user_choice(welcome_message).lower()






         

