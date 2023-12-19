from util.dbConnection import dbConnection


class Company(dbConnection):
    def create(self):
        query = '''CREATE TABLE IF NOT EXISTS Company (
                    CompanyID INT PRIMARY KEY,
                    CompanyName VARCHAR(255),
                    Location VARCHAR(255))'''
        self.execute(query)

    def insert(self):
        companyID = int(input("Enter Company ID : "))
        companyName = input("Enter company name : ")
        location = input("Enter Location: ")
        query = f'''INSERT INTO COMPANY VALUES
                    ({companyID},'{companyName}','{location}')'''
        try:
            self.execute(query)
        except Exception as e:
            print(str(e) + '---COMPANY ID EXISTS---')

    def select(self):
        query = '''SELECT * FROM COMPANY'''
        data = self.excute_return(query)
        return data

    def update(self):
        companyID = int(input("Enter Company ID : "))
        companyName = input("Enter company name : ")
        location = input("Enter Location: ")
        data = [(companyName, location, companyID)]
        query = f'''UPDATE COMPANY 
                    SET companyNAME = %s, LOCATION = %s
                    WHERE COMPANYID = %s'''
        self.execute_many(query, data)

    def delete(self):
        ID = int(input("Enter company ID : "))
        query = f'''DELETE FROM company WHERE companyID = {ID}'''
        self.execute(query)