#Program 1
emp_dict = {}
flag = True
while flag == True :
    emp_name =input("Enter employee name: ")
    if emp_name == 'no':
        flag = False
        break
    else:
        emp_salary = input("Enter employee salary: ")
        emp_dict[emp_name] = emp_salary
for emp_name, emp_salary in emp_dict.items():
    print(f"Name: {emp_name}, Salary: {emp_salary}")
