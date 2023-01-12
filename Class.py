class Posi_list(list):
    def append(self, new_elem):
        self.new_elem = new_elem
        if type(self.new_elem) == int and self.new_elem >= 0:
            super().append(new_elem)
        else:
            pass

class Student():
    def __init__(self, first_name='', last_name='', score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score

