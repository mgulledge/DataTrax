from iptcinfo import IPTCInfo
from datetime import date, timedelta
import sys, MySQLdb, os

def captioner(person, yesterday):
    # >> the captioning 
    filename = person[0]
    firstname = person[1]
    lastname = person[2]
    offense = person[3]
    
    fn = "mugs/%s" % (filename)
    print "FILENAME:"
    print filename
    print firstname
    print lastname
    print offense

    info = IPTCInfo(fn, force=True)

    # call the sql for the mug

    # note there needs to be a lot more caption stuff here 
    info.data['caption/abstract'] = "%s %s was booked into the Greene County jail on %s. Offenses as listed by the jail upon booking, starting with warrant number, level of offense, the offense and the bond amount: %s" % (firstname, lastname, yesterday, offense)
    info.data['by-line'] = "Greene County Jail"

    # create the directory to save the file
    saveAsDir = "./dailymugs/%s" % (yesterday)

    if not os.path.exists(saveAsDir):
        os.makedirs(saveAsDir)

    # save the file 
    saveasName = "%s/%s" % (saveAsDir, filename)

    info.saveAs(saveasName)




# >> find yesterday's date
yesterday = date.today() - timedelta(1)

# datetime to string
date = yesterday.strftime("%Y-%m-%d")

# >> call mysql to find mug names for that day

# Open database connection
db = MySQLdb.connect("127.0.0.1","greeneco_python","gcnl!342342342343","greeneco")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# call for the list of mugs

print date

call = "SELECT mugshot, firstname, lastname, offense from inmate where DATE(in_time) = '%s'" % (date)
cursor.execute(call)
data = cursor.fetchall()

for person in data:
    try:
        captioner(person, yesterday)
    except:
        print "ERROR: Did not write the photo correctly."

