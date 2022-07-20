'''
This file reads rolling.txt and 
returns a list of absent students
'''
#absent-student_data

def a_student_data():
  with open('rolling.txt' , 'r') as r:
    data=r.read().strip()
  
  data=data[:-1]
  absent_students=list(set(data.split(",")))
  
  return absent_students
