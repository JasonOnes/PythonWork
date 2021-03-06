""" getting the classy juices flowing  using person template as a means
to experiment with __getattr__ and embedding a class to make a composite"""


# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaiseto(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#     def __repr__(self):
#         return '[Person: {}, {}]'.format(self.name, self.pay)

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]
    def giveRaiseto(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: {}, {}]'.format(self.name, self.pay)

class Manager:  #notice no (Person) inheritance
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaiseto(self, percent, bonus=.10):
        self.person.giveRaiseto(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __repr__(self):
        return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaiseto(self, percent):
        for person in self.members:
            person.giveRaiseto(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Brown', 'dev', 100000)

    tom = Manager('Tom Beringer', 45000)

    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaiseto(.10)
    development.showAll()
