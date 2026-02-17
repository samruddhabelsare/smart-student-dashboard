import pandas as pd
import numpy as np
import random

np.random.seed(42)

names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Kunal", "Rohan", "Rahul",
    "Sanya", "Ananya", "Isha", "Neha", "Pooja", "Kavya", "Aditi"
]

departments = ["CSE", "IT", "ECE", "EEE", "MECH", "CIVIL"]
genders = ["Male", "Female"]

data = []

for i in range(1, 101):
    data.append({
        "Student_ID": f"STU{i:03d}",
        "Name": random.choice(names),
        "Gender": random.choice(genders),
        "Age": random.randint(18, 24),
        "Department": random.choice(departments),
        "Year": random.choice([1, 2, 3, 4]),
        "CGPA": round(random.uniform(5.0, 9.8), 2),
        "Attendance_Percent": random.randint(60, 100),
        "Math_Score": random.randint(40, 100),
        "Science_Score": random.randint(40, 100),
        "English_Score": random.randint(40, 100),
        "Programming_Score": random.randint(40, 100),
        "Backlogs": random.randint(0, 3),
        "Internship": random.choice(["Yes", "No"]),
        "Placement_Status": random.choice(["Placed", "Not Placed"])
    })

df = pd.DataFrame(data)
df.to_csv("students_data.csv", index=False)

print("students_data.csv created successfully!")
