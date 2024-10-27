sum=0
###defining the list of dictionary for students
students=[]
userFlag="Y"
##they are connected through index
##

while(userFlag=="Y"):
    ##creating a dictionary for a new student
    student={}
    name=input("Enter the name of the student")
    student["name"]=name
 #   feedback=int(input("Enter the feedback of the student one by one"))
    feedbackAvailable=input("Do you want to provide feedback? Enter Y or N")
    if(feedbackAvailable=="Y"):
        feedback=int(input("Enter the feedback of the student one by one"))
        student["feedback"]=feedback
    else:
        feedback = 0    
    userFlag=input("Do you want to continue? Enter Y or N")
    ##adding the student to the list of students
    print(student)
    students.append(student)
    sum=sum+feedback
print(students)
average=sum/len(students)

if(average>4):
    print("Very good")
elif(average>3):
    print("Average feedback is  average")
elif(average>2):
    print("average feedback is bad")
else:
    print("replace the teacher")

print("#########Feedback of the students#########")
for student in students:
    print("the name of the student is",student["name"])
    print("the feedback of the student is",student["feedback"])

search_name = input("Enter the name of the student to search for their feedback: ")
found = False
for student in students:
    if student["name"].lower() == search_name.lower():
        print(f"Feedback for {search_name}: {student['feedback']}")
        found = True
        break

if not found:
    print("Error: Student not found.")
