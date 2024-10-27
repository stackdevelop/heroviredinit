feedback_sum = 0
num_participants = 5
for i in range(1, num_participants + 1):
    feedback = int(input(f"Enter the feedback of participant {i}: "))
    feedback_sum += feedback
average = feedback_sum / num_participants
print("The average feedback is", average)
if average > 41:
    print("Very good")
elif average > 3:
    print("Average feedback is average")
elif average > 2:
    print("Average feedback is bad")
else:
    print("Replace the teacher")
