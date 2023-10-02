class Phone:
    price=1200
    color='blue'
    brand='samsung'
    features=['camera','speaker','hammer']

    def call(self):
        print('calling')
    def send_sms(self,phone,sms):
        text= f'sending sms to {phone} and message :{sms}'
        return text
my_phone= Phone()
print(my_phone.features)
res=my_phone.send_sms(4122,'send')
print(res)

