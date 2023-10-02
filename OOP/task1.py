class Calculator:
    brand='casio'
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mult(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        return num1/num2
my_cal= Calculator()
addition=my_cal.add(2,3)
substraction=my_cal.sub(4,5)
multiplication=my_cal.mult(2,3)
devide=my_cal.div(3,4)
print(addition)
print(substraction)
print(multiplication)
print(devide)
