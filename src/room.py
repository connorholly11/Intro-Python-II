# Implement a class to hold room information. This should have name and
# description attributes.

# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from item import Item
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # # 1) Adding these as attributes in the constructor is optional;
        # # in python you can arbitrarily set attributes on instances
        # # 2) the `: Room` syntax is a typehint. It just serves as a reminder
        # # for other developers that self.n_to is storing a Room object (as opposed to a str)
        # self.n_to: Room = None
        # self.s_to: Room = None
        # self.e_to: Room = None
        # self.w_to: Room = None
        self.items: List[Item] = []
    def get_item(self, item_name: str):
        """ Returns the item corresponding to item_name if it exists in the room
        otherwise returns None"""
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self, item: Item):
        self.items.remove(item)