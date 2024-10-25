# Read the students data from the specified file.
def read_student_data(filename):
    student_data = []
    with open(filename, 'r') as file:
        num_students = int(file.readline().strip())
        for line in file:
            student_info = line.strip().split(',')
            student_data.append({
                'code': int(student_info[0]),
                'name': student_info[1],
                'course_marks': [int(x) for x in student_info[2:5]],
                'exam_mark': int(student_info[5])
            })
    return student_data

# Assigning the variable "filename" to the file studentMarks.txt
filename = 'C:\\Users\\User\\Desktop\\Exercise 3 - Student Manager\\studentMarks.txt'
students = read_student_data(filename)

# Calculate overall percentage and grade
def calculate_overall_percentage(student): # Defines a function

    total_coursework_marks = sum(student['course_marks']) # This calculates the total coursework marks.
    total_marks = total_coursework_marks + student['exam_mark'] # This calculates the total marks using total_coursework_marks + student.
    overall_percentage = (total_marks / 160) * 100 # Divides total marks and 160 then multiplies the result to 100, that is what "overall_percentage" is.

# This code checks the overall percentage depending using conditional statements.
    if overall_percentage >= 70: 
        grade = 'A'
    elif overall_percentage >= 60:
        grade = 'B'
    elif overall_percentage >= 50:
        grade = 'C'
    elif overall_percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'

    return overall_percentage, grade # Returns a tuple containing the overall percentage and assigned grade.

# This code updates the students data with the overall percentages and grades.
for student in students:
    student['overall_percentage'], student['grade'] = calculate_overall_percentage(student)

# Main Menu options.
def view_all_student_records():
    print("Student Records:")

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Student Number: {student['code']}")
        print(f"Total Coursework Mark: {sum(student['course_marks'])}")
        print(f"Exam Mark: {student['exam_mark']}")
        print(f"Overall Percentage: {student['overall_percentage']:.2f}%")
        print(f"Grade: {student['grade']}\n")

    # The summary of the entire student body.
    num_students = len(students)
    average_percentage = sum(student['overall_percentage'] for student in students) / num_students

    print(f"Number of students: {num_students}")
    print(f"Average percentage: {average_percentage:.2f}%")

view_all_student_records()