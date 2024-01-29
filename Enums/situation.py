from enum import Enum

class Situation(Enum):
    ABSCENCE_FAILED = 'Reprovado por Falta'
    GRADE_FAILED = 'Reprovado por Nota'
    FINAL_EXAM = 'Exame Final'
    APROVED = 'Aprovado'