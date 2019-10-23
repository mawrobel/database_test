from initdata import Anastasia, John
import shelve

db = shelve.open("people-shelve")
db['Anastasia'] = Anastasia
db['John'] = John
db.close()
