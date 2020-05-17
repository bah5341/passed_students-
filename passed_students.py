import csv

file = open('COA_LTC_Falls_and_Fall_Prevention_Post_Test.csv', 'r') 

student_records = csv.DictReader(file) 

passed_students = []

for record in student_records:
    if float(record['SC0']) > 79.99: 
        passed_students.append(record['Q2_2'])

print(passed_students)