"""testing shelve methods"""

from person import Person, Manager
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Brown', 'dev', 100000)
tom = Manager('Tom Beringer', 45000)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

print(db)
