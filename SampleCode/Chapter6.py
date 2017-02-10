class Fridge:
    def __init__(self, items =  {}):
        if type(items) != type({}):
            raise TypeError("Fridge require a dictionary but you have given %s" % type(items))
        self.items = items
        return 

    def __add_multi(self, food_name, quatity):
        if (not food_name in self.items):
            self.items[food_name] = 0
        self.items[food_name] = self.items[food_name] + quatity

    def add_one(self, food_name):
        if type(food_name) != type(''):
            raise TypeError("add_one require string, but given %s" % type(food_name))
        self.__add_multi(food_name, 1)
        return True

    def add_many(self, food_dict):
        if (type(food_dict) != type ({})):
            raise TypeError("add_many require dict, but given %s" % type(food_dict))
        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
        return             
    
    def has(self, food_name, quantity=1):
        return self.has_various({food_name, quantity})

    def has_various(self, food_dict):
        try:
            for food in food_dict.keys():
                if (self.items[food]) <= food_dict[food]):
                    return True 
                return False
        except KeyError:
            return False

    def __get_multi(self, food_name, quantity):
        try:
            if (self.items[food_name] is None):
                return False
            
            if (quantity > self.items[food_name]):
                return False

            self.item[food_name] = self.items[food_name] - quantity
        except KeyError:
            return False
        return quantity

    def get_one(self, food_name):
        if (type(food_name) != type('')):
            raise TypeError("food_name required type string, given this %s" % type(food_name))
        return self.__get_multi(food_name, 1)

    def get_many(self, food_dict):
        if self.has_various(food_dict):
            removed_items = {}
            for items in food_dict.keys():
                removed_items[items] = self.__get_multi(items, food_dict(items))
            return removed_items

    def get_ingredients(self, food):
        """
        if passed an object that has the __ingredients__ method, get_many will invoke this to get the list of ingredients.
        """
        pass 
        
            