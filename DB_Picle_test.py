from initdata import db
import pickle

"i'm Pickling record from .txt file"

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
"printing record in console"
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, "=>\n", db[key])
dbfile.close()

"Make separate .pkl file for all records from initdata"

from initdata import Anastasia, John
for (key, record) in [('Anastasia', Anastasia), ('John', John)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()

"Modify Anastasia's record"
Anafile = open('Anastasia.pkl', 'rb')
Ana = pickle.load(Anafile)
Anafile.close()

Ana['age'] += 1
Anafile = open('Anastasia.pkl', 'wb')
pickle.dump(Ana, Anafile)
Anafile.close()


