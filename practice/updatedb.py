import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t=>', db[key])

sue = db['Sue Brown'] #fetch
sue.giveRaiseto(.12) #update
db['Sue Brown'] = sue #updates
db.close()
