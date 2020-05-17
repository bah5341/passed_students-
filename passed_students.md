## First you want to import your CSV from Qualtrics or whatever software you are using.

import csv

## Next you want to open the CSV that you would like to work with and indicate that you would like to read ('r') the file. 

file = open('COA_LTC_Falls_and_Fall_Prevention_Post_Test.csv', 'r') 

## Now you need to give your CSV a name and create your dictionary to work with. I called my file student_records since I am working with student grades. 

student_records = csv.DictReader(file) 

## Next, we need to create an empty repository for our passed students list to populate in! Here I use the name "passed_students" to create the empty list. 

passed_students = []

## Next you want to dig in to your student_records (your CSV) to find the data that you need. For me, I wanted to find the students that received a score higher than 79.99 (our parameters for passing the course) on their post test. In this code "SC0" is equal to the column with student scores and "Q2_2" is the column that with student last names. It is important to note that in order to pull the scores I needed to create a float. Lastly, in order to add the records to the empty list you created, you must append the record you are looking for (in this case the student last names) into passed_students (our empty list).

for record in student_records:
    if float(record['SC0']) > 79.99: 
        passed_students.append(record['Q2_2'])

## Finally you need to print your list (passed_students), which is no longer empty. Yey!

print(passed_students)

# If you are interested in also getting the names of the students who have failed you can run the code above by creating a failed_students empty list and changing the float parameters (instead of > 79.99 in my case I would put < 80.00) and re-run the code. 