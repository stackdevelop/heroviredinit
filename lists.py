names = []
feedbacks = []
for i in range(1, 6):
    name = input(f"Enter the name of participant {i}: ")
    names.append(name)   
    while True:
        feedback = int(input(f"Enter the feedback of participant {i} (from 1 to 5): "))
        if 1 <= feedback <= 5:
            feedbacks.append(feedback)
            break
        else:
            print("Feedback must be between 1 and 5. Please try again.")
average_feedback = sum(feedbacks) / len(feedbacks)
print("\nFeedback summary:")
for i in range(5):
    print(f"Participant {names[i]} gave a feedback of {feedbacks[i]}")

print(f"\nThe average feedback is: {average_feedback:.2f}")
