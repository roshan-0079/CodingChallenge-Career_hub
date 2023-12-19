from dao.applicant import Applicant as a
from dao.company import Company as c
from dao.jobListing import JobListing as jl
from dao.jobApplication import JobApplication as ja

a1 = a()
c1 = c()
jl1 = jl()
ja1 = ja()


def insertJobListing():
    jl.insert(self=a1)


def insertCompany():
    c.insert(c1)


def insertApplicant():
    a.insert(a1)


def insertJobApplication():
    ja.insert(ja1)


def getJobListings():
    data = jl.select(jl1)
    for i in data:
        print(i)


def getCompanies():
    data = c.select(c1)
    for i in data:
        print(i)


def getApplicants():
    data = a.select(a1)
    for i in data:
        print(i)


def getApplicantsForJob():
    ja.getApplicants(ja1)


def salaryBasedJobs():
    jl.jobsBasedOnSalary(jl1)