class Phone:
    manufactured='china'
    def __init__(self,owner , brand ,price):
        self.owner= owner
        self.brand=brand
        self.price=price

my_phone= Phone('kala','oppo',9800)
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone= Phone('she','samsung',6000)
print(her_phone.owner,her_phone.brand,her_phone.price)