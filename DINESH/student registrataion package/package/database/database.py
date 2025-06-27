from package.studentregistration import student_registration
from package.studentsearch import student_search

data = []

def add_students(student_list):
    
    data.extend(student_list)

def get_all_students():
    
    return data
