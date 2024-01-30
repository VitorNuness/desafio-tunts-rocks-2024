from math import ceil
from Enums.situation import Situation
from student import Student

def test_add_grade():
    student = Student(1, "Vitor", 0)
    student.add_grade(80)
    assert student.grades == [80]

def test_calculate_average():
    student = Student(1, "Vitor", 0)
    student.grades = [70, 80, 90]
    assert student.calculate_average() == ceil((70 + 80 + 90) / 3)

def test_calculate_average_empty_grades():
    student = Student(1, "Vitor", 0)
    assert student.calculate_average() == 0

def test_calculate_percentual_absences():
    student = Student(1, "Vitor", 5)
    assert student.calculate_percentual_absences(20) == ceil((5 / 20) * 100)

def test_calculate_situation_absence_failed():
    student = Student(1, "Vitor", 30)
    student.calculate_percentual_absences(20)
    student.calculate_situation()
    assert student.situation == Situation.ABSCENCE_FAILED.value
    assert student.final_situation == 0

def test_calculate_situation_grade_failed():
    student = Student(1, "Vitor", 10)
    student.grades = [40, 45, 30]
    student.calculate_average()
    student.calculate_situation()
    assert student.situation == Situation.GRADE_FAILED.value
    assert student.final_situation == 0

def test_calculate_situation_final_exam():
    student = Student(1, "Vitor", 5)
    student.grades = [60, 65, 70]
    student.calculate_average()
    student.calculate_situation()
    assert student.situation == Situation.FINAL_EXAM.value
    assert student.final_situation == 100 - student.average

def test_calculate_situation_approved():
    student = Student(1, "Vitor", 5)
    student.grades = [80, 85, 90]
    student.calculate_average()
    student.calculate_situation()
    assert student.situation == Situation.APROVED.value
    assert student.final_situation == 0
