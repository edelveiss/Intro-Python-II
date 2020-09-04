# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.player_items = []

    def get_items(self):
        output = f"{'-'*20}I N V E N T O R Y{'-'*20}\n{self.name}' Inventory: "
        if len(self.player_items) != 0:
            i=1
            for item in self.player_items:
                output += f"\n {i}. {item}"
                i +=1
            return f"{output}\n{'-'*60}\n"
        else:
            return f"{output} there is no item\n{'-'*60}\n"

        

    def add_item(self, item_name):
        found_item = [el for el in self.current_room.items if el.name == item_name]
        if len(found_item) != 0:
            self.player_items.append(found_item[0])
            found_item[0].on_take()
            # print(f"{self.name} got the {found_item[0].name}")
            return found_item[0]
        else:
            print(f"You can not take {item_name}, it is not in {self.current_room}")
            return None


        

    def drop_item(self, item_name):
        found_item = [el for el in self.player_items if el.name == item_name]
        if len(found_item) != 0:
            self.player_items.remove(found_item[0])
            found_item[0].on_drop()
            # print(f"{self.name} dropped the {found_item[0].name}")
            return found_item[0]
        else:
            print (f"{self.name} does not have a {item_name}")
            # print(f"{item_name} is not in a {self.name} player")
            return None
             

    def __str__(self):
        return f"Player's name: {self.name}, {self.current_room},"

    # def __repr__(self):
    #     return f"self.name = {self.name}; self.current_room = {self.current_room}"