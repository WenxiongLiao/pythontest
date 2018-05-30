class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print('Hi my name is' + self.name)
        print('Hi my grade is' + str(self.grade))

    def impove(self,amount):
        self.grade = self.grade + amount

jim = Student('jim',86)
jim.introduce()

jim.impove(10)
jim.introduce()