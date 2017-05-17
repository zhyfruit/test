class Customer(object):
    def __init__(self, name=''):
        self.name = name
    def placeOrder(self, server, foods):
        return server.takeOrder(foods)
    def show(self, server, foods):
        print('Customer: ', self.name,'orders ')
        for i in foods:
            print(i, end = ' '),
        print('from', server.name)
        
class Employee():
    def __init__(self, name=''):
        self.name = name
    def takeOrder(self, food2eat):
        f = Food(food2eat)
        return f       
        
class Food():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return('%s'%(self.name))
    
class Lunch():
    def __init__(self,cus, em):
        self.cus = cus
        self.em = em
        self.food = []
        
    def order(self, name):
        self.food = name
        self.cus.placeOrder(self.em,self.food)
        
    def result(self):
        self.cus.show(self.em, self.food)
        
if __name__ == '__main__':
    customer_name = Customer(input('please input your name:'))
    server_name = Employee(input('please input your server:'))
    #food_name = input('please input your food today:')
    food_name = []
    num = eval(input('how many dishes?'))
    for i in range(0, num):
        fn = input()
        food_name.append(fn)
    today_lunch = Lunch(customer_name, server_name)
    today_lunch.order(food_name)
    today_lunch.result()
    
    
