import csv, math

def get_output ():
    dept = {}
    csvfile1 = open("Department.csv","r")
    reader = csv.reader(csvfile1, delimiter=",")
    for row in reader:
        dept_id = row[0]
        dept_name = row[1]
        dept[dept_id] = dept_name

    csvfile1.close()

    emp = {}
    csvfile2 = open("Employee.csv","r")
    reader = csv.reader(csvfile2, delimiter=",")
    for row in reader:
        emp_id = row[0]
        emp_name = row[1]
        dept_id = row[2]
        emp[emp_id] = {"name": emp_name,"department_id": dept_id}
    csvfile2.close()

    sal = {}
    csvfile3 = open("Salaries.csv","r")
    reader = csv.reader(csvfile3, delimiter=",")
    for row in reader:
        emp_id = row[0]
        month = row[1]
        salary = row[2]
        sal[emp_id] = sal.get(emp_id, {})
        sal[emp_id][month] = salary

    answer = []
    answer.append(("Dept_Name","Average_salary"))
    for dept_id, dept_name in dept.items():
        total_salary = 0
        count = 0
        for emp_id, emp_data in emp.items():
            if emp_data["department_id"] == dept_id:
                for month, salary in sal[emp_id].items():
                    total_salary += int(salary)
                    count += 1

        if count!=0:
            average_salary = round((total_salary / count), 2)
            answer.append((dept_name, average_salary))
    return answer

	
output = get_output()
for dept_name, average_salary in output:
    print(dept_name,average_salary)
