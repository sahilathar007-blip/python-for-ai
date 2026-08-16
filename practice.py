class student:
    def __init__(self, name, age , city , country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        
def display_student_info(student):
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"City: {student.city}")
    print(f"Country: {student.country}")
    
s1 = student("John Doe", 20, "New York", "USA")
s2 = student("Jane Smith", 22, "Los Angeles", "USA")
s3 = student("Alice Johnson", 19, "Chicago", "USA")
s4 = student("Bob Brown", 21, "Houston", "USA")

print("Student 1 Info:")
display_student_info(s1)
print("\nStudent 2 Info:")
display_student_info(s2)
print("\nStudent 3 Info:")
display_student_info(s3)
print("\nStudent 4 Info:")
display_student_info(s4)
    
        
        