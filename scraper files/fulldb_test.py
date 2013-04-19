import urllib2, re, csv, MySQLdb, urllib
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
import datetime
from email import Encoders
from bs4 import BeautifulSoup
import os
from jail import Offense #propretary 


alpha = map(chr, range(65,91))

#declare
m = []
n = []
gcid = []
i = 0
tolist = "4173806500@vtext.com, mgulledge@gannett.com, kwall@news-leader.com, jshorman@news-leader.com, 7853121854@vtext.com"
gmail_user = "snlalerts@gmail.com"
gmail_pwd = "651Boonville"
jailID = ""
height = ""
weight = ""
sex = ""
eye = ""
hair = ""
race = ""
pod = ""
charges = ""

#Inmate info lookup function

def inmatelookup(greeneID):
        try:
                global charges, jailID, height, weight, sex, eye, hair, race, pod
                print "THIS IS HITTING"
                
                offenserow = []
                response = urllib2.urlopen("http://www.greenecountymo.org/sheriff/offender.php?id=%s" % (greeneID))
                page_source = response.read()

                soup = BeautifulSoup(page_source)

                maindiv = soup.find("div", { "class" : "main-content" })

                x=0
                mytables = maindiv.findAll("table")
                headingType = []
                value = []
                for row in mytables[0].findAll('tr'):
                        #print row
                        col = row.findAll('td')
                        try:
                                if (len(col) == 2):
                                        headingType.append(col[0].string.strip())
                                        value.append(col[1].string.strip())
                        except:
                                print "ERROR --- DID NOT SPLIT."

                # at this point you could just assign the values into your variables by the
                # index

                o_row = []
                for row in mytables[1].findAll('tr'):
                        col = [] 
                        for data in row.findAll('td'):
                                if (len(data) > 0):
                                        col.append(data.string.strip())
                        o_row.append(col)

                # loop thru the charges

                offenses = len(o_row)-1
                charges = ""
                while (offenses > 0):
                        try:
                                working = ""
                                working =  '| '.join(o_row[offenses])
                                working = working.split('| ')
                                charges = charges + working[0] + ", "  + working[1] + ", " +  working[2] + ", $" +  working[3] + "; "
                               # charges = re.escape(charges)
                               # charges = [c.replace('\'s', 's') for c in charges]
                                print charges
                                offObject = Offense(greeneID, value[0], working[0], working[1], working[2], working[3])
                                print offObject.stringline()

                                cursor.execute(offObject.generateQuery())
                                db.commit()
                        except:
                                print "ERROR --- DID NOT ADD"
                        offenses = offenses - 1
                        
                # assign other values

                jailID = value[0]
                height = value[2]
                weight = value[3]
                sex = value[4]
                eye = value[5]
                hair = value[6]
                race = value[7]
                pod = value[8]

                print "values assigned"
                print jailID
                print height 
                print weight 
                print sex
                print eye
                print hair
                print race
                print pod

                returnData = [jailID, height, weight, sex, eye, hair, race, pod, charges]
                return returnData;
        except:
                print "ERROR --- MOVING TO NEXT NAME." 

# Open database connection
db = MySQLdb.connect("127.0.0.1","greeneco_python","gcnl!342342342343","greeneco")

# prepare a cursor object using cursor() method
cursor = db.cursor()

print "Working..."

# WHERE WHAT ALPHA IS SELECTED
x = 0
while (i <= 25): 
        response = urllib2.urlopen("http://www.greenecountymo.org/sheriff/list.php?search=" + alpha[i])
        page_source = response.read()
        m = m + re.findall('[A-Z]+, [A-Z]+', page_source)
        n = n + re.findall('offender.php\?id\=[0-9]+', page_source)
        i = i + 1

#parse out the ID numbers in the array
x = 0
while (x<len(m)):
        gcid = gcid + re.findall('[0-9]+', n[x])
        x = x + 1

x = 0
while (x<len(m)):
        name = m[x]
        id = n[x]
        print m[x]
        print gcid[x]
        call = "SELECT name FROM WATCH_LIST WHERE NAME='%s' AND sent = 'N'" % (name)
        cursor.execute(call)
        data = cursor.fetchone()

        if data!=None:

                def mail(to, subject, text):
                   msg = MIMEMultipart()

                   msg['From'] = gmail_user
                   msg['To'] = ",".join(tolist)
                   msg['Subject'] = subject

                   msg.attach(MIMEText(text))

                   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
                   mailServer.ehlo()
                   mailServer.starttls()
                   mailServer.ehlo()
                   mailServer.login(gmail_user, gmail_pwd)
                   mailServer.sendmail(gmail_user, to.split(","), msg.as_string())
                  # Should be mailServer.quit(), but that crashes...
                   mailServer.close()

                mail(tolist,
                   "NEWS-LEADER ALERT",
                   "%s is in the Greene County Jail. (Ignore attachment message)" % (name))
                
                print "***NEWS-LEADER ALERT*** %s is in the Greene County Jail." % (name)

                #update database

                call2 = "UPDATE WATCH_LIST SET sent = 'Y' WHERE NAME='%s'" % (name)
                cursor.execute(call2)
                data = cursor.fetchone()
                cursor.connection.commit();
                
        x = x+1

x = 0

# set all to not active first
call5 = "UPDATE inmate SET active='N'" 
cursor.execute(call5)

while (x<len(m)):
        name = m[x]
        new_name = name.split(', ')
        lastname = new_name[0]
        firstname = new_name[1]
        greenecoID = gcid[x]
# NOTE CHANGE MADE HERE FOR WORK
        call = "SELECT * FROM inmate WHERE gcid='%s'" % (greenecoID)
        cursor.execute(call)
        data = cursor.fetchone()

        d=datetime.datetime.now()
 
        # datetime to string
        time = d.strftime("%Y-%m-%d %H:%M:%S")
        
      #  if the inmate is currently being held

        if data!=None:
               
                call4 = "UPDATE inmate SET last_seen='%s', active='Y' WHERE gcid = '%s'" % (time, greenecoID)
                cursor.execute(call4)
                print greenecoID, lastname

        # now insert the new rows 
        if data==None:

                print "INMATE LOOKUP ******************************"
                try:
                        returndata = inmatelookup(greenecoID)
                        print "RETURN DATA"
                        print returndata
                except:
                        print "ERROR: Moving to next name."
                
                #pull in mug
                imgurl = "http://www.greenecountymo.org/sheriff/picture.php?id=%s" % (greenecoID)
                imgname = "mugs/%s_%s_%s.jpg" % (lastname, firstname, greenecoID)
                imgnamedb = "%s_%s_%s.jpg" % (lastname, firstname, greenecoID)
                urllib.urlretrieve(imgurl, imgname)
                try:
                        call3 = "INSERT INTO inmate (LastName, FirstName, height, weight, sex, eye, hair, race, pod, offense, active, in_time, last_seen, mugshot, gcid, jailID) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','Y','%s','%s','%s','%s','%s')" % (lastname, firstname, height, weight, sex, eye, hair, race, pod, charges, time, time, imgnamedb, greenecoID, jailID)
                        cursor.execute(call3)

                        db.commit()
                        print "NEW: %s %s" % (greenecoID, lastname)
                except:
                        print "+~+~+~+~+~+~++~+~ERROR+~+~+~+~+~+~+~+~+~+~"


        
        x=x+1

db.commit()
db.close()


