# Creating a dictionary of employees
employees = {
    1: {"name": "Alice Smith", "age": 30, "salary": 70000},
    2: {"name": "Bob Johnson", "age": 45, "salary": 80000},
    3: {"name": "Charlie Brown", "age": 29, "salary": 60000},
    4: {"name": "Diana Prince", "age": 35, "salary": 90000},
    5: {"name": "Edward King", "age": 50, "salary": 95000},
}

# Printing the dictionary
for emp_id, details in employees.items():
    print(f"Employee ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Salary: ${details['salary']}")

