# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
class Room:
    counter_items = 0
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        Room.counter_items += len(items)
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def print_items(self,room_items):
        outpt = ""
        for item in room_items:
            outpt += f" *** {item.name} "
        return outpt


    def __str__(self):
        output = f"Room name: {self.name}, Counter_Items={Room.counter_items} \nDescription: {textwrap.fill(self.description, width =52)}\n"
        if self.n_to:
            output += f"north to --> {self.n_to.name} {self.print_items(self.n_to.items)}\n"
        if self.s_to:
            output += f"south to --> {self.s_to.name} {self.print_items(self.s_to.items)}\n"
        if self.e_to:
            output += f"east to  --> {self.e_to.name} {self.print_items(self.e_to.items)}\n"
        if self.w_to:
            output += f"west to  --> {self.w_to.name} {self.print_items(self.w_to.items)}\n"

        i=1
        for item in self.items:
            output += f"\n {i}. {item}"
            i +=1
        
        return output

    def __repr__(self):
        return f"self.name = {self.name}; self.items = {self.items}"

    def add_item(self, item):
        self.items.append(item)
        Room.counter_items +=1
        print(f"{item.name} was added in a {self.name} room")
        return self.items

    def remove_item(self, item):
        found_item = [el for el in self.items if el.name == item.name]
        if len(found_item) != 0:
            self.items.remove(found_item[0])
            Room.counter_items -=1
            print(f"{item.name} was removed from a {self.name} room")
        else:
            print(f"{item.name} is not in a {self.name}")