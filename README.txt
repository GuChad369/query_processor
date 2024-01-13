Relax System Documentation

Instruction:
    To run the system using: python3 main.py
    video: https://youtu.be/65hB8GWHNqA

Overview:
    The "Relax" system is designed to process text-based representations of relations and execute relational algebra queries.

Data Structure:
    Relations are stored using dictionaries.

Entering Relations:
    Format: Relations must be defined in a structured format as shown in the examples below.
    End Marker: Always conclude your relation input with "END" on a new line.
    Example:
        Student = {
            id, name, email, Dept
            1, 'Alex', 'alex@carleton.ca', Sales
            2, 'John', 'john@carleton.ca', Finance
            3, 'Mo', 'mo@carleton.ca', HR
        }
        END

Relational Algebra Query Format:
    Queries must adhere to the following syntax:
        1.Selection:
            select [Age = 18] (Student)
        2.Projection:
            project [name, age] (Student)
        3.Join Operations:
            join [Student.name = Employee.name] (Student, Employee)
            fjoin [Student.name = Employee.name] (Student, Employee)
            rjoin [Student.name = Employee.name] (Student, Employee)
            fjoin [Student.name = Employee.name] (Student, Employee)
        4.Set Operations:
            Union: (Student) + (Employee)
            Intersection: (Student) ^ (Employee)
            Difference: (Student) - (Employee)

Example:
Student = {
    id, name, email, Dept
    1, 'Alex', 'alex@carleton.ca', Sales
    2, 'John', 'john@carleton.ca', Finance
    3, 'Mo', 'mo@carleton.ca', HR
}

Employee = {
    id, name, email, Dept
    1, 'Alex', 'alex@carleton.ca', Sales
    2, 'Max', 'max@carleton.ca', Finance
    3, 'Go', 'go@carleton.ca', HR
}

Department = {
    name, budget
    'Finance', 20000
    'Sales', 30000
    'IT', 40000
}
END

project [Employee.id, Department.name, Department.budget] (select [Employee.id > 1] (fjoin [Employee.Dept = Department.name] (Employee, Department)))

(project [name, email] ((select [id > 2] (Employee)) - (select [id < 2] (Student)))) ^ (project [name, email] ((select [id > 2] (Employee)) + (select [id < 2] (Student))))

