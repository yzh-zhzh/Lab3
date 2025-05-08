import employee_info

def test_get_employees_by_age_range():
    assert employee_info.get_employees_by_age_range(20, 30) == [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}, {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert employee_info.get_employees_by_age_range(30, 40) == [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000}, {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]

def test_calculate_average_salary():
    assert employee_info.calculate_average_salary() == 60166.67

def test_get_employees_by_dept():
    assert employee_info.get_employees_by_dept('Sales') == [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    assert employee_info.get_employees_by_dept('Marketing') == [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}, {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert employee_info.get_employees_by_dept('Engineering') == [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000}, {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]