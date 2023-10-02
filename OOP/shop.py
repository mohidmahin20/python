class Shop:
    cart=[] # here cart is a class atribute
    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,item):
        self.cart.append(item)

mahjabeen = Shop('mehjabeen')
mahjabeen.add_to_cart('shoes')
mahjabeen.add_to_cart('phone')
print(mahjabeen.cart)

nisho=Shop('noiso')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)