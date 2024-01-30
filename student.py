from math import ceil
from dataclasses import dataclass, field
from Enums.situation import Situation

@dataclass
class Student:
    """
    Represents a student with information such as student ID, name, absences, grades, etc.
    
    Attributes:
    - student_id (int|str): The ID of the student.
    - name (str): The name of the student.
    - absences (int): The number of absences.
    - grades (list[int]): A list of grades.
    - percentual_absences (int): The percentage of absences.
    - average (int): The average of grades.
    - situation (str): The situation of the student.
    - final_situation (int): The final grade of the student.

    Methods:
    - add_grade(grade: int) -> list[int]:
        Adds a grade to the student's list of grades.

    - calculate_average() -> int:
        Calculates the average of the student's grades.

    - calculate_percentual_absences(classes_total: int) -> int:
        Calculates the percentage of absences for the student.

    - calculate_situation() -> str:
        Calculates the student's situation based on absences and grades.
    """

    student_id: int|str
    name: str
    absences: int

    grades: list[int] = field(default_factory=list)
    percentual_absences: int = 0
    average: int = 0
    situation: str = ''
    final_situation: int = 0

    def add_grade(self, grade: int) -> list[int]:
        """
        Adds a grade to the student's list of grades.

        Parameters:
        - grade (int): The grade to be added.

        Returns:
        - list[int]: Updated list of grades.
        """
        self.grades.append(grade)
        return self.grades

    def calculate_average(self) -> int:
        """
        Calculates the average of the student's grades.

        Returns:
        - int: The calculated average.
        """
        if len(self.grades) == 0:
            self.average = 0
            return self.average
        grandes_sum = sum(self.grades)
        grades_total = len(self.grades)
        self.average = ceil(grandes_sum / grades_total)
        return self.average

    def calculate_percentual_absences(self, classes_total: int) -> int:
        """
        Calculates the percentage of absences for the student.

        Parameters:
        - classes_total (int): Total number of classes.

        Returns:
        - int: Percentage of absences.
        """
        self.percentual_absences = ceil((self.absences / classes_total) * 100)
        return self.percentual_absences

    def calculate_situation(self) -> str:
        """
        Calculates the student's situation based on absences and grades.

        Returns:
        - str: The student's situation.
        """
        if self.percentual_absences > 25:
            self.situation = Situation.ABSCENCE_FAILED.value
            self.final_situation = 0
        elif self.average < 50:
            self.situation = Situation.GRADE_FAILED.value
            self.final_situation = 0
        elif 50 <= self.average < 70:
            self.situation = Situation.FINAL_EXAM.value
            self.final_situation = 100 - self.average
        else:
            self.situation = Situation.APROVED.value
            self.final_situation = 0
        
        return self.situation