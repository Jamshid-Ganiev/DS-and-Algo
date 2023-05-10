def array2D(row, column):
    array = []
    for i in range(row):
        col = []
        for j in range(column):
            col.append('')
        array.append(col)
    return array


filename = 'grades.txt'

# Open the text file for reading
gradeFile = open(filename, 'r')

# Extract the first two values which indicate the size of the 2D array
numExams = int(gradeFile.readline())
numStudents = int(gradeFile.readline())

# Create 2D array to store grades
examGrades = array2D(numStudents, numExams)

# Extract the grades from the remaining lines
i = 0
j = 0
for student in gradeFile:
    if i > 2:
        i = 0
    grades = student.split()
    for k in range(3):
        examGrades[i][j] = int(grades[k])
        i += 1
    j += 1
# Close the thext file
gradeFile.close()

# Computing each students average grade
for i in range(numStudents):
    # tally the exam grades fro each student
    total = 0
    for j in range(numExams):
        total += examGrades[i][j]

    examAvg = total / numExams
    print(f"Average score of Student numer {i+1}: {examAvg}")

