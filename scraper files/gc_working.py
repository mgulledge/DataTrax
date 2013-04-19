import urllib2, re, csv, MySQLdb
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

alpha = map(chr, range(65,91))

#declare
m = []
i = 0
#, 4172343322@vtext.com
tolist = "4173806500@vtext.com, mgulledge@gannett.com, kwall@news-leader.com, jshorman@news-leader.com, 7853121854@vtext.com"
gmail_user = "snlalerts@gmail.com"
gmail_pwd = "651Boonville"




# Open database connection
db = MySQLdb.connect("127.0.0.1","greeneco_python","gcnl!342342342343","greeneco" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
cursorUP = db.cursor()

print "Working..."

while (i <= 25): 
        response = urllib2.urlopen("http://www.greenecountymo.org/sheriff/list.php?search=" + alpha[i])
        page_source = response.read()
        m = m + re.findall('[A-Z]+, [A-Z]+', page_source)
        i = i + 1

x = 0
while (x<len(m)):
        name = m[x]
        call = "SELECT name FROM WATCH_LIST WHERE (NAME='%s' AND sent='N')" % (name)
        cursor.execute(call)
        data = cursor.fetchone()

        if data!=None:

                # send out alert
                
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
                   "%s is in the Greene County jail." % (name))
                
                #update database

                call2 = "UPDATE WATCH_LIST SET sent = 'Y' WHERE NAME='%s'" % (name)
                cursorUP.execute(call2)
                data2 = cursorUP.fetchone()
                cursorUP.connection.commit();
                
                
        x = x+1
db.close()

        


