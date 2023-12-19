from util.dbConnection import dbConnection


class Applicant(dbConnection):
    def create(self):
        query = '''CREATE TABLE IF NOT EXISTS Applicant (
                    ApplicantID INT PRIMARY KEY,
                    FirstName VARCHAR(50),
                    LastName VARCHAR(50),
                    Email VARCHAR(50),
                    Phone VARCHAR(20),
                    Resume VARCHAR(50))'''
        self.execute(query)

    def insert(self):
        applicantID = int(input("Enter Applicant ID: "))
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        resume = input("Enter Resume Filename or Reference: ")
        query = f'''INSERT INTO APPLICANT VALUES
                    ({applicantID},'{firstName}','{lastName}',
                    '{email}','{phone}','{resume}')'''
        try:
            self.execute(query)
        except Exception as e:
            print(str(e) + '---APPLICANT ID EXISTS---')

    def select(self):
        query = '''SELECT * FROM APPLICANT'''
        data = self.excute_return(query)
        return data

    def update(self):
        applicantID = int(input("Enter Applicant ID: "))
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        resume = input("Enter Resume Filename or Reference: ")
        data = [(firstName, lastName, email, phone, resume, applicantID)]
        query = f'''UPDATE APPLICANT 
                    SET firstName = %s, lastname = %s, email = %s,
                    phone = %s, resume = %s
                    WHERE applicantID = %s'''
        self.execute_many(query, data)

    def delete(self):
        ID = int(input("Enter APPLICANT ID : "))
        query = f'''DELETE FROM APPLICANT WHERE APPLICANTID = {ID}'''
        self.execute(query)