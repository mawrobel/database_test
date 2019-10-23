"printing record from shelve database"
import shelve
db = shelve.open("people-shelve")
for key in db:
    print( 24 * "-")
    print( key, ":")
    print("name <-> ", db[key]['name'])
    print("age <-> ", db[key]['age'])
    print("job <-> ", db[key]['job'])
print( 24 * "-")
print(db['John']["name"])
db.close()
print("\n\n")
"update database by add new record"
from initdata import Micki
db = shelve.open("people-shelve")
db["Micki"] = Micki
for key in db:
    print( 24 * "-")
    print(key, ":")
    print("name <-> ", db[key]['name'])
    print("age <-> ", db[key]['age'])
    print("job <-> ", db[key]['job'])
print(24 * "-")
db.close()