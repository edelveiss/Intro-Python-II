# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        

    def __str__(self):
        output = f"Room name: {self.name}, \nDescription: {self.description}\n"
        if self.n_to:
            output += f"north to --> {self.n_to.name}\n"
        if self.s_to:
            output += f"south to --> {self.s_to.name}\n"
        if self.e_to:
            output += f"east to  --> {self.e_to.name}\n"
        if self.w_to:
            output += f"west to  --> {self.w_to.name}\n"
        return output