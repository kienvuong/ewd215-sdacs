# import pymysql
#
# class Pool:
#     def __init__(self):
#         self.conn = pymysql.connect(host='localhost', port=3306, db='testDB', user='root', password='0856')
#
#     def cursorFetchall(self, sql):
#         with self.conn.cursor() as cursor:
#             cursor.execute(sql)
#             self.conn.commit()
#             return cursor.fetchall()
#
#     def cursorRows(self, sql):
#         with self.conn.cursor() as cursor:
#             rows = cursor.execute(sql)
#             self.conn.commit()
#             return rows
#
#     def checkAmountofUsers(self):
#         sql = "SELECT * FROM `users`"
#         try:
#             return self.cursorFetchall(sql)
#         except pymysql.MySQLError as error:
#             print(error)
#
#     def insertUser(self, userName, userPwd):
#         sql = f"INSERT INTO `users`(`userName`, `userPwd`) VALUES ('{userName}', '{userPwd}')"
#         try:
#             if self.cursorRows(sql) >= 1:
#                 return True
#             else:
#                 return False
#         except pymysql.MySQLError as error:
#             print(error)
#
# if __name__ == '__main__':
#     for i in Pool().checkAmountofUsers():
#         print(i)
#     print(Pool().insertUser('kien', 'kien'))
#-----------------------------------------------------------------------------------------------------


