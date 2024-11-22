def singleton(arg):
    L=[]
    def inner():
        if len(L)==0:
            obj=arg()
            L.append(obj)
        return L[0]
    return inner
@singleton
class movies1():
    def __init__(self):
        self.totaltic=200
    def booking(self):
        reqtic = int(input('enter the number of tickets :  ' ))
        if reqtic <= self.totaltic:
            print('tickets booked successfully....')
            self.totaltic  -= reqtic
            print(f'Available tickets are {self.totaltic}')
        else:
            print('tickests not available..')
@singleton
class movies2():
    def __init__(self):
        self.totaltic=200
    def booking(self):
        reqtic = int(input('enter the number of tickets :  ' ))
        if reqtic <= self.totaltic:
            print('tickets booked successfully....')
            self.totaltic  -= reqtic
            print(f'Available tickets are {self.totaltic}')
        else:
            print('tickests not available..')
@singleton
class movies3():
    def __init__(self):
        self.totaltic=200
    def booking(self):
        reqtic = int(input('enter the number of tickets :  ' ))
        if reqtic <= self.totaltic:
            print('tickets booked successfully....')
            self.totaltic  -= reqtic
            print(f'Available tickets are {self.totaltic}')
        else:
            print('tickests not available..')
def bmyshow():
    print('1) movie1 \n2) movie2 \n3) movie3'  )
    choice = int(input('enter the movie choice :- '))
    if choice == 1:
        user=movies1()
        user.booking()
    elif choice ==2:
        user=movies1()
        user.booking()
    elif choice == 3:
        user=movies1()
        user.booking()
    else:
        print('no movies available')
        
user1= bmyshow()
print('-'*20)    
user2= bmyshow()
print('-'*20)   
user3= bmyshow()
                     
    
    