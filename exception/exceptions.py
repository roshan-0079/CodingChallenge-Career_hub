class InvalidEmailFormatException(Exception):
    def __init__(self, msg="INVALID EMAIL FORMAT"):
        super().__init__(msg)


class SalaryCalculationException(Exception):
    def __init__(self, msg="SORRY, NO JOBS FOUND IN THE PROVIDED RANGE"):
        super().__init__(msg)


class FileUploadException(Exception):
    pass


class ApplicationDeadlineException(Exception):
    pass


class DatabaseConnectionException(Exception):
    pass
