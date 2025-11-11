class Student:
    def __init__(self, grades=None):
        if grades is None:
            self.grades = []
        else:
            self.grades = grades
        self.count_grades = len(self.grades)
        self.academic_average = (
            sum(self.grades) / len(self.grades) if self.grades else 0
        )

    def add_grade(self, grade):
        if grade < 0 or grade > 20:
            raise InvalidGrade("Grade should be between 0 and 20")
        self.grades.append(grade)
        self.academic_average = sum(self.grades) / len(self.grades)


class InvalidGrade(Exception):
    pass
