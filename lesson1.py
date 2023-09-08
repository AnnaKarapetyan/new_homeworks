class BanckAccount:
    def __init__(self,account_number,b=0):
        self.__account_number=account_number
        self.__balance=b
        self.__transactions=[]
    def deposit(self,a):
        self.__balance+=a
        self.__transactions.append(f'Deposit - {a}')
    def withdraw(self,a):
        if(self.__balance-a>=0):
            self.__balance-=a
            self.__transactions.append(f'Deposit + {a}')
        else:
            print('error')
    def transfer(self,oa,a):
        if(oa.__balance-a>=0):
            oa.__balance-=a
            oa.__transactions.append(f'Deposit + {a}')
            self.__balance+=a
            self.__transactions.append(f'Deposit - {a}')
        else:
            print('error')
    def generate_statment(self):
        print(self.__transactions)
        print('Current balance ->',self.__balance)
    def get_balance(self):
        return self.__balance
    def clear_transactions(self):
        self.__transactions=[]
# a=BanckAccount('2142')
# a.deposit(300)
# a.withdraw(210)
# p=BanckAccount('2132',900)
# a.transfer(p,400)
# a.generate_statment()
#-----------lesson34------------

#----------ex2-----------------
class Trianglechecker:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def is_triangle(self):
        if(type(self.__a)!=float or type(self.__b)!=float or type(self.__c)!=float):
            a='Нужно вводить только числа!'
        elif (self.__a < 0 or self.__b<0 or self.__c<0):
            a='С отрицательными числами ничего не выйдет!'
        elif(self.__a+self.__b<=self.__c or self.__b+self.__c<=self.__a or self.__a+self.__c<=self.__b):
            a='Жаль, но из этого треугольник не сделать.'
        else:
            a='Ура, можно построить треугольник!'
        return a
# a=Trianglechecker(4.0,4.0,5.0)
# print(a.is_triangle())
#______________________________

#-------------ex3--------------
class kgtopounds:
    def __init__(self,k):
        self.__kg=k
    def set_kg(self,nk):
        self.__kg=nk
    def get_kg(self):
        return self.__kg
    def to_pounds(self):
        return self.__kg*2.2
# a=kgtopounds(4)
# print(a.get_kg())
# a.set_kg(5)
# print(a.to_pounds())
# print(a.get_kg())
#______________________________

#-------------ex4--------------
class Nikola:
    def __init__(self,n,a):
        if n!='Николая':
            n=f'Я не {n}, а Николай'
        self.__n=n
        self.__a=a
    def get_n(self):
        return self.__n
# a=Nikola('Anna',18) 
# print(a.get_n()) 
#______________________________

#-------------ex5--------------
class RealString:
    def __init__(self,a):
        self.__s=a
    def __lenght(self,b):
        if len(self.__s)>len(b):
            return self.__s
        elif(len(self.__s)<len(b)):
            return b
        else:
            return 'equal'
    def lenght(self,b):
        if type(b)==RealString:
            return self.__lenght(b.__s)
        elif(type(b)==str):
            return self.__lenght(b)
        else:
            return 'should be str or Realstring type'
# a=RealString('Anna')
# b=RealString('Anahit')
# c='Anahit'
# print(a.lenght(b))
# print(a.lenght(c))
#______________________________

#-----------lesson36-----------

#-------------ex1--------------
from math import pi
class corona:
    def __init__(self,t) -> None:
        self.t=t
    def is_corona(self):
        a=self.t*pi
        if a-int(a)<=0.5:
            a=int(a)+1
        else:
            a=int(a)
        if (120<=a<=128):
            return 'You Have coronavirus'
        return 'Everything is ok'
# a=corona(40.74)
# print(a.is_corona())
#______________________________

#-------------ex2--------------
class widespreed:
    def __init__(self,n) -> None:
       dic={'ajs':1,'bkt':2,'clu':3,'dmv':4,'enw':5,'fox':6,'gpy':7,'hqz':8,'ir':9}
       s=0
       n=n.lower()
       for i in n:
           for j in dic:
               if i in j:
                   s+=dic[j]
                   break
       self.__s=s
    def if_widespreed(self):
        if (self.__s)**0.5<5:
            return "Yes"
        return 'No'
# a=widespreed('Shakira')
# print(a.if_widespreed())
#______________________________

#--------------ex3-------------
from random import choice
class HPvsV:
    def __init__(self,f,s,t) -> None:
        self.f=f
        self.s=s
        self.t=t
    def fight(self,a=choice(['Avada Kedavra', 'Crucio', 'Imperio']),b=choice(['Avada Kedavra', 'Crucio', 'Imperio']),c=choice(['Avada Kedavra', 'Crucio', 'Imperio'])):
        s=0
        if a==self.f:
            s+=1
        if b==self.s:
            s+=1
        if c==self.t:
            s+=1
        if s>=2:
            return f'Harry won :)\nHarry-> 1){self.f}, 2){self.s}, 3){self.t}\nVoldemort-> 1){a}, 2){b}, 3){c}'
        return f'Voldemort won :(\nHarry-> 1){self.f}, 2){self.s},3) {self.t}\nVoldemort-> 1){a}, 2){b}, 3){c}'
# a=HPvsV('Imperio','Crucio','Imperio')
# print(a.fight())
#______________________________