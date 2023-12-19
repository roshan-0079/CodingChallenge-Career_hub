import mysql.connector as sql
from exception.exceptions import DatabaseConnectionException


# DATABASE CONNECTIVITY
class dbConnection:
    def getConnection(self):
        try:
            self.conn = sql.connect(host='localhost', database='career_hub', user='root', password='Shaik@123')
            self.stmt = self.conn.cursor()
        except DatabaseConnectionException as e:
            print('---DATABASE NOT FOUND---')

    def close(self):
        try:
            self.conn.close()
        except Exception as e:
            print(str(e))

    def execute(self, query):
        self.getConnection()
        self.stmt = self.conn.cursor()
        try:
            self.stmt.execute(query)
        except DatabaseConnectionException as e:
            print('---INVALID DATA---')
        else:
            self.conn.commit()
        finally:
            self.close()

    def execute_many(self, query, data):
        self.getConnection()
        self.stmt = self.conn.cursor()
        try:
            self.stmt.executemany(query, data)
        except DatabaseConnectionException as e:
            print('---INVALID DATA---')
        else:
            self.conn.commit()
        finally:
            self.close()

    def excute_return(self, query):
        self.getConnection()
        self.stmt = self.conn.cursor()
        self.stmt.execute(query)
        data = self.stmt.fetchall()
        self.close()
        return data