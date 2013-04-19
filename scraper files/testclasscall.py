from jail import Offense
import urllib2, re, csv, MySQLdb, urllib

# Open database connection
db = MySQLdb.connect("127.0.0.1","greeneco_python","gcnl!342342342343","greeneco")

# prepare a cursor object using cursor() method
cursor = db.cursor()

t = Offense('1300962356','104609','1231CR05586-CC3', 'F','DRUG VIO/POSS RSMO 195.202','0')

try:
    print t.generateQuery()
except:
    print "ERROR"
    
cursor.execute(str(t.generateQuery()))
db.commit()
db.close;


