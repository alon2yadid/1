from random import randint

class Lottery:
    def __init__(self):
        self.numbers=[]

    def rand_numbers(self):
        return [randint(1,45) for i in range(6)]

    def valid_numbers(self):
        """this function checks that the rand_numbers function returns a unique list of numbers with no duplications"""
        self.numbers=self.rand_numbers()
        # set do not allow duplicate values
        set1=set(self.numbers)
        if len(set1)==len(self.numbers):
            return True
        else:
            return False

    def valid_range(self):
        """this function checks the range of the returned list that the rand_numbers function returns"""
        list1 = self.rand_numbers()
        for i in list1:
            if i < 1 or i > 45:
                return False
            else:
                return True


    def __str__(self):
        return f"numbers: {self.numbers}"



