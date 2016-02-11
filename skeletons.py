class Drone(object):
    def __init__(self, id, location, max_load):
        self.id = id
        self.location = location
        self.max_load = max_load
        
    def set_current_location(self, grid_cordinate):
        self.location = grid_cordinate
        
    def get_distance_from_order(self, destination):
        #get drone nearer
        
    def load(self, product):
        #load product
        
    def wait(self, duration):
        #wait asshole
        
    def deliver(self, address):
        #deliver
        
    def unload(self, product):
        #remove it
        
        
class Product(object):
    
    def __init__(self, weight, product_type, id):
        self.id = id
        self.weight = weight
        self.product_type = product_type
        
         
class Orders(object):
    def __init__(self, product, number, location):
        self.product = product
        self.number = number
        self.location = location

    def make_order(self,  number):
        s
