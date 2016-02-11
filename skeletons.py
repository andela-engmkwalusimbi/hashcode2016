import sys

class Drone(object):
    def __init__(self, id, location, max_load):
        self.id = id
        self.location = location
        self.max_load = max_load

    def set_current_location(self, grid_cordinate):
        self.location = grid_cordinate

    def get_distance_from_order(self, destination):
        pass

    def load(self, product):
        pass

    def wait(self, duration):
        pass

    def deliver(self, address):
        pass

    def unload(self, product):
        pass


class Product(object):
    def __init__(self, weight, product_types):
        self.id = id
        self.weight = weight
        self.product_types = product_types


class Order(object):
    def __init__(self, product, number, location):
        self.product = product
        self.number = number
        self.location = location

product_weights = {}
warehouse_data = {}
product_orders = {}
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as contents:
        r, c, d, t, p  = map(int, contents.readline().strip().split())
        product_types = int(contents.readline().strip())
        for index, weight in enumerate(contents.readline().strip().split()):
            product_weights[index] = int(weight)
        warehouses = int(contents.readline().strip())
        for x in range(warehouses):
            warehouse_data['w'+ str(x)] = {}
            warehouse_data['w'+ str(x)]['location'] = contents.readline().strip()
            warehouse_data['w'+ str(x)]['products'] = contents.readline().strip().split()
        orders = int(contents.readline().strip())
        for y in range(orders):
            product_orders['o'+ str(y)] = {}
            product_orders['o'+ str(y)]['location'] = contents.readline().strip()
            order_items = int(contents.readline().strip())
            for z in map(int, contents.readline().strip().split()):
                if z not in product_orders['o'+ str(y)]:
                    product_orders['o'+ str(y)][z] = 1
                else:
                    product_orders['o'+ str(y)][z] += 1
        print(product_orders)
