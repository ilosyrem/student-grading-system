# print("hello students come and see your grades")
# student_name = input("Enter your name: ")
# print(f"Hello, {student_name}! Welcome to the student grading portal.")
# passed= score != "F"
# status = "passed" if passed else "failed"
def find_grade(score):
    if score >= 80 and score <= 100:
        return "A"
    elif score >= 70 and score < 80:
        return "B"
    elif score >= 60 and score < 70:
        return "C"
    elif score >= 50 and score < 60:
        return "D"
    else:
        return "F"

def analize_grade():
    name= input("Enter your name: ")
    grades = {}
    subjects = ["Math", "Science", "English"]
    for subject in subjects:
        score =float(input(f"Enter your score for {subject}: "))
        while score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
            score = float(input(f"Enter your score for {subject}: "))
        grades[subject] = find_grade(score)

    print(f"\n{name}'s Grades:")
    print (grades)

analize_grade()