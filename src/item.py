class Item:
    def __init__(self, name, description ):
        self.name = name
        self.description = description
       
    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")


class Treasure(Item):
    def __init__(self, name, description, material):
        super().__init__(name, description)
        self.material = material

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} Treasure material: {self.material}"

class Book(Item):
    def __init__(self, name, description, secret):
        super().__init__(name, description)
        self.secret = secret

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} Book secret: {self.secret}"

class Weapon(Item):
    def __init__(self, name, description, length):
        super().__init__(name, description)
        self.length = length

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} Weapon length: {self.length}"



