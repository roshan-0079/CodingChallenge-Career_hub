from util.dbConnection import dbConnection
from exception.exceptions import SalaryCalculationException


class JobListing(dbConnection):
    def create(self):
        query = '''CREATE TABLE IF NOT EXISTS JobListing (
                    JobID INT PRIMARY KEY,
                    CompanyID INT,
                    JobTitle VARCHAR(255),
                    JobDescription VARCHAR(255),
                    JobLocation VARCHAR(255),
                    Salary INT,
                    JobType VARCHAR(50),
                    PostedDate DATE,
                    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID) ON DELETE CASCADE)'''
        self.execute(query)

    def insert(self):
        jobID = int(input("Enter Job ID: "))
        companyID = int(input("Enter Company ID: "))
        jobTitle = input("Enter Job Title: ")
        jobDescription = input("Enter Job Description: ")
        jobLocation = input("Enter Job Location: ")
        salary = int(input("Enter Salary: "))
        jobType = input("Enter Job Type (e.g., Full-time, Part-time, Contract): ")
        postedDate = input("Enter Posted Date (YYYY-MM-DD): ")
        self.query = f'''INSERT INTO JOBLISTING VALUES
                    ({jobID},{companyID},'{jobTitle}',
                    '{jobDescription}','{jobLocation}',{salary},'{jobType}','{postedDate}')'''
        try:
            self.execute(self.query)
        except Exception as e:
            print(str(e) + '---JOB ID EXISTS---')

    def select(self):
        query = '''SELECT * FROM JOBLISTING'''
        data = self.excute_return(query)
        return data

    def update(self):
        jobID = int(input("Enter Job ID: "))
        companyID = int(input("Enter Company ID: "))
        jobTitle = input("Enter Job Title: ")
        jobDescription = input("Enter Job Description: ")
        jobLocation = input("Enter Job Location: ")
        salary = int(input("Enter Salary: "))
        jobType = input("Enter Job Type (e.g., Full-time, Part-time, Contract): ")
        postedDate = input("Enter Posted Date (YYYY-MM-DD): ")
        data = [(companyID, jobTitle, jobDescription, jobLocation, salary, jobType, postedDate, jobID)]
        query = f'''UPDATE JOBLISTING 
                    SET companyID = %s, jobTitle = %s, jobDescription = %s,
                    jobLocation = %s, salary = %s, jobType = %s, postedDate = %s
                    WHERE JOBID = %s'''
        self.execute_many(query, data)

    def delete(self):
        ID = int(input("Enter job ID : "))
        query = f'''DELETE FROM JOBLISTING WHERE JOBID = {ID}'''
        self.execute(query)

    # METHODS
    def getJob(self):
        ID = int(input("Enter Company ID : "))
        query = f'''select * from joblisting where companyID = {ID}'''
        data = self.excute_return(query)
        for i in data:
            print(i)

    def jobsBasedOnSalary(self):
        low = int(input('Enter least package you would work for : '))
        high = int(input('Enter highest package you expect : '))
        query = f'''SELECT * FROM JOBLISTING WHERE SALARY BETWEEN {low} AND {high}'''
        data = self.excute_return(query)
        try:
            if data != []:
                for i in data:
                    print(i)
            else:
                raise SalaryCalculationException
        except SalaryCalculationException as e:
            print(e)