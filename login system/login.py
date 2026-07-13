import time


print("hello students come and see your grades")
print("please login to see your grades")
def login_system():
    CORRECT_USERNAME = "student"
    CORRECT_PASSWORD = "password123"

    failed_attempts = 0
    delay= [5, 10, 15, 20]  
    while failed_attempts < 5:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            print("welcome to the student grading system!")
            return True
        else:
            failed_attempts += 1
            print(f"Incorrect username or password. Attempt {failed_attempts} of 5.")
            if failed_attempts < 5:
                print(f"Please wait for {delay[failed_attempts - 1]} seconds before trying again.")
                time.sleep(delay[failed_attempts - 1])

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
    marks=[]
    subjects = ["Math", "Science", "English"]
    for subject in subjects:
        score =float(input(f"Enter your score for {subject}: "))
        while score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
            score = float(input(f"Enter your score for {subject}: "))
        grades[subject] = find_grade(score)
        marks.append(score)
    avarage=sum(marks)/len(marks)
    status="pass" if avarage >= 50 else "fail"

    return{
        "name":name,
        "grades":grades,
        "avarage":avarage,
        "status":status,
    }
print("Hello students come and see your grades\n")

if login_system():
    result = analize_grade()
    print("\n--- FINAL REPORT ---")
    for key, value in result.items():
        print(f"{key}: {value}")
