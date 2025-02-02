class ClassNotFoundError(Exception):
    def __init__(self, course, number, crn):
        self.course = course
        self.number = number
        self.crn = crn

    def __str__(self):
        return f"{self.course} {self.number} with CRN {self.crn} not found"


class InvalidNumberError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} must be a number"
