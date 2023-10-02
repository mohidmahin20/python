class Company:
    def __init___(self ,name,addres):
        self.name=name
        self.bus=[]
        self.routes=[]
        self.drivers=[]
        self.counter=[]
        self.manager=[]
        self.supervisors=[]
class Driver:
    def __init__(self,license,name,age) -> None:
        self.license =license
        self.name=name 
        self.age=age
class Counter:
    def __init__(self) -> None:
        pass
    def purchase_ticket(self,start,destination):
        pass

class Passenger:
    pass
class Supervisor:
    pass
lal_mia=Driver('a','1223',34)