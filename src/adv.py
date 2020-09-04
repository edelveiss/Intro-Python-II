from room import Room
from player import Player
from item import Item
from item import Weapon
from item import Treasure
from item import Book

# Declare all the rooms
torch = Weapon("torch", "produces a hot flame", "50inch" )
sword = Weapon("sword", "curved", "60inch")
key = Treasure("key", "key from secret chamber", "gold")
jewelry = Treasure("jewelry", "dream necklace","dimond")
coin = Treasure("coin", "old town coin","gold")
adventure = Book("adventure", "full of secrets", "silk pages")


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [torch, coin]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [sword, key]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [jewelry]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [adventure]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [jewelry,coin]),
}


  

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

welcome_message = f"{'-'*60}\nPlease enter: \nOne direction: North: 'n' South: 's' East: 'e' West: 'w'\nTake item: take [item]\nDrop item: drop [item] \nInventory: 'i'\nQuit:  'q'\n{'-'*60}\n"
user_input = get_user_choice(welcome_message).lower().split()
playing = True

while True:
    if 'i' in user_input[1:]:
        print(player.get_items())
    if 'take' in user_input[1:]:
        added_item_to_player = player.add_item(user_input[user_input.index("take") + 1])
        if added_item_to_player is not None:
            player.current_room.remove_item(added_item_to_player)

        
    if 'drop' in user_input[1:]:
        removed_item_from_player= player.drop_item(user_input[user_input.index("drop") + 1])
        if removed_item_from_player is not None:
            player.current_room.add_item(removed_item_from_player)

    if player.current_room.counter_items == 0:
        print("YOU ARE WON!!!!!!!!")
        break

    elif user_input[0] == 'q':
        print("The game is over")
        break
    else:
        if parse_move(player, user_input[0]) is not None:
            print(parse_move(player, user_input[0]))
            player.current_room = parse_move(player, user_input[0])
        else:
           print("There is no room. Try it again!") 
 

    user_input = get_user_choice(welcome_message).lower().split()





         

