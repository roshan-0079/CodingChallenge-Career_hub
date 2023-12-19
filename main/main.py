from dao import databaseManager as db

while True:
    print("\n select 1 to post a job")
    print(" 2 for enrolling a company")
    print(" 3 for enrolling as an applicant")
    print(" 4 to apply for a job")
    print(" 5 to see the available jobs")
    print(" 6 to see all the companies")
    print(" 7 to see all applicants")
    print(" 8 to see applicants for specific job")
    print(" 9 to see jobs according to salary ranges")
    print(" 10 to exit")
    s = input("Enter your choice : ")
    if s == '1':
        try:
            db.insertJobListing()
        except Exception as e:
            print(str(e))
    elif s == '2':
        try:
            db.insertCompany()
        except Exception as e:
            print(str(e))
    elif s == '3':
        try:
            db.insertApplicant()
        except Exception as e:
            print(str(e))
    elif s == '4':
        try:
            db.insertJobApplication()
        except Exception as e:
            print(str(e))
    elif s == '5':
        try:
            db.getJobListings()
        except Exception as e:
            print(str(e))
    elif s == '6':
        try:
            db.getCompanies()
        except Exception as e:
            print(str(e))
    elif s == '7':
        try:
            db.getApplicants()
        except Exception as e:
            print(str(e))
    elif s == '8':
        try:
            db.getApplicantsForJob()
        except Exception as e:
            print(str(e))
    elif s == '9':
        try:
            db.salaryBasedJobs()
        except Exception as e:
            print(str(e))
    elif s == '10':
        print("*"*30 + " THANK YOU FOR USING CAREER HUB " + "*"*30)
        break
    else:
        print("Invalid choice")
