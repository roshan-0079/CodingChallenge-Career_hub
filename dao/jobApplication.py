from util.dbConnection import dbConnection


class JobApplication(dbConnection):
    def create(self):
        query = '''CREATE TABLE IF NOT EXISTS JobApplication (
                    ApplicationID INT PRIMARY KEY,
                    JobID INT,
                    ApplicantID INT,
                    ApplicationDate DATE,
                    CoverLetter VARCHAR(50),
                    FOREIGN KEY (JobID) REFERENCES JobListing(JobID) ON DELETE CASCADE,
                    FOREIGN KEY (ApplicantID) REFERENCES Applicant(ApplicantID) ON DELETE CASCADE)'''
        self.execute(query)

    def insert(self):
        applicationID = int(input("Enter Application ID: "))
        jobID = int(input("Enter Job ID: "))
        applicantID = int(input("Enter Applicant ID: "))
        applicationDate = input("Enter Application Date (YYYY-MM-DD): ")
        coverLetter = input("Enter Cover Letter: ")
        query = f'''INSERT INTO JOBAPPLICATION VALUES
                    ({applicationID},{jobID},{applicantID},
                    '{applicationDate}','{coverLetter}')'''
        try:
            self.execute(query)
        except Exception as e:
            print(str(e) + '---APPLICATION ID EXISTS---')

    def select(self):
        query = '''SELECT * FROM JOBAPPLICATION'''
        data = self.excute_return(query)
        return data

    def update(self):
        applicationID = int(input("Enter Application ID: "))
        jobID = int(input("Enter Job ID: "))
        applicantID = int(input("Enter Applicant ID: "))
        applicationDate = input("Enter Application Date (YYYY-MM-DD): ")
        coverLetter = input("Enter Cover Letter: ")
        data = [(jobID, applicantID, applicationDate, coverLetter, applicationID)]
        query = f'''UPDATE JOBAPPLICATION 
                    SET jobID = %s, applicantID = %s, applicationDate = %s,
                    coverLetter = %s
                    WHERE applicationID = %s'''
        self.execute_many(query, data)

    def delete(self):
        ID = int(input("Enter applicationID : "))
        query = f'''DELETE FROM jobapplication WHERE applicationID = {ID}'''
        self.execute(query)

    # METHODS
    def apply(self):
        self.insert()

    def getApplicants(self):
        ID = int(input("Enter job ID : "))
        query = f'''select * from jobapplication where jobID = {ID}'''
        data = self.excute_return(query)
        for i in data:
            print(data)