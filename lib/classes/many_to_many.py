class Coffee:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name') and 3 <= len(name):
            self._name = name
        
    def orders(self):
        # order is an instance of Order
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        if len(self.orders()) >= 1:
            return len(self.orders())
        return 0

    def average_price(self):
        prices = [order.price for order in self.orders()]
        sum_of_prices = sum(prices)
        length_of_list = self.num_orders()
        if len(self.orders()) >= 1:
            return sum_of_prices/length_of_list
        return 0

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, new_coffee, new_price):
        return Order(self, new_coffee, new_price)
           
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and not hasattr(self, 'price') and 1.0 <= price <= 10.0:
            self._price = price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    # customer is an instance 
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    # coffee is an instance 
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

# coffee_1 = Coffee("Mocha")
# coffee_2 = Coffee("Vanilla Latte")
# customer = Customer("Steve")
# customer_2 = Customer("Dima")
# Order(customer, coffee_1, 2.0)
# Order(customer_2, coffee_1, 5.0)
# Order(customer, coffee_2, 5.0)
# print(coffee_1.average_price()) 
