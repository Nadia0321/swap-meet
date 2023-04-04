from swap_meet.item import Item
import uuid

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory 
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        if id not in self.inventory:
            return None
        self.id = Item(id)
    



        