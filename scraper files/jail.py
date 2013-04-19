# classes for the jail app

class Offense:
    def __init__(self,greenecoid,jailid,warrantno,level,offense,bond):
        self.greenecoid = greenecoid
        self.jailid = jailid
        self.warrantno = warrantno
        self.level = level
        self.offense = offense
        self.bond = bond

    def stringline(self):
        return self.warrantno + ", " + self.level + ", " + self.offense + ", " + self.bond + ";"

    def generateQuery(self):
        query = "INSERT INTO OFFENSES (greenecoid, jailid, warrantNo, offense, bond, offenseLevel) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (self.greenecoid, self.jailid, self.warrantno, self.offense, self.bond, self.level)
        print query
        return query

