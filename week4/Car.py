class car:
    def _init_(self,model,make,year,engine_capacity):
        self.model = model
        self.make = make
        self.year = year
        self.engine_capacity = engine_capacity 

#getters

def get_model(self):
    return self.model 

def get_make(self):
    return self.make

def get_year(self):
    return self.year

def get_engine_capacity(self):
    return self.engine_capacity

#setters - sets the attributes

def set_model(self,model):
    self.model = model

def set_make(self,make):
    self.make = make

def set_year(self,year):
    self.year = year

def set_engine_capacity(self,engine_capacity):
    self.engine_capacity = engine_capacity


#objects
car1 = car("Demio","Nissan","2018","1300CC")
car2 = car("Toyota","Nissan","2020","2500CC")
car3 = car("Bughatti","Mercedes","2020","3500CC")

print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car2.get_year())