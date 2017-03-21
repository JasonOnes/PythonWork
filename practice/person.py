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
    

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Brown', 'dev', 100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.job)
    sue.pay *= 1.10
    print('%.2f'% sue.pay)
    sue.giveRaiseto(0.05)
    print(sue.pay)
    print(bob.lastName())
    print(bob)
    print(sue)
