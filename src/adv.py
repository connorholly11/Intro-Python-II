from item import Item
from player import Player1
from room import Room
# Declare all the rooms
# Dictionary of rooms mapping name to Room
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
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['outside'].items.append(Item("Knife", "Sharp thing"))
room['outside'].items.append(Item("Potion", "Green and bubbly liquid in a glass vial"))
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player1 = Player1(room['outside'])
# Write a loop that:
#
while True:
# * Prints the current room name
    current_room = player1.current_room
    print("player1", player1.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player1.current_room.description)
# * Print items in the room
    print("The room contains the following items:")
    for item in current_room.items:
        print(item)
# * Waits for user input and decides what to do.
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w') or get or take an item:\n")
# If the user enters a cardinal direction, attempt to move to the room there.
    # moving to a room --> setting current_room on player
    if user_input == "q":
        break
    split_input = user_input.split()
    print(split_input)
    if len(split_input) == 1:
        # move the player
        direction_attribute = f"{user_input}_to"
        if hasattr(current_room, direction_attribute):
            print("Trying to move to: ", getattr(current_room, direction_attribute))
            player1.current_room = getattr(current_room, direction_attribute)
        else:
            print("Choose a valid direction to move in")
            continue
    elif len(split_input) == 2:
        item_name = split_input[1]
        if split_input[0].lower() == "get":
# If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.
            item = current_room.get_item(item_name)
            if item:
                item.on_take()
                # remove the item from the room
                current_room.remove_item(item)
                # Add it to the player's items
                player1.items.append(item)
            else:
                print(f"{item_name} does not exist in room")
        elif split_input[0].lower() == "drop":
            # drop the item
            # check if item is on player
            # if it is:
            #   call item.on_drop()
            #   remove from player
            #   add to room
            pass
        else:
            print("I didn't recognize that command")
            continue
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#--------------------------------------------

# The /src directory contains the files adv.py, which is where the main logic for the game should live, room.py, which will contain the definition of the Room class, and player.py, which will contain the definition of the Player class.

# Add a REPL parser to adv.py that accepts directional commands to move the player

# After each move, the REPL should print the name and description of the player's current room
# Valid commands are n, s, e and w which move the player North, South, East or West
# The parser should print an error if the player tries to move where there is no room.
# Put the Room class in room.py based on what you see in adv.py.

# The room should have name and description attributes.

# The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.

# Put the Player class in player.py.

# Players should have a name and current_room attributes
# Create a file called item.py and add an Item class in there.

# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.

# Add the ability to add items to rooms.

# The Room class should be extended with a list that holds the Items that are currently in that room.

# Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.

# Add capability to add Items to the player's inventory. The inventory can also be a list of items "in" the player, similar to how Items can be in a Room.

# Add a new type of sentence the parser can understand: two words.

# Until now, the parser could just understand one sentence form:

# verb

# such as "n" or "q".

# But now we want to add the form:

# verb object

# such as "take coins" or "drop sword".

# Split the entered command and see if it has 1 or 2 words in it to determine if it's the first or second form.

# Implement support for the verb get followed by an Item name. This will be used to pick up Items.

# If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.

# If it is there, remove it from the Room contents, and add it to the Player contents.

# If it's not there, print an error message telling the user so.

# Add an on_take method to Item.

# Call this method when the Item is picked up by the player.

# on_take should print out "You have picked up [NAME]" when you pick up an item.

# The Item can use this to run additional code when it is picked up.

# Add an on_drop method to Item. Implement it similar to on_take.

# Implement support for the verb drop followed by an Item name. This is the opposite of get/take.

# Add the i and inventory commands that both show a list of items currently carried by the player.