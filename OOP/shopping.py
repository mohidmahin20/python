class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]

    def add_to_cart(self,item,price,quantity):
        product={'item': item,'price': price,'quantity': quantity}
        self.cart.append(product)
    def checkout(self,amount):
        total=0
        for item in self.cart:
            #print(item)
            total+= item['price']* item['quantity']
        print ('total price ',total)
        if amount< total:
            print(f'please provide {total-amount} more')
        else: 
            extra=amount -total
            print(f'here is your items and extra money {extra}')

swapan =Shopping('alan swapan')
swapan.add_to_cart('alu',59,8)
swapan.add_to_cart('dim',12,5)
swapan.add_to_cart('rice',40,4)
print(swapan.cart)
#swapan.checkout(600)
swapan.checkout(600)