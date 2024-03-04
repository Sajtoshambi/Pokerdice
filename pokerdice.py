import random
def Pokerdice:
    def __init__(self):
        self.dice =[1,2,3,4,5]


    def dobas(self):
        self.dice = [random.randint(1, 6)] for i in range(5):]


    def kocka(self):
        print("Kocka", self.dice)

    def checkhand(self):
        e_érték=(
set(self.dice))
        if len(e_érték)==1:
            return "5 ugyanolyan"
        elif len(e_érték)==2
            for value in e_érték:
         if self.dice.count(value)==4:
            return ("4 ugyanolyan"
                            "Full Haus")
         elif len(e_érték)==5:
             return print("High card")
         else:
             print("Érvénytelen leosztás")


