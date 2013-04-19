import os, os.path, urllib, urllib2

jpegs = []
##for root, dirs, files in os.walk('mugs'):
##    for file in files:
##    	if file.endswith('.jpg'):
##    		dirc.append(file)

for f in os.listdir( 'mugs' ):
    #checking to see if the extension is .xml and that the first character is not a .
    if f.split( "." )[ -1 ] == "jpg" and f[0] != ".":
            jpegs.append(f)
print jpegs


print "Working on cleaning mugs"

count = 0
#while count > 0:
for jpeg in jpegs:
    if (os.path.getsize("mugs/" + jpeg) == 0):
        print jpeg
        name = jpeg.split('_')
        greenecoID = name[2].split('.')[0]
        imgurl = "http://www.greenecountymo.org/sheriff/picture.php?id=%s" % (greenecoID)
        urllib.urlretrieve(imgurl, "mugs/"+jpeg)
    else:
        print "%s OK" % (count)
        
    count += 1
    
