from owners import Owner
class Board_tile:
    def __init__(self, owned, owner):
        self.owned = owned
        self.owner = owner
    
    def is_occupied(self):
        return self.owned

    def change_owner(self, new_owner):
        self.owner = new_owner
    
    def get_owner(self):
        return self.owner

    def occupy(self):
        self.owned = True