import pymysql

class Pool():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, db='ewd215', user='ewd215', password='PxcNeyKt85QcOyot')

    def cursorFetchall(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            return cursor.fetchall()

    def cursorRows(self, sql):
        with self.conn.cursor() as cursor:
            rows = cursor.execute(sql)
            self.conn.commit()
            return rows

    def cursorKey(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            return cursor.lastrowid

    def selectAllCompaniesRecords(self):
        sql = "SELECT * FROM `companies`"
        try:
            return self.cursorFetchall(sql)
        except pymysql.MySQLError as error:
            print(error)

    def selectAllCompanies(self):
        sql = "SELECT full_name_company FROM companies WHERE `location` != ''"
        try:
            return self.tupleToList(self.cursorFetchall(sql))
        except pymysql.MySQLError as error:
            print(error)

    def checkIfCompanyExist(self, companyName, companyLocation):
        sql = f"SELECT companyID FROM companies WHERE `full_name_company` = '{companyName}' and `location` = '{companyLocation}'"
        try:
            if type(self.cursorFetchall(sql)[0][0]) == int:
                return True
        except:
            return False

    def selectCompanyAndLocation(self, companyName):
        sql = f"SELECT `full_name_company`, `location` FROM `companies` WHERE `full_name_company` = '{companyName}'"
        try:
            return self.cursorFetchall(sql)[0]
        except pymysql.MySQLError as error:
            print(error)

    def selectCompanyId(self, companyName, companyLocation):
        sql = f"SELECT companyID FROM companies WHERE `full_name_company` = '{companyName}' and `location` = '{companyLocation}'"
        try:
            return self.cursorFetchall(sql)[0][0]
        except pymysql.MySQLError as error:
            print(error)

    def tupleToList(self, tuple):
        result = [str(x) for x, in tuple]
        return result

    def insertCompany(self, companyName, companyLocation):
        sql = f"INSERT INTO `companies`(`full_name_company`, `location`) VALUES ('{companyName}', '{companyLocation}')"
        try:
            return self.cursorKey(sql)
        except pymysql.MySQLError as error:
            print(error)

    def insertStation(self, companyId, stationName):
        sql = f"INSERT INTO `stations`(`company_id`, `station_name`) VALUES ({companyId}, '{stationName}')"
        try:
            if self.cursorRows(sql) >= 1:
                return False
            else:
                return False
        except pymysql.MySQLError as error:
            print(error)



if __name__ == '__main__':
    # for i in Pool().selectAllCompaniesRecords():
    #     print(i)
    # for i in Pool().selectAllCompanies():
    #     print(i)
    pool = Pool()
    a = pool.selectCompanyId("Coolblue", "Rotterdam")
    print(pool.checkIfCompanyExist("Coolblue", "Rotterdam"))

    # print(Pool().insertUser('kien', 'kien'))
