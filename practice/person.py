""" getting the classy juices flowing"""


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

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaiseto(self, percent, bonus=0.10):
        """bad way self.pay = int(self.pay * (1+ percent + bonus))"""
        Person.giveRaiseto(self, percent + bonus) #augment = good

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaiseto(self, percent):
        for person in self.members:
            person.giveRaiseto(person)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Brown', 'dev', 100000)
    # print(bob.name, bob.pay)
    # print(sue.name, sue.job)
    # sue.pay *= 1.10
    # print('%.2f'% sue.pay)
    # sue.giveRaiseto(0.05)
    # print(sue.pay)
    # print(bob.lastName())
    # print(bob)
    # print(sue)
    tom = Manager('Tom Beringer', 45000)
    # print(tom.pay)
    # tom.giveRaiseto(0.10)
    # print(tom.pay)
    # print(tom.lastName())
    # print(tom)
    development = Department(bob, sue)
    development.addMember(tom)
    #development.giveRaiseto(0.10)
    development.showAll
