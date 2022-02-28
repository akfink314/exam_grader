def grade(split_line):
    student_answers = split_line
    raw_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = raw_key.split(',')
    grade = 0
    count = 0
    while count < 25:
        if student_answers[count] == answer_key[count]:
            grade += 4
            count += 1
        elif student_answers[count] == '':
            grade += 0
            count += 1
        else:
            grade -= 1
            count += 1
    return grade

filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")
while True:
    try:
        file = open(filename + ".txt")
        Lines = file.readlines()
        print("Successfully opened " + filename + ".txt")
        print()
        break
    except:
        print("Sorry, I can't find this file!")
        filename = input("Enter a filename: ")
        continue
counter = 0
num_lines = 0
num_invalid = 0
num_valid = 0

print("**** ANALYZING ****")
print()
valid_grades = []
valid_names = []
for raw_line in Lines:
    num_lines += 1
    line = raw_line.strip()
    split_line = line.split(',')
    student_ID = split_line[0]
    split_line.pop(0)
    #print(split_line)
    #print(student_ID)
    #error checking student id
    if student_ID[0] == 'N':
        student_ID = student_ID[1:]
        if len(student_ID) != 8:
            num_invalid += 1
            print("Invalid line of data: N# is invalid")
            print(raw_line)
            continue
        else:
            if student_ID.isdigit() == False:
                num_invalid += 1
                print("Invalid line of data: N# is invalid")
                print(raw_line)
                continue
    else:
        num_invalid += 1
        print("Invalid line of data: N# is invalid")
        print(raw_line)
        continue
        
    #error checking answers
    if len(split_line) != 25:
        num_invalid += 1
        print("Invalid line of data: does not contain exactly 26 values:")
        print(raw_line)
        continue
    else:
        student_grade = grade(split_line)
        valid_grades.append(student_grade)
        valid_names.append(student_ID)
        
if num_invalid == 0:
    print("No errors found!")

print("**** REPORT ****")
print()
num_valid = num_lines - num_invalid
print("Total valid lines of data:", num_valid)
print("Total invalid lines of data:", num_invalid)
print()

highest_grade = max(valid_grades)
lowest_grade = min(valid_grades)
grade_range = highest_grade - lowest_grade
average = sum(valid_grades) / len(valid_grades)

sorted_grades = valid_grades.copy()
sorted_grades.sort()
#if num grades is even
if len(sorted_grades) % 2 == 0:
    middle_upper = int(len(sorted_grades)/2)
    median = (sorted_grades[middle_upper] + sorted_grades[middle_upper - 1])/2
else:
    middle = int(len(sorted_grades)/2)
    median = sorted_grades[middle]

print("Mean (average) score: ", round(average, 2))
print("Highest score: ", highest_grade)
print("Lowest score: ", lowest_grade)
print("Range of scores: ", grade_range)
print("Median score: ", median)

new_name = filename + "classgrades.txt"

with open(new_name, 'w') as new_file:
    counter = 0
    valid = len(valid_grades)
    while counter < valid:
        new_file.write('N' + valid_names[counter] + ", " + str(valid_grades[counter]))
        counter += 1
        
