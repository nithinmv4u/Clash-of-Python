import random

# class Trial:
#     def __init__(self):
#         self.places=['nilambur','banglore','kozhikode','thrissur']
        
#     def sort(self,name):
#         print(name, 'is in', random.choice(self.places))

# trial=Trial()
# trial.sort('Harry')

class Trial:
    places=['nilambur','banglore','kozhikode','thrissur']

    @classmethod
    def sort(cls,name):
        print(name, 'is in' ,random.choice(cls.places))

Trial.sort('harry')