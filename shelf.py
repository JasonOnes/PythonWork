""" Using shelve to store portfolio instances """

import shelve
from class_acts import Portfolio, Holding, StockFund, BondFund

holding_1 = StockFund(name='VTSMX', 'Domestic', 'Total', 0.7)
holding_2 = StockFund(name='VGTSX', 'Foreign', 'Mid-Cap', 0.3)
holding_3 = BondFund(name='VWAHX', 'Municipal', '5-year', 1.0)

db = shelv.open('holdtestDB')
for obj in (holding_1, holding_2, holding_3):
    db[obj.name] = obj
db.close()

""" to 'see' the database from python prompt
import glob
glob.glob('holdtest*')
print(open('holdtest.dir').read()))

import shelve
db = shelve.open('holdtestDB')
len(db)
any dictionary builtins apply Here
list(db.keys())
for key in db:
    print(key, '=>', db[key])
for key in sorted(db):
    print(key, ':', db[key])
etc. """
